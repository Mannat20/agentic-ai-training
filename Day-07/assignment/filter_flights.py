from flight import flights

def filter_flights(flights, key):
    
    if key=='carrier':
        carrier=input('Enter Carrier Name: ')
        for flight in flights:
            if flight['carrier']==carrier:
                print(flight)
    elif key=='fare':
        number1=int(input('Enter lower amount of price range: '))
        number2=int(input('Enter higher amount of price range: '))
        for flight in flights:
            if number1<=flight['fare']<=number2:
                print(flight)
    elif key=='duration':
        number1=float(input('Enter lower duration of flight: '))
        number2=float(input('Enter higher duration of flight: '))
        for flight in flights:
            if number1<=flight['duration']<=number2:
                print(flight)
    else:
        print('Invalid Key')


def main():
    key=input('Enter Filtering Criteria: carrier/fare/duration: ')
    filter_flights(flights,key)
if __name__=='__main__':
    main()