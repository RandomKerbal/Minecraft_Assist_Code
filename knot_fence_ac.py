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

        output = '\n"/execute'

        for var in variants[:-1]:
            output += f' unless block {adj} {var}'

        output += f' run tag @s {add} {tag}",'
        print(output)

        print(f'"/execute if block {adj} {variants[-1]} run tag @s {remove} {tag}",')
        print(f'"/tp @s[tag={NOT}{tag}] {adj} 0 0",')