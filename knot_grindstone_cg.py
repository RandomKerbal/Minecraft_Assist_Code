from knot_grindstone_ac import states, states2

if __name__ == "__main__":
    for i, state in enumerate(states):
        for state2 in states2:
            if not ((state == 'standing' and state2 in ('0', '2', '3',)) or (state == 'hanging' and state2 in ('2', '3',))):
                output = ''
                output += '"is_'
                output += state
                output += state2
                output += '":{"minecraft:variant":{"value":'
                output += str(i)
                output += state2
                output += '}},'
                print(output)
        print()