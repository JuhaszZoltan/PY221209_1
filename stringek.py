szoveg:str = 'Alma a Fa Alatt'

hossz:int = len(szoveg)
print(f'söveg hossza: {hossz}')

betu:chr = szoveg[0]
print(f'szöveg nullás indexű karaktere: {betu}')

for betu in szoveg:
    print(betu, end='\n')

chrlist:list[chr] = ['a', 'b', 'c', 'd']

# ez nem fog működni, mert 'csak olvasható' mint 'lista':
# szoveg[0] = 'E'

szoveg += ' van'
print(szoveg)

# -----------------------------

csupa_kisbetu = szoveg.lower()
print(csupa_kisbetu)
csupa_nagybetu = szoveg.upper()
print(csupa_nagybetu)

kapitalizalt:str = szoveg.capitalize()
print(kapitalizalt)
cimszeru:str = szoveg.title()
print(cimszeru)

cicaval_kezdodik:bool = szoveg.startswith('Cica')
print(cicaval_kezdodik)

vannal_vegzodik:bool = szoveg.endswith('van')
print(vannal_vegzodik)

faindex:int = szoveg.index('Fa')
print(faindex)
# cicaindex:int = szoveg.index('Cica!')
# print(cicaindex)

van_benne_fa:bool = 'Fa' in szoveg
print(van_benne_fa)

cserelt:str = szoveg.replace('Alma', 'Körte')
print(cserelt)
cserelt_2:str = szoveg.replace('A', 'Ö')
print(cserelt_2)
cserelt_3:str = szoveg.replace('A', 'Ö').replace('a', 'ö')
print(cserelt_3)

szavak:list[str] = szoveg.split()
print(szavak)


szoveg = '    \t\t\n\n   John Doe;male;1992-05-18;Budapest\n\n  \t'
print(szoveg)
szoveg:str = szoveg.strip()
print(szoveg)

szavak_2:list[str] = szoveg.split(';')
print(szavak_2)