import requests


def do_requests():
    resp = requests.get('https://example.com')
    print('example.com =>', resp.status_code)


def main():
    for _ in range(0, 10):
        do_requests()


if __name__ == '__main__':
    main()
