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
    def test_given_full_name_when_valid_or_invalid_returns_result(self, input_type, input_data, result):
        obj = MainClass()
        is_valid = obj.get_input(input_type, input_data)
        assert is_valid == result


    @pytest.mark.parametrize("input_type, input_data, result",[
        ("email", "abc@yahoo.com",True),
                ("email", "abc-100@yahoo.com",True),
                ("email", "abc.100@yahoo.com",True),
                ("email", "abc111@abc.com",True),
                ("email", "abc-100@abc.net",True),
                ("email", "abc.100@abc.com.au",True),
                ("email", "abc@1.com",True),
                ( "email", "abc@gmail.com.com",True),
                ("email", "abc+100@gmail.com",True),
                ("email", "abc",False),
                ("email", "abc@.com.my",False),
                ("email", "abc123@gmail.a",False),
                ("email", "abc123@.com",False),
                ("email", "abc123@.com.com",False),
                ("email", ".abc@abc.com",False),
                ("email", "abc()*@gmail.com",False),
                ("email", "abc@%*.com",False),
                ("email", "abc..2002@gmail.com",False),
                ("email", "abc.@gmail.com",False),
                ("email", "abc@abc@gmail.com",False),
                ("email", "abc@gmail.com.1a",False),
                ("email", "abc@gmail.com.aa.au",False)
    ])
    def test_given_email_when_valid_or_invalid_returns_result(self, input_type, input_data, result):
        obj = MainClass()
        is_valid = obj.get_input(input_type, input_data)
        assert is_valid == result


    