import json
from dfence_entity_bp import variants as dfence_variants
from dwall_entity_bp import variants as dwall_variants

if __name__ == "__main__":
    filepath = 'D:\\My Downloads\\dfence_item_textures\\'
    with open(f'{filepath}item_texture.json', 'w') as f:
        data = '#"resource_pack_name":"dblocks","texture_name":"atlas.items","texture_data":#'
        for var in dfence_variants:
            data += f'"rk:dfence_{var}":#"textures":"textures/items/dfence/{var}"##,'

        for var in dwall_variants:
            data += f'"rk:dwall_{var}":#"textures":"textures/items/dwall/{var}"##,'

        data = data[:-1]  # removes comma at the end
        data += '####'

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