from knot_grindstone_ac import states, states2
import math


def str_int0(val: float) -> str:
    return '0' if val == 0.0 else str(val)


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
                output += '},"minecraft:custom_hit_test":{"hitboxes":[{"width":0.4,"height":0.875,"pivot":['

                # x-offset
                x = 0
                if state == 'side':
                    x = 0.125 * -math.sin(int(state2) * math.pi/2)
                output += str_int0(round(x, 3))

                # y-offset
                output += f',{str(0.625 - 0.125*i)},'

                # z-offset
                z = 0
                if state == 'side':
                    z = 0.125 * math.cos(int(state2) * math.pi/2)
                output += str_int0(round(z, 3))

                output += ']}]}},'
                print(output)