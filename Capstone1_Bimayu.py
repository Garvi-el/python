listBg = [
    {
        'kode' : 'BG001',
        'nama' : 'CATAN',
        'umur' : 10,
        'durasi' : "60 - 120 Menit",
        'tipe' : 'Strategi',
        'kesulitan' : 'Sedang'
    },
    {
        'kode' : 'BG002',
        'nama' : 'MYSTERIUM',
        'umur' : 10,
        'durasi' : "40 - 80 Menit",
        'tipe' : 'Kooperatif',
        'kesulitan' : 'mudah'
    },
    {
        'kode' : 'BG003',
        'nama' : 'COUP',
        'umur' : 13,
        'durasi' : "15 - 30 Menit",
        'tipe' : 'Deduksi',
        'kesulitan' : 'Mudah'
    },
    {
        'kode' : 'BG004',
        'nama' : 'DIXIT',
        'umur' : 8,
        'durasi' : '30 - 60 Menit',
        'tipe' : 'Party',
        'kesulitan' : 'Mudah'
    },
    {
        'kode' : 'BG005',
        'nama' : 'DEAD OF WINTER',
        'umur' : 14,
        'durasi' : '60 - 120 Menit',
        'tipe' : 'Kooperatif',
        'kesulitan' : 'Sulit'
    },
    {
        'kode' : 'BG006',
        'nama' : 'SCYTHE',
        'umur' : 14,
        'durasi' : '90 - 150 Menit',
        'tipe' : 'Strategi',
        'kesulitan' : 'Sulit'
    },
    {
        'kode' : 'BG007',
        'nama' : 'TICKET TO RIDE',
        'umur' : 8,
        'durasi' : '30 - 60 Menit',
        'tipe' : 'Strategi',
        'kesulitan' : 'Sedang'
    },
    {
        'kode' : 'BG008',
        'nama' : 'AVALON',
        'umur' : 13,
        'durasi' : '30 - 60 Menit',
        'tipe' : 'Deduksi',
        'kesulitan' : 'Mudah'
    },
    {
        'kode' : 'BG009',
        'nama' : 'TERRAFORMING MARS',
        'umur' : 13,
        'durasi' : '90 - 120 Menit',
        'tipe' : 'Strategi',
        'kesulitan' : 'Sulit'
    },
    {
        'kode' : 'BG010',
        'nama' : 'PANDEMIC',
        'umur' : 13,
        'durasi' : '45 - 60 Menit',
        'tipe' : 'Kooperatif',
        'kesulitan' : 'Sedang'
    },
    {
        'kode' : 'BG011',
        'nama' : 'ULTIMATE WEREWOLF',
        'umur' : 14,
        'durasi' : '30 - 90 Menit',
        'tipe' : 'Party',
        'kesulitan' : 'Mudah'
    }
]

bayar = 25000

def tabel(list):
    print('-'*39 + 'DAFTAR BOARDGAME YANG TERSEDIA' + '-'*39 )
    print('='*108)
    print(f'{'Kode':<10} | {'Nama Boardgame':<20} | {'Minimal Usia':<13} | {'Durasi Permainan':<17} | {'Tipe Permainan':<15} | {'Tingkat Kesulitan':<20}')
    print('='*108)
    for i in range(len(list)) :
        print(f'{list[i]['kode']:<10} | {list[i]['nama']:<20} | {list[i]['umur']:<13} | {list[i]['durasi']:<17} | {list[i]['tipe']:<15} | {list[i]['kesulitan']:<20}')
#Fungsi Read
def listBoardGame(list) :
    while True :
        menuTampilkan = (input('''                     
            1. Tampilkan Semua List Boardgame
            2. Tampilkan Bedasarkan kata Kunci
            3. Kembali ke Menu Utama

            Masukan nomor yang Sesuai :                   
            ''' ))
        if menuTampilkan == '1' :
            print(tabel(listBg))
            
        elif menuTampilkan == '2' :
            while True :
                cari = input('Masukan Kata Kunci yang sesuai : ')
                print('INFO :MASUKAN HURUF E UNTUK EXIT ATAU KEMBALI KE MENU UTAMA')
                print(f'{'Kode':<10} | {'Nama Boardgame':<20} | {'Minimal Usia':<13} | {'Durasi Permainan':<17} | {'Tipe Permainan':<15} | {'Tingkat Kesulitan':<20}')
                ada = False
                for cariBg in listBg:
                    if cariBg['nama'] == cari.upper() or cariBg['kesulitan'] == cari.capitalize() or cariBg['durasi'] in cari.capitalize() or cariBg['tipe'] == cari.capitalize():
                        print(f'{cariBg['kode']:<10} | {cariBg['nama']:<20} | {cariBg['umur']:<13} | {cariBg['durasi']:<17} | {cariBg['tipe']:<15} | {cariBg['kesulitan']:<20}')
                        ada = True
                if cari.upper() == 'E' :
                    break
                elif ada == False :
                    print(f'{cari.upper()} TIDAK ADA DALAM LIST BOARDGAME')
        elif menuTampilkan == '3' :
            break            
        else :
            tempelate()
            
def tempelate() :
    print('\n*****NOMOR TIDAK SESUAI, MASUKAN NOMOR YANG SESUAI*****')

def hargaSewa() :
    sewa = int(input('Ingin menyewa berapa jam?\nINFO : Lihat List Boardgame untuk melihat rata-rata durasi permainan pada judul Boardgame!'))
    while True :
        harga = input(f'Anda menyewa untuk bermain selama {sewa} Jam. Apakah anda yakin?\nINFO : Lihat List Boardgame untuk melihat rata-rata durasi permainan pada judul Boardgame! (y/n) ').lower()
        if harga == 'y' :
            print(f'Total bermain anda {sewa} Jam dan Total yang harus dibayarkan {sewa*bayar}.\nSilahkan membayar di kasir\nTerima Kasih!')
            break
    
#Fungsi Create
def menambahBG(list):
    while True :
        menuTambah = input('''
                               
            1. Tambahkan List Boardgame baru
            2. Kembali ke Menu Utama

            Masukan nomor yang Sesuai :              
            ''')

        if menuTambah == '1' : 
            while True :
                kodeBg = input('Masukan kode Boardgame : ').upper()
                cekKode = False
                for listBgBaru in listBg :
                    if kodeBg == listBgBaru['kode'] :
                        cekKode = True
                        break
                if cekKode :
                    print('*******KODE YANG ANDA MASUKAN SUDAH ADA*******')
                else :
                    break
                
            while True :                                         
                namaBg = input('Masukan nama Boardgame : ').upper()
                cekNama = False
                for listBgBaru in listBg :
                    if namaBg == listBgBaru['nama'] :
                        cekNama = True
                        break
                if cekNama :
                    print('*******NAMA YANG ANDA MASUKAN SUDAH ADA*******')
                else :
                    break
            
            while True :
                try :
                    umurBg = int(input('Masukan minimal umur Boardgame : '))
                    break
                except :
                    print('*******FORMAT SALAH, MASUKAN FORMAT ANGKA*******')
            
            durasiBg = input('Masukan durasi permainan Boardgame : ').capitalize()
            tipeBg = input('Masukan tipe Boardgame : ').capitalize()
            kesulitanBg = input('Masukan kesulitan Boardgame : ').capitalize()
            yakin = input(f'Anda memasukkan {kodeBg} {namaBg} {umurBg} {durasiBg} {tipeBg} {kesulitanBg}\n\n apakah anda yakin ingin menambahkan Boardgame? (y/n) ').lower()
            if yakin == 'y' :
                listBg.append({
                'kode' : kodeBg,
                'nama' : namaBg,
                'umur' : umurBg,
                'durasi' : durasiBg,
                'tipe' : tipeBg,
                'kesulitan' : kesulitanBg
            })
                tabel(listBg)
                print('BOARDGAME BERHASIL DISIMPAN')
                lagi = input('Ingin menambahkan Boardgame lainnya? (y/n) ').lower()
                if lagi == 'n' :
                    break
            else :
                tabel(listBg)
                print('BOARDGAME GAGAL DISIMPAN')
                lagi = input('Ingin menambahkan Boardgame lainnya? (y/n) ').lower()
                if lagi == 'n' :
                    break
            
            
        elif menuTambah == '2' :
            break
        else :
            tempelate() 
#Fungsi Delete
def menghapusBg(list):
    while True :
        menuHapus = (input('''
                              
        1. Hapus list Boardgame
        2. Kembali ke Menu Utama

        Masukan nomor yang sesuai : 
    '''))
        if menuHapus == '1' :
            print(tabel(listBg))
            while True :
                hapus = (input('Masukan nama Boardgame yang ingin di hapus ')).upper()
                for hapusBg in listBg :
                    if hapusBg['nama'] == hapus :
                        yakin = input(f'Anda ingin menghapus {hapus} dari list\n\n apakah anda yakin ingin menghapus Boardgame? (y/n) ').lower()
                        if yakin == 'y':
                            listBg.remove(hapusBg)
                            tabel(listBg)
                            print('BOARDGAME BERHASIL DIHAPUS')                        
                        else :
                            print('BOARDGAME BATAL DIHAPUS')
                            break
                hapusLagi = input('Ingin menghapus Boardgame lainnya? (y/n) ').lower()
                if hapusLagi == 'n' :
                    break
                else : 
                    print('*****NAMA BOARDGAME TIDAK DITEMUKAN, MASUKAN NAMA YANG BENAR*****')
        elif menuHapus == '2' :
            break
        else :
            tempelate()
#Fungsi Update
def updateBg(list) :
    print(tabel(listBg))
    while True :
        menuUpdate = input('''
                       
        1. Update list Boardgame
        2. Kembali ke Menu Utama
        
        Masukan nomor yang sesuai : 
    ''')
        if menuUpdate == '1' :
            while True :
                update = input('Masukan nama Boardgame yang ingin diubah : ').upper()
                for updateBg in listBg :
                    if updateBg['nama'] == update :
                        updateBg['nama'] = input(f'Masukan nama Boardgame yang baru. Lama = ({updateBg['nama']}) : ').upper()
                        updateBg['umur'] = int(input(f'Masukan umur Boardgame yang baru. Lama = ({updateBg['umur']}) : '))
                        updateBg['durasi'] = input(f'Masukan durasi Boardgame yang baru. Lama = ({updateBg['durasi']}) : ').capitalize()
                        updateBg['tipe'] = input(f'Masukan tipe yang baru. Lama = ({updateBg['tipe']}) : ').capitalize()
                        updateBg['kesulitan'] = input(f'Masukan kesulitan Boardgame yang baru. Lama = ({updateBg['kesulitan']}) : ').capitalize()
                        print(tabel(listBg))
                        print('List Boardgame berhasil diperbaharui.')
                        break                      
                else :
                    print('*****NAMA BOARDGAME TIDAK DITEMUKAN, MASUKAN NAMA YANG BENAR*****')    
                lagi = input('\nIngin mengedit list Boardgame lagi? (y/n) ')
                if lagi.lower() == 'n' :
                    break      
        elif menuUpdate == '2' :
            break
        else :
            tempelate()

def menuUser() :
    while True :
        user = input('''
                PURWADHIKA BOARD GAMES & CAFE
        
        Login sebagai :
        1. Admin
        2. User
        3. Keluar program
                         
        Masukan nomor yang sesuai :      
    ''')
        if user == '1' :
            passAdmin()
        elif user == '2' :
            menuUtamaUser()
        elif user == '3' :
            break
        else :
            tempelate()
            
def passAdmin() :
    while True :
        print('KETIK E UNTUK KEMBALI KE MENU USER')
        password = input('Masukan password admin : ')
        if password.upper() =='E':
            break
        elif password == '0000' :
            menuUtama()
        else :
            print('*****PASSWORD YANG ANDA MASUKAN SALAH. COBA LAGI*****')

def menuUtama() : 
    while True :
        pilihan = input(('''
        Halo Admin 
                    
        Menu Utama

        1. Tampilkan List Boardgame Yang Tersedia
        2. Tambah Boardgame Ke Dalam List Boardgame
        3. Edit List Boardgame
        4. Hapus List Boargame 
        5. Keluar Dari Menu Utama  

        Masukan nomor menu yang sesuai :                         
        '''))
          
        if pilihan == '1' :
            listBoardGame(listBg)
        elif pilihan == '2' :
            menambahBG(listBg)
        elif pilihan == '3' :
            updateBg(listBg)
        elif pilihan == '4' :
            menghapusBg(listBg)
        elif pilihan == '5' :
            break
        else :
            tempelate()
        
def menuUtamaUser() :
    while True :
        pilihanUser = input('''
            Halo User 
                    
        Menu Utama

        1. Tampilkan List Boardgame Yang Tersedia
        2. Sewa Boardgame (25.000/Jam)
        3. Keluar Dari Menu Utama   
           
        Masukann nomor yang sesuai :                  
        ''')
        if pilihanUser == '1' :
            listBoardGame(listBg)
        elif pilihanUser == '2' :
            hargaSewa()
            break
        elif pilihanUser == '3' :
            menuUser()
        else :
            tempelate()
                    
print(menuUser())

                    
                 

                    


    
