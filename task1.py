import sys
from nclib.netcat import Netcat

def fib(n):
    global cache
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
        if n + 1 in errors:
            cache[n] += errors[n + 1]
    return cache[n]

def clearCache():
    global cache
    cache = {0: 0, 1: 1}

def challenge(start, end):
    end -= 1
    result = [0, 0]
    for index in range(1, end):
        result.append(fib(index) + result[index])
    result = result[start-1:end]
    return " ".join([str(x) for x in result])

printErrorChecks = True
errorCheckRange = 100
errorOffset = 1
errors = {}
sys.setrecursionlimit(10000)
clearCache()
nc = Netcat(("pwning.io", 11235), verbose=True)
# Get 1 to 100
nc.recv()
nc.send("1\n".encode())
nc.recv()
nc.send((str(errorCheckRange) + "\n").encode())
test = nc.recv().decode().splitlines()[1]
print(test)

# Identify errors
reference = challenge(1, errorCheckRange)
if printErrorChecks:
    print("REFERENCE BEFORE CHECK")
    print(reference)
    print("=======================================================================")
    print("EXTERNAL INPUT")
    print(test)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for _ in range(3):
    error = False
    reference = challenge(1, errorCheckRange)
    testNumbers = [int(x) for x in test.split(" ") if x.strip()]
    referenceNumbers = [int(x) for x in  reference.split(" ")]
    for index in range(len(testNumbers)):
        if not testNumbers[index] == referenceNumbers[index]:
            print("Error detected at index " + str(index) + ". Correcting and starting over.")
            errors[index] = errorOffset
            errorOffset += 1
            error = True
            break
    clearCache()
    if not error:
        break
reference = challenge(1, errorCheckRange)
if printErrorChecks:
    print("REFERENCE AFTER CHECK")
    print(reference)

# Discard second attempt for now
'''

nc.send("1\n".encode())
nc.recv()
nc.send("1\n".encode())
    
numbers = nc.recv().decode().split("\n")[3]
numbers = [int(x) for x in numbers.split(" ")]
result = challenge(numbers[0],  numbers[1])
nc.send_line(result.encode())
nc.recv_all()

print("============================================")
print(result)
'''