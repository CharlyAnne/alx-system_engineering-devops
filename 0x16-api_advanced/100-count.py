#!/usr/bin/python3
"""Script prints a sorted count of given keywords"""
import json
import requests


def count_words(subreddit, word_list):
  """Functiom counts all words
