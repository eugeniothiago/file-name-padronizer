import os
from unidecode import unidecode
from pathlib import Path
import argparse
import re

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


def create_log_structure():
    if not os.path.exists('logs'):
        os.mkdir("logs")
    open("logs/folders_accessed.txt", "w").close()


def add_break_line(path_list: list):
    for item in path_list:
        yield item
        yield "\n"


def write_log(path_list: list) -> None:
    with open("logs/folders_accessed.txt", mode="a") as file:
        file.writelines(add_break_line(path_list))


def access_next_path(path: str) -> None:
    directory_log_list = []
    with open("logs/folders_accessed.txt", mode="a") as file:
        file.write(f"{path}\n")
        file.close()

    if not path.endswith("/"):
        path = path + "/"

    path_list = os.listdir(path)

    for path_item in path_list:
        path_item_name, extension = os.path.splitext(path_item)
        new_path = os.path.join(path, path_item_name) + "/"
        if not extension:
            try:
                directory_log_list.append(new_path)
                access_next_path(new_path)
            except:
                pass
        elif extension == ".ini":
            continue
        else:
            file_padronizer(
                path=path, remove_accent=remove_accent, lower=lower, recursive=recursive
            )
    write_log(path_list=directory_log_list)


def file_padronizer(
    path: str, remove_accent: bool, lower: bool, recursive: bool
) -> None:
    path_list = os.listdir(path)
    for file in path_list:
        name, extension = os.path.splitext(file)
        if name in [".git", ".git/"]:
            continue
        if extension and extension != ".ini":  # in program_formats or text_formats:
            new_name = name.strip()
            new_name = re.sub(pattern=r"\+|-|\(|\)|\.|\_|\__|\s|,|_{2,}|’|'",repl="_",string=new_name)
            new_name = re.sub(pattern=r"_{2,}",repl="_", string=new_name)
            new_name = re.sub(pattern=r"_+$",repl="",string=new_name)
            new_name = re.sub(pattern=r"^_+",repl="", string=new_name)
            if remove_accent:
                new_name = unidecode(unidecode(new_name))
            if lower:
                new_name = new_name.lower()
            elif not lower:
                new_name = new_name.upper()
            new_file = new_name + extension
            os.rename(src=f"{os.path.join(path,file)}", dst=f"{os.path.join(path,new_file)}")
        elif not extension and recursive:
            try:
                new_path = os.path.join(path, name) + "/"
                access_next_path(new_path)
            except:
                continue


if __name__ == "__main__":
    create_log_structure()
    file_padronizer(path, remove_accent, lower, recursive)
