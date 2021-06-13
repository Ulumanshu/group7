import string

a_list = [s for s in string.ascii_lowercase]
print(a_list, type(a_list))

splice1 = a_list[:8]
print(splice1)

splice2 = a_list[4:]
print(splice2)

splice3 = a_list[4:8]
print(splice3)

splice4 = a_list[::-1]
print(splice4)

phrase = "The animal I really dig, Above all others is the pig."

# mini uzduotis
# 1. Ishlicinti dig, all, pig i kintamuosius, juos atprintinti
# 2. apsukti zodi pig i gip ir apsukti zodi animal, i kintamuosius ir atprintinti.
# pvz:
# dig reverse
dig = phrase[22:19:-1]
print(dig)
