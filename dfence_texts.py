from dfence_entity_bp import variants as variants

# generate en_variants from variants
en_variants = []
for var in variants:
    en_variants.append(
        ' '.join(
            word[0].upper() + word[1:] for word in var.split('_')
        )
    )

langs = {
    'en_US.lang': (en_variants, 'Diagonal Fence'),
    'en_GB.lang': (en_variants, 'Diagonal Fence'),
    'zh_CN.lang': (('橡木', '云杉木', '白桦木', '丛林木', '金合欢木', '深色橡木', '红树木', '樱花木', '苍白橡木', '竹板', '绯红木', '诡异木', '下界砖'), '斜栅栏'),
    'zh_TW.lang': (('橡木', '雲杉木', '白樺木', '叢林木', '金合歡木', '深色橡木', '紅樹木', '櫻花木', '蒼白橡木', '竹闆', '緋紅木', '詭異木', '下界磚'), '斜圍欄')
}
print(langs, end='\n\n')

if __name__ == "__main__":
    for lang, (lang_vars, dfence) in langs.items():
        filepath = 'D:\\My Downloads\\dfence_texts\\'
        with open(f'{filepath}{lang}', 'w', encoding='utf-8') as f:
            data = ''
            for i, var in enumerate(lang_vars):
                data += f'item.spawn_egg.entity.rk:dfence_{variants[i]}.name={var} {dfence}\n'
            data += '\n'

            for i, var in enumerate(lang_vars):
                data += f'entity.rk:dfence_{variants[i]}.name={var[0].upper()}{var[1:]} {dfence}\n'
            data += '\n'

            data += '###END###'

            print(data)
            f.write(data)
    print(f'All data saved in {filepath}')