import re


PATTERNS = ["person=[a-z]*\\srelation=[a-z]*", "mother=[a-z]*\\sson=[a-z]*",
            "husband=[a-z]*\\swife=[a-z]*", "wife=[a-z]*\\shusband=[a-z]*"]

def parse(args):
    """
    Parse the arguments from the command line with regex.

    Args:
        args (str): Arguments from command line..

    Returns:
        dict: A dictionary that conatins the parsed arguments from
              the CLI.
    """

    parsed_args = []

    for p in PATTERNS:
        match = re.match(p, args.lower())
        if match:
            r = match.group(0)
            arg1, arg2 = r.split(" ")
            return {arg1.split("=")[0]: arg1.split("=")[1],
                    arg2.split("=")[0]: arg2.split("=")[1]}
