import json
from dfence_entity_bp import variants
textures = {
    'dark_oak': 'planks_big_oak',
    'mangrove': 'mangrove_planks',
    'cherry': 'cherry_planks',
    'pale_oak': 'pale_oak_planks',
    'bamboo': 'bamboo_planks',
    'crimson': 'huge_fungus/crimson_planks',
    'warped': 'huge_fungus/warped_planks',
    'nether_brick': 'nether_brick'
}
sounds_spawn = {
    'cherry': 'place.cherry_wood',
    'bamboo': 'place.bamboo_wood',
    'crimson': 'place.nether_wood',
    'warped': 'place.nether_wood'
}
sounds_despawn = {
    'cherry': 'break.cherry_wood',
    'bamboo': 'break.bamboo_wood',
    'crimson': 'break.nether_wood',
    'warped': 'break.nether_wood'
}

if __name__ == "__main__":
    for var in variants:
        filename = f'dfence_{var}.json'
        with open(f'D:\\My Downloads\\dfence_rp\\{filename}', 'w') as f:
            data = f'''
#
  "format_version": "1.10.0",
  "minecraft:client_entity":#
    "description":#
      "identifier": "rk:dfence_{var}",
      "materials":#
        "default": "entity"
      ##,
      "textures":#
        "default": "textures/blocks/{textures[var] if var in textures else 'planks_' + var}"
      ##,
      "geometry":#
        "horizontal": "geometry.dfence_horizontal",
        "vertical": "geometry.dfence_vertical"
      ##,
      "spawn_egg":#
        "texture": "rk:dfence_{var}",
        "texture_index": 0
      ##,
      "scripts":#
        "animate":[
          "spawn_despawn"
        ]
      ##,
      "animations":#
        "spawn_despawn": "controller.animation.entity_block.spawn_despawn"
      ##,
      "particle_effects":#
        "despawn": "rk:{var}_break_particle"
      ##,
      "sound_effects":#
        "spawn": "{sounds_spawn[var] if var in sounds_spawn else 'dig.' + ('nether_brick' if var == 'nether_brick' else 'wood')}",
        "despawn": "{sounds_despawn[var] if var in sounds_despawn else 'dig.' + ('nether_brick' if var == 'nether_brick' else 'wood')}"
      ##,
      "render_controllers": [
        "controller.render.dfence"
      ]
    ##
  ##
##
            '''
            # swap # and ## to curly brackets
            data = data.replace('##', '}').replace('#', '{')

            # format json
            try:
                data = json.loads(data)
            except json.JSONDecodeError as e:
                print("Invalid JSON:", e)
                raise
            data = json.dumps(data, indent=2)

            print(data, end='\n\n')
            f.write(data)
    print('All data saved in D:\\My Downloads\\dfence_rp')