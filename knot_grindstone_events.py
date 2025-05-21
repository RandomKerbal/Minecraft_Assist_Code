from knot_grindstone_ac import states, states2

if __name__ == "__main__":
    for i, state in enumerate(states):
        print()

        for state2 in states2:
            if state in ('standing', 'hanging') and state2 in ('2', '3'):
                continue

            else:
                output = '"is_'
                output += state + state2
                output += '":{"add":{"component_groups":["is_'
                output += state + state2
                output += '"]}},'
                print(output)