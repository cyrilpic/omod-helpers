import json
import os
import re
from pathlib import Path

import pandas as pd


def extract_design(folder_path, design_id):
    """Extract the design data of `design_id` from optimization results
    downloaded from OMOD in folder `folder_path` and generate an input yaml
    for OMOD integrated model."""

    path = Path(folder_path)

    if not path.is_dir():
        raise Exception("Path to result folder is not a directory")

    folder_name = path.name
    matches = re.match(r"ev-(\d+)", folder_name)
    if not matches:
        raise Exception("Could not extract evaluation id from folder name")
    ev_id = int(matches[1])
    json_fname = f"{path.name}.json"

    with open(path / json_fname) as f:
        ev_data = json.load(f)

    if ev_data['model_name'] != "optimization":
        raise Exception("Results are not optimization results")

    op = ev_data['input']['op']
    settings = ev_data['input']['settings']
    topology = ev_data['input']['topology']

    results = None
    for res in ev_data['results']:
        if res['name'] == 'raw_pop':
            results = pd.DataFrame(res['data'])
            results.index = results.index.astype('int')
            results.sort_index(inplace=True)

    if results is None:
        raise Exception("Results are empty")

    actuator = results.iloc[design_id, :].to_dict()

    for key in list(actuator.keys()):
        if key.startswith('c') or key.startswith('z'):
            del actuator[key]

    output = {
        'op': op,
        'settings': settings,
        'topology': topology,
        'actuator': actuator
    }

    with open(path / f"actuator-{ev_id}-{design_id}.json", "w") as f:
        json.dump(output, f, indent=2)
