from subprocess import Popen, PIPE, STDOUT

p = Popen(['./blob4.bin'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

print(p.communicate('2\n'.encode())[0].rstrip())
for _ in range(5):
    print(p.stdout.readline().rstrip())
print(p.stdout.readline().rstrip())
print(p.stdout.readline().rstrip())
print(p.stdout.readline().rstrip())
