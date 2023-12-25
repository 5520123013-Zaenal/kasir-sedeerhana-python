print("="*70)
print("          S E L A M A T   D A T A N G   DI   W A R K O P         ")
print("="*70)         
n = str(input("kode kasir : "))
while (n !="zero"):
    print("silakan input kode yang benar!")
    n = str(input("kode kasir:"))
while (n =="zero"):
    print("="*63)
    print("                   M E N U   K A S I R             ")
    print("="*63)

    Open_Menu = input("Apakah ingin masuk ke menu utama kasir?(Y/N)")
    if Open_Menu == "N":
        print("Keluar dari menu utama kasir")
        break
    elif Open_Menu == "Y":
        #menu makanan 
        List_Makanan = ['1. bebek goreng Rp.25000','2. steak Rp.25000','3. ayam geprek Rp.10000',
                        '4. nila bakar / goreng Rp.25000','5. nasi goreng udang Rp.20000','6. soto banjar Rp.17000','7. ayam goreng lalapan Rp.15000']
        #menu minuman
        List_minuman = ['8. coconut coffe Rp.20000','9.  caramel latte Rp.18000','10. strawberry choco Rp.18000',
                        '11. americano moderen Rp.20000','12. soda gembira Rp.15000','13. jus alpukat Rp.15000','14. es buah Rp.17000',
                        '15. es kelapa Rp.15000','16. black tea Rp.15000','17. jus mangga Rp.15000']
        #stok menu restoran
        Stok_makanan = [100, 100, 100, 100, 100, 100, 100 ]
        Stok_minuman = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

        harga_makanan = 0
        harga_minuman = 0     

        struk =" "         
        
       #cetak menu makanan 
        print("="*63)
        print("                    M E N U  M A K A N A N                  ")
        print("="*63)
        for Makanan in List_Makanan:
            print(' ',Makanan)

        #cetak menu minuman
        print("="*63)
        print("                    M E N U  M I N U M A N                  ")
        print("="*63)
        for Minuman in List_minuman:
            print(' ',Minuman)
        print("="*63)

        def hitung_harga_makanan(menu_makanan, A):
            global Stok_makanan
            Stok_makanan[int(menu_makanan) - 1] = Stok_makanan[int(menu_makanan) - 1] - A
            if (Stok_makanan[int(menu_makanan) - 1] <= 0):
                CRED = '\033[91m'
                CEND = '\033[0m'
                print(CRED + "Stok tidak cukup" + CEND)
                Stok_makanan[int(menu_makanan) - 1] = Stok_makanan[int(menu_makanan) - 1] + A
                print('\x1b[6;30;43m' + 'Stok menu ke-{} hanya:{}'.format(List_Makanan[int(menu_makanan) - 1], Stok_makanan[int(menu_makanan) - 1]) + '\x1b[0m')
                return
            global struk
            if menu_makanan == '1':
                C = int(A*25000)
                ss = ("bebek goreng       {} x {} = {}".format (A,25000,C))
                struk = struk + ss + '\n'
            elif menu_makanan == '2':
               C = int(A*25000)
               ss = ("steak               {} x {} = {}".format (A,25000,C))
               struk = struk + ss + '\n'
            elif menu_makanan == '3':
               C = int(A*10000)
               ss = ("ayam geprek             {} x {} = {}".format (A,10000,C))
               struk = struk + ss + '\n'
            elif menu_makanan == '4':
               C = int(A*25000) 
               ss = ("nila bakar / goreng     {} x {} = {}".format (A,25000,C))
               struk = struk + ss + '\n'
            elif menu_makanan == '5':
               C = int(A*20000)
               ss = ("nasi goreng udang       {} x {} = {}".format (A,20000,C))
               struk = struk + ss + '\n'
            elif menu_makanan == '6':
               C = int(A*17000)
               ss = ("soto banjar             {} x {} = {}".format (A,17000,C))
               struk = struk + ss + '\n'
            elif menu_makanan == '7':
               C = int(A*15000)
               ss = ("ayam goreng lalapan     {} x {} = {}".format (A,15000,C))
               struk = struk + ss + '\n'
            else:
                C = 0

            global harga_makanan
            harga_makanan = harga_makanan + C

        def hitung_harga_minuman(menu_minuman, B):
            global Stok_minuman
            Stok_minuman[int(menu_minuman) - 8] = Stok_minuman[int(menu_minuman) - 8] - B
            if (Stok_minuman[int(menu_minuman) - 8] <= 0):
                CRED = '\033[91m'
                CEND = '\033[0m'
                print(CRED + "Stok tidak cukup" + CEND)
                Stok_minuman[int(menu_minuman) - 8] = Stok_minuman[int(menu_minuman) - 8] + B
                print('\x1b[6;30;43m' + 'Stok menu ke-{} hanya:{}'.format(List_minuman[int(menu_minuman) - 1], Stok_minuman[int(menu_minuman) - 8]) + '\x1b[0m')
                return
            global struk
            if menu_minuman == '8':
                E = int(B*20000)
                ss = ("coconut coffe      {} x {} ={}".format (B,20000,E))
                struk = struk + ss + '\n'
            elif menu_minuman == '9':
                E = int(B*18000)
                ss = ('caramel latte      {} x {} ={}'.format (B,18000,E))
                struk = struk + ss + '\n'
            elif menu_minuman == '10':
                E = int(B*18000)
                ss = ('strawberry choco    {} x {} ={}'.format (B,18000,E))
                struk = struk + ss + '\n'
            elif menu_minuman == '11':
                E = int(B*20000)
                ss = ('americano moderen   {} x {} ={}'.format (B,20000,E))
                struk = struk + ss + '\n'
            elif menu_minuman == '12':
                E = int(B*15000)
                ss = ('soda gembira        {} x {} ={}'.format (B,15000,E))
                struk = struk + ss + '\n'
            elif menu_minuman == '13':
                E = int(B*15000)
                ss = ('jus alpukat         {} x {} ={}'.format (B,15000,E))
                struk = struk + ss + '\n'
            elif menu_minuman == '14':
                E = int(B*17000)
                ss = ('es buah             {} x {} ={}'.format (B,17000,E))
                struk = struk + ss + '\n'
            elif menu_minuman == '15':
                E = int(B*15000)
                ss = ('es kelapa           {} x {} ={}'.format (B,15000,E))
                struk = struk + ss + '\n'
            elif menu_minuman == '16':
                E = int(B*15000)
                ss = ('black tea           {} x {} ={}'.format (B,15000,E))
                struk = struk + ss + '\n'
            elif menu_minuman == '17':
                E = int(B*15000)
                ss = ('jus mangga          {} x {} ={}'.format (B,15000,E))
                struk = struk + ss + '\n'
            else:
                E = 0
            
            global harga_minuman
            harga_minuman = harga_minuman + E

        print("                   M E N U  P E S A N A N                ")
        print("="*63)
        #input pesanan makanan 
        pesan_lagi = 2
        for i in range(pesan_lagi):
            print('\x1b[5;30;46m' + 'silakan menambah pesanan makanan!' + '\x1b[0m')
            jumlah_varianMakanan = int(input("masukkan jumlah varian makanan : "))
            while(jumlah_varianMakanan):
                menu_makanan = input("~ pilih makanan (1/2/3/4/5/6/7): ")
                A = eval(input("~ masukkan porsi makanan: "))
                hitung_harga_makanan(menu_makanan, A)
                jumlah_varianMakanan = jumlah_varianMakanan - 1
            
        #input pesanan minumann
        pesan_lagi = 2
        for i in range(pesan_lagi):
            print('\x1b[5;30;46m' + 'silakan menambah pesanan minuman!' + '\x1b[0m')
            jumlah_varianMinuman = int(input("masukkan jumlah varian minuman : "))
            while(jumlah_varianMinuman):
                menu_minuman = input("~ pilih minuman (8/9/10/11/12/13/14/15/16/17): ")
                B = eval(input("~ masukkan porsi minuman: "))
                hitung_harga_minuman(menu_minuman, B)
                jumlah_varianMinuman = jumlah_varianMinuman - 1
        print("="*63)

        #cetak struk
        print(" "*47)
        print(" "*47)
        print("~~~~~~~~~~~~  CETAK STRUK PEMBAYARAN  ~~~~~~~~~~~~~~")
        print(" "*47)
        print('\x1b[1;30;47m' + '======  W A R K O P  ======' + '\x1b[0m')
        nomor_pesanan = int(input("NO pesanan :  "))
        nomor_meja = input("meja :  ")
        nama_pembeli = input("nama pembeli  :  ")
        nama_staff = input("kasir :  ")
        import time;
        tanggal = time.asctime( time.localtime(time.time()) )
        print ("Date    :", tanggal)
        print(" "*47)

        print(struk)

        total_harga = int(harga_makanan+harga_minuman)
        #diskon diberlakukan bagi pembeli yang belanja lebih dari 500.000 rupiah
        print("subtotal Rp.",format(total_harga))
        if total_harga > 500000:
            Discount = int(input("your Discount(%):  "))
            total_harga = total_harga - ((Discount/100)*total_harga)
            print("Total     Rp.",format(total_harga))
        else:
            print("Total     Rp.",format(total_harga))
        bayar = int(input("pembayaran      Rp."))
        kembalian = bayar - total_harga
        print("kembalian    Rp.",kembalian)
        print(" "*47)
        print('\x1b[1;30;47m' + '====  THANKS {} FOR CHOOSING WARKOP  ===='.format(nama_pembeli) + '\x1b[0m')
        print(" "*47)



       
        

        



            




    

    
    
