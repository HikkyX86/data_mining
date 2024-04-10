import random

def generate_random_list(start_char, end_char, min_length, max_length, num_lines):
    with open('data_rnp.txt', 'w') as file:
        for _ in range(num_lines):
            num_groups = random.randint(2, 6)
            line = []
            for _ in range(num_groups):
                group_length = random.randint(min_length, max_length)
                group = [random.choice([chr(i) for i in range(ord(start_char), ord(end_char) + 1)]) for _ in range(group_length)]
                unique_sorted_group = sorted(set(group))
                line.append(f"[{''.join(unique_sorted_group)}]")
            file.write(''.join(line) + '\n')

start_char = 'a'
end_char = 'f' 
min_length = 1
max_length = 6
num_lines = 100

generate_random_list(start_char, end_char, min_length, max_length, num_lines)
