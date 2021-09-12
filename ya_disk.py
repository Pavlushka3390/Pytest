import requests

class YandexDisk:

    def __init__(self, token):
        self.token = token
        self.headers_Ya = {'Accept': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_link(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.status_code


    def upload_folder(self, name):
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources?path=%2F' + name, headers=self.headers_Ya)
        if response.status_code == 201:
            return f'создана папка с именем {name}, статус кода - {response.status_code}'
        elif response.status_code == 409:
            return f'папка {name} уже существует, статус кода - {response.status_code}'


if __name__ == '__main__':
    ya = YandexDisk(token="")
    print(ya.get_link())
    print(ya.upload_folder('folder1'))
