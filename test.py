import urllib.request





if __name__ == '__main__':
    response = urllib.request.urlopen('https://www.python.org')
    print(response.read().decode('utf-8'))
