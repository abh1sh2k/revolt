import json
import sys

from Revolt import Revolt

if __name__ == "__main__":
    revolt = Revolt()
    arguments = sys.argv[1:]
    input_data = revolt.read_data()
    out_dict = revolt.get_dict(input_data, arguments)  # type: List
    print(json.dumps(out_dict))
