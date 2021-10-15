a = int(input("Masukkan jumlah anak ayam: "))
print("tek kotek kotek kotek, anak ayam turun berkotek")
if a>=1:
     while a>1:
         print("Anak ayam turunlah %d Mati 1 tinggallah %d"%(a,a-1))
         a = a - 1
         if a<=1:
             print("Anak ayam turunlah %d Mati 1 tinggallah induknya"%(a))
 
else:
     print("anak ayam ada %d beli lagi aja yang banyak dipasar"%(a))