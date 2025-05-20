from knot_grindstone_ac import states

if __name__ == "__main__":
    for i, state in enumerate(states):
        if state != 'standing':
            output = '"is_'
            output += state
            output += '":{"add":{"component_groups":["is_'
            output += state
            output += '"]}},'
            print(output)
