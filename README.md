# **Capstone Project 1 Purwadhika** 

### By Hafidh Diya Ulhaqi Dewantoro

## **DATABASE PASIEN RUMAH SAKIT**
Sebagai database awal, saya mendefinisikan 2 data pasien dengan data id Pasien, Nama, NIK, Jenis Kelamin, Umur, Alamat, Pekerjaan, dan Penyakit. Untuk unique value, saya memilih id Pasien karena bisa digunakan sebagai identitas pasien yang nantinya digunakan untuk pemanggilan data sesuai nomor id nya.

<img width="801" alt="Screenshot 2023-12-11 at 20 39 45" src="https://github.com/hafidhdiya/Capstone-Project-1---Purwadhika/assets/89533026/c345b5a5-e8a0-45e7-b47d-4b6a3bb027cd">

Seluruh program code, saya definisikan dengan function def agar terlihat lebih rapi dan efisien. Terdapat function def tambahan agar memudahkan dalam pemanggilan fungsi yang berulang.

<img width="562" alt="Screenshot 2023-12-11 at 20 40 40" src="https://github.com/hafidhdiya/Capstone-Project-1---Purwadhika/assets/89533026/5324dfb9-355f-41c6-8160-c1a5a7ef2d0d">

Program yang dibuat terdiri dari 7 menu utama, yaitu:

<img width="477" alt="Screenshot 2023-12-11 at 20 40 57" src="https://github.com/hafidhdiya/Capstone-Project-1---Purwadhika/assets/89533026/9bf7e7a3-25ac-4ca0-8d9f-f42b9cd0b4d6">

### Menu 1 : Menampilkan Data Pasien

<img width="612" alt="Screenshot 2023-12-11 at 20 41 27" src="https://github.com/hafidhdiya/Capstone-Project-1---Purwadhika/assets/89533026/23b2e797-27af-423f-ac8d-9c883ef3548d">

   Pada menu ini, terdapat 4 sub menu, yaitu:
   
   a. Data Seluruh Pasien
   
       User dapat memilih menu ini untuk menampilkan seluruh data pasien yang ada pada suatu tabel.
       
   b. Data Pasien berdasarkan Nomor NIK
   
       User dapat memilih menu ini untuk menampilkan data pasien tertentu dengan mencarinya melalui Nomor NIK.
   
   c. Menu Sorting
       
       User dapat memilih menu ini untuk mengurutkan data seluruh pasien berdasarkan:
       
       - Nama (A - Z)

           Mengurutkan Data Pasien berdasarkan Nama A - Z
           
       - Nama (Z - A)

           Mengurutkan Data Pasien berdasarkan Nama Z - A
       
       - Usia (Muda - Tua)

           Mengurutkan Data Pasien berdasarkan Usia Muda - Tua
       
       - Usia (Tua - Muda)

           Mengurutkan Data Pasien berdasarkan Usia Tua - Muda
       
       - Tanggal Registrasi

           Mengurutkan Data Pasien berdasarkan Tanggal Registrasi
   
   d. Kembali ke Main Menu

       User memilih menu ini untuk kembali ke menu utama.
   
### Menu 2 : Menambah Data Pasien

<img width="720" alt="Screenshot 2023-12-11 at 20 41 45" src="https://github.com/hafidhdiya/Capstone-Project-1---Purwadhika/assets/89533026/cdb779ad-ff92-4eed-9414-ed3d84017ef8">

   Pada menu ini, terdapat 2 sub menu, yaitu:
   
   a. Menambah Data Pasien baru

       User dapat memilih menu ini untuk menambahkan data pasien baru.
   
   b. Kembali ke Main Menu

       User memilih menu ini untuk kembali ke menu utama
   
### Menu 3 : Memperbarui Data Pasien

<img width="617" alt="Screenshot 2023-12-11 at 20 42 03" src="https://github.com/hafidhdiya/Capstone-Project-1---Purwadhika/assets/89533026/9c65cc6a-1c27-425b-9369-4344606e3d8b">

   Pada menu ini, terdapat 2 sub menu, yaitu:
   
   a. Meng-update Data Pasien

       User dapat meng-update data pasien berdasarkan Nama, NIK, Jenis Kelamin, Umur, Alamat, Pekerjaan, dan Penyakit.
   
   b. Kembali ke Main Menu

       User memilih menu ini untuk kembali ke menu utama
   
### Menu 4 : Menghapus Data Pasien

<img width="618" alt="Screenshot 2023-12-11 at 20 42 20" src="https://github.com/hafidhdiya/Capstone-Project-1---Purwadhika/assets/89533026/e8a29c9b-2ba2-449d-b4fb-646119f35d25">

   Pada menu ini terdapat 2 sub menu, yaitu:
   
   a. Menghapus Data Pasien tertentu

       User dapat memilih menu ini untuk menghapus data pasien.
   
   b. Kembali ke Main Menu

       User memilih menu ini untuk kembali ke menu utama
   
### Menu 5 : Menu Daftar Obat

<img width="596" alt="Screenshot 2023-12-11 at 20 42 37" src="https://github.com/hafidhdiya/Capstone-Project-1---Purwadhika/assets/89533026/e1336ad4-ec60-4e16-b91f-79333a8f4870">

   Pada menu ini, terdapat 3 sub menu, yaitu:
   
   a. Menampilkan Daftar Obat

       User dapat memilih menu ini untuk menampilkan daftar obat yang tersedia.
   
   b. Menambah Data Obat

       User dapat memilih menu ini untuk menambah data obat, seperti Jenis Obat, Nama Obat, Stok, dan Harga.
   
   c. Kembali ke Main Menu

       User memilih menu ini untuk kembali ke menu utama
       
### Menu 6 : Menu Pembelian Obat

<img width="584" alt="Screenshot 2023-12-11 at 20 42 49" src="https://github.com/hafidhdiya/Capstone-Project-1---Purwadhika/assets/89533026/abc40c6c-0978-4b69-99fe-226e35da0e4a">

   Pada menu ini, terdapat 4 sub menu, yaitu:
   
   a. Pembelian obat untuk pasien tertentu

       Menu ini diperuntukan untuk user agar bisa membeli obat berdasarkan pasien tertentu dengan meng-input Nomor index obat dan jumlah yang ingin dibeli.
   
   b. Menampilkan Daftar Obat yang dibeli oleh Pasien

       Menu ini berfungsi untuk menampilkan daftar obat yang telah dibeli oleh pasien pada menu sebelumnya.
   
   c. Pembayaran Tagihan Obat

       Menu ini berfungsi untuk melakukan pembayaran sesuai dengan jumlah obat yang telah dibeli.
   
   d. Kembali ke Main Menu

       User memilih menu ini untuk kembali ke menu utama
   
### Menu 7 : Exit Program

    Menu ini berfungsi untuk keluar dari program.


    **Note : Semua input sudah diproteksi apabila harus diisi integer maka akan ada notifikasi ketika tidak diisi dengan integer**
