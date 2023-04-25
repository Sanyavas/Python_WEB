from icrawler.builtin import GoogleImageCrawler


def image():
    google_crawler = GoogleImageCrawler(storage={'root_dir': 'your_image_dir'})
    google_crawler.crawl(keyword='Albert Einstein', max_num=1)


if __name__ == '__main__':
    image()
