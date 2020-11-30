from DNAToolkit import *
import random

# Creating a random DNA sequence for testing:
randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(20)])

print(validateSeq(randDNAStr))
print(countNucFreq(randDNAStr))

DNAStr = validateSeq(randDNAStr)
print(countNucFreq(DNAStr))


