# -*- coding: utf-8 -*-

import math
import os
from time import time
from collections import OrderedDict

from pprint import pprint


def sort_by_second_value(original_dict):
    ordered_dict = OrderedDict()
    tuples = [(key, value) for key, value in original_dict.items()]
    sorted_tuples = sorted(tuples, key=lambda tuple: tuple[1])
    for tuple in sorted_tuples:
        ordered_dict[tuple[0]] = tuple[1]
    return ordered_dict


class Library(object):
    def __init__(self, library_id, signup_time, books, books_per_day, global_book_scores):
        self.library_id = library_id
        self.signup_time = signup_time

        # Sort books by score. We want the highest-scoring books to be first
        self.books = list(reversed(sorted(books, key=lambda book: global_book_scores[book])))
        self.book_amount = len(self.books)
        self.books_per_day = books_per_day
        self.global_book_scores = global_book_scores

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

    def score_for_x_days(self, x_days):
        return sum([self.book_scores[book_id] for book_id in self.books[0:x_days * self.books_per_day]])

    def books_for_days_left(self, days_left):
        possible_books = self.books_per_day * days_left
        return self.books[:possible_books]


def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        total_counts = lines[0]
        amount_of_books, amount_of_libraries, days_for_scanning = map(int, total_counts.split(' '))
        book_scores_line = lines[1]
        book_scores = {}
        for index, value in enumerate(map(int, book_scores_line.split(' '))):
            book_scores[index] = value

        book_scores = sort_by_second_value(book_scores)

        libraries = []
        for i in range(amount_of_libraries):
            lib_stats = lines[2 + 2 * i]
            lib_books = lines[2 + 2 * i + 1]
            books_in_library, signup_time, shippings_per_day = map(int, lib_stats.split(' '))
            books = list(map(int, lib_books.split(' ')))
            libraries.append(Library(i, signup_time, books, shippings_per_day, book_scores))

        # print('Book scores: ')
        # pprint(book_scores)
        # print('\n\n')
        return libraries, days_for_scanning


def solve(libraries, days_for_scanning, out_file_name):
    # do something

    days_left = days_for_scanning

    active_libraries = []
    while True:
        # Sort libraries by highest score for days_left - signup time
        libraries = sorted(libraries, key=lambda library: library.score_for_x_days(days_left - library.signup_time))
        chosen_library = libraries[0]
        days_left -= chosen_library.signup_time

        # Books that we can scan from this library given we have days_left left
        books_for_chosen_library = chosen_library.books_for_days_left(days_left)
        active_libraries.append((chosen_library.library_id, len(books_for_chosen_library), books_for_chosen_library))

        libraries = libraries[1:]

        if days_left <= 0 or len(libraries) == 0:
            break

    # for tup in active_libraries:
    #     print(tup)

    with open(out_file_name, 'w+') as out_file:
        out_file.write('{}\n'.format(len(active_libraries)))
        for tup in active_libraries:
            if (tup[1] > 0):
                out_file.write('{} {}\n'.format(tup[0], tup[1]))
                out_file.write('{}\n'.format(' '.join(list(map(str, tup[2])))))


def main():
    input_files = ['a_example.txt',
                   'b_read_on.txt',
                   'c_incunabula.txt',
                   'd_tough_choices.txt',
                   'e_also_big.in',
                   'e_so_many_books.txt',
                   'f_libraries_of_the_world.txt']
    for input_file in input_files:
        start_time = time()
        file, ext = input_file.split('.')
        libraries, days_for_scanning = get_input(input_file)
        solve(libraries, days_for_scanning, file + '_out.' + ext)
        print('Done with file ', input_file, ' in time ', (time()-start_time))


if __name__ == "__main__":
    main()