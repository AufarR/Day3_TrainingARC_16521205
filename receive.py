import socket as socklib

sock = socklib.socket(socklib.AF_INET, socklib.SOCK_DGRAM)
myIP = "172.29.134.128"
myPort = 9993
sock.bind((myIP, myPort))

while True:
  data, addr = sock.recvfrom(1024)
  print("received message: {}".format(data))
  if input("Ketik 1 dan tekan enter untuk berhenti menerima pesan (isi dengan yang lain untuk melanjutkan menerima pesan): ") == "1":
    break