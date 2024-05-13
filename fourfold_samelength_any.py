import os, sys
from itertools import combinations

def is_header(line):
    return line.startswith('>')

# Read the file and skip the first line
with open(sys.argv[1], 'r') as file:
    lines = file.readlines()[0:]

headers = []
sequences = []
current_sequence = ''

# Collect sequences and their corresponding headers
for line in lines:
    if is_header(line):
        if current_sequence:
            sequences.append(current_sequence)
            current_sequence = ''
        headers.append(line.strip())
    else:
        current_sequence += line.strip()

if current_sequence:
    sequences.append(current_sequence)

# Function to count differences and matching patterns
def count_differences_with_patterns(s1, s2):
    matching_patterns_counter = 0
    differences_counter = 0
    patterns = ["CT", "GT", "TC", "CC", "AC", "GC", "CG", "GG"]
    min_length = min(len(s1), len(s2))

    for i in range(0, min_length - 2, 3):
        segment1, segment2 = s1[i:i+2], s2[i:i+2]
        if segment1 in patterns and segment2 in patterns:
            matching_patterns_counter += 1
            if s1[i+2] != s2[i+2]:
                differences_counter += 1

    return matching_patterns_counter, differences_counter

# Calculate and print results for each pair of sequences
for (i, j) in combinations(range(len(sequences)), 2):
    matching_patterns, differences = count_differences_with_patterns(sequences[i], sequences[j])
    print(f"{sys.argv[1]}{chr(9)}{headers[i]}{chr(9)}{headers[j]}{chr(9)}{matching_patterns}{chr(9)}{differences}")


