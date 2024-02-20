# Usage:

chmod +x install_ase.sh
./install_ase.sh
sbatch sub_to_queue.sh

# What it does:

This script does the following:
    1. Creates a parent directory "molecules".
    2. Reads an array of molecules and does the following steps for each molecule:
        3. Creates a sub-directory for current molecule.
        4. Generates .xyz file containing Cartesian coordinates of current molecule.
        5. Decides if to write or to append the .log file.
        6. Optimizes the initial geometry of current molecule with EMT and ...
        6. ... writes optimization .log and ASE trajectory files for current molecule.
