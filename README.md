# Installation

Install python 3.7: https://wsvincent.com/install-python3-mac/

Normally I would recommend using pyenv and virtualenv: https://github.com/pyenv/pyenv

But since it's probably too complicated, just do:
`pip3 install --user requirements.txt`

# Running

From the root:
`python3 export_data.py {FOLDER_PATH} {JSON_FILEPATH}`

`python3 export_data.py -- wh {FOLDER_PATH} {JSON_FILEPATH}`

with `--wh` option, it will only export width and height data.

(`python3 export_data.py --help` if you forget which arg goes first)

