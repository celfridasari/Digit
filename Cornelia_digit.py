def digitAwal(x,y): #fungsi digit awal
    kuadrat = str(x**y) #untuk menghitung kuadrat dari variable x dan y
    listKuadrat = [char for char in kuadrat] #menjadikan variable kuadrat menjadi list
    return listKuadrat[0] #mengambil value paling awal dari list kuadrat sebagai digit awal
print('#Output:') #label output
print(digitAwal(10,8))
print(digitAwal(2,3))
print(digitAwal(6,3))
print('\n') #spasi antara output digit awal dan digit akhir
def digitAkhir(x,y): #fungsi digit akhir
    kuadrat = str(x**y) #untuk menghitung kuadrat dari variable x dan y
    listKuadrat = [char for char in kuadrat] #menjadikan variable kuadrat menjadi list
    return listKuadrat[-1]#mengambil value paling akhir dari list kuadrat sebagai digit akhir
print('#Output:') #label output
print(digitAkhir(10,8))
print(digitAkhir(2,3))
print(digitAkhir(6,3))