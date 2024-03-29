import random
import string
import json
import inspect
import types
import re


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

def get_all_tests(my_class):
    methodList = [v for n, v in inspect.getmembers(my_class, inspect.ismethod) if isinstance(v, types.MethodType)]
    test_list = [test for test in methodList if "test_" in test.__name__ and "runner" not in test.__name__]
    return test_list

def get_all_tests(my_class):
    methodList = [v for n, v in inspect.getmembers(my_class, inspect.ismethod) if isinstance(v, types.MethodType)]
    test_list = [test.__name__ for test in methodList if "test_" in test.__name__]
    return test_list

def prepair_all_tests(test_classes):
    lst = []
    for test_class in test_classes:
        for i in get_all_tests(test_class()):
            lst.append((test_class,i))
    return lst

def read_json(location):
    with open(location) as f:
        data = json.load(f)
    return data


def extract_idf_from_link(link):
    id = link.split("/")[5]
    return id

def is_sorted_descending(nums):
    return all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))

def is_sorted_ascending(nums):
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))

def is_in_range(lst, lower_bound=None, upper_bound=None):
    if lower_bound is not None and upper_bound is not None:
        for num in lst:
            if not lower_bound <= num <= upper_bound:
                return False
    elif lower_bound is not None:
        for num in lst:
            if num < lower_bound:
                return False
    elif upper_bound is not None:
        for num in lst:
            if num > upper_bound:
                return False
    return True

