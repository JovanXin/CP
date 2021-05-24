n_sd = int(input())
n_md = int(input())
n_ld = int(input())

longest = max(n_sd, n_md, n_ld)

e_sd = longest - n_sd
e_md = longest - n_md
e_ld = longest - n_ld

lm = "L" * n_ld
mm = "M" * n_md
sm = "S" * n_sd

lm = "_" * (e_ld // 2) + lm + "_" * (e_ld // 2)
mm = "_" * (e_md // 2) + mm + "_" * (e_md // 2)
sm = "_" * (e_sd // 2) + sm + "_" * (e_sd // 2)

if e_ld % 2 != 0:
    lm = lm + "_"
if e_md % 2 != 0:
    mm = mm + "_"
if e_sd % 2 != 0:
    sm = sm + "_"

print(lm)
print(mm)
print(sm)
