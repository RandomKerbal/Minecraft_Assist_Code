import json

dimensions = {
    'full': ('', '', '', ''),
    'half_top': ('', '/2', '', ''),
    'half_bottom': ('', '/2', '', '+v.texture_sz.v/2'),
    'half_left': ('/2', '', '', ''),
    'half_right': ('/2', '', '+v.texture_sz.u/2', ''),
    'quad1': ('/2', '/2', '+v.texture_sz.u/2', ''),
    'quad2': ('/2', '/2', '', ''),
    'quad3': ('/2', '/2', '', '+v.texture_sz.v/2'),
    'quad4': ('/2', '/2', '+v.texture_sz.u/2', '+v.texture_sz.v/2'),
    'quad': ('/2', '/2', '+v.texture_sz.u/16*4', '+v.texture_sz.v/16*4'),
    'quad_bottom': ('/2', '/2', '+v.texture_sz.u/16*4', '+v.texture_sz.v/2'),
    'semiquad': ('/4', '/4', '+v.texture_sz.u/16*6', '+v.texture_sz.v/16*6'),
    'semiquad_left': ('/4', '/4', '', '+v.texture_sz.v/2'),
    'semiquad_right': ('/4', '/4', '+v.texture_sz.u/16*12', '+v.texture_sz.v/2'),
    '4pix': ('/4', '', '', ''),
    '4pix_bottom': ('', '/4', '', '+v.texture_sz.v/16*12'),
    '3pix': ('', '/16*3', '', ''),
    '2pix': ('/8', '', '+v.texture_sz.u/16*7', ''),
}
"""
key = name of dimension

val = tuple(
    x scale factor, given that a full block scale = 1,
    
    y scale factor, given that a full block scale = 1,
    
    x offset, given that a full block offset = v.texture_sz.u,
    
    y offset, given that a full block offset = v.texture_sz.v
)
"""

if __name__ == "__main__":
    for name, (x_scale, y_scale, x_offset, y_offset) in dimensions.items():
        filepath = 'D:\\My Downloads\\copycat_particles\\'
        filename = f'copycat_{name}.particle.json'
        with open(f'{filepath}{filename}', 'w') as f:
            data = f'''
#
	"format_version":"1.10.0",
	"particle_effect":#
		"description":#
			"identifier":"rk:copycat_{name}",
			"basic_render_parameters":#
				"material":"particles_blend_culling",
				"texture":"atlas.terrain"
			##
		##,
		"components":#
			"minecraft:emitter_local_space":#
				"position":true,
				"rotation":true
			##,
			"minecraft:emitter_rate_instant":#
				"num_particles":1
			##,
			"minecraft:emitter_lifetime_expression":#
				"expiration_expression": "q.is_owner_identifier_any('minecraft:shulker')*(q.variant != 16)"
			##,
			"minecraft:emitter_shape_point":#
			##,
			"minecraft:particle_lifetime_expression":#
				"expiration_expression":"q.is_owner_identifier_any('minecraft:shulker')*(q.variant != 16)"
			##,
			"minecraft:particle_appearance_billboard":#
				"size":["0.5{x_scale}", "0.5{y_scale}"],
				"facing_camera_mode":"emitter_transform_xz",
				"uv":#
					"texture_width":1,
					"texture_height":1,
					"uv":["v.texture_coord.u{x_offset}", "v.texture_coord.v{y_offset}"],
					"uv_size":["v.texture_sz.u{x_scale}", "v.texture_sz.v{y_scale}"]
				##
			##,
            "minecraft:particle_appearance_tinting":#
              "color": [
                "v.tint",
                "v.tint",
                "v.tint",
                0
              ]
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
