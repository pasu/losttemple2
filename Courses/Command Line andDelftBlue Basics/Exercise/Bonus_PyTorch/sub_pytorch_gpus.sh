#!/bin/bash
#
#SBATCH --job-name="PyTorch"
#SBATCH --time=00:10:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --gpus-per-task=1
#SBATCH --partition=gpu
#SBATCH --mem=4G
#SBATCH --account=Education-EEMCS-Courses-LinuxCLI

module load 2023r1
module load openmpi
module load py-torch

srun python test_pytorch_gpus.py
