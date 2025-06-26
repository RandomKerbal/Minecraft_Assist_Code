import json
from dfence_entity_bp import variants
textures = {
    'dark_oak':'planks_big_oak',
    'mangrove':'mangrove_planks',
    'cherry':'cherry_planks',
    'pale_oak':'pale_oak_planks',
    'bamboo':'bamboo_planks',
    'crimson':'huge_fungus/crimson_planks',
    'warped':'huge_fungus/warped_planks',
    'nether_brick':'nether_brick'
}
sounds_spawn = {
    'cherry':'place.cherry_wood',
    'bamboo':'place.bamboo_wood',
    'crimson':'place.nether_wood',
    'warped':'place.nether_wood'
}
sounds_despawn = {
    'cherry':'break.cherry_wood',
    'bamboo':'break.bamboo_wood',
    'crimson':'break.nether_wood',
    'warped':'break.nether_wood'
}

if __name__ == "__main__":
    for var in variants:
        filepath = 'D:\\My Downloads\\dfence_rp\\'
        filename = f'dfence_{var}.json'
        with open(f'{filepath}{filename}', 'w') as f:
            data = f'''
#
  "format_version":"1.10.0",
  "minecraft:client_entity":#
    "description":#
      "identifier":"rk:dfence_{var}",
      "materials":#
        "default":"entity_alphablend"
      ##,
      "textures":#
        "default":"textures/blocks/{textures[var] if var in textures else 'planks_' + var}",
        "hitbox":"textures/particle/particles"
      ##,
      "geometry":#
        "horizontal":"geometry.dfence.horizontal",
        "vertical":"geometry.dfence.vertical",
        "hitbox":"geometry.dfence.hitbox"
      ##,
      "spawn_egg":#
        "texture":"rk:dfence_{var}",
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
        "spawn":"{sounds_spawn[var] if var in sounds_spawn else 'dig.' + ('nether_brick' if var == 'nether_brick' else 'wood')}",
        "despawn":"{sounds_despawn[var] if var in sounds_despawn else 'dig.' + ('nether_brick' if var == 'nether_brick' else 'wood')}"
      ##,
      "render_controllers":[
        "controller.render.dfence",
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