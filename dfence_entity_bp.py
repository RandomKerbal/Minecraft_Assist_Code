import json
variants = ('oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'mangrove', 'cherry', 'pale_oak', 'bamboo', 'crimson', 'warped', 'nether_brick')
fire_immune = ('crimson', 'warped', 'nether_brick')

if __name__ == "__main__":
    for var in variants:
        filename = f'dfence_{var}.json'
        with open(f'D:\\My Downloads\\dfence_bp\\{filename}', 'w') as f:
            data = f'''
#
  "format_version":"1.13.0",
  "minecraft:entity":#
     "description":#
        "identifier":"rk:dfence_{var}",
        "is_spawnable":true,
        "is_summonable":true,
        "is_experimental":false,
        "animations":#
           "facing":"controller.animation.dfence.facing"
        ##,
        "scripts":#
           "animate":[
              "facing"
           ]
        ##
     ##,
     "component_groups":#
        "horizontal0":#
           "minecraft:variant":#
              "value":0
           ##,
            "minecraft:collision_box":#
               "height":0.9,
               "width":0.5
            ##
        ##,
        "horizontal1":#
           "minecraft:variant":#
              "value":1
           ##,
            "minecraft:collision_box":#
               "height":0.9,
               "width":0.5
            ##
        ##,
        "vertical0":#
           "minecraft:variant":#
              "value":10
           ##,
            "minecraft:collision_box":#
               "height":0.9,
               "width":0.5
            ##
        ##,
        "pick_up":#
           "minecraft:transformation":#
              "into":"rk:dfence_{var}<despawn>",
              "delay":#
                 "value":0.2
              ##
           ##
        ##,
        "despawn":#
           "minecraft:variant":#
              "value":-2
           ##,
           "minecraft:spawn_entity":#
              "entities":[
                 #
                    "max_wait_time":0,
                    "min_wait_time":0,
                    "num_to_spawn":1,
                    "spawn_item":"rk:dfence_{var}_spawn_egg",
                    "single_use":true
                 ##
              ]
           ##,
           "minecraft:instant_despawn":#
           ##
        ##
     ##,
     "components":#
        "minecraft:variant":#
           "value":-1
        ##,
        "minecraft:type_family":#
           "family":[
              "inanimate",
              "dfence"
           ]
        ##,
        "minecraft:damage_sensor":#
           "triggers":[
              #
                 "on_damage":#
                    "filters":#
                       "any_of":[
                          #
                             "test":"has_damage",
                             "subject":"self",
                             "value":"fatal"
                          ##,
                          #
                             "all_of":[
                                #
                                   "test":"is_sneaking",
                                   "subject":"other"
                                ##,
                                #
                                   "test":"is_family",
                                   "subject":"other",
                                   "value":"player"
                                ##
                             ]
                          ##
                       ]
                    ##,
                    "event":"pick_up"
                 ##,
                 "deals_damage":false
              ##,
              #
                 "cause":"all",
                 "deals_damage":false
              ##
           ]
        ##,
        "minecraft:fire_immune":true,
        "minecraft:physics":#
           "has_collision":false,
           "has_gravity":false
        ##,
        "minecraft:pushable":#
           "is_pushable":false,
           "is_pushable_by_piston":false
        ##,
        "minecraft:knockback_resistance":#
           "value":1.0
        ##
     ##,
     "events":#
        "horizontal0":#
           "add":#
              "component_groups":[
                 "horizontal0"
              ]
           ##
        ##,
        "horizontal1":#
           "add":#
              "component_groups":[
                 "horizontal1"
              ]
           ##
        ##,
        "vertical0":#
           "add":#
              "component_groups":[
                 "vertical0"
              ]
           ##
        ##,
        "pick_up":#
           "add":#
              "component_groups":[
                 "pick_up"
              ]
           ##
        ##,
        "despawn":#
           "add":#
              "component_groups":[
                 "despawn"
              ]
           ##
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
                raise
            data = json.dumps(data, indent=2)

            print(data, end='\n\n')
            f.write(data)
    print('All data saved in D:\\My Downloads\\dfence_bp')