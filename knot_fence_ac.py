variants = ('fence', 'mangrove_fence', 'cherry_fence', 'pale_oak_fence', 'bamboo_fence', 'crimson_fence', 'warped_fence', 'nether_brick_fence')
adjs = ('~1~~', '~-1~~', '~~~1', '~~~-1', '~~1~', '~~-1.5~')

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