import requests

class YaUploader:
    #  Авторизация

    def __init__(self, token, folder_name):
        self.OAuth = token
        self.folder_name = folder_name
        self.APT_BASE_URL = 'https://cloud-api.yandex.net/'
        self.headers = {'Authorization': self.OAuth}
        self.params = {'path': self.folder_name}

    def create_folder(self):

        #self.folder_name = folder_name


        try:
            req1 = requests.put(self.APT_BASE_URL + 'v1/disk/resources/', params=self.params, headers=self.headers)
            if req1.status_code == 201:
                return f'Папка {self.folder_name} успешно создана'
            elif req1.status_code == 409:
                return 'Папка с таким именем уже существует'
            else:
                return 'Убедитесь в правильности токена Yandex. {error}'
        except Exception as error:
            return 'Убедитесь в правильности токена Yandex. {error}'


def outh():

    with open('files/config.txt', 'r', encoding='UTF-8') as f:
        token = f.readline()
        return token


def main():
    token = outh()
    uploader_y = YaUploader(token, 'Test_folder')
    print(uploader_y.create_folder())


if __name__ == '__main__':
    main()

    ___________