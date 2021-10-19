import json
import os
import sys
from .argument_parser import parse
from .tree import Tree

DATA = {
    "alex": {
        "brothers": [
            "john",
            "joe"
        ],
        "father": "evan",
        "grandaughters": [
            "sophia"
        ],
        "grandsons": [
            "bern"
        ],
        "mother": "diana",
        "sisters": [
            "nisha"
        ],
        "sons": [
            "jacob",
            "shaun"
        ],
        "wife": "nancy"
    },
    "bern": {
        "father": "jacob",
        "grandfather": "alex",
        "grandmother": "nancy",
        "mother": "rufi",
        "uncles": [
            "shaun"
        ],
    },
    "george": {
        "wife": "sophia"
    },
    "jacob": {
        "aunts": [
            "nisha"
        ],
        "brothers": [
            "shaun"
        ],
        "daughters": [
            "sophia"
        ],
        "father": "alex",
        "grandfather": "evan",
        "grandmother": "diana",
        "mother": "nancy",
        "sons": [
            "bern"
        ],
        "uncles": [
            "joe",
            "john"
        ],
        "wife": "rufi"
    },
    "nancy": {
        "grandaughters": [
            "sophia"
        ],
        "grandsons": [
            "bern"
        ],
        "husband": "alex",
        "sons": [
            "jacob",
            "shaun"
        ]
    },
    "piers": {
        "cousins": [
            "jacob",
            "shaun",
            "ruth",
            "william"
        ],
        "daughters": "sarah",
        "father": "joe",
        "mother": "niki",
        "sisters": [
            "sally"
        ],
        "wife": "pippa"
    },
    "rufi": {
        "daughters": [
            "sophia"
        ],
        "husband": "jacob",
        "sons": [
            "bern"
        ]
    },
    "sophia": {
        "brothers": [
            "bern"
        ],
        "father": "jacob",
        "grandfather": "alex",
        "grandmother": "nancy",
        "husband": "george",
        "mother": "rufi"
    }
}


def main():
    """Parse the input, load the family tree and run
        the appropriate command.

    Returns:
        str: The message from the command that was run.
    """
    print('running')
    try:
        args = sys.argv[1:]

        if len(args) != 2:
            raise ValueError(
                "Incorrect input. Please see the README.rst"
                "for input instructions.")

        parsed_arguments = parse(" ".join(args))

        if not parsed_arguments:
            raise ValueError(
                "Could not parse input please check"
                "supported input formats.")

        tree = Tree(DATA)

        return run_command(tree, parsed_arguments)

    except ValueError as e:
        return(e)
    except Exception as e:
        return e.message


def run_command(tree, args):
    """Run a command based on the parsed inputs.

    Args:
        tree (str):The data to perform an action with.
        args (str): The arguments parsed from the CLI.

    Returns:
        str: The message from the command that was run.
    """

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
    """Write the family tree to a JSON file.

    Args:
        data (str): The family tree JSON.
    """

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)

if __name__ == '__main__':
    main()
