import json
from dfence_entity_bp import variants
from dfence_entity_rp import textures

if __name__ == "__main__":
    for var in variants:
        filepath = 'D:\\My Downloads\\dfence_attachables\\'
        filename = f'dfence_{var}.atc.json'
        with open(f'{filepath}{filename}', 'w') as f:
            data = f'''
#
  "format_version":"1.10.0",
  "minecraft:attachable":#
    "description":#
      "identifier":"rk:dfence_{var}_spawn_egg",
      "materials":#
        "default":"entity",
        "enchanted":"entity_alphatest_glint"
      ##,
      "textures":#
        "default":"textures/blocks/{textures[var] if var in textures else 'planks_' + var}",
        "enchanted":"textures/misc/enchanted_item_glint" 
      ##,
      "geometry":#
        "default":"geometry.dfence.egg"
      ##,
      "scripts":#
        "animate":[
          #
            "hold_first_person":"context.is_first_person == 1.0"
          ##,
          #
            "hold_third_person":"context.is_first_person == 0.0"
          ##
        ]
      ##,
      "animations":#
        "hold_first_person":"animation.dfence.egg.hold_first_person",
        "hold_third_person":"animation.dfence.egg.hold_third_person"
      ##,
      "render_controllers":[
        "controller.render.item_default"
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
