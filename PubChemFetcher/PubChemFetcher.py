import pubchempy as pcp
import pandas as pd
#This script searches for molecular weight, molecular formula, H-bond donors, H-bond acceptors,
# XlogP values and SMILES string for a list of compounds and outputs them to a csv file
# User needs to enter the compound list of interest.

# Search for multiple compound
compound_list = ['caffeine','aspirin','nicotine']
data = []

for compound_name in compound_list:
    compounds = pcp.get_compounds(compound_name,'name')

    if compounds:
        compound = compounds[0]
        data.append({
            "Compound name": compound_name,
            "Molecular weight (g/mol)":compound.molecular_weight,
            "Connectivity SMILES": compound.connectivity_smiles,
            "Number of H-bonds donors": compound.h_bond_donor_count,
            "Number of H - bonds acceptors": compound.h_bond_acceptor_count,
            "XlogP values": compound.xlogp,
        })

        print(f"Name: {compound_name}")
        print(f"Molecular Formula: {compound.molecular_formula}")
        print(f"Molecular Weight: {compound.molecular_weight}")
        print(f"Connectivity SMILES: {compound.connectivity_smiles}")
        print(f"Number of H-bonds donors: {compound.h_bond_donor_count}")
        print(f"Number of H-bonds acceptors: {compound.h_bond_acceptor_count}")
        print(f"XlogP values: {compound.xlogp}")
    else:
        data.append({
            "Compound name": compound_name,
            "Molecular weight (g/mol)": None,
            "Connectivity SMILES": None,
            "Number of H-bonds donors": None,
            "Number of H - bonds acceptors": None,
            "XlogP values": None,
        })
        print(f"{compound_name} not found in PubChem.")

#Create DataFrame and csv output file
df = pd.DataFrame(data)
output_file = 'molecule_properties.csv'
df.to_csv(output_file, index = False)
print(f"\n Saved {len(df)} records to {output_file}")
print(df)