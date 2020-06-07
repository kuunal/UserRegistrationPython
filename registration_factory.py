from full_name import FullName

class RegistrationFactory:

    def return_object(self, input_type):
        switcher = {
            "name" : FullName()
        }
        return switcher.get(input_type)
 