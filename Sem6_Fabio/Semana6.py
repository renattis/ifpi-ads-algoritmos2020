howManyNumbers = int(input('Quantos valores pretende digitar: '))
array = []
for number in range(0, howManyNumbers):
    n = int(input('Digite um número: '))
    array.append( n )



def isPair( n ):
    return n % 2 == 0
def isPositive(n):
    return n >= 0


def parseNumbersInArray( array ):
    for i in range(len(array)):
        if( isPositive(array[i]) ):
            array[i] = array[i] * 2
        else:
            array[i] = array[i] / 2
    return array

def showTypeNumbers( array ):
    for n in array:
        print('-' * 20)
        if( isPair( n ) ):
            print('{} é par'.format(n))
        else:
            print('{} é ímpar'.format(n))

        if( isPositive(n) ):
            print('{} é positivo'.format(n))
        else:
            print('{} é negativo'.format(n))

def mediaNumbersIn( array ):
    media = 0
    for n in array:
        media += n
    return media / len(array)



showTypeNumbers( array )

array = parseNumbersInArray(array)

print('-+' * 40)

showTypeNumbers( array )

print('-+' * 40)

print('média ->', mediaNumbersIn(array) )
