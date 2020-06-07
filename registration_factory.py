from validate_full_name import FullName
from validate_email import Email

class RegistrationFactory:

    def return_object(self, input_type):
        switcher = {
            "name" : FullName(),
            "email": Email()
        }
        return switcher.get(input_type)
 