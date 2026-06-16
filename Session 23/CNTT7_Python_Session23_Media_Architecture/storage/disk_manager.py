import math

def calculate_disk_blocks(size_bytes, block_size=4096):
    # Dùng math.ceil để làm tròn lên vì dù dư 1 byte cũng tốn 1 block
    return math.ceil(size_bytes / block_size)