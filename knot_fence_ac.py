from knot_fence_inside_block_notifier import variants
adjs = ('~1~~', '~-1~~', '~~1~', '~~-1~', '~~~1', '~~~-1')

if __name__ == "__main__":
    for adj in adjs:
        for var in variants:
            output = ''
            output += '"/execute at @s if block '
            output += adj
            output += ' '
            output += var
            output += ' run tp @s '
            output += adj
            output += ' 0 0",'
            print(output)
        print()