play_data = {
    'result' : '승리',
    'chame_name' : '비에고',
    'kill' : 13,
    'death' : 9,
    'assist' : 13
}

# keys()
for key in play_data.keys():
    print(key)

# values()
for value in play_data.values():
    print(value)

# items()
for key, value in play_data.items():
    print(key, value)