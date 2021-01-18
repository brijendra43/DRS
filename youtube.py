import os
def youtubedow():
    url = input("enter url: ")
    os.system(f'youtube-dl {url}')