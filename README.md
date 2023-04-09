# File name padronizer
A **really** simple script to padronize file name substituting spaces and other characters with underlines.

## How does it work?
The script has 3 arguments:
- `path`(`str`): The path to the folder where you want do padronize the file's names
- `remove_accent`(`bool`): If you want to remove special characters such as "~,^,´, etc from letters. Default value is **`True`**
- `lower`(`bool`): Change the file to lowercase. Default value is **`True`**
- `recursive`(`bool`): The script will also process files in subfolders in the path provided. Default value is **`False`**.

## Requirements:
- [Python](https://www.python.org/downloads/)
- [Unidecode](https://pypi.org/project/Unidecode/). Execute `python -m pip install unidecode` to install it in your current environment

## Running the script

Example file: **foo Bar BAZ - 2002/05+01.pdf"**

`python file_padronizer.py --path path/to/the/files --remove_accents True --lower True --recursive True` returns **"foo_bar_baz_2002_05_01.pdf"**

`python file_padronizer.py --path path/to/the/files --remove_accents False --lower False --recursive True` returns **"FOO_BAR_BAZ_2002_05_01.pdf"**


**obs**: Please be aware that if you pass a path with multiple subfolders and the `recursive`parameter setted to `True` the script may take some time to process all the files.