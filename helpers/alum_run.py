import chimera
import glob, sys
pdbs = glob.glob(sys.argv[1]+"*.pdb")

for pdb in pdbs:
	mol = chimera.openModels.open(pdb)
	chimera.runCommand('del element.H')
	chimera.runCommand('runscript /home/jr/x/gaudi/alum.py')
	chimera.openModels.close(mol)