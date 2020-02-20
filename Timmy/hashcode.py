# -*- coding: utf-8 -*-


def get_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()


def solve(input_list, out_file_name):
    # do something
    with open(out_file_name, 'w+') as out_file:
        for list in input_list:
            out_file.write(list)


def main():
    input_files = ['test_file1.txt']
    for input_file in input_files:
        file, ext = input_file.split('.')
        input_list = get_input(input_file)
        solve(input_list, file + '_out.' + ext)


if __name__ == "__main__":
    main()