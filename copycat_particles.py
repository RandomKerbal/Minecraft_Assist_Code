import json

dimensions = {
    'full': ('', '', '', ''),
    'half_top': ('', '/2', '', ''),
    'half_bottom': ('', '/2', '', '+query.surface_particle_texture_size.v/2'),
    'half_left': ('/2', '', '', ''),
    'half_right': ('/2', '', '+query.surface_particle_texture_size.u/2', ''),
    'quad1': ('/2', '/2', '+query.surface_particle_texture_size.u/2', ''),
    'quad2': ('/2', '/2', '', ''),
    'quad3': ('/2', '/2', '', '+query.surface_particle_texture_size.v/2'),
    'quad4': ('/2', '/2', '+query.surface_particle_texture_size.u/2', '+query.surface_particle_texture_size.v/2'),
    'quad': ('/2', '/2', '+query.surface_particle_texture_size.u/16*4', '+query.surface_particle_texture_size.v/16*4'),
    'semiquad': ('/4', '/4', '+query.surface_particle_texture_size.u/16*6', '+query.surface_particle_texture_size.v/16*6'),
    '4pix': ('/4', '', '', ''),
    '3pix': ('', '/16*3', '', ''),
    '2pix': ('/8', '', '+query.surface_particle_texture_size.u/16*7', ''),
}
"""
key = name of dimension

val = tuple(
    x scale factor, given that a full block scale = 1,
    
    y scale factor, given that a full block scale = 1,
    
    x offset, given that a full block offset = query.surface_particle_texture_size.u,
    
    y offset, given that a full block offset = query.surface_particle_texture_size.v
)
"""

if __name__ == "__main__":
    for name, (x_scale, y_scale, x_offset, y_offset) in dimensions.items():
        filepath = 'D:\\My Downloads\\copycat_particles\\'
        filename = f'copycat_{name}.particle.json'
        with open(f'{filepath}{filename}', 'w') as f:
            data = f'''
#
	"format_version": "1.10.0",
	"particle_effect":#
		"description":#
			"identifier": "rk:copycat_{name}",
			"basic_render_parameters":#
				"material": "particles_blend_culling",
				"texture": "atlas.terrain"
			##
		##,
		"components":#
			"minecraft:emitter_local_space":#
				"position": true,
				"rotation": true
			##,
			"minecraft:emitter_rate_instant":#
				"num_particles": 1
			##,
			"minecraft:emitter_lifetime_once":#
			##,
			"minecraft:emitter_shape_point":#
			##,
			"minecraft:particle_lifetime_expression":#
			##,
			"minecraft:particle_appearance_billboard":#
				"size": ["0.5{x_scale}", "0.5{y_scale}"],
				"facing_camera_mode": "emitter_transform_xz",
				"uv":#
					"texture_width": 1,
					"texture_height": 1,
					"uv": ["query.surface_particle_texture_coordinate.u{x_offset}", "query.surface_particle_texture_coordinate.v{y_offset}"],
					"uv_size": ["query.surface_particle_texture_size.u{x_scale}", "query.surface_particle_texture_size.v{y_scale}"]
				##
			##,
			"minecraft:particle_appearance_lighting":#
			##,
            "minecraft:particle_appearance_tinting":#
              "color": ["Math.clamp(query.surface_particle_color.r, 0, 1)", "Math.clamp(query.surface_particle_color.g, 0, 1)", "Math.clamp(query.surface_particle_color.b, 0, 1)", "Math.clamp(query.surface_particle_color.a, 0, 1)"]
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
