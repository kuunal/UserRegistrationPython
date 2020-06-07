from validate_full_name import FullName
from validate_email import Email
from validate_phone_no import PhoneNumber

class RegistrationFactory:

    def return_object(self, input_type):
        switcher = {
            "name" : FullName(),
            "email": Email(),
            "phone": PhoneNumber()
        }
        return switcher.get(input_type)
 