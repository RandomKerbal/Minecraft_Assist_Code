from dfence_entity_bp import variants as raw_variants

langs = {
    'en_US.lang': (raw_variants, 'Diagonal Fence'),
    'en_GB.lang': (raw_variants, 'Diagonal Fence'),
    'zh_CN.lang': (('橡木', '云杉木', '白桦木', '丛林木', '金合欢木', '深色橡木', '红树木', '樱花木', '苍白橡木', '竹板', '绯红木', '诡异木', '下界砖'), '斜围栏'),
    'zh_TW.lang': (('橡木', '雲杉木', '白樺木', '叢林木', '金合歡木', '深色橡木', '紅樹木', '櫻花木', '蒼白橡木', '竹闆', '緋紅木', '詭異木', '下界磚'), '斜圍欄')
}

if __name__ == "__main__":
    for lang, (variants, dfence) in langs.items():
        with open(f'D:\\My Downloads\\dfence_texts\\{lang}', 'w', encoding='utf-8') as f:
            data = ''
            for i, var in enumerate(variants):
                data += f'item.spawn_egg.entity.rk:dfence_{raw_variants[i]}.name={var[0].upper()}{var[1:]} {dfence}\n'
            data += '\n'

            for i, var in enumerate(variants):
                data += f'entity.rk:dfence_{raw_variants[i]}.name={var[0].upper()}{var[1:]} {dfence}\n'
            data += '\n'

            data += '###END###'

            print(data)
            f.write(data)
    print('All data saved in D:\\My Downloads\\dfence_texts')