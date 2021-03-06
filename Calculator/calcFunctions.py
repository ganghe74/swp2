from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        if n > 100000:
            return 'Error!'
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    result=''
    try:

        n = int(numStr)
        ##움수일 경우에 앞에 음수부호를 붙일수 있도록 함
        if numStr[0]=='-':
            result='-'
            n=int(numStr)
            n*=-1
    except:
        return 'Error!'
    
    if n>= 4000:
        return 'Error!'
    if n==0:
        return 'Zero'
    
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]


    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result

def romanToDec(romanNumStr):
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]
    romanNumStrBackup = romanNumStr
    result = 0
    for value, letters in romans:
        while romanNumStr[:len(letters)] == letters:
            romanNumStr = romanNumStr[len(letters):]
            result += value

    if decToRoman(str(result)) != romanNumStrBackup:
        return 'Error!'
    return result
