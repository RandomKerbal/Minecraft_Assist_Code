adjs = ('~1~~', '~-1~~', '~~~1', '~~~-1', '~~1~', '~~-1~')
states = ('standing', 'side', 'hanging')
states2 = ('0', '1', '2', '3',)

if __name__ == "__main__":
    for adj in adjs:
        output = ''
        output += '"/execute at @s if block '
        output += adj
        output += ' grindstone run tp @s '
        output += adj
        output += ' 0 0"'
        print(output)
    print()

    for state in states:
        for state2 in states2:
            if not (state == 'standing' and state2 == '0'):
                output = ''
                output += r'"/execute at @s if block ~~~ grindstone [\"attachment\"=\"'
                output += state
                output += r'\", \"direction\"='
                output += state2
                output += '] run event entity @s is_'
                output += state
                output += state2 if state == 'side' else str(int(state2) % 2)
                output += '",'
                print(output)
        print()