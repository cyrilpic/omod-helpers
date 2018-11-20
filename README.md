# OMOD extractor

In this repo, there are a few scripts to you help you work with OMOD.

## readJSON.m

`readJSON.m` is a MATLAB function to load a json file given its path.

```matlab
data = readJSON('path/to/my/file.json')
```

## extract_design.py

`extract_design.py` is a python script to extract a given design from optimization 
results and prepare a JSON file that can be used as input to the integrated model
on OMOD.

In order to use it, you need `python >= 3.5` with `pandas`.

```python
from extract_design import extract_design

# extract actuator 10 (starting from 0) from ev-XX
extract_design('/path/to/ev-XX', 10)

# The resulting file is located at /path/to/ev-XX/actuator-XX-10.json
```
