room_for_search = int(input('Номер искомой комнаты: '))

block = 1
first_room = 1
stage = 1

while room_for_search >= first_room + block ** 2:
    first_room = first_room + block ** 2
    stage += block
    block += 1

stage += ((room_for_search - first_room) // block)
room_sequence = int((room_for_search - first_room) % block + 1)

print(stage, room_sequence)
