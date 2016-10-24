#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pytest
from conftest import datapath, expressed
from gaudi.genes.molecule import Molecule
from gaudi.similarity import rmsd, _rmsd_squared


@pytest.mark.parametrize("path1, path2, threshold", [
    ('5dfr_minimized.pdb', '5dfr_minimized.pdb', 0.0),
    ('3pk2_ligand.pdb', '3pk2_ligand_rotated.pdb', 5.911),
])
def test_molecule(individual, individual2, path1, path2, threshold):
    absolute_path1 = os.path.abspath(datapath(path1))
    absolute_path2 = os.path.abspath(datapath(path2))
    individual.genes['Molecule'] = Molecule(parent=individual, path=absolute_path1)
    individual.__ready__()
    individual.__expression_hooks__()
    individual2.genes['Molecule'] = Molecule(parent=individual2, path=absolute_path2)
    individual2.__ready__()
    individual2.__expression_hooks__()

    with expressed(individual, individual2):
        sqrmsd = _rmsd_squared(individual.genes['Molecule']._expressed_coordinates,
                               individual2.genes['Molecule']._expressed_coordinates)
        assert abs(sqrmsd - threshold*threshold) < 0.01
        assert rmsd(individual, individual2, ['Molecule'], threshold)
