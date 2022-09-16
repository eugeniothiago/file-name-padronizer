import os
from unidecode import unidecode
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path", type=str, required=True)
parser.add_argument("--remove_accent", type=bool, required=False, default=True)
parser.add_argument("--lower", type=bool, required=False, default=True)
args = parser.parse_args()

path = args.path
remove_accent = args.remove_accent
lower = args.lower


def main():
    for file in os.listdir(path):
        name, extension = os.path.splitext(file)
        if extension:  # in program_formats or text_formats:
            new_name = (
                name.strip()
                .replace(" ", "_")
                .replace("(", "")
                .replace(")", "")
                .replace("__", "")
                .replace("___", "")
                .replace("____", "")
                .replace("-", "_")
                .replace("+", "-")
            )
            if remove_accent:
                new_name = unidecode(new_name)
            if lower:
                new_name = new_name.lower()
            elif lower:
                new_name = new_name.upper()
            if new_name.startswith("_"):
                new_name = new_name[1:]
            new_file = new_name + extension
            os.rename(src=f"{path}{file}", dst=f"{path}{new_file}")
