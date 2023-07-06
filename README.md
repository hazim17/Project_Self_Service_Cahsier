# Project Self Service Cahsier

## **Problem:**
- Andi pemilik supermarket di salah satu kota di Indonesia ingin membuat sistem kasir self-service supaya customer di luar kota bisa tetap berbelanja di supermarketnya. Karena nya Andi memerlukan program yang bisa melakukan kegiatan tersebut.


## **Goals**
- Menciptakan CRUD program self cashier sesuai dengan requirements yang diminta (add item, update nama/harga/quantity, delete row, reset, check order dan total harga belanja)


## **Objectives**
- Membuat Flow chart untuk program nya
- Membuat CRUD program dengan alur yang jelas dan mudah dipahami.
- Program dibuat dalam sistem modular, clean code serta memiliki try-error dalam penggunaan branching


## **Flow Chart**
<p align="center">
<img src="Flow Chart self cashier project - White BG (Use This).png" alt="flow_chart" >
</p>
Gambar 1. Flow Chart

### Penjelasan Flow Chart:
Dalam project ini di asumsikan nama supermarket nya adalah CarreSix (C6)
1. Customer ingin berbelanja di CarreSix. Sehingga customer ketik Transaction() [customer membuat object]. object tersebut bisa langsung di tulis atau dimasukkan dalam variabel
2. Customer menjawab apakah ingin bertransaksi. Jika ya/yes, maka akan eksekusi ke selanjutnya. Jika mengetik yang lain maka program selesai.
3. Transaction id secara otomatis terbentuk. Kemudian pilihan yang customer bisa pilih keluar:
Berikutnya:
```
 - Ketik 'add_new_item': untuk memasukkan nama, quantitas dan harga produk
 - Ketik 'update_nama': untuk update nama produk, jika ada kesalahan
 - Ketik 'update_qty': untuk update quantitas produk, jika ada kesalahan
 - Ketik 'update_harga': untuk update harga produk, jika ada kesalahan
 - ketik 'delete_row_item': untuk hapus satu row data
 - ketik 'reset': untuk hapus semua data
 - ketik 'check_order': untuk checkout
 - ketik 'total_price': untuk melihat harga dan membayar
 - ketik 'exit': untuk keluar tanpa menyimpan apapun
```
4. kemudian akan muncul kotak untuk menginput method yang akan dilakukan **(kotak inputan)** dengan tulisan "Masukkan Command"
5. customer memasukkan method yang ingin dilakukan.
```
 - 'add_new_item': customer memasukkan nama, harga dan quantity produk yang akan dibeli
 - 'update_nama': customer memasukkan nama yang dari produk yang ingin diubah dan masukkan nama baru
 - 'update_qty': customer memasukkan nama dari prouk yang quantity nya ingin diubah, lalu memasukkan quantity baru
 - 'update_harga': customer memasukkan nama dari produk yang harga nya ingin diubah, lalu memasukkan harga yang baru
 - 'delete_row_item': customer memasukkan nama produk yang ingin dihapus data nya
 - 'reset': customer bisa ketik ya/yes jika ingin menghapus semua data transaksi pada id transaksi yang sedang berjalan. Jika ketik yang lain, program akan kembali ke point 4 (Kotak inputan masukkan command)
 - 'check_order': untuk checkout brang yang dipilih apakah sudah sesuai nama dan harganya dengan database yang ada
 - 'total_price': untuk melihat harga dan membayar
 - 'exit': untuk keluar tanpa menyimpan apapun
```
Secara umum, semua metode di atas (kecuali total_price dan exit) akan kembali ke kotak inputan "Masukkan Command" jika telah selesai memasukkan nilai pada command tersebut.
6. Jika memilih 'total_price' atau 'exit', maka program akan berhenti dan mengeluarkan output yang sesuai. Jika 'total_price' akan mengeluarkan harga yang harus dibayarkan. Jika 'exit' tidak mengeluarkan apapun.


## **Test Case**
1. Test 1
Customer ingin menambahkan dua item baru menggunakan method add_item() [*pada projek ini yaitu 'add_new_item'*]. item yang ditambahkan adalah sebagai berikut:

- Nama item: Ayam Goreng, Qty: 2 dan harga per item: 20000
- Nama item: Pasta Gigi, Qty: 3 dan harga per item: 15000

Hasil: 
<p align="center">
<img src="/hasil_test_case/test_1.png" alt="test_1">
</p>

2. Test 2
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan. Maka customer menggunakan method delete_item() [*pada projek ini yaitu 'delete_row_item'*] untuk menghapus item. Item yang ingin dihapus adalah Pasta gigi.
 
Hasil: 
<p align="center">
<img src="/hasil_test_case/test_2.png" alt="test_2">
</p>

3. Test 3
Ternyata setelah dipikir-pikir Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu-sat, maka Customer cukup menggunakan method reset_transaction() [*pada projek ini yaitu 'reset'*] untuk menghapus semua item yang sudah ditambahkan.

Hasil: 
<p align="center">
<img src="/hasil_test_case/test_3.png" alt="test_3" >
</p>

4. Test 4
Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.

Hasil: 
<p align="center">
<img src="/hasil_test_case/test_41.png" alt="test_41">
</p>
<p align="center">
<img src="/hasil_test_case/test_42.png" alt="test_42">
</p>


## **This Repository Organzation**
```
_
|── Flow Chart self cashier project - White BG (Use This).png       
                            : gambar flow chart program yang dijalankan

├── main_demonstrasi.ipynb                 
                            : Berisi Code untuk eksekusi module transaction serta Demonstrasi Test Case dan hasilnya
├── module_transaction.py   : file module yang berisi class C6_trx, di dalamnya terdapat method-method untuk melakukan transaksi. Seperti add item, update, delete dan check order.
├── Project Self Service Cashier.ipynb       
                            : code keseluruhan program dalam 1 file ipynb
└── README.md               : File Readme
```

Muhammad Hazim M

Pacmann - Analystics & Data Science
Batch 14
