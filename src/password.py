from argon2 import PasswordHasher


hasher = PasswordHasher()

def hash(password: str) -> str:
    """
    Returns the hash of `password`
    """
    return hasher.hash(password)


def verify(password:str, hash:str) -> bool:
    """
    Returns true if the hash of `password` is `hash
    """
    return bool(hasher.verify(hash, password))