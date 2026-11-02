import hashlib

def calculate_hash(path):
    with open(path,"rb") as file:
        content= file.read()
        hash_file = hashlib.sha256(content).hexdigest()
        return  hash_file

path= input("Type the file path: ")
try:
    original_hash=calculate_hash(path)

    print("Original Hash:", original_hash)
    input("Press ENTER after modify the file...")
    new_hash= calculate_hash
    if(original_hash==new_hash):
        print("The file was not altered")
    else:
        print("WARNING: file altered!")
except FileNotFoundError:
    print("Error: the file was not found!")

