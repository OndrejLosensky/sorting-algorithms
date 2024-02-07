import random

def generate_random_lines(num_lines):
    lines = []
    for _ in range(num_lines):
        line = ''.join(str(random.randint(0, 9)) for _ in range(8))
        lines.append(line)
    return lines

num_lines = 2500
random_lines = generate_random_lines(num_lines)

# Print the generated random lines
for line in random_lines:
    print(line)
