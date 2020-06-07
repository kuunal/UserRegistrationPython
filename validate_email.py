from validate import Validate
import re

class Email(Validate):

    def validate_input(self, user_input):
        full_name_pattern = "^[a-zA-Z0-9]+[\\.\\-\\+\\_]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[.]?[a-zA-Z]{2,4}[\\.]?([a-z]{2,4})?$"
        match_object = re.match(full_name_pattern, user_input)
        return False if match_object == None else True