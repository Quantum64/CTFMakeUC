import sys
from nclib.netcat import Netcat

nc = Netcat(("pwning.io", 11235), verbose=False)
nc.recv()
nc.send("0\n".encode())
nc.recv()
nc.send((str(1000) + "\n").encode())
test = nc.recv_until("you get 1 freebies".encode())
test = test.decode()
with open("wtf.txt", "w") as f:
    f.write(test)
test = test.splitlines()[1]
testNumbers = [int(x) for x in test.split(" ") if x.strip()]

nc.send("1\n".encode())
nc.recv()
nc.recv()
nc.send("1\n".encode())
challenge = nc.recv().decode().splitlines()[3].split(" ")

start = int(challenge[0])
end = int(challenge[1])
print("START " + str(start) + ", END " + str(end))
result = testNumbers[start:end]
result = " ".join([str(x) for x in result])
nc.send_line(result.encode())

for _ in range(2):
    challenge = nc.recv().decode().split(" ")
    start = int(challenge[0])
    end = int(challenge[1])
    print("START " + str(start) + ", END " + str(end))
    result = testNumbers[start:end]
    result = " ".join([str(x) for x in result])
    nc.send_line(result.encode())


print(nc.recv_all().decode())