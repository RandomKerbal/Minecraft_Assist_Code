import json
shapes = ('block', 'slab', 'stair', 'trapdoor', 'pane', 'fence', 'wall')

if __name__ == "__main__":
    filepath = 'D:\\My Downloads\\copycat_rp\\'
    with open(f'{filepath}sounds.json', 'w') as f:
        data = '#"entity_sounds":#"entities":#'

        for shape in shapes:
            sound_hurt = 'hit.stone'
            data += f'"rk:copycat_{shape}":#"volume":1.0,"pitch":[0.8,1.2],"events":#"hurt":"{sound_hurt}","hurt.in.water":#"sound":"{sound_hurt}","volume":0.8,"pitch":[0.4,0.8]##,"death":""####,'

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
