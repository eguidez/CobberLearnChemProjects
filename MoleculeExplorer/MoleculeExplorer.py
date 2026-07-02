import pubchempy as pcp
import pandas as pd
from rdkit import Chem, DataStructs
from rdkit.Chem import Descriptors, Lipinski, AllChem
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# This code calculates molecular properties from File strings.
# Notes:
# Step 1 : Have students generate a code using AI that reads SMILES string and outputs molecular properties
# Step 2: Combine PubChem Fetcher code to generate SMILES string from molecule name and then output properties with RDKit
# Step 3 : Output properties in a Table like what was done with PubChem Fetcher
# Step 4: Generate similarity matrix
# step 5: Plot similarity matrix

# Input SMILES string
#smiles = "CCO"   # Ethanol
#smiles = "CC(=O)O"   # Acetic acid
#smiles = "CC(C)Cc1ccc(cc1)[C@@H](C)C(=O)O" # ibuprofen

#  # Search for multiple compound
compound_list = ['caffeine','aspirin','nicotine']
data = []

# Generate SMILES string from molecule name
for compound_name in compound_list:
    compounds = pcp.get_compounds(compound_name,'name')
    if compounds:
        compound = compounds[0]
        smiles = compound.connectivity_smiles
        # Create RDKit molecule
        mol = Chem.MolFromSmiles(smiles)
        #Molecular weight
        mw = Descriptors.MolWt(mol)
        # Hydrogen bond donors
        hbd = Lipinski.NumHDonors(mol)
        # TPSA
        tpsa = Descriptors.TPSA(mol)
        # Num of rotatable bonds
        rot_bonds = Lipinski.NumRotatableBonds(mol)
        # Num of aromatic rings
        ar_rings = Lipinski.NumAromaticRings(mol)
        data.append({
            "SMILES": smiles,
            "Compound name": compound_name,
            "Molecular weight (g/mol)": mw,
            "TPSA": tpsa,
            "Number of H-bonds donors": hbd,
            "Number of rotatable bonds": rot_bonds,
            "Number of aromatic rings": ar_rings,
        })
        print("Molecule successfully created!")
        print("Molecular Weight:", mw, "g/mol")
        print("Number of hydrogen bond donors:", hbd)
        print("TPSA", tpsa, "A^2")
        print("Number of rotatable bonds:", rot_bonds)
        print("Number of aromatic rings:", ar_rings)
        print("Number of atoms:", mol.GetNumAtoms())
        print("Canonical SMILES:", Chem.MolToSmiles(mol))
# Check that the molecule was successfully created
    else:
            print("Invalid SMILES string.")
            data.append({
                "Compound name": compound_name,
                "Molecular weight (g/mol)": None,
                "Connectivity SMILES": None,
                "Number of H-bonds donors": None,
                "Number of H - bonds acceptors": None,
                "XlogP values": None,
            })
            print(f"{compound_name} not found in PubChem.")
# Create DataFrame and csv output file
df = pd.DataFrame(data)
output_file = 'molecule_properties_rdkit.csv'
df.to_csv(output_file, index=False)
print(f"\n Saved {len(df)} records to {output_file}")
print(df)

#Build molecular weight similarity matrix
#1. Get molecular weights and names from dataframe
mw = df["Molecular weight (g/mol)"].values
names = df["Compound name"].values

#2. Create similarity matrix
n = len(mw)
sim_matrix = np.zeros((n, n))
# Bandwidth (data spread)
sigma = np.std(mw)

for i in range(n):
    for j in range(n):
        diff = mw[i] - mw[j]
# Formula for similarity score: Sij = exp(-(MWi-MWj)^2/(2sigma^2))
        sim_matrix[i, j] = np.exp(-(diff ** 2) / (2 * sigma ** 2))

# 5. Convert to DataFrame
sim_df = pd.DataFrame(
    sim_matrix,
    index=names,
    columns=names)

#5. Visualization
sns.heatmap(sim_df, cmap="viridis")
plt.title("Molecular Weight Similarity (Tanimoto)")
plt.show()

#Save to csv
sim_df.to_csv("similarity_matrix.csv")