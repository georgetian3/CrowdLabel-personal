import re
from validate_email import validate_email

# printable chars excluding space and delete
allowed_chars = r'\x21-\x7e'

min_username_length = 3
max_username_length = 32
min_password_length = 8
max_password_length = 32


def check_string(str: str, min_length: int, max_length: int) -> bool:
    pattern = fr'[{allowed_chars}]{{{min_length},{max_length}}}'
    is_valid = re.fullmatch(pattern, str)
    return bool(is_valid)


def check_username(username: str) -> bool:
    return check_string(username, min_username_length, max_username_length)


def check_password(password: str) -> bool:
    return check_string(password, min_password_length, max_password_length)


def check_email(email: str) -> bool:
    is_valid = validate_email(
        email=email,
    )
    return bool(is_valid)


if __name__ == '__main__':
    pass
    #print(check_string('test', 1, 10))
