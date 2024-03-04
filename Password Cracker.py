import hashlib

def crack_password(hash_value, dictionary_file):
    with open(dictionary_file, 'r') as f:
        for word in f:
            word = word.strip()
            hashed_word = hashlib.sha256(word.encode()).hexdigest()
            if hashed_word == hash_value:
                return f"Password cracked: {word}"
    return "Password not found in dictionary"

if __name__ == "__main__":
    # Example hash value (replace with your target hash)
    target_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

    # Example dictionary file (replace with your dictionary file path)
    dictionary_file = "rockyou.txt"

    result = crack_password(target_hash, dictionary_file)
    print(result)
