from typing import Literal

noConn_blocks = (
    'activator_rail',
    'air',
    'amethyst_cluster',
    'anvil',
    'bamboo',
    'bamboo_fence',
    'bamboo_mosaic_slab',
    'bamboo_sapling',
    'bamboo_slab',
    'bed',
    'beetroot',
    'bell',
    'big_dripleaf',
    'blackstone_slab',
    'brewing_stand',
    'brown_mushroom',
    'cactus',
    'cake',
    'campfire',
    'carpet',
    'carrots',
    'cave_vines',
    'cave_vines_body_with_berries',
    'cave_vines_head_with_berries',
    'chain',
    'cherry_fence',
    'cherry_slab',
    'cobbled_deepslate_slab',
    'crimson_fence',
    'crimson_fungus',
    'crimson_roots',
    'crimson_slab',
    'cut_copper_slab',
    'daylight_detector',
    'daylight_detector_inverted',
    'deadbush',
    'deepslate_brick_slab',
    'deepslate_tile_slab',
    'detector_rail',
    'double_plant',
    'end_rod',
    'exposed_cut_copper_slab',
    'fence',
    'flowing_lava',
    'flowing_water',
    'flower_pot',
    'frame',
    'glass_pane',
    'glow_frame',
    'glow_lichen',
    'golden_rail',
    'grindstone',
    'hanging_roots',
    'iron_bars',
    'kelp',
    'ladder',
    'large_amethyst_bud',
    'lectern',
    'lever',
    'lightning_rod',
    'mangrove_fence',
    'mangrove_propagule',
    'mangrove_slab',
    'melon_stem',
    'medium_amethyst_bud',
    'moss_carpet',
    'mud_brick_slab',
    'nether_brick_fence',
    'nether_sprouts',
    'nether_wart',
    'oxidized_cut_copper_slab',
    'pitcher_plant',
    'pointed_dripstone',
    'polished_blackstone_brick_slab',
    'polished_blackstone_slab',
    'polished_deepslate_slab',
    'portal',
    'potatoes',
    'pumpkin_stem',
    'rail',
    'reeds',
    'red_flower',
    'red_mushroom',
    'redstone_torch',
    'redstone_wire',
    'sapling',
    'scaffolding',
    'sculk_vein',
    'seagrass',
    'sea_pickle',
    'small_amethyst_bud',
    'small_dripleaf_block',
    'snow_layer',
    'soul_campfire',
    'soul_lantern',
    'soul_torch',
    'spore_blossom',
    'stained_glass_pane',
    'standing_banner',
    'stone_block_slab',
    'stone_block_slab2',
    'stone_block_slab3',
    'stone_block_slab4',
    'stonecutter_block',
    'sweet_berry_bush',
    'tallgrass',
    'torch',
    'torchflower',
    'trip_wire',
    'tripwire_hook',
    'twisting_vines',
    'vine',
    'wall_banner',
    'warped_fence',
    'warped_fungus',
    'warped_roots',
    'warped_slab',
    'water',
    'waterlily',
    'waxed_cut_copper_slab',
    'waxed_exposed_cut_copper_slab',
    'waxed_oxidized_cut_copper_slab',
    'waxed_weathered_cut_copper_slab',
    'web',
    'weathered_cut_copper_slab',
    'weeping_vines',
    'wheat',
    'wither_rose',
    'wooden_slab'
)
dirs_per_connType = (
    # direction(s) to check for a wall that is connected to...
    (),             # neither positive nor negative side
    ('1',),         # positive side
    ('1', '-1'),    # both positive side & negative side
    ('-1',)         # negative side
)

if __name__ == "__main__":
    def _1d_to_2d(_1d: int, ax: int) -> str:
        """
        Converts a 1D direction vector to 2D based on given axis.
        """
        if ax == 'x':
            return f'^{_1d}^^'
        elif ax == 'y':
            return f'^^{_1d}^'
        elif ax == 'z':
            return f'^^^{_1d}'

    def recur_block(layer: Literal['x', 'y', 'z'], connType_prev: int = None, output: str = 'execute ') -> None:
        """
        :param layer:
        Must be 'x', 'y', or 'z'.
        Has 2 purposes:
            1. Indicates which layer of the tree we are in. 'z' or 'y' indicates layer 0, while 'x' indicates layer 1.
            2. Indicates the axis that the generated Minecraft commands will check.
        :param connType_prev:
            Stands for: Connection Type on the Previous axis.
            Store the type of connection (must be 0, 1, 2, 3 - see documentation on dirs_per_connType) on the axis used in the previous iteration. Note: Invalid when layer == 'z' or 'y'.
        :param output: Minecraft command to print
        """

        for connType, dirs in enumerate(dirs_per_connType):
            output2 = output

            for dir in dirs:
                for block in noConn_blocks:
                    output2 += f'unless block {_1d_to_2d(dir, layer)} {block} '

            if layer != 'x':
                recur_block('x', connType, output2)

            else:
                if connType_prev == connType == 0:
                    continue  # we don't want "/execute run event entity @s conn_x0z0"

                else:
                    print(output2 + f'run event entity @s conn_yz{connType_prev}x{connType}')

    def recur_entity(layer: Literal['x', 'y', 'z'], connType_prev: int = None, output: str = 'execute ') -> None:
        """
        See documentation on recur_block.
        """

        for connType, dirs in enumerate(dirs_per_connType):
            output2 = output

            for dir in dirs:
                output2 += f'positioned {_1d_to_2d(dir, layer)} if entity @e[r=0.01, c=1, type=rk:copycat_wall] '

            if layer != 'x':
                recur_entity('x', connType, output2)

            else:
                if connType_prev == connType == 0:
                    continue  # we don't want "/execute run event entity @s conn_x0z0"

                else:
                    print(output2 + f'run event entity @s conn_yz{connType_prev}x{connType}')


    print('# zx block')
    recur_block('z')
    print('\n# zx entity')
    recur_entity('z')
    print('\n# event add variant, set rotation, add hitbox\nevent entity @s is_standing0')

    print('\n# yx block')
    recur_block('y')
    print('\n# yx entity')
    recur_entity('y')
