


# def test(dictt, N):
#     result = sorted(dictt, key=dictt.get, reverse=True)[:N]
#     return result 
# dictt = {'a':5, 'b':14, 'c': 32, 'd':35, 'e':24, 'f': 100, 'g':57, 'h':8, 'i': 100}
# print("\nOriginal Dictionary:")
# print(dictt)
# N = 1
# print("\n",N,"maximum value(s) in the said dictionary:")
# print(test(dictt, N))
# N = 2
# print("\n",N,"maximum value(s) in the said dictionary:")
# print(test(dictt, N))
# N = 5
# print("\n",N,"maximum value(s) in the said dictionary:")
# print(test(dictt, N))



def anjani(dict,n):
    re=sorted(dict,key=dict.get,reverse=True)[:n]
    return re

dictt = {'a':5, 'b':14, 'c': 32, 'd':35, 'e':24, 'f': 100, 'g':57, 'h':8, 'i': 100}
n=1
print(anjani(dictt,n))
n=2
print(anjani(dictt,n))
n=5
print(anjani(dictt,n))