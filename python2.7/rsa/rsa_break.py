# import primefac as pf
from primefac import *
import multiprocessing
import math
#we are going to break the 10 digit p and q values 
#  p  = 1500450271 
#  q  = 3628273133 
# n = 5444043405671869043
# 7256546266L
# 9576890767 
# 3628273133 
print("***********************")
print("first 10 digit p and 10 digit q the 20 digit n ")

# 34747575467581863011L
# 20 digit prime numbers
# n = 2630492240413883318777134293253671517529
#  p = 48112959837082048697 
# q  = 54673257461630679457 
# 72191103626161875816648846887
# n = 174566959525992854403922757701L
# print("this is factorization of n the p or q value in elliptic curve",p,q)
n = int(input("enter the number  ; ")) 
p =  ecm(n, B1=10, B2=30)
q = n/p
if q < p:
    q = n/p

m = mpqs(n)
print("this is factorization of n the p or q value in quadratic sieve method ",m,q)


def ecm(n, B1=10, B2=20):       
    if isprime(n): return n
    m = ispower(n)
    if m: return m
    iters = 1
    while True:
        for _ in xrange(iters):                
            seed = randrange(6, n)
            u, v = (seed**2 - 5) % n, 4*seed % n
            p = pow(u, 3, n)
            Q, C = (pow(v-u,3,n)*(3*u+v) % n, 4*p*v % n), (p, pow(v,3,n))
            pg = primegen()
            p = pg.next()
            while p <= B1: Q, p = ecmul(p**ilog(B1, p), Q, C, n), pg.next()
            g = gcd(Q[1], n)
            if 1 < g < n: return g
            while p <= B2:
                Q = ecmul(p, Q, C, n)
                g *= Q[1]
                g %= n
                p = pg.next()
            g = gcd(g, n)
            if 1 < g < n: return g
            
        B1 *= 3
        B2 *= 3
        iters *= 2
