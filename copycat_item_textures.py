import json
from copycat_sounds import shapes

if __name__ == "__main__":
    filepath = 'D:\\My Downloads\\copycat_item_textures\\'
    with open(f'{filepath}item_texture.json', 'w') as f:
        data = '#"resource_pack_name":"copycats","texture_name":"atlas.items","texture_data":#'

        for shape in shapes:
            data += f'"rk:copycat_{shape}":#"textures":"textures/items/copycat/{shape}"##,'

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