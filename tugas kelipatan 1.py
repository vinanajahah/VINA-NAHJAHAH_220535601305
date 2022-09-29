#Himpunan

#from re import I


from re import I, I


Jumlah_seluruh_bilangan_asli = 0
for I in range(1000):
    if (I%3 == 0 or I%5 == 0):
     Jumlah_seluruh_bilangan_asli = Jumlah_seluruh_bilangan_asli + I

print("Jumlah seluruh bilangan asli yang merupakan kelipatan 3 atau 5 kurang dari 1000=", Jumlah_seluruh_bilangan_asli)