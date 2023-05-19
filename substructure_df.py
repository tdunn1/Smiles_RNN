# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:55:58 2023

@author: Tim
"""

import requests
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors
from collections import defaultdict
import pandas as pd
import pdb

header = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug'
search_in = 'compound/substructure/smiles/C1CCCCC1' 
search_out = 'txt?MaxRecords=30000&list_return=listkey'
comp_re = '/'.join([header,search_in,search_out])

req = requests.get(comp_re)
pdb.set_trace()
final_re = req.text
list_key = final_re.split(':')[-1]
mol_dict = defaultdict(list)

# for smi in smi_list:
#     mol = Chem.MolFromSmiles(smi)
#     if mol is None: continue

#     mol_dict['Smiles'].append(smi)
#     mol_dict['Formula'].append(rdMolDescriptors.CalcMolFormula(mol))
#     mol_dict['Weight'].append(rdMolDescriptors.CalcExactMolWt(mol))
#     mol_dict['Csp3'].append(rdMolDescriptors.CalcFractionCSP3(mol))
#     mol_dict['Amide Bonds'].append(rdMolDescriptors.CalcNumAmideBonds(mol))
#     mol_dict['Aromatic Carbocycles'].append(rdMolDescriptors.CalcNumAromaticCarbocycles(mol))
#     mol_dict['Aromatic Heterocycles'].append(rdMolDescriptors.CalcNumAromaticHeterocycles(mol))

# df = pd.DataFrame(mol_dict)

# df.to_csv('ring_substruct.csv')

        
        

