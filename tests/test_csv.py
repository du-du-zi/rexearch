import os
from re import I
import sys
import csv
import unit_rule

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # This is just for test env
import rexearch  # noqa : E402

rx = rexearch.Rexearch()
rx.load_json_file("tests/unit.number.rule.json")
# rx.load_json_file("tests/jay.test.rules.json")
sample_input = open("tests/titles.csv", mode="r",encoding='utf-8')

rx.custom_functions["find_unit_number"] = unit_rule.find_unit_number
# rx.custom_functions["html_entity_decoder"] = unit_rule.html_entity_decoder

rdr = csv.reader(sample_input)

with open("output_.csv",'w',encoding='utf-8') as f:
    writer_object =  csv.writer(f)

    for i, line in enumerate(rdr):
        results = rx.search(str(line))
        extract_ = []
        repr_ = []
        for result in results:
            extract_.append("\'" + result['raw'] + "\'")
            repr_.append("\'" + result['repr'] + "\'")
        if extract_:
            line.append("||||".join(extract_))
            line.append("||||".join(repr_))
        else:
            line.append(None)
            line.append(None)
        writer_object.writerow(line)
    f.close()
sample_input.close()


# results = rx.search(sample_input)
# for result in results:
#     print(result)
