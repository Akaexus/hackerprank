def validCelsius(c):
    return c >= -273.25

def validKelvin(k):
    return k >= 0

def validFahrenheit(f):
    return f >= -459.67


def Celsius2Kelvin(c):
    if not validCelsius(c):
        return None
    else:
        return c + 273.15

def Kelvin2Celsius(k):
    if not validKelvin(k):
        return None
    else:
        return k - 273.15

def Celsius2Fahrenheit(c):
    if not validCelsius(c):
        return None
    return c * 9 / 5 + 32

def Fahrenheit2Celsius(c):
    if not validCelsius(c):
        return None
    return (c - 32) * 5 / 9

def Fahrenheit2Kelvin(f):
    if not validFahrenheit(f):
        return None
    return Celsius2Kelvin(Fahrenheit2Celsius(f))

def Kelvin2Fahrenheit(k):
    if not validKelvin(k):
        return None
    return Celsius2Fahrenheit(Kelvin2Celsius(k))

while True:
    try:
        value, baseTemp, destTemp = input().split(' ')
    except EOFError:
        break
    scales = ['Kelvin', 'Fahrenheit', 'Celsius']
    if baseTemp in scales and destTemp in scales:
        temp = globals()['{}2{}'.format(baseTemp, destTemp)](int(value))
        if temp == None:
            print('NO')
        else:
            print('{0:0.2f}'.format(temp))