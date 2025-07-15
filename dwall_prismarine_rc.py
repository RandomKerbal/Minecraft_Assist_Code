condition = 'math.mod(math.floor(query.time_stamp/300),21)'
frame_to_ind = {
    0: 0,
    1: 1,
    2: 0,
    3: 2,
    4: 0,
    5: 3,
    6: 0,
    7: 1,
    8: 2,
    9: 1,
    10: 3,
    11: 1,
    12: 0,
    13: 2,
    14: 1,
    15: 2,
    16: 3,
    17: 2,
    18: 0,
    19: 1,
    20: 1,
    21: 3
}
bracket_count = 0
output = ''

for frame in range(21):  # up to 20 because last frame (frame 21) expression is different - doesn't need condition.
    output += f'{condition} == {frame} ? {frame_to_ind[frame]}/4 : ('
    bracket_count += 1

# write last frame expression separately
output += f'{frame_to_ind[21]}/4'
output += ')'*bracket_count

print(output)