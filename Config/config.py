import os


def get_chromedriver_path():
    stream = os.popen('which chromedriver')
    return stream.read().strip()
