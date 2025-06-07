variants = ('fence', 'mangrove_fence', 'cherry_fence', 'bamboo_fence', 'crimson_fence', 'warped_fence', 'nether_brick_fence', 'pale_oak_fence')
adjs = ('~1~~', '~-1~~', '~~~1', '~~~-1', '~~1~', '~~-1~')
tag = 'NoFence_if_odd_else_HasFence'

if __name__ == "__main__":
    for adj in adjs:
        if adjs.index(adj) % 2 == 0:
            add = 'add'
            remove = 'remove'
            NOT = '!'
        else:
            add = 'remove'
            remove = 'add'
            NOT = ''

        print()
        output = '"/execute at @s'

        for var in variants[:-1]:
            output += f' unless block {adj} {var}'

        output += f' run tag @s {add} {tag}",'
        print(output)

        print(f'"/execute at @s if block {adj} {variants[-1]} run tag @s {remove} {tag}",')
        print(f'"/tp @s[tag={NOT}{tag}] {adj} 0 0",')


# for adj in adjs:
#     print()
#
#     for var in variants:
#         output = ''
#         output += '"/execute at @s if block '
#         output += adj
#         output += ' '
#         output += var
#         output += ' run tp @s '
#         output += adj
#         output += ' 0 0",'
#         print(output)