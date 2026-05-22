import streamlit as st
import json

# ===================================================
# 1. データ定義
# ===================================================
list_origin = ["ファンタジア", "ノクターン"]
list_level = [f"Lv{i}" for i in range(1, 11)]
list_age = ["幼年", "青年", "壮年", "中年", "老年"]
list_gender = ["男", "女", "中性"]
list_ethnicity = ["東方人", "西方人", "南方人", "北方人"]

list_race_common = [
    "人間族", "獣人族", "翼人族", "鬼人族", "兎人族", "呪い人", "人魚族",
    "ドラシオン", "巨人族", "猫人族", "妖怪", "妖狐", "ドリュアス",
    "不死者", "甲虫人", "半獣人", "マンティコア", "天狗", "鬼半妖",
    "クラーケン", "蹄人族", "マリオネット", "メルフェディオヌ"
]
list_race_fantasia = list_race_common + [
    "ハイエルフ", "ハーフエルフ", "ダークエルフ", "ドワーフ", "ウッドエルフ",
    "フェルダー", "ヴァンパイア", "人狼", "デュラハン", "ダンピール",
    "レウィス・ゴーレム", "ゴブリン", "ハーフドラゴン", "スノウエルフ", "妖精族",
    "ホムンクルス", "ダークドワーフ", "蛇人", "幻蛛族", "失耀天使", "コブラナイ",
    "フレイムエルフ", "ウーンゲフォイヤー", "ヴァンシー"
]
list_race_nocturne = list_race_common + [
    "炉心異常体", "魔眼発現体", "演算異常体", "強化演算体", "サイボーグ",
    "アンドロイド", "クローン《デザイナーベビー》", "幻影体発現者", "ヴィロン",
    "ノクト・ヴァンパイア", "ノクス・エルフ", "ノクス・ハーフエルフ",
    "ホットロード・サイボーグ", "意識人造体（イニシエーター）", "人工獣人",
    "強化人兵", "羅刹", "オートマタ", "アルラウネ", "デトネーター",
    "スチームブッチャー", "怪異憑依者／怪人"
]
list_bg_fantasia = ["騎士", "賊", "魔術師", "聖職者", "貴族", "放浪戦士", "芸術家", "盗人", "狩人", "侍", "窶し者", "双剣士", "銃剣士", "商人", "淑女", "通常使用人", "戦闘使用人", "多重人格者", "対偶者", "海賊", "祈祷者", "蛮族", "贖血徒"]
list_bg_nocturne = ["軍人", "暴漢", "ブルジョア", "傭兵", "芸術家", "盗人", "狩人", "貧者", "商人", "探偵", "煙突掃除人", "使用人", "官吏", "医者", "淑女", "多重人格者", "警官", "無法者", "対偶者", "教授", "ペテン師", "怪盗", "水兵", "僭称者", "叫喚者", "拳闘士", "囚憶者"]
list_past0 = ["①凡庸", "➁生存", "③悲哀", "④愚行", "⑤才能", "⑥血統", "⑦復讐", "⑧不要"]
list_past1 = ["①孤独", "➁平凡", "③愛情", "④禁断", "⑤特別", "⑥苦痛"]
list_past2 = ["①暴力", "➁矜持", "③風詠", "④勤勉", "⑤失意", "⑥憧憬"]
list_attr = ["無属性", "血属性", "地属性", "花属性", "雪属性", "氷属性", "水属性", "風属性", "炎属性", "雷属性", "光属性", "夜属性", "双属性"]
list_attr_sub = ["地属性", "花属性", "雪属性", "氷属性", "水属性", "風属性", "炎属性", "雷属性", "光属性", "夜属性"]
list_skill = ["(なし)", "〈技力Lv1〉", "〈技力Lv2〉", "〈技力Lv3〉", "〈技力Lv4〉"]
list_martial = ["(なし)", "〈武芸Lv1〉", "〈武芸Lv2〉", "〈武芸Lv3〉", "〈武芸Lv4〉"]
list_craft = ["(なし)", "〈工芸Lv1〉", "〈工芸Lv2〉", "〈工芸Lv3〉", "〈工芸Lv4〉"]
list_blessing = ["(なし)", "氷影神の加護", "水輝神の加護", "夜影神の加護", "炎輝神の加護", "地影神の加護", "風影神の加護", "雷影神の加護", "雪神の加護", "花神の加護", "金紅神の加護 (血契)", "屍王神の加護 (血契)", "魔血神の加護 (血契)", "魔狼神の加護 (血契)", "魔炎神の加護 (血契)", "魔鬼神の加護 (血契)"]
list_stance = ["(なし)", "正眼の構え", "天の構え", "地の構え", "八相の構え", "陽の構え", "霞の構え", "蜻蛉の構え"]
list_school = ["(なし)", "ミドガルネ帝国魔導学園", "ユーグランス天空魔術学園", "方術院", "シャルディア中央魔導城", "イリコフォティア大魔導学院", "陰陽学所", "アンブローズ王立魔法学校", "ロクス魔導騎士学院", "元素教会神秘学舎", "神聖魔術学園", "白亜の魔導塔", "冒険者ギルド元素魔導教練所", "星見の魔導空船", "冒険者ギルド魔力魔導教練所", "大修道院治癒術伝習所", "アスガリア治癒学校"]
list_spec_route = ["(なし)", "野戦部隊(軍人)", "特殊部隊(軍人)", "戦闘員(傭兵)", "遊撃士(傭兵)", "シビリアン(市民)", "エンフォーサー(市民)"]
dict_spec = {
    "(なし)": [["(なし)"], ["(なし)"], ["(なし)"], ["(なし)"]],
    "野戦部隊(軍人)": [["(なし)", "小銃手", "機関銃手", "対兵器兵"], ["(なし)", "浸透突撃", "効率携行術", "高精度狙撃"], ["(なし)", "突撃兵", "機動偵察兵", "選抜射手"], ["(なし)", "武装偵察兵", "単座式装甲歩行機", "狙撃手", "行進射撃"]],
    "特殊部隊(軍人)": [["(なし)", "近接戦闘（CQB）", "近接格闘（CQC）"], ["(なし)", "生存戦術", "即応警戒"], ["(なし)", "特殊工作兵", "潜入兵", "空挺兵"], ["(なし)", "特殊工作兵Lv2", "潜入兵Lv2", "空挺兵Lv2"]],
    "戦闘員(傭兵)": [["(なし)", "マーセナリー", "パフォーマー"], ["(なし)", "サボター", "ブロッカー", "ハートブレイク"], ["(なし)", "ベテラン", "クロスファイア", "メンアットアームズ"], ["(なし)", "コンドッティエーレ", "ハイランダー", "コンキスタドール"]],
    "遊撃士(傭兵)": [["(なし)", "ダンサー", "ウィーゼル"], ["(なし)", "タンゴ", "ピューマ"], ["(なし)", "ワルツ", "レオパルド"], ["(なし)", "グラディエーター", "ティーガー"]],
    "シビリアン(市民)": [["(なし)", "ハンドワーカー", "アプレンティス", "スカラー"], ["(なし)", "フォアマン", "アーティスト", "インテレクチュアル"], ["(なし)", "ジャーニーマン", "エキシヴィター", "フェロウ"], ["(なし)", "アルチザン", "ローリエット", "プロフェッサー"]],
    "エンフォーサー(市民)": [["(なし)", "追手", "荒くれ者"], ["(なし)", "スルース", "アンダーリング", "オブザーバー"], ["(なし)", "オペレーター", "ブルーザー", "エミサリー"], ["(なし)", "ノワール・リミエ", "エセクトーレ", "アウフゼーア"]]
}
list_job1 = ["(なし)", "旅騎士", "軽槍兵", "修練者", "魔術師", "魔法術師", "魔女", "治癒術師", "霊術師", "魔力射撃士", "軽業師", "遊撃師", "射撃士", "蛮戦士", "戦士", "冒険者"]
list_job2 = ["(なし)", "騎士", "魔導騎士", "魔導士", "魔導術師", "魔導狙撃士", "錬金術師", "治癒神官", "死霊術師", "竜騎士", "狂戦士", "銃士", "武士", "忍", "剣闘士", "精霊師", "弓騎士", "勇者"]
list_job_noc1 = ["(なし)", "下士官", "傭兵", "斥候", "襲撃者", "強奪者", "旅芸人", "手品師", "早撃手", "労働者", "歩兵", "格闘兵"]
list_job_noc2 = ["(なし)", "特技士官", "突撃傭兵", "狙撃手", "略奪者", "強襲兵", "喜劇役者", "奇術師", "近接兵", "銃巧手"]
list_job_lv = ["0", "1", "2", "3"]
list_job2_lv = ["0", "1", "2", "3", "4"]
list_stats = ["(なし)", "筋力", "知力", "敏捷", "精神", "体格", "生命", "容姿", "芸術", "商才", "信仰"]
base_stats_names = ["筋力", "知力", "敏捷", "精神", "体格", "生命", "容姿", "芸術", "商才", "信仰"]
list_sub_stats = ["膂力", "叡智", "体力", "持久力", "技量", "神聖", "商売", "表現力", "探求心"]
dict_max_sp = {"Lv1": 2, "Lv2": 4, "Lv3": 6, "Lv4": 8, "Lv5": 10, "Lv6": 13, "Lv7": 16, "Lv8": 19, "Lv9": 22, "Lv10": 26}
demon_races = ["鬼人族", "ヴァンパイア", "人狼", "デュラハン", "マンティコア", "クラーケン", "ウーンゲフォイヤー", "メルフェディオヌ", "ノクト・ヴァンパイア"]
cursed_races = ["呪い人", "羅刹", "アルラウネ", "スチームブッチャー", "怪異憑依者／怪人", "ゴブリン", "妖怪", "妖狐", "不死者" "天狗", "鬼半妖","マリオネット","ホムンクルス","失耀天使"]

# ===================================================
# 2. ヘルパー関数
# ===================================================
def get_int(val):
    if isinstance(val, (int, float)):
        return int(val)
    s = str(val).strip()
    return int(s) if s.lstrip('-').isdigit() else 0

def si(key, options, default_idx=0):
    """セッションステートから安全にインデックスを取得"""
    val = st.session_state.get(key)
    if val is not None and val in options:
        return options.index(val)
    return default_idx

# ===================================================
# 3. 計算ロジック（元のcalculate()をパラメータ受け取り形式に）
# ===================================================
def calculate():
    p = st.session_state
    mod_hp = 0
    mod_mp = 0
    mod_stamina = 0
    bonus_sp = 0  # 👈 これが一番上にあれば UnboundLocalError は絶対に出ません
    base_sp = 0
    spent_sp = 0
    max_sp = 0
    magic_sp = 0
    sub_stats = st.session_state.get('sub_stats', {})
    origin = st.session_state.get('origin', 'ファンタジア') # 無かったら 'ファンタジア' を使う
    race = st.session_state.get('race', '人間族')          # 無かったら '人間族' を使う
    race_sub = p.get('race_sub', '')
    lineage = st.session_state.get('lineage', 0)           # 無かったら 0 を使う
    lvl_num = st.session_state.get('lvl_num', 0)           # 無かったら 0 を使う
    current_attrs = st.session_state.get('current_attrs', [])
    st.error(f"【種族チェック】現在のrace: {len(race)}文字 (※正解は9文字)")
    st.error(f"【種族生データ】{repr(race)}")
    st.error(f"【種族一致判定】race == 'スチームブッチャー' の結果: {race == 'スチームブッチャー'}")
    magic_sp_text = ""
    
    stats = {
        "筋力": 0, "知力": 0, "敏捷": 0, "精神": 0, 
        "体格": 0, "生命": 0, "芸術": 0, "容姿": 0, "芸術": 0,  "商才": 0, "信仰": 0
    }

    def add_stats_group(val, exclude=[]):
        for k in ["筋力", "知力", "敏捷", "精神", "体格", "生命", "容姿"]:
            if k not in exclude:
                stats[k] = stats.get(k, 0) + val
    
    # 画面で選ばれたレベル(例:"Lv2")を取得して、dict_max_spの表から最大SPを引っ張ってくる！
    level_str = p.get('level', 'Lv1')
    max_sp = dict_max_sp.get(level_str, 0)
    
    # 【おまけの修正】種族スキルの計算で使う「lvl_num（数字のみ）」もここで作ってあげます
    lvl_num = int(level_str.replace('Lv', ''))
    
    warning_errors = []
    is_atoning_blood = False
    
    # 統計情報の初期化
    stats = {k: p.get(f'base_{k}', 0) + p.get(f'sp_{k}', 0) for k in base_stats_names}
    spent_sp += sum(p.get(f'sp_{k}', 0) for k in base_stats_names)
    # ----------------------

    # ★ここから追加：種族の計算が始まる「前」に、属性を確定させる！
    actual_attr = p.get('attr', '無属性')
    actual_attr1 = p.get('attr1', '地属性')
    actual_attr2 = p.get('attr2', '花属性')

    is_demon = race in demon_races
    is_cursed = race in cursed_races

    if is_cursed:
        actual_attr = "無属性"
    elif is_demon:
        actual_attr = "血属性"
    elif origin == "ノクターン" and race != "幻影体発現者":
        actual_attr = "無属性"

    if actual_attr == "双属性":
        current_attrs = [actual_attr1, actual_attr2]
        attr_text = f"双属性 ({actual_attr1} / {actual_attr2})"
    else:
        current_attrs = [actual_attr]
        attr_text = actual_attr
    # ★追加ここまで
    
    # 計算で使いそうな変数をあらかじめ定義
    bonus_ab_melee = 0
    bonus_ab_magic = 0
    bonus_mental = 0
    mod_luck = 0
    
    if origin == "ファンタジア" or (origin == "ノクターン" and race in list_race_common):
        if race == "人間族":
                val = 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_hp += val; mod_mp += val; mod_stamina += (3 if lineage == 100 else (2 if lineage >= 71 else 1))
                add_stats_group(val)
                bonus_sp += 400 if lineage == 100 else (350 if lineage >= 90 else (300 if lineage >= 71 else 250))
        elif race == "獣人族":
                mod_hp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                mod_stamina += 5 if lineage == 100 else (4 if lineage >= 71 else 3)
                stats["筋力"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                add_stats_group(11 if lineage == 100 else (7 if lineage >= 71 else 3), exclude=["筋力", "知力"])
                stats["知力"] += 0 if lineage == 100 else (-5 if lineage >= 71 else -10)
        elif race == "翼人族":
                mod_hp += 10 if lineage == 100 else (8 if lineage >= 71 else 5)
                mod_mp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_stamina += 8 if lineage == 100 else (7 if lineage >= 71 else 6)
                add_stats_group(10 if lineage == 100 else (7 if lineage >= 71 else 4))
        elif race == "鬼人族":
                mod_hp += 30 if lineage == 100 else (25 if lineage >= 91 else (20 if lineage >= 71 else 15))
                mod_mp += 12 if lineage == 100 else (8 if lineage >= 71 else 4)
                mod_stamina += 6 if lineage == 100 else (4 if lineage >= 71 else 3)
                str_vit = 30 if lineage == 100 else (24 if lineage >= 71 else 20)
                stats["筋力"] += str_vit; stats["生命"] += str_vit
                add_stats_group(20 if lineage == 100 else (15 if lineage >= 71 else 10), exclude=["筋力", "生命"])
        elif race == "兎人族":
                mod_hp += 7 if lineage == 100 else (5 if lineage >= 71 else 3)
                mod_stamina += 5 if lineage == 100 else (4 if lineage >= 71 else 3)
                add_stats_group(12 if lineage == 100 else (8 if lineage >= 71 else 4), exclude=["敏捷"])
                agi_mer = 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                stats["敏捷"] += agi_mer; stats["商才"] += agi_mer
        elif race == "呪い人":
                if lineage >= 10:
                    mod_hp -= 15; mod_mp -= 15; mod_stamina -= 5; bonus_sp += 150
                    add_stats_group(-30)
                else:
                    diff = 11 - lineage
                    mod_hp += diff * 2; mod_mp += diff * 2; mod_stamina += diff * 0.5; bonus_sp += 30 * diff
                    add_stats_group(diff * 2)
        elif race == "人魚族":
                mod_hp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_mp += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                mod_stamina += 3 if lineage == 100 else (2 if lineage >= 71 else 1)
                main_stat = 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["知力"] += main_stat; stats["精神"] += main_stat; stats["容姿"] += main_stat
                add_stats_group(7 if lineage == 100 else (5 if lineage >= 71 else 3), exclude=["知力", "精神", "容姿"])
        elif race == "ドラシオン":
                hp_mp = 35 if lineage == 100 else (30 if lineage >= 71 else 25)
                mod_hp += hp_mp; mod_mp += hp_mp
                mod_stamina += 3 if lineage == 100 else (2 if lineage >= 71 else 1)
                add_stats_group(17 if lineage == 100 else (12 if lineage >= 71 else 7))
        elif race == "巨人族":
                mod_hp += 20 if lineage == 100 else (15 if lineage >= 71 else 10); mod_mp += 5
                mod_stamina += 6 if lineage == 100 else (4 if lineage >= 71 else 2)
                add_stats_group(12 if lineage == 100 else (6 if lineage >= 90 else 3), exclude=["筋力", "体格"])
                stats["体格"] += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                stats["筋力"] += 22 if lineage == 100 else (17 if lineage >= 71 else 12)
                if race_sub == "山の一族": mod_hp += 5
                elif race_sub == "霧の一族": mod_mp += 5
        elif race == "猫人族":
                val = 12 if lineage == 100 else (8 if lineage >= 71 else 4)
                mod_hp += val; mod_mp += val
                mod_stamina += 3 if lineage == 100 else (2 if lineage >= 71 else 1)
                stats["敏捷"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                add_stats_group(7 if lineage == 100 else (4 if lineage >= 71 else 2), exclude=["敏捷", "知力"])
                stats["知力"] += 6 if lineage == 100 else (4 if lineage >= 71 else 2)
                stats["商才"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                bonus_sp += 150
                if race_sub == "ベスティアケット": stats["容姿"] -= 5; mod_hp += 7
                elif race_sub == "アニマケット": stats["容姿"] += 2; mod_mp += 2
        elif race == "妖怪":
                hp_mp = 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_hp += hp_mp; mod_mp += hp_mp; mod_stamina += 2
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5))
                bonus_sp -= 100
        elif race == "妖狐":
                mod_hp += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                mod_mp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                mod_stamina += 3 if lineage == 100 else (2 if lineage >= 71 else 1)
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5), exclude=["容姿", "知力"])
                val = 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                stats["容姿"] += val; stats["知力"] += val
                bonus_sp -= 50
        elif race == "ドリュアス":
                mod_hp += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_mp += 30 if lineage == 100 else (20 if lineage >= 71 else 10)
                stats["知力"] += 23 if lineage == 100 else (17 if lineage >= 71 else 12) + lvl_num
                mod_mp += lvl_num * 5
                stats["容姿"] += 17 if lineage == 100 else (12 if lineage >= 71 else 8)
                add_stats_group(12 if lineage == 100 else (8 if lineage >= 71 else 4), exclude=["知力", "容姿", "商才"])
        elif race == "不死者":
                val = 5 if lineage == 100 else (4 if lineage >= 91 else (3 if lineage >= 71 else 2))
                mod_hp += val; mod_mp += val; mod_stamina += 1
        elif race == "甲虫人":
                hp_add = 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mp_add = 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_mp += mp_add
                if race_sub == "全甲種":
                    mod_hp += hp_add
                    stats["筋力"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                    stats["生命"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                    stats["敏捷"] -= 15
                    add_stats_group(5, exclude=["筋力", "生命", "敏捷"])
                elif race_sub == "亜甲種":
                    mod_hp += hp_add - 3 
                    stats["筋力"] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                    stats["生命"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                    add_stats_group(11 if lineage == 100 else (8 if lineage >= 71 else 5), exclude=["筋力", "生命"])
        elif race == "半獣人":
                hp_mp = 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_hp += hp_mp; mod_mp += hp_mp
                mod_stamina += 4 if lineage == 100 else (3 if lineage >= 71 else 2)
                stats["筋力"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                add_stats_group(11 if lineage == 100 else (7 if lineage >= 71 else 3), exclude=["筋力"])
                bonus_sp += 250 if lineage == 100 else (200 if lineage >= 71 else 150)
        elif race == "マンティコア":
                mod_hp += 35 if lineage == 100 else (25 if lineage >= 71 else 15)
                mod_mp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                add_stats_group(15)
        elif race == "天狗":
                mod_hp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_mp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                mod_stamina += -1 if lineage == 100 else (-2 if lineage >= 71 else -3)
                stats["知力"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5), exclude=["知力"])
                bonus_sp -= 100
        elif race == "鬼半妖":
                mod_hp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                mod_mp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_stamina += 2
                stats["筋力"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5), exclude=["筋力"])
                bonus_sp += 300 if lineage == 100 else (250 if lineage >= 71 else 200)
        elif race == "クラーケン":
                hp_mp = 35 if lineage == 100 else (30 if lineage >= 71 else 25)
                mod_hp += hp_mp; mod_mp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_stamina += 5 if lineage == 100 else (4 if lineage >= 71 else 3)
                add_stats_group(20 if lineage == 100 else (15 if lineage >= 71 else 10))
        elif race == "蹄人族":
                mod_hp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                mod_mp += 5; mod_stamina += 5 if lineage == 100 else (4 if lineage >= 71 else 3)
                stats["敏捷"] += 18 if lineage == 100 else (14 if lineage >= 71 else 8)
                stats["筋力"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                stats["容姿"] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                add_stats_group(11 if lineage == 100 else (7 if lineage >= 71 else 3), exclude=["筋力", "敏捷", "容姿"])
        elif race == "マリオネット":
                mod_hp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_mp += 22 if lineage == 100 else (17 if lineage >= 71 else 12)
                stats["敏捷"] += 10 if lineage == 100 else (7 if lineage >= 71 else 3)
                stats["容姿"] += 18 if lineage == 100 else (15 if lineage >= 71 else 8)
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5), exclude=["敏捷", "容姿"])
        elif race == "メルフェディオヌ":
                hp_mp = 40 if lineage == 100 else (35 if lineage >= 71 else 30)
                mod_hp += hp_mp; mod_mp += hp_mp
                mod_stamina += 4 if lineage == 100 else (3 if lineage >= 71 else 2)
                add_stats_group(20 if lineage == 100 else (15 if lineage >= 71 else 10))

        if race == "フェルダー": stats["体格"] = int(stats["体格"] * 0.7)
        if race == "コブラナイ": stats["体格"] = int(stats["体格"] * 0.7); stats["敏捷"] = int(stats["敏捷"] * 0.7)
        if race == "ゴブリン":
                if lineage == 100: stats["知力"] = int(stats["知力"] * 0.9)
                elif lineage >= 71: stats["知力"] = int(stats["知力"] * 0.8)
                else: stats["知力"] = int(stats["知力"] * 0.7)
        if race == "フェルダー": mod_hp = int((((stats["生命"] + stats["体格"]) // 5) + mod_hp) * 0.7) - ((stats["生命"] + stats["体格"]) // 5)

        if origin == "ファンタジア":
            if race == "ハイエルフ":
                mod_hp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_mp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                stats["知力"] += 20 if lineage == 100 else (17 if lineage >= 71 else 12)
                stats["容姿"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                for k in ["精神", "敏捷", "体格", "筋力", "生命"]: stats[k] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
            elif race == "ハーフエルフ":
                hp_mp = 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_hp += hp_mp; mod_mp += hp_mp
                stats["知力"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["容姿"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                for k in ["筋力", "敏捷", "精神", "体格", "生命"]: stats[k] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                bonus_sp += 270 if lineage == 100 else (220 if lineage >= 71 else 170)
            elif race == "ダークエルフ":
                mod_hp += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_mp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                stats["知力"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["容姿"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                for k in ["精神", "敏捷", "体格", "筋力", "生命"]: stats[k] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
            elif race == "ドワーフ":
                mod_hp += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_mp += 12 if lineage == 100 else (8 if lineage >= 71 else 4)
                mod_stamina += 7 if lineage == 100 else (5 if lineage >= 71 else 3)
                stats["筋力"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["生命"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["体格"] += 5
                for k in ["知力", "敏捷", "精神", "容姿", "芸術", "商才", "信仰"]: stats[k] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
            elif race == "ウッドエルフ":
                mod_hp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_mp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                stats["知力"] += 24 if lineage == 100 else (20 if lineage >= 71 else 14)
                stats["容姿"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                for k in ["精神", "敏捷", "体格", "筋力", "生命"]: stats[k] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                if lineage >= 71: mod_mp += 5
                mod_mp += lvl_num * 3
            elif race == "フェルダー":
                mod_hp += 7 if lineage == 100 else (5 if lineage >= 71 else 3)
                mod_mp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                stats["知力"] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                stats["商才"] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                stats["敏捷"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                for k in ["筋力", "精神", "生命", "容姿", "芸術", "信仰"]: stats[k] += 10 if lineage == 100 else (7 if lineage >= 71 else 4)
            elif race == "ヴァンパイア":
                hp_mp = 40 if lineage == 100 else (35 if lineage >= 71 else 30)
                mod_hp += hp_mp; mod_mp += hp_mp
                add_all = 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                add_stats_group(add_all, exclude=["容姿"])
                stats["容姿"] += 30 if lineage == 100 else (25 if lineage >= 71 else 20)
            elif race == "人狼":
                mod_hp += 30 if lineage == 100 else (25 if lineage >= 71 else 20)
                mod_stamina += 4 if lineage == 100 else (3 if lineage >= 71 else 2)
                str_agi = 40 if lineage == 100 else (35 if lineage >= 71 else 30)
                stats["筋力"] += str_agi; stats["敏捷"] += str_agi
                add_stats_group(10, exclude=["筋力", "敏捷", "知力"])
                stats["知力"] += 10 if lineage == 100 else (0 if lineage >= 71 else -10)
            elif race == "デュラハン":
                mod_hp += 25 if lineage == 100 else (20 if lineage >= 91 else (15 if lineage >= 71 else 10))
                mod_mp += 10
                mod_stamina += 6 if lineage == 100 else (4 if lineage >= 71 else 2)
                str_agi = 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                stats["筋力"] += str_agi; stats["敏捷"] += str_agi
                add_stats_group(12 if lineage == 100 else (8 if lineage >= 71 else 4), exclude=["筋力", "敏捷"])
            elif race == "ダンピール":
                hp_mp = 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_hp += hp_mp; mod_mp += hp_mp
                add_stats_group(17 if lineage == 100 else (12 if lineage >= 71 else 7))
                bonus_sp += 250 if lineage == 100 else (200 if lineage >= 71 else 150)
            elif race == "レウィス・ゴーレム":
                mod_hp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                mod_stamina += 4 if lineage == 100 else (3 if lineage >= 71 else 2)
                add_stats_group(11 if lineage == 100 else (7 if lineage >= 71 else 3))
            elif race == "ゴブリン":
                if lineage == 100:
                    mod_hp += 20; mod_mp += 10; stats["容姿"] -= 10
                    for k in ["筋力", "生命"]: stats[k] += 20
                    stats["敏捷"] += 15
                    add_stats_group(10, exclude=["筋力", "生命", "敏捷", "容姿", "知力"])
                elif lineage >= 71:
                    mod_hp += 15; mod_mp += 5; stats["容姿"] -= 15
                    for k in ["筋力", "生命", "敏捷"]: stats[k] += 15
                    add_stats_group(8, exclude=["筋力", "生命", "敏捷", "容姿", "知力"])
                else:
                    mod_hp += 10; stats["容姿"] -= 20
                    for k in ["筋力", "生命", "敏捷"]: stats[k] += 10
                    add_stats_group(5, exclude=["筋力", "生命", "敏捷", "容姿", "知力"])
            elif race == "ハーフドラゴン":
                mod_hp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_mp += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_stamina += 4 if lineage == 100 else (3 if lineage >= 71 else 2)
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5))
                bonus_sp += 150 if lineage == 100 else (100 if lineage >= 71 else 50)
            elif race == "スノウエルフ":
                mod_hp += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                mod_mp += 27 if lineage == 100 else (22 if lineage >= 71 else 17)
                stats["知力"] += 22 if lineage == 100 else (17 if lineage >= 71 else 12)
                stats["容姿"] += 21 if lineage == 100 else (16 if lineage >= 71 else 11)
                for k in ["筋力", "敏捷", "精神", "体格", "生命", "芸術", "信仰"]: stats[k] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                if lineage >= 91 and ("氷属性" in current_attrs or "雪属性" in current_attrs):
                    mod_hp += 5; mod_mp += 5
            elif race == "妖精族":
                mod_hp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_mp += 50 if lineage == 100 else (35 if lineage >= 71 else 20)
                stats["容姿"] += 20 if lineage == 100 else (14 if lineage >= 71 else 8)
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5), exclude=["容姿"])
            elif race == "ホムンクルス":
                mod_hp += 20 if lineage == 100 else 15
                mod_mp += 20 if lineage == 100 else 15
                mod_stamina += 3 if lineage == 100 else 2
                add_stats_group(17 if lineage == 100 else 12)
                bonus_sp += 100 if lineage == 100 else (50 if lineage >= 71 else 0)
            elif race == "ダークドワーフ":
                mod_hp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_mp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                stats["体格"] += 5
                stats["知力"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                stats["筋力"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5), exclude=["知力", "筋力", "体格"])
            elif race == "蛇人":
                if gender == "女":
                    mod_hp += 5; mod_mp += 20 if lineage == 100 else (15 if lineage >= 71 else 10); mod_stamina += 1
                    stats["容姿"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                    stats["精神"] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                    add_stats_group(11 if lineage == 100 else (7 if lineage >= 71 else 3), exclude=["容姿", "精神"])
                else:
                    mod_hp += 20 if lineage == 100 else (15 if lineage >= 71 else 10); mod_mp += 5; mod_stamina += 2
                    stats["生命"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                    stats["敏捷"] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                    add_stats_group(11 if lineage == 100 else (7 if lineage >= 71 else 3), exclude=["生命", "敏捷"])
                if lineage == 1: mod_mp += 15
            elif race == "幻蛛族":
                mod_hp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_mp += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                mod_stamina += 2
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5))
                stats["芸術"] += 7 if lineage == 100 else (5 if lineage >= 71 else 3)
            elif race == "失耀天使":
                mod_hp += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_mp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                mod_stamina += 3 if lineage == 100 else (2 if lineage >= 71 else 1)
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5))
            elif race == "コブラナイ":
                mod_hp += 15 if lineage == 100 else (12 if lineage >= 71 else 10)
                mod_stamina += 5 if lineage == 100 else (3 if lineage >= 71 else 2)
                stats["筋力"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["商才"] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                add_stats_group(4 if lineage == 100 else (3 if lineage >= 71 else 2), exclude=["体格", "敏捷", "筋力", "商才"])
            elif race == "フレイムエルフ":
                mod_hp += 20 if lineage == 100 else (14 if lineage >= 71 else 8)
                mod_mp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                stats["知力"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["容姿"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                for k in ["筋力", "敏捷", "精神", "体格", "生命", "芸術", "信仰"]: stats[k] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                if "炎属性" in current_attrs:
                    mod_mp += 10
                    ab_magic_extra = " (+1D)"
            elif race == "ウーンゲフォイヤー":
                hp_mp = 30 if lineage == 100 else (25 if lineage >= 71 else 20)
                mod_hp += hp_mp; mod_mp += hp_mp
                mod_stamina += 5 if lineage == 100 else (4 if lineage >= 71 else 3)
                stats["容姿"] -= 30
                add_stats_group(20 if lineage == 100 else (15 if lineage >= 71 else 10), exclude=["容姿"])
            elif race == "ヴァンシー":
                mod_hp += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_mp += 30 if lineage == 100 else (25 if lineage >= 71 else 20)
                mod_stamina += 1
                stats["容姿"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                for k in ["筋力", "知力", "敏捷", "精神", "体格", "生命", "芸術", "商才", "信仰"]: stats[k] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                
        elif origin == "ノクターン":
            st.error(f"【種族チェック】現在のrace: {len(race)}文字 (※正解は9文字)")
            st.error(f"【種族生データ】{repr(race)}")
            st.error(f"【種族一致判定】race == 'スチームブッチャー' の結果: {race == 'スチームブッチャー'}")
            if race == "炉心異常体":
                mod_hp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                stats["筋力"] += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5), exclude=["筋力"])
                if lineage >= 71: warning_errors.append("💡【運命武器】家柄71以上のため使用可能です。")
                bonus_sp += 230 if lineage == 100 else (170 if lineage >= 71 else 90)
            elif race == "魔眼発現体":
                val = 15 if lineage == 100 else (10 if lineage >= 91 else (8 if lineage >= 71 else 5))
                mod_hp += val; mod_mp += val
                add_stats_group(val)
                bonus_sp += 230 if lineage == 100 else (180 if lineage >= 71 else 120)
                if lineage >= 71: warning_errors.append("💡【運命武器】家柄71以上のため使用可能です。")
            elif race == "演算異常体":
                stats["敏捷"] += 15; stats["知力"] += 10
                add_stats_group(5, exclude=["敏捷", "知力", "精神"])
                bonus_sp += 240 if lineage == 100 else (200 if lineage >= 71 else 160)
                if lineage >= 71: warning_errors.append("💡【運命武器】家柄71以上のため使用可能です。")
            elif race == "強化演算体":
                stats["敏捷"] += 15; stats["知力"] += 10; stats["精神"] -= 15
                add_stats_group(5, exclude=["敏捷", "知力", "精神"])
                bonus_sp += 240 if lineage == 100 else (200 if lineage >= 71 else 160)
                if lineage >= 71: warning_errors.append("💡【運命武器】家柄71以上のため使用可能です。")
            elif race == "サイボーグ":
                mod_hp += 22 if lineage == 100 else (17 if lineage >= 71 else 12)
                mod_stamina += 3 if lineage == 100 else (2 if lineage >= 71 else 1)
                for k in ["筋力", "生命", "敏捷"]: stats[k] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5), exclude=["筋力", "生命", "敏捷"])
                bonus_sp += 170 if lineage == 100 else (120 if lineage >= 71 else 70)
            elif race == "アンドロイド":
                mod_hp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                mod_mp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_stamina += 4 if lineage == 100 else (3 if lineage >= 71 else 2)
                add_stats_group(17 if lineage == 100 else (12 if lineage >= 71 else 7))
            elif race == "クローン《デザイナーベビー》":
                mod_hp += 17 if lineage == 100 else (12 if lineage >= 71 else 8)
                mod_mp += 17 if lineage == 100 else (12 if lineage >= 71 else 8)
                mod_stamina += 4 if lineage == 100 else 3
                add_stats_group(17 if lineage == 100 else (12 if lineage >= 71 else 8))
                bonus_sp += 200 if lineage == 100 else (150 if lineage >= 71 else 100)
                warning_errors.append("💡【クローン】運命武器使用可能です。")
            elif race == "幻影体発現者":
                mod_hp += 10 if lineage == 100 else (6 if lineage >= 91 else (4 if lineage >= 71 else 2))
                mod_mp += 10 if lineage == 100 else (6 if lineage >= 91 else (4 if lineage >= 71 else 2))
                mod_stamina += 4 if lineage == 100 else (3 if lineage >= 71 else 2)
                for k in ["筋力", "生命", "容姿"]: stats[k] += 8 if lineage == 100 else (6 if lineage >= 91 else (4 if lineage >= 71 else 2))
                if sub == "エレメンツ": bonus_sp += 150 if lineage == 100 else (100 if lineage >= 71 else 50)
            elif race == "ヴィロン":
                mod_hp += 30 if lineage == 100 else (25 if lineage >= 71 else 20)
                stats["筋力"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                add_stats_group(5, exclude=["筋力"])
            elif race == "ノクト・ヴァンパイア":
                hp_mp = 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_hp += hp_mp; mod_mp += hp_mp
                add_stats_group(20 if lineage == 100 else (15 if lineage >= 71 else 10))
            elif race == "ノクス・エルフ":
                mod_hp += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                mod_mp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                stats["知力"] += 22 if lineage == 100 else (17 if lineage >= 71 else 12)
                stats["容姿"] += 21 if lineage == 100 else (16 if lineage >= 71 else 11)
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5), exclude=["商才", "知力", "容姿"])
                if lineage >= 91: mod_hp += 5; mod_mp += 5
            elif race == "ノクス・ハーフエルフ":
                mod_hp += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                mod_mp += 22 if lineage == 100 else (17 if lineage >= 71 else 12)
                stats["知力"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                stats["容姿"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                add_stats_group(15 if lineage == 100 else (8 if lineage >= 71 else 4), exclude=["知力", "容姿"])
                bonus_sp += 250 if lineage == 100 else (150 if lineage >= 71 else 50)
                warning_errors.append("💡【運命武器】運命装備使用可能です。")
            elif race == "ホットロード・サイボーグ":
                warning_errors.append("💡【改造点】生命+精神の合計分だけ自身を強化可能です(手動で加算)。")
            elif race == "意識人造体（イニシエーター）":
                mod_hp += 15 if lineage == 100 else (12 if lineage >= 71 else 10)
                mod_mp += 15 if lineage == 100 else (12 if lineage >= 71 else 10)
                mod_stamina += 3 if lineage == 100 else (2 if lineage >= 71 else 1)
                add_stats_group(15 if lineage == 100 else (12 if lineage >= 71 else 10))
            elif race == "人工獣人":
                mod_hp += 30 if lineage == 100 else (25 if lineage >= 71 else 20)
                mod_stamina += 5 if lineage == 100 else (4 if lineage >= 71 else 3)
                stats["筋力"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                add_stats_group(10 if lineage == 100 else (5 if lineage >= 71 else 3), exclude=["筋力", "知力", "精神"])
                stats["知力"] -= 3 if lineage == 100 else (5 if lineage >= 71 else 10)
                stats["精神"] -= 3 if lineage == 100 else (5 if lineage >= 71 else 10)
            elif race == "強化人兵":
                mod_mp += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_stamina += 3 if lineage == 100 else (2 if lineage >= 71 else 1)
                add_stats_group(17 if lineage == 100 else (12 if lineage >= 71 else 7), exclude=["精神"])
                stats["精神"] -= 5 if lineage == 100 else (10 if lineage >= 71 else 15)
            elif race == "羅刹":
                mod_hp += 6 if lineage == 100 else (4 if lineage >= 71 else 2)
                mod_mp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_stamina += 1
                add_stats_group(6 if lineage == 100 else (4 if lineage >= 71 else 2), exclude=["容姿"])
                stats["容姿"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                if sub == "悪夢(15点)": stats["精神"] += 5
                elif sub == "悲痛(20点)": stats["生命"] += 5
                elif sub == "狂乱(25点)": stats["生命"] += 5
                elif sub == "血涙(30点)": mod_hp += 5
            elif race == "オートマタ":
                mod_hp += 22 if lineage == 100 else (17 if lineage >= 71 else 12)
                mod_mp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_stamina += 3 if lineage == 100 else (2 if lineage >= 71 else 1)
                for k in ["筋力", "知力", "敏捷", "精神", "体格", "生命"]: stats[k] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                stats["容姿"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
            elif race == "アルラウネ":
                mod_hp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                mod_mp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                stats["容姿"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5), exclude=["容姿"])
                stats["容姿"] += lvl_num; mod_hp += lvl_num * 3
            elif race == "デトネーター":
                mod_hp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                mod_mp += 11 if lineage == 100 else (8 if lineage >= 71 else 5)
                add_stats_group(11 if lineage == 100 else (8 if lineage >= 71 else 5))
            elif race == "スチームブッチャー":
                # ↓↓↓ これをブロックの先頭に追加 ↓↓↓
                st.success("✅ スチームブッチャーの部屋に侵入成功！")
                st.info(f"【＋30する前】の筋力: {stats['筋力']}")
        
                # (元々の計算コード)
                mod_hp += 25; mod_mp += 10; mod_stamina -= 2
                add_stats_group(8, exclude=["筋力"])
                stats["筋力"] += 30
        
                # ↓↓↓ これを計算の直後に追加 ↓↓↓
                st.info(f"【＋30した後】の筋力: {stats['筋力']}")
            elif race == "怪異憑依者／怪人":
                val = 15 if lineage == 1 else (13 if lineage == 100 else (8 if lineage >= 71 else 3))
                mod_hp += val; mod_mp += val
                add_stats_group(val)


    blessing = st.session_state.get('blessing', [])
    blessing_text_out = ""

    actual_attr = st.session_state.get('attr')
    actual_attr1 = p.get('attr1', list_attr_sub[0])
    actual_attr2 = p.get('attr2', list_attr_sub[1])

    ab_magic_extra = ""

    # --- 基本補正 ---
    age = p['age']
    if age == "幼年":
        mod_hp -= 10; mod_stamina += 3; stats["精神"] -= 5; stats["知力"] -= 5; stats["敏捷"] += 10; stats["体格"] -=10; bonus_sp -= 70
    elif age == "青年":
        mod_hp += 10; mod_mp += 5; stats["筋力"] += 3
        for k in ["知力", "敏捷", "精神", "体格", "生命", "容姿"]: stats[k] += 2
    elif age == "壮年":
        mod_hp += 5; mod_mp += 10; stats["精神"] += 3
        for k in ["筋力", "知力", "敏捷", "体格", "生命", "容姿"]: stats[k] += 2
    elif age == "中年":
        mod_hp -= 5; mod_stamina -= 1; mod_mp += 10; stats["精神"] += 5; stats["知力"] += 5; stats["筋力"] -= 5; stats["敏捷"] -= 5; bonus_sp += 35
        for k in ["体格", "生命", "容姿"]: stats[k] += 1
    elif age == "老年":
        mod_hp -= 10; mod_stamina -= 2; mod_mp += 15; stats["知力"] += 10; stats["精神"] += 10; stats["生命"] -= 10; stats["体格"] -= 10; stats["筋力"] -= 10; stats["敏捷"] -= 5; bonus_sp += 70

    gender = p['gender']
    if gender == "男": stats["筋力"] += 5; stats["生命"] += 5; mod_hp += 5
    elif gender == "女": stats["知力"] += 5; stats["敏捷"] += 5; mod_mp += 5
    elif gender == "中性":
        mod_hp += 2; mod_mp += 2
        for k in ["筋力", "知力", "敏捷", "精神"]: stats[k] += 2

    ethnicity = p['ethnicity']
    if ethnicity == "東方人": stats["精神"] += 3; stats["敏捷"] += 3
    elif ethnicity == "西方人": stats["知力"] += 3; stats["容姿"] += 3
    elif ethnicity == "南方人": stats["生命"] += 3; stats["筋力"] += 3
    elif ethnicity == "北方人": stats["体格"] += 3; stats["生命"] += 3

    lineage = p['lineage']
    if p['past0'] == "⑥血統": lineage += 2
    if p['past1'] == "④禁断": lineage += 2

    past0, past1, past2 = p['past0'], p['past1'], p['past2']
    if past0 == "➁生存": stats["生命"] += 3; mod_hp += 5
    if past0 == "③悲哀": stats["精神"] += 3; mod_mp += 5
    if past0 == "④愚行": stats["筋力"] += 3; mod_stamina += 1
    if past0 == "⑤才能": stats["知力"] += 3; bonus_sp += 50
    if past0 == "⑦復讐": stats["敏捷"] += 3; mod_hp += 3; mod_mp += 3
    if past1 == "①孤独": stats["筋力"] += 5; stats["知力"] -= 5
    if past1 == "③愛情": stats["知力"] += 5; stats["筋力"] -= 5
    if past1 == "④禁断": stats["精神"] += 5; stats["生命"] -= 5
    if past1 == "⑤特別":
        for k in base_stats_names: stats[k] += 1
    if past1 == "⑥苦痛": stats["敏捷"] += 5; stats["精神"] -= 5
    if past2 == "①暴力": stats["筋力"] += 5; stats["知力"] -= 5
    elif past2 == "➁矜持": stats["精神"] += 5
    elif past2 == "③風詠": stats["敏捷"] += 5; stats["生命"] -= 5
    elif past2 == "④勤勉": stats["知力"] += 5; stats["筋力"] -= 5
    elif past2 == "⑤失意": stats["生命"] += 5; stats["精神"] -= 5
    elif past2 == "⑥憧憬": stats["容姿"] += 2; stats["精神"] -= 4; mod_luck += 2

    adjust_val = 1 if past0 == "①凡庸" else (2 if past1 == "➁平凡" else 0)
    if adjust_val > 0:
        for cp in p.get('combo_plus', []):
            if cp != "(なし)" and cp in stats: stats[cp] += adjust_val
        for cm in p.get('combo_minus', []):
            if cm != "(なし)" and cm in stats: stats[cm] -= adjust_val

    # --- 出自 ---
    bg = p['bg']
    bg_sub = p.get('bg_sub', '')

    if origin == "ファンタジア":
        if bg == "騎士": mod_hp += 10
        elif bg == "賊": bonus_ab_melee += 2
        elif bg == "魔術師": bonus_ab_magic += 2; mod_mp += 10
        elif bg == "聖職者": mod_mp += 20
        elif bg == "貴族":
            if lineage >= 71: bonus_sp += 120
            else: warning_errors.append("【貴族】家柄71以上が必要です")
        elif bg == "放浪戦士": mod_stamina += 2; bonus_ab_melee += 1
        elif bg in ["侍", "双剣士", "銃剣士"]: bonus_sp += 70
        elif bg == "商人": stats["商才"] += 10; bonus_sp += 30
        elif bg == "淑女":
            if gender == "女": bonus_sp += 70; stats["容姿"] += 6
            else: warning_errors.append("【淑女】性別「女」専用です")
        elif bg == "通常使用人": stats["容姿"] += 3; stats["知力"] += 3; bonus_sp += 70; mod_mp += 5
        elif bg == "戦闘使用人": stats["容姿"] += 3; stats["知力"] += 3; bonus_sp += 70; mod_hp += 5
        elif bg == "多重人格者": mod_mp += 5; bonus_sp += 30
        elif bg == "対偶者": bonus_sp += 35; stats["容姿"] += 2
        elif bg == "海賊": mod_hp += 5; mod_stamina += 1; bonus_sp += 30
        elif bg == "祈祷者": mod_mp += 10
        elif bg == "蛮族": mod_hp += 5; bonus_sp += 20
        elif bg == "贖血徒":
            if is_demon:
                is_atoning_blood = True; mod_stamina -= 1
                for key in base_stats_names: stats[key] -= 10
            else: warning_errors.append("【贖血徒】魔族専用の出自です")
    elif origin == "ノクターン":
        if bg == "軍人":
            mod_hp += 5
            if bg_sub == "下士官": bonus_sp += 100
            elif bg_sub == "パイロット": bonus_sp += 140
            warning_errors.append("💡【軍人ボーナス】指定ステータスに+4手動で割り振ってください。")
        elif bg == "暴漢": stats["筋力"] += 6; bonus_ab_melee += 2
        elif bg == "ブルジョア":
            if lineage >= 71: bonus_sp += 150
            else: warning_errors.append("【ブルジョア】家柄71以上が必要です")
        elif bg == "傭兵": mod_stamina += 1; bonus_ab_melee += 1; stats["筋力"] += 3; stats["敏捷"] += 3; mod_hp += 5; bonus_sp += 50
        elif bg == "芸術家": bonus_sp += 140; stats["精神"] += 6
        elif bg == "盗人": bonus_sp += 140; stats["敏捷"] += 6
        elif bg == "狩人": bonus_sp += 140; stats["敏捷"] += 3; stats["生命"] += 3
        elif bg == "貧者": pass
        elif bg == "商人": stats["商才"] += 10; bonus_sp += 30
        elif bg == "探偵": bonus_sp += 120; mod_mp += 12; stats["知力"] += 10
        elif bg == "煙突掃除人": mod_hp += 7; mod_mp += 7; bonus_sp += 120; warning_errors.append("💡【煙突掃除人】指定ステータスに+4手動で割り振ってください。")
        elif bg == "使用人":
            stats["容姿"] += 3; stats["知力"] += 3
            if bg_sub == "使用人": bonus_sp += 120; mod_mp += 5
            elif bg_sub == "戦闘使用人": bonus_sp += 120; mod_hp += 5
        elif bg == "官吏": bonus_sp += 150; stats["精神"] += 6
        elif bg == "医者": bonus_sp += 70; stats["知力"] += 6; mod_hp += 3; mod_mp += 5
        elif bg == "淑女":
            if gender == "女": bonus_sp += 120; stats["容姿"] += 6
            else: warning_errors.append("【淑女】性別「女」専用です")
        elif bg == "多重人格者": mod_mp += 5; bonus_sp += 30
        elif bg == "警官":
            if bg_sub == "警官": bonus_sp += 70; mod_hp += 10; warning_errors.append("💡【警官】指定ステータスに+8手動で割り振ってください。")
            elif bg_sub == "汚職警官": bonus_sp += 120; mod_hp += 5; warning_errors.append("💡【汚職警官】指定ステータスに+5手動で割り振ってください。")
        elif bg == "無法者":
            if bg_sub == "ギャング": bonus_sp += 50; mod_hp += 5; stats["筋力"] += 5
            elif bg_sub == "マフィア": bonus_sp += 70; bonus_ab_melee += 3; mod_mp += 5; stats["筋力"] += 2
        elif bg == "対偶者": bonus_sp += 35; stats["容姿"] += 2
        elif bg == "教授": bonus_sp += 180; mod_mp += 5; mod_hp += 5
        elif bg == "ペテン師": mod_hp += 5; mod_mp += 5; stats["知力"] += 3; bonus_sp += 60
        elif bg == "怪盗": mod_mp += 10; bonus_sp += 100
        elif bg == "水兵": mod_hp += 5; mod_mp += 5; bonus_sp += 120; warning_errors.append("💡【水兵】指定ステータスに+4手動で割り振ってください。")
        elif bg == "僭称者": bonus_sp += 200; warning_errors.append("💡【僭称者】家柄を+1d10して手動で修正してください。")
        elif bg == "叫喚者": pass
        elif bg == "拳闘士": pass
        elif bg == "囚憶者": mod_mp += 5

    # --- ジョブ処理 ---
    job1_1 = p['job1_1']; job1_1_lv = int(p['job1_1_lv'])
    job1_2 = p['job1_2']; job1_2_lv = int(p['job1_2_lv'])
    job2 = p['job2']; job2_lv = int(p['job2_lv'])
    magic_sp = 0
    job_texts = []

    if origin == "ファンタジア":
        def apply_job_passive_fan(job_name, lv):
            nonlocal magic_sp, mod_mp, mod_hp, mod_stamina
            if job_name == "治癒術師":
                mod_mp += 5; magic_sp += 40 if lv >= 2 else 0; magic_sp += 40 if lv >= 3 else 0
            elif job_name == "霊術師": mod_mp += 10
            elif job_name == "魔力射撃士": mod_mp += 5; mod_mp += 5 if lv >= 2 else 0
            elif job_name == "蛮戦士":
                if lv >= 3: mod_hp += 5; mod_stamina += 2
            elif job_name == "戦士": mod_hp += 3; mod_mp += 3 if lv >= 2 else 0
            elif job_name == "冒険者": mod_hp += 5; mod_mp += 5
            elif job_name == "魔術師": magic_sp += 40 if lv >= 2 else 0; magic_sp += 40 if lv >= 3 else 0
            elif job_name == "魔法術師": magic_sp += 40 if lv >= 2 else 0; magic_sp += 40 if lv >= 3 else 0
            elif job_name == "魔女": magic_sp += 30 if lv >= 1 else 0; magic_sp += 30 if lv >= 3 else 0

        if job1_1 != "(なし)": apply_job_passive_fan(job1_1, job1_1_lv)
        if job1_2 != "(なし)": apply_job_passive_fan(job1_2, job1_2_lv)

        if job2 != "(なし)":
            if lvl_num < 4 and job2 != "武士": warning_errors.append("【二次職エラー】二次職はLv4以上から選択可能です。")
            elif lvl_num < 5 and job2 == "武士": warning_errors.append("【二次職エラー】武士はLv5以上から選択可能です。")
            def check_job_req(req1, req2):
                has_req1 = (job1_1 == req1 and job1_1_lv >= 3) or (job1_2 == req1 and job1_2_lv >= 3)
                has_req2 = (job1_1 == req2 and job1_1_lv >= 3) or (job1_2 == req2 and job1_2_lv >= 3)
                if not (has_req1 and has_req2): warning_errors.append(f"【二次職条件未達】{job2}の条件({req1}Lv3＆{req2}Lv3)を満たしていません。")
            if job2 == "騎士":
                check_job_req("旅騎士", "修練者"); mod_hp += 15; job_texts.append("騎士【全防御力+25】")
                if job2_lv >= 2: mod_hp += 5; job_texts.append("騎士Lv2【全防御力+25(累計+50)】")
            elif job2 == "魔導騎士": check_job_req("旅騎士", "魔術師"); mod_mp += 10 if job2_lv >= 2 else 0
            elif job2 == "魔導士":
                check_job_req("魔術師", "修練者"); mod_mp += 10 if job2_lv >= 2 else 0; mod_hp += 5 if job2_lv >= 4 else 0
            elif job2 == "魔導術師": check_job_req("魔術師", "魔法術師"); mod_mp += 10; mod_mp += 10 if job2_lv >= 2 else 0
            elif job2 == "魔導狙撃士": check_job_req("魔力射撃士", "魔術師"); mod_mp += 7; mod_mp += 8 if job2_lv >= 2 else 0
            elif job2 == "錬金術師": check_job_req("魔女", "修練者"); mod_mp += 10
            elif job2 == "治癒神官": check_job_req("治癒術師", "修練者"); mod_mp += 10
            elif job2 == "死霊術師": check_job_req("霊術師", "魔女"); mod_mp += 10
            elif job2 == "竜騎士": check_job_req("軽槍兵", "軽業師"); mod_mp += 5 if job2_lv >= 2 else 0
            elif job2 == "狂戦士":
                check_job_req("戦士", "蛮戦士"); mod_hp += 5
                if job2_lv >= 2: mod_stamina += 2
                if job2_lv >= 4: bonus_ab_melee += 5
            elif job2 == "銃士": check_job_req("射撃士", "遊撃師")
            elif job2 == "武士": check_job_req("旅騎士", "修練者"); mod_hp += 10
            elif job2 == "忍":
                check_job_req("軽業師", "遊撃師")
                job_texts.append("忍Lv0: 忍術【魔導剣&脇差威力+20% / 回避+2(突破)】")
                if job2_lv >= 1: job_texts.append("忍Lv1: 手投げ術【投擲使用時、威力+50%】")
                if job2_lv >= 2: job_texts.append("忍Lv2: 忍術強化【魔導剣&脇差威力+30% / 回避+3】")
                if job2_lv >= 3: job_texts.append("忍Lv3: 透破【隠密70以上時、回避失敗時に基準値-10で再判定可(CT3)】")
                if job2_lv >= 4: job_texts.append("忍Lv4: 乱波【戦技発動後2ターン片手武器ダメ+5(CT3)】")
                
            elif job2 == "剣闘士":
                check_job_req("戦士", "軽槍兵")
                mod_hp += 5
                if job2_lv >= 1: job_texts.append("剣闘士Lv1: 戦闘本能【1ターン回避-20&被ダメ+50%の代わり物理+70%(CT3)】")
                if job2_lv >= 2: mod_hp += 10
                if job2_lv >= 3: job_texts.append("剣闘士Lv3: 開戦鼓舞【味方全体(最大4名)のHP・ST10%回復(CT3)】")
                if job2_lv >= 4: job_texts.append("剣闘士Lv4: 開戦鼓舞強化【HP・ST回復量20%に上昇】")
                
            elif job2 == "精霊師":
                check_job_req("霊術師", "治癒術師")
                mod_mp += 10; job_texts.append("精霊師Lv0: 魔法消費MP-5 / 回復魔法消費MP-5")
                if job2_lv >= 1: job_texts.append("精霊師Lv1: 精霊たちの祝福【味方全体(最大4名)のHP・MP10%回復＆解呪(CT5)】")
                if job2_lv >= 2: job_texts.append("精霊師Lv2: 精霊たちの祝福強化【事前動作に変更 / MP回復量20%】")
                if job2_lv >= 3: job_texts.append("精霊師Lv3: 精霊纏い【2ターンの間、即死ダメ時に幸運成功でHP1生存(1戦闘1回)】")
                if job2_lv >= 4: job_texts.append("精霊師Lv4: 精霊纏い強化【幸運判定失敗時、基準値10で一度だけ再判定可】")
                
            elif job2 == "弓騎士":
                check_job_req("射撃士", "修練者")
                if job2_lv >= 1: job_texts.append("弓騎士Lv1: 銀撃【1ターン物理射撃ダメ30%UP(CT3)】")
                if job2_lv >= 2: job_texts.append("弓騎士Lv2: 銀撃強化【効果ターン+1】")
                if job2_lv >= 3: job_texts.append("弓騎士Lv3: アーチェリーオブバトルライン【両手射撃装備時、回避失敗時に基準値20で再判定可(CT5)】")
                if job2_lv >= 4: job_texts.append("弓騎士Lv4: アーチェリーオブバトルライン強化【発動中、射撃威力+5】")
                
            elif job2 == "勇者":
                # ツール上の一次職枠は2つなので、エラーで進行不能にならないよう警告のみ出します
                warning_errors.append("💡【勇者】前提条件として冒険者・修練者・旅騎士・魔術師のLv3が必要です。")
                mod_hp += 5; mod_mp += 5
                job_texts.append("勇者Lv0: 全武器威力+10%(片手剣,両手剣,複銃剣除く)")
                if job2_lv >= 1: job_texts.append("勇者Lv1: 勇気の剣術【片/両手剣威力+20% / 複銃剣斬撃+20% / 双剣に防御半減付与】")
                if job2_lv >= 2: job_texts.append("勇者Lv2: 勇気の魔法【魔法攻撃+10% / 魔法回復+5% / 魔法消費MP-10%】")
                if job2_lv >= 3: job_texts.append("勇者Lv3: 勇者への道【1ターン攻撃+15%, 全防御+15%, 全防護+5, 回避+5(突破)(1戦闘1回)】")
                if job2_lv >= 4: job_texts.append("勇者Lv4: 勇者への道強化【持続ターン数が2ターンに増加】")

    elif origin == "ノクターン":
        def apply_job_passive_noc(job_name, lv):
            nonlocal mod_mp, mod_hp, mod_stamina, bonus_mental
            if job_name == "下士官":
                if lv >= 1: mod_hp += 2
                if lv >= 2: mod_mp += 2
                if lv >= 3: job_texts.append("戦技『規律』(与ダメ+10%/CT3)")
            elif job_name == "傭兵":
                if lv >= 1: mod_hp += 2
                if lv >= 2: mod_hp += 2
                if lv >= 3: job_texts.append("戦技『突撃』(被ダメ-10%/CT3)")
            elif job_name == "斥候":
                if lv >= 1: job_texts.append("戦技『斥候射撃』(狙撃銃威力+20%/MP-20/CT1)")
                if lv >= 2: mod_mp += 3
                if lv >= 3: job_texts.append("戦技『斥候射撃(強)』(狙撃銃威力+30%/MP-30/CT1)")
            elif job_name == "襲撃者":
                if lv >= 1: mod_hp += 2
                if lv >= 2: job_texts.append("回避+2")
                if lv >= 3: job_texts.append("戦技『襲撃』(命中-20, 与ダメ+20%/CT3)")
            elif job_name == "強奪者":
                if lv >= 1: mod_stamina += 2
                if lv >= 2: job_texts.append("回避+2")
                if lv >= 3: job_texts.append("戦技『強奪』(ダメ30%ドレイン/CT3)")
            elif job_name == "旅芸人":
                if lv >= 1: job_texts.append("戦技『曲芸』(敵回避基準+5/CT3)")
                if lv >= 2: mod_mp += 5; job_texts.append("『曲芸』強化(継続2T/CT2)")
                if lv >= 3: job_texts.append("特性『不測の芸当』(曲芸中ナイフ投擲+30%)")
            elif job_name == "手品師":
                if lv >= 1: job_texts.append("戦技『ミスディレクション』(魔法威力+25%/CT2)")
                if lv >= 2: mod_mp += 10
                if lv >= 3: job_texts.append("戦技『シャッフル・ルーレット』(HPダメ or 回復)")
            elif job_name == "早撃手":
                if lv >= 1: mod_mp += 3
                if lv >= 2: mod_mp += 3
                if lv >= 3: job_texts.append("戦技『早撃ち』(リボルバー2発発射)")
            elif job_name == "労働者":
                if lv >= 1: job_texts.append("戦技『労働精神』(敵ダメ累減-10%/CT3)")
                if lv >= 2: bonus_mental += 1
                if lv >= 3: bonus_mental += 1
            elif job_name == "歩兵":
                if lv >= 1: job_texts.append("戦技『小銃射撃』(小銃威力+5%)")
                if lv >= 2: mod_hp += 2
                if lv >= 3: mod_mp += 2
            elif job_name == "格闘兵":
                if lv >= 0: job_texts.append("戦技『強襲格闘』(近接+10%, 接近+5, 回避-10)")
                if lv >= 1: job_texts.append("『強襲格闘』強化(近接+20%)")
                if lv >= 2: job_texts.append("戦技『アサルトインファイト』(連撃反動-8)")
                if lv >= 3: job_texts.append("『アサルトインファイト』強化(連撃反動-5)")

        if job1_1 != "(なし)": apply_job_passive_noc(job1_1, job1_1_lv)
        if job1_2 != "(なし)": apply_job_passive_noc(job1_2, job1_2_lv)

        if job2 != "(なし)":
            if lvl_num < 4: warning_errors.append("【二次職エラー】二次職はLv4以上から選択可能です。")
            def check_job_req_noc(req1, req2=None):
                has_req1 = (job1_1 == req1 and job1_1_lv >= 3) or (job1_2 == req1 and job1_2_lv >= 3)
                has_req2 = (job1_1 == req2 and job1_1_lv >= 3) or (job1_2 == req2 and job1_2_lv >= 3) if req2 else True
                if req2 and not (has_req1 and has_req2): warning_errors.append(f"【二次職条件未達】{job2}の条件({req1}Lv3＆{req2}Lv3)を満たしていません。")
                elif not req2 and not has_req1: warning_errors.append(f"【二次職条件未達】{job2}の条件({req1}Lv3)を満たしていません。")
            if job2 == "特技士官":
                check_job_req_noc("下士官")
                if job2_lv >= 1: mod_hp += 5
                if job2_lv >= 2: mod_mp += 5
                if job2_lv >= 3: job_texts.append("戦技『特殊作戦』(与ダメ+30%/CT3)")
                if job2_lv >= 4: mod_hp += 5; mod_mp += 5
            elif job2 == "突撃傭兵":
                check_job_req_noc("傭兵")
                if job2_lv >= 1: mod_hp += 3
                if job2_lv >= 2: mod_hp += 3
                if job2_lv >= 3: job_texts.append("戦技『散兵突撃』(被ダメ-20%/CT3)")
                if job2_lv >= 4: job_texts.append("『散兵突撃』強化(攻撃威力+10%)")
            elif job2 == "狙撃手":
                check_job_req_noc("斥候")
                if job2_lv >= 1: job_texts.append("戦技『急所狙撃』(狙撃銃威力+1D, 狙撃威力+15%/MP-25)")
                if job2_lv >= 2: job_texts.append("狙撃銃威力+10%")
                if job2_lv >= 3: job_texts.append("『急所狙撃』強化(狙撃銃威力+2D)")
                if job2_lv >= 4: job_texts.append("狙撃銃威力+20%")
            elif job2 == "略奪者":
                check_job_req_noc("襲撃者")
                if job2_lv >= 1: mod_hp += 3
                if job2_lv >= 2: job_texts.append("回避+3")
                if job2_lv >= 3: job_texts.append("戦技『略奪』(ダメ半分ドレイン/CT6)")
                if job2_lv >= 4: mod_hp += 5
            elif job2 == "強襲兵":
                check_job_req_noc("歩兵")
                if job2_lv >= 1: mod_mp += 3
                if job2_lv >= 2: job_texts.append("回避+2")
                if job2_lv >= 3: job_texts.append("戦技『強襲』(HP-50%,MP-30/与ダメ+50%,命中+20,被ダメ+100%/CT10)")
                if job2_lv >= 4: mod_hp += 3
            elif job2 == "喜劇役者":
                check_job_req_noc("旅芸人")
                if job2_lv >= 1: job_texts.append("戦技『笑劇』(敵回避基準+10/CT6)")
                if job2_lv >= 2: job_texts.append("戦技『喜劇』(HP&MP20%回復/CT6)")
                if job2_lv >= 3: job_texts.append("『笑劇』強化(CT3)")
                if job2_lv >= 4: job_texts.append("『喜劇』強化(回復量40%)")
            elif job2 == "奇術師":
                check_job_req_noc("手品師", "旅芸人")
                if job2_lv >= 0: mod_mp += 10; job_texts.append("魔術消費MP-3")
                if job2_lv >= 1: job_texts.append("戦技『Truth or Lie』(魔術確定命中/威力倍率上限50%/CT3)")
                if job2_lv >= 2: job_texts.append("戦技『This Illusion, No Deception』(ダメ予想±5で魔法威力+100%/CT3)")
                if job2_lv >= 3: mod_mp += 5
                if job2_lv >= 4: job_texts.append("特性『Ladies and Gentlemen』(男女ペアでHP&MP+10%)")
            elif job2 == "近接兵":
                check_job_req_noc("格闘兵")
                if job2_lv >= 0: job_texts.append("戦技『白兵戦闘』(近接+20%/CT2)")
                if job2_lv >= 1: job_texts.append("戦技『高速突撃』(接近失敗時基準20で再判定/CT2)")
                if job2_lv >= 2: job_texts.append("『高速突撃』強化(基準10で再判定)")
                if job2_lv >= 3: job_texts.append("『高速突撃』強化(CT1)")
                if job2_lv >= 4: job_texts.append("『白兵戦闘』強化(近接+30%)")
            elif job2 == "銃巧手":
                check_job_req_noc("早撃手", "歩兵")
                if job2_lv >= 0: mod_hp += 5; mod_stamina += 3; job_texts.append("銃の反動-1")
                if job2_lv >= 1: job_texts.append("戦技『カウンターバレット』(リボルバー手持ち時回避でカウンター射撃)")
                if job2_lv >= 2: job_texts.append("戦技『ファーストスウィング』(騎兵銃+1D/CT3)")
                if job2_lv >= 3: job_texts.append("戦技『ブルズアイショット』(拳銃威力+3/敵回避基準+5/CT5)")

    # --- ファンタジア限定システム ---
    fan_sys_texts = []
    if origin == "ファンタジア":
        stance = p['stance']
        stance_lv = int(p['stance_lv'])
        school = p['school']
        if stance != "(なし)" and stance_lv > 0:
            if stance == "正眼の構え":
                if stance_lv >= 1: mod_stamina += 1
                if stance_lv >= 2: mod_hp += 5
                if stance_lv >= 3: mod_mp += 5
            elif stance == "天の構え":
                if stance_lv >= 1: fan_sys_texts.append("【天の構え】威力+30% / 被ダメ+30% / 回避-10")
                if stance_lv >= 2: mod_hp += 2
                if stance_lv >= 3: mod_hp += 2
            elif stance == "地の構え":
                if stance_lv >= 1: fan_sys_texts.append("【地の構え】弾き成功時、敵ダメージ-10%")
                if stance_lv >= 2: mod_mp += 2
                if stance_lv >= 3: mod_mp += 2
            elif stance == "八相の構え":
                if stance_lv >= 1: fan_sys_texts.append("【八相の構え】威力+10%")
                if stance_lv >= 2: mod_hp += 3
                if stance_lv >= 3: mod_mp += 3
            elif stance == "陽の構え":
                if stance_lv >= 1: fan_sys_texts.append("【陽の構え】弾き成功時、敵ダメ-5% / 弾き成功時HP-10でカウンター可")
                if stance_lv >= 2: mod_stamina += 1
                if stance_lv >= 3: mod_stamina += 1
            elif stance == "霞の構え":
                if stance_lv >= 1: fan_sys_texts.append("【霞の構え】弾き成功時、初撃のみ確定反撃 / 1戦闘1回のみ弾き値+2d")
                if stance_lv >= 2: mod_stamina += 1
                if stance_lv >= 3: mod_hp += 2
            elif stance == "蜻蛉の構え":
                if stance_lv >= 1: fan_sys_texts.append("【蜻蛉の構えLv1】(※発声必須) 初撃威力+30% / 被ダメ+30% / 回避-5")
                if stance_lv >= 2: fan_sys_texts.append("【蜻蛉の構えLv2】初撃威力+10% / 被ダメ+10% / 回避-5 (累積)")
                if stance_lv >= 3: fan_sys_texts.append("【蜻蛉の構えLv3】初撃威力+10% / 被ダメ+10% / 回避-5 (累積)")
                warning_errors.append("💡【蜻蛉の構え】「天の構えLv2」の解放が前提条件です。")
        if school != "(なし)":
            elf_races = ["ハイエルフ", "ダークエルフ", "ウッドエルフ", "スノウエルフ", "フレイムエルフ"]
            if school == "ミドガルネ帝国魔導学園":
                mod_hp -= 15; fan_sys_texts.append(f"【{school}】元素魔術の消費MP-10%")
            elif school == "ユーグランス天空魔術学園":
                mod_mp -= 10; fan_sys_texts.append(f"【{school}】元素魔術使用時、威力+10%")
            elif school == "方術院":
                mod_hp -= 5; mod_mp -= 5; fan_sys_texts.append(f"【{school}】元素AB+1D / 元素MP-5%")
            elif school == "シャルディア中央魔導城":
                mod_mp -= 15; fan_sys_texts.append(f"【{school}】元素魔術使用時、魔導学AB+2D")
            elif school == "イリコフォティア大魔導学院":
                mod_hp -= 15; fan_sys_texts.append(f"【{school}】魔力魔術使用時の消費MP-10%")
            elif school == "陰陽学所":
                mod_mp -= 10; fan_sys_texts.append(f"【{school}】魔力魔術使用時、威力+10%")
            elif school == "アンブローズ王立魔法学校":
                mod_hp -= 5; mod_mp -= 5; fan_sys_texts.append(f"【{school}】魔力AB+1D / 魔力MP-5%")
            elif school == "ロクス魔導騎士学院":
                mod_mp -= 15; fan_sys_texts.append(f"【{school}】魔力魔術使用時、魔導学AB+2D")
            elif school == "元素教会神秘学舎":
                mod_hp -= 15; fan_sys_texts.append(f"【{school}】回復系神秘術＆回復魔法の消費MP-10%")
                if actual_attr != "光属性": warning_errors.append(f"⚠️【流派エラー】{school}は光属性専用です。")
            elif school == "神聖魔術学園":
                mod_hp -= 15; fan_sys_texts.append(f"【{school}】攻撃系神秘術の消費MP-10%")
                if actual_attr != "光属性": warning_errors.append(f"⚠️【流派エラー】{school}は光属性専用です。")
            elif school == "白亜の魔導塔":
                mod_hp -= 20; mod_mp -= 20; fan_sys_texts.append(f"【{school}】元素AB+2D / 元素MP-10%")
                if race not in elf_races: warning_errors.append(f"⚠️【流派エラー】{school}はエルフ専用（ハーフ不可）です。")
            elif school == "冒険者ギルド元素魔導教練所":
                fan_sys_texts.append(f"【{school}】元素魔術使用時の消費MP-5%")
            elif school == "星見の魔導空船":
                mod_hp -= 20; mod_mp -= 20; fan_sys_texts.append(f"【{school}】魔力AB+2D / 魔力MP-10%")
            elif school == "冒険者ギルド魔力魔導教練所":
                fan_sys_texts.append(f"【{school}】魔力魔術使用時の消費MP-5%")
            elif school == "大修道院治癒術伝習所":
                fan_sys_texts.append(f"【{school}】回復系神秘術＆回復魔法の消費MP-5%")
            elif school == "アスガリア治癒学校":
                mod_hp -= 15; fan_sys_texts.append(f"【{school}】回復魔法＆支援魔法の消費MP-10%")

    # --- ノクターン限定システム ---
    noc_sys_texts = []
    if origin == "ノクターン":
        s1 = p.get('spec_1', '(なし)'); s2 = p.get('spec_2', '(なし)')
        s3 = p.get('spec_3', '(なし)'); s4 = p.get('spec_4', '(なし)')
        if s1 != "(なし)":
            if lvl_num < 2: warning_errors.append("⚠️【スペシャリスト】第1層の解放にはLv2以上が必要です。")
            if s1 == "小銃手": noc_sys_texts.append(f"【1層: {s1}】自動小銃の反動-2")
            elif s1 == "機関銃手": noc_sys_texts.append(f"【1層: {s1}】伏射中のマシンガン精度+5")
            elif s1 == "対兵器兵": noc_sys_texts.append(f"【1層: {s1}】携行重兵器・対物狙撃・手榴弾の対兵器ダメージ+20%")
            elif s1 == "近接戦闘（CQB）": noc_sys_texts.append(f"【1層: {s1}】フルオート射撃時の弾薬威力1.2倍")
            elif s1 == "近接格闘（CQC）": noc_sys_texts.append(f"【1層: {s1}】武術/短剣使用前に拳銃による事前攻撃可能")
            elif s1 == "マーセナリー": mod_hp += 5; noc_sys_texts.append(f"【1層: {s1}】銃術+5")
            elif s1 == "パフォーマー": noc_sys_texts.append(f"【1層: {s1}】SG特殊弾可 / 重火器予備弾+2 / 使い捨てロケラン片手持ち可(ペナルティ有)")
            elif s1 == "ダンサー": noc_sys_texts.append(f"【1層: {s1}】『二丁拳銃』使用可能")
            elif s1 == "ウィーゼル": noc_sys_texts.append(f"【1層: {s1}】『ダブルブレード』使用可能(連撃まで)")
            elif s1 == "ハンドワーカー": noc_sys_texts.append(f"【1層: {s1}】制作系(前提無)1つ初期値35 / 資金報酬+10%")
            elif s1 == "アプレンティス": noc_sys_texts.append(f"【1層: {s1}】芸術系技能1つ初期値35")
            elif s1 == "スカラー": noc_sys_texts.append(f"【1層: {s1}】学術系(芸術除く/前提無)1つ初期値35")
            elif s1 == "追手": mod_hp += 5; noc_sys_texts.append(f"【1層: {s1}】索敵技能初期値+10")
            elif s1 == "荒くれ者": mod_stamina += 1; noc_sys_texts.append(f"【1層: {s1}】白兵攻撃力+10%")
        if s2 != "(なし)":
            if lvl_num < 3: warning_errors.append("⚠️【スペシャリスト】第2層の解放にはLv3以上が必要です。")
            if s2 == "浸透突撃": noc_sys_texts.append(f"【2層: {s2}】敵人数差1人につき銃撃ダメ+5%(最大+20%)")
            elif s2 == "効率携行術": noc_sys_texts.append(f"【2層: {s2}】マガジン/砲弾/ミサイル携行数+2")
            elif s2 == "高精度狙撃": noc_sys_texts.append(f"【2層: {s2}】狙撃銃初弾威力1.5倍(命中10以下でHSとなり2倍)")
            elif s2 == "生存戦術": noc_sys_texts.append(f"【2層: {s2}】即死ダメ時、精神ロール成功でHP1生存(1戦闘1回)")
            elif s2 == "即応警戒": noc_sys_texts.append(f"【2層: {s2}】蘇生後ペナルティ無効化(1戦闘1回)")
            elif s2 == "サボター": mod_hp += 5; noc_sys_texts.append(f"【2層: {s2}】妨害装置装備可能")
            elif s2 == "ブロッカー": mod_stamina += 1; noc_sys_texts.append(f"【2層: {s2}】大盾装備可能")
            elif s2 == "ハートブレイク": noc_sys_texts.append(f"【2層: {s2}】即死ダメ時、生命ロール成功でHP1生存(1戦闘1回)")
            elif s2 == "タンゴ": noc_sys_texts.append(f"【2層: {s2}】『二丁拳銃〈マシンピストル〉』使用可能")
            elif s2 == "ピューマ": noc_sys_texts.append(f"【2層: {s2}】『アクロバット』使用可能(※要パルクール70)")
            elif s2 == "フォアマン": noc_sys_texts.append(f"【2層: {s2}】制作系(前提無)1つ初期値70(1層上書き可)")
            elif s2 == "アーティスト": noc_sys_texts.append(f"【2層: {s2}】1層スカラー技能失敗時、基準値30で再判定可(1回)")
            elif s2 == "インテレクチュアル": noc_sys_texts.append(f"【2層: {s2}】学術系(芸術除く/前提無)1つ初期値70(1層上書き可)")
            elif s2 == "スルース": noc_sys_texts.append(f"【2層: {s2}】回避+1(上限突破) / 隠れる初期値+10")
            elif s2 == "アンダーリング": mod_hp += 5; noc_sys_texts.append(f"【2層: {s2}】名声-1 / 解錠or盗み初期値+20")
            elif s2 == "オブザーバー": mod_mp += 5; noc_sys_texts.append(f"【2層: {s2}】捜索初期値+15")
        if s3 != "(なし)":
            if lvl_num < 4: warning_errors.append("⚠️【スペシャリスト】第3層の解放にはLv4以上が必要です。")
            if s3 == "突撃兵": noc_sys_texts.append(f"【3層: {s3}】戦技『突撃』取得(2T被ダメ+100%,回避-20/1T与ダメ+50%/CT10)")
            elif s3 == "機動偵察兵": mod_hp += 5; noc_sys_texts.append(f"【3層: {s3}】古びた偵察バイク入手")
            elif s3 == "選抜射手": noc_sys_texts.append(f"【3層: {s3}】対物狙撃銃威力+20% / マークスマンライフル使用可")
            elif s3 == "特殊工作兵": noc_sys_texts.append(f"【3層: {s3}】対人ダメ+10%, 被ダメ-5%, 対兵器ダメ+10%(重兵器時)")
            elif s3 == "潜入兵": noc_sys_texts.append(f"【3層: {s3}】サプレッサー威力+15% / 潜入戦闘服装備可 / 回避+5")
            elif s3 == "空挺兵": noc_sys_texts.append(f"【3層: {s3}】落下ダメ-50%, 装備弾倉数+2, 回避+5, 被ダメ-10%")
            elif s3 == "ベテラン": mod_hp += 5; mod_mp += 5; noc_sys_texts.append(f"【3層: {s3}】与ダメージ+10%")
            elif s3 == "クロスファイア": noc_sys_texts.append(f"【3層: {s3}】銃撃ダメ+10%, 弾倉数+2 / スキル『クロスファイア』(機関銃失敗時MP-15で再射撃)")
            elif s3 == "メンアットアームズ": noc_sys_texts.append(f"【3層: {s3}】コンバットアーマー装備可 / 被ダメージ-10%")
            elif s3 == "ワルツ": noc_sys_texts.append(f"【3層: {s3}】銃撃時、サブ片手剣等で事前攻撃可(2連まで) / 片手剣威力+20%")
            elif s3 == "レオパルド": noc_sys_texts.append(f"【3層: {s3}】回避+5 / パルクールコンボでダメ+50%(アクロバットで+70%)")
            elif s3 == "ジャーニーマン": noc_sys_texts.append(f"【3層: {s3}】アイテム製作失敗時、1日1回基準値30で再判定可")
            elif s3 == "エキシヴィター": mod_mp += 5; stats['知力'] += 1; noc_sys_texts.append(f"【3層: {s3}】技能P+40 / 知力+1(上限突破)")
            elif s3 == "フェロウ": mod_mp += 10; stats['知力'] += 2; noc_sys_texts.append(f"【3層: {s3}】高等学問1つ初期値30(前提無) / 知力+2(上限突破)")
            elif s3 == "オペレーター": mod_stamina += 1; noc_sys_texts.append(f"【3層: {s3}】射撃威力+10% / 名声-5以下への攻撃力+10%")
            elif s3 == "ブルーザー": mod_hp += 5; noc_sys_texts.append(f"【3層: {s3}】喧嘩術威力+50% / 対ホワイトナイトダメ+20%")
            elif s3 == "エミサリー": mod_mp += 10; noc_sys_texts.append(f"【3層: {s3}】『監視』技能解禁(事前判定成功で回避基準5&防護3貫通付与)")
        if s4 != "(なし)":
            if lvl_num < 5: warning_errors.append("⚠️【スペシャリスト】第4層の解放にはLv5以上が必要です。")
            if s4 == "武装偵察兵": mod_mp += 10; noc_sys_texts.append(f"【4層: {s4}】索敵1回振り直し可 / スカウト70で対人ダメ+25%")
            elif s4 == "単座式装甲歩行機": noc_sys_texts.append(f"【4層: {s4}】技能『操縦〈AW〉』解禁(初期10) / AWグラディエーター型入手")
            elif s4 == "狙撃手": noc_sys_texts.append(f"【4層: {s4}】技能『狙撃』取得(初弾威力+100%, 射撃後1T被ダメ+50%)")
            elif s4 == "行進射撃": noc_sys_texts.append(f"【4層: {s4}】戦技『行進射撃』(2T機関銃立射命中減少半減, 弾数固定, 威力+20%, 被ダメ+30%)")
            elif s4 == "特殊工作兵Lv2": noc_sys_texts.append(f"【4層: {s4}】(※1層上書)対人ダメ+20%, 被ダメ-10%, 対兵器ダメ+20%(重兵器時)")
            elif s4 == "潜入兵Lv2": noc_sys_texts.append(f"【4層: {s4}】(※1層上書)サプレッサー威力+30% / 回避+7")
            elif s4 == "空挺兵Lv2": noc_sys_texts.append(f"【4層: {s4}】(※1層上書)落下ダメ-60%, 装備弾倉数+3, 回避+5, 被ダメ-20%")
            elif s4 == "コンドッティエーレ": mod_hp += 10; mod_mp += 10; noc_sys_texts.append(f"【4層: {s4}】(※3層上書)与ダメージ+20% / 被ダメージ-10%")
            elif s4 == "ハイランダー": mod_hp -= 30; noc_sys_texts.append(f"【4層: {s4}】近接武器ダメ+40%, 銃撃ダメ+20%, 被ダメ+40%")
            elif s4 == "コンキスタドール": mod_hp += 5; mod_mp -= 30; noc_sys_texts.append(f"【4層: {s4}】索敵+5(突破) / 回避+5 / 被ダメ-10% / 銃撃ダメ+20%")
            elif s4 == "グラディエーター": noc_sys_texts.append(f"【4層: {s4}】近接連撃回数+1 / 近接武器ダメージ+10%")
            elif s4 == "ティーガー": mod_hp += 10; mod_mp += 10; mod_stamina += 2; noc_sys_texts.append(f"【4層: {s4}】重機関銃装備可 / 被ダメージ-10% / 回避-20")
            elif s4 == "アルチザン": noc_sys_texts.append(f"【4層: {s4}】アイテム製作技能値+5(突破) / 製作アイテム耐久値+10%")
            elif s4 == "ローリエット": noc_sys_texts.append(f"【4層: {s4}】上級芸術技能解禁 / 1つ初期値35で取得可(要:通常芸術70)")
            elif s4 == "プロフェッサー": mod_mp += 10; bonus_mental += 10; noc_sys_texts.append(f"【4層: {s4}】70以上の高等技能値+5(突破)")
            elif s4 == "ノワール・リミエ": bonus_mental += 15; noc_sys_texts.append(f"【4層: {s4}】白兵+20%, 射撃+10%, 防護点+1 / 先手時1T目ダメ補正+2(1発毎)")
            elif s4 == "エセクトーレ": mod_hp += 5; mod_mp += 5; noc_sys_texts.append(f"【4層: {s4}】名声-5以降-1毎に白兵威力+5%(最大25%) / 白兵ダメの5%HP吸収")
            elif s4 == "アウフゼーア": mod_mp += 10; noc_sys_texts.append(f"【4層: {s4}】敵回避基準+5常時 / 命中時敵分析進行(毎T被ダメ-5%, 最大-20%)")
            
        
    # ==========================================
    # 製作系ジョブの処理（必ず最終計算より上に置く！）
    # ==========================================
    # 1. 画面の入力内容を拾い上げて、採取人と職人のLvを自動判定する
    g_lv = 0
    c_lv = 0
    
    c1_1 = p.get('job_craft1_1', '(なし)')
    c1_1_lv = int(p.get('job_craft1_1_lv', '0'))
    c1_2 = p.get('job_craft1_2', '(なし)')
    c1_2_lv = int(p.get('job_craft1_2_lv', '0'))
    
    # 枠1で何が選ばれたかチェック
    if "採取人" in c1_1: g_lv = max(g_lv, c1_1_lv)
    elif "職人" in c1_1: c_lv = max(c_lv, c1_1_lv)
    
    # 枠2で何が選ばれたかチェック
    if "採取人" in c1_2: g_lv = max(g_lv, c1_2_lv)
    elif "職人" in c1_2: c_lv = max(c_lv, c1_2_lv)

    job_craft2 = p.get('job_craft2', '(なし)')
    job_craft2_lv = p.get('job_craft2_lv', '0')

    # 1. 採取人
    if g_lv == 1:
        job_texts.append("採取人Lv1: 採取等判定時、敏捷/筋力+5(技能上限+2)")
    elif g_lv == 2:
        job_texts.append("採取人Lv2: 採取等判定時、敏捷/筋力+5 / 道具耐久+2 / 1日1回幸運成功で獲得物+1")
    elif g_lv == 3:
        job_texts.append("採取人Lv3: 採取等判定時、敏捷/筋力+10(技能上限+5) / 道具耐久合計+3 / 1日1回幸運で獲得物+1")

    # 2. 職人
    if c_lv == 1:
        job_texts.append("職人Lv1: 修理クリティカル時、修理回数消費なし")
    elif c_lv == 2:
        job_texts.append("職人Lv2: 1日1回設計/制作ダイスを幸運ロールで振り直し可 / 修理クリティカル消費なし")
    elif c_lv == 3:
        job_texts.append("職人Lv3: 1日1回制作技能失敗時に振り直し可(ファンブル不可) / 修理クリティカル消費なし")

    # 3. 匠
    if job_craft2 == "匠〈マイスター〉":
        if lvl_num < 4: warning_errors.append("⚠️【匠エラー】二次職「匠」はLv4以上から選択可能です。")
        if g_lv < 3 or c_lv < 3: warning_errors.append("⚠️【匠条件未達】職人Lv3および採取人Lv3の両方が必要です。")
        
        # ★ここでスタミナを確実に+1する！
        mod_stamina += 1 
        
        job_texts.append("匠Lv0: 疲れ知らず【修理回数+2 / スタミナ+1】")
        if job_craft2_lv >= "1": job_texts.append("匠Lv1: 効率修理強化【クリティカル時回復値+1】")
        if job_craft2_lv >= "2": job_texts.append("匠Lv2: 熟練採取強化【1日2回幸運成功で獲得物+1】")
        if job_craft2_lv >= "3": job_texts.append("匠Lv3: 最短採取【採取スタミナ消費半減】")
        if job_craft2_lv >= "4": job_texts.append("匠Lv4: 名工【補正半減 / 1日1回ロスト防止】")
    
    # --- サブステータス処理 ---
    sub_keys = ["膂力", "叡智", "体力", "持久力", "技量", "神聖", "商売", "表現力", "探求心"]
    sub_stats = {k: p.get(f'sub_{k}', 0) for k in sub_keys}
    for k in list(sub_stats.keys()):
        if sub_stats[k] > 20:
            warning_errors.append(f"⚠️【サブステ】{k}は最大20までです(現在{sub_stats[k]})。20に修正しました。")
            sub_stats[k] = 20
    base_combat_val = sum([stats[k] for k in ["筋力", "知力", "敏捷", "精神", "体格", "生命", "容姿"]])
    max_sub_sp = base_combat_val // 10
    spent_sub_sp = sum(sub_stats.values())
    sub_sp_text = f"サブステP消費: {spent_sub_sp} / {max_sub_sp}"
    if spent_sub_sp > max_sub_sp:
        warning_errors.append(f"⚠️【サブステP超過】割り振り({spent_sub_sp})が上限({max_sub_sp})を超えています。")
    sub_melee_ab_bonus = min(5, int(sub_stats.get('膂力', 0) * 0.25))
    sub_str_mod = int(sub_stats.get('膂力', 0) * 0.5)
    sub_magic_ab_bonus = min(5, int(sub_stats.get('叡智', 0) * 0.25))
    sub_int_mod = int(sub_stats.get('叡智', 0) * 0.5)
    sub_hp_bonus = min(10, int(sub_stats.get('体力', 0) * 0.5))
    mod_hp += sub_hp_bonus
    sub_stamina_bonus = min(5, int(sub_stats.get('持久力', 0) * 0.25))
    mod_stamina += sub_stamina_bonus
    sub_skill_mod = min(5, int(sub_stats.get('技量', 0) * 0.25))
    sub_eva_mod = min(5, int(sub_stats.get('技量', 0) * 0.25))
    sub_holy_mod = min(100, int(sub_stats.get('神聖', 0) * 5))
    sub_biz_mod = min(10, int(sub_stats.get('商売', 0) * 0.5))
    sub_art_mod = min(10, int(sub_stats.get('表現力', 0) * 0.5))
    sub_exp_mod = int(sub_stats.get('探求心', 0) * 0.5)
    bonus_ab_melee += sub_melee_ab_bonus
    bonus_ab_magic += sub_magic_ab_bonus
    sub_texts = []
    if sub_stats.get('膂力', 0) > 0: sub_texts.append(f"・膂力: 白兵AB+{sub_melee_ab_bonus} / 筋力判定基準値-{sub_str_mod}")
    if sub_stats.get('叡智', 0) > 0: sub_texts.append(f"・叡智: 知力AB+{sub_magic_ab_bonus} / 知力判定基準値-{sub_int_mod}")
    if sub_stats.get('体力', 0) > 0: sub_texts.append(f"・体力: HP+{sub_hp_bonus}")
    if sub_stats.get('持久力', 0) > 0: sub_texts.append(f"・持久力: スタミナ+{sub_stamina_bonus}")
    if sub_stats.get('技量', 0) > 0: sub_texts.append(f"・技量: 技能ロール+{sub_skill_mod} / 回避+{sub_eva_mod}(上限50)")
    if sub_stats.get('神聖', 0) > 0: sub_texts.append(f"・神聖: 信仰系攻撃威力+{sub_holy_mod}%")
    if sub_stats.get('商売', 0) > 0: sub_texts.append(f"・商売: 商才ロール補正+{sub_biz_mod}")
    if sub_stats.get('表現力', 0) > 0: sub_texts.append(f"・表現力: 芸術力ロール補正+{sub_art_mod}")
    if sub_stats.get('探求心', 0) > 0: sub_texts.append(f"・探求心: 探索系基準値-{sub_exp_mod}")
    combat_sub_names = ["膂力", "叡智", "体力", "持久力", "技量"]
    sub_to_main_combat = {"膂力": "筋力", "叡智": "知力", "体力": "生命", "持久力": "体格", "技量": "敏捷"}
    combat_subs = {k: sub_stats.get(k, 0) for k in combat_sub_names}
    sorted_csubs = sorted(combat_subs.values(), reverse=True)
    v1, v2, v3 = sorted_csubs[0], sorted_csubs[1], sorted_csubs[2]
    if (v1 - v2 >= 10) or (v1 - v3 >= 10) or (v2 - v3 >= 10):
        max_val = v1
        for sub_k, sub_v in combat_subs.items():
            diff = max_val - sub_v
            if diff >= 10:
                penalty = 0
                if 10 <= diff <= 11: penalty = 10
                elif 12 <= diff <= 13: penalty = 15
                elif 14 <= diff <= 15: penalty = 20
                elif 16 <= diff <= 17: penalty = 25
                elif 18 <= diff <= 19: penalty = 30
                elif diff >= 20: penalty = 35
                linked_main = sub_to_main_combat[sub_k]
                stats[linked_main] -= penalty
                warning_errors.append(f"⚠️【サブ格差ペナルティ】{sub_k}の格差(差{diff})により、{linked_main}が -{penalty}")

    # --- 個別最大値チェック ---
    over_limit_stats = []
    for k in base_stats_names:
        limit = 70
        if race == "ヴァンパイア" and origin == "ファンタジア": limit = 80
        elif race == "人狼" and k in ["筋力", "敏捷"]: limit = 85
        elif race == "兎人族" and k == "敏捷": limit = 80
        elif race == "鬼人族" and k in ["筋力", "生命"]: limit = 80
        elif race == "炉心異常体" and k == "筋力": limit = 80
        elif race == "スチームブッチャー" and k == "筋力": limit = 80
        if bg == "淑女" and gender == "女" and k == "容姿": limit += 6
        if stats[k] > limit:
            over_limit_stats.append(f"{k} (素ステ{stats[k]} → {limit})")
            stats[k] = limit
    if blessing == "水輝神の加護": stats["商才"] += 5

    # --- 最終計算 ---
    final_hp = (stats["生命"] + stats["体格"]) // 5 + mod_hp
    final_mp = (stats["知力"] + stats["精神"]) // 5 + mod_mp
    if is_atoning_blood:
        final_hp = int(final_hp * 0.8)
        final_mp = int(final_mp * 0.8)
    if race == "強化演算体": final_hp = int(final_hp * 0.7)
    shield_hp_str = f" (＋庇護HP: {int(final_hp * 0.3)})" if blessing == "雪神の加護" else ""
    final_stamina = (stats["敏捷"] + stats["生命"]) // 10 + mod_stamina
    if blessing in ["地影神の加護", "風影神の加護"]: final_stamina = max(1, final_stamina - 3)
    if race == "炉心異常体": final_stamina //= 2
    luck = min(50, (sum([stats["筋力"], stats["知力"], stats["敏捷"], stats["精神"], stats["体格"], stats["生命"], stats["容姿"]]) // 10) + mod_luck)
    faint = (stats["生命"] + stats["体格"] + stats["精神"]) // 5
    depend = (stats["精神"] + stats["知力"]) // 10
    base_sp = sum([stats["筋力"], stats["知力"], stats["敏捷"], stats["精神"], stats["体格"], stats["生命"], stats["容姿"], stats["芸術"], stats["商才"]])
    final_mental = stats['精神']
    if race in ["強化演算体"]: final_mental -= 10
    elif race in ["怪異憑依者／怪人", "アンドロイド"]:
        final_mental += 5 if race == "怪異憑依者／怪人" else (15 if lineage == 100 else (10 if lineage >= 71 else 5))
    if bg == "叫喚者": final_mental -= 10
    final_mental += bonus_mental
    if bg == "囚憶者":
        lost_mental = final_mental // 2
        final_mental -= lost_mental
        bonus_sp += lost_mental * 7
    sp_status_text = f"{spent_sp} / {max_sp}"
    if spent_sp > max_sp: sp_status_text += " ⚠️【最大SP超過】"
    warning_text = ""
    if over_limit_stats: warning_text += f"\n⚠️【上限自動補正】：{', '.join(over_limit_stats)}"
    if warning_errors: warning_text += "\n\n" + "\n".join(warning_errors)
    sub_text = f" ({race_sub})" if race_sub else ""
    bg_sub_text = f" ({bg_sub})" if bg_sub else ""
    blessing_section = f"\n【加護の効果】\n{blessing_text_out}\n" if blessing_text_out else ""
    magic_sp_text = f"\n魔法専用技能P: {magic_sp}" if magic_sp > 0 else ""
    job_info_text = f"一次職1: {job1_1} Lv{job1_1_lv}　|　一次職2: {job1_2} Lv{job1_2_lv}\n二次職: {job2} Lv{job2_lv}"
    if job_texts: job_info_text += f"\n(適用パッシブ: {', '.join(job_texts)})"
    final_ab_melee = (stats['筋力'] // 10) + bonus_ab_melee
    final_ab_magic = (stats['知力'] // 10) + bonus_ab_magic
    ab_melee_str = f"{final_ab_melee}" if bonus_ab_melee == 0 else f"{final_ab_melee} (ボーナス+{bonus_ab_melee}込み)"
    ab_magic_str = f"{final_ab_magic}" if bonus_ab_magic == 0 else f"{final_ab_magic} (ボーナス+{bonus_ab_magic}込み)"
    ab_magic_str += ab_magic_extra
    sub_section = ""
    if sub_texts: sub_section = f"\n【サブステータス効果】 ({sub_sp_text})\n" + "\n".join(sub_texts) + "\n"
    fan_sys_section = ""
    if fan_sys_texts: fan_sys_section = f"\n【ファンタジア限定システム効果】\n" + "\n".join(fan_sys_texts) + "\n"
    noc_sys_section = ""
    if noc_sys_texts: noc_sys_section = f"\n【ノクターン限定システム効果 (スペシャリスト)】\n" + "\n".join(noc_sys_texts) + "\n"

    result_text = f"""【プロフィール】
星: {origin}　|　種族: {race}{sub_text}
属性: {attr_text}　|　家柄: {lineage}
出自: {bg}{bg_sub_text}　|　加護: {blessing}

【ジョブ】
{job_info_text}

【SP状況】
SP消費量: {sp_status_text}

【最終基礎ステータス（補正・SP込み）】{warning_text}
筋力: {stats['筋力']}
知力: {stats['知力']}
敏捷: {stats['敏捷']}
精神: {stats['精神']}
体格: {stats['体格']}
生命: {stats['生命']}
容姿: {stats['容姿']}
芸術: {stats['芸術']}
商才: {stats['商才']}
信仰: {stats['信仰']}

【戦闘・派生ステータス】
HP: {final_hp}{shield_hp_str}
MP: {final_mp}
スタミナ: {final_stamina}

気絶点: {faint}
依存点: {depend}
幸運: {luck} (最大50)
精神限界: {final_mental}
魅力: {stats['容姿']}
知識: {stats['知力']}

基礎技能P合計: {base_sp + bonus_sp} (基本:{base_sp} ＋ ボーナス:{bonus_sp}){magic_sp_text}

【AB】
白兵AB: {ab_melee_str}
知力AB: {ab_magic_str}
{fan_sys_section}{noc_sys_section}{sub_section}{blessing_section}"""
    return result_text


# ===================================================
# 4. Streamlit メインUI
# ===================================================
st.set_page_config(
    page_title="ステラリアクロニクル ステ計ツール",
    layout="wide",
    page_icon="⚔️"
)

st.title("⚔️ ステラリアクロニクル ステ計ツール")

# ---- サイドバー: セーブ/ロード ----
with st.sidebar:
    st.header("💾 セーブ / ロード")

    uploaded = st.file_uploader("JSONファイルを読み込む", type=["json"])
    if uploaded is not None:
        try:
            raw = json.load(uploaded)
            for k, v in raw.items():
                st.session_state[k] = v
            st.success("✅ 読み込み完了！")
            st.rerun()
        except Exception as e:
            st.error(f"読み込みエラー: {e}")

    st.markdown("---")
    st.caption("計算後、ステータス統計の下のボタンでデータをJSON保存できます。")

# ---- 3カラムレイアウト ----
col_left, col_center, col_right = st.columns([1.2, 1.1, 1.7])

# ===================================================
# 左カラム: プロフィール選択
# ===================================================
with col_left:
    st.markdown("### 📋 プロフィール選択")

    origin = st.selectbox("出身星", list_origin, index=si('origin', list_origin), key='origin')

    c1, c2 = st.columns(2)
    with c1: level = st.selectbox("レベル", list_level, index=si('level', list_level), key='level')
    with c2: age = st.selectbox("年代", list_age, index=si('age', list_age), key='age')

    c3, c4 = st.columns(2)
    with c3: gender = st.selectbox("性別", list_gender, index=si('gender', list_gender), key='gender')
    with c4: ethnicity = st.selectbox("人種", list_ethnicity, index=si('ethnicity', list_ethnicity), key='ethnicity')

    # 種族（出身星で切り替え）
    race_list = list_race_fantasia if origin == "ファンタジア" else list_race_nocturne
    race = st.selectbox("種族", race_list, index=si('race', race_list), key='race')

    # 種族派生
    race_sub_map = {
        "巨人族": ["山の一族", "霧の一族"],
        "猫人族": ["ベスティアケット", "アニマケット"],
        "妖怪": ["百鬼妖怪", "流浪妖怪"],
        "甲虫人": ["全甲種", "亜甲種"],
        "幻影体発現者": ["エレメンツ", "エンチャント"],
        "羅刹": ["悪夢(15点)", "悲痛(20点)", "狂乱(25点)", "血涙(30点)", "慟哭(36点)"],
        "怪異憑依者／怪人": ["羽虫(Lv1)", "蠕虫(Lv1)", "毒虫(Lv2)", "蛾(Lv2)", "鼬(Lv2)", "黒蝶(Lv3)", "細蠍(Lv3)", "貂(Lv3)"]
    }
    race_sub = ""
    if race in race_sub_map:
        sub_opts = race_sub_map[race]
        race_sub = st.selectbox("└ 種族派生", sub_opts, index=si('race_sub', sub_opts), key='race_sub')

    # 加護（ファンタジアのみ）
    blessing = "(なし)"
    if origin == "ファンタジア":
        blessing = st.selectbox("加護/血契", list_blessing, index=si('blessing', list_blessing), key='blessing')

    st.markdown("**過去**")
    c5, c6, c7 = st.columns(3)
    with c5: past0 = st.selectbox("0章", list_past0, index=si('past0', list_past0), key='past0')
    with c6: past1 = st.selectbox("1章", list_past1, index=si('past1', list_past1), key='past1')
    with c7: past2 = st.selectbox("2章", list_past2, index=si('past2', list_past2), key='past2')

    # 出自（出身星で切り替え）
    bg_list = list_bg_fantasia if origin == "ファンタジア" else list_bg_nocturne
    bg = st.selectbox("出自", bg_list, index=si('bg', bg_list), key='bg')

    # 出自派生
    bg_sub_map = {}
    if origin == "ノクターン":
        bg_sub_map = {"使用人": ["使用人", "戦闘使用人"], "軍人": ["下士官", "パイロット"],
                      "警官": ["警官", "汚職警官"], "無法者": ["ギャング", "マフィア"]}
    else:
        bg_sub_map = {"蛮族": ["極北の蛮族", "漂海の蛮族"], "贖血徒": ["贖血の叫び", "贖血の呟き"]}
    bg_sub = ""
    if bg in bg_sub_map:
        bg_sub_opts = bg_sub_map[bg]
        bg_sub = st.selectbox("└ 出自派生", bg_sub_opts, index=si('bg_sub', bg_sub_opts), key='bg_sub')

    # 属性
    attr = st.selectbox("属性", list_attr, index=si('attr', list_attr), key='attr')
    attr1, attr2 = list_attr_sub[0], list_attr_sub[1]
    if attr == "双属性":
        ca1, ca2 = st.columns(2)
        with ca1: attr1 = st.selectbox("└ 属性1", list_attr_sub, index=si('attr1', list_attr_sub, 0), key='attr1')
        with ca2: attr2 = st.selectbox("└ 属性2", list_attr_sub, index=si('attr2', list_attr_sub, 1), key='attr2')

    lineage = st.number_input("家柄（基本値）", min_value=0, max_value=100,
                              value=get_int(st.session_state.get('lineage', 0)), step=1, key='lineage')

    st.markdown("---")
    st.markdown("### ⚔️ ジョブ")
    job1_list = list_job1 if origin == "ファンタジア" else list_job_noc1
    job2_list = list_job2 if origin == "ファンタジア" else list_job_noc2

    j1a, j1b = st.columns([3, 1])
    with j1a: job1_1 = st.selectbox("一次職1", job1_list, index=si('job1_1', job1_list), key='job1_1')
    with j1b: job1_1_lv = st.selectbox("Lv", list_job_lv, index=si('job1_1_lv', list_job_lv), key='job1_1_lv', label_visibility="visible")

    j2a, j2b = st.columns([3, 1])
    with j2a: job1_2 = st.selectbox("一次職2", job1_list, index=si('job1_2', job1_list), key='job1_2')
    with j2b: job1_2_lv = st.selectbox("Lv ", list_job_lv, index=si('job1_2_lv', list_job_lv), key='job1_2_lv')

    j3a, j3b = st.columns([3, 1])
    with j3a: job2 = st.selectbox("二次職", job2_list, index=si('job2', job2_list), key='job2')
    with j3b: job2_lv = st.selectbox("Lv  ", list_job2_lv, index=si('job2_lv', list_job2_lv), key='job2_lv')

    st.markdown("---")
    st.markdown("### 🛠️ 製作・専門ジョブ（併任可能）")

    list_craft_job = ["(なし)", "採取人〈ギャザラー〉", "職人〈クラフトマン〉"]

    # 製作系一次職1
    jc1a, jc1b = st.columns([3, 1])
    with jc1a: 
        st.selectbox("製作系一次職1", list_craft_job, index=si('job_craft1_1', list_craft_job), key='job_craft1_1')
    with jc1b: 
        st.selectbox("Lv", ["0", "1", "2", "3"], index=si('job_craft1_1_lv', ["0", "1", "2", "3"]), key='job_craft1_1_lv')

    # 製作系一次職2
    jc2a, jc2b = st.columns([3, 1])
    with jc2a: 
        st.selectbox("製作系一次職2", list_craft_job, index=si('job_craft1_2', list_craft_job), key='job_craft1_2')
    with jc2b: 
        st.selectbox("Lv ", ["0", "1", "2", "3"], index=si('job_craft1_2_lv', ["0", "1", "2", "3"]), key='job_craft1_2_lv')

    # 製作系二次職「匠」
    list_craft_job2 = ["(なし)", "匠〈マイスター〉"]
    jc3a, jc3b = st.columns([3, 1])
    with jc3a: 
        st.selectbox("製作系二次職", list_craft_job2, index=si('job_craft2', list_craft_job2), key='job_craft2')
    with jc3b: 
        st.selectbox("Lv  ", ["0", "1", "2", "3", "4"], index=si('job_craft2_lv', ["0", "1", "2", "3", "4"]), key='job_craft2_lv')
        
    st.markdown("---")
    st.markdown("### 🎯 アビリティ")
    skill = st.selectbox("技量", list_skill, index=si('skill', list_skill), key='skill')
    martial = st.selectbox("武芸", list_martial, index=si('martial', list_martial), key='martial')
    craft = st.selectbox("工芸", list_craft, index=si('craft', list_craft), key='craft')

    # ファンタジア限定
    stance = "(なし)"; stance_lv = "0"; school = "(なし)"
    if origin == "ファンタジア":
        st.markdown("---")
        st.markdown("### 🌸 ファンタジア限定")
        fs1, fs2 = st.columns([3, 1])
        with fs1: stance = st.selectbox("刀術の構え", list_stance, index=si('stance', list_stance), key='stance')
        with fs2: stance_lv = st.selectbox("Lv   ", ["0","1","2","3"], index=si('stance_lv', ["0","1","2","3"]), key='stance_lv')
        school = st.selectbox("魔導流派", list_school, index=si('school', list_school), key='school')

    # ノクターン限定
    spec_route = "(なし)"; spec_1 = spec_2 = spec_3 = spec_4 = "(なし)"
    if origin == "ノクターン":
        st.markdown("---")
        st.markdown("### 🔮 ノクターン限定（スペシャリスト）")
        spec_route = st.selectbox("ルート", list_spec_route, index=si('spec_route', list_spec_route), key='spec_route')
        spec_lists = dict_spec.get(spec_route, [["(なし)"], ["(なし)"], ["(なし)"], ["(なし)"]])
        spec_1 = st.selectbox("└ 1層 (Lv2)", spec_lists[0], index=si('spec_1', spec_lists[0]), key='spec_1')
        spec_2 = st.selectbox("└ 2層 (Lv3)", spec_lists[1], index=si('spec_2', spec_lists[1]), key='spec_2')
        spec_3 = st.selectbox("└ 3層 (Lv4)", spec_lists[2], index=si('spec_3', spec_lists[2]), key='spec_3')
        spec_4 = st.selectbox("└ 4層 (Lv5)", spec_lists[3], index=si('spec_4', spec_lists[3]), key='spec_4')

# ===================================================
# 中央カラム: ステータス入力
# ===================================================
with col_center:
    st.markdown("### 📊 基礎ステータス入力")

    hc1, hc2, hc3 = st.columns([1.5, 1, 1])
    hc1.markdown("**ステータス**")
    hc2.markdown("**基本値**")
    hc3.markdown("**SP振分**")

    stats_base = {}
    stats_sp = {}
    for stat in base_stats_names:
        sc1, sc2, sc3 = st.columns([1.5, 1, 1])
        sc1.write(stat)
        stats_base[stat] = sc2.number_input(
            f"base_{stat}", min_value=0, max_value=200,
            value=get_int(st.session_state.get(f'base_{stat}', 0)),
            step=1, key=f'base_{stat}', label_visibility="collapsed"
        )
        stats_sp[stat] = sc3.number_input(
            f"sp_{stat}", min_value=0, max_value=50,
            value=get_int(st.session_state.get(f'sp_{stat}', 0)),
            step=1, key=f'sp_{stat}', label_visibility="collapsed"
        )

    st.markdown("---")
    st.markdown("**⚙️ 特殊調整（凡庸・平凡用）**")
    combo_plus = []
    combo_minus = []
    for i in range(3):
        cp_key = f'combo_plus_{i}'
        cm_key = f'combo_minus_{i}'
        pp, pm = st.columns(2)
        with pp:
            val = st.selectbox(f"上昇{i+1}", list_stats,
                               index=si(cp_key, list_stats),
                               key=cp_key)
            combo_plus.append(val)
        with pm:
            val = st.selectbox(f"下降{i+1}", list_stats,
                               index=si(cm_key, list_stats),
                               key=cm_key)
            combo_minus.append(val)

    st.markdown("---")
    st.markdown("**🔷 サブステータス (0〜20)**")
    sub_stats = {}
    for i in range(0, len(list_sub_stats), 3):
        cols = st.columns(3)
        for j, sub in enumerate(list_sub_stats[i:i+3]):
            sk = f'sub_{sub}'
            with cols[j]:
                sub_stats[sub] = st.number_input(
                    sub, min_value=0, max_value=20,
                    value=get_int(st.session_state.get(sk, 0)),
                    step=1, key=sk
                )

    st.markdown("---")
    calc_btn = st.button("🎲 ステータスを計算する", use_container_width=True, type="primary")

# ===================================================
# 右カラム: 計算結果
# ===================================================
with col_right:
    st.markdown("### 📜 計算結果シート")

    if calc_btn:
        params = {
            'origin': origin, 'level': level, 'age': age,
            'gender': gender, 'ethnicity': ethnicity,
            'race': race, 'race_sub': race_sub,
            'blessing': blessing,
            'past0': past0, 'past1': past1, 'past2': past2,
            'bg': bg, 'bg_sub': bg_sub,
            'attr': attr, 'attr1': attr1, 'attr2': attr2,
            'lineage': lineage,
            'job1_1': job1_1, 'job1_1_lv': job1_1_lv,
            'job1_2': job1_2, 'job1_2_lv': job1_2_lv,
            'job2': job2, 'job2_lv': job2_lv,
            'skill': skill, 'martial': martial, 'craft': craft,
            'stance': stance, 'stance_lv': stance_lv, 'school': school,
            'spec_route': spec_route,
            'spec_1': spec_1, 'spec_2': spec_2,
            'spec_3': spec_3, 'spec_4': spec_4,
            'stats_base': stats_base, 'stats_sp': stats_sp,
            'combo_plus': combo_plus, 'combo_minus': combo_minus,
            'sub_stats': sub_stats,
        }
        result = calculate()
        st.session_state['last_result'] = result
        st.session_state['last_params'] = params

    if 'last_result' in st.session_state:
        st.code(st.session_state['last_result'], language=None)

        # セーブボタン（計算後に表示）
        st.markdown("---")
        save_data = {}
        simple_keys = ['origin', 'level', 'age', 'gender', 'ethnicity', 'race', 'race_sub',
                       'blessing', 'past0', 'past1', 'past2', 'bg', 'bg_sub',
                       'attr', 'attr1', 'attr2', 'lineage',
                       'job1_1', 'job1_1_lv', 'job1_2', 'job1_2_lv','job_craft2', 'job_craft2_lv'
                       'job2', 'job2_lv', 'skill', 'martial', 'craft',
                       'stance', 'stance_lv', 'school',
                       'spec_route', 'spec_1', 'spec_2', 'spec_3', 'spec_4']
        for k in simple_keys:
            if k in st.session_state:
                save_data[k] = st.session_state[k]
        for stat in base_stats_names:
            save_data[f'base_{stat}'] = st.session_state.get(f'base_{stat}', 0)
            save_data[f'sp_{stat}'] = st.session_state.get(f'sp_{stat}', 0)
        for i in range(3):
            save_data[f'combo_plus_{i}'] = st.session_state.get(f'combo_plus_{i}', '(なし)')
            save_data[f'combo_minus_{i}'] = st.session_state.get(f'combo_minus_{i}', '(なし)')
        for sub in list_sub_stats:
            save_data[f'sub_{sub}'] = st.session_state.get(f'sub_{sub}', 0)

        json_str = json.dumps(save_data, ensure_ascii=False, indent=2)
        st.download_button(
            label="💾 JSONでセーブ（ダウンロード）",
            data=json_str,
            file_name="character.json",
            mime="application/json",
            use_container_width=True
        )
    else:
        st.info("左・中央のフォームを入力して「ステータスを計算する」を押してください。")
