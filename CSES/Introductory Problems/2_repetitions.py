seq = input()

max_seq = 1
curr_seq = 1
for i in range(1, len(seq)):
    if seq[i] == seq[i - 1]:
        curr_seq += 1
    else:
        curr_seq = 1
    max_seq = max(max_seq, curr_seq)


print(max_seq)