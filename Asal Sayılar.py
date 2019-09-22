# coding=utf-8

"""
    Girdiğimiz bir sayıya kadar ki asal olan bütün sayıları listeleme
"""


asal = []
deger=1
while 1:
    for i in range(deger*deger, (deger+1)*(deger+1)):
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = True
                break
        if not flag:
            asal.append(i)

    for i in asal:
        print(i)
    if(len(asal)!=0):
        deger += deger
    else:
        print("Buldunuz {}",deger)
        break

print("\n{} - {} arasında toplam {} tane asal sayı vardır.".format(deger*deger,(deger+1)*(deger+1), len(asal)))
