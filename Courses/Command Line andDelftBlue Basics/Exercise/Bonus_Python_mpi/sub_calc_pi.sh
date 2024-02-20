#!/bin/bash
#
#SBATCH --job-name="Py_pi"
#SBATCH --time=00:10:00
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --partition=compute
#SBATCH --mem-per-cpu=1G
#SBATCH --account=Education-EEMCS-Courses-LinuxCLI
#SBATCH --reservation=DelftBlueWorkshop

module load 2023r1
module load openmpi
module load python
module load py-numpy
module load py-mpi4py

srun python calculate_pi.py
