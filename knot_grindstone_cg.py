from knot_grindstone_ac import states, states2

if __name__ == "__main__":
    for i, state in enumerate(states):
        print()

        for state2 in states2:
            if state in ('standing', 'hanging') and state2 in ('2', '3'):
                continue

            else:
                output = ''
                output += '"is_'
                output += state
                output += state2
                output += '":{"minecraft:variant":{"value":'
                output += str(i)
                output += state2
                output += '},"minecraft:custom_hit_test":{"hitboxes":[{"width": 0.4,"height":0.875,"pivot":['
                # x-offset
                x = 0
                if state == 'side':
                    if state2 == '1':
                        x -= 0.125
                    elif state2 == '3':
                        x += 0.125
                output += str(x)

                # y-offset
                if state == 'standing':
                    output += ',0.625,'
                elif state == 'hanging':
                    output += ',0.375,'
                else:
                    output += ',0.5,'

                # z-offset
                z = 0
                if state == 'side':
                    if state2 == '0':
                        z += 0.125
                    elif state2 == '2':
                        z -= 0.125
                output += str(z)

                output += ']}]}},'
                print(output)