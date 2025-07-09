import json
from dfence_entity_bp import variants as dfence_variants
from dwall_entity_bp import variants as dwall_variants

sounds_hurt = {
    'cherry': 'cherry_wood',
    'bamboo': 'bamboo_wood',
    'crimson': 'nether_wood',
    'warped': 'nether_wood',
    'nether_brick': 'nether_brick',
    'red_nether_brick': 'nether_brick',
    'cobbled_deepslate': 'deepslate',
    'polished_deepslate': 'deepslate',
    'deepslate_bricks': 'deepslate_bricks',
    'deepslate_tiles': 'deepslate_bricks'
}

if __name__ == "__main__":
    filepath = 'D:\\My Downloads\\dfence_rp\\'
    with open(f'{filepath}sounds.json', 'w') as f:
        data = '#"entity_sounds":#"entities":#'
        # dfence sounds
        for var in dfence_variants:
            sound_hurt = f"hit.{sounds_hurt[var] if var in sounds_hurt else 'wood'}"
            data += f'"rk:dfence_{var}":#"volume":1.0,"pitch":[0.8,1.2],"events":#"hurt":"{sound_hurt}","hurt.in.water":#"sound":"{sound_hurt}","volume":0.8,"pitch":[0.4,0.8]##,"death":""####,'

        # dwall sounds
        for var in dwall_variants:
            sound_hurt = f"{'block.mud_bricks.hit' if var == 'mud_bricks' else 'hit.' + (sounds_hurt[var] if var in sounds_hurt else 'stone')}"
            data += f'"rk:dwall_{var}":#"volume":1.0,"pitch":[0.8,1.2],"events":#"hurt":"{sound_hurt}","hurt.in.water":#"sound":"{sound_hurt}","volume":0.8,"pitch":[0.4,0.8]##,"death":""####,'

        data = data[:-1]  # removes comma at the end
        data += '######'

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
