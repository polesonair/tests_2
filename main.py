import unittest

import create_f
from create_f import YaUploader

token = create_f.outh()
uploader = YaUploader(token, 'MyFolder')


class TestAPI(unittest.TestCase):
    def test_create_folder(self):
        self.assertEqual(uploader.create_folder(), "Папка MyFolder успешно создана")

    def test_create_folder_exist(self):
        self.assertEqual(uploader.create_folder(), "Папка с таким именем уже существует")


if __name__ == '__main__':
    unittest.main()