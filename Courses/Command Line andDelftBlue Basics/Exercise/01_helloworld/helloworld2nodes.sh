#!/bin/bash
#
#SBATCH --job-name="hello"
#SBATCH --time=00:10:00
#SBATCH --partition=compute
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --account=education-eemcs-courses-linuxcli
#SBATCH --reservation=delftblueworkshop

echo "Hello, World!" >> helloworld.txt
echo "The following nodes are reporting for duty:" >> helloworld.txt
srun hostname >> helloworld.txt
echo "Have a great day!" >> helloworld.txt
