#! /usr/bin/env python3

"""
A script for randomly selecting a restaurant from aotourism.com.
"""

import os
import sys
import random
import argparse
import requests
from bs4 import BeautifulSoup

def get_best_bites():
    """
    Returns a list of restaurants recommended as "best bites" on aotourism.com.

    The function takes no arguments.

    Returns
    -------
    list
        Restaurants highlighted on aotourism.com.
    """
    url = "https://www.aotourism.com/dining/best-bites/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    main_content = soup.find(
        'div',
        {'class': 'content', 'id': 'main-content'},
    )
    restaurants = []
    for slide_title in main_content.find_all('h2', {'class': 'slide-title'}):
        restaurant_name = slide_title.find('span', {'class': 'slide-title-text'})
        restaurants.append(restaurant_name.text)
    return restaurants

def pick_random_element(elements, random_num_generator = None):
    """
    Picks a random element from any type of iterable object.

    Parameters
    ----------
    elements : iterable 
        The iterable object to randomly select an element from.
        This could be a list, tuple, generator, etc.

    random_generator : random.Random, optional
        A random number generator.

    Returns
    -------
    object
        The selected item (could be any type).
    """
    if not random_num_generator:
        random_num_generator = random
    return random_num_generator.choice(elements)

def arg_is_positive_int(i):
    """
    Validating argument `i` a positive integer.
    Returns int if `i` is valid, or raises
    argparse.ArgumentTypeError.

    Parameters
    ----------
    i : str
        The argument string.

    Returns
    -------
    int
        Positive integer.

    Raises
    ------
    argparse.ArgumentTypeError
        If `i` cannot be converted into an int that is greater than zero.
    """
    try:
        if int(i) < 1:
            raise
    except:
        msg = '{0!r} is not a positive integer'.format(i)
        raise argparse.ArgumentTypeError(msg)
    return int(i)

def main_cli():
    """
    The main command-line interface for this script.

    The function takes no arguments and returns None.
    """
    # Create a command-line arg parser
    parser = argparse.ArgumentParser()

    # Add seed argument to our parser
    parser.add_argument(
        '-s', '--seed',
        action = 'store',
        # Using a function for the argument type
        type = arg_is_positive_int,
        help = ('Seed for random number generator.'),
    )

    # Use our arg parser to parse the command-line args
    args = parser.parse_args()

    # Create a pseudo-random number generator
    random_num_generator = random.Random()

    seed = args.seed
    if not seed:
        seed = random.randint(1, 999999999)
    print("Seeding the random number generator with", seed)
    random_num_generator.seed(seed)

    restaurants = get_best_bites()
    chosen_restaurant = pick_random_element(restaurants, random_num_generator)

    print(f"Tonight, you're dining at {chosen_restaurant}! Enjoy!")

if __name__ == '__main__':
    main_cli()
