import random

# Bag. 0 Menghasilkan suatu bilangan besar acak
def generateRandomPrime(n, low_primes):
    while True:
        num = random.randrange(2**(n-1)+1, 2**n - 1)
        if check_low_prime(num,low_primes):
            return num

# Bag. 1 Membentuk list bilangan prima rendah
def sieve_of_eratosthenes(n):
    list_of_primes = [True for i in range(n+1)]
    for i in range(2, int(n**(1/2))+1, 1):
        if list_of_primes[i]:
            for j in range(i**2, n+1, i):
                list_of_primes[j] = False
    new_primes = []
    for k in range(2,n+1):
        if (list_of_primes[k]):
            new_primes.append(k)
    return new_primes

# Bag. 2 mengecek apakah bilangan tersebut dapat dibagi
# oleh bilangan-bilangan prima rendah, kalau habis dibagi
# artinya, bilangan tersebut adalah bilangan komposit.
def check_low_prime(n, low_primes):
    for primes in low_primes:
        if n % primes == 0 and primes**2 <= n:
            return False
        else:
            return True

# Bag. 3 mengecek bilangan prima dengan algoritma
# uji prima Miller-Rabin
def Miller_Rabin(n_prime):
    m = 0
    e = n_prime-1
    while n_prime % 2 == 0:
        e >>= 1
        m += 1
    def isComposite(n):
        if pow(n, e, n_prime) == 1:
            return False
        for i in range(m):
            if pow(n, 2**i * e, n_prime) == n_prime-1:
                return False
        return True
    iteration = 25
    for i in range(iteration):
        random_a = random.randrange(2, e)
        if isComposite(random_a):
            return False
    return True

# Bagian Utama Program
if __name__ == '__main__':
    low_primes = []
    low_primes = sieve_of_eratosthenes(10000)
    while True:
        long_bit = 2048
        calon_prima = generateRandomPrime(long_bit, low_primes)
        if not Miller_Rabin(calon_prima):
            # Jika hasil prima random yang diambil gagal, 
            # akan diulang sampai ketemu
            continue
        else:
            # Bilangan berhasil melewati pengujian
            print("length of the prime: ", len(str(calon_prima)))
            print("result: ", calon_prima)
            break
 
