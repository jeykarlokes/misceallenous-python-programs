# import primefac as pf
from primefac import ecm
import multiprocessing
import math
# n = 32331814254917753352786760682821529706480829142993L
# p = 48112959837082048697
# q  = 671998030559713968361666935769
n = int(input("enter the number  ; ")) 
p =  ecm(n, B1=10, B2=20)
print("this is factorization of n the p or q value in elliptic curve",p)

m = mpqs(n)
print("this is factorization of n the p or q value in quadratic sieve method ",m)


