# store a {id : sentence_list}
import json
from collections import defaultdict

split = "test"
store = defaultdict(set)
doc_ids_for_split = set()

outfile = open(f'test.txt.tmp', 'w')
with open('data.txt') as file:
    for line in file:
        line = line.rstrip()
        for word in line.split():
            label = 'B-LOC'
            outfile.write(word + " " + label + '\n')
    outfile.write("\n")
