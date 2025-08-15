armType: int
"""
Must be 0, 1, 2, 3. An armType means how a wall is connected to adjacent blocks:

armType0 = [ air ] [wall] [ air ]

armType1 = [block] [wall] [ air ]

armType2 = [block] [wall] [block]

armType3 = [ air ] [wall] [block]
"""


def _1d_to_2d(_1d: int, ax: int) -> str:
    """
    Converts a 1D direction vector into 2D based on given axis.
    """
    if ax == 'x':
        return f'^{_1d}^^'
    elif ax == 'y':
        return f'^^{_1d}^'
    elif ax == 'z':
        return f'^^^{_1d}'


def armCount(armType_prev: int, armType: int) -> int:
    """
    Step 1: converts the type of arm (must be 0, 1, 2, 3 - see documentation on armType) on each axis into the number of arms.
    Examples:
        - armType = 1 -> 1 arm
        - armType = 2 -> 2 arms
        - armType = 3 -> 1 arm
    Step 2: total the number of arms on both axes.
    """
    armType_prev = armType_prev if armType_prev != 3 else 1
    armType = armType if armType != 3 else 1

    return armType_prev + armType


def recur(b_or_e: str, ax: str, armType_prev: int = None, output_prev: str = 'execute ') -> None:
    """
    :param b_or_e:
    Must be 'b' or 'e'.

    'b':
        Stands for: "block".
        Generate Minecraft commands that check for adjacent blocks.
    'e':
        Stands for: "entity".
        Generate Minecraft commands that check for adjacent copycat wall entities.

    :param ax:
    Must be 'x', 'y', or 'z'.

    Has 2 purposes:
        1. Indicates the axis that the generated Minecraft commands will check.
        2. Indicates which layer of the tree we are in. 'z' or 'y' indicates layer 0, while 'x' indicates layer 1.

    :param armType_prev:
        Stands for: Arm Type on the Previous axis.
        Store the type of arm (must be 0, 1, 2, 3 - see documentation on armType) on the axis in the previous iteration. Note: Invalid when layer == 'z' or 'y'.

    :param output_prev: Minecraft commands generated with the axis in the previous iteration
    """

    for armType, dirs in enumerate(dirs_per_armType):
        output = output_prev

        if b_or_e == 'b':
            for dir in dirs:
                for block in noArm_blocks:
                    output += f'unless block {_1d_to_2d(dir, ax)} {block} '

        elif b_or_e == 'e':
            for dir in dirs:
                output += f'positioned {_1d_to_2d(dir, ax)} if entity @e[r=0.01, c=1, type=rk:copycat_wall] '

        if ax != 'x':
            recur(b_or_e, 'x', armType, output)

        else:
            if armType_prev == armType == 0:
                continue  # we don't want "/execute run event entity @s arm_x0z0"

            else:
                outputs[armCount(armType_prev, armType)-1] += (output + f'run event entity @s arm_yz{armType_prev}x{armType}\n')


def outputs_reset() -> None:
    global outputs
    outputs = ["", "", "", ""]
    """
    index = total number of arms; value = generated Minecraft commands
    """
    outputs_newl('b')
    return


def outputs_newl(b_or_e: str) -> None:
    global outputs
    for i in range(len(outputs)):
        outputs[i] += f'\n# {"block" if b_or_e == 'b' else "entity"}\n'
    return


noArm_blocks = (
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
noArm_blocks = ('_',)

dirs_per_armType = (
    # index = armType (see documentation on armType); value = direction(s) to check with the specified armType.
    (),             # neither positive nor negative side
    ('1',),         # positive side
    ('1', '-1'),    # both positive side & negative side
    ('-1',)         # negative side
)

if __name__ == "__main__":

    for ax in ('y', 'z'):
        outputs_reset()
        recur('b', ax)
        outputs_newl('e')
        recur('e', ax)
        for armNum, output in enumerate(outputs):
            armNum += 1
            print(f"# check if {armNum} arm{'s' if armNum != 1 else ''} in {ax}x plane{output}")

    print('# event add variant, set rotation, add hitbox\nevent entity @s is_standing0\n')  # only for ax == 'z'