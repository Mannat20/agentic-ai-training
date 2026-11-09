from functools import reduce
flights = [
    {
        "flight_name": "Air India",
        "flight_no": "AI 7713",
        "source": "Delhi",
        "destination": "Zurich",
        "price": 5500,
        "duration": 6
    },
    {
        "flight_name":"Swiss",
        "flight_no": "LX 2646",
        "source": "Zurich",
        "destination": "Delhi",
        "price": 6200,
        "duration": 1.5
    }
]

print(flights)
discounted_flights = list(map(lambda flight: {
        **flight,
        "price":flight['price'] * 0.5
    },flights))
print(discounted_flights)

fast_flights = list(filter(lambda flight: flight['duration']>2,flights))
print(fast_flights)

total_price = reduce(lambda flight1,flight2: flight1['price']+flight2['price'],flights)
print(total_price)