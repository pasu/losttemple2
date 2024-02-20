#!/bin/bash
#
#SBATCH --job-name="gen_mol"
#SBATCH --time=00:10:00
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1GB
#SBATCH --account=education-eemcs-courses-linuxcli
#SBATCH --reservation=delftblueworkshop

# Run Python script:
module load 2023r1
module load python
module load py-numpy
module load py-scipy
module load py-matplotlib

srun python gen_mol_folders.py