# 1. Nusiskaityti is failo data.txt kainu duomenis
# 2. Susideti duomenis i dictionary
# 3. Sukurti nauja objekta kuriam butu aishkiai parasyta kiek kg galima itemo nupirkti uz biudzeta.

budet_limit = 15 # eu

with open('data.txt', 'rt') as f:
    file_data = f.read()
    print(file_data)