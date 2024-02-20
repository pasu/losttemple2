#!/bin/bash

# Install ASE:
module load 2023r1
module load python
module load py-pip
module load py-numpy
module load py-scipy
module load py-matplotlib

python -m pip install --user ase
