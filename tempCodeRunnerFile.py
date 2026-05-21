rooms=[[[False for r in range(20)]for f in range(15)] for t in range(3)]
print(rooms)
rooms[1][9][13]=True
rooms[1][9][1]=True

vacancy = 0
for room_number in range(20):
    if not rooms[1][9][room_number]:
        vacancy += 1
print("vacancy in 3rd 15th floor of 3rd building: ", vacancy)