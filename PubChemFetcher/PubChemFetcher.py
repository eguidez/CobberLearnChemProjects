import pubchempy as pcp
#This script searches for molecular weight, molecular formula and SMILES string for a compound.
# User needs to replace compound_name with the compound of interest.

# Search PubChem for theobromine
compound_name = 'cobberite'

# Search for multiple compound
compound_list = ['caffeine','aspirin','nicotine']
for compound_name in compound_list:
    compounds = pcp.get_compounds(compound_name,'name')

    if compounds:
        compound = compounds[0]

        print(f"Name: {compound_name}")
        print(f"Molecular Formula: {compound.molecular_formula}")
        print(f"Molecular Weight: {compound.molecular_weight}")
        print(f"Connectivity SMILES: {compound.connectivity_smiles}")
        print(f"Number of H-bonds donors: {compound.h_bond_donor_count}")
        print(f"Number of H-bonds acceptors: {compound.h_bond_acceptor_count}")
        print(f"XlogP values: {compound.xlogp}")
    else:
        print(f"{compound_name} not found in PubChem.")