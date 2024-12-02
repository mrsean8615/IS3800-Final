import re

def regex_email(value):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, value) is not None

# Contains at least one lowercase letter.
# Contains at least one uppercase letter.
# Contains at least one digit.
# Contains at least one special character from @$!%*?&#.
# Is at least 8 characters long.
def regex_password(value):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$'
    return re.match(pattern, value) is not None