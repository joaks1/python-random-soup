# Learning goals

The script `hungry.py` demonstrates how to
1. Scrape web data using the requests and BeautifulSoup packages.
2. Use pseudo-random number generators in Python.


# Contents

-   [Getting set up](#getting-set-up)
-   [Creating-the-conda-environment](#creating-the-conda-environment)
-   [Touring the `hungry.py` script](#touring-the-hungrypy-script)
    -   [Web scraping](#web-scraping)
    -   [Pseudo-random number generators](#pseudo-random-number-generators)
-   [Try out the script!](#try-out-the-script)
-   [License](#license)

# Getting set up

I recommend you fork this repository so that you can tinker with the
`hungry.py` script to help learn how it works.

1.  Login to your [Github](https://github.com/) account.

2.  Fork [this repository](https://github.com/joaks1/python-random-soup), by
    clicking the 'Fork' button on the upper right of the page.

    After a few seconds, you should be looking at *your* 
    copy of the repo in your own Github account.

3.  Click the 'Clone or download' button, and copy the URL of the repo via the
    'copy to clipboard' button.

4.  In your terminal, navigate to where you want to keep this repo (you can
    always move it later, so just your home directory is fine). Then type:

        git clone the-url-you-just-copied

    and hit enter to clone the repository. Make sure you are cloning **your**
    fork of this repo.

5.  Next, `cd` into the directory:

        cd python-random-soup


# Creating the conda environment

The `hungry.py` script requires 2 Python packages: requests and beautifulsoup4.
The `environment.yml` file defines a conda environment with these required packages.
To create this conda environment, use this command:

    conda env create --name soup --file environment.py

Once conda finishes, use this command to activate the new "soup" environment:

    conda activate soup


# Touring the `hungry.py` script

## Web scraping

There are several Python packages to help get data from webpages.
in the `hungry.py` script, the `get_best_bytes` function demonstrates how
to use the `requests` and `bs4` (BeautifulSoup4) packages to create a list
of all the restaurants highlighted as "best bites" by the
Auburn-Opelika tourism website:

```python
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
```

[Go here for the aotoursim.com best-bites page](https://www.aotourism.com/dining/best-bites/)
from which we will "scrape" the list of restaurants.
In the `get_best_bites` function,
we use the  `requests` module to get the HTML data from this page.
Then, we create an instance of a `BeautifulSoup` object that parses the HTML
data and makes it easier for us to find what we need.
We use the `find` method of the `BeautifulSoup` object to grab just the HTML
content of the "main" part of the page.
From that, we use the `find_all` method to find the title element of all the
"slides" on the page; these hold the names of the restaurants on the page.

## Pseudo-random number generators

Nothing is truly random with computers; it's all 0s and 1s!
Pseudorandom number generators (PRNG) are algorithms that provide sequences of numbers
that appear random, but are in fact 100% deterministic.
These algorithms allow us to do random-like things that are 100% repeatable if
we know the starting state ("seed") of the PRNG algorithm.

In the `main_cli` function, we create an instance of a random number generator
object on this line:

```python
random_num_generator = random.Random()
```

If a seed was provided on the command line, we use it to set the starting seed
of the `random_num_generator` object.
Otherwise, we just use Pythons global PRNG to pseudo-randomly pick an integer
between 1 and 999999999 as the seed for our `random_num_generator` object:

```python
    seed = random.randint(1, 999999999)
```

We then pass our `random_num_generator` to the `pick_random_element` function.
This function uses the `choice` method fo the `random_num_generator` to
randomly choose one of the restaurants.

# Try out the script!

Try running the `hungry.py` script multiple times.
You should get a (pseudo) random restaurant each time.
Here's an example from my terminal:

    $ python3 hungry.py
    Seeding the random number generator with 614736347
    Tonight, you're dining at The Waverly Local! Enjoy!
    $ python3 hungry.py
    Seeding the random number generator with 403309895
    Tonight, you're dining at Byron's Smokehouse! Enjoy!
    $ python3 hungry.py
    Seeding the random number generator with 433157817
    Tonight, you're dining at Pannie-George's Kitchen! Enjoy!

Now, copy the random number seed from your last output (386382552, in my
example above).
If you specify this seed when running `hungry.py`, you will get
the same results every time.
For example:

    $ python3 hungry.py
    Seeding the random number generator with 433157817
    Tonight, you're dining at Pannie-George's Kitchen! Enjoy!
    $ python3 hungry.py
    Seeding the random number generator with 433157817
    Tonight, you're dining at Pannie-George's Kitchen! Enjoy!

This could NOT happen if the random number generator was ***truly*** random.


# License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US">Creative Commons Attribution 4.0 International License</a>.
