import os
from unidecode import unidecode
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path", type=str, required=True)
parser.add_argument("--remove_accent", type=bool, required=False, default=True)
parser.add_argument("--lower", type=bool, required=False, default=True)
parser.add_argument("--recursive", type=bool, required=False, default=False)
args = parser.parse_args()

path = args.path
remove_accent = args.remove_accent
lower = args.lower
recursive = args.recursive


def access_next_path(path: str) -> None:
    if not path.endswith("/"):
        path = path + "/"
    for path_item in os.listdir(path):
        path_item_name, extension = os.path.splitext(path_item)
        new_path = os.path.join(path, path_item_name) + "/"
        if not extension:
            try:
                print(new_path)
                access_next_path(f"{new_path}")
                # return new_path
            except:
                pass
        elif extension == ".ini":
            continue
        else:
            file_padronizer(path, remove_accent, lower, recursive)


def file_padronizer(
    path: str, remove_accent: bool, lower: bool, recursive: bool
) -> None:
    for file in os.listdir(path):
        name, extension = os.path.splitext(file)
        if extension and extension != ".ini":  # in program_formats or text_formats:
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
            elif not lower:
                new_name = new_name.upper()
            if new_name.startswith("_"):
                new_name = new_name[1:]
            new_file = new_name + extension
            os.rename(src=f"{path}{file}", dst=f"{path}{new_file}")
        elif not extension and recursive:
            try:
                new_path = os.path.join(path, name) + "/"
                access_next_path(f"{new_path}")
            except:
                continue


if __name__ == "__main__":
    file_padronizer(path, remove_accent, lower, recursive)
