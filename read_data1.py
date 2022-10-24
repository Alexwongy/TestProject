import json


def build_add_data():
    with open('add_data.json') as f:
        data = json.load(f)
    return data


def build_add_data_1():
    with open('add_data_1.json') as f:
        data_list = json.load(f)

        new_list = []
        for data in data_list:
            new_list.append(tuple(data.values()))

        return new_list


if __name__ == '__main__':
    print(build_add_data_1())