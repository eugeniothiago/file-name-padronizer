# File name padronizer
A **really** simple script to padronize file name substituting spaces and other characters with underlines.

## How does it work?
The script has 3 arguments:
- `path`(`str`): The path to the folder where you want do padronize the file's names
- `remove_accent`(`bool`): If you want to remove special characters such as "~,^,´, etc) from letters. Default value is **`True`**
- `lower`(`bool`): Change the file to lowercase. Default value is **`True`**

## Requirements:
- [Python](https://www.python.org/downloads/)
- [Unidecode](https://pypi.org/project/Unidecode/). Execute `python -m pip install unidecode` to install it in your current environment

## Running the script

Example file: **"a incrível carreira de tião do arroz - 2002+05+01.pdf"**

`python script.py --path path/to/the/files --remove_accents True --lower True` returns **"a_incrivel_carreira_de_tiao_do_arroz_2002_05_01.pdf"**

`python script.py --path path/to/the/files --remove_accents False --lower False` returns **"A_INCRÍVEL_CARREIRA_DE_TIÃO_DO_ARROZ_2002_05_01.pdf"**