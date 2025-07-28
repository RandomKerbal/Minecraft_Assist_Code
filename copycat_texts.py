from pprint import pprint
from copycat_sounds import shapes

# generate english name for each shape
en_names = ['Copycat ' + shape.title() for shape in shapes]

# generate chinese names for each shape
zh_cn_names = ['伪装 ' + shape for shape in ('方块', '台阶', '楼梯', '活板门', '玻璃板', '栅栏', '墙')]
zh_tw_names = ['偽裝 ' + shape for shape in ('方塊', '厚板', '階梯', '地板門', '玻璃窗格', '柵欄', '牆壁')]

langs = {
    'en_US.lang': en_names,
    'en_GB.lang': en_names,
    'zh_CN.lang': zh_cn_names,
    'zh_TW.lang': zh_tw_names
}

if __name__ == "__main__":
    pprint(langs)
    for lang, names in langs.items():
        filepath = 'D:\\My Downloads\\copycat_rp\\'

        with open(f'{filepath}{lang}', 'w', encoding='utf-8') as f:
            data = ''

            # generate name for spawn eggs
            for i, name in enumerate(names):
                data += f'item.spawn_egg.entity.rk:copycat_{shapes[i]}.name={name}\n'
            data += '\n'

            # generate name for entities
            for i, name in enumerate(names):
                data += f'entity.rk:copycat_{shapes[i]}.name={name}\n'
            data += '\n'

            data += '###END###'

            print(data)
            f.write(data)
    print(f'All data saved in {filepath}')