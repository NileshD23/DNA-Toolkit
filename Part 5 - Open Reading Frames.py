from DNAToolkit import *
from utilities import colored # use terminal for colored bases
import random

# Creating a random DNA sequence for testing:
randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(20)])

print(validateSeq(randDNAStr))
print(countNucFreq(randDNAStr))

DNAStr = validateSeq(randDNAStr)
print(countNucFreq(DNAStr))

print(f'\nSequence: {DNAStr}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFreq(DNAStr)}\n')

print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')

print(f"[4] + DNA String + Reverse Complement:\n5' {DNAStr} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]")
print(f"5' {reverse_complement(DNAStr)} 3' [Rev. Complement]\n")

print(f'[5] + GC Content: {gc_content(DNAStr)}%\n')
print(f'[6] + GC Content in Subsection k = 5: {gc_content_subsec(DNAStr, k = 5)}\n')

print(f'[7] + Amino Acid Sequence from DNA: {translate_seq(DNAStr, 0)}\n')

print(f'[8] + Codon Frequency (L): {codon_usage(DNAStr, "L")}\n')

print(f'[9] + Reading frames:')
for frame in gen_reading_frames(DNAStr):
    print(frame)