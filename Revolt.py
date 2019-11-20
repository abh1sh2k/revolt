import sys
import json


class Revolt:
    def __init__(self):
        pass

    def get_dict(self, input_data, arguments):
        # type: (string, list) -> dict
        outdict = {}
        temp = outdict
        for data in input_data:
            for i, level in enumerate(arguments):
                if i + 1 < len(arguments):
                    if data[level] not in temp:
                        temp[data[level]] = {}
                    temp = temp[data[level]]
                else:
                    temp[data[level]] = self.adjust_non_argument_key(arguments, data)
            temp = outdict
        return outdict

    @staticmethod
    def adjust_non_argument_key(arguments, data):
        not_listed = []
        for key in data:
            if key not in arguments:
                not_listed.append({key: data[key]})

        return not_listed

    @staticmethod
    def read_data():
        input_text = ''
        for line in sys.stdin.readlines():
            input_text += line
        return json.loads(input_text)
