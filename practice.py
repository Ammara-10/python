# numbers= [1,2,3,4,5,6,7]
# number_length=len(numbers)
# def avg(numbers):
#     return sum(numbers) / number_length
#
# avg(numbers)
# print(avg(numbers))

response = [
    {
        'coins': [
            {
                'BTCUSDT': {'price': 50000, 'volume': '1B'}
             },
            {
                'ETHUSDT': {'price': 2000, 'volume': '500M'}
            },
        ],
    }
]




print(response[0]['coins'][1]['ETHUSDT']['volume'])
