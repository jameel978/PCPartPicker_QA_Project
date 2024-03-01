import random
import string
import json

def generate_random_username():
    letters = ''.join(random.choices(string.ascii_letters, k=6))
    numbers = ''.join(random.choices(string.digits, k=6))
    return letters + numbers

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def check_if_list_is_in_order(lst,order):
    if order == "descending":
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                return False
        return True
    elif order == "increasing":
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True
    else:
        return False


def read_json(location):
    with open(location) as f:
        data = json.load(f)
    return data
def get_test_variables(location):
    return read_json(location)["test_variables"][0]

def get_browser_config(location):
    return read_json(location)["browser_config"]


def get_test_config(location):
    return read_json(location)["test_config"][0]
