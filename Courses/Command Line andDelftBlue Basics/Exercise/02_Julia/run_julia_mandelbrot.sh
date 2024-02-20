#!/bin/bash 
#
#SBATCH --job-name="julia"
#SBATCH --time=00:10:00
#SBATCH --partition=compute
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --account=education-eemcs-courses-linuxcli
#SBATCH --reservation=delftblueworkshop

module load 2023r1
module load julia 

srun julia mandelbrot.jl
