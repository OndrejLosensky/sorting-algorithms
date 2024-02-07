import random
import string

def generate_random_id(length=10):
    return ''.join(random.choices(string.digits, k=length))

def generate_ids_file(n, file_name):
    with open(file_name, 'w') as f:
        for _ in range(n):
            f.write(generate_random_id() + '\n')


n = 10000  # Number of IDs to generate
file_name = "input.txt" 
generate_ids_file(n, file_name)
print(f"{n} random IDs generated and saved to '{file_name}'.")
