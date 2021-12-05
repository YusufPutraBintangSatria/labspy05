# Labspy05

Modul praktikum 5 berisi latihan untuk menggunakan dictionary pada python, praktikum membuat Program Daftar Nilai Mahasiswa menggunakan dictionary dan menampilkan pilihan menu yaitu : Ubah, Tambah, Hapus, Cari, & Lihat!

# Latihan 


### Latihan pertama adalah membuat daftar kontak menggunakan dictionary pada python
- Berikut adalah gambar source code nya:

![1](https://user-images.githubusercontent.com/92704969/144747827-c300b5c3-ba99-4388-9d4c-404c1e050184.png)


Penjelasan source code sebagai berikut:
- Dibawah ini adalah untuk menampung data dari dictionary

```python
daftarkontak = {"Nama":"Nomor Telepon"}
kontak = {'Ari':'081267888', 'Dina':'087677776'}
```

- Code dibawah adalah untuk mengakses atau menampilkan kontak yang telah ditampung dalam data dictionary

```python
print("="*80)
print("   Nama  |    Nomor Telepon   ")
print("="*80)
print(" # Ari   |   ",kontak['Ari'])
print(" # Dina  |   ",kontak['Dina'])
print("="*80)
```

- berikut ini adalah hasil programnya :

![2](https://user-images.githubusercontent.com/92704969/144747831-fce3e9b8-3cee-4e0a-96ff-696107fab6f4.png)

- Code dibawah ini untuk menampilkan salah satu dari daftar kontak yang ada, berikut akan di tampilkan daftar kontak Ari

```python
print("Menampilkan kontak Ari")
print("="*80)
print(" # Ari   |   ",kontak['Ari'])
print("="*80)
```

- berikut ini adalah hasil programnya :

![3](https://user-images.githubusercontent.com/92704969/144747832-0519baf5-9359-4ce4-8844-59bcf2af8d8d.png)

- Code dibawah ini untuk menambahkan kontak dengan nama Riko dan nomor 087654544

```python
print("Menambah kontak dengan dana Riko dan Nomor Telepon 087654544")
kontak['Riko']='087654544'
print("="*80)
print("  Riko   |   ",kontak['Riko'])
print("="*80)
```

- berikut ini adalah hasil programnya :

![4](https://user-images.githubusercontent.com/92704969/144747833-7bcee5a3-1ba3-473b-9c8f-998aef618dcb.png)

- Code dibawah untuk mengubah kontak Dina dengan nomor baru 0889999776

```python
print("Mengubah kontak Dina dengan nomor baru 0889999776")
kontak['Dina']='0889999776'
print("="*80)
print(" # Dina  |   ",kontak['Dina'])
print("="*80)
```

- berikut ini adalah hasil programnya :

![5](https://user-images.githubusercontent.com/92704969/144747834-fd3a0dc5-2330-449c-8d4e-2ec9c7138f6d.png)

- Code dibawah untuk menampilkan semua nama yang ada dalam daftar kontak

```python
print("Menampilkan semua nama")
print("="*80)
print(kontak.keys())
print("="*80)
```

- berikut ini adalah hasil programnya:

![6](https://user-images.githubusercontent.com/92704969/144747836-9c3ca491-c692-4cb5-9259-fa74c59fa66e.png)

- Code di bawah untuk menampilkan semua nomor yang ada dalam daftar kontak

```python
print("Menampilkan semua nomor")
print("="*80)
print(kontak.values())
print("="*80)
```

- berikut ini adalah hasil programnya :

![7](https://user-images.githubusercontent.com/92704969/144747837-03c72c01-2c31-497a-b72f-8be9ee0f7bae.png)

- Code berikut untuk menampilkan semua daftar kontak beserta nama dan nomornya

```python
print("Menampilkan daftar nama dan nomor")
print("="*80)
print(kontak.items())
print("="*80)
```

- berikut ini adalah hasil programnya :

![8](https://user-images.githubusercontent.com/92704969/144747838-3225b05b-095a-4a04-a189-7b56d102f4aa.png)

- Code dibawah untuk menghapus kontak Dina yang tersimpan dalam daftar kontak

```python
print("Hapus kontak Dina")
kontak.pop('Dina')
print("="*80)
print(kontak.items())
print("="*80)
```

- berikut ini adalah hasil programnya:

![9](https://user-images.githubusercontent.com/92704969/144747840-4bf06038-a5f3-42c8-bbda-c59340abbeb3.png)


# Praktikum

### Dibawah ini adalah program sederhana untuk membuat daftar nilai mahasiswa dengan menggunakan dictionary, dan menampilkan pilihan menu tambah, ubah, cari, hapus, dan lihat

- Gambar source code :

![10](https://user-images.githubusercontent.com/92704969/144747841-382197de-c5ff-4079-adf2-6b6f201844d1.png)

- Flowchart program:

![11](https://user-images.githubusercontent.com/92704969/144747843-b9f40511-a263-4295-8ed0-a5ea6a022914.png)

Dengan penjelasan source code sebagai berikut:
- Code dibawah ini untuk membuat dictionary kosong, untuk menampung dictionary dengan menggunakan tuple

```python
a = {}
```

- Code dibawah ini untuk perulangan while, dan juga untuk menginisialkan penambahan menu pilihan Tambah, Ubah, Hapus, Cari, Lihat dan Keluar:

```python
while True:
    x = input("(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")
```

- Code dibawah adalah untuk syntax penambahan data, dengan ketentuan jika kita mengetikkan 't' pada keyboard, maka akan melakukan penambahan data dan ditampung kedalam dictionary 'a' yang telah kita buat, dengan nama sebagai keys, dan yang lainnya sebagai values

```python
    if x.lower() == 't':
        print("Tambah Data")
        nama = input("Nama           : ")
        nim = int(input("NIM            : "))
        uts = int(input("Nilai UTS      : "))
        uas = int(input("Nilai UAS      : "))
        tugas = int(input("Nilai Tugas    : "))
        n_akhir = tugas * 0.30 + uts * 0.35 + uas * 0.35
        a[nama] = nim, uts, uas, tugas, n_akhir
```

- Code dibawah adalah untuk syntax mengubah data, dengan ketentuan jika kita mengetikkan 'u' pada keyboard, maka akan melakukan perubahan data yang telah di tampung ke dalam dictionary 'a' yang telah kita buat, tetapi data yang dapat diubah hanya data yang berupa values nya saja

```python
    elif x.lower() == 'u':
        print("Ubah Data")
        nama = input("Masukkan Nama   : ")
        if nama in a.keys():
            nim = int(input("NIM            : "))
            uts = int(input("Nilai UTS      : "))
            uas = int(input("Nilai UAS      : "))
            tugas = int(input("Nilai Tugas    : "))
            n_akhir = tugas*0.30 + uts*0.35 + uas*0.35
            a[nama] = nim, uts, uas, tugas, n_akhir
        else:
            print("Nama{0} Tidak Ditemukan".format(nama))
```

- Code dibawah adalah untuk syntax penghapusan data, dengan ketentuan jika kita mengetikkan 'h' pada keyboard, maka akan melakukan penghapusan data yang telah kita masukkan kedalam dictionary 'a' yang telah kita buat dengan statemen ```del a[nama]```

```python
    elif x.lower() == 'h':
        print("Hapus Data")
        nama = input("Masukkan Nama  : ")
        if nama in a.keys():
            del a[nama]
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))
```

- Code dibawah adalah untuk syntax pencarian data, dengan ketentuan jika kita mengetikkan 'c' pada keyboard, maka akan melakukan pencarian data dengan memasukkan keys dari data yang telah kita masukkan kedalam dictionary 'a' yang telah kita buat

```python
    elif x.lower() == 'c':
        print("Cari Data")
        nama = input("Masukkan Nama : ")
        if nama in a.keys():
            print("=" * 73)
            print("|                             Daftar Mahasiswa                          |")
            print("=" * 73)
            print("| Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("=" * 73)
            print("| {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                  .format(nama, nim, uts, uas, tugas, n_akhir))
            print("=" * 73)
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))
```

- Code dibawah adalah untuk syntax melihat data, dengan ketentuan jika kita mengetikkan 'l' pada keyboard, maka akan menampilkan keseluruhan dari data yang telah kita masukkan dan ditampung ke dalam dictionary 'a' yang telah kita buat

```python
    elif x.lower() == 'l':
        if a.items():
            print("=" * 78)
            print("|                               Daftar Mahasiswa                             |")
            print("=" * 78)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("=" * 78)
            i = 0
            for y in a.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                      .format(y[0][:13], y[1][0], y[1][1], y[1][2], y[1][3], y[1][4], no=i))
                print("=" * 78)
```

- Code dibawah adalah untuk menampilkan 'TIDAK ADA DATA', jika kita belum pernah memasukkan data kedalam dictionary 'a'

```python
        else:
            print("=" * 78)
            print("|                               Daftar Mahasiswa                             |")
            print("=" * 78)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("=" * 78)
            print("|                                TIDAK ADA DATA                              |")
            print("=" * 78)
```

- sedangkan code dibawah adalah untuk syntax keluar dari program, untuk menghentikan program, dengan ketentuan jika kita mengetikkan 'k' pada keyboard, maka akan keluar dari program tersebut

```python
    elif x.lower() == 'k':
        break
```

- Dan code yang terakhir adalah untuk syntax jika kita mengetikkan pada keyboard selain dari huruf yang telah di definisikan di atas seperti 't', 'u', 'h', 'c', 'l', dan 'k', maka akan menampilkan Pilih Menu Yang Tersedia

```python
    else:
        print("Pilih Menu Yang Tersedia")
```

### Berikut hasil program praktikum, jika programnya di jalankan

- Menambahkan Data dengan syntax 't' dan melihat data dengan syntax 'l'

![12](https://user-images.githubusercontent.com/92704969/144747844-e9d5fc85-c4cc-47a7-a58f-c048cdc7360f.png)

![13](https://user-images.githubusercontent.com/92704969/144747845-abc57bad-8a28-41bd-b57b-18089b152ead.png)

- Mengubah data dengan syntax 'u', dan melihat data dengan syntax 'l'

![14](https://user-images.githubusercontent.com/92704969/144747846-c54a18b2-f53e-477b-ad97-11038e7072df.png)

- Mencari data dengan syntax 'c', dan melihat data dengan syntax 'l'

![15](https://user-images.githubusercontent.com/92704969/144747848-ba34000b-efbe-4816-bf75-189d9854552a.png)

- Menghapus data dengan syntax 'h' dan melihat data dengan syntax 'l'

![16](https://user-images.githubusercontent.com/92704969/144747850-131e7273-1f25-406c-acb9-262b7281b7fc.png)

- Keluar dari program dengan syntax 'k'

![17](https://user-images.githubusercontent.com/92704969/144747851-854b8f2f-7309-4da4-b964-2bbc17c10b5a.png)




### Sekian Terima Kasih. Praktikum Modul 5 Menggunakan Dictionary Pada Python. 