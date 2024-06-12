import os, sys
from itertools import combinations

#make sure the input file is in fasta format with headers starting with >
def is_header(line):
    return line.startswith('>')

# Read the file; replace lines = file.readlines()[0:] with lines = file.readlines()[1:] if there is a sequence length as your header
with open(sys.argv[1], 'r') as file:
    lines = file.readlines()[0:]

headers = []
sequences = []
current_sequence = ''

# Collect sequences and their corresponding populations
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

# Function to find positions where patterns match across all sequences
def find_matching_positions(sequences):
    patterns = ["CT", "GT", "TC", "CC", "AC", "GC", "CG", "GG"]
    min_length = min(len(s) for s in sequences)
    matching_positions = []

    for i in range(0, min_length - 2, 3):
        segments = [s[i:i+2] for s in sequences]
        if all(segment in patterns for segment in segments):
            matching_positions.append(i)

    return matching_positions

# Function to count pairwise differences at matching positions
def count_pairwise_differences(sequences, matching_positions):
    pairwise_results = []
    for (i, j) in combinations(range(len(sequences)), 2):
        differences_counter = 0
        for pos in matching_positions:
            if sequences[i][pos+2] != sequences[j][pos+2]:
                differences_counter += 1
        pairwise_results.append((i, j, differences_counter))
    return pairwise_results

# Find matching positions
matching_positions = find_matching_positions(sequences)

# Count pairwise differences at matching positions
pairwise_differences = count_pairwise_differences(sequences, matching_positions)

# Print results
for i, j, differences in pairwise_differences:
    print(f"{sys.argv[1]}{chr(9)}{headers[i]}{chr(9)}{headers[j]}{chr(9)}{len(matching_positions)}{chr(9)}{differences}")



