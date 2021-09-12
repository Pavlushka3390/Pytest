import pytest
from ya_disk import YandexDisk
ya = YandexDisk(token="")

class Test_ya_disk:

    def test_get_link(self):
        assert ya.get_link() == 200

    @pytest.mark.parametrize('name, expected_result', [
        ['folder6', 'создана папка с именем folder6, статус кода - 201'],
        ['folder6', 'папка folder6 уже существует, статус кода - 409']
    ])
    def test_upload_file_to_disk(self, name, expected_result):
        assert ya.upload_folder(name) == expected_result