# Python 3.11.2
# 主要功能：寻找整数a、b之间的所有质数，返回用列表对象存储的质数
# 函数名称最后四位为版本号，版本号越高计算效率越高
# 创建时间：2023年4月13日


import time

# 版本号：v100
# 实现原理：根据质数定义，对于[a, b]之间每一个数字i，与从[2, i)之间的数字执行取余运算
#         如果没有发现可以与i整除的数，则判断i为质数
def find_prime_num_v100(a, b):
    start_time = time.time()
    s = []
    if a < 2:
        a = 2
    if a >= b:
        print('a larger than b or equal to b')
        return None
    rang = range(a,b+1)
    for i in rang:
        k = 0
        for j in range(2,i):  # 无脑机械执行
            if i % j == 0:
                k = j
                break
        if k == 0:
            s.append(i)
    end_time = time.time()
    print('find prime number in [%d, %d] cost time:'%(a, b) ,end_time-start_time)
    return s

def find_prime_num_v101(a, b):
    start_time = time.time()
    s = []
    if a < 2:
        a = 2
    if a >= b:
        print('a larger than b or equal to b')
        return None
    rang = range(a,b+1)
    
    for i in rang:
        k = 0
        for j in range(2,int(i ** 0.5)+1):  # 本质上是优化第二次循环次数
            if i % j == 0:
                k = j
                break
        if k == 0:
            s.append(i)
    end_time = time.time()
    print('find prime number in [%d, %d] cost time:'%(a, b) ,end_time-start_time)
    return s

def find_prime_num_v102(a, b):
    start_time = time.time()
    s = []
    s0a = []
    if a <= 2:
        a = 2
    else:
        s0a = find_prime_num_v102(2, a)
        s = s0a[:]
    if a >= b:
        print('a larger than b or equal to b')
        return None
    rang = range(a,b+1)
    
    for i in rang:
        k = 0
        temp = int(i ** 0.5)
        for j in s:  # 使用已找到的素数优化第二次循环次数
            if j >= temp + 1:
                break
            if i % j == 0:
                k = j
                break
        if k == 0:
            s.append(i)
    if s0a != []:
        del s[0: len(s0a)]
    end_time = time.time()
    print('find prime number in [%d, %d] cost time:'%(a, b) ,end_time-start_time)
    return s

def find_prime_num_v110(a, b):
    start_time = time.time()
    s = []
    s0a = []
    if a <= 2:
        s = [2]
        a = 2
    else:
        s0a = find_prime_num_v110(2, a)
        s = s0a[:]
    if a >= b:
        print('a larger than b or equal to b')
        return None
    
    rang = None
    if a % 2 == 0:
        # 缩减所有偶数进一步减少搜索范围，不过偶数并不是导致时间增加的主要原因
        # 所以只筛掉偶数不一定可以提升速度
        rang = range(a+1, b+1, 2)
    else:
        rang = range(a, b+1, 2)
    
    #rang = range(a, b+1)
    for i in rang:
        k = 0
        temp = int(i ** 0.5)
        for j in s:  # 使用已找到的素数优化第二次循环次数
            if j >= temp + 1:
                break
            if i % j == 0:
                k = j
                break
        if k == 0:
            s.append(i)
    if s0a != []:
        del s[0: len(s0a)]
    end_time = time.time()
    print('find prime number in [%d, %d] cost time:'%(a, b) ,end_time-start_time)
    return s

def find_prime_num_v200(a, b):
    start_time = time.time()

    # 获得[0, √b]之间的所有素数
    s = find_prime_num_v110(0, int(b ** 0.5))
    if s is None:
        return s

    if a < 2:
        a = 2
    rang = [True] * (b + 1)  # {i: True for i in range(a, b+1)}
    
    for i in s:
        temp = int(a/i)+1
        if temp < 2:
            temp = 2
        # 通过将质因子倍数筛掉，确认所有质因子倍数均被筛掉后，那么剩下的只能是质数
        # 这个算法的缺陷在于质因子乘的倍数包含了被筛掉掉数字，那么他们乘积必然也被筛过
        # 所以这个算法重复执行了很多工作
        for j in range(temp * i, b+1, i):
            rang[j] = False

    s = []
    for i in range(a, b+1):
        if rang[i] == True:
            s.append(i)
    
    end_time = time.time()
    print('find prime number in [%d, %d] cost time:'%(a, b) ,end_time-start_time)
    return s

def find_prime_num_v201(a, b):
    start_time = time.time()
    if a < 2:
        a = 2

    rang = {i : True for i in range(2, b+1)}

    # 第一层搜索范围为[2, √b]范围内的数字，[a, b]范围内的合数在这个范围内必然有质因子
    for i in range(2, int(b ** 0.5)+1):
        if rang[i]:
            # 第二层必须使得i*j小于等于b
            for j in range(i, int(b / i) + 1):
                rang[i * j] = False

    s = []
    for i in range(a, b+1):
        if rang[i] == True:
            s.append(i)
    
    end_time = time.time()
    print('find prime number in [%d, %d] cost time:'%(a, b) ,end_time-start_time)
    return s

def find_prime_num_v202(a, b): # testing
    start_time = time.time()
    if a < 2:
        a = 2

    rang = [True] * (b + 1)  # {i : True for i in range(2, b+1)}
    s = []

    for i in range(2, b+1):
        if rang[i]:
            s.append(i)
        for j in s:
            k = i * j
            if k > b:
                break
            rang[k] = False
            if i % j == 0:
                break
    for i in s:
        if i >= a:
            break
        s.remove(i)
    
    end_time = time.time()
    print('find prime number in [%d, %d] cost time:'%(a, b) ,end_time-start_time)
    return s


v202 = find_prime_num_v202(0, 10000000)
v201 = find_prime_num_v201(0, 10000000)
v200 = find_prime_num_v200(0, 10000000)
# v110 = find_prime_num_v110(0, 10000000)
# v102 = find_prime_num_v102(0, 10000000)
# v101 = find_prime_num_v101(0, 10000000)
# v100 = find_prime_num_v100(0, 100000)
'''
if v100 == v101:
    print('v100 == v101')

if v110 == v200:
    print('v110 == v200')
'''
if v200 == v201:
    print('v200 == v201')

if v200 == v202:
    print('v200 == v202')
