""" finding all mails in a file result.txt """

import email
from turtle import pu
from numpy import empty
import re
import itertools
import codecs

fhand = open("C:\\Users\hp\\Desktop\\combined files\\result.txt",
             "r", encoding='utf-8')


def pullout():
    all_mails = []
    for line in fhand:
        if line == empty:
            continue
        elif line != empty:
            line = line.strip()
            lst = re.findall('[0-9a-zA-Z-.]+@\w+\.\w+', line)

        if lst:
            for emails in itertools.chain(lst):
                all_mails.append(emails)
    return all_mails


print("Emails fetched...")
