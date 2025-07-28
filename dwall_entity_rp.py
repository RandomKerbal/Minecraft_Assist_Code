import json
from dwall_entity_bp import variants

textures = {
    'mossy_cobblestone': 'cobblestone_mossy',
    'mossy_stonebrick': 'stonebrick_mossy',
    'andesite': 'stone_andesite',
    'diorite': 'stone_diorite',
    'granite': 'stone_granite',
    'sandstone': 'sandstone_normal',
    'red_sandstone': 'red_sandstone_normal',
    'prismarine': 'prismarine_rough',
    'end_stone_brick': 'end_bricks'
}
sounds_spawn = {
    'nether_brick': 'dig.nether_brick',
    'cobbled_deepslate': 'place.deepslate',
    'deepslate_brick': 'place.deepslate_bricks',
    'polished_deepslate': 'place.deepslate',
    'deepslate_tiles': 'place.deepslate_bricks',
    'mud_brick': 'block.mud_bricks.place'
}
sounds_despawn = {
    'nether_brick': 'dig.nether_brick',
    'cobbled_deepslate': 'dig.deepslate',
    'deepslate_brick': 'dig.deepslate_bricks',
    'polished_deepslate': 'dig.deepslate',
    'deepslate_tiles': 'dig.deepslate_bricks',
    'mud_brick': 'block.mud_bricks.break'
}

if __name__ == "__main__":
    for var in variants:
        filepath = 'D:\\My Downloads\\dwall_rp\\'
        filename = f'dwall.{var}.json'
        with open(f'{filepath}{filename}', 'w') as f:
            data = f'''
#
  "format_version":"1.10.0",
  "minecraft:client_entity":#
    "description":#
      "identifier":"rk:dwall_{var}",
      "materials":#
        "default":"{'player_spectator' if var == 'prismarine' else 'entity_alphablend'}"
      ##,
      "textures":#
        "default":"textures/blocks/{'deepslate/' if 'deepslate' in var else ''}{
            textures[var] if var in textures else
            var + 's' if (var[-6:] == '_brick' or var[-4:] == 'tile') and ('nether' not in var) else
            var
            }",
        "hitbox":"textures/particle/particles"
      ##,
      "geometry":#
        "horizontal":"geometry.dwall.horizontal",
        "vertical":"geometry.dwall.vertical",
        "hitbox":"geometry.dfence.hitbox"
      ##,
      "spawn_egg":#
        "texture":"rk:dwall_{var}",
        "texture_index":0
      ##,
      "scripts":#
        "animate":[
          "facing",
          "spawn_despawn"
        ],
        "pre_animation":[
          "variable.snap_rot = -query.body_y_rotation + Math.round(query.body_y_rotation / 90) * 90;",
          "variable.look_at_entity = query.distance_from_camera < 2.5 && Math.abs(Math.abs(query.rotation_to_camera(1) - query.camera_rotation(1)) - 180) < 25 && Math.abs(query.rotation_to_camera(0) + query.camera_rotation(0)) < 20;"
        ]
      ##,
      "animations":#
        "facing":"animation.dfence.facing",
        "spawn_despawn":"controller.animation.entity_block.spawn_despawn"
      ##,
      "particle_effects":#
        "despawn":"rk:{var}_break_particle"
      ##,
      "sound_effects":#
        "spawn":"{sounds_spawn[var] if var in sounds_spawn else 'dig.stone'}",
        "despawn":"{sounds_despawn[var] if var in sounds_despawn else 'dig.stone'}"
      ##,
      "render_controllers":[
        "controller.render.{'dwall_prismarine' if var == 'prismarine' else 'dfence'}",
        "controller.render.dfence.hitbox"
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
    print(f'All data saved in {filepath}')
