from validate import Validate
import re

class FullName(Validate):

    def validate_input(self, user_input):
        full_name_pattern = "^[A-Z][a-z]{2,} [A-Z][a-z]{2,}$"
        match_object = re.match(full_name_pattern, user_input)
        return False if match_object == None else True