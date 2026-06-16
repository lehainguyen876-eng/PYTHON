import random
import string

def generate_assignment_code():
    pool = string.ascii_uppercase + string.digits
    random_chars = "".join(random.choices(pool, k=4))
    return f"PY-{random_chars}"