from knot_fence_ac import variants, tag
adjs_x = ('~1~~', '~-1~~')
adjs_z = ('~~~1', '~~~-1')

print('Note: Command line starts as even (tag already existed)!', end='\n\n')
for adj_x in adjs_x:
    for adj_z in adjs_z:
        output = '"/execute at @s '
        for var in variants[:-1]:
            output += f'unless block {adj_x} {var} '

        for var in variants[:-1]:
            output += f'unless block {adj_z} {var} '

        output += f'run tag @s remove {tag}",'
        print(output)

        print(f'"/execute at @s if block {adj_x} {variants[-1]} run tag @s add {tag}",')
        print(f'"/execute at @s if block {adj_z} {variants[-1]} run tag @s add {tag}",')

        print(f'"/event entity @s[tag={tag}] horizontal0"', end='\n\n')

        # Recheck with 180 rotation
        adj_x = adjs_x[1 - adjs_x.index(adj_x)]
        adj_z = adjs_z[1 - adjs_z.index(adj_z)]
        output = '"/execute at @s '

        print()