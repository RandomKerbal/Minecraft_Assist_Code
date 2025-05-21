variants = ('fence', 'mangrove_fence', 'cherry_fence', 'pale_oak_fence', 'bamboo_fence', 'crimson_fence', 'warped_fence', 'nether_brick_fence')
adjs = ('~1~~', '~-1~~', '~~~1', '~~~-1', '~~1~', '~~-1~')

if __name__ == "__main__":
    for adj in adjs:
        print()
        print()
        count = 0
        for var in variants:
            if count == 4:
                print()

            output = ''
            output += '"/execute at @s if block '
            output += adj
            output += ' '
            output += var
            output += ' run tp @s '
            output += '~~-1.5~' if adj == '~~-1~' else adj
            output += ' 0 0",'
            print(output)

            count += 1