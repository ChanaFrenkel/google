import json
import re

from search import get_best_k_completions
from init_data_structure import offline

size_of_string = 6
size_of_res = 5


def print_result(json_lines, auto_list):
    for index, i in enumerate(auto_list):
        line = json_lines[str(i.file_id)][str(i.offset)]
        index_comp = line.find(i.completed_sentence)
        print(

            f'{index + 1}. \033[31m{i.score}'
            f'\t\033[35m\033[1m{line[:index_comp]}'
            f'\x1b[3;95m\033[4m{i.completed_sentence}\033[0m'
            f'\033[35m\033[1m{line[index_comp + len(i.completed_sentence):len(line) - 1]}\033[0m    '
            f',\033[37m( file:\033[94m\033[4m{i.source_text}\033[0m\033[37m ) '
            f',(arg:{i.offset})\033[0m')


def run(json_data, json_lines):
    print("Hi user!")
    while 1:
        input_user = input("\nPlease enter the string you want us to search for you or enter exit\n")
        if input_user == "exit":
            print("GoodBye:)")
            break
        print_result(json_lines,
                     get_best_k_completions(json_data, json_lines,
                                            re.sub(r"[^a-z0-9]+", ' ', input_user.lower()[:size_of_string]))[
                     :size_of_res])
        while 1:
            input_user += input(input_user)
            if input_user[-1] == '#':
                break
            print_result(json_lines,
                         get_best_k_completions(json_data, json_lines,
                                                re.sub(r"[^a-z0-9]+", ' ', input_user.lower()[:size_of_string]))[
                         :size_of_res])


def read_from_file():
    file_data = open("data.json")
    json_data = json.load(file_data)
    file_data.close()
    file_data = open("line.json")
    json_lines = json.load(file_data)
    file_data.close()
    return json_data, json_lines


def online():
    file = read_from_file()
    run(file[0], file[1])


if __name__ == '__main__':
    print("loading...")
    offline()
    online()
