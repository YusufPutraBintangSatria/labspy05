daftarkontak = {"Nama":"Nomor Telepon"}
kontak = {'Ari':'081267888', 'Dina':'087677776'}

print("="*80)
print("   Nama  |    Nomor Telepon   ")
print("="*80)
print(" # Ari   |   ",kontak['Ari'])
print(" # Dina  |   ",kontak['Dina'])
print("="*80)

# Menampilkan kontak Ari
print("Menampilkan kontak Ari")
print("="*80)
print(" # Ari   |   ",kontak['Ari'])
print("="*80)

#Menambahkan kontak dengan nama Riko dan nomor 087654544
print("Menambah kontak dengan dana Riko dan Nomor Telepon 087654544")
kontak['Riko']='087654544'
print("="*80)
print("  Riko   |   ",kontak['Riko'])
print("="*80)

#Mengubah kontak Dina dengan nomor baru 0889999776
print("Mengubah kontak Dina dengan nomor baru 0889999776")
kontak['Dina']='0889999776'
print("="*80)
print(" # Dina  |   ",kontak['Dina'])
print("="*80)

#Menampilkan semua nama
print("Menampilkan semua nama")
print("="*80)
print(kontak.keys())
print("="*80)

#Menampilkan semua nomor
print("Menampilkan semua nomor")
print("="*80)
print(kontak.values())
print("="*80)

#Menampilkan semua daftar kontak beserta nama dan nomornya
print("Menampilkan daftar nama dan nomor")
print("="*80)
print(kontak.items())
print("="*80)

#Menghapus kontak Dina
print("Hapus kontak Dina")
kontak.pop('Dina')
print("="*80)
print(kontak.items())
print("="*80)