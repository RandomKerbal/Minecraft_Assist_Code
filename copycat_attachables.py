import json
from copycat_sounds import shapes

if __name__ == "__main__":
    for shape in shapes:
        filepath = 'D:\\My Downloads\\copycat_attachables\\'
        filename = f'copycat.{shape}.atc.json'
        with open(f'{filepath}{filename}', 'w') as f:
            data = f'''
#
  "format_version":"1.10.0",
  "minecraft:attachable":#
    "description":#
      "identifier":"rk:copycat_{shape}_spawn_egg",
      "materials":#
        "default":"entity",
        "enchanted":"entity_alphatest_glint"
      ##,
      "textures":#
        "default":"textures/items/copycat",
        "enchanted":"textures/misc/enchanted_item_glint" 
      ##,
      "geometry":#
        "default":"geometry.copycat.{shape}.egg"
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
        "hold_first_person":"animation.copycat.egg.hold_first_person",
        "hold_third_person":"animation.copycat.egg.hold_third_person"
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
