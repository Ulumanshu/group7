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

# Tuple - nemutabilus rinkiniai
tuple1 = (1, 365, 14, 20) # tuple()


# Complex variables !!!!!!!!!!!!!!!!!!!!! they are more like references in comples structures
# List (Array) - sarasas, su pozicijomis ir pirma pozicija yra 0
list1 = list()  # list1 = []
list2 = []
list3 = [bool1, bool2, integer2, integer2]

# Dictionaries - Objects - raktazodis: reiksme tipo duomeny stuktura, nera eilishkumo
zodynas1 = dict()  # {}
zodynas1['raktas_1'] = integer1 # speciali sintakse prideti i zodyna zodyno_kintamasis['naujas_raktas'] = reiksme
zodynas1['raktas_2'] = bool2
zodynas1['raktas_3'] = False  #  list3

abc4 = zodynas1.get('raktas_3', []) #, []) or []
print("ABC$: ", abc4)

# abc = list3[0]
# abc2 = list3[1]
# maks_indexas = len(list3) - 1
# print(maks_indexas)
# index = 3
# if index <= maks_indexas:
#     abc3 = list3[index]
#     print("ABC3: ", abc3)
# else:
#     print("INDEX OUT OF RANGE!")

# print(list3, abc, abc2)
# Sets - setai, unikaliu reiksmiu sarasas
setas1 = set()  # pridejimo metodas .add()
setas1.add(string2)
setas1.add(string2)
setas1.add(string1)
# print("SETAS1: ", setas1)

# print("ZODYNAS1: ", zodynas1)
zodynas2 = zodynas1.copy()  #  sekli zodyno kopija, visi kompleksiniai duomenu tipai yra nuorodos ty tarp zodynu tas pats objektas
# print("ZODYNAS2: ", zodynas1)

sarasas_x = zodynas2.get('raktas_3', []) or []
# sarasas_x.append('NEMATYTA')
# print("LIST3: ", list3)
# print("ZODYNAS1: ", zodynas1)
# print("ZODYNAS2: ", zodynas2)

# print("Visi sarasai po sukurimo", list1, list2, list3)
# Saraso valdymo bazines komandos
list1.append('tiesiog reiksme')  # galima prideti duomenis tiesiogiai
list1.append(integer1)  # galima prideti kintamaji, prideti elementai visad prisideda gale
list2.append(string2)
list2.append(float2)
# print("Visi sarasai po pridejimo", list1, list2, list3)

mano_sarasas = list()
# print("Mano Sarasas", mano_sarasas)
# # ["pirmas", 1, "antras", 2, 'trecias', 3]
# # print('Baigiasi su s: ', string3.endswith('s'))
# # print('Baigiasi su t: ', string3.endswith('t'))
# print("Pirmas sveikas sk: ", type(integer1))

# print('Visi sveiki skaiciai: ', integer1, integer2, integer3)

# For loopas
naujas_didelis_listas = [
    integer2, integer2, integer1, string2, string3, string1, tuple1, float1, float1, float3, float2
]
unikalus_nariu_sarasas = set()  # pridedam i ji su add()
atrinktu_nariu_sarasas = []
for elementai_is_eiles in naujas_didelis_listas:
    print('LISTAS3 VISAS: ', naujas_didelis_listas)
    elemento_tipas = type(elementai_is_eiles)
    texto_tipas = type('bet koks teksto tipas')
    print('LISTAS3 ELEMENTAS CIKLE: ', elementai_is_eiles)
    if elemento_tipas == texto_tipas:
        print('LISTAS3 TEXT ELEMENTAS CIKLE: ', elementai_is_eiles)




