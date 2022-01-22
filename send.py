import socket as socklib

message = input("Masukkan pesan yang akan dikirim: ")
targetPort = 9993
mysocket = socklib.socket(socklib.AF_INET,socklib.SOCK_DGRAM)

allIP = ["172.29.190.157", "172.29.3.201", "172.29.162.64", "172.29.134.128", "172.29.14.93", "172.29.254.142", "172.29.78.4"]
if input("Ketik 1 dan tekan enter untuk mengirim pesan pada seluruh anggota kelompok (isi dengan yang lain untuk input satu persatu): ") == "1":
  for i in allIP:
    mysocket.sendto(message.encode(),(i,targetPort))
  exit()

targetIP = []
targetIP.append(input("Masukkan IP penerima pertama: "))
while True:
  if input("Ketik 1 dan tekan enter untuk menambah penerima (isi dengan yang lain jika sudah selesai): ") == "1":
    targetIP.append(input("Masukkan IP penerima berikutnya: "))
  else:
    break

for i in targetIP:
  mysocket.sendto(message.encode(),(i,targetPort))