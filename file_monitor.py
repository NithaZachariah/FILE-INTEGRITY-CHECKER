import hashlib
import os
import json

HASH_ALGORITHM = 'sha256'
HASH_FILE = 'hashes.json'

def calculate_file_hash(filepath):
    hasher = hashlib.new(HASH_ALGORITHM)
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

def create_baseline(file_list):
    hashes = {}
    for file in file_list:
        hash_value = calculate_file_hash(file)
        if hash_value:
            hashes[file] = hash_value
        else:
            print(f"⚠️ File not found: {file}")
    with open(HASH_FILE, 'w') as f:
        json.dump(hashes, f, indent=4)
    print(f"✅ Baseline created and saved to {HASH_FILE}")

def check_integrity():
    if not os.path.exists(HASH_FILE):
        print(f"❌ No baseline hash file found: {HASH_FILE}")
        return
    with open(HASH_FILE, 'r') as f:
        old_hashes = json.load(f)

    for file, old_hash in old_hashes.items():
        current_hash = calculate_file_hash(file)
        if not current_hash:
            print(f"⚠️ File missing: {file}")
        elif current_hash != old_hash:
            print(f"❗ File changed: {file}")
        else:
            print(f"✅ File OK: {file}")

if __name__ == '__main__':
    print("1. Create baseline")
    print("2. Check for changes")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        files_to_monitor = input("Enter file paths separated by commas: ").split(',')
        files_to_monitor = [f.strip() for f in files_to_monitor]
        create_baseline(files_to_monitor)

    elif choice == '2':
        check_integrity()

    else:
        print("Invalid choice.")
