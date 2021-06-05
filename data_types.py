# Data types - duomenu tipai

# Simple data types they are direct values in complex structures
# 1 Integer - Sveikas Skaicius
integer1 = 1  # int()
integer2 = 2
integer3 = 3

# Float - Skaicius su kableliu
float1 = 1.53  # float()  metodai pvz: .is_integer()
float2 = 2.45
float3 = 5.75

# String - textas arba baitai.
string1 = "pirmas"  # str() endswith() .isupper()
string2 = "antras"
string3 = 'trecias'  # naujas_kitamasis = list() [] .append() naujas_kint = str() '' .endswith() .isupper()

# Bool - loginiai
bool1 = True # bool()
bool2 = False

# None - tipas neapibreztiems dalykams
# TODO paaiskinti prasme funcijos priemimo skliaustuose, pvz su sarasu def kazkas(kint1=None arba [])!
none1 = None

# Complex variables !!!!!!!!!!!!!!!!!!!!! they are more like references in comples structures
# List (Array) - sarasas, su pozicijomis ir pirma pozicija yra 0
list1 = list()  # list1 = []
list2 = []
list3 = [bool1, bool2]

# Dictionaries - Objects - raktazodis: reiksme tipo duomeny stuktura, nera eilishkumo
zodynas1 = dict()  # {}
zodynas1['raktas_1'] = integer1 # speciali sintakse prideti i zodyna zodyno_kintamasis['naujas_raktas'] = reiksme
zodynas1['raktas_2'] = bool2
zodynas1['raktas_3'] = list3


print("ZODYNAS1: ", zodynas1)
zodynas2 = zodynas1.copy()  #  sekli zodyno kopija, visi kompleksiniai duomenu tipai yra nuorodos ty tarp zodynu tas pats objektas
print("ZODYNAS2: ", zodynas1)

sarasas_x = zodynas2.get('raktas_3')
sarasas_x.append('NEMATYTA')
print("LIST3: ", list3)
print("ZODYNAS1: ", zodynas1)
print("ZODYNAS2: ", zodynas2)



print("Visi sarasai po sukurimo", list1, list2, list3)
# Saraso valdymo bazines komandos
list1.append('tiesiog reiksme')  # galima prideti duomenis tiesiogiai
list1.append(integer1)  # galima prideti kintamaji, prideti elementai visad prisideda gale
list2.append(string2)
list2.append(float2)
print("Visi sarasai po pridejimo", list1, list2, list3)

mano_sarasas = list()
print("Mano Sarasas", mano_sarasas)
# ["pirmas", 1, "antras", 2, 'trecias', 3]
# print('Baigiasi su s: ', string3.endswith('s'))
# print('Baigiasi su t: ', string3.endswith('t'))
print("Pirmas sveikas sk: ", type(integer1))

# print('Visi sveiki skaiciai: ', integer1, integer2, integer3)




