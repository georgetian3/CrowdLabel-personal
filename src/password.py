from argon2 import PasswordHasher


hasher = PasswordHasher()

def hash(password: str) -> str:
    """
    Returns the hash of `password`,
    and empty string if hashing failed
    """

    try:
        return hasher.hash(password)
    except:
        return ''


def verify(password:str, hash:str) -> bool:
    """
    Returns true if the hash of `password` is `hash
    Returns false if password and hash don't match, or exception was raised
    """
    try:
        return bool(hasher.verify(hash, password))
    except:
        return False