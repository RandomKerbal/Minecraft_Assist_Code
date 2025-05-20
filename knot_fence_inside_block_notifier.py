variants = ('oak_fence', 'spruce_fence', 'birch_fence', 'jungle_fence', 'acacia_fence', 'dark_oak_fence', 'mangrove_fence', 'cherry_fence', 'pale_oak_fence', 'bamboo_fence', 'crimson_fence', 'warped_fence', 'nether_brick_fence')

if __name__ == "__main__":
    output = ''
    for var in variants:
        output += '{"block": {"name": "minecraft:'
        output += var
        output += '"},"entered_block_event": {"event": "is_in_block","target": "self"},"exited_block_event": {"event": "pick_up","target": "self"}},'

    output = output[:-1]  # removes comma at the end

    print(output)