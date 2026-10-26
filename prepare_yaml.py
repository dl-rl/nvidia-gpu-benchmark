# Copyright (c) 2024, DL-RL Inc.
# All rights reserved.

import yaml
import os
cwd = os.getcwd()

input_filename = "data/coco128.yaml"
output_filename = "data/custom.yaml"

with open(input_filename, "r") as fobj:
  data = yaml.safe_load(fobj)

data["path"] = f"{cwd}/datasets/coco128"

with open(output_filename, "w") as fobj:
  yaml.dump(data, fobj)