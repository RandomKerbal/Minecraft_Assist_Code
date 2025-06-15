import json
from dfence_entity_bp import variants

if __name__ == "__main__":
    for var in variants:
        filepath = 'D:\\My Downloads\\dfence_recipes\\'
        filename = f'dfence_{var}.rec.json'
        with open(f'{filepath}{filename}', 'w') as f:
            data = f'''
#
  "format_version": "1.13",
  "minecraft:recipe_shaped":#
    "description":#
    "identifier": "rk:dfence_{var}"
    ##,
    "tags": [
      "crafting_table"
    ],
    "pattern": [
      " P",
      "P "
    ],
    "key":#
      "P":#
        "item": "minecraft:{('planks:' + str(variants.index(var))) if variants.index(var) <= 5 else ('netherbrick' if var == 'nether_brick' else (var + '_planks'))}"
      ##
    ##,
    "result":#
      "item": "minecraft:spawn_egg",
      "data": "query.get_actor_info_id('rk:dfence_{var}')",
      "count": {'1' if var == 'nether_brick' else '2'}
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