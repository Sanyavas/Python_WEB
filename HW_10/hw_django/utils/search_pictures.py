from icrawler.builtin import GoogleImageCrawler


def image():
    google_crawler = GoogleImageCrawler(storage={'root_dir': 'your_image_dir'})
    file_urls = []
    google_crawler.crawl(keyword='J.K. Rowling', max_num=1)
    file_urls.append(google_crawler.downloader.image)
    print(file_urls)


if __name__ == '__main__':
    image()

