# Create a file analyze-insulin.py 
# Retrieve the protein sequence of human insulin from human preproinsulin
# Obtain the protein sequence of human insulin
# Create a file preproinsulin-seq-clean.txt and copy the results
# Programmatically delete ORIGIN, 1, 61, //, and the spaces and return carriages
# Confirm that your file has 110 characters of lowercase letters
# Create a file lsinsulin-seq-clean.txt save amino acids 1–24. Verify that the file has 24 characters
# Create a file binsulin-seq-clean.txt, save amino acids 25–54. Verify that the file has 30 characters
# Create a file cinsulin-seq-clean.txt, save amino acids 55–89. Verify that the file has 35 characters
# Create a file ainsulin-seq-clean.txt, save amino acids 90–110. Verify that your file has 21 characters

def cleanMyInsulin(txt, unwanted_characters):
    for unwanted_characters in unwanted_characters:
        txt = txt.replace(unwanted_characters, "")
    return txt

with open('preproinsulin-seq.txt', 'r') as uncleanFile:
     unclean_txt = uncleanFile.read()

unwanted_characters = ["ORIGIN", "61", "1", "//", " ", "\n"]

pure_insulin = (cleanMyInsulin(unclean_txt, unwanted_characters))
pure_insulin_count = len(pure_insulin)

with open('preproinsulin-seq-clean.txt', 'w') as cleanFile:
    cleanFile.write(pure_insulin)
    print(f"Insulin Successfully Processed : length {pure_insulin_count}")

with open('lsinsulin-seq-clean.txt', 'w') as cleanFile2:
    cleanFile2.write(pure_insulin[0:24])
    print(f"Isinsulin Successfully Processed: {len(pure_insulin[0:24])}")

with open('binsulin-seq-clean.txt', 'w') as cleanFile3:
    cleanFile3.write(pure_insulin[24:54])
    print(f"binsulin Successfully Processed: {len(pure_insulin[24:54])}")

with open('cinsulin-seq-clean.txt', 'w') as cleanFile4:
    cleanFile4.write(pure_insulin[54:89])
    print(f"cinsulin Successfully Processed: {len(pure_insulin[54:89])}")
  
with open('ainsulin-seq-clean.txt', 'w') as cleanFile5:
    cleanFile5.write(pure_insulin[89:110])
    print(f"ainsulin Successfully Processed: {len(pure_insulin[89:110])}")

#
