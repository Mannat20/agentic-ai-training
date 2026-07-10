flight1 = {
    'code': '6E6673',
    'carrier': 'indigo',
    'source': 'delhi',
    'destinition': 'bengaluru',
    'fare': 5000,
    'duration': 3.5
}


flight2 = {
    'code': 'AI5962',
    'carrier': 'air india',
    'source': 'delhi',
    'destinition': 'bengaluru',
    'fare': 3500,
    'duration': 3
}

flight3 = {
    'code': 'AI2973',
    'carrier': 'air india',
    'source': 'delhi',
    'destinition': 'bengaluru',
    'fare': 6000,
    'duration': 2.5
}

flight4 = {
    'code': '6E2314',
    'carrier': 'indigo',
    'source': 'delhi',
    'destinition': 'bengaluru',
    'fare': 2500,
    'duration': 5
}

flight5 = {
    'code': '6E810',
    'carrier': 'indigo',
    'source': 'delhi',
    'destinition': 'bengaluru',
    'fare': 9000,
    'duration': 2
}

# List of Dictionaries
#.              0       1       2        3        4
flights = [flight1, flight2, flight3, flight4, flight5]

# 1. Search a Flight - code
# 2. Sort Flights - fare, duration
# 3. Filter Flights - carrier, price (> <), duration <


def search_flight(flights,code):
    for flight in flights:
        if flight['code']==code:
            print('Flight Found ',flight)
            break
    else:
        print('Flight Not Found ',code)

def main():
    code=input('Enter Flight Code to Search: ')
    search_flight(flights,code)
if __name__=='__main__':
    main()