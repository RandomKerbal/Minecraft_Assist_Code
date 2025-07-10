import json
from dwall_entity_bp import variants as dwall_variants
from dwall_entity_rp import textures

if __name__ == "__main__":
    for var in dwall_variants:
        if var != 'nether_brick':
            filepath = 'D:\\My Downloads\\dwall_particles\\'
            filename = f'{var}_break.particle.json'
            with open(f'{filepath}{filename}', 'w') as f:
                data = f'''
#
  "format_version":"1.10.0",
  "particle_effect":#
    "description":#
      "identifier":"rk:{var}_break_particle",
      "basic_render_parameters":#
        "material":"particles_alpha",
        "texture":"textures/blocks/{'deepslate/' if 'deepslate' in var else ''}{
            textures[var] if var in textures else
            var + 's' if (var[-6:] == '_brick' or var[-4:] == 'tile') and ('nether' not in var) else
            var
            }"
      ##
    ##,
    "components":#
      "minecraft:emitter_rate_instant":#
        "num_particles":35
      ##,
      "minecraft:emitter_lifetime_once":#
      ##,
      "minecraft:particle_motion_collision":#
        "coefficient_of_restitution":0.1,
        "collision_drag":10,
        "collision_radius":0.1
      ##,
      "minecraft:particle_appearance_lighting":#
      ##,
      "minecraft:emitter_shape_box":#
        "half_dimensions":[
          0.5,
          0.5,
          0.5
        ],
        "offset":[0, 0.5, 0],
        "direction":[
          "Math.random(-1,1)",
          1,
          "Math.random(-1, 1)"
        ]
      ##,
      "minecraft:particle_appearance_billboard":#
        "size":[
          "variable.particle_random_1 * 0.0375 + 0.0375",
          "variable.particle_random_1 * 0.0375 + 0.0375"
        ],
        "facing_camera_mode":"lookat_xyz",
        "uv":#
          "texture_width":16,
          "texture_height":16,
          "uv":[
            "math.round(variable.particle_random_1*6.5 + variable.particle_random_2*6.5)",
            "math.round(variable.particle_random_1*6.5 + variable.particle_random_2*6.5)"
          ],
          "uv_size":[
            3,
            3
          ]
        ##
      ##,
      "minecraft:particle_motion_dynamic":#
        "linear_acceleration":[
          0,
          -9.8,
          0
        ],
        "linear_drag_coefficient":0.5
      ##,
      "minecraft:particle_initial_speed":2,
      "minecraft:particle_lifetime_expression":#
        "max_lifetime":"0.2f / (Math.random(0.0, 1.0) * 0.9f + 0.1f)"
      ##
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