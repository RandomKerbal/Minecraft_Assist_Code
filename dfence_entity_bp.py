import json
variants = ('oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'mangrove', 'cherry', 'pale_oak', 'bamboo', 'crimson', 'warped', 'nether_brick')
fire_immune = ('crimson', 'warped', 'nether_brick')

if __name__ == "__main__":
    for var in variants:
        filename = f'dfence_{var}.json'
        with open(f'D:\\My Downloads\\dfence\\{filename}', 'w') as f:
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
                           "facing":"controller.animation.entity_block.facing",
                           "collision":"controller.animation.entity_block.collision"
                        ##,
                        "scripts":#
                           "animate":[
                              "facing",
                              "collision"
                           ]
                        ##
                     ##,
                     "component_groups":#
                        "is_standing0":#
                           "minecraft:variant":#
                              "value":0
                           ##
                        ##,
                        "is_side0":#
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
                        "minecraft:leashable":#
                           "soft_distance":16.0,
                           "hard_distance":16.0,
                           "max_distance":16.0,
                           "can_be_stolen":true
                        ##,
            '''
            if var in fire_immune:
                data += f'''
                  "minecraft:fire_immune":true,
               '''

            data += f'''
                        "minecraft:collision_box":#
                           "height":1.0,
                           "width":1.0
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
                        "is_standing0":#
                           "add":#
                              "component_groups":[
                                 "is_standing0"
                              ]
                           ##
                        ##,
                        "is_side0":#
                           "add":#
                              "component_groups":[
                                 "is_side0"
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
                print("Invalid JSON:", e)
                raise
            data = json.dumps(data, indent=2)

            f.write(data)