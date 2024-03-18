import json
import sys
import argparse
import os.path

def load_existing_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            existing_data = json.load(file)
        return existing_data
    else:
        return {}

def save_to_json(variables, filename):
    with open(filename, 'w') as file:
        json.dump(variables, file, indent=4)
    print(f"Variables saved to '{filename}'.")

def main():
    parser = argparse.ArgumentParser(description="Save variables to a JSON file")
    parser.add_argument("filename", help="JSON file name to save variables")
    args = parser.parse_args()

    existing_data = load_existing_data(args.filename)

    variables = existing_data
    for arg in sys.argv[2:]:  # Start from index 2 to skip the script name and filename
        key, value = arg.split('=')
        variables[key] = value

    save_to_json(variables, args.filename)

if __name__ == "__main__":
    main()
