from flight import flights
def sort_flights(flights,key,low_to_high):
    for i in range(len(flights)):
        for j in range(len(flights)-1-i):
            if low_to_high:
                if flights[j][key]>flights[j+1][key]:
                    flights[j],flights[j+1]=flights[j+1],flights[j]
            else:
                if flights[j][key]<flights[j+1][key]:
                    flights[j],flights[j+1]=flights[j+1],flights[j]


criteria = input('Enter Sorting Criteria: fare/duration: ')

# sort(flights)
sort_flights(flights, criteria, low_to_high=False)

for i in flights:
    print(i)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')