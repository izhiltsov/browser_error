#!/Users/iz/.local/share/virtualenvs/python-NSorJJ5m/bin/python


from selenium import webdriver
import time


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


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def main():

    filename = 'urls.txt'
    urls = read_urls(filename)

    for url in urls:
        if check_console_error(url):
            print(f'Page {url} has console error')


if __name__ == '__main__':
    main()
