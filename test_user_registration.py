from main_file import MainClass
import pytest

class TestUserRegistration:

    @pytest.mark.parametrize("input_type, input_data, result",[
        ("name", "Get Right", True),
        ("name", "get Right", False),
        ("name", "Get right", False),
        ("name", "GetRight", False),
        ("name", "Ge Right", False),
        ("name", "Get Ri", False)

    ])
    def test_given_first_name_when_valid_returns_true(self, input_type, input_data, result):
        obj = MainClass()
        is_valid = obj.get_input(input_type, input_data)
        assert is_valid == result
