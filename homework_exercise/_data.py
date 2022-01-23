import json
import os
from importlib import resources
import io

with resources.open_binary("data_file.json") as f_p:
    data = f_p.read()
DATA_DICT = json.load(io.BytesIO(data))

_DATA2_DICT = None

def delay_data():
    global _DATA2_DICT
    if _DATA2_DICT is not None:
        return _DATA2_DICT

    import toml
    with resources.open_binary("data_file_2.toml") as f_p:
        data = f_p.read()
    _DATA2_DICT = = toml.load(io.BytesIO(data))
    return _DATA2_DICT
