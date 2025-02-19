import hashlib

def sha256_hash_file(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

file_path = "./docs/moon.jpg"
sha256_hash = sha256_hash_file(file_path)
print("SHA256 Hash:", sha256_hash)
