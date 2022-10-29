import re
from validate_email import validate_email
from database import MAX_USERNAME_LENGTH

# printable chars excluding space and delete
ALLOWED_CHARS = r'\x21-\x7e'

MIN_USERNAME_LENGTH = 3
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 32


def check_string(s: str, min_length: int, max_length: int) -> bool:
    if type(s) != str:
        return False

    # returns True if `s` only contains `allowed_chars`,
    # and its length is between `min_length` and `max_length` inclusive
    pattern = fr'[{ALLOWED_CHARS}]{{{min_length},{max_length}}}'
    is_valid = re.fullmatch(pattern, s)
    return bool(is_valid)


def check_username_format(username: str) -> bool:
    return check_string(username, MIN_USERNAME_LENGTH, MAX_USERNAME_LENGTH)


def check_password_format(password: str) -> bool:
    return check_string(password, MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)


def check_email_format(email: str) -> bool:
    # True to check if email actually exists
    # False to just check format
    comprehensive = False
    is_valid = validate_email(
        email_address=email,
        check_blacklist=comprehensive,
        check_dns=comprehensive,
        check_smtp=comprehensive
    )
    return bool(is_valid)

usertypes = {
    0: 'sender',
    1: 'receiver',
    2: 'admin',
}

def check_usertype_format(usertype: int) -> bool:
    if type(usertype) != int:
        return False

    return usertype in usertypes

format_checkers = {
    'username': check_username_format,
    'password': check_password_format,
    'email': check_email_format,
    'usertype': check_usertype_format,
}

if __name__ == '__main__':
    pass
    #print(check_string('test', 1, 10))
