from tabulate import tabulate
from operator import itemgetter
import datetime

print(f"\n----------------------------------------")
print("Selamat Datang di Rumah Sakit Purwadhika")
print("--------------Data Pasien---------------")
print("----------------------------------------")

daftarPasien = [
    {'id' : 2204001, 'Nama' : 'Federick Samuel', 'NIK' : 3404130420010002, 'Jenis Kelamin' : 'Pria', "Umur" : 22,'Alamat' : 'Kelapa Gading', 'Pekerjaan': 'Mahasiswa', 'Penyakit' : 'Gangguan Otak', 'Tanggal Registrasi' : datetime.date(2023,6,21).strftime("%d %b %Y")},
    {'id' : 2204002, 'Nama' : 'Hafidh Diya', 'NIK' : 3404120410980004, 'Jenis Kelamin' : 'Pria', "Umur" : 25,'Alamat' : 'Bekasi', 'Pekerjaan': 'Karyawan Swasta', 'Penyakit' : 'Gangguan Pencernaan', 'Tanggal Registrasi' : datetime.date(2023,10,2).strftime("%d %b %Y")}
]

daftar_obat = [
    {'Nomor' : 0, 'Jenis Obat' : 'Obat Demam', 'Nama Obat' : 'Paracetamol', 'Stok' : 20, 'Harga' : 10000},
    {'Nomor' : 1, 'Jenis Obat' : 'Obat Diare', 'Nama Obat' : 'Loperamide', 'Stok' : 20, 'Harga' : 15000},
    {'Nomor' : 2, 'Jenis Obat' : 'Obat Alergi', 'Nama Obat' : 'Epinefrin', 'Stok' : 20, 'Harga' : 8000},
    {'Nomor' : 3, 'Jenis Obat' : 'Obat Batuk', 'Nama Obat' : 'Bisolvon', 'Stok' : 20, 'Harga' : 35000},
    {'Nomor' : 4, 'Jenis Obat' : 'Obat Flu', 'Nama Obat' : 'Ibuprofen', 'Stok' : 20, 'Harga' : 5000},
    {'Nomor' : 5, 'Jenis Obat' : 'Antibiotik', 'Nama Obat' : 'Cefixime', 'Stok' : 20, 'Harga' : 11000},
    {'Nomor' : 6, 'Jenis Obat' : 'Vitamin', 'Nama Obat' : 'Neurosanbe', 'Stok' : 20, 'Harga' : 18000},
    {'Nomor' : 7, 'Jenis Obat' : 'Anti Radang', 'Nama Obat' : 'Lameson', 'Stok' : 20, 'Harga' : 10000},
]

konsumsi_obat = []

#Menu Utama
def main_menu():
    print()
    while True : 
        print(f'''\nList Main Menu : 
            1. Tampilkan Data Pasien
            2. Tambah Pasien Baru
            3. Perbarui Data Pasien
            4. Hapus Data Pasien
            5. Menu Daftar Obat
            6. Menu Pembelian Obat
            7. Keluar Program
            ''')
        try : #Proteksi Inputan Menu
            menu = int(input("Masukkan Pilihan Menu : "))
            print(f'\n')

            if menu in [1,2,3,4,5,6,7] :
                break
            else :
                print("Menu yang dimasukkan salah, silahkan coba lagi.")

        except :
            print("Menu yang dimasukkan salah, silahkan coba lagi.")
        
    if menu == 1 : #Menampilkan Data Pasien
        menu1()

    elif menu == 2 : #Penambahan Pasien Baru
        menu2()

    elif menu == 3 : #Update Data Pasien
        menu3()
            
    elif menu == 4 : #Menghapus Data Pasien
        menu4()
    
    elif menu == 5 : #Menu Daftar Obat
        menu5()
    
    elif menu == 6 : #Data Pembelian Obat
        menu6()

    elif menu == 7 : #Keluar Program
        print(f"Terima kasih sudah berkunjung.\n")
        exit()

#Menu 1
#Menu Menampilkan Daftar Pasien
def menu1():
    menu1_con = True
    while menu1_con :
        while True :
            print(f'''Daftar Pasien : 
                1. Data Seluruh Pasien
                2. Data Pasien Berdasarkan Nomor NIK
                3. Menu Sorting Data Pasien
                4. Menu Utama
                \n''')
            try : #Proteksi Inputan Menu
                menu_1 = int(input("Masukkan Pilihan Menu : "))
                print(f'\n')

                if menu_1 in [1,2,3,4] :
                    break
                else :
                    print("Menu yang dimasukkan salah, silahkan coba lagi.")

            except :
                print("Menu yang dimasukkan salah, silahkan coba lagi.")

        if menu_1 == 1 : #Menu Data Seluruh Pasien
            show_data()
        
        elif menu_1 == 2 : #Menu Pengambilan Data Pasien Berdasarkan NIK
            konfirmasi_NIK = True
            while konfirmasi_NIK :
                NIK_pasien = int(input("Masukkan NIK Pasien : "))
                for k in range(len(daftarPasien)) :
                    if NIK_pasien == daftarPasien[k]['NIK'] :
                        print(f'Data Pasien dengan NIK {NIK_pasien} : ')
                        print(f"\nNama             \t: {daftarPasien[k]['Nama']}")
                        print(f"NIK             \t: {daftarPasien[k]['NIK']}")
                        print(f"Jenis Kelamin    \t: {daftarPasien[k]['Jenis Kelamin']}")
                        print(f"Umur             \t: {daftarPasien[k]['Umur']}")
                        print(f"Alamat            \t: {daftarPasien[k]['Alamat']}")
                        print(f"Pekerjaan        \t: {daftarPasien[k]['Pekerjaan']}")
                        print(f"Penyakit         \t: {daftarPasien[k]['Penyakit']}")
                        print(f"Tanggal Registrasi\t: {daftarPasien[k]['Tanggal Registrasi']}\n")
                        konfirmasi_NIK = False
                    else : 
                        print(f"NIK yang dimasukkan salah\n")
        
        elif menu_1 == 3 : #Menu Sorting Data Pasien
            konfirmasi_sorting = True

            while konfirmasi_sorting :
                try : #Proteksi Inputan Menu
                    print('''Sorting Data Pasien berdasarkan :
                        1. Nama Pasien (A - Z)
                        2. Nama Pasien (Z - A)
                        3. Usia Pasien (Muda - Tua)
                        4. Usia Pasien (Tua - Muda)
                        5. Tanggal Registrasi
                        ''')
                    menu_sorting = int(input("Masukkan Pilihan Menu Sorting : "))
                    
                    if menu_sorting == 1 : #Sorting berdasarkan Nama Pasien (A - Z)
                        sort('Nama')

                    elif menu_sorting == 2 : #Sorting berdasarkan Nama Pasien (Z - A)
                        sort('Nama', reverse=True)

                    elif menu_sorting == 3 : #Sorting berdasarkan Usia Pasien (Muda - Tua)
                        sort('Umur')

                    elif menu_sorting == 4 : #Sorting berdasarkan Usia Pasien (Tua - Muda)
                        sort('Umur', reverse=True)

                    elif menu_sorting == 5 : #Sorting berdasarkan Tanggal Registrasi
                        daftarPasien.sort(key = lambda i:i['Tanggal Registrasi'], reverse=True)
                        headersP = daftarPasien[0].keys()
                        dataP = [j.values() for j in daftarPasien]
                        print(tabulate(dataP,headersP, tablefmt="grid"))
                    
                    while True :
                        jawab_sorting = input(f"\nApakah ingin menggunakan menu sorting lagi? (Ya / Tidak) : ")
                        print()
                        if jawab_sorting.lower() == 'ya' :
                            break
                        elif jawab_sorting.lower() == 'tidak' :
                            konfirmasi_sorting = False
                            break
                        else :
                            print("Input salah, silahkan coba lagi.")

                except :
                    print(f"Menu yang dimasukkan salah, silahkan coba lagi.\n")

        elif menu_1 == 4 :
            menu1_con = False
            main_menu()            

#Menu 2
#Menambah Data Pasien Baru
def menu2():
    menu2_con = True
    while menu2_con :
        while True :
            print(f'''Menu Menambah Data Pasien Baru
                1. Menambah Data Pasien Baru
                2. Menu Utama\n''')
            try : #Proteksi Inputan Menu
                menu_2 = int(input("Masukkan Pilihan Menu : "))
                print()
                if menu_2 in [1,2] :
                    break
                else :
                    print(f"Menu yang dimasukkan salah, silahkan coba lagi.\n")
            except :
                print(f"Menu yang dimasukkan salah, silahkan coba lagi.\n")
        print()
        if menu_2 == 1 :
            #Input Nama
            n_num = 0
            n_alpha = 0
            while True : #Proteksi Input Nama
                nama_baru = input("Masukkan Nama Pasien : ")
                for l in range(len(nama_baru)): #Pengecekan apakah terdapat angka di dalam Nama
                    if nama_baru[l].isdigit() == True :
                        n_num +=1
                    elif nama_baru[l].isalpha() == True :
                        n_alpha +=1
                if n_num > 0 :
                    print("Nama yang diinput mengandung angka, silahkan coba lagi.")
                    n_num = 0
                elif n_num == 0 and n_alpha == 0 :
                    print('Tidak ada Inputan, silahkan coba lagi.')
                else :
                    nama_baru = str(nama_baru)
                    break
            print(f'\n')

            #Input NIK
            n_NIKnum = 0
            n_NIKalpha = 0
            while True : #Proteksi Input NIK
                NIK_baru = input("Masukkan NIK Pasien : ")
                
                for l in range(len(NIK_baru)): #Pengecekan apakah terdapat huruf di dalam NIK
                    if NIK_baru[l].isdigit() == True :
                        n_NIKnum += 1
                    elif NIK_baru[l].isalpha() == True :
                        n_NIKalpha += 1
                
                if n_NIKalpha > 0 :
                    print("NIK yang diinput mengandung huruf, silahkan coba lagi.")
                    n_NIKalpha = n_NIKnum = 0
                elif n_NIKnum != 16 :
                    print("Masukkan 16 digit NIK")
                    n_NIKalpha = n_NIKnum = 0
                else :
                    NIK_baru = int(NIK_baru)
                    break
            print(f'\n')

            #Input Jenis Kelamin
            while True : #Proteksi Input Jenis Kelamin
                gender_baru = str(input("Masukan Jenis Kelamin Pasien (Pria / Wanita): "))

                if gender_baru.lower() == 'pria' or gender_baru.lower() == 'wanita' :
                    break
                else :
                    print("Jenis Kelamin yang dimasukkan salah, silahkan coba lagi.")
            gender_baru = gender_baru.capitalize()
            print(f'\n')

            #Input Umur
            while True: #Proteksi Input Umur
                try :
                    umur_baru = int(input("Masukkan Umur Pasien : "))
                    break
                except :
                    print("Masukkan Umur yang Benar.")
            print(f'\n')

            #Input Alamat
            alamat_baru = str(input("Masukkan Alamat Pasien : ")).title()
            print(f'\n')

            #Input Pekerjaan
            pekerjaan_baru = str(input("Masukkan Pekerjaan Pasien : ")).title()
            print(f'\n')
            
            #Input Penyakit
            penyakit_baru = str(input("Masukkan Penyakit Pasien : ")).title()

            #Input Tanggal Registrasi
            tgl_regis = datetime.datetime.now()

            #Fungsi menambahkan data pasien baru ke dalam Data Utama
            daftarPasien.append({
                'id' : int(daftarPasien[len(daftarPasien)-1]['id'] + 1),
                'Nama' : nama_baru.title(),
                'NIK' : NIK_baru,
                'Jenis Kelamin' : gender_baru,
                'Umur' : umur_baru,
                'Alamat' : alamat_baru,
                'Pekerjaan' : pekerjaan_baru,
                'Penyakit' : penyakit_baru,
                'Tanggal Registrasi' : tgl_regis.strftime("%d %b %Y")
            })
            print(f"Data pasien atas nama {nama_baru} telah berhasil ditambahkan.\n")
            show_data()
        
        elif menu_2 == 2 :
            menu2_con = False
            main_menu()
            
#Menu 3
#Update Data Pasien
def menu3() :
    menu3_con = True
    while menu3_con :
        while True :
            print(f'''\nMenu Update Data Pasien
                1. Update Data Pasien yang ada
                2. Menu Utama\n
                ''')
            try : #Proteksi Inputan Menu
                menu_3 = int(input("Masukkan Pilihan Menu : "))
                print()
                if menu_3 in [1,2] :
                    break
                else :
                    print("Menu yang dimasukkan salah, silahkan coba lagi.")
            except :
                print("Menu yang dimasukkan salah, silahkan coba lagi.")
        print()

        if menu_3 == 1 :
            show_data()
            update = True
            while update :
                index_update = proteksi_id()                
                
                for k in range(len(daftarPasien)):
                    if index_update == daftarPasien[k]['id'] :
                        update2 = True
                        while update2 :
                            print(f"\nData Pasien : \n")
                            print(f"{daftarPasien[k]['id']}\t| {daftarPasien[k]['Nama']}   \t| {daftarPasien[k]['NIK']}\t| {daftarPasien[k]['Jenis Kelamin']}       \t| {daftarPasien[k]['Umur']}\t| {daftarPasien[k]['Alamat']}\t| {daftarPasien[k]['Pekerjaan']}     \t| {daftarPasien[k]['Penyakit']}\t| {daftarPasien[k]['Tanggal Registrasi']}\t|\n")
                            jawab = str(input("Apakah anda ingin meng-update data pasien? (Ya / Tidak) : "))
                            print()
                            if jawab.lower() == 'ya' :
                                print('''Pilihan Kolom yang Ingin Di-Update :
                                    1. Nama
                                    2. NIK
                                    3. Jenis Kelamin
                                    4. Umur
                                    5. Alamat
                                    6. Pekerjaan
                                    7. Penyakit
                                    ''')    
                                while True :
                                    try : #Proteksi Inputan Menu
                                        kolom_update = int(input("Masukkan kolom yang ingin di-update : "))
                                        print()
                                        if kolom_update in [1,2,3,4,5,6,7] :
                                            break
                                        else :
                                            print("Menu yang dimasukkan salah, silahkan coba lagi.")
                                    except :
                                        print("Menu yang dimasukkan salah, silahkan coba lagi.")
                                    
                                if kolom_update == 1 : #Update Nama    
                                    n_num = 0
                                    n_alpha = 0
                                    nama_update = False
                                    while True :
                                        nama_update = input("Masukkan Nama baru: ")
                                        for l in range(len(nama_update)): #Pengecekan apakah terdapat angka di dalam Nama
                                            if nama_update[l].isdigit() == True :
                                                n_num +=1
                                            elif nama_update[l].isalpha() == True :
                                                n_alpha +=1
                                        if n_num > 0 :
                                            print("Nama yang diinput mengandung angka, silahkan coba lagi.")
                                            n_num = 0
                                        elif n_num == 0 and n_alpha == 0 :
                                            print('Tidak ada Inputan, silahkan coba lagi.')
                                        else :
                                            nama_update = str(nama_update)
                                            daftarPasien[k]['Nama'] = nama_update.title()
                                            print(f"\n~Data berhasil diperbarui~\n")
                                            break

                                elif kolom_update == 2 : #Update NIK baru
                                    n_NIKnum = 0
                                    n_NIKalpha = 0
                                    NIK_update = False
                                    while True :
                                        NIK_update = str(input("Masukkan NIK baru : "))
                                        for l in range(len(NIK_update)): #Pengecekan apakah terdapat huruf di dalam NIK
                                            if NIK_update[l].isdigit() == True :
                                                n_NIKnum += 1
                                            elif NIK_update[l].isalpha() == True :
                                                n_NIKalpha += 1
                                        
                                        if n_NIKalpha > 0 :
                                            print("NIK yang diinput mengandung huruf, silahkan coba lagi.")
                                            n_NIKalpha = n_NIKnum = 0
                                        elif n_NIKnum != 16 :
                                            print("Masukkan 16 digit NIK")
                                            n_NIKalpha = n_NIKnum = 0
                                        else :
                                            NIK_update = int(NIK_update)
                                            daftarPasien[k]['NIK'] = NIK_update
                                            print(f"\n~Data berhasil diperbarui~\n")
                                            break
                                    print(f'\n')

                                elif kolom_update == 3 : #Update Jenis Kelamin Baru
                                    while True:
                                        try :
                                            gender_update = str(input("Masukkan Jenis Kelamin Baru : "))
                                            daftarPasien[k]['Jenis Kelamin'] = gender_update.capitalize()
                                            print(f"\n~Data berhasil diperbarui~\n")
                                            break
                                        except :
                                            print("Input salah, silahkan coba lagi.")

                                elif kolom_update == 4 : #Update Umur baru
                                    while True :
                                        try :
                                            umur_update = int(input("Masukkan Umur baru : "))
                                            daftarPasien[k]['Umur'] = umur_update
                                            print(f"\n~Data berhasil diperbarui~\n")
                                            break
                                        except :
                                            print("Input salah, silahkan coba lagi.")
                                        
                                elif kolom_update == 5 : #Update Alamat baru
                                    alamat_update = str(input("Masukkan Alamat baru : "))
                                    daftarPasien[k]['Alamat'] = alamat_update.title()
                                    print(f"\n~Data berhasil diperbarui~\n")

                                elif kolom_update == 6 : #Update Pekerjaan baru
                                    pekerjaan_update = str(input("Masukkan Pekerjaan baru : "))
                                    daftarPasien[k]['Pekerjaan'] = pekerjaan_update.title()
                                    print(f"\n~Data berhasil diperbarui~\n")

                                elif kolom_update == 7 : #Update Penyakit baru
                                    penyakit_update = str(input("Masukkan Penyakit baru : "))
                                    daftarPasien[k]['Penyakit'] = penyakit_update.title()
                                    print(f"\n~Data berhasil diperbarui~\n")

                                jawab2 = str(input("Apakah masih ingin meng-update Data Pasien? (Ya / Tidak) : "))
                                if jawab2.lower() == 'ya' :
                                    continue
                                elif jawab2.lower() == 'tidak' :
                                    update2 = False
                                    break
                                else :
                                    print("Masukkan input yang benar")

                            elif jawab.lower() == 'tidak' : 
                                break    

                            else :
                                print(f"Masukkan input yang benar\n")            

                        update = False
                        break
                        
        elif menu_3 == 2 :
            menu3_con = False
            main_menu()
            break

#Menu 4
#Menghapus Data Pasien
def menu4():
    menu4_con = True
    while menu4_con :
        while True :
            print(f'''\nMenu Hapus Data Pasien
                    1. Hapus Data Pasien
                    2. Menu Utama
                    ''')
            try : #Proteksi Inputan Menu
                menu_4 = int(input("Masukkan Pilihan Menu : "))

                if menu_4 in [1,2] :
                    break
                else :
                    print("Menu yang dimasukkan salah, silahkan coba lagi.")
            except :
                print("Menu yang dimasukkan salah, silahkan coba lagi.")
        print()

        if menu_4 == 1 :
            show_data()
            print()

            menu4_1_con = True
            while menu4_1_con :
                index_hapus = proteksi_id()

                for i in range(len(daftarPasien)) :
                    if index_hapus == daftarPasien[i]['id']:
                        menu4_conf = input(f"Apakah Anda yakin menghapus Data Pasien dengan nomor {index_hapus}? (Ya / Tidak) :")
                        if menu4_conf.lower() == 'ya' : 
                            del daftarPasien[i]
                            print(f"\nData Pasien dengan nomor {index_hapus} telah berhasil dihapus.\n")
                            show_data()
                            menu4_1_con = False
                            break
                            
                        elif menu4_conf.lower() == 'tidak' :
                            break

                        else :
                            print("Masukkan inputan yang benar.")   

        elif menu_4 == 2 :
            menu4_con = False
            main_menu()

#Menu 5
#Menu Data Obat
def menu5() :
    menu5_conf = True
    while menu5_conf :
        while True :
            print(f'''\nMenu Data Obat :
                1. Tampilkan Daftar Obat
                2. Menambah Daftar Obat
                3. Menu Utama
                ''')
            try : #Proteksi Inputan Menu
                menu_5 = int(input("Masukkan Pilihan Menu : "))
                print()
                if menu_5 in [1,2,3] :
                    break
                else :
                    print("Menu yang dimasukkan salah, silahkan coba lagi.")
            except :
                print("Menu yang dimasukkan salah, silahkan coba lagi.")
        print()

        if menu_5 == 1 : #Menampilkan daftar obat
            show_data_obat()
        
        elif menu_5 == 2 : #Menambah data obat
            jenis_obat = str(input("Masukkan Jenis Obat : "))
            nama_obat = str(input("Masukkan Nama Obat : "))
            while True :
                try : 
                    stok_obat = int(input("Masukkan Stok Obat : "))
                    break
                except :
                    print("Masukkan stok obat yang benar.")
            while True :
                try :    
                    harga_obat = float(input("Masukkan Harga Obat : "))
                    break
                except :
                    print("Masukkan harga obat yang benar.")

            daftar_obat.append({'Nomor' : daftar_obat[len(daftar_obat)-1]['Nomor'] + 1,
                            'Jenis Obat' : jenis_obat.title(),
                            'Nama Obat' : nama_obat.title(),
                            'Stok' : stok_obat,
                            'Harga Obat' : harga_obat})
            print(f"\nJenis Obat baru berhasil ditambahkan.")

        elif menu_5 == 3 :
            menu5_conf = False
            main_menu()

#Menu 6
#Menu Pembelian Obat
def menu6() :
    menu6_conf = True
    while menu6_conf :
        while True :
            print(f'''\nMenu Pembelian Obat : 
                1. Pembelian Obat untuk Pasien
                2. Tampilkan Daftar Obat yang Dikonsumsi Pasien
                3. Pembayaran Tagihan Obat
                4. Menu Utama
                ''')
            try : #Proteksi Inputan Menu
                menu_6 = int(input("Masukkan Pilihan Menu : "))
                print()
                if menu_6 in [1,2,3,4] :
                    break
                else :
                    print("Menu yang dimasukkan salah, silahkan coba lagi.")
            except :
                print("Menu yang dimasukkan salah, silahkan coba lagi.")

        if menu_6 == 1 :
            show_data()
            menu_6_con = True
            while menu_6_con :
                kons_obat = proteksi_id()

                for i in range(len(daftarPasien)) :
                    if kons_obat == daftarPasien[i]['id'] :
                        namaPasien(kons_obat)
                        show_data_obat()
                        
                        jawaban = True
                        while jawaban :
                            #Cek Obat
                            while True :
                                try :
                                    pilih_obat = int(input(f"\nPilih Obat yang ingin dikonsumsi oleh {namaPasien(kons_obat)}: "))    
                                    for i in range(len(daftar_obat)) :
                                        if pilih_obat == daftar_obat[i]['Nomor'] :
                                            #Cek Ketersediaan Obat
                                            sedia_obat = True
                                            while sedia_obat :
                                                try :
                                                    jumlah_obat = int(input("Masukan Jumlah Obat yang ingin dibeli : "))
                                                    if jumlah_obat <= daftar_obat[pilih_obat]['Stok'] :
                                                        sedia_obat = False
                                                    else :
                                                        print(f"Stock tidak cukup, stok {daftar_obat[pilih_obat]['Nama Obat']} tinggal {daftar_obat[pilih_obat]['Stok']}")
                                                except : 
                                                    print('Input salah, silahkan coba lagi.')
                                            
                                            print()
                                        else:
                                            pass
                                    break
                                except : 
                                    print('Input salah, silahkan coba lagi.')

                            #Memasukkan obat ke dalam keranjang belanja
                            list_obat = [namaPasien(kons_obat), daftar_obat[pilih_obat]['Jenis Obat'], daftar_obat[pilih_obat]['Nama Obat'], jumlah_obat, daftar_obat[pilih_obat]['Harga']]
                            konsumsi_obat.append(list_obat)

                            #Memasukkan data obat ke dalam data pasien
                            cart_obat(kons_obat)

                            #Update Stok Obat
                            for j in range(len(daftar_obat)) :
                                if daftar_obat[j]['Nomor'] == pilih_obat :
                                    daftar_obat[j]['Stok'] -= jumlah_obat

                            jawab = str(input(f"\nMau beli yang lain? (ya/tidak) : "))
                            
                            while True :
                                if jawab.lower() == 'tidak': 
                                    jawaban = False
                                    menu6()
                                    break
                                elif jawab.lower() == 'ya':
                                    jawaban = True
                                    break
                                else :
                                    print("Masukkan jawaban ya / tidak.")
                                    jawab = str(input("Mau beli yang lain? (ya/tidak) : "))
            
        elif menu_6 == 2 : #Menampilkan Daftar Obat Yang dikonsumsi Pasien
            show_data()
            menu6_2_con = True
            while menu6_2_con :
                noPasien = proteksi_id()
                for i in range(len(daftarPasien)) :
                    if noPasien == daftarPasien[i]['id']:
                        print(f'\nDaftar Obat yang dikonsumsi :\n')
                        cart_obat(noPasien)
                        menu6_2_con = False
                        break
                else :
                    print(f"Data pasien dengan nomor {noPasien} tidak ditemukan, silahkan coba lagi.")
                
        elif menu_6 == 3 : #Pembayaran Tagihan Obat
            show_data()
            menu6_3_con = True
            obatpasien_none = False
            while menu6_3_con :
                no_Pasien = proteksi_id()

                for i in range(len(daftarPasien)) :
                    if no_Pasien == daftarPasien[i]['id']:

                        if len(konsumsi_obat) == 0 :
                            obatpasien_none = True
                            break

                        else :                            
                            #Detail Belanja Obat
                            total_belanja = 0
                            for j in range(len(konsumsi_obat)):
                                if namaPasien(no_Pasien) == konsumsi_obat[j][0]:
                                    print(f'\nDaftar Obat yang dikonsumsi :\n')
                                    cart_obat(no_Pasien)
                                    harga_total_obat = konsumsi_obat[j][3] * konsumsi_obat[j][4]
                                    total_belanja += harga_total_obat
                                    print(f"\n{konsumsi_obat[j][2]}\t\t: {konsumsi_obat[j][3]} x {konsumsi_obat[j][4]}")
                                    print(f"\nTotal Belanja untuk pasien {namaPasien(no_Pasien)} sebesar {total_belanja}\n")
                                    
                                    #Pembayaran
                                    while True : 
                                        jumlah_uang = float(input("Masukkan Jumlah Uang : "))
                                        print('\n')

                                        if jumlah_uang < total_belanja :
                                            print(f"Uang anda kurang sebesar : {total_belanja - jumlah_uang}\n")
                                        else :
                                            kembalian = jumlah_uang - total_belanja
                                            print("Terima kasih")
                                            print(f"\nUang kembalian anda : {kembalian}")
                                            menu6_3_con = False
                                            break
                                    break
                                else :
                                    obatpasien_none = True
                        break

                if obatpasien_none == True :
                    print(f"Pasien dengan nomor {no_Pasien} belum membeli obat.")
                    menu6_3_con = False
                    menu6()

            main_menu()
            
        elif menu_6 == 4 : #Menu Utama
            menu6_conf = False
            main_menu()

##Fungsi Tambahan
#Fungsi Menampilkan Data Pasien
def show_data() :
    print("Data Pasien Rumah Sakit")
    headersP = daftarPasien[0].keys()
    dataP = [j.values() for j in daftarPasien]
    print(tabulate(dataP,headersP, tablefmt="grid"))

#Fungsi Sort
def sort(sorting, reverse = False):
    list = sorted(daftarPasien, key=itemgetter(sorting), reverse = reverse)
    headersP = list[0].keys()
    dataP = [j.values() for j in list]
    print(tabulate(dataP,headersP, tablefmt="grid"))

#Fungsi Pemanggil Nama Pasien
def namaPasien(no_pasien) :
    for i in range(len(daftarPasien)) :
        if no_pasien == daftarPasien[i]['id'] :
            return daftarPasien[i]['Nama']

#Fungsi Menampilkan Cart Obat
def cart_obat(no_pasien) :
    print(f"Nama Pasien\t| Jenis Obat\t| Nama Obat\t\t| Jumlah\t| Harga\t|")
    for j in range(len(konsumsi_obat)):
        if namaPasien(no_pasien) == konsumsi_obat[j][0]:
            print(f'{konsumsi_obat[j][0]}\t| {konsumsi_obat[j][1]} \t| {konsumsi_obat[j][2]}\t\t| {konsumsi_obat[j][3]}\t\t| {konsumsi_obat[j][4]}\t|')

#Fungsi Menampilkan Data Obat
def show_data_obat() :
    headers = daftar_obat[0].keys()
    data = [i.values() for i in daftar_obat]
    print(tabulate(data,headers, tablefmt="grid"))

#Fungsi proteksi input id pasien
def proteksi_id():
    while True :
        try : #Proteksi pencarian pasien
            id = (input(f"\nPilih Nomor Pasien : "))
            if len(id) == 0 :
                print("Tidak ada input, silahkan coba lagi.")
            else :
                for i in range(len(daftarPasien)) :
                    id = int(id)
                    if id == daftarPasien[i]['id'] :
                        return id
            break
        except :
            print(f"Nomor pasien mengandung huruf, silahkan coba lagi.")

main_menu() #Menjalankan Program 