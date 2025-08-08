adjs = ('~1~~', '~-1~~', '~~~1', '~~~-1', '~~1~', '~~-1~')
states = ('standing', 'side', 'hanging')
states2 = ('0', '1', '2', '3',)

if __name__ == "__main__":
    for adj in adjs:
        output = f'"/execute if block {adj} grindstone run tp @s {adj} 0 0"'
        print(output)

    print()

    for state in states:
        print()

        for state2 in states2:
            if not (state == 'standing' and state2 == '0'):
                output = rf'"/execute if block ~~~ grindstone [\"attachment\"=\"{state}\", \"direction\"={state2}] run event entity @s is_{state}{state2 if state == 'side' else str(int(state2) % 2)}",'
                print(output)