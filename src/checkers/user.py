import re
from validate_email import validate_email

# printable chars excluding space and delete
allowed_chars = r'\x21-\x7e'

min_username_length = 3
max_username_length = 32
min_password_length = 8
max_password_length = 32

def check_string(str: str, min_length: int, max_length: int) -> bool:
    is_valid = re.fullmatch(
        fr'''^{allowed_chars}$'''
        '''{{{min_length}-{max_length}}}''',
        str
    )
    return bool(is_valid)

def check_username(username: str) -> bool:
    return check_string(username, min_username_length, max_username_length)

def check_password(password: str) -> bool:
    return check_string(password, min_password_length, max_password_length)

def check_email(email: str) -> bool:
    is_valid = validate_email(
        email_address=email,
    )
    return bool(is_valid)
