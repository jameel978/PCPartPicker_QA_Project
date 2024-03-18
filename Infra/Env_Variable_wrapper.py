import json
import sys
import argparse
import os.path


def create_tokens_file(dictionary, filename='tokens.json'):
    with open(filename, 'w') as file:
        json.dump(dictionary, file)


def main():
    my_tokens = {
        "JIRA_EMAIL": os.environ['JIRA_EMAIL'],
        "JIRA_TOKEN": os.environ['JIRA_TOKEN'],
        "JIRA_URL": os.environ['JIRA_URL'],
        "PROJECT_KEY": os.environ['PROJECT_KEY'],
    }

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    config = os.path.join(cur_dir, "tokens.json")
    create_tokens_file(my_tokens, config)


if __name__ == "__main__":
    main()
    print(os.environ['JIRA_URL'])
