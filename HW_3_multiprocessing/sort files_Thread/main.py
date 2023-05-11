"""
Сортування файлів в теці # багатопотоковість # parser Terminal
"""

import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

"""
--source [-s] files-sor
--output [-o]
"""

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="sorted_мотлох")

args = vars(parser.parse_args())

source = Path(args.get("source"))
output = Path(args.get("output"))

folders = []

file_extension = {"audio": ['.mp3', '.ogg', '.wav', '.amr'],
                  "images": ['.jpeg', '.png', '.jpg', '.svg'],
                  "documents": ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
                  "archives": ['.zip', '.gz', '.tar'],
                  "video": ['.avi', '.mp4', '.mov', '.mkv'],
                  "py_files": ['.py'],
                  }


def grabs_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)


def path_to_folder(ext):
    folder_name = "different"
    for key, val in file_extension.items():
        if ext in val:
            folder_name = key
    return folder_name


def copy_file(path: Path) -> None:

    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[:]
            folder_name = path_to_folder(ext)
            new_path = output / folder_name / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el, new_path / el.name)
            except OSError as error:
                logging.error(error)


def main():
    logging.basicConfig(level=logging.ERROR, format="%(threadName)s %(message)s")
    print(f'{source} -> {output}')
    folders.append(source)
    grabs_folder(source)
    print(folders)
    threads = []
    for folder in folders:
        th = Thread(target=copy_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]

    print(f"\nВидаліть стару теку...")


if __name__ == "__main__":
    main()
