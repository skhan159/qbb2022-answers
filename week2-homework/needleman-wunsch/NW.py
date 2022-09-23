import numpy as np
import sys
from fasta import readFASTA
import pandas as pd

input_sequences = readFASTA(open(sys.argv[1]))

seq1_id, x = input_sequences[0]
seq2_id, y = input_sequences[1]
print('Script name:', sys.argv[0])

df = pd.read_table(sys.argv[2], delim_whitespace=True, index_col=0) #i think pandas are fluffy nice animals that does not deserve da hate


# x = 'TACGATTA'
# y = 'ATTAACTTA'

if len(sys.argv) < 2:
        raise Exception("Usage: 'file.fa', 'matrix_type.txt', gap_penalty")

print('Arguments passed:', sys.argv[2:])

gap = int(sys.argv[3])
matrix_type = sys.argv[2]

nx = len(x)  # length of first base sequence
ny = len(y)  # length of second base sequence


if sys.argv[2] == "HOXD70.txt":
    F = np.zeros((nx + 1, ny + 1))  #form F-matrix array
    Tr = np.zeros((nx + 1, ny + 1)) #form traceback matrix
    Tr[:,0] = 3
    Tr[0,:] = 4 #arbitrary assignment
    F[:, 0] = np.linspace(0, -gap * nx, nx + 1) #continuous gap scores increase the negative count for seq 1
    F[0, :] = np.linspace(0, -gap * ny, ny + 1) #continuous gap scores increase the negative count for seq 2
    t = np.zeros(3) #initalize a matrix to store the score of the three alignments (this could be done with three variables as well)
    for i in range(nx):
        for j in range(ny):
            #iteration step: take the max (inserting gap in first sequence, inserting gap in second sequence, match or mutation)
            if x[i] == y[j]: #if bases match
                t[0] = F[i, j] + df.at[x[i], y[j]]
                #increase the F-matrix score for the first matrix member in t by match
            else:
                t[0] = F[i, j] + df.at[x[i], y[j]] #bases don't match, decrease the score at the index for the first matrix member in t
            # gap in first sequence
            t[1] = F[i, j + 1] - gap
            # gap in second sequence
            t[2] = F[i + 1, j] - gap
            tmax = np.max(t)
            F[i + 1, j + 1] = tmax
            if t[0] == tmax:
                Tr[i+1, j+1] += 1 #print bases
            elif t[1] == tmax:
                Tr[i+1, j+1] += 2 #gap in first sequence
            elif t[2] == tmax:
                Tr[i+1, j+1] += 3 #gap in second sequence
    i = nx
    j = ny
    rx = []
    ry = []
    while i > 0 or j > 0:

        # if there is a match/mismatch
        if Tr[i, j] in [1]:
            rx.append(x[i - 1])
            ry.append(y[j - 1])
            i -= 1
            j -= 1

        # if there's a gap in the first sequence
        elif Tr[i, j] in [2]:
            rx.append(x[i - 1])
            ry.append('-')
            i -= 1

        # if there's a gap in the second sequence
        elif Tr[i, j] in [3]:
            rx.append('-')
            ry.append(y[j - 1])
            j -= 1
# Reverse the strings.
    rx = ''.join(rx)[::-1]
    ry = ''.join(ry)[::-1]
    complete = '\n'.join([rx, ry])
    gaps = complete.count('-')
    score = F[-1, -1]
    print(complete)
    print(gaps)
    print(score)
    with open("output_DNA.txt", "a") as f:
        print(complete, gaps, score, file=f)

if sys.argv[2] == "BLOSUM62.txt":
    F = np.zeros((nx + 1, ny + 1))  # form F-matrix array
    Tr = np.zeros((nx + 1, ny + 1))  # form traceback matrix
    Tr[:, 0] = 3
    Tr[0, :] = 4  # arbitrary assignment
    F[:, 0] = np.linspace(0, -gap * nx, nx + 1)  # continuous gap scores increase the negative count for seq 1
    F[0, :] = np.linspace(0, -gap * ny, ny + 1)  # continuous gap scores increase the negative count for seq 2
    t = np.zeros(3)  # initalize a matrix to store the score of the three alignments (this could be done with three variables as well)
    for i in range(nx):
        for j in range(ny):
            # iteration step: take the max (inserting gap in first sequence, inserting gap in second sequence, match or mutation)
            if x[i] == y[j]:  # if bases match
                t[0] = F[i, j] + df.at[x[i], y[j]]
                # increase the F-matrix score for the first matrix member in t by match
            else:
                t[0] = F[i, j] + df.at[x[i], y[j]]  # bases don't match, decrease the score at the index for the first matrix member in t
            # gap in first sequence
            t[1] = F[i, j + 1] - gap
            # gap in second sequence
            t[2] = F[i + 1, j] - gap
            tmax = np.max(t)
            F[i + 1, j + 1] = tmax
            if t[0] == tmax:
                Tr[i + 1, j + 1] += 1  # print bases
            elif t[1] == tmax:
                Tr[i + 1, j + 1] += 2  # gap in first sequence
            elif t[2] == tmax:
                Tr[i + 1, j + 1] += 3  # gap in second sequence
    i = nx
    j = ny
    rx = []
    ry = []
    while i > 0 or j > 0:

        # if there is a match/mismatch
        if Tr[i, j] in [1]:
            rx.append(x[i - 1])
            ry.append(y[j - 1])
            i -= 1
            j -= 1

        # if there's a gap in the first sequence
        elif Tr[i, j] in [2]:
            rx.append(x[i - 1])
            ry.append('-')
            i -= 1

        # if there's a gap in the second sequence
        elif Tr[i, j] in [3]:
            rx.append('-')
            ry.append(y[j - 1])
            j -= 1
    # Reverse the strings.
    rx = ''.join(rx)[::-1]
    ry = ''.join(ry)[::-1]
    complete = '\n'.join([rx, ry])
    gaps = complete.count('-')
    score = F[-1, -1]
    print(complete)
    print(gaps)
    print(score)
    with open("output_AA.txt", "a") as f:
        print(complete, gaps, score, file=f)



