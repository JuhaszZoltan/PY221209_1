szoveg:str = input('írj be valamit: ')

c:int = 0
for b in szoveg:
    if b in 'Ee': c += 1
print(f'"E" betűk száma: {c}')