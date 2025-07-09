from dfence_entity_bp import variants as dfence_variants
from dwall_entity_bp import variants as dwall_variants

# generate english name for dfence_variants
en_variants = []
for var in dfence_variants:
    en_variants.append(
        ' '.join(
            word[0].upper() + word[1:] for word in var.split('_')
        )
        + ' Diagonal Fence'
    )

# generate chinese names for dfence_variants
zh_cn_variants = [word + ' 斜栅栏' for word in ('橡木', '云杉木', '白桦木', '丛林木', '金合欢木', '深色橡木', '红树木', '樱花木', '苍白橡木', '竹板', '绯红木', '诡异木', '下界砖')]
zh_tw_variants = [word + ' 斜圍欄' for word in ('橡木', '雲杉木', '白樺木', '叢林木', '金合歡木', '深色橡木', '紅樹木', '櫻花木', '蒼白橡木', '竹闆', '緋紅木', '詭異木', '下界磚')]

langs = {
    'en_US.lang': en_variants,
    'en_GB.lang': en_variants,
    'zh_CN.lang': zh_cn_variants,
    'zh_TW.lang': zh_tw_variants
}
print(langs, end='\n\n')

if __name__ == "__main__":
    for lang, lang_vars in langs.items():
        filepath = 'D:\\My Downloads\\dfence_dwall_texts\\'

        with open(f'{filepath}{lang}', 'w', encoding='utf-8') as f:
            data = ''
            for i, var in enumerate(lang_vars):
                data += f'item.spawn_egg.entity.rk:dfence_{dfence_variants[i]}.name={var}\n'
            data += '\n'

            for i, var in enumerate(lang_vars):
                data += f'entity.rk:dfence_{dfence_variants[i]}.name={var[0].upper()}{var[1:]}\n'
            data += '\n'

            data += '###END###'

            print(data)
            f.write(data)
    print(f'All data saved in {filepath}')