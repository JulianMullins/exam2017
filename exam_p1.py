trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
         '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}



def speak_Chinese(number):
    '''
    number: an integer, 0<=number<=999

    Returns: a string that is the number in Chinese
    '''
    zero = trans[str(0)]
    ten = trans[str(10)]
    hundred = trans[str(100)]

    if number < 0 or number > 999:
        return "Number is out of range"
    else:
        if number <= 10 or number == 100:
            return trans[str(number)]
        elif number <= 19:
            return ten + " " + trans[str(number)[1]]
        elif number <= 99:
            if str(number)[1] == str(0):
                return trans[str(number)[0]] + " " + ten
            else:
                return trans[str(number)[0]] + " " + ten + " " + trans[str(number)[1]]
        elif number <= 999:
            if str(number)[1] == str(0):
                if str(number)[2] == str(0):
                    return trans[str(number)[0]] + " " + hundred
                else:
                    return trans[str(number)[0]] + " " + hundred + " " + zero + " " + trans[str(number)[2]]
            else:
                return trans[str(number)[0]] + " " + hundred + " " + trans[str(number)[1]] + " " + ten + " " + trans[str(number)[2]]


# For testing
def main():
    print(speak_Chinese(9))
    print('In Chinese: 9 = jiu')
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(200))
    print('In Chinese: 200 = er bai')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()