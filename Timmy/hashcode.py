# -*- coding: utf-8 -*-

import math

from pprint import pprint


class Library(object):
    def __init__(self, library_id, signup_time, books, books_per_day, global_book_scores):
        self.library_id = library_id
        self.signup_time = signup_time
        self.books = books
        self.book_amount = len(self.books)
        self.books_per_day = books_per_day

        self.book_scores = {book_id: global_book_scores[book_id] for book_id in self.books}
        self.library_total_score = sum(self.book_scores.values())

    def __repr__(self):
        return 'Library: {} \n ' \
               'Signup Time: {} \n ' \
               'Amount of books: {} \n ' \
               'Books per day: {} \n ' \
               'Books: {} \n ' \
               'Total score of books in library: {} \n' \
               'Time to completion: {}'.format(
            self.library_id, self.signup_time, self.book_amount, self.books_per_day, ', '.join(map(str,self.books)),
            self.library_total_score, self.time_to_completion()
        )

    def time_to_completion(self, start_time=0):
        return start_time + self.signup_time + math.ceil(self.book_amount / self.books_per_day)


def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        total_counts = lines[0]
        amount_of_books, amount_of_libraries, days_for_scanning = map(int, total_counts.split(' '))
        book_scores_line = lines[1]
        book_scores = {}
        for index, value in enumerate(map(int, book_scores_line.split(' '))):
            book_scores[index] = value

        pprint(book_scores)

        return_value = []
        for i in range(amount_of_libraries):
            lib_stats = lines[2 + 2 * i]
            lib_books = lines[2 + 2 * i + 1]
            books_in_library, signup_time, shippings_per_day = map(int, lib_stats.split(' '))
            books = list(map(int, lib_books.split(' ')))
            return_value.append(Library(i, signup_time, books, shippings_per_day, book_scores))
        return return_value


def solve(input_list, out_file_name):
    # do something
    with open(out_file_name, 'w+') as out_file:
        for list in input_list:
            out_file.write(list)


def main():
    input_files = ['a_example.txt']
    for input_file in input_files:
        file, ext = input_file.split('.')
        libraries = get_input(input_file)
        for library in libraries:
            print(library)


if __name__ == "__main__":
    main()