import json
variants = ('oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'mangrove', 'cherry', 'pale_oak', 'bamboo', 'crimson', 'warped', 'nether_brick')
fire_immune = ('crimson', 'warped', 'nether_brick')

if __name__ == "__main__":
    for var in variants:
        filepath = 'D:\\My Downloads\\dfence_bp\\'
        filename = f'dfence_{var}.json'
        with open(f'{filepath}{filename}', 'w') as f:
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
        "horizontal":#
           "minecraft:variant":#
              "value":0
           ##
        ##,
        "vertical":#
           "minecraft:variant":#
              "value":1
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
        "minecraft:health":#
           "value":10,
           "max":10
        ##,
        "minecraft:damage_sensor":#
           "triggers":[
              #
                 "on_damage":#
                    "filters":#
                       "any_of":[
                          #
                             "all_of":[
                                #
                                   "test":"has_damage",
                                   "subject":"self",
                                   "value":"fatal"
                                ##,
                                #
                                   "test":"has_component",
                                   "subject":"self",
                                   "operator":"!=",
                                   "value":"minecraft:transformation"
                                ##
                             ]
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
              {'''
              #
                 "cause":"temperature",
                 "deals_damage":true
              ##,
              ''' if var not in fire_immune else ''}
              #
                 "cause":"fire",
                 "deals_damage":false
              ##,
              #
                 "cause":"all",
                 "deals_damage":false
              ##
           ]
        ##,
        {'''
        "minecraft:hurt_on_condition":#
           "damage_conditions":[
              #
                 "filters":#
                    "any_of":[
                       #
                          "test":"in_block",
                          "subject":"self",
                          "value":"minecraft:fire"
                       ##
                    ]
                 ##,
                 "cause":"temperature",
                 "damage_per_tick":1
              ##,
              #
                 "filters":#
                      "test":"in_lava",
                      "subject":"self",
                      "value":true
                 ##,
                 "cause":"temperature",
                 "damage_per_tick":4
              ##,
              #
                "filters": #
                  "any_of": [
                    #
                      "test": "is_moving",
                      "subject": "self",
                      "value": true
                    ##,
                    #
                      "test": "is_riding",
                      "subject": "self",
                      "value": true
                    ##
                  ]
                ##,
                "cause": "temperature",
                "damage_per_tick": 9999
              ##
           ]
        ##,
        ''' if var not in fire_immune else ''}
        "minecraft:collision_box":#
           "height":0.25,
           "width":0.25
        ##,
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
        "horizontal":#
           "add":#
              "component_groups":[
                 "horizontal"
              ]
           ##
        ##,
        "vertical":#
           "add":#
              "component_groups":[
                 "vertical"
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
    print(f'All data saved in {filepath}')