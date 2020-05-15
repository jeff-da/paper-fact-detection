# store a {id : sentence_list}
import json
from collections import defaultdict

split = "test"
store = defaultdict(set)
doc_ids_for_split = set()

with open(f'data/claims_{split}.jsonl') as file:
    for line in file:
        data = json.loads(line.rstrip())
        for doc_id in data["evidence"]:
            doc_id = int(doc_id)
            label_list = data["evidence"][str(doc_id)]
            for label in label_list:
                for sentence_id in label["sentences"]:
                    sentence_id = int(sentence_id)
                    store[doc_id].add(sentence_id)
            doc_ids_for_split.add(doc_id)

outfile = open(f'{split}.txt.tmp', 'w')
print(doc_ids_for_split)
with open('data/corpus.jsonl') as file:
    for line in file:
        data = json.loads(line.rstrip())
        doc_id = data["doc_id"]
        if doc_id not in doc_ids_for_split:
            continue
        for index, abstract_sentence in enumerate(data["abstract"]):
            for word in abstract_sentence.split():
                label = 'O' if index in store[doc_id] else 'B-LOC'
                outfile.write(word + " " + label + '\n')
        outfile.write("\n")
