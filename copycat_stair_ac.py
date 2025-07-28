variants = ('oak_stairs', 'spruce_stairs', 'birch_stairs', 'jungle_stairs', 'acacia_stairs', 'dark_oak_stairs', 'mangrove_stairs', 'cherry_stairs', 'bamboo_stairs', 'bamboo_mosaic_stairs', 'crimson_stairs', 'warped_stairs', 'normal_stone_stairs', 'granite_stairs', 'polished_granite_stairs', 'diorite_stairs', 'polished_diorite_stairs', 'andesite_stairs', 'polished_andesite_stairs', 'stone_stairs', 'mossy_cobblestone_stairs', 'stone_brick_stairs', 'mossy_stone_brick_stairs', 'brick_stairs', 'end_brick_stairs', 'nether_brick_stairs', 'red_nether_brick_stairs', 'sandstone_stairs', 'smooth_sandstone_stairs', 'red_sandstone_stairs', 'smooth_red_sandstone_stairs', 'quartz_stairs', 'smooth_quartz_stairs', 'purpur_stairs', 'prismarine_stairs', 'prismarine_bricks_stairs', 'dark_prismarine_stairs', 'blackstone_stairs', 'polished_blackstone_stairs', 'polished_blackstone_brick_stairs', 'cut_copper_stairs', 'exposed_cut_copper_stairs', 'weathered_cut_copper_stairs', 'oxidized_cut_copper_stairs', 'waxed_cut_copper_stairs', 'waxed_exposed_cut_copper_stairs', 'waxed_weathered_cut_copper_stairs', 'waxed_oxidized_cut_copper_stairs', 'cobbled_deepslate_stairs', 'polished_deepslate_stairs', 'deepslate_brick_stairs', 'deepslate_tile_stairs', 'mud_brick_stairs', 'pale_oak_stairs')
weirdoDirs_per_copycatDir = {
    'z': ('0', '1'),
    'x': ('2', '3')
}
"""
key = direction that copycat stair is facing; val = weirdo_direction(s) of the real stair in which the copycat stair needs to change shape
"""
rot_per_weirdoDirs = {
    '0': ('45', '135'),  # west
    '1': ('-135', '-45'),  # east
    '2': ('135', '-135'),  # north
    '3': ('-45', '45')  # south
}
"""
key = weirdo_direction of a real stair
val = (
    minimum y rotation required for a copycat stair to face the same direction as a real stair with the weirdo_direction
    maximum y rotation required for a copycat stair to face the same direction as a real stair with the weirdo_direction
)
"""
tag = 'not_weirdoDir'

if __name__ == "__main__":
    for copycat_dir, weirdo_dirs in weirdoDirs_per_copycatDir.items():
        print(f'\n{copycat_dir}+-')

        for weirdo_dir in weirdo_dirs:
            output = f'execute'

            for upside_down_bit in ('false', 'true'):
                for var in variants[:-1]:
                    output += f' unless block ~~~ {var} ["weirdo_direction"={weirdo_dir}, "upside_down_bit"={upside_down_bit}]'
            output += f'unless entity @e[r=0.01, c=1, type=rk:copycat_stair, rym={rot_per_weirdoDirs[weirdo_dir][0]}, ry={rot_per_weirdoDirs[weirdo_dir][1]}]'
            output += f' run tag @s add {tag}{'0or2' if weirdo_dir in ('0', '2') else '1or3'}'
            print(output)

        print(f'function tag_weirdoDir/{copycat_dir}_newBlocks')

        for weirdo_dir in weirdo_dirs:
            for upside_down_bit in ('false', 'true'):
                print(f'execute if block ~~~ {variants[-1]} ["weirdo_direction"={weirdo_dir}, "upside_down_bit"={upside_down_bit}] run tag @s remove {tag}{'0or2' if weirdo_dir in ('0', '2') else '1or3'}')