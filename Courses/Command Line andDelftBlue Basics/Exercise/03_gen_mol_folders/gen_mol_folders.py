#!/usr/bin/env python3

####  Prerequisites: install ase package  #######
#                                               #
#  python3 -m pip install --upgrade --user ase  #
#                                               #
#       https://wiki.fysik.dtu.dk/ase           #
#                                               #
#################################################

# Import modules:
import os
import sys
import subprocess
import ase
from ase.io import read,write
from ase.build import molecule
from ase.optimize import BFGS
from ase.calculators.emt import EMT


def main():
    # Print info:
    info = """
    This script does the following:
    1. Creates a parent directory "molecules".
    2. Reads an array of molecules and does the following steps for each molecule:
        3. Creates a sub-directory for current molecule.
        4. Generates .xyz file containing Cartesian coordinates of current molecule.
        5. Decides if to write or to append the .log file.
        6. Optimizes the initial geometry of current molecule with EMT and ...
        6. ... writes optimization .log and ASE trajectory files for current molecule.
    """
    print(info)

    # Step 1: Create parent folder if it does not already exist:
    parent_dir = "molecules"
    if os.path.exists(parent_dir): # check if folder exists 
        print("Parent directory", parent_dir, "already exists.","\n")
    else: 
        os.mkdir(parent_dir) # create folder
        print("Parent directory", parent_dir, "is created.","\n")

    # Step 2: Create array of molecules:
    molecules = ['H2', 'CO', 'CO2', 'C6H6', 'butadiene', 'H2O', 'CH4', 'H2O2', 'NO2', 'C3H9C', 'isobutene', 'H2CCHCN', 'trans-butane', 'C3H4_D2d', 'C3H6_D3h', 'C3H8'] 

    print("Your molecules are:", molecules,"\n") # Printing molecules array

    # Steps 3-6: Looping through the array of molecules:
    for x in molecules:

        # Set output to terminal:
        sys.stdout = sys.__stdout__

        # Step 3: Create sub-folder if it does not already exist:
        path = os.path.join(parent_dir, x) 
        if os.path.exists(path): # check if folder exists 
            print("Directory", x, "already exists.")
        else: 
            os.mkdir(path) # create folder
            print("Directory", x, "is created.")
        os.chdir(path) 
        
        # Step 4: Create .xyz coordinates file:
        atoms = molecule(x) 
        filename = x+'.xyz'
        if os.path.exists(filename): # check if file exists
            print("File", filename, "already exists. Skipping this step.")
        else: 
            write(filename, atoms) # create file
            print("File", filename, "is created.")
        
        print("Optimizing", x)
        
        # Step 5: Set output to log file, decide if to write or to append:
        outname = x+'.log'
        if os.path.exists(outname): # if file exists, then check if writable and append
        
            if os.access(outname, os.W_OK): # check if writable
                print("Log file already exists. Appending...","\n")

                # Check how many times the optimization has already been done:
                optcounter = 1
                with open(outname) as f:
                    for line in f:
                        optcounter += line.count("optimization")

                sys.stdout = open(outname, 'a')
                print("Geometry optimization #", optcounter, " with EMT calculator:")
                
            else: # if file exists but is not writable
                print("Log file already exists, but is not writable.")
                print("Skipping appending. Check permissions!")
                print("Output will be written to a new file instead.","\n")
                regularoutname = x+'.log'
                outname = x + '_new' + '.log'
                sys.stdout = open(outname, 'w')
                print("#############")
                print("Regular", regularoutname, "file already exists, but is not writable. Check permissions!")
                print("This is a back-up", outname, "file, which will be re-written if the problem persists.")
                print("This optimization will not be counted towards the total number of optimizations.")
                print("#############","\n")
                print("Extra geometry optimization with EMT calculator:")
                
        else: # if file does not exist, then write
            print("Creating new log file. Writing...","\n")
            sys.stdout = open(outname, 'w')
            print("Geometry optimization # 1 with EMT calculator:")

        # Step 6: Optimize geometry with EMT calculator:
        atoms.set_calculator(EMT()) 
        trajname = x+'.traj'
        dyn = BFGS(atoms, trajectory=trajname)
        dyn.run(fmax=0.05)
        
        # Close log file:
        sys.stdout.close()
        
        # Go back to where we started:
        os.chdir('../..') 

    sys.stdout = sys.__stdout__ # set output back to terminal
    print("All done for", len(molecules), "molecules!")


if __name__ == "__main__":
    main()
