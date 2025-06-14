import json
from dfence_entity_bp import variants

if __name__ == "__main__":
    with open('D:\\My Downloads\\dfence_items_texture\\item_texture.json', 'w') as f:
        data = '#"resource_pack_name":"dfence","texture_name":"atlas.items","texture_data":#'
        for var in variants:
            data += f'"rk:dfence_{var}":#"textures":"textures/items/dfence_{var}"##,'

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
    print('All data saved in D:\\My Downloads\\dfence_rp')