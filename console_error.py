

from selenium import webdriver


def read_urls(filename):
    """Returns a list of the urls from the given txt file"""
    with open(filename, 'r') as f:
        list_of_urls = [line for line in f]
    return list_of_urls


def check_console_error(url):
    """Return browser's console errors"""

    console_errors = []
    driver = webdriver.Chrome()
    log = driver.get_log('browser')
    for entry in log:
        if entry['level'] == 'SEVERE':
            console_errors.append(entry['message'])


def main():

    filename = 'urls.txt'
    urls = read_urls(filename)

    for url in urls:
        if check_console_error(url):
            print(f'Page {url} has console error')


if __name__ == '__main__':
    main()
