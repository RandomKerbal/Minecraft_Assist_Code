from knot_grindstone_ac import states

if __name__ == "__main__":
    for i, state in enumerate(states):
        if state != 'standing':
            output = ''
            output += '"is_'
            output += state
            output += '":{"minecraft:variant":{"value":'
            output += str(i)
            output += '}},'
            print(output)