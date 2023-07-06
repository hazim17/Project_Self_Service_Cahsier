# Import libraries
from datetime import date
import pandas as pd


class C6_trx:
    """
    Class untuk melakukan transaksi self service cashier.

    Terdapat method:
        - constructor (__init__): Melakukan looping untuk memilih method yang
                                  user pilih untuk melakukan tindakan yang
                                  sesuai dilakukan
        - add_new_item: Menambahkan nama, harga, dan qty baru
        - update_nama: Mengganti nama pada data yang ada (berdasarkan nama)
        - update_harga: Mengganti harga pada data yang ada (berdasarkan nama)
        - update_qty: Mengganti qty pada data yang ada (berdasarkan nama)
        - delete_row_item: Menghapus satu row data (nama, harga, qty)
                           berdasarkan nama yang sama
        - reset: Hapus semua data pada id transaksi  yang sedang digunakan
        - check_order: Mengecek apakah semua data sudah benar
                       sesuai data produk (database_pdct)
        - total_price: Menghitung total harga yang sudah diberi diskon
                       (jika dapat diskon)
        - salah_ketik_order: Mengembalikan tulisan salah ketik command dan akan
                             kembali memberikan input untuk masukkan
                             command baru
    """

    def __init__(self, id_trx, c6_dict, database_pdct,
                 command, num = 1, n = 1, is_ok = "not"):
        """
        Parameter:
            - id_trx (str): id transaksi
            - c6_dict: dictionary untuk menyimpan data transaksi
            - database_pdct: Database product yang kita miliki
            - command: perintah yang nantinya dijalankan
                       (add_new_item, update_name, delete_row_item, reset, dll)
            - num = untuk iterasi while loop di method __init__ ini
            - n = untuk membuat id row di setiap transaksi
            - is_ok = untuk validasi apakah saat di command total_price bisa
                      keluar harga atau masih ada data yang salah
        """
        self.id_trx = id_trx
        self.c6_dict = c6_dict
        self.database_pdct = database_pdct
        self.command = command
        self.num = num
        self.n = n
        self.is_ok = "not"

        while self.num == 1:
            try:
                if self.command == "add_new_item":
                    self.add_item()
                    self.command = input("masukkan command: ")
                elif self.command == "update_nama":
                    self.update_item_name()
                    self.command = input("masukkan command: ")
                elif self.command == "update_harga":
                    self.update_item_harga()
                    self.command = input("masukkan command: ")
                elif self.command == "update_qty":
                    self.update_item_qty()
                    self.command = input("masukkan command: ")
                elif self.command == "delete_row_item":
                    self.delete_item()
                    self.command = input("masukkan command: ")
                elif self.command == "reset":
                    self.reset_transaction()
                    self.command = input("masukkan command: ")
                elif self.command == "check_order":
                    self.check_order()
                    self.command = input("masukkan command: ")
                elif self.command == "total_price":
                    if self.is_ok == "yes":
                        self.check_order()
                        self.total_price()
                        self.num = 3
                    else:
                        self.check_order()
                        if self.is_ok == "yes":
                            self.total_price()
                            self.num = 3
                        else:
                            self.command = input("masukkan command: ")
                elif self.command == "exit":
                    self.num = 3
                    print("Terima kasih telah berbelanja di CarreSix.")
                else:
                    self.salah_ketik_order()
                    self.command = input("masukkan command: ")

            except Exception as error:
                print("An error occurred:", type(error).__name__)

    def add_item(self):
        """
        method untuk mengimplementasikan add item
        Menambahkan nama, harga, dan qty baru
        """

        try:
            # Mengecek apakah id transaksi ada di c6_dict
            if self.id_trx in list(self.c6_dict.keys()):
                # Meminta input dari user untuk nama, harga dan jumlah barang
                nama_prod = input("Masukkan nama barang: ")
                harga_prod = input("Masukkan harga barang tersebut: ")
                jumlah_prod = input("Masukkan jumlah barang yang ingin dibeli: ")
                # Menambahkan hasil input dari user ke dictionary
                self.c6_dict[self.id_trx].update({self.n: [nama_prod,
                                                          jumlah_prod,
                                                          harga_prod]})
                # Iterasi untuk key pada c6_dict dictionary
                self.n += 1
                # Lihat hasil dari c6_dict setelah ditambah data
                print(self.c6_dict[self.id_trx])
                print("-------------------")

            else:
                print("ID Transaksi Tidak Ditemukan")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def update_item_name(self):
        """
        method untuk mengupdate nama item di c6_dict
        Mengganti nama pada data yang ada (berdasarkan nama)
        """

        try:
            # Mengecek apakah id transaksi ada di c6_dict
            if self.id_trx in list(self.c6_dict.keys()):
                # Meminta input dari user untuk nama produk (baru dan update)
                nama_prod_now = input("Masukkan nama barang yang akan di update: ")
                nama_prod_new = input("Masukkan nama barang yang benar: ")

                # Iterasi untuk update nama produk
                for key, val in self.c6_dict[self.id_trx].items():
                    if nama_prod_now == val[0]:
                        self.c6_dict[self.id_trx][key][0] = nama_prod_new
                    else:
                        pass

                # Lihat hasil dari c6_dict setelah diupdate nama
                print(self.c6_dict[self.id_trx])
                print("-------------------")

            else:
                print("ID Transaksi Tidak Ditemukan")
                
        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def update_item_harga(self):
        """
        method to implement an update item price di c6_dict
        Mengganti harga pada data yang ada (berdasarkan nama)
        """
        
        try:
            # Mengecek apakah id transaksi ada di c6_dict
            if self.id_trx in list(self.c6_dict.keys()):
                # Meminta input dari user untuk nama produk lama dan harga baru nya
                nama_prod_now = input("Masukkan nama barang yang akan di update: ")
                harga_prod_new = input("Masukkan harga barang yang benar: ")

                # Iterasi untuk update harga produk
                for key, val in self.c6_dict[self.id_trx].items():
                    if nama_prod_now == val[0]:
                        self.c6_dict[self.id_trx][key][2] = harga_prod_new
                    else:
                        pass

                # Lihat hasil dari c6_dict setelah diupdate harga
                print(self.c6_dict[self.id_trx])
                print("-------------------")

            else:
                print("ID Transaksi Tidak Ditemukan")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def update_item_qty(self):
        """
        method to implement an update item quantity di c6_dict
        Mengganti qty pada data yang ada (berdasarkan nama)
        """
 
        try:
            # Mengecek apakah id transaksi ada di c6_dict
            if self.id_trx in list(self.c6_dict.keys()):
                nama_prod_now = input("Masukkan nama barang yang akan di update: ")
                qty_prod_new = input("Masukkan quantity barang yang benar: ")

                # Iterasi untuk update quantity produk
                for key, val in self.c6_dict[self.id_trx].items():
                    if nama_prod_now == val[0]:
                        self.c6_dict[self.id_trx][key][1] = qty_prod_new
                    else:
                        pass

                # Lihat hasil dari c6_dict setelah diupdate quantity
                print(self.c6_dict[self.id_trx])
                print("-------------------")

            else:
                print("ID Transaksi Tidak Ditemukan")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def delete_item(self):
        """
        method to implement delete items
        Menghapus satu row data (nama, harga, qty) berdasarkan nama yang sama
        """

        try:
            # Mengecek apakah id transaksi ada di c6_dict
            if self.id_trx in list(self.c6_dict.keys()):
                # Meminta user memasukkan barang yang ingin di hapus
                nama_prod_now = input("Masukkan nama barang yang akan di hapus data nya: ")

                # Menghapus data yang sesuai
                for key, val in self.c6_dict[self.id_trx].items():
                    if nama_prod_now == val[0]:
                        self.c6_dict[self.id_trx].update({key: ['data dihapus', 0, 0]})
                    else:
                        pass

                # Lihat hasil dari c6_dict setelah didelete item
                print(self.c6_dict[self.id_trx])
                print("-------------------")

            else:
                print("ID Transaksi Tidak Ditemukan")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def reset_transaction(self):
        """
        method to implement reset transaction
        Hapus semua data pada id transaksi yang sedang digunakan
        """

        try:
            # Mengecek apakah id transaksi ada di c6_dict
            if self.id_trx in list(self.c6_dict.keys()):
                # Memastikan user ingin menghapus semua data transaksi
                user_yakin = input("Anda yakin ingin menghapus semua data?, ketik ya/yes: ")

                # Reset Transaction
                if user_yakin == "yes" or user_yakin == "ya":
                    self.c6_dict[self.id_trx].clear()
                else:
                    pass

                #  Lihat hasil dari c6_dict setelah reset
                print(self.c6_dict[self.id_trx])
                print("-------------------")

            else:
                print("ID Transaksi Tidak Ditemukan")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def check_order(self):
        """
        method to implement a check order
        Mengecek apakah semua data sudah benar
        sesuai database produk (database_pdct)
        """

        try:
            # Mengecek apakah id transaksi ada di c6_dict
            if self.id_trx in list(self.c6_dict.keys()):

                # Iterasi untuk cek apakah transaksi sudah sesuai
                for key, val in self.c6_dict[self.id_trx].items():
                    # Jika nama produk di c6_dict tidak ada di database produk
                    if self.c6_dict[self.id_trx][key][0] not in list(self.database_pdct.keys()):
                        print(f"Produk '{self.c6_dict[self.id_trx][key][0]}' tidak ada dalam database, mohon periksa kembali apakah ada kesalahan dalam penulisan.")
                        self.is_ok = "not"

                    # Jika nama produk di c6_dict ada di database produk
                    elif self.c6_dict[self.id_trx][key][0] in list(self.database_pdct.keys()):
                        # Jika Harga salah
                        if int(self.c6_dict[self.id_trx][key][2]) != int(self.database_pdct[self.c6_dict[self.id_trx][key][0]]):
                            print(f"Produk '{self.c6_dict[self.id_trx][key][0]}' memiliki harga yang salah, mohon periksa kembali.")
                            self.is_ok = "not"

                        # Jika semua benar
                        else:
                            print('Pesanan Sudah benar')
                            self.is_ok = "yes"

                # Return Hasil Tabel yang akan di cek
                df = pd.DataFrame.from_dict(self.c6_dict[self.id_trx],
                                        orient='index',
                                        columns=['Nama Item',
                                                'Jumlah Item',
                                                'Harga Item'])
                df['Total Harga'] = df['Jumlah Item'].astype(int) * df['Harga Item'].astype(int)
                print(df)
                print("-------------------")

            else:
                print("ID Transaksi Tidak Ditemukan")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def total_price(self):
        """
        method untuk menghitung total harga yang harus di bayar (termasuk diskon)
        """

        try:
            # Mengecek apakah id transaksi ada di c6_dict
            if self.id_trx in list(self.c6_dict.keys()):
                df = pd.DataFrame.from_dict(self.c6_dict[self.id_trx],
                                            orient='index',
                                            columns=['Nama Item',
                                                    'Jumlah Item',
                                                    'Harga Item'])
                df['Total Harga'] = df['Jumlah Item'].astype(int) * df['Harga Item'].astype(int)

                # Menghitung total diskon sesuai total belanja
                if df['Total Harga'].sum() > 200000:
                    total_belanja = df['Total Harga'].sum() - (df['Total Harga'].sum() * 0.05)
                    print(f"Total belanjaan kamu sebesar Rp{total_belanja:,}. Silahkan di bayar.")

                elif df['Total Harga'].sum() > 300000:
                    total_belanja = df['Total Harga'].sum() - (df['Total Harga'].sum() * 0.08)
                    print(f"Total belanjaan kamu sebesar Rp{total_belanja:,}. Silahkan di bayar.")

                elif df['Total Harga'].sum() > 500000:
                    total_belanja = df['Total Harga'].sum() - (df['Total Harga'].sum() * 0.1)
                    print(f"Total belanjaan kamu sebesar Rp{total_belanja:,}. Silahkan di bayar.")

                else:
                    total_belanja = df['Total Harga'].sum()
                    print(f"Total belanjaan kamu sebesar Rp{total_belanja:,}. Silahkan di bayar.")

            else:
                print("ID Transaksi Tidak Ditemukan")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

    def salah_ketik_order(self):
        """
        method jika user salah tulis command
        Menembalikan tulisan salah ketik command dan akan
        kembali memberikan input untuk masukkan command baru
        """

        try:
            # Mengecek apakah id transaksi ada di c6_dict
            if self.id_trx in list(self.c6_dict.keys()):
                df = pd.DataFrame.from_dict(self.c6_dict[self.id_trx],
                                            orient='index',
                                            columns=['Nama Item',
                                                    'Jumlah Item',
                                                    'Harga Item'])
                df['Total Harga'] = df['Jumlah Item'].astype(int) * df['Harga Item'].astype(int)
                print(df)

                # Memberikan Response kepada user
                print("Command yang dimasukkan tidak ada / salah. Mohon masukkan command dengan benar.")
                print("-------------------")

            else:
                print("ID Transaksi Tidak Ditemukan")

        except Exception as error:
            print("An error occurred:", type(error).__name__)

