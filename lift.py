import os
import time

# pembukaan program
def welcome() :
    os.system("cls")
    print(f"{'welcome':^20}")
    print(f"{'program lift':^20}")
    print('='*30)

welcome() 

# kondisi gedung/bagunan serta kemampuan lift
N = int(input("jumlah lantai yang ada :"))
x = 0
print("Gedung ini akan memiliki {} lantai".format(N))
print("")
tabint = [0 for i in range (N)]
bebanmax = 500 

# tombol elevator
print("Kondisi tombol elevator : ")
if N%3 == 0 :
    for k in range (1,N,3) :     
        print("|",{k}, {k+1},     {k+2},        "|")
elif N%4 == 0 :
    for k in range (1,N,4) :
        print("|",{k}, {k+1}, {k+2}, {k+3}, "|")
elif N == 10 :
    for k in range (1,N+1,3) :
        if k < N :
            print("|",{k}, {k+1},     {k+2},     "|")
        elif k == N :
            print("|",{k}, "{ }", "{ }", "|")
else : 
    for k in range (1,N,3) :
        if k+2 < N :
            print("|",{k}, {k+1},     {k+2},     "|")
        elif k+2 >= N : 
            print("|",{k}, {k+1}, "{ }", "|")
        

# input dari luar 
# asumsikan input dilakukan oleh sensor 
while True : 
    for i in range (N) :
        tanya = input("\napakah ada panggilan ? (ya/tidak) : ") # dijawab oleh sensor 
        if tanya ==  "ya" :
            lokasi    = int(input("lokasi lif : "))# di input oleh sensor
            if lokasi > N  or lokasi == 0:
                print("input lokasi lift salah")
                break
            else :
                pass
            panggilan = int(input("panggilan ke lantai : "))# berdasarkan input bila ada            
            if panggilan > N or panggilan <= 0 :
                print("lantai tidak ada !!! ")
                break
            if lokasi == panggilan :
                print("buka pintu lift")
            elif panggilan > lokasi :
                print(f"'lift naik menuju lantai {panggilan} ")
                print("\n...\n"*(panggilan-lokasi)) # loading, waktu tunggu
                time.sleep(2)
                print("'lift membuka pintu lift'")
            else :
                print(f"'lift turun menuju lantai {panggilan} ")
                print("\n...\n"*(lokasi-panggilan)) # loading, waktu tunggu
                time.sleep(2)
                print("'lift membuka pintu lift'")
            lokasi = panggilan
        else :
            pass
    
# input di dalam lift  
# asumsikan input dilakukan oleh tombol dan sensor  
        quest  = input("apakah ada input dari dalam ? (ya/tidak) : ")
        if quest == "tidak" :
            break
        for j in range (N) :
            lokasi    = int(input("lokasi lif : "))# di input oleh sensor
            if lokasi > N  or lokasi == 0:
                print("input lokasi lift salah")
                break
            beban = float(input("beban penumpang lift : ")) # diinput oleh sensor
            if beban <= bebanmax :
               break
            else : 
                print("beban terlalu besar !!!!") # ditampilkan di display lift
                print("buka pintu lift")          # command ke mesin pintu
                print("")
                pass
            
        tujuan = int(input("masukan no lantai tujuan : "))

        tabint[i] = tujuan
        if tujuan > N : 
            print("lantai tidak ada")  
            break
        elif tujuan <= N : 
            pass
        if tujuan == lokasi :
            print("lift diam")
            print("buka pintu lift")
        elif tujuan > lokasi :
            print("Tutup pintu")
            time.sleep(0.5)
            print("lift naik ke lantai", tujuan)
            print("\n...\n"*(tujuan-lokasi))
            time.sleep(2)
            print("buka pintu lift")
        elif tujuan < lokasi :
            print("Tutup pintu")
            time.sleep(0.5)
            print("lift turun ke lantai", tujuan)
            print("\n...\n"*(lokasi-tujuan))
            time.sleep(2)
            print("buka pintu lift")
        lokasi = tujuan
        time.sleep(2)
        print("tutup pintu lift")
    pertanyan = str(input("apakah ada input dalam waktu 3 detik ? (ya/tidak) : ")) #dijawab oleh sensor
    if pertanyan == "tidak" :
        break
print("\nlift idle") # informasi ke prosesor lift
