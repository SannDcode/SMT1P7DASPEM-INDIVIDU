# inisialisasi modul os bawaan python, berfungsi untuk memanggil mengakses system atau terminal, contoh seperti membersihkan terminal menggunakan syntax os.system('cls')
import os
# deklarasi data-data menu makan dan minum, seperti nama menu dan harga menu
datatampil1 = ['1 jenis Menu (Makanan aja/Minuman aja)', '2. 2 Jenis Menu (Makanan dan Minuman)']
dataMinum = ['Kopi ☕', 'Teh 🍵', 'Susu 🥛', [2500, 1500, 2000]]
dataMakanRingan = ['Lontong 🍃', 'Risol Mozzapop 🍤', 'Singkong Gulung 🍥', [2000, [12000,13000], 2000]]
dataMakanBerat = ['Spaghetti 🍝', 'Nasi Padang 🍘', 'Nasi Udhukk 🍚', [11000, 9000, 7000]]
# deklarasi data-data troli atau biasa di sebut keranjang. Tempat menyimpan data menu sementara yang di pilih oleh user
keranjangUser = [[],[],[],[],[[],[]],[],[],[],[]]
# deklarasi nilai tetap untuk menentukan 2 nilai saja, tidak boleh selain huruf yang ada di dalam tipe data tuple
konfirm = ('y', 'n', 'Y', 'N')
# MEMBUAT variable LANDING PROGRAM, SEPERTI MEMUNCULKAN selamat datanb=g dan icon toko
logo = '''
        ██╗    <+>
        ██║ ┌──
  {~}   ██║ │ ███╗   ███╗
        ██║   ████╗ ████║    [^^]
        ██║   ██╔████╔██║  -------
        ╚═╝   ██║╚██╔╝██║ ┏━┃┏━┃━┏┛
----  {<}     ██║ ╚═╝ ██║ ┏━┃┏┏┛ ┃ 
              ╚═╝     ╚═╝ ┛ ┛┛ ┛ ┛
━━━━━━━━━━━━━ Isan Mart ━━━━━━━━━━━━━━
'''
# output Selamat datang di Isan Mart,
# kami disini menjual makanan dan minuman.'
aloIsan = 'Selamat datang di Isan Mart,\nkami disini menjual makanan dan minuman.'
# mendefinisikan atau bisa disebut fungsi. ini berfungsi untuk membersihkan layar terminal dengan nama fungsi isan()
def isan():
    os.system('cls')
# memanggil variable logo dan text selamat daatang
print(f'{logo}{aloIsan}\n======================================')
# mendefinisikan fungsi konfirmasi,jika melanjutkan ke program ataupun tidak.
def isanBreak():
    # membuat variable yang didalamnya itu ada fungsi input. kutip 3 dsini maksudnya membuat kalimat paragraf dengan tipe data string.
    isanbreak = input('''╭─ Ketik y untuk melanjutkan, ketik n untuk keluar
╰─────➣  ''')
    # jika user menginputkan y, maka baris kode 39 akan di jalankan, yang mana akan menjalankan fungsi isan
    if isanbreak == konfirm[0] or isanbreak == konfirm[2]: # or disini maksudnya, jika salah satunya bernilai true maka akan mengeksekusi baris kode terrsebut
        isan()
        isanTampil1() # menampilkan menu awal
    elif isanbreak == konfirm[1] or isanbreak == konfirm[3]:
        print('Terimakasih Telah mengunjungi IsanMart !! ✌😁✌')
        exit()
    else:
        print(f'Mohon untuk mengetikkan antara y dan n !!!, bukan ketik {isanbreak}\n\n')
        isanBreak()

# menampilkan menu awal, disini user menentukan ingin milih jenis menu atau keluar(tidak jadi beli)
def isanTampil1():
    print(f'''
     ┳┳┓        ┏┓     ┓
┏━━━ ┃┃┃┏┓┏┓┓┏  ┣┫┓┏┏┏┓┃ ━━━━━━━━━━━━━━━━━━━━━━┓
┃    ┛ ┗┗ ┛┗┗┻  ┛┗┗┻┛┗┻┗                       ┃
┃  1. jenis Menu (Makanan aja/Minuman aja)     ┃
┃  0. Keluar                                   ┃
┃                                              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
    pilih1 = input('''╭─ Ketik nomor yang sudah di tentukan sesuai keinginan yang mau di beli 😁
╰─────➣  ''')
    if pilih1 == '1' or pilih1 == 1:
        isan()
        print(datatampil1[0])
        makanOrMinum() #jika user menginputkan nilai string 1 atau angka 1 maka akan membersihkan layar,mencetak text yang berada di variable datatampil1 di index ke 0, lalu menjalankan fungsi makanOrMinum() di baris code 72
    elif pilih1 == '0' or pilih1 == 0:
        print('Maaf ga jadi beli')
        exit()
    # jika user menginputkan selain nilai yang di tentukan seperti 1 dan 0, maka akan mengeksekusi baris kode 69 sampai 70
    else:
        print(f'Budayakan membaca!, Jenis menu yang anda masukkan {pilih1} tidak tersedia 😒')
        isanTampil1() #membalikan fungsi jika user salah menginput
# menjalankan atau menampilkan menujenis apa saja
def makanOrMinum():
    print('''
    ╺┓   ┏┳┓┏━╸┏┓╻╻ ╻    ┏┓┏━╸┏┓╻╻┏━┓
┏━━━ ┃   ┃┃┃┣╸ ┃┗┫┃ ┃     ┃┣╸ ┃┗┫┃┗━┓ ━━━━━━━━━┓
┃   ╺┻╸  ╹ ╹┗━╸╹ ╹┗━┛   ┗━┛┗━╸╹ ╹╹┗━┛          ┃
┃       1. Makanan            2. Minuman       ┃
┃                                              ┃
┃    99. Kembali Ke Menu Utama                 ┃
┃                                              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
    pilih2 = input('''╭─ Ketik nomor yang sudah di tentukan sesuai menu yang tampil diatas ✌
╰─────➣  ''')
    if pilih2 == 1 or pilih2 == '1':
        makanannyaApa() # mengeksekusi fungsi makanannyaApa()di baris kode 94 untuk memilih mau makanan apa?
    elif pilih2 == 2 or pilih2 == '2':
        minumannyaApa() # mengeksekusi fungsi minumannyaApa()di baris kode 329 untuk memilih mau makanan apa?
    elif pilih2 == 99 or pilih2 == '99':
        isanTampil1() # balik ke menu awal
    else:
        print(f'Lihat daftar yang tersedia !, yang kamu masukkan {pilih2} tidak tersedia 😒')
        makanOrMinum() #membalikan fungsi jika salah
# menjalankan atau menampilkan jenis makanan apa saja
def makanannyaApa():
    print(f'''
     ┏┓┏━╸┏┓╻╻┏━┓   ┏┳┓┏━┓╻┏ ┏━┓┏┓╻┏━┓┏┓╻
┏━━━  ┃┣╸ ┃┗┫┃┗━┓   ┃┃┃┣━┫┣┻┓┣━┫┃┗┫┣━┫┃┗┫ ━━━━━┓
┃   ┗━┛┗━╸╹ ╹╹┗━┛   ╹ ╹╹ ╹╹ ╹╹ ╹╹ ╹╹ ╹╹ ╹      ┃
┃    1. Makanan Berat                          ┃
┃    2. Makanan Ringan                         ┃
┃    0. Kembali Sebelumnya                     ┃
┃    99. Kembali Ke Menu Utama                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
    makanannyaapa = input('''╭─ Ketik nomor yang sudah di tentukan sesuai menu yang tampil diatas ✌
╰─────➣  ''')
    if makanannyaapa == 1 or makanannyaapa == '1':
        makananBerat() # menjalankan fungsi makananBerat() di baris kode 118 untuk menalmpilkan jenis makanan berat
    elif makanannyaapa == 2 or makanannyaapa == '2':
        makananRingan() # menjalankan fungsi makananBerat()di baris kode 208 untuk menalmpilkan jenis makanan ringan 
    elif makanannyaapa == 0 or makanannyaapa == '0':
        makanOrMinum() # kembali ke pemilihan jenis menu sebelumnya
    elif makanannyaapa == 99 or makanannyaapa == '99':
        isanTampil1() # kembali ke menu awal
    else:
        print(f'Lihat daftar yang tersedia !, yang kamu masukkan {makanannyaapa} tidak tersedia 😒')
        makanannyaApa() # menampilkan pesan kesalahan input, jika user ngasal inputnya

def makananBerat(): #apa maksudnya f'''...''', yang artinya adalah f-string atau formatted string, untuk menyisipkan variable ke dalam string.
    print(f'''
    ┏┳┓┏━┓╻┏ ┏━┓┏┓╻┏━┓┏┓╻   ┏┓ ┏━╸┏━┓┏━┓╺┳╸
┏━━ ┃┃┃┣━┫┣┻┓┣━┫┃┗┫┣━┫┃┗┫   ┣┻┓┣╸ ┣┳┛┣━┫ ┃  ━━━┓
┃   ╹ ╹╹ ╹╹ ╹╹ ╹╹ ╹╹ ╹╹ ╹   ┗━┛┗━╸╹┗╸╹ ╹ ╹     ┃
┃    1. {dataMakanBerat[0]}\t>>>>>>>> Rp.{dataMakanBerat[3][0]:,.0f}     ┃
┃    2. {dataMakanBerat[1]}\t>>>>>>>> Rp.{dataMakanBerat[3][1]:,.0f}      ┃
┃    3. {dataMakanBerat[2]}\t>>>>>>>> Rp.{dataMakanBerat[3][2]:,.0f}      ┃
┃    4. Lanjut Pembayaran 💳                   ┃
┃    0. Kembali Sebelumnya 🔙                  ┃
┃    99. Kembali Ke Menu Utama 1️⃣              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''') # fungsi :,.0f untuk menampilkan koma setelah 3 angka sebelumnya
    makananberat = input('''╭─ Ketik nomor yang sudah di tentukan sesuai menu yang tampil diatas ✌
╰─────➣  ''')
    if makananberat == 1 or makananberat == '1':
        spgty = dataMakanBerat[0]
        qtySpageti = int(input(f'''╭─ Mau beli {spgty} berapa??
╰─────➣  '''))
        nol = 0
        for cekqtyspgty in range(nol,qtySpageti):
            keranjangUser[0].append(spgty)
        print(f'✅️ MAKANAN {spgty.upper()} SUDAH DI TAMBAHKAN KE KERANJANG KAMU YA!!! ✅️')
        print(f'{spgty} kamu sekarang ada {len(keranjangUser[0])}')
        tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        while tanya != konfirm[0] and tanya != konfirm[1] and tanya != konfirm[2] and tanya != konfirm[4]: # konfirmasi
            print('Jawab y atau n !! 😒')
            tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        if tanya == konfirm[0] or tanya == konfirm[2]:
            isan()
            makananBerat()
        elif tanya == konfirm[1] or tanya == konfirm[3]:
            isan()
            isanTampil1()
    elif makananberat == 2 or makananberat == '2': # menentukan 3 kondisi kondisi pertama memilih makanan berat spaghetti yang berada di variable list dataMakanBerat[0] di index ke 0
        pdng = dataMakanBerat[1]
        qtyPdng = int(input(f'''╭─ Mau beli {pdng} berapa??
╰─────➣  '''))
        nol = 0
        for cekqtypdng in range(nol,qtyPdng): # melakukan perulangan sebanyak user yang menginputkan.
            keranjangUser[1].append(pdng)
        print(f'✅️ MAKANAN {pdng.upper()} SUDAH DI TAMBAHKAN KE KERANJANG KAMU YA!!! ✅️')
        print(f'{pdng} kamu sekarang ada {len(keranjangUser[1])}')
        tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        while tanya != konfirm[0] and tanya != konfirm[1] and tanya != konfirm[2] and tanya != konfirm[4]:
            print('Jawab y atau n !! 😒')
            tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        if tanya == konfirm[0] or tanya == konfirm[2]:
            isan()
            makananBerat()
        elif tanya == konfirm[1] or tanya == konfirm[3]:
            isan()
            isanTampil1()
    elif makananberat == 3 or makananberat == '3':
        udhukk = dataMakanBerat[2] #mendeklarasikan variable udhukk dengan nilai variable List index ke 2 yaitu nasi uduk
        qtyudhukk = int(input(f'''╭─ Mau beli {udhukk} berapa??
╰─────➣  '''))
        nol = 0
        for cekqtyudhukk in range(nol,qtyudhukk):
            keranjangUser[2].append(udhukk)
        print(f'✅️ MAKANAN {udhukk.upper()} SUDAH DI TAMBAHKAN KE KERANJANG KAMU YA!!! ✅️')
        print(f'{udhukk} kamu sekarang ada {len(keranjangUser[2])}')
        tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        while tanya != konfirm[0] and tanya != konfirm[1] and tanya != konfirm[2] and tanya != konfirm[4]:
            print('Jawab y atau n !! 😒')
            tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        if tanya == konfirm[0] or tanya == konfirm[2]:
            isan()
            makananBerat()
        elif tanya == konfirm[1] or tanya == konfirm[3]:
            isan()
            isanTampil1()
    elif makananberat == 4 or makananberat == '4':
        isan()
        prosesPembayaran()
    elif makananberat == 0 or makananberat == '0':
        isan()
        makanannyaApa()
    elif makananberat == 99 or makananberat == '99':
        isan()
        isanTampil1()
    else:
        print(f'Lihat daftar yang tersedia !, yang kamu masukkan {makananberat} tidak tersedia 😒')
        makananBerat()

def makananRingan(): # mencetak makan ringan...., user memasukan nomor yang di tentukan, baca kondisi if baris 222 jika false baca kondisi elif baris 243 jika false jalankan elif baris295 sampay baris else yatiu 325
    print(f'''
    ┏┳┓┏━┓╻┏ ┏━┓┏┓╻┏━┓┏┓╻   ┏━┓╻┏┓╻┏━╸┏━┓┏┓╻
┏━━ ┃┃┃┣━┫┣┻┓┣━┫┃┗┫┣━┫┃┗┫   ┣┳┛┃┃┗┫┃╺┓┣━┫┃┗┫ ━━━━━━━━━━━━┓
┃   ╹ ╹╹ ╹╹ ╹╹ ╹╹ ╹╹ ╹╹ ╹   ╹┗╸╹╹ ╹┗━┛╹ ╹╹ ╹             ┃
┃    1. {dataMakanRingan[0]}\t>>>>>>>> Rp.{dataMakanRingan[3][0]:,.0f}                ┃
┃    2. {dataMakanRingan[1]} >>>>>>>> Rp.{dataMakanRingan[3][1][0]:,.0f} - Rp.{dataMakanRingan[3][1][1]:,.0f} ┃
┃    3. {dataMakanRingan[2]} >>>>>>>> Rp.{dataMakanRingan[3][2]:,.0f}            ┃
┃    4. Lanjut Pembayaran 💳                             ┃
┃    0. Kembali Sebelumnya 🔙                            ┃
┃    99. Kembali Ke Menu Utama 1️⃣                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
    makananringan = input('''╭─ Ketik nomor yang sudah di tentukan sesuai menu yang tampil diatas ✌
╰─────➣  ''')
    if makananringan == 1 or makananringan == '1':
        lntg = dataMakanRingan[0]
        qtyLntg = int(input(f'''╭─ Mau beli {lntg} berapa??
╰─────➣  '''))
        nol = 0
        for cekqtylntg in range(nol,qtyLntg):
            keranjangUser[3].append(lntg)
        print(f'✅️ MAKANAN {lntg.upper()} SUDAH DI TAMBAHKAN KE KERANJANG KAMU YA!!! ✅️')
        print(f'{lntg} kamu sekarang ada {len(keranjangUser[3])}')
        tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        while tanya != konfirm[0] and tanya != konfirm[1] and tanya != konfirm[2] and tanya != konfirm[4]:
            print('Jawab y atau n !! 😒')
            tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        if tanya == konfirm[0] or tanya == konfirm[2]:
            isan()
            makananRingan()
        elif tanya == konfirm[1] or tanya == konfirm[3]:
            isan()
            isanTampil1()
    elif makananringan == 2 or makananringan == '2':
        rsol = dataMakanRingan[1]
        print(f'''
┏━━ VARIANT RISOL MOZZAPOP ━━━━━━━━━━┓
┃   1. Original 😎 Rp {dataMakanRingan[3][1][0]}   ┃
┃   2. Pedas HOT 😛  Rp {dataMakanRingan[3][1][1]}         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''') #maksud dataMakanRingan[3][1][1] yaitu memanggil nilai yang berada pada variable list dataMakanRingan di index 3 tipde data list, di kolom ke 1 tipe data list, di index 1 tipedata integer.
        selectVRsol = int(input('''╭─ Masukkan angka yang tersedia atau yang ingin di pilih !
╰─────➣  '''))
        if selectVRsol == 1 or selectVRsol == '1':
            qtyrsol = int(input(f'''╭─ Mau beli {rsol} variant Original berapa??
╰─────➣  '''))
            nol = 0
            for cekqtyrsol in range(nol,qtyrsol):
                keranjangUser[4][0].append(rsol)
            print(f'✅️ MAKANAN {rsol.upper()} VARIANT ORIGINAL SUDAH DI TAMBAHKAN KE KERANJANG KAMU YA!!! ✅️')
            print(f'{rsol} kamu sekarang ada {len(keranjangUser[4][0])}')
            tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
            while tanya != konfirm[0] and tanya != konfirm[1] and tanya != konfirm[2] and tanya != konfirm[4]:
                print('Jawab y atau n !! 😒')
                tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
            if tanya == konfirm[0] or tanya == konfirm[2]: # nested if atau if beranak/bersarang, ada kondisi di dalam kondisi
                isan()
                makananRingan()
            elif tanya == konfirm[1] or tanya == konfirm[3]:
                isan()
                isanTampil1()
        elif selectVRsol == 2 or selectVRsol == '2':
            qtyrsol2 = int(input(f'''╭─ Mau beli {rsol} variant Pedas berapa??
╰─────➣  '''))
            nol = 0
            for cekqtyrsol in range(nol,qtyrsol2):
                keranjangUser[4][1].append(rsol)
            print(f'✅️ MAKANAN {rsol.upper()} VARIANT PEDAS SUDAH DI TAMBAHKAN KE KERANJANG KAMU YA!!! ✅️')
            print(f'{rsol} kamu sekarang ada {len(keranjangUser[4][1])}')
            tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
            while tanya != konfirm[0] and tanya != konfirm[1] and tanya != konfirm[2] and tanya != konfirm[4]:
                print('Jawab y atau n !! 😒')
                tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
            if tanya == konfirm[0] or tanya == konfirm[2]:
                isan()
                makananRingan()
            elif tanya == konfirm[1] or tanya == konfirm[3]:
                isan()
                isanTampil1()
            else:
                print(f'Lihat daftar yang tersedia !, yang kamu masukkan {selectVRsol} tidak tersedia 😒')
                makananRingan()
    elif makananringan == 3 or makananringan == '3':
        sngkng = dataMakanRingan[2]
        qtysngkng = int(input(f'''╭─ Mau beli {sngkng} berapa??
╰─────➣  '''))
        nol = 0
        for cekqtysngkng in range(nol,qtysngkng):
            keranjangUser[5].append(sngkng)
        print(f'✅️ MAKANAN {sngkng.upper()} SUDAH DI TAMBAHKAN KE KERANJANG KAMU YA!!! ✅️')
        print(f'{sngkng} kamu sekarang ada {len(keranjangUser[5])}')
        tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        while tanya != konfirm[0] and tanya != konfirm[1] and tanya != konfirm[2] and tanya != konfirm[4]:
            print('Jawab y atau n !! 😒')
            tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        if tanya == konfirm[0] or tanya == konfirm[2]:
            isan()
            makananRingan()
        elif tanya == konfirm[1] or tanya == konfirm[3]:
            isan()
            isanTampil1()
    elif makananringan == 4 or makananringan == '4':
        isan()
        prosesPembayaran()
    elif makananringan == 0 or makananringan == '0':
        isan()
        makanannyaApa()
    elif makananringan == 99 or makananringan == '99':
        isan()
        isanTampil1()
    else:
        print(f'Lihat daftar yang tersedia !, yang kamu masukkan {makananringan} tidak tersedia 😒')
        makananRingan()

def minumannyaApa():
    print(f'''
    ┏┳┓   ╻   ┏┓╻   ╻ ╻   ┏┳┓   ┏━┓   ┏┓╻
┏━━ ┃┃┃   ┃   ┃┗┫   ┃ ┃   ┃┃┃   ┣━┫   ┃┗┫ ━━┓
┃   ╹ ╹   ╹   ╹ ╹   ┗━┛   ╹ ╹   ╹ ╹   ╹ ╹   ┃
┃    1. {dataMinum[0]}\t>>>>>>>> Rp.{dataMinum[3][0]:,.0f}     ┃
┃    2. {dataMinum[1]}\t>>>>>>>> Rp.{dataMinum[3][1]:,.0f}      ┃
┃    3. {dataMinum[2]}\t>>>>>>>> Rp.{dataMinum[3][2]:,.0f}      ┃
┃    4. Lanjut Pembayaran 💳                   ┃
┃    0. Kembali Sebelumnya 🔙                  ┃
┃    99. Kembali Ke Menu Utama 1️⃣             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
    minumannyaapa = input('''╭─ Ketik nomor yang sudah di tentukan sesuai menu yang tampil diatas ✌
╰─────➣  ''')
    if minumannyaapa == 1 or minumannyaapa == '1':
        kopi = dataMinum[0]
        qtykopi = int(input(f'''╭─ Mau beli {kopi} berapa??
╰─────➣  '''))
        nol = 0
        for cekqtykopi in range(nol,qtykopi):
            keranjangUser[6].append(kopi)
        print(f'✅️ MAKANAN {kopi.upper()} SUDAH DI TAMBAHKAN KE KERANJANG KAMU YA!!! ✅️')
        print(f'{kopi} kamu sekarang ada {len(keranjangUser[6])}')
        tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        while tanya != konfirm[0] and tanya != konfirm[1] and tanya != konfirm[2] and tanya != konfirm[4]:
            print('Jawab y atau n !! 😒')
            tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        if tanya == konfirm[0] or tanya == konfirm[2]:
            isan()
            minumannyaApa()
        elif tanya == konfirm[1] or tanya == konfirm[3]:
            isan()
            isanTampil1()
    elif minumannyaapa == 2 or minumannyaapa == '2':
        teh = dataMinum[1]
        qtyteh = int(input(f'''╭─ Mau beli {teh} berapa??
╰─────➣  '''))
        nol = 0
        for cekqtyteh in range(nol,qtyteh):
            keranjangUser[7].append(teh)
        print(f'✅️ MAKANAN {teh.upper()} SUDAH DI TAMBAHKAN KE KERANJANG KAMU YA!!! ✅️')
        print(f'{teh} kamu sekarang ada {len(keranjangUser[7])}')
        tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        while tanya != konfirm[0] and tanya != konfirm[1] and tanya != konfirm[2] and tanya != konfirm[4]:
            print('Jawab y atau n !! 😒')
            tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        if tanya == konfirm[0] or tanya == konfirm[2]:
            isan()
            minumannyaApa()
        elif tanya == konfirm[1] or tanya == konfirm[3]:
            isan()
            isanTampil1()
    elif minumannyaapa == 3 or minumannyaapa == '3':
        susu = dataMinum[2]
        qtysusu = int(input(f'''╭─ Mau beli {susu} berapa??
╰─────➣  '''))
        nol = 0
        for cekqtysusu in range(nol,qtysusu):
            keranjangUser[8].append(susu)
        print(f'✅️ MAKANAN {susu.upper()} SUDAH DI TAMBAHKAN KE KERANJANG KAMU YA!!! ✅️')
        print(f'{susu} kamu sekarang ada {len(keranjangUser[8])}')
        tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        while tanya != konfirm[0] and tanya != konfirm[1] and tanya != konfirm[2] and tanya != konfirm[4]:
            print('Jawab y atau n !! 😒')
            tanya = input(f'''╭─ Mau beli makanan yang sebelumnya? y/n
╰─────➣  ''')
        if tanya == konfirm[0] or tanya == konfirm[2]:
            isan()
            minumannyaApa()
        elif tanya == konfirm[1] or tanya == konfirm[3]:
            isan()
            isanTampil1()
    elif minumannyaapa == 4 or minumannyaapa == '4':
        isan()
        prosesPembayaran()
    elif minumannyaapa == 0 or minumannyaapa == '0':
        isan()
        makanOrMinum()
    elif minumannyaapa == 99 or minumannyaapa == '99':
        isan()
        isanTampil1()
    else:
        print(f'Lihat daftar yang tersedia !, yang kamu masukkan {minumannyaapa} tidak tersedia 😒')
        minumannyaApa()

# menampilkan daftar jenis menu yang di pilih untuk di beli
def troliKamu():
    nomorTroli = 1
    rngnTroli = 0
    mnmTroli = 0
    colTroli = 0
    colRsol = 0 # variable nomorTroli rngnTroli mnmTroli colTroli colRsol untuk meringkas pemborosan pengkondisian, nantinya variable tersebut akan di lakukan increment penambahan atau dekrement pengurangan
    print(f'''
  ╺┳╸┏━┓┏━┓╻  ╻   ╻┏ ┏━┓┏┳┓╻ ╻
┏━ ┃ ┣┳┛┃ ┃┃  ┃   ┣┻┓┣━┫┃┃┃┃ ┃ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  ╹ ╹┗╸┗━┛┗━╸╹   ╹ ╹╹ ╹╹ ╹┗━┛                                 ┃
┃   No\tNama Menu\t\t     Qty\t  Nominal      ┃''')
    for ulangiTroli in range(1):
      for ulangiTroli in keranjangUser:
            if dataMakanBerat[colTroli] in keranjangUser[colTroli]:
                dataMakanBerat[0] = 'Spaghetti   🍝'
                nominal = f'{dataMakanBerat[3][colTroli]:,.0f}'
                if len(str(nominal)) == 6:
                    spasi = '    ┃'
                    nominal += spasi
                if len(str(nominal)) == 5:
                    spasi2 = '     ┃'
                    nominal += spasi2
                print('┃   '+str(nomorTroli)+'.',f' {dataMakanBerat[colTroli]}\t\t     ',len(keranjangUser[colTroli]),f'\t  Rp.{str(nominal)}')
                nomorTroli += 1        
            colTroli += 1

            if colTroli > 2:
                        break
      colTroli = 3
      idxLima = 5
      for ulangiTroli in keranjangUser:
        nominal = f'{dataMakanRingan[3][0]:,.0f}'
        nominalr = f'{dataMakanRingan[3][1][0]:,.0f}'
        if len(str(nominal)) == 6:
            spasi = '    ┃'
            nominal += spasi
        if len(str(nominalr)) == 6:
            spasi = '    ┃'
            nominalr += spasi
        if len(str(nominal)) == 5:
            spasi2 = '     ┃'
            nominal += spasi2
        if len(str(nominalr)) == 5:
            spasi2 = '       \t┃'
            nominalr += spasi2
        if dataMakanRingan[rngnTroli] in keranjangUser[colTroli]:
            dataMakanRingan[0] = 'Lontong        🍃'
            print('┃   '+str(nomorTroli)+'.',f' {dataMakanRingan[rngnTroli]}\t     ',len(keranjangUser[colTroli]),f'\t  Rp.{str(nominal)}')
            nomorTroli += 1     
            colTroli += 1
        if dataMakanRingan[rngnTroli] in keranjangUser[4][0]:
            print('┃   '+str(nomorTroli)+'.',f' {dataMakanRingan[rngnTroli]} Original   ',len(keranjangUser[4][0]),f'\t  Rp.{str(nominalr)}')
            nomorTroli += 1
        if dataMakanRingan[rngnTroli] in keranjangUser[4][1]:
            print('┃   '+str(nomorTroli)+'.',f' {dataMakanRingan[rngnTroli]} Pedas\t     ',len(keranjangUser[4][1]),f'\t  Rp.{str(nominalr)}')
            nomorTroli += 1
        if dataMakanRingan[rngnTroli] in keranjangUser[idxLima]:
            print('┃   '+str(nomorTroli)+'.',f' {dataMakanRingan[2]}\t     ',len(keranjangUser[5]),f'\t  Rp.{str(nominal)}')
            nomorTroli += 1

        colRsol += 1   
        rngnTroli += 1
        if rngnTroli > 2:  
            break
      colTroli = 6
      for ulangiTroli in keranjangUser:
        nominal = f'{dataMinum[3][mnmTroli]:,.0f}'
        if dataMinum[mnmTroli] in keranjangUser[colTroli]:
            print('┃   '+str(nomorTroli)+'. ',f'{dataMinum[mnmTroli]}\t     ',len(keranjangUser[colTroli]),f'          {nominal}')
            nomorTroli += 1
        mnmTroli += 1
        colTroli += 1
        if mnmTroli > 2:
            break
      jmlPay = (len(keranjangUser[0]) * dataMakanBerat[3][0], len(keranjangUser[1]) * dataMakanBerat[3][1], len(keranjangUser[2]) * dataMakanBerat[3][2], len(keranjangUser[3]) * dataMakanRingan[3][0], len(keranjangUser[4][0]) * dataMakanRingan[3][1][0], len(keranjangUser[4][1]) * dataMakanRingan[3][1][0], len(keranjangUser[5]) * dataMakanRingan[3][2], len(keranjangUser[6]) * dataMinum[3][0], len(keranjangUser[7]) * dataMinum[3][1], len(keranjangUser[8]) * dataMinum[3][2])
      totalPay = jmlPay[0]+jmlPay[1]+jmlPay[2]+jmlPay[3]+jmlPay[4]+jmlPay[5]+jmlPay[6]+jmlPay[7]+jmlPay[8]+jmlPay[9]
      if len(str(totalPay)) == 4:
          space = '        '
      elif len(str(totalPay)) == 5:
          space = '       '
      elif len(str(totalPay)) == 6:
          space = '      '
      elif len(str(totalPay)) == 7:
          space = '     '
      elif len(str(totalPay)) == 8:
          space = '    '
      elif len(str(totalPay)) == 9:
          space = '   '
      elif len(str(totalPay)) == 10:
          space = '  '
      space = space
      print(f'''┃                                                              ┃
┃   --------------------------------------------------------   ┃
┃   Total:\t\t\t|\t\tRp.{totalPay}{space}┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
    tanyaLgi = input('''Ketik 1 untuk kembali Ke Proses Pembayaran
╰─────➣  ''')
    if tanyaLgi == konfirm[0] or tanyaLgi == konfirm[2]: # or disini maksudnya, jika salah satunya bernilai true maka akan mengeksekusi baris kode terrsebut
        isan() # membersihkan layar
        prosesPembayaran() # menampilkan proses pembayaran
    else:
        print(f'Mohon untuk mengetikkan antara y dan n !!!, bukan ketik {tanyaLgi}\n\n')
        troliKamu()

def prosesPembayaran1(): #user membayar via online
    print(f'''
❚█══ 𝗣𝗥𝗢𝗦𝗘𝗦 𝗣𝗘𝗠𝗕𝗔𝗬𝗔𝗥𝗔𝗡 ══█❚
  **** SCAN QRCODE UNTUK MEMILIH METODE PEMBAYARAN ****
  
  █▀▀▀▀▀█ █ ▄ ▀▀█▀▀ █▀▀▀▀▀█  
  █ ███ █ ▄▀▄▄▄ ▄▀▄ █ ███ █  
  █ ▀▀▀ █ ▀▀█ ▄ ▄█▀ █ ▀▀▀ █  
  ▀▀▀▀▀▀▀ ▀ █▄█ █ ▀ ▀▀▀▀▀▀▀  
  █ ▄  ▄▀█▄▀█▀█▀▀▀ █ ▄▀█▄▀█  
  █▄▄██▄▀  ▀  ▀▀▀   ▄ ▀ ▄▀█  
   ▀▄▄█ ▀██ █ ██▀▀▀▄▄█▀▄▀ ▄  
  █  ▄  ▀▄▀▄▄▄ ▄█▀ ▀▀██▀ ▀▄  
    ▀ ▀ ▀▀▀██▄▀▀▄▀█▀▀▀█▄▀▄▀  
  █▀▀▀▀▀█ ▀▄█ ▀ ▀▄█ ▀ █▀ ▄▀  
  █ ███ █  ██▄ ▀█▄▀▀▀▀▀ █▀▄  
  █ ▀▀▀ █  █ █ ▄█▀██   ▄██   
  ▀▀▀▀▀▀▀ ▀ ▀▀▀ ▀▀  ▀  ▀▀▀▀ 
''') 
    
def prosesPembayaran():
    print('''
┏━━━━━━ P R O S E S  P E M B A Y A R A N ━━━━━━┓
┃                                              ┃
┃   1. QRIS ☑                                  ┃
┃   2. LIHAT TROLI 🛒                          ┃
┃   0. GA JADI BELI 😢                         ┃
┃                                              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
''')
    prosespembayaran = input('''╭─ Ketik nomor yang sudah di tentukan sesuai menu yang tampil diatas ✌
╰─────➣  ''')
    if prosespembayaran == 1 or prosespembayaran == '1':
        prosesPembayaran1()
    elif prosespembayaran == 2 or prosespembayaran == '2':
        troliKamu()
    elif prosespembayaran == 0 or prosespembayaran == '0':
        isan()
        exit()
    else:
        print(f'Lihat daftar yang tersedia !, yang kamu masukkan ({prosespembayaran}) tidak tersedia 😒')
        prosesPembayaran()
isanBreak()
isanTampil1()

#NIM : 19251534
#NAMA : MAULANA ABDUL IHSAN PALUPI
# KELAS : 19.1B.05
# 4NOV2025
