import json
from dwall_entity_bp import variants
metadata = {
    'mossy_stonebrick': 'stonebrick:1',
    'andesite': 'stone:5',
    'diorite': 'stone:3',
    'granite': 'stone:1',
    'brick': 'brick_block'
}

if __name__ == "__main__":
    for var in variants:
        filepath = 'D:\\My Downloads\\dwall_recipes\\'
        filename = f'dwall_{var}.rec.json'
        with open(f'{filepath}{filename}', 'w') as f:
            data = f'''
#
  "format_version":"1.13",
  "minecraft:recipe_shaped":#
    "description":#
    "identifier":"rk:dwall_{var}"
    ##,
    "tags":[
      "crafting_table"
    ],
    "pattern":[
      " S",
      "S "
    ],
    "key":#
      "S":#
        "item":"minecraft:{metadata[var] if var in metadata else var}"
      ##
    ##,
    "result":#
      "item":"minecraft:spawn_egg",
      "data":"query.get_actor_info_id('rk:dwall_{var}')",
      "count":2
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