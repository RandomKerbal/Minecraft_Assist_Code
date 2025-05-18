from knot_fence_ac import adjs
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
            if not ((state == 'standing' and state2 in ('0', '2', '3',)) or (state == 'hanging' and state2 in ('2', '3',))):
                output = ''
                output += r'"/execute at @s if block ~~~ grindstone [\"attachment\"=\"'
                output += state
                output += r'\", \"direction\"='
                output += state2
                output += '] run event entity @s is_'
                output += state
                output += state2
                output += '",'
                print(output)
        print()