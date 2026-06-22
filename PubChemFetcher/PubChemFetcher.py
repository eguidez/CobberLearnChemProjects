import pubchempy as pcp
#This script searches for molecular weight, molecular formula and SMILES string for a compound.
# User needs to replace compound_name with the compound of interest.

# Search PubChem for theobromine
compound_name = 'theobromine'
compounds = pcp.get_compounds(compound_name,'name')

if compounds:
    compound = compounds[0]

    print(f"Name: {compound_name}")
    print(f"Molecular Formula: {compound.molecular_formula}")
    print(f"Molecular Weight: {compound.molecular_weight}")
    print(f"Connectivity SMILES: {compound.connectivity_smiles}")
else:
    print("Theobromine not found in PubChem.")