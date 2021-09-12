import pytest
from shelves import get_doc_owner_name, add_new_doc, delete_doc, documents, directories

class Test_shelves:

    @pytest.mark.parametrize('a, expected_result', [
        ['10006', 'Аристарх Павлов'],
        ['1525', None],
        [' ', None]
    ])
    def test_get_doc_owner_name(self, a, expected_result):
        assert get_doc_owner_name(a) == expected_result

    @pytest.mark.parametrize('a, b, c, d, expected_result', [
        ['12', 'passport', 'james', '2', '2'],
        ['12', 'passport', 'james', '4', '4'],
        ['12', 'passport', 'james', ' ', ' ']
    ])
    def test_add_new_doc(self, a, b, c, d, expected_result):
        assert add_new_doc(a, b, c, d) == expected_result

    @pytest.mark.parametrize('a, expected_result', [
        ['11-2', 'документ 11-2 успешно удален'],
        ['15', 'номер не найден'],
        [' ', 'номер не найден']
    ])
    def test_delete_doc(self, a, expected_result):
        assert delete_doc(a) == expected_result
