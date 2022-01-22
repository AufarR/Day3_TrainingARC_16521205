import socket as socklib

message = input("Masukkan pesan yang akan dikirim: ")
targetIP = []
targetIP.append(input("Masukkan IP penerima pertama: "))
while True:
  if input("Ketik 1 dan tekan enter untuk menambah penerima (isi dengan yang lain jika sudah selesai): ") == "1":
    targetIP.append(input("Masukkan IP penerima berikutnya: "))
  else:
    break
targetPort = 9993

mysocket = socklib.socket(socklib.AF_INET,socklib.SOCK_DGRAM)
for i in targetIP:
  mysocket.sendto(message.encode(),(i,targetPort))