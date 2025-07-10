from pprint import pprint
from dfence_entity_bp import variants as dfence_variants
from dwall_entity_bp import variants as dwall_variants

variants = {
    'dfence': dfence_variants,
    'dwall': dwall_variants
}
'''
Data Structure:

shapes (dfence, dwall,...)
    ┗ variants (oak, cobblestone,...)
'''

# generate english name for dfence and dwall variants
en_names = {
    'dfence': [var.replace('_', ' ').title() + ' Diagonal Fence' for var in dfence_variants],
    'dwall': [var.replace('stonebrick', 'Stone Brick').replace('_', ' ').title() + ' Diagonal Wall' for var in dwall_variants]
}

# generate chinese names for dfence and dwall variants
zh_cn_names = {
    'dfence': [word + ' 斜栅栏' for word in ('橡木', '云杉木', '白桦木', '丛林木', '金合欢木', '深色橡木', '红树木', '樱花木', '苍白橡木', '竹板', '绯红木', '诡异木', '下界砖')],
    'dwall': [word + ' 斜墙' for word in ('圆石', '苔石', '石砖', '苔石砖', '安山岩', '闪长岩', '花岗岩', '砂岩', '红砂岩', '砖块', '海晶石', '下界砖', '红色下界砖', '末地石砖', '黑石', '磨制黑石', '磨制黑石砖', '深板岩圆石', '磨制深板岩', '深板岩砖', '深板岩瓦', '泥砖')]
}
zh_tw_names = {
    'dfence': [word + ' 斜圍欄' for word in ('橡木', '雲杉木', '白樺木', '叢林木', '金合歡木', '深色橡木', '紅樹木', '櫻花木', '蒼白橡木', '竹闆', '緋紅木', '詭異木', '下界磚')],
    'dwall': [word + ' 斜牆' for word in ('圓石', '苔石', '石磚', '苔石磚', '安山岩', '閃長岩', '花崗岩', '砂岩', '紅砂岩', '磚塊', '海晶石', '下界磚', '紅色下界磚', '末地石磚', '黑石', '磨製黑石', '磨製黑石磚', '深闆岩圓石', '磨製深闆岩', '深闆岩磚', '深闆岩瓦', '泥磚')]
}

langs = {
    'en_US.lang': en_names,
    'en_GB.lang': en_names,
    'zh_CN.lang': zh_cn_names,
    'zh_TW.lang': zh_tw_names
}
'''
Data Structure:

langs (en_US, zh_CN,...)
    ┗ shapes (dfence, dwall,...)
        ┗ names (Oak Diagonal Fence, Cobblestone Diagonal Wall,...)
'''

if __name__ == "__main__":
    pprint(langs)
    for lang, shapes in langs.items():
        filepath = 'D:\\My Downloads\\dfence_dwall_texts\\'

        with open(f'{filepath}{lang}', 'w', encoding='utf-8') as f:
            data = ''

            # generate name for spawn eggs
            for shape, names in shapes.items():
                for i, name in enumerate(names):
                    data += f'item.spawn_egg.entity.rk:{shape}_{variants[shape][i]}.name={name}\n'
                data += '\n'

            # generate name for entities
            for shape, names in shapes.items():
                for i, name in enumerate(names):
                    data += f'entity.rk:{shape}_{variants[shape][i]}.name={name}\n'
                data += '\n'

            data += '###END###'

            print(data)
            f.write(data)
    print(f'All data saved in {filepath}')