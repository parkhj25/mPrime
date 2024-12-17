import math

# 1. 소수 판별 알고리즘
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# 2. 메르센 소수 판별 알고리즘
def is_mersenne_prime(n):
    
    if not is_prime(n):
        return False
    
    mersenne_number = 2**n - 1
    return is_prime(mersenne_number)

# 계산
n = 7
if is_mersenne_prime(n):
    print(f"{2**n - 1}는 메르센 소수입니다.")
else:
    print(f"{2**n - 1}는 메르센 소수가 아닙니다.")
