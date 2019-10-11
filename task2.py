from nclib.netcat import Netcat

decrypted = """the purpose of encoding is to transform data so that it can be properly and safely consumed by a different type of system eg binary data being sent over email or viewing special characters on a web page the goal is not to keep information secret but rather to ensure that its able to be properly consumed encoding transforms data into another format using a scheme that is publicly available so that it can easily be reversed it does not require a key as the only thing required to decode it is the algorithm that was used to encode it the purpose of encryption is to transform data in order to keep it secret from others eg sending someone a secret letter that only they should be able to read or securely sending a password over the internet rather than focusing on usability the goal is to ensure the data cannot be consumed by anyone other than the intended recipients encryption transforms data into another format in such a way that only specific individuals can reverse the transformation it uses a key which is kept
secret in conjunction with the plaintext and the algorithm in order to perform the encryption operation as such the ciphertext algorithm and key are all required to return to the plaintext """

nc = Netcat(("pwning.io", 63741), verbose=True)
encrypted = nc.recv().decode().splitlines()[1]
key = {}
for index in range(len(decrypted)):
    key[encrypted[index]] = decrypted[index]
target = encrypted
result = ""
for index in range(len(target)):
    result += key[target[index]]
print(result)
nc.sendline(result.encode())

nc.recv_all()
