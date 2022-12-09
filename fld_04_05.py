szoveg:str = input('írj be valamit: ')
# 0 1 2 3
# C I C A == 4

for i in range(len(szoveg)):
    print(szoveg[len(szoveg) - 1 - i], end='\0')

# ---------------------

karlista:list[chr] = list[chr](szoveg)
karlista.reverse()
forditott:str = ''.join(karlista)
print(f'\n{forditott}')

# ---------------------

print(szoveg[::-1])