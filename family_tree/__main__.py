import json
import os
import sys
from .argument_parser import parse
from .tree import Tree

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tree.json")

def main():

    try:
        args = sys.argv[1:]

        if len(args) == 2:

            parsed_arguments = parse(" ".join(args))

            if not parsed_arguments:
                raise ValueError("Could not parse input please check supported input formats")

            data = {}

            with open(DATA_FILE, "r") as f:
                data = json.load(f)

            tree = Tree(data)

            return run_command(tree, parsed_arguments)
    except ValueError as e:
        return(e)
    except Exception as e:
        return e.message

def run_command(tree, args):

    if "person" in args.keys():
        return tree.get_relationships(args["person"], args["relation"])

    if "husband" in args.keys():
        message = tree.add_spouse(args["husband"], args["wife"])
        save_tree(tree.data)
        return message

    if "mother" in args.keys():
        message = tree.add_child(args["son"], args["mother"], "sons")
        save_tree(tree.data)
        return message

def save_tree(data):

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    main()
