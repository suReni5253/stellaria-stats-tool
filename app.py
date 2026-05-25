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
    "人間族", "獣人族", "翼人族", "鬼人族", "兎人族", "呪い人", "マーメイド",
    "ドラシオン", "巨人族", "猫人族", "妖怪", "妖狐", "ドリュアス",
    "不死者", "甲虫人", "半獣人", "天狗", "鬼半妖",
    "蹄人族", "マリオネット"
]
list_race_fantasia = list_race_common + [
    "ハイエルフ", "ハーフエルフ", "ダークエルフ", "ドワーフ", "ウッドエルフ",
    "フェルダー", "ヴァンパイア", "人狼", "デュラハン", "ダンピール",
    "レウィス・ゴーレム", "ゴブリン", "ハーフドラゴン", "スノウエルフ", "妖精族",
    "ホムンクルス", "ダークドワーフ", "蛇人", "幻蛛族", "失耀天使", "コブラナイ",
    "フレイムエルフ", "ウーンゲフォイヤー", "ヴァンシー", "クラーケンF","マンティコアF", "メルフェディオヌF, ローレライ"
]
list_race_nocturne = list_race_common + [
    "炉心異常体", "魔眼発現体", "演算異常体", "強化演算体", "サイボーグ",
    "アンドロイド", "クローン《デザイナーベビー》", "幻影体発現者", "ヴィロン",
    "ノクト・ヴァンパイア", "ノクス・エルフ", "ノクス・ハーフエルフ",
    "ホットロード・サイボーグ", "意識人造体（イニシエーター）", "人工獣人",
    "強化人兵", "羅刹", "オートマタ", "アルラウネ", "デトネーター",
    "スチームブッチャー", "怪異憑依者／怪人", "クラーケンN", "マンティコアN", "メルフェディオヌN, セイレーン"
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
demon_races = ["鬼人族", "ヴァンパイア", "人狼", "デュラハン", "マンティコアF","マンティコアN", "クラーケンF", "クラーケンN", "ウーンゲフォイヤー", "メルフェディオヌ", "ノクト・ヴァンパイア"]
cursed_races = ["呪い人", "羅刹", "アルラウネ", "スチームブッチャー", "怪異憑依者／怪人", "ゴブリン", "妖怪", "妖狐", "不死者", "天狗", "鬼半妖","マリオネット","ホムンクルス","失耀天使"]

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
    mod_evasion = 0       # 👈 追加: 通常の回避補正（上限50）
    eva_limit_break = 0
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
    is_atoning_blood = False
    magic_sp_text = ""
    extra_buff_section = ""
    
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
    attr_sys_texts = []
    
    for a in current_attrs:
        if a == "炎属性":
            attr_sys_texts.append("【炎属性】《燃焼》炎・水・夜光属性以外の敵に対して攻撃威力+10%(無属性にも有効)")
        elif a == "風属性":
            attr_sys_texts.append("【風属性】《拡散》風属性攻撃時、与ダメの20%を追加ダメージとして与える(風魔法扱い)\n《飄風》常時回避+5")
            mod_evasion += 5
        elif a == "地属性":
            attr_sys_texts.append("【地属性】《堅牢》自身の防護点を+20%する\n《地母神の加護》HP+2")
            mod_hp += 2
        elif a == "氷属性":
            attr_sys_texts.append("【氷属性】《凍傷》氷・夜光以外の敵に氷攻撃時、凍傷ゲージ+1d10(最大10で次ターン氷ダメ2倍/CT3T)")
        elif a == "水属性":
            attr_sys_texts.append("【水属性】《湿潤》水回復で火属性持続ダメ解除 / 水攻撃で敵を1T湿潤化(雷ダメ1.5倍化)\n《水明》回復魔法の消費MP-5 / 状態異常：火傷を無効化")
        elif a == "雷属性":
            attr_sys_texts.append("【雷属性】《感電》雷・夜光以外の敵からの回避+5 / 湿潤状態の敵へのダメージ+50%")
        elif a == "雪属性":
            attr_sys_texts.append("【雪属性】《吹雪》自身の攻撃に対する火・水以外の敵回避を常時-10(下限5)")
        elif a == "花属性":
            attr_sys_texts.append("【花属性】《荊棘毒》湿潤化した敵への花属性攻撃ダメージ1.5倍(ダメ50%は回復不可)\n《華風》HP+5")
            mod_hp += 5
        elif a == "光属性":
            attr_sys_texts.append("【光属性】《神光》無属性以外のダメに対する防護点+2 / 神秘術使用可 / 回復魔法の回復量+10%")
        elif a == "夜属性":
            attr_sys_texts.append("【夜属性】《夜月》回避+2(突破) / ファンタジアでの〈敷波流〉取得時追加SP不要")
            eva_limit_break += 2
    
    # 計算で使いそうな変数をあらかじめ定義
    bonus_ab_melee = 0
    bonus_ab_magic = 0
    bonus_mental = 0
    mod_luck = 0
    
    if origin == "ファンタジア" or (origin == "ノクターン" and (race in list_race_common or race in list_race_nocturne)):
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
                eva_limit_break += 5 if lineage == 100 else (4 if lineage >= 91 else (3 if lineage >= 71 else 2))
                stats["敏捷"] += agi_mer; stats["商才"] += agi_mer
        elif race == "呪い人":
                if lineage >= 10:
                    mod_hp -= 15; mod_mp -= 15; mod_stamina -= 5; bonus_sp += 150
                    add_stats_group(-30)
                else:
                    diff = 11 - lineage
                    mod_hp += diff * 2; mod_mp += diff * 2; mod_stamina += diff * 0.5; bonus_sp += 30 * diff
                    add_stats_group(diff * 2)
        elif race == "マーメイド":
                hp_mp = 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                mod_hp += hp_mp; mod_mp += hp_mp
                mod_stamina += 3 if lineage == 100 else (2 if lineage >= 71 else 1)
                add_stats_group(7 if lineage == 100 else (5 if lineage >= 71 else 3), exclude=["生命", "精神", "容姿"])
                stats["生命"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["精神"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["容姿"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
        elif race == "ドラシオン":
                hp_mp = 35 if lineage == 100 else (30 if lineage >= 71 else 25)
                mod_hp += hp_mp; mod_mp += hp_mp
                mod_stamina += 3 if lineage == 100 else (2 if lineage >= 71 else 1)
                add_stats_group(17 if lineage == 100 else (12 if lineage >= 71 else 7))
                mod_evasion += 2
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
                eva_limit_break += 2
                bonus_sp += 150
                if race_sub == "ベスティアケット": stats["容姿"] -= 5; mod_hp += 7
                elif race_sub == "アニマケット": stats["容姿"] += 2; mod_mp += 2
        elif race == "妖怪":
                mod_hp += 20 if lineage == 100 else (15 if lineage >= 71 else 10) 
                mod_mp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                mod_stamina += 2
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5))
                bonus_sp += 100
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
                    mod_evasion += 3
                    add_stats_group(5, exclude=["筋力", "生命", "敏捷"])
                elif race_sub == "亜甲種":
                    mod_hp += hp_add - 3 
                    stats["筋力"] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                    stats["生命"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                    mod_evasion += 5
                    add_stats_group(11 if lineage == 100 else (8 if lineage >= 71 else 5), exclude=["筋力", "生命"])
        elif race == "半獣人":
                hp_mp = 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_hp += hp_mp; mod_mp += hp_mp
                mod_stamina += 4 if lineage == 100 else (3 if lineage >= 71 else 2)
                stats["筋力"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                add_stats_group(11 if lineage == 100 else (7 if lineage >= 71 else 3), exclude=["筋力"])
                bonus_sp += 250 if lineage == 100 else (200 if lineage >= 71 else 150)
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
                for k in ["知力", "敏捷", "精神", "容姿", "芸術"]: stats[k] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
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
                for k in ["筋力", "精神", "生命", "容姿"]: stats[k] += 10 if lineage == 100 else (7 if lineage >= 71 else 4)
            elif race == "ヴァンパイア":
                hp_mp = 40 if lineage == 100 else (35 if lineage >= 71 else 30)
                mod_hp += hp_mp; mod_mp += hp_mp
                add_all = 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                add_stats_group(add_all, exclude=["容姿"])
                stats["容姿"] += 30 if lineage == 100 else (25 if lineage >= 71 else 20)
                ab_melee_str = "(格闘AB+1D)"
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
                    extra_melee_str = "(白兵AB+1D)"
                elif lineage >= 71:
                    mod_hp += 15; mod_mp += 5; stats["容姿"] -= 15
                    for k in ["筋力", "生命", "敏捷"]: stats[k] += 15
                    add_stats_group(8, exclude=["筋力", "生命", "敏捷", "容姿", "知力"])
                    extra_melee_str = "(白兵AB+1D)"
                else:
                    mod_hp += 10; stats["容姿"] -= 20
                    for k in ["筋力", "生命", "敏捷"]: stats[k] += 10
                    add_stats_group(5, exclude=["筋力", "生命", "敏捷", "容姿", "知力"])
                    extra_melee_str = "(白兵AB+1D)"
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
                for k in ["筋力", "敏捷", "精神", "体格", "生命"]: stats[k] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
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
                mod_hp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                mod_stamina += 5 if lineage == 100 else (3 if lineage >= 71 else 2)
                stats["筋力"] += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                stats["商才"] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                add_stats_group(5 if lineage == 100 else (4 if lineage >= 71 else 3), exclude=["体格", "敏捷", "筋力", "商才"])
            elif race == "フレイムエルフ":
                mod_hp += 20 if lineage == 100 else (14 if lineage >= 71 else 8)
                mod_mp += 25 if lineage == 100 else (20 if lineage >= 71 else 15)
                stats["知力"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["容姿"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                for k in ["筋力", "敏捷", "精神", "体格", "生命"]: stats[k] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                if "炎属性" in current_attrs:
                    mod_mp += 10
                    ab_magic_extra = " (+1D)"
            elif race == "ウーンゲフォイヤー":
                hp_mp = 30 if lineage == 100 else (25 if lineage >= 71 else 20)
                mod_hp += hp_mp; mod_mp += hp_mp
                mod_stamina += 5 if lineage == 100 else (4 if lineage >= 71 else 3)
                mod_evasion += 5
                stats["容姿"] -= 30
                add_stats_group(20 if lineage == 100 else (15 if lineage >= 71 else 10), exclude=["容姿"])
            elif race == "ヴァンシー":
                mod_hp += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_mp += 30 if lineage == 100 else (25 if lineage >= 71 else 20)
                mod_stamina += 1
                stats["容姿"] += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                for k in ["筋力", "知力", "敏捷", "精神", "体格", "生命"]: stats[k] += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
            elif race == "マンティコアF":
                mod_hp += 35 if lineage == 100 else (25 if lineage >= 71 else 15)
                mod_mp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                eva_limit_break += 5
                add_stats_group(15)
            elif race == "クラーケンF":
                mod_hp += 35 if lineage == 100 else (30 if lineage >= 71 else 25)
                mod_mp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_stamina += 5 if lineage == 100 else (4 if lineage >= 71 else 3)
                add_stats_group(20 if lineage == 100 else (15 if lineage >= 71 else 10))
            elif race == "メルフェディオヌF":
                hp_mp = 40 if lineage == 100 else (35 if lineage >= 71 else 30)
                mod_hp += hp_mp; mod_mp += hp_mp
                mod_stamina += 4 if lineage == 100 else (3 if lineage >= 71 else 2)
                mod_evasion += 3
                add_stats_group(20 if lineage == 100 else (15 if lineage >= 71 else 10))
            elif race == "ローレライ":
                mod_hp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_mp += 17 if lineage == 100 else (12 if lineage >= 71 else 7)
                mod_stamina += 3 if lineage == 100 else (2 if lineage >= 71 else 1)
                stats["容姿"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["知力"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["精神"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                add_stats_group(7 if lineage == 100 else (5 if lineage >= 71 else 3), exclude=["容姿", "知力", "精神"])
            
        if race == "フェルダー": stats["体格"] = int(stats["体格"] * 0.7)
        if race == "コブラナイ": stats["体格"] = int(stats["体格"] * 0.7)
        if race == "コブラナイ": stats["敏捷"] = int(stats["敏捷"] * 0.7)
        if race == "ゴブリン":
                if lineage == 100: stats["知力"] = int(stats["知力"] * 0.9)
                elif lineage >= 71: stats["知力"] = int(stats["知力"] * 0.8)
                else: stats["知力"] = int(stats["知力"] * 0.7)
        if race == "フェルダー": mod_hp = int((((stats["生命"] + stats["体格"]) // 5) + mod_hp) * 0.7) - ((stats["生命"] + stats["体格"]) // 5)

        if origin == "ノクターン":
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
                mod_hp += 25; mod_mp += 10; mod_stamina -= 2
                add_stats_group(8, exclude=["筋力"])
                stats["筋力"] += 30
            elif race == "怪異憑依者／怪人":
                val = 15 if lineage == 1 else (13 if lineage == 100 else (8 if lineage >= 71 else 3))
                mod_hp += val; mod_mp += val
                add_stats_group(val)
            elif race == "マンティコアN":
                mod_hp += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_mp += 7 if lineage == 100 else (5 if lineage >= 71 else 2)
                eva_limit_break += 2
                add_stats_group(7)
            elif race == "クラーケンN":
                mod_hp += 17 if lineage == 100 else (15 if lineage >= 71 else 12)
                mod_mp += 7 if lineage == 100 else (5 if lineage >= 71 else 2)
                mod_stamina += 2 if lineage == 100 else (2 if lineage >= 71 else 1)
                add_stats_group(10 if lineage == 100 else (7 if lineage >= 71 else 5))
            elif race == "メルフェディオヌN":
                hp_mp = 20 if lineage == 100 else (17 if lineage >= 71 else 15)
                mod_hp += hp_mp; mod_mp += hp_mp
                mod_stamina += 2 if lineage == 100 else (1 if lineage >= 71 else 1)
                mod_evasion += 1
                add_stats_group(15 if lineage == 100 else (10 if lineage >= 71 else 5))
            elif race == "セイレーン":
                mod_hp += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                mod_mp += 15 if lineage == 100 else (10 if lineage >= 71 else 5)
                mod_stamina += 4 if lineage == 100 else (3 if lineage >= 71 else 2)
                stats["容姿"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["筋力"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                stats["生命"] += 20 if lineage == 100 else (15 if lineage >= 71 else 10)
                add_stats_group(7 if lineage == 100 else (5 if lineage >= 71 else 3), exclude=["容姿", "生命", "筋力"])

# === 🧬 種族スキルの処理 ===
    race_skill_text = ""

    if race == "人間族":
        race_skill_text = "【種族スキル】家柄1〜から運命装備が使用可能/投擲威力+20%/1回の戦闘で一度だけ、あらゆる基準値を１つだけ半減可能(例：基準値20→10)"
    elif race == "獣人族": 
        race_skill_text = """【種族スキル】
            近接威力+10%
            ♢獣化
            【2ターン持続/スタミナ-3/近接威力+20%、HP+10/発動時HP30%回復/被ダメージ-10%減】
            ♢獣王化
            【家柄100の場合、獣化が獣王化に変更/2ターン持続/スタミナ-5/近接威力+30%、HP+15/発動時HP50%回復/被ダメージ20%減】
            ⚠獣化/蛮王化は一回の戦闘につき一度きり"""
    elif race == "翼人族":
        race_skill_text = """【種族スキル】
            特殊技能：飛行が50の達成値で可能（家柄71〜：60/家柄100：70）
            弓技能+10（15/20）/家柄100の場合、血属性被ダメージ-20%
            ◉陸下手
            【飛行系を除く全てのスタミナ消費が3倍になる】"""
    elif race == "鬼人族":
        race_skill_text = """【種族スキル】
            聖水無効
            ◉猛鬼化：《自身の体に血色のオーラを纏い、HP上限を-50%する代わりに1ターンの間敵からの被ダメージ-50%
            /猛鬼化発動中は月の呪いを無効化し、近接攻撃威力+20%
            /発動終了後、3ターンの間クールタイム
            /猛鬼化は受動作での発動不可》

            ◉月の呪い
            └常時被ダメージ+50%

            選択種族スキル
            〈いずれか1つのみ選択できる(途中変更不可)〉
            ①童子舞
            【助動作/2ターン継続/酩酊によるペナルティを無効化/発動時に酩酊点が上限の50%以上まで到達している場合、近接攻撃威力+30%&回避+5(上限突破)/発動後、3ターンのクールタイム】

            ②鬼神舞
            【事前動作/1ターン継続/発動宣言後、次のターンに効果が発揮される/近接攻撃威力+1d5×10%/発動後、3ターンのクールタイム】

            ③冠者舞
            【事前動作/1ターン継続/1d3を行い、1が出ると白兵AB+2D、2が出ると回避+10(上限突破)、3が出ると防護点+10の効果を得る/発動後、3ターンのクールタイム】"""
    elif race == "兎人族":
        race_skill_text = """【種族スキル】
            家柄100は《玉兎》となり、常時被ダメージ-10%
            兎人族のみ俊敏のステータス70制限が80制限に上昇/スタミナを3使用することで大ジャンプ（助動作/使用時は2ターンの間、被ダメージ-10%&近接攻撃威力が俊敏値÷2％上昇/効果ターン終了後1ターンのクールタイム）が可能（技能値70（家柄100で80）
            ♢軽耐久
            【HP上限-30%（例：HP100の場合 0.7倍されて70に低下）】"""
    elif race == "呪い人":
        race_skill_text = """【種族スキル】
            ♢呪いの一撃
            【助動作で発動/発動後2ターンの間、敵に攻撃を一発でも命中させるとHP&MP20%回復（複数回攻撃しても効果重複はしない）/発動ターン終了後、3ターンのクールタイム】"""
    elif race == "マーメイド":
        race_skill_text = """【種族スキル】
            固有歌は《嬉遊曲〈ディヴェルティメント〉》
            特性
            ♢麗しき人魚
            【自ターン終了後にHPとMPを1d5回復/水属性ダメージを受けると、ダメージ加算後にHPとMPを+5追加回復する（ダメージ加算時点で戦闘不能になった場合は発動しない）】"""
    elif race == "セイレーン":
        race_skill_text = """【種族スキル】
            固有歌は《子守歌〈ララバイ〉》
            特性
            ♢妖しき人魚
            【自ターン終了後にHPを1d10回復/水属性ダメージを受けると、ダメージ加算後にHPを+10追加回復する（ダメージ加算時点で戦闘不能になった場合は発動しない）】"""
    elif race == "ローレライ":
        race_skill_text = """【種族スキル】
            固有歌は《夢想曲〈トロイメライ〉》
            特性
            ♢美しき人魚
            【自ターン終了後にMPを1d10回復/水属性ダメージを受けると、ダメージ加算後にMPを+10追加回復する（ダメージ加算時点で戦闘不能になった場合は発動しない）】"""
    elif race == "ドラシオン":
        race_skill_text = """【種族スキル】
            竜神の加護：家柄91以上運命武器使用可能
            ①竜血化
            └事前動作で発動。一時的にドラゴンの力を発揮する。HP+50%回復/攻撃ダメージ1.5倍/物理&魔法ダメージカット率+20%/竜の呪いの一時解除効果（竜血化の発動ターン内のみ）を得る。
            竜血化の発動には〈竜血点〉が必要である。
            これらは1ターン経過する毎に1ずつ溜まっていく。
            消費した竜血点の数値に比例して竜血化になれるターン数は増加（竜血点1ごとの持続ターンは1ターン）
            竜血点上限は家柄1-70で2/家柄71-99で3/家柄100で4である。　また、竜血点は竜血化発動中は加点されない。
            竜血化効果終了後、2ターン行動不能（受動作による防御行動のみ可能）。また、行動不能中に竜血点は増加しない
            〈竜血化は竜血点が2点以上でなければ発動できない〉
            ②竜の呪い（-50%した数値は端数切り捨て）
            └常時敵ダメージ+30%/防具防護点−5（盾除く）/防具防御力-100（物理、魔法問わず/盾除く）/HP-10/MP-10"""
    elif race == "巨人族":
        race_skill_text = """【種族スキル】
            巨人化が可能/回避基準値+10
            覚醒：巨人たちは星ごとで起きた災厄の後、生まれたときから自らの魂や血に制約をかけ人間のような見た目で過ごしている。しかし本人の意志が強く示された場合、短時間であるが、かつての巨人を彷彿とさせる姿（3m程度）に覚醒する事が可能である（永久覚醒は制約によって困難）
            【戦闘中、助動作宣言で発動/覚醒している間はHP+100、防護点+5&防御力+100（人間形態の防具（服、盾含む）は使用不可になり、全ての防御効果が無効化される）、白兵アタックボーナスが+2D（大槌、両手斧以外の武器使用不可）、回避不可、常時命中-10、覚醒中一時的に無属性化、覚醒終了後3ターンのクールタイム、覚醒終了直後は1ターンのあいだ全行動不可&被ダメージ+50%】
            〈覚醒できるターン数：1d2+1ターン〉
            〈覚醒している間の他効果/前衛などを含んだ通常のダメージ増加効果が全て無効化される（巨人時のダメージ増加効果が必要）/覚醒時、筋力と身長を÷4した数値分、威力が%上昇（筋力70で身長70の場合、威力+35%）/攻撃を全体攻撃することが可能（4体まで、ダメージ-50%）/一部の武器以外使用不可〉"""
    elif race == "猫人族":
        race_skill_text = """【種族スキル】
            QP+3
            猫神の加護：技能ポイント+150
            ◉高度な動体視力
            └他種族に比べ優れた動体視力を持つ
            【命中+2（上限突破）】
            ◉高度な身体能力
            └他種族に比べ優れた身体能力を持つ
            【ジャンプ・回避の技能値+2（限界突破）/落下ダメージ-2d（ただし落下ダメージが1d以下にはならない）】
            ◉幸運の猫
            └猫は古くから幸運の象徴だった
            【ファンブル時、一回の戦闘に一度だけ幸運を成功させることでファンブルを無効化する（戦闘はシナリオ中の通常フェーズも含む/採取やアルバイトは戦闘の定義に含まない）】"""
    elif race == "妖怪":
        race_skill_text = """【種族スキル】
            妖怪の伝統：技能ポイント+100/妖力量：4/6/8（戦闘開始時点は0。戦闘中に増やしていく形となる）】
            ◉妖怪
            └おそれを具現した者たちの総称。その力は人知を超える
            【呪族と魔族以外に対するダメージ+20%/被ダメージ+20%】
            ◉妖力
            └妖怪などの邪悪な存在に存在する力。魔力と異なり、人の恐怖や悔恨を食い物にする
            【一回の戦闘で"自分で敵を1体倒す・パーティーの味方が1人倒れる"のいずれかが行われた場合、妖力が+2される（ただし同じ味方がもう一度倒れても妖力は増えない）/1ターンの間、なにも動作を消費せずに待機を行うと、妖力が+1増加する】
            ―――――
            ◉妖技
            └妖怪の持つ特別な技。それぞれ種類があり、特色が存在する。ただし発動には妖力が必要。発動は武器スキルと同じく動作を使用しない
            ―――――
            いずれか1つまで選択可能
            ①魑魅魍魎
            └天道に謀反する存在、それが妖怪である
            【妖力-4/ファンブルを反転して成功にする(確定成功)/クールタイム4ターン】
            ②狐狸妖怪
            └夕焼け時、皆が家に籠もり始めた頃に妖怪は現れる。お天道様の目が無くなり始めれば、俗世の闇から姿を表す
            【妖力-3/与ダメージ+100%/クールタイム3ターン】
            ③蛟竜毒蛇
            └あやかしはえいやこらせと祭囃子を立てながら、夜刻に恐れの種を播く
            【妖力-2/自身のHPを70%回復する/クールタイム4ターン】
            ④異類異形
            └百鬼夜行はおそれを知らず。人々の恐れを吸って進んでいく。しかし百鬼夜行が目的地についたことは過去一度しかない
            【妖力-1/自身のMPを70%回復する/クールタイム2ターン】
            ―――――
            ※種族選択時、百鬼妖怪と流浪妖怪の2つのうち、いずれか1つを選択可能。
            百鬼妖怪を選択すると特性:妖怪の呪族と魔族以外に対するダメージ増加量が+30%に上昇
            流浪妖怪を選択すると、待機時の妖力増加量が+2に上昇する"""
    elif race == "妖狐":
        race_skill_text = """【種族スキル】
            妖狐の呪縛：技能ポイント-50/妖力量：3（戦闘開始時点は0、戦闘中に増やす形となる）】
            ◉妖力
            └妖怪などの邪悪な存在に存在する力。魔力と異なり、人の恐怖や悔恨を食い物にする
            【一回の戦闘で"自分で敵を1体倒す・パーティーの味方が1人倒れる"のいずれかが行われた場合、妖力が+1される（ただし同じ味方がもう一度倒れても妖力は増えない）/1ターンの間、なにも動作を消費せずに待機を行うと、妖力が+1増加する】
            ◉妖術
            └助動作/妖術効果は1ターン発動/発動するとCT3ターン/妖力1消費につき攻撃力+10%
            ◉白面金毛九尾狐
            └事前動作で可能。妖力3と自身のHPを50%(最大値HPのため、例えばHP上限が60で残存HP55未満の場合は戦闘不能になる)消費することで、尻尾を3(家柄71未満)/5(家柄71以上)/9本(家柄100)発現させる。発現させる。尻尾一つに付きそれぞれHPが30%/18%/10%ずつ割り振られており、基礎値5%＋尻尾一本につき攻撃力+5%されていく(最大＋50%)。しかし攻撃を受けるたびにダメージ分に相当した尻尾HPが消耗されていき、それぞれの尻尾HPがゼロになると尻尾は消滅する。最終的に尻尾がすべて破壊されるか、残存している尻尾HP以上のダメージを受けると自身のHPが強制的に0になり、蘇生不可の戦闘不能となる
            (尻尾HPは小数点以下切り捨て)"""
    elif race == "ドリュアス":
        race_skill_text = """【種族スキル】
            QP+1（+2/+3）
            ♢樹人族
            【自身が地属性の場合はHP+5、花属性の場合はHP+10/敵を攻撃したら与えたダメージの5%分を吸収する(例:敵に100ダメージを与えるとHPが5回復する/小数点以下切り捨て、種別は最終ダメージ)】
            ♢受け継がれし智脈
            【レベルが上がるごとに知力が+１、MPが+５されていく】
            ♢草樹の友人
            【自身が地属性か花属性の場合、毎ターン、MP+5&スタミナ+1ずつ自ターン開始時に回復（双属性で効果は重複しない）/武器特性：〈草樹の秘力〉を発動させることができる】"""
    elif race == "不死者":
        race_skill_text = """【種族スキル】
            ♢不死の呪い
            【蘇生費が半額/ケガレが最初から2つ存在/蘇生費を支払うと〈不死の代償〉によってHP上限が-5されていく/不死の代償によってHP上限が20以下になるとケガレが+1され、朽彷者になってロスト（不死の代償以外によるHP上限減少は含まない）】
            ♢刹那の安息
            【特定のアイテムを使用することで不死の代償によるHP上限減少を回復できる/または1日に1回、QPを３消費することでHP上限を+5回復可能】
            ♢運命への道
            【名声を+5以上にすることで運命を得て、呪族と魔族以外に一度だけの種族変更が可能/種族変更を行った際、〈不死の贖罪〉によってHP&MP+3/全ステータス値が+3/技能ポイントが+150（種族変更時の名声が+6より上の場合、取得技能ポイントが以下のように増加/名声+6：180/名声+7：210/名声+8：240/名声+9：270/名声+10：300）される】
            ※不死の贖罪のボーナスは通常の種族変更では取得できない"""
    elif race == "甲虫人":
        race_skill_text = """【種族スキル】
            〈全甲種〉常時防護点+3/毒系・裂傷系の状態異常を無効化する/対虫特性が弱点
            〈亜甲種〉常時防護点+1/毒系・麻痺系の状態異常を無効化する/対虫特性が弱点
            種族特性〈全甲種、亜甲種共通〉
            ♢堅甲の矜持/アクティブ
            【戦闘時に事前宣言で発動/HPが1減るごとに物理攻撃ダメージが+1%増加していく（例：HP50の状態でHPが30減少した場合、物理攻撃ダメージ+30%）/発動時、被ダメージ+50%/戦闘が終了するまで効果は持続する（自身が戦闘不能になって蘇生された場合、再度の宣言が必要）】
            ♢外骨格防御/アクティブ
            【外骨格を駆使し、敵の攻撃の威力を減衰させる/受動作/MP-30消費で発動/敵ダメージに累減-50%（盾等の累減と併用不可能）/発動後、20の固定ダメージを受けて1ターンの行動不可&5ターンのクールタイム。また、クールタイム中に敵ダメージを受けて倒された場合、強制的に10の固定ダメージを受ける（HP1を残して生存する耐久判定時等を行った場合は、成功したあとに固定ダメージを受ける）】
            ♢優れた視界/パッシブ
            【目星判定、または索敵判定時、+5の上限突破補正値を得る（スカウトには適用されない）】
            ♢高速接近/パッシブ
            【接近判定時、+10の補正値を得る】
            ♢外骨格破壊/特殊
            【HP残量がHP上限の50%未満になった場合、防護点と防御力（ダメージカット率）が0となる。更に被ダメージ+30%】"""
    elif race == "半獣人":
        race_skill_text = """【種族スキル】
            白兵威力+5%/投擲威力+10%/運命装備使用可能
            ♢半獣化
            【1ターン持続（家柄71以上の場合は2ターン持続）/白兵攻撃与ダメージ1.2倍、HP+10、被ダメージ10%減/発動後は1ターン行動不可/発動後、3ターンのクールタイム】
            ♢半獣の怒り
            【種族特性:人間&獣人に対して物理威力+20%】"""
    elif race == "マンティコアF":
        race_skill_text = """【種族スキル】
            常時防護点+5
            銃と火属性攻撃に対する被ダメージ+50％
            ♢変貌
            【パッシブ/自由に姿や声を変えることが可能（ただし、人格や意識はすべて単一である）/ファンタジアで教会に襲われる際、基準値30の変装技能判定成功で逃走が可能
            （もし味方に魔族がいて見つかった際は、そのまま自身だけ離脱が可能）】
            ♢暴食
            【助動作/倒した敵（倒してから2ターン経過すると暴食の対象にすることが不可能になる）を喰らうことでHPが30％回復し、1ターンの間攻撃威力が+50％される/敵が1体しかいない場合、敵のHPが半分以下になると発動できるようになる（その際に敵側は暴食に対して回避を行う）/発動後､1ターンのクールタイム】
            ♢飢餓
            【戦闘で3ターン以上が経過した場合、飢餓によってHPが35％ずつ減少していく。この際に倒した敵を暴食発動によって喰らうか、もしくは料理を食べなければカウントが進んでいき、HPが0になって戦闘不能になる】
            ♢魔獣化
            【助動作/人面の獅子のような悍ましい魔獣の姿になり、1ターンの間HP上限が+100％され、HPを全回復する/ターン終了後は1ターン全行動不能（受動作含む）の上でHPが1になり、2ターンの状態異常：出血を付与される】"""
    elif race == "マンティコアN":
        race_skill_text = """【種族スキル】
            常時防護点+2
            銃と火属性攻撃に対する被ダメージ+50％
            ♢変貌
            【パッシブ/自由に姿や声を変えることが可能（ただし、人格や意識はすべて単一である）/ファンタジアで教会に襲われる際、基準値30の変装技能判定成功で逃走が可能
            （もし味方に魔族がいて見つかった際は、そのまま自身だけ離脱が可能）】
            ♢暴食
            【助動作/倒した敵（倒してから2ターン経過すると暴食の対象にすることが不可能になる）を喰らうことでHPが30％回復し、1ターンの間攻撃威力が+50％される/敵が1体しかいない場合、敵のHPが半分以下になると発動できるようになる（その際に敵側は暴食に対して回避を行う）/発動後､1ターンのクールタイム】
            ♢飢餓
            【戦闘で3ターン以上が経過した場合、飢餓によってHPが35％ずつ減少していく。この際に倒した敵を暴食発動によって喰らうか、もしくは料理を食べなければカウントが進んでいき、HPが0になって戦闘不能になる】
            ♢魔獣化
            【助動作/人面の獅子のような悍ましい魔獣の姿になり、1ターンの間HP上限が+100％され、HPを全回復する/ターン終了後は1ターン全行動不能（受動作含む）の上でHPが1になり、2ターンの状態異常：出血を付与される】"""
    elif race == "天狗":
        race_skill_text = """【種族スキル】
            妖怪の呪い：技能ポイント-100/妖力量：3（戦闘開始時点は0。戦闘中に増やしていく形となる）
            ◉天狗の風読み
            └天狗は風を読み、見出した流れに翼で乗る。一方で、風を読まなければ飛べない欠点を持つ
            《風読み【天狗】技能を使用可能。技能値は家柄〜70で50、71〜で60、100で70。技能判定が成功すると、1d3ターンの間だけ飛行が可能。算出されたターン数分だけスタミナを消費し、飛行中は回避をしてもスタミナを消費しない（判定や処理は翼人の飛行技能と同様）/発動後、3ターンのクールタイム》
            ◉妖力
            └妖怪などの邪悪な存在に存在する力。魔力と異なり、人の恐怖や悔恨を食い物にする
            【一回の戦闘で"自分で敵を1体倒す・パーティーの味方が1人倒れる"のいずれかが行われた場合、妖力が+1される（ただし同じ味方がもう一度倒れても妖力は増えない）/1ターンの間、なにも動作を消費せずに待機を行うと、妖力が+1増加する】
            ―――――
            ♢妖技《天狗の外法》
            └妖力3で発動可能。これを使用すると一時的に皮膚が赤く染まり、顔が鳥のようになるか、もしくは鼻が高くなる。またはそれらにならず、お面を被るだけの天狗も存在する
            （ただし皮膚が赤く染まらないだけで、常に鼻が高かったりする者も存在する）
            《この妖技を発動した状態で風読み【天狗】技能を成功すると、飛行ターン数の間だけ、攻撃威力が+100%されるほか、敵からのダメージを-20%する》"""
    elif race == "鬼半妖":
        race_skill_text = """【種族スキル】
            投擲威力+10%/通常攻撃で魔族を浄化可能
            ◉鬼半舞
            【事前動作/発動後、HP残量を-1〜-50することにより、減らしたHPの分だけ攻撃力を1ターン増加させる（最大+50%まで）/発動後、3ターンのクールタイム】
            ◉浴血の怒撃
            【前提条件：魔族にダメージを与える
            （魔族であれば同一でなくとも構わない。ただし、敵である必要がある）
            魔族（以下、敵）のHPを30以上減らした場合、浴血Lv1の効果を得る。
            Lv1の状態で敵のHPを60以上減らした場合、Lv2となる。
            そしてLv2の状態で敵のHPを120以上減らした場合、Lv3となる
            /浴血の怒撃は事前動作で発動宣言を行うと、以後は発動開始から戦闘終了まで常時発動状態となる】
            効果
            Lv1：対魔族威力+20%、被ダメージ-10%
            ↓
            Lv2：対魔族威力+40%、被ダメージ-20%
            ↓
            Lv3：対魔族威力+80%、被ダメージ-30%、敵からの属性相性無効化
            （例：自分が水属性で雷属性ダメージを与えられても、ダメージが倍加されない。逆に自身の属性で敵の弱点属性を突くことは可能になる）"""
    elif race == "クラーケンF":
        race_skill_text = """【種族スキル】
            水泳技能+30
            ♢海棲の魔族
            【水に関係した舞台特性の場合、常時攻撃力+30%&HP、MP+20増加/水属性ダメージを受けるとHP、MP10%&スタミナ1回復
            ♢水底の擬態
            【擬態により、魔族とバレづらくなる/1日に1回のみ、襲撃判定が成功しても幸運判定を成功させることで無効化することが可能（事前のクエストで後述の不利効果を受けた場合、これは無効化される）/不利効果：祝福武器、もしくは光属性の攻撃を受けた場合、戦闘中常時被ダメージ+50%の効果と共に正体が露呈する】
            ♢捕食
            【助動作/敵に格闘技能判定を行い、成功して噛みつくことで、全防護点&全防御力半減のダメージを与える/与えたダメージ分、HPが回復/捕食発動時の格闘技能には血属性が付与される/敵が水属性の場合、回復量2倍/クールタイム1ターン】"""
    elif race == "クラーケンN":
        race_skill_text = """【種族スキル】
            水泳技能+15
            ♢海棲の魔族
            【水に関係した舞台特性の場合、常時攻撃力+30%&HP、MP+20増加】
            ♢水底の擬態
            【擬態により、魔族とバレづらくなる】
            ♢捕食
            【助動作/敵に格闘技能判定を行い、成功して噛みつくことで、全防護点&全防御力半減のダメージを与える/与えたダメージ分、HPが回復/敵が水属性の場合、回復量2倍/クールタイム1ターン】"""
    elif race == "蹄人族":
        race_skill_text = """【種族スキル】
            近接威力+10%
            ♢蹄獣化
            【1ターン持続（家柄100の場合は2ターン持続）/白兵攻撃与ダメージ1.1倍、効果ターン中、回避を1ターンに一回だけ再判定可能（再判定は回避値の半分の基準値が付与される）/物理防護点+2（家柄100の場合は物理防護点+4に上昇）/効果終了後、3ターンのクールタイム】
            ♢蹄人の誇り
            【種族特性:敵の名声が-5以上、もしくは魔族か呪族の場合、攻撃力+20%】"""  
    elif race == "マリオネット":
        race_skill_text = """【種族スキル】
            常時被ダメージ+10%
            ♢糸仕掛けの繰り人形
            【事前動作でHPを30消費すると1ターンの間、攻撃力を+20%/この特性の使用後はクールタイムによって3ターンのあいだ再使用が不可となる】
            ♢一糸不乱のバラッド
            【事前動作/発動時、精神限界-20%（混乱判定は起きない）/発動後1ターンの間攻撃力+5%/以降、1ターンごとに攻撃力が+5%されていく（初期威力増加と合わせて最大30%まで増加する）/効果は戦闘終了後まで続く】"""
    elif race == "メルフェディオヌF":
        race_skill_text = """【種族スキル】
            常時被ダメージ+30%
            ①邪血の秘術
            └事前動作で発動。血腥き、神をも恐れぬ弑逆の術を発動する。
            〈HP+70%回復/1ターンの間、攻撃ダメージ1.8倍・物理&魔法ダメージカット率+30%〉
            血耽りの秘術の発動には〈邪血点〉が必要である。
            これらは敵に攻撃を行い、HPの吸収量が自身HP上限の10%以上に達すると1ずつ増えていく。
            （1ターンに増加する邪血点の数は1点まで）
            消費した邪血点の数値に比例して邪血の秘術のターン数は増加（邪血点1ごとの持続ターンは1ターン）
            邪血点上限は家柄1-70で3/家柄71-99で4/家柄100で5である。また、邪血点は効果発動中は加点されない。
            効果終了後、3ターン行動不能（受動作による防御行動のみ可能）。行動不能中に邪血点は増加しない
            〈邪血化は邪血点が2点以上でなければ発動できない〉
            ②裂け血啜り
            └敵を攻撃して与えたダメージの10%を吸収し、吸収したぶんを自身のHPに反映して回復することが可能。亜竜に攻撃した場合は吸収量が20%に変化。半竜か竜に攻撃した場合は同族喰らいの特性が付き、吸収量が30%に変化する
            ③異端の血竜
            【亜竜に対するダメージ+20%/半竜に対するダメージ+30%/竜（ドラシオン含む）に対するダメージ+40%】"""
    elif race == "メルフェディオヌN":
        race_skill_text = """【種族スキル】
            常時被ダメージ+30%
            ①邪血の秘術
            └事前動作で発動。血腥き、神をも恐れぬ弑逆の術を発動する。
            〈HP+50%回復/1ターンの間、攻撃ダメージ1.6倍・物理&魔法ダメージカット率+25%〉
            血耽りの秘術の発動には〈邪血点〉が必要である。
            これらは敵に攻撃を行い、HPの吸収量が自身HP上限の10%以上に達すると1ずつ増えていく。
            （1ターンに増加する邪血点の数は1点まで）
            消費した邪血点の数値に比例して邪血の秘術のターン数は増加（邪血点1ごとの持続ターンは1ターン）
            邪血点上限は家柄1-70で3/家柄71-99で4/家柄100で5である。また、邪血点は効果発動中は加点されない。
            効果終了後、3ターン行動不能（受動作による防御行動のみ可能）。行動不能中に邪血点は増加しない
            〈邪血化は邪血点が2点以上でなければ発動できない〉
            ―――――
            ②裂け血啜り
            └敵を攻撃して与えたダメージの10%を吸収し、吸収したぶんを自身のHPに反映して回復することが可能。亜竜に攻撃した場合は吸収量が20%に変化。半竜か竜に攻撃した場合は同族喰らいの特性が付き、吸収量が30%に変化する
            ※ノクターンの場合は吸収量が全て-5減少
            ―――――
            ③異端の血竜
            【亜竜に対するダメージ+20%/半竜に対するダメージ+30%/竜（ドラシオン含む）に対するダメージ+40%】"""
    elif race == "ハイエルフ":
        race_skill_text = """【種族スキル】
            特性：エルフの貴種
            【全魔法の威力・効果+1.2倍（これは回復魔法の回復量や、魔導弓などの魔導武器などにも適用される）/攻撃魔法の命中クリティカル時、威力+2D】
            我らこそエルフの統治者なり
            【全魔法MP消費-5%/知力依存技能+5】"""
    elif race == "ハーフエルフ":
        race_skill_text = """【種族スキル】
            運命装備使用可能
            特性：交差した血統
            【全魔法の威力+10%/攻撃魔法の命中クリティカル時、威力+1D/投擲威力+10%】"""
    elif race == "ダークエルフ":
        race_skill_text = """【種族スキル】
            特性：黒魔術
            【攻撃魔法の威力+50%/攻撃魔法の消費MP+20%】"""
    elif race == "ドワーフ":
        race_skill_text = """【種族スキル】
            白兵ABの補正値+2（例：白兵ABが1d10なら1d10+2になる）/片手斧の威力+20%"""
    elif race == "ウッドエルフ":
        race_skill_text = """【種族スキル】
            特性：アカシックレコード
            【攻撃魔法のダメージ-10%/消費MP-10%(軽減上限の範囲外)/知力依存技能判定+10】
            原初のエルフ
            【家柄71以上の場合は弓技能（魔弓含む）の威力1.2倍&命中+5/家柄71以上の場合はMP+5】
            太古の氏族
            【Lvが1上がるごとにMPが3ずつ増加】
            豊かな言語知識
            【母語とエルフ語と共通語を除いたあらゆる言語技能を1つだけ、70で取得可能】"""
    elif race == "フェルダー":
        race_skill_text = """【種族スキル】
            特殊技能《高速回避》
            ♢活発
            └QP+2
            ♢生活の心得
            └シナリオ・クエスト・労働での獲得資金+5%/家柄71-：+10%/家柄100：+15%
            （クエストで仲間とパーティを組んでいた場合は自身の獲得資金ボーナスの半分倍加させてあげることができる〈例：家柄70のフェルダーがいた場合はパーティ全員+2.5%のボーナス〉/同特性同士が同行していた場合、重複はせずに家柄が高い方のボーナスが優越される/他の資金倍加ボーナスがあった際は通常通り加算方式）
            ♢疲弊
            └フェルダーはすばしっこいが、同時に疲れやすい性質も持つ。回避時の消費スタミナ+1（高速回避時も同様に消費する）/スタミナ残量が50%未満の時、被ダメージ+20%
            ♢軽耐久
            【HP上限-30%（例：HP100の場合 0.7倍されて70に低下）】"""
    elif race == "ヴァンパイア":
        race_skill_text = """【種族スキル】
            特殊技能：吸血〈家柄71未満の場合は50以下、71以上の場合は70以下、100の場合は90以下が達成値〉
            浄化攻撃系に対しての被ダメージ2倍/格闘ダメージ+1D(血属性自動付与/三連撃まで可能になる/次撃以降命中-10)
            ♢浄化攻撃以外では部位も破損せず死なずにその場で蘇生する（クエスト時などは普通に戦闘不能になる〈ただし蘇生費がなくなってもケガレがたまらない〉
            ♢自身の家柄以下のものを吸血成功後眷属にすることが可能〈ただしPLやプレイアブルキャラの場合は相手に同意が必要〉
            ♢戦闘時、1ターンが経過するたびにHPを10%再生回復
            ♢戦闘中、吸血技能で敵or味方に吸血して吸血点を得ることで1回につき攻撃力を+10%（最大+30%/吸血1命中につき1点）/戦闘終了で吸血点はリセット/吸血点が3点に達すると、再生効果が1ターンにつき20%回復に変化
            ♢神秘術を使用してHPを回復することが不可能（アイテム回復は可能）
            ♢吸魂：ダンピール&鬼半妖と魔族を除く仲間から許可を得ることにより、助動作でHPを吸うことが可能。一気に吸える最大人数は4名まで/一人につき10%(レッサー)/20%(ノーブル)/30%(吸血鬼の王)までHPを吸うことが可能/一度使用すると3ターン使用不可/技能値は60(レッサー)、70(ノーブル)、80(吸血鬼の王)/使用後は3ターンの間、吸魂されたプレイヤーたちは吸収されたぶんのHPを3ターンの間回復不可。発動するとカルマ＋1 """
    elif race == "人狼":
        race_skill_text = """【種族スキル】
            人狼化が可能（助動作/発動時スタミナ-3消費、2ターンの間自身の爪撃ダメージ+1D、爪撃を含む物理攻撃力+20%、HP+25）　/100の場合（発動時スタミナ-5消費、2ターンの間自身の爪撃ダメージ+2D、爪撃を含む物理攻撃力+30%、HP+35）　/属性は血固定/筋力＆俊敏の上限85】
            〘格闘が爪撃に変容。爪撃には血属性が付与される/威力+5d（その代わり喧嘩術、武術取得不可）/次撃以降は反動で命中が-10されていく/3撃目まで連撃可能（連撃増加は不可）/片手武器装備時、もう片方になにも装備していない場合、一撃のみ爪撃での事前攻撃が可能〙
            ※人狼化は一回の戦闘につき一度まで"""
    elif race == "デュラハン":
        race_skill_text = """【種族スキル】
            QP-1
            ♢黒血の篝火
            └黒き血炎の馬に跨り首から上を轟々の血炎で覆いながら、篝火の如く燃え盛る自らの頭を抱え臨む
            【HPを-50%して助動作で変化/全攻撃ダメージ+30%/回避+10/敵ダメージに累減-15%/この形態中は自ターン終了後にHP-10のスリップダメージ（毎ターン）/形態終了には1ターン必要（その間は行動不可/スリップダメージ継続）/この形態中はあらゆる回復手段を受け付けない/黒血発動中に戦闘不能になった場合、蘇生不可】
            ♢虚ろの幻像
            └人とは目に見えるものしかわからない。それは誰も同じである。
            【属性などありとあらゆるものを仮初めの幻で偽装する/魔族・ダンピール・出自：聖職者の者に目星/または浄化攻撃を行われると正体を見破られる/Lv3になって魂喰らいをしても教会にバレない（ただし、クエスト中に黒血の篝火か魔法攻撃を行うとばれてしまい、通常の魔族通りの教会判定が始まる）】"""
    elif race == "ダンピール":
        race_skill_text = """【種族スキル】
            特殊技能：魔族狩り（魔族に対して与ダメージ+100%）
            ブルーブラッド（吸血などの魔族の特性攻撃を無効/魔族からのダメージ-30%〈この特性はあらゆるダメージカット率軽減効果を無効化する〉/魔族に対して基準値20の目星判定を行い成功した場合、その魔族の正体を見破ることができる。ただし、目星判定を行うには原則として相応の理由が必要）/運命武器を使用可能/投擲威力+10%/通常攻撃で魔族を浄化可能"""
    elif race == "レウィス・ゴーレム":
        race_skill_text = """【種族スキル】
            家柄〜70で物理防護点1、71〜99で物理防護点2、100で物理防護点3を常に持つ（防具を着用していた場合、重複する）
            ♢再起動【魔導術式】
            └アクティブ/受動作/1回の戦闘で一度だけ、HPが0になるダメージを受けた場合、幸運判定を成功させることにより、残りHP10の状態で生存が可能。ただし、発動後は1ターンは受動作以外の行動ができなくなる。この特性は他にある同様の効果よりも優先して強制発動される
            ♢防御形態
            └アクティブ/事前動作/1ターンの間、自身被ダメージに累減-20%を付与する/発動時、攻撃力-30%/2ターンのクールタイム"""
    elif race == "ゴブリン":
        race_skill_text = """【種族スキル】
            白兵AB+1D
            〈種族能力〉
            《呪われた本能：人族・亜人族を含む人間族に対するダメージを常時+50%》
            《蛮族：クエスト成功での獲得アイテム(素材のみ)を幸運成功で+1する(ただし入手していない場合、これが適用されることはない)》"""
    elif race == "ハーフドラゴン":
        race_skill_text = """【種族スキル】
            運命武器使用可能
            投擲威力+10%
            ①ドラゴンハート
            └助動作/発動時、MP-20消費/一時的にドラゴンの力を発揮。半竜であるため本物のドラゴンに比べると力は劣るが、敵の全防護点-2、攻撃ダメージ1.2倍、物理&魔法ダメージカット率+5%の効果と半竜の呪いの一時解除効果（ドラゴンハートの発動ターン内のみ）を得る
            ドラゴンハートの効果継続ターン数は3ターン
            また、ドラゴンハートの効果終了後、2ターンは再発動することができない
            ②半竜の呪い
            └被ダメージ+20%"""
    elif race == "スノウエルフ":
        race_skill_text = """【種族スキル】
            QP家柄71未満+1/71以上+2/100なら+3）】
            ♢氷雪の貴人
            【氷/雪属性&家柄91以上の場合はHP&MP+5/魔導AB+1D】
            ♢白雪の誇り
            【魔法威力+20%/毎ターン、行動終了後にMPを精神の10%で1d回復(例：精神が70の場合は毎ターン1d7回復)/ハイエルフが敵の場合、魔法威力+100%】"""
    elif race == "妖精族":
        race_skill_text = """【種族スキル】
            ◉魔力体
            《MPが0になると即時戦闘不能状態になる/魔法・戦技・武器スキルの消費MP+1.2倍（魔導弓は対象外）》
            ◉妖精
            《HPが0になったとしてもMPが残っている場合、精神ロール成功で1ターンだけ生存可（ただしHP回復は不可）》
            ◉妖精魔法
            《攻撃魔法ダメージ+10%/中級魔法までなら助動作で可能（ただし助動作で中級魔法を使用した際は判定の成否にかかわらず、その後の主動作は下級魔法でなくてはならない。助動作が下級魔法だった場合、主動作は自由）》
            ◉妖精庭園〈フェアリーガーデン〉
            《主動作/発動には天級魔法技能の成功判定が必須》
            【一回の戦闘に一度だけ発動可能/発動時、自身以外の指定した3名のプレイヤーのHP/MPを50%回復する。その代わり自身のHPとMPは50%減少する/発動後次のターンから、1(家柄71未満)/2(家柄71以上)/3ターン(家柄100)の間だけ自らのMP消費が1.2倍から等倍になり、魔法威力+20%&敵からの魔法ダメージ-20%】
            ◉妖精の舞
            【助動作でダンス技能を成功させると、MPが30%回復する/1回の戦闘に一度だけ使用可能】"""
    elif race == "ホムンクルス":
        race_skill_text = """【種族スキル】
            QP+1（家柄100の場合は+2）
            ◉錬金の素質
            └ホムンクルスは錬金術によって生を受けた存在である。ゆえに、彼らには確かな才が存在するのだ。
            【錬金術初期値+10/錬金術威力+20%/錬金術の消費MP-10%/魔毒によるダメージや状態異常等の不利効果を全て無効化する】"""
    elif race == "ダークドワーフ":
        race_skill_text = """【種族スキル】
            家柄100の場合、〈クリエーション・マジックウェポン〉を発動できる/白兵AB+2（例:白兵ABが1d10の場合、1d10+2のようになる）/両手斧威力+20%
            ◉魔導器鍛
            《特殊鍛冶【魔導武器】の初期値が増加/家柄1〜70：初期値15/家柄71〜90：20/家柄91〜99：25/家柄100：30》
            ◉魔纏強化
            《戦闘中に特殊鍛冶【魔導武器】を使用した場合、仲間の武器に〈助動作〉で自身の属性（双属性の場合はいずれかを選択）をエンチャントすることができる。自身の武器には付与できない/使用時MP-20/エンチャント持続ターン-家柄1〜70：初期値1/家柄71〜90：2/家柄91〜99：3/家柄100：4》
            ◉クリエーション・マジックウェポン
            《通常武器を鍛冶で作成中、〈魔導素材〉を素材に追加することでその素材に応じた特性と属性を付与することができる》"""
    elif race == "蛇人":
        race_skill_text = """【種族スキル】
            ラミア（性別：女）
            種族特性
            ♢蛇人の祭祀
            【知力ABのダイス値+2（例:知力ABが1d10の場合、1d12になる）】
            ♢高貴なる変化
            【青鱗以上の家柄の場合、助動作による宣言後にMPを15消費することで蛇尾から人間の足に変化することが可能。ただし、変化中は回避が-15される】
            リザードマン（性別：男&中性）
            ♢蛇人の戦士
            【白兵ABの出目+1（例：白兵ABが1d10の場合、1d12になる）】
            特殊種族特性
            ♢虹鱗の祝福
            (家柄100限定)
            【蛇人の祭祀/蛇人の戦士のダイス値増加が+2から+4になる(例：通常の加算後数値が1d12だとして、この特性が適用されると1d14になる)】
            ♢灰鱗の因果
            (家柄1限定)
            【エキドナの因果により、MPが+15/魔法ダメージが+10%される】"""
    elif race == "幻蛛族":
        race_skill_text = """【種族スキル】
            ♢幻蛛の毒牙
            【事前動作/技能値50（家柄71〜：60/家柄100：70）/相手に命中すると、1ターンの間、自身の攻撃に対する回避基準値が+10される（特性：麻痺などの回避基準値増加効果とは重複せず、こちらが上書きされる）/使用後、クールタイム3ターン】
            ♢蜘蛛の謀略
            【助動作/隠密を70以上習得した状態で短剣を装備している場合、短剣攻撃に回避不可属性を与えることができる/このスキルの発動中は威力増加率が+100％までに制限される（クリティカルは制限外）/使用後、クールタイム2ターン】
            ♢幻蛛の蜘糸
            【1d10mまで蜘蛛尾から糸を紡ぐことが可能/戦闘時は受動作でのみ使用可能。その場合、回避が+1d10増加する（上限突破）/使用後、クールタイム3ターン】
            特殊種族特性
            ♢貴き幻蛛の血統
            (家柄100)
            【幻蛛の毒牙と幻蛛の蜘糸のクールタイムが3ターンから2ターンになる】
            ♢伝統の糸織
            【製作判定時、素材に糸がある場合は技能値が+5向上する（上限突破）】"""
    elif race == "失耀天使":
        race_skill_text = """【種族スキル】
            QP+1
            ♢黒冠の祈り
            /パッシブ
            【敵からの光属性ダメージ-20%】
            ♢黒翼の誓い
            /アクティブ
            【MP-50/俊敏判定/判定成功後、最大2ターンの間飛行が可能。飛行中はスタミナが1ターンにつき-3されていく/飛行効果については翼人の物と同様】
            ♢天墜の撃印
            /アクティブ
            【助動作/HP-30&MP-30/知力判定/判定成功後、対象に1ターンの間、撃印を付与/撃印を付けられた対象に与えられる夜属性&光属性ダメージ+50%/使用後、クールタイム3ターン】"""
    elif race == "コブラナイ":
        race_skill_text = """【種族スキル】
            ♢生活の心得
            └シナリオ・クエスト・労働での獲得資金+5%/家柄71-：+10%/家柄100：+15%
            （クエストで仲間とパーティを組んでいた場合は自身の獲得資金ボーナスの半分倍加させてあげることができる〈例：家柄70 の同特性者がいた場合はパーティ全員+2.5%のボーナス〉/同じ特性同士が同行していた場合、重複はせずに家柄が高い方のボーナスが優越される/他の資金倍加ボーナスがあった際は通常通り加算方式）
            ♢採掘の心得
            └採掘時の筋力判定+10（上限突破）/採掘した獲得数+1（例：鉄鉱石を入手した場合、+1されて2つ入手可能）
            ♢鉱石の目利き
            └インゴットに精製する製作が成功して一つでも完成品を得た場合、判定値70(家柄71〜90：80/家柄91〜99：85/家柄100：90/この判定値はアビリティの影響を受けない)で獲得数+1（例：5個のインゴットを精製して3つ成功した場合、目利き判定を3回成功させることで+3個入手/この判定にクリティカルとファンブルは存在しない）。アイテム名にインゴットとつくものならばすべてに適用される(鉄→鋼でも獲得数は増加される)"""
    elif race == "アルケミーゴーレム":
        race_skill_text = """【種族スキル】
            家柄〜70で魔法防護点1、71〜99で魔法防護点2、100で魔法防護点3を常に持つ（防具を着用していた場合、重複する）
            HPにダメージを15受けるごとに自己魔毒値+1/錬金術威力+2D
            ♢魔毒蓄積
            └アルケミーゴーレムには自己魔毒値（生命力ステータス÷5）が存在し、魔毒が発生するなどで溜まっていく。これは戦闘が終了するとリセットされるが、上限に達すると即時戦闘不能となり、同チームの仲間全体（自身以外に最大三名）に魔毒1d10をばら撒く。ただし、魔毒が1上がるごとに攻撃力が+5%されていく
            （最大+30%まで上昇）
            ♢再起動【錬金術式】
            └アクティブ/受動作/1回の戦闘で一度だけ、HPが0になるダメージを受けた場合、幸運判定を成功させることにより、残りHP10の状態で生存が可能。ただし、発動後は1ターンは受動作以外の行動ができなくなる。この特性は他にある同様の効果よりも優先して強制発動される/発動時、自己魔毒値+1d5
            ♢攻撃形態
            └アクティブ/事前動作/1ターンの間、攻撃力+20%&自身攻撃に対する敵回避に基準値10付与/発動時、被ダメージ+20%&自己魔毒値+1d3/2ターンのクールタイム"""
    elif race == "フレイムエルフ":
        race_skill_text = """【種族スキル】
            ♢火末の因果
            【炎属性の場合はMP+10/知力AB+1D】
            ♢猛炎の誇り
            【全火属性攻撃威力+20%/毎ターン、行動終了後にMPを精神の10%で1d回復(例：精神が70の場合は毎ターン1d7回復)/フレイムエルフ以外のエルフが敵の場合、魔法威力+50%】"""
    elif race == "ウーンゲフォイヤー":
        race_skill_text = """【種族スキル】
            防護点5/防御力50
            ①魔毒纏い
            └助動作で発動。己をも蝕む魔毒を纏うことで、強力なダメージを敵に与える
            【発動後、3ターン効果継続/1ターンにつき15の固定ダメージを受ける(1ターン目は発動開始時点で確定として受ける)/1ターン経過するごとに攻撃威力を+20%していく(初期状態+0%/2ターン目：+20%/3ターン目：+40%)/敵を1回攻撃するごとに、敵のHP上限を10減らしていく/効果終了後、1ターン行動不可】
            ―――――
            ②アルケミアの悍ましき遺産
            【魔毒汚染を無効/魔毒ダメージを無効/敵に20以上の最終ダメージを与えると、スタミナ1回復(錬金術でダメージを与えた場合はHP10回復)/錬金術ダメージ+30%】
            ―――――
            ③人工の魔族
            【他魔族に対するダメージ+20%/他魔族からの被ダメージ+20%/製作技能の初期値+5】"""
    elif race == "ヴァンシー":
        race_skill_text = """【種族スキル】
            QP+1
            詠歌初期値+20
            ♢魔力体
            【MPが0になると即時戦闘不能状態になる/魔法・戦技・武器スキルの消費MP+1.2倍（魔導弓は対象外）】
            ♢妖精
            【HPが0になったとしてもMPが残っている場合、精神ロール成功で1ターンだけ生存可（ただしHP回復は不可）】
            ♢鎮魂の詠叫
            /アクティブ
            【助動作/詠歌技能によって発動/指定した2名(自身を指定可能)のMPを30%回復&瘴気を解除し、更に1ターンの間瘴気を無効化する/クールタイム2ターン】
            ♢弔いの一閃
            /アクティブ
            【効果ターン：1/自属性を付与した属性物理攻撃の威力を+20%/効果中、あらゆる防護点や防御力を半減する(既に近似した特性がついているか、同一の特性を持った攻撃に関しては付与されない)/クールタイム2ターン】
            ♢瘴気払いの力
            /パッシブ
            【死霊術師&死霊に対するダメージ+50%/呪族&魔族に対するダメージ+10%/瘴気ダメージ-10%/死霊術使用不可】"""
    elif race == "炉心異常体":
        race_skill_text = """【種族スキル】
            回避基準値+15/スタミナ-50%（例：スタミナ5の場合、2に減少）/家柄71以上で運命武器を使用可能/投擲威力+10%】
            ♢筋肉の鎧：筋力÷20の1d防護点を得る（敵ダメージを受けた際、筋力70の場合は筋肉の鎧で敵ダメージを1撃毎1d3点軽減する/筋肉の鎧の判定は敵の連撃数に問わず一律一括判定となる）
            ♢筋肉の底力：白兵攻撃の威力+20%強化
            /武器攻撃の連撃数−１
            （該当する武器攻撃は格闘、喧嘩術、武術以外の全ての白兵戦闘技能を指す）"""
    elif race == "魔眼発現体":
            race_skill_text = """【種族スキル】
                特殊技能：魔眼（家柄:〜70：40/71〜：50/91〜：60/家柄100：70の達成値/重ねがけ不可）
                投擲威力+10%/家柄71以上で運命武器を使用可能"""
    elif race == "演算異常体":
            race_skill_text = """【種族スキル】
                技能：先読み（詳細は技能ルールの種族技能の項目を参照）
                投擲威力+10%/家柄71以上で運命武器を使用可能
                ♢軽耐久
                【HP上限-30%（例：HP100の場合 0.7倍されて70に低下）"""
    elif race == "強化演算体":
            race_skill_text = """【種族スキル】
                技能：先読み（詳細は技能ルールの種族技能の項目を参照）
                投擲威力+10%/家柄71以上で運命武器を使用可能
                ♢ルサンチマン
                【強化演算体のみ使用可能／戦闘中、精神限界を-1d6することで回数限界を超えて先読みを可能にする（戦闘終了で減少した上限は回復）／最大４回まで発動可能】
                ♢軽耐久
                【HP上限-30%（例：HP100の場合 0.7倍されて70に低下）】"""
    elif race == "サイボーグ":
            race_skill_text = """【種族スキル】
                ♢限界突破
                └事前動作/1ターン（家柄71以上で2ターンに上昇）の間パルクール〈技能値70〉が使用可能/回避+10、被ダメージ-20%、与ダメージ+20%/発動時、HP&MPを30%即時回復/使用後、1ターンのクールタイム（家柄71以上の場合は2ターンのクールタイム）"""
    elif race == "アンドロイド":
            race_skill_text = """【種族スキル】
                ♢オーバードライブ
                └1ターン（100：2ターン）の間、被ダメージ+200%&与ダメージ+100%&回避基準値+20/ 効果終了後2ターン行動不可）"""
    elif race == "クローン":
            race_skill_text = """【種族スキル】
                運命武器使用可能"""
    elif race == "幻影体発現者":
            race_skill_text = """【種族スキル】
                固有能力は《幻影異能》：ノクターンで属性を行使することが出来る
                ◉エレメンツ/エンチャントの2つのうち、いずれかを選びます。エレメンツは《短期戦》向き/エンチャントは《長期戦》向きです
                ✧エレメンツ：MP-10で家柄71未満：威力1d10&命中50/71以上：威力2d10&命中60/100：威力3d10&命中70の幻影術（魔法扱い）を使用可能〈事前攻撃可能/1ターンに2発まで連射可能〉】
                ✦エンチャント：MP-15で兵器・武器に属性エンチャントをかけることができる。ただし属性エンチャント付与中の攻撃は【与ダメージ30%軽減】される。
                それぞれ家柄71未満：1ターン/71以上：2ターン/100：3ターンの間、エンチャントが持続する。
                ただしそれぞれエンチャント終了後のクールタイムが〈1ターン/3ターン/6ターン〉"""
    elif race == "ヴィロン":
            race_skill_text = """【種族スキル】
                家柄〜70で防護点6、71〜99で防護点8、100で防護点10を常に持つ〈ただし防護点付きの服、防具は装備不可〉
                全操縦技能+5（+10/+15）/回避基準値+10"""
    elif race == "ノクト・ヴァンパイア":
            race_skill_text = """【種族スキル】
                特殊技能：吸血〈家柄71未満の場合は30以下、71以上は50以下、100の場合は70以下が達成値/敵を操ることは不可能〉
                浄化武器系列に対しての被ダメージ2倍
                1ターンごとに2d5ほどHPが再生していく
                レッサーは昼間（リアルタイム）だと再生効果を失い、通常武器でも死ぬ/ヴァンパイアは食事の効果を受けることができず、食事バフを受けたい場合は一日一度は吸血しなければならない/ヴァンパイアは吸血以外でアイテムや魔法を使用してHPを回復させることが不可能（MP回復は可能）
                ◉教会の祝福
                └蘇生費二倍/魔族でありながら常人と同じく穢れがたまるとロストする上に祝福&運命武器からの倍加ダメージは受ける/被ダメージ+25%
                ◉ブラッディ・ウェポン
                └血属性武器を生成する。武器種は片手剣と両手剣のいずれかのみ（技能必須）、近接武器のみ可能。威力は片手武器の場合1d〈家柄÷5〉・三連撃まで可能/両手武器の場合2d〈家柄÷5〉・連撃不可/1ターンの形状維持にHP−5&MP−5/形状維持解除またはHP不足で強制解除されると3ターンは生成不可/ブラッディウェポンで傷付けられた敵は原則回復不可能&防護点貫通（兵器を除く）/ブラッディウェポンの連撃数はありとあらゆる要素でも一切増加しない（通常の武器とは異なる）"""
    elif race == "ノクス・エルフ":
            race_skill_text = """【種族スキル】
                ♢夜想の貴人
                【家柄91以上の場合はHP&MP+5】"""
    elif race == "ノクス・ハーフエルフ":
            race_skill_text = """【種族スキル】
                運命装備使用可能/投擲威力+10%"""
    elif race == "ホットロード・サイボーグ":
            race_skill_text = """【種族スキル】
                【生命+精神（基礎値）の合計を《改造点》とし、その改造点のぶんだけ自身を強化可能である。家柄71〜は改造点+15/家柄100は改造点+30/自身の改造点+20まで"超過"は可能だが、超過することで様々な〈サイバーエラー〉が生じる/ホットロード・サイボーグの全ステータスの上限は70】
                【改造要素一覧】
                ◉ステータス（筋力〜容姿）：ひとつのステータスを+1すると改造点-4
                ◉HP/MP：HP/MPのいずれかを+1すると改造点-2
                ◉限界突破（シナリオ/戦闘/ミッション中に原則1回のみ、1/2/3ターンの間パルクール〈技能値70〉が使用可能、回避+25、被ダメージ10%減、白兵武器による与ダメージ1.2倍、ただし限界突破が終了した場合は1ターン動けなくなる）】：取得に改造点-30/ターン数を増加させたい場合は改造点を更に-20（2ターン）/-30（3ターン）する
                ◉限界突破〈ホットロード〉特殊な限界突破が可能（シナリオ/戦闘/ミッション中に原則1回のみ、1/2ターンの間パルクール〈技能値70〉が使用可能、回避+30、被ダメージ20%減、白兵武器による与ダメージ1.4倍、ただし限界突破が終了した場合は3ターン動けなくなる）】：取得に改造点-40/ターン数を増加させたい場合は改造点を更に-40（2ターン）する
                部品暴走
                └適応外の部品を使用したことによるシステムの暴走を指す。ホットロード・サイボーグを選択したキャラクター作成終了後、1でも改造点を超過していた場合は精神ロール（基礎値）失敗でキャラロスト（クールタイムとして1日間キャラ作成不可。2度目の作成で本種族を選択してロストした場合、そのキャラクターでこの種族は二度と選択できない/また、一度ホットロードサイボーグでロストしてから再度選択した場合、家柄ダイスが1d70、ステータスダイスが1d25+5に変化する）/万一精神ロールに成功したとしても、ステータスの精神値が永続的に半減する"""
    elif race == "意識人造体（イニシエーター）":
            race_skill_text = """【種族スキル】
                モード・マキアが使用可能
                ♢モード・マキア
                └事前動作で自身のHP/MPを-30%する代わりに1ターンの間、攻撃命中+5（上限突破）&威力+15%/家柄71以上で発動時の攻撃威力+25%/家柄100以上で+35%/使用後はクールタイム5ターン）
                〈効果発動中に単発攻撃（重撃やバースト射撃ではない通常の一発攻撃）を行った場合、威力上昇ボーナスが+20%される（例：モードマキア発動中の家柄71未満威力+10%が+30%になる）〉
                ♢高機動フェーズ
                └イニシエーターの特徴として、助動作で高機動フェーズに移行することが可能。毎ターンスタミナを-50%する代わりに、自身へ回避値+10（限界突破はしない）・敵攻撃命中に基準値10を付与する(全体攻撃に対しては不可)/持続時間：家柄〜70:1ターン/家柄71〜:2ターン/家柄100：3ターン/使用終了後クールタイム6ターン
                ♢計画部隊
                └デトネーターと同じパーティーにいる状態で戦闘開始すると、HPとMPの上限が+20％される（上限値に応じて残量も合わせられる）"""
    elif race == "人工獣人":
            race_skill_text = """【種族スキル】
                白兵ダメージ+20%
                ♢造獣の怒り
                【精神限界-10で1ターンの間被ダメージ+100%/白兵攻撃ダメージ+50%（減少する精神限界の量を-30にすることで2ターンの間継続可能）/効果終了後3ターンのクールタイム】"""
    elif race == "強化人兵":
            race_skill_text = """【種族スキル】
                命中+2（上限突破）
                ♢超反射
                └改造された身体によって高度な反射回避を実現した。しかしその負荷は凄まじい
                【事前動作/精神限界-5で1ターンの間回避55固定/ターン終了後は2d10の固定ダメージ／一度使用すると、その戦闘では使用不可になるが〈アッドロウ〉が使用可能になる（兵器では使用不可）】
                ♢アッドロウ〈シングル〉
                └ADD-ROWとも呼ばれる強化人兵特有の能力。人間の脳は基本原則とて100%作動しており、かつて仮説として建てられたサイレントエリア説は現代では否定された。しかし、ADD-ROWはあえて脳にサイレントエリアを作り出し、そのエリアまで無理やり処理機能を拡充する技術である
                【回避+10（限界突破）/HP上限-10/MP上限-10/毎ターンHP-5/与ダメージ・被ダメージ+20%（兵器では使用不可）/2ターン経過でトワイスに移行】
                ♢アッドロウ〈トワイス〉
                └元々アッドロウは強化人兵にするにあたって失われた強化人間の機能を獲得するためのものだった。しかしアッドロウの危険度は想像を超えていた。シングル以上に踏み込めば途端に多くの廃人を生み出し、挙げ句には死亡者まで続出。だが、確実にアッドロウの性能が上がっていたことは確かだった。
                【回避+15（限界突破）/HP上限-15/MP上限-15/毎ターンHP-10/与ダメージ・被ダメージ+30%に更新（兵器では使用不可）/2ターン経過でスライスに移行】
                ♢アッドロウ〈スライス〉
                └スライスに追いつくことができたのはごく少数である。大半は息絶えるか、精神的に崩壊するだけだった。だが、この段階まで来ると体は限界をことごとく訴え始める。圧倒的な処理能力と引き換えに、確実に肉や血は煮えたぎり燃えていく
                【アッドロウの効果が回避+20（限界突破）/HP上限-20/MP上限-20/毎ターンHP-15/与ダメージ・被ダメージ+40%に更新（兵器では使用不可）/2ターン経過でクアドルプルに移行】
                ♢アッドロウ〈クアドルプル〉
                └生か死か。お前はもう分かっているはずだろう？眼の前の敵を殺すことに全力を尽くせ
                【アッドロウの効果が回避+25（限界突破）/クアドルプル到達時にHP・MP全回復/毎ターンHP-20/与ダメージ・被ダメージ+50%に更新（兵器は使用不可）/2ターン経過で戦闘不能】"""
    elif race == "羅刹":
            race_skill_text = """【種族スキル】
                ◉心羅刹
                └心の内に眠る羅刹が目覚め、すべてを殺すまでは止まることはない
                【咎が顕現した時点から次のターンに強制発動する。他の条件では一切発動しない。
                メリット/生存している間、全ての攻撃ダメージ+20%（家柄71以上：+30%/家柄100：+40%）&回避+2（家柄71以上：+4/家柄100：+6）&敵ダメージ-5%（家柄71以上：-10%/家柄100：-15%）&命中+2（家柄71以上：+4/家柄100：+6）
                デメリット/命中時、フィールドに居る自陣仲間と敵陣全てに対してランダムに見境なく攻撃を行う（仲間と敵を事前に数字付けして1d人数を行うことでランダム判定を行う）/敵を1体でも倒すとスキルが発動停止して次ターンから1ターンの間あらゆる行動不可】
                ―――――
                咎(トガ)
                〈羅刹の発動条件。種族選択時に必ず選択。一度選ぶと変更は不可。咎を決めた場合はそれに関連する事象を設定に書き込むこと。すべての必要ロールで出た数の合計値によって咎が決定する〉
                《必要ロールは全て1d12》
                必要ロール①
                〈夂〉
                5点：幼い頃に故郷を焼かれた
                6点：兄弟姉妹を全員殺された
                7点：親から道具として扱われた
                8点：奴隷として売り飛ばされた
                9点：奴隷扱いされた
                10点：自分が誰かもわからず、生きるために窃盗を繰り返した
                11点：誰かを自分の罪の身代わりにした
                12点：不義の子だった。生まれを望まれなかった
                必要ロール②
                〈人〉
                5点：出生のせいでそしられた
                6点：おぞましい扱いを受けた
                7点：両親にそしられた
                8点：見たくないものを見た
                9点：親に捨てられた
                10点：大切なものを失った
                11点：友人から棄てられた
                12点：消えない怪我を負った
                必要ロール③
                〈口〉
                5点：幼少期に人を殺した
                6点：言葉で人を貶めた
                7点：言葉巧みに人を騙し奪った
                8点：嘘をついて人を陥れた
                9点：自らのためならば他は礎に過ぎない
                10点：暴力を使って人から物を奪った
                11点：戦場で殺し合い、生き残った
                12点：弱き者から奪った
                ―――――
                15点：悪夢
                〈10以上の精神ダメージを受けると咎が顕現する/精神+5〉
                20点：悲痛
                〈自身のHP残量が10以下になると咎が顕現する/生命+5〉
                25点：狂乱
                〈自身のMP残量が10以下になると咎が顕現する/生命+5〉
                30点：血涙
                〈1ターンに自身のHPの80%以上ほダメージを受けると咎が顕現する/HP+5〉
                36点：慟哭
                〈自身のHPとMPが5以下になると咎が顕現する〉
                """
    elif race == "オートマタ":
            race_skill_text = """【種族スキル】
                ♢時計仕掛けの自動人形
                【事前動作でMPを30消費すると1ターンの間、攻撃力を+2d12%増加可能/高級時計を装備している場合、攻撃時のダメージが+1dされ、+3d12%に増加する。ただし、この特性の使用後はクールタイムによって3ターンのあいだ再使用が不可となる
                （例：ダイスロールで10が出た場合、ダメージ+10%）】
                ♢人形劇の幕間
                【戦闘中にMPが0になると動力不足によって即時戦闘不能になる/この特性を無効化する専用アクセサリーを装備している場合にのみ、MP0による戦闘不能を無効することができる】"""
    elif race == "アルラウネ":
            race_skill_text = """【種族スキル】
                QP家柄71未満+1/家柄71以上+2/家柄100+3
                ♢妖樹族
                【敵を攻撃したら与えたダメージの15%分を吸収する(例:敵に100ダメージを与えるとHPが15回復する/小数点以下切り捨て、種別は最終ダメージ)】
                ♢受け継がれし妖脈
                【レベルが上がるごとに容姿が+１、HPが+３されていく】
                ♢妖花の吸血
                【戦闘中に一度も吸血（技能値70固定/人間、獣人、亜人、半機人にのみ可能/HP+20%回復/助動作/クールタイム2ターン）をしていない場合、HPが50%以下になると2ターン以内に吸血をしなければ戦闘不能になってしまう／吸血を行うと1ターンの間攻撃ダメージが＋10%される/味方を吸血することは不可能】"""
    elif race == "デトネーター":
            race_skill_text = """【種族スキル】
                家柄〜70で防護点3、71〜99で防護点4、100で防護点5を常に持つ〈防護点3以上の服&防具装備不可〉
                射撃威力+5%/軽機関銃&機関銃威力+10%
                ♢モード・マキナ
                └助動作で発動した際、3ターンの間、自身のHP/MPを毎ターン+20%回復する/効果終了後、1ターン行動不可&クールタイム3ターン
                ♢超過戦闘フェーズ
                └デトネーターの特徴として、助動作で重戦闘フェーズに移行することが可能。毎ターンHPを-50%する代わりに、自身へ防御力200・自攻撃に対する敵回避に基準値10を付与する/持続時間：家柄〜70:1ターン/家柄71〜:2ターン/家柄100：3ターン/使用終了後クールタイム5ターン
                ♢計画部隊
                └イニシエーターと同じパーティーにいる状態で戦闘開始すると、HPとMPの上限が+20％される（上限値に応じて残量も合わせられる）
                """
    elif race == "スチームブッチャー":
            race_skill_text = """【種族スキル】
                回避基準値+10
                攻撃器具
                └スチームブッチャーの特徴ともいえるものが攻撃器具である。普段は取り外しているが、蒸気型器官を作動させた状態で義肢に装着して変形させると強力な武装へと変貌する
                〈択一選択式/使用技能は筋力判定/全て近接攻撃であり、使用動作は主動作〉
                ①ミンサー
                └ドリル型の攻撃器具。一つ一つの螺旋が堅固で鋭いナイフのようになっており、生半可な対象は細切れに切り裂き、強靭な対象には大穴を開ける万能型
                【威力2d10+白兵AB×1d6撃/敵防護点半減/最大+50%まで威力増加可能/連撃不可】
                ②シザー
                └ハサミ型の攻撃器具。重厚な刃で敵を挟み、容赦なく砕き斬ることを目的としている。多少の鉄材程度ならば破断可能
                【威力4d10+白兵AB/敵防御力半減/最大+100%まで威力増加可能/連撃可能（次撃以降、命中-20/連撃数増加不可）】
                ③クリーヴァー
                └包丁型の攻撃器具。刃渡りは1m半から2メートル前後と様々。剣先が平たい鉈のような形をしており、切れ味が特別秀でているわけではない。しかし他に比べて質量に優れており、そのまま対象へと無骨に叩きつけるだけでも凶悪な威力を発揮可能。また、この攻撃器具はスチームブッチャーたちにとっては最も古く、最も象徴的な存在である
                【威力6d10+白兵AB/ダメージを与えると、最終ダメージの1割を敵に衝撃ダメージとして与える/最大+150%まで威力増加可能/連撃不可】
                種族スキル
                ♢蒸気型器官〈作動〉
                【事前宣言したのち、1ターン後に発動/このスキルを発動して蒸気型器官を起動させることで、攻撃器具が使用可能となる/使用中は攻撃器具と片手武器（盾等防御装備を除く）以外使用不可能&1ターンにつきHP-10、スタミナ-1されていく/最大3ターンまで作動可能/ターン終了後はクールタイム3ターン】
                ♢冷却服
                【蒸気型器官〈作動〉が発動した場合、同時に発動する（動作不使用）/着用している防具、もしくは服の性能やスキル等すべての効果が無効化される（着用する形での準兵器等も含まれる）/発動時、防護点+5&防御力100を自身に付与】
                ♢強行突破
                【射撃武器を装備していない状態かつ、無武装もしくは近接武器を装備している状態の場合、敵に対しての接近判定が失敗しても、一回の戦闘で一度だけ基準値25で振り直すことが出来る（判定値が基準値以下の場合は振り直し不可）】
                """
    elif race == "怪異憑依者/怪人":
            race_skill_text = """【種族スキル】
            種族特性
            ♢憑異脈動
            └憑依した怪異の力を呼び起こす
            【助動作/発動時、選択した怪異の力を一定ターンの間使うことができる/発動時に精神限界-5】
            怪異一覧
            （家柄2以上70以下はLv1まで、家柄71以上はLv2まで、家柄100と家柄1はLv3までの怪異を選択可能／怪異は一つのみ選択可能で、変更できない）
            ♢羽虫/Lv1
            └羽の生えた貧相な虫の類。非力だが、すばやい
            【有利効果：2ターンの間、回避+5（上限突破）&回避時のスタミナ消費を0にする/不利効果：被ダメージ+20%/効果終了後、2ターンのクールタイム】
            ♢蠕虫/Lv1
            └不気味な芋虫の類。非力だが、しぶとい
            【有利効果：1ターンの間、50未満の最終ダメージを無効化する/不利効果：50以上の最終ダメージを受けると残りHPと防御性能にかかわらず戦闘不能になる/効果終了後、2ターンのクールタイム】
            ♢毒虫/Lv2
            └醜悪な虫の類。ひりつくような毒を持つ
            【有利効果：2ターンの間、自身が敵に与えたダメージは回復不可ダメージになる（累計で最大100ダメージまで）/不利効果：効果ターン中に受けたダメージは回復不可になる/効果終了後、2ターンのクールタイム】
            ♢蛾/Lv2
            └目を見開いたような羽を持つ蝶になれなかったモノ。贋物なりの力はある
            【有利効果：2ターンの間、ターン開始時にHPとMPを20%ずつ再生する/不利効果：効果ターン中の被ダメージ+20%/効果終了後、2ターンのクールタイム】
            ♢鼬/Lv2
            └獣の怪異は虫よりも凶悪である。うまく御せねば、喰われるは己である
            【有利効果：2ターンの間、20未満の最終ダメージを無効化し、攻撃を与えてきた敵に対する攻撃力+10%/不利効果：発動ターン中、1ターンごとに精神限界-10%/効果終了後、2ターンのクールタイム】
            ♢黒蝶/Lv3
            └黒色の羽根を持つ蝶。その舞に酔い痴れぬように
            【有利効果：2ターンの間、ターン開始時にHPとMPを10%ずつ再生し、回避時のスタミナ消費を0にする/不利効果：効果ターン中の被ダメージ+20%&命中基準値+10/効果終了後、2ターンのクールタイム】
            ♢細蠍/Lv3
            └細身の蠍。小なれど、鋏と尾針は射貫く力を持つ
            【有利効果：2ターンの間、敵物理防護点と物理防御力を半減する（既に半減される攻撃には適用されない）/不利効果：効果ターン中の命中基準値+20/効果終了後、2ターンのクールタイム】
            ♢貂/Lv3
            └獣の怪異は虫よりも凶悪である。ましてやこの獣は、甘く見るには凶暴が過ぎる
            有利効果：2ターンの間、30未満の最終ダメージを無効化し、攻撃を与えてきた敵に対する攻撃力+20%/不利効果：発動ターン中、1ターンごとに精神限界-20%/効果終了後、2ターンのクールタイム】"""

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
        for k in ["体格", "生命", "容姿", "知力", "俊敏"]: stats[k] += 1
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
    if past1 == "⑤特別": add_stats_group(1)
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
        elif bg == "放浪戦士": mod_stamina += 2; bonus_ab_melee += 1; mod_evasion += 5
        elif bg in ["侍", "双剣士", "銃剣士"]: bonus_sp += 70
        elif bg == "商人": stats["商才"] += 10; bonus_sp += 30
        elif bg == "淑女":
            if gender != "女": warning_errors.append("⚠️【淑女】性別「女」専用です")
            if p.get('is_lady_contracted', False):
                bonus_sp += 100; stats["容姿"] += 6; mod_hp += 10; mod_mp += 10; mod_stamina += 2
                warning_errors.append(f"💡【淑女】相手(男性)との家柄差は±5以内の必要があります(自身の家柄:{lineage})。")
            else:
                warning_errors.append("💡【淑女】男性と契約を行うまで、技能Pなどの恩恵は適用されません。")
        elif bg == "通常使用人": 
            stats["容姿"] += 3; stats["知力"] += 3; bonus_sp += 70; mod_mp += 5
            if p.get('is_servant_mastered', False): mod_mp += 5
            if p.get('is_steward', False): mod_mp += 5
        elif bg == "戦闘使用人": 
            stats["容姿"] += 3; stats["知力"] += 3; bonus_sp += 70; mod_hp += 5
            if p.get('is_servant_mastered', False): mod_hp += 5
            if p.get('is_steward', False): mod_hp += 5
        elif bg == "多重人格者": mod_mp += 5; bonus_sp += 30
        elif bg == "対偶者": 
            bonus_sp += 35; stats["容姿"] += 2
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
            if bg_sub == "使用人":
                bonus_sp += 120; mod_mp += 5
                if p.get('is_servant_mastered', False): mod_mp += 5
                if p.get('is_steward', False): mod_mp += 5
            elif bg_sub == "戦闘使用人":
                bonus_sp += 120; mod_hp += 5
                if p.get('is_servant_mastered', False): mod_hp += 5
                if p.get('is_steward', False): mod_hp += 5
        elif bg == "官吏": bonus_sp += 150; stats["精神"] += 6
        elif bg == "医者": bonus_sp += 70; stats["知力"] += 6; mod_hp += 3; mod_mp += 5
        elif bg == "淑女":
            if gender != "女": warning_errors.append("⚠️【淑女】性別「女」専用です")
            if p.get('is_lady_contracted', False):
                bonus_sp += 150; stats["容姿"] += 6; mod_hp += 10; mod_mp += 10; mod_stamina += 2
                warning_errors.append(f"💡【淑女】相手(男性)との家柄差は±5以内の必要があります(自身の家柄:{lineage})。")
            else:
                warning_errors.append("💡【淑女】男性と契約を行うまで、技能Pなどの恩恵は適用されません。")
        elif bg == "多重人格者": mod_mp += 5; bonus_sp += 30
        elif bg == "警官":
            if bg_sub == "警官": bonus_sp += 70; mod_hp += 10; warning_errors.append("💡【警官】指定ステータスに+8手動で割り振ってください。")
            elif bg_sub == "汚職警官": bonus_sp += 120; mod_hp += 5; warning_errors.append("💡【汚職警官】指定ステータスに+5手動で割り振ってください。")
        elif bg == "無法者":
            if bg_sub == "ギャング": bonus_sp += 50; mod_hp += 5; stats["筋力"] += 5
            elif bg_sub == "マフィア": bonus_sp += 70; bonus_ab_melee += 3; mod_mp += 5; stats["筋力"] += 2
        elif bg == "対偶者": 
            bonus_sp += 35; stats["容姿"] += 2
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
                job_texts.append("忍Lv0: 忍術【魔導剣&脇差威力+20% / 回避+2(突破)】"); eva_limit_break += 2
                if job2_lv >= 1: job_texts.append("忍Lv1: 手投げ術【投擲使用時、威力+50%】")
                if job2_lv >= 2: job_texts.append("忍Lv2: 忍術強化【魔導剣&脇差威力+30% / 回避+3】"); eva_limit_break += 3
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
            nonlocal mod_mp, mod_hp, mod_stamina, bonus_mental, mod_evasion
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
                if lv >= 2: job_texts.append("回避+2"); mod_evasion += 2
                if lv >= 3: job_texts.append("戦技『襲撃』(命中-20, 与ダメ+20%/CT3)")
            elif job_name == "強奪者":
                if lv >= 1: mod_stamina += 2
                if lv >= 2: job_texts.append("回避+2"); mod_evasion += 2
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
                if lv >= 0: job_texts.append("戦技『強襲格闘』(近接+10%, 接近+5, 回避-10)"); mod_evasion -= 10
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
                if job2_lv >= 2: job_texts.append("回避+3"); mod_evasion += 3
                if job2_lv >= 3: job_texts.append("戦技『略奪』(ダメ半分ドレイン/CT6)")
                if job2_lv >= 4: mod_hp += 5
            elif job2 == "強襲兵":
                check_job_req_noc("歩兵")
                if job2_lv >= 1: mod_mp += 3
                if job2_lv >= 2: job_texts.append("回避+2"); mod_evasion += 2
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
                if stance_lv >= 1: fan_sys_texts.append("【天の構え】威力+30% / 被ダメ+30% / 回避-10"); mod_evasion -= 10
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
                if stance_lv >= 1: fan_sys_texts.append("【蜻蛉の構えLv1】(※発声必須) 初撃威力+30% / 被ダメ+30% / 回避-5"); mod_evasion -= 5
                if stance_lv >= 2: fan_sys_texts.append("【蜻蛉の構えLv2】初撃威力+10% / 被ダメ+10% / 回避-5 (累積)"); mod_evasion -= 5
                if stance_lv >= 3: fan_sys_texts.append("【蜻蛉の構えLv3】初撃威力+10% / 被ダメ+10% / 回避-5 (累積)"); mod_evasion -= 5
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
            elif s2 == "スルース": noc_sys_texts.append(f"【2層: {s2}】回避+1(上限突破) / 隠れる初期値+10"); mod_evasion += 1
            elif s2 == "アンダーリング": mod_hp += 5; noc_sys_texts.append(f"【2層: {s2}】名声-1 / 解錠or盗み初期値+20")
            elif s2 == "オブザーバー": mod_mp += 5; noc_sys_texts.append(f"【2層: {s2}】捜索初期値+15")
        if s3 != "(なし)":
            if lvl_num < 4: warning_errors.append("⚠️【スペシャリスト】第3層の解放にはLv4以上が必要です。")
            if s3 == "突撃兵": noc_sys_texts.append(f"【3層: {s3}】戦技『突撃』取得(2T被ダメ+100%,回避-20/1T与ダメ+50%/CT10)")
            elif s3 == "機動偵察兵": mod_hp += 5; noc_sys_texts.append(f"【3層: {s3}】古びた偵察バイク入手")
            elif s3 == "選抜射手": noc_sys_texts.append(f"【3層: {s3}】対物狙撃銃威力+20% / マークスマンライフル使用可")
            elif s3 == "特殊工作兵": noc_sys_texts.append(f"【3層: {s3}】対人ダメ+10%, 被ダメ-5%, 対兵器ダメ+10%(重兵器時)")
            elif s3 == "潜入兵": noc_sys_texts.append(f"【3層: {s3}】サプレッサー威力+15% / 潜入戦闘服装備可 / 回避+5"); mod_evasion += 5
            elif s3 == "空挺兵": noc_sys_texts.append(f"【3層: {s3}】落下ダメ-50%, 装備弾倉数+2, 回避+5, 被ダメ-10%"); mod_evasion += 5
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
            elif s4 == "潜入兵Lv2": noc_sys_texts.append(f"【4層: {s4}】(※1層上書)サプレッサー威力+30% / 回避+7"); mod_evasion += 7
            elif s4 == "空挺兵Lv2": noc_sys_texts.append(f"【4層: {s4}】(※1層上書)落下ダメ-60%, 装備弾倉数+3, 回避+5, 被ダメ-20%"); mod_evasion += 5
            elif s4 == "コンドッティエーレ": mod_hp += 10; mod_mp += 10; noc_sys_texts.append(f"【4層: {s4}】(※3層上書)与ダメージ+20% / 被ダメージ-10%")
            elif s4 == "ハイランダー": mod_hp -= 30; noc_sys_texts.append(f"【4層: {s4}】近接武器ダメ+40%, 銃撃ダメ+20%, 被ダメ+40%")
            elif s4 == "コンキスタドール": mod_hp += 5; mod_mp -= 30; noc_sys_texts.append(f"【4層: {s4}】索敵+5(突破) / 回避+5 / 被ダメ-10% / 銃撃ダメ+20%"); mod_evasion += 5
            elif s4 == "グラディエーター": noc_sys_texts.append(f"【4層: {s4}】近接連撃回数+1 / 近接武器ダメージ+10%")
            elif s4 == "ティーガー": mod_hp += 10; mod_mp += 10; mod_stamina += 2; noc_sys_texts.append(f"【4層: {s4}】重機関銃装備可 / 被ダメージ-10% / 回避-20"); mod_evasion -= 20
            elif s4 == "アルチザン": noc_sys_texts.append(f"【4層: {s4}】アイテム製作技能値+5(突破) / 製作アイテム耐久値+10%")
            elif s4 == "ローリエット": noc_sys_texts.append(f"【4層: {s4}】上級芸術技能解禁 / 1つ初期値35で取得可(要:通常芸術70)")
            elif s4 == "プロフェッサー": mod_mp += 10; bonus_mental += 10; noc_sys_texts.append(f"【4層: {s4}】70以上の高等技能値+5(突破)")
            elif s4 == "ノワール・リミエ": bonus_mental += 15; noc_sys_texts.append(f"【4層: {s4}】白兵+20%, 射撃+10%, 防護点+1 / 先手時1T目ダメ補正+2(1発毎)")
            elif s4 == "エセクトーレ": mod_hp += 5; mod_mp += 5; noc_sys_texts.append(f"【4層: {s4}】名声-5以降-1毎に白兵威力+5%(最大25%) / 白兵ダメの5%HP吸収")
            elif s4 == "アウフゼーア": mod_mp += 10; noc_sys_texts.append(f"【4層: {s4}】敵回避基準+5常時 / 命中時敵分析進行(毎T被ダメ-5%, 最大-20%)")
            
        
    # ==========================================
    # 製作系ジョブの処理（必ず最終計算より上に置く！）
    # ==========================================
    if origin == "ファンタジア":
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
        job_craft2_lv = str(p.get('job_craft2_lv', '0'))

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
            
            mod_stamina += 1 
            
            job_texts.append("匠Lv0: 疲れ知らず【修理回数+2 / スタミナ+1】")
            if job_craft2_lv >= "1": job_texts.append("匠Lv1: 効率修理強化【クリティカル時回復値+1】")
            if job_craft2_lv >= "2": job_texts.append("匠Lv2: 熟練採取強化【1日2回幸運成功で獲得物+1】")
            if job_craft2_lv >= "3": job_texts.append("匠Lv3: 最短採取【採取スタミナ消費半減】")
            if job_craft2_lv >= "4": job_texts.append("匠Lv4: 名工【補正半減 / 1日1回ロスト防止】")
    # ==========================================
    
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
    mod_evasion += sub_eva_mod
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
                
    # ==========================================
    # 加護・血契の処理
    # ==========================================
    blessing_str = p.get('blessing', '(なし)')
    blessing = blessing_str       # 一番下のプロフィールテキスト表示用
    blessing_text_out = ""        # 加護の効果テキスト表示用
    is_blessing_active = False    # スタミナ計算用のスイッチ
    
    is_exception = (stats.get("信仰", 0) >= 55 or sub_stats.get("神聖", 0) >= 17)

    if blessing_str != "(なし)":
        # ... 以下、今書かれているコードをそのまま残す
        # 血契のリスト
        list_blood_covenant = [
            "金紅神の加護 (血契)", "屍王神の加護 (血契)", "魔血神の加護 (血契)", 
            "魔狼神の加護 (血契)", "魔炎神の加護 (血契)", "魔鬼神の加護 (血契)"
        ]
        
        # 誓いの加護（HP/MP補正データ）
        oath_bonus = {
            "氷影神の加護": {"mod_hp": 2, "mod_mp": 5},
            "水輝神の加護": {"mod_hp": 0, "mod_mp": 7},
            "夜影神の加護": {"mod_hp": 7, "mod_mp": 0},
            "炎輝神の加護": {"mod_hp": 0, "mod_mp": 7},
            "地影神の加護": {"mod_hp": 5, "mod_mp": 2},
            "風影神の加護": {"mod_hp": 3, "mod_mp": 3},
            "雷影神の加護": {"mod_hp": 3, "mod_mp": 5},
            "雪神の加護": {"mod_hp": 2, "mod_mp": 2},
            "花神の加護": {"mod_hp": 10, "mod_mp": 0},
        }

        # 【A】血契の処理（種族制限なしで素通り！）
        if blessing_str in list_blood_covenant:
            # ここに血契ごとの数値を直接書いていく
            if blessing_str == "金紅神の加護 (血契)":
                mod_mp += 10
            elif blessing_str == "屍王神の加護 (血契)":
                mod_mp += 10
            elif blessing_str == "魔血神の加護 (血契)":
                mod_mp += 10
            elif blessing_str == "魔狼神の加護 (血契)":
                mod_hp += 10
            elif blessing_str == "魔炎神の加護 (血契)":
                mod_hp += 5; mod_mp += 5
            elif blessing_str == "魔鬼神の加護 (血契)":
                mod_hp += 10; mod_stamina += 2
                
            blessing_text_out = f"【血契】{blessing_str}適用"

        # 【B】誓いの加護の処理（魔族・呪族の制限あり）
        else:
            if is_demon:
                warning_errors.append(f"⚠️ 【加護エラー】{blessing_str}は魔族は使用できません。")
            elif is_cursed and not is_exception:
                warning_errors.append(f"⚠️ 【加護エラー】{blessing_str}の追加効果は呪族には効果がありません（信仰・神聖不足）。")
            else:
                # 1. HP/MP補正の適用
                data = oath_bonus.get(blessing_str, {})
                mod_hp += data.get("mod_hp", 0)
                mod_mp += data.get("mod_mp", 0)
                
                # 2. ♢効果（特殊ステータス補正など）の適用
                if blessing_str == "水輝神の加護":
                    stats["商才"] += 5
                elif blessing_str == "風影神の加護":
                    mod_evasion += 2
                elif blessing_str == "雷影神の加護":
                    mod_evasion -= 5
                
                blessing_text_out = f"【加護】{blessing_str}適用"
                
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

    # === フリー手入力バフの加算 ===
    val_extra_hp = p.get('extra_hp', 0)
    val_extra_mp = p.get('extra_mp', 0)
    val_extra_stamina = p.get('extra_stamina', 0)
    val_extra_evasion = p.get('extra_evasion', 0)
    val_extra_text = p.get('extra_text', "")

    mod_hp += val_extra_hp
    mod_mp += val_extra_mp
    mod_stamina += val_extra_stamina
    mod_evasion += val_extra_evasion

    # === アビリティによるステータス加算 ===
    val_skill = p.get('skill', '(なし)')
    val_martial = p.get('martial', '(なし)')
    val_craft = p.get('craft', '(なし)')

    # キャラクターレベル制限の判定用辞書 (Lv1: キャラクタLv2以上, Lv2: Lv4以上...)
    req_lv_dict = {1: 2, 2: 4, 3: 6, 4: 7}

    def check_and_get_lv(name, val_str):
        if "Lv1" in val_str: lv = 1
        elif "Lv2" in val_str: lv = 2
        elif "Lv3" in val_str: lv = 3
        elif "Lv4" in val_str: lv = 4
        else: return 0
        
        # レベル制限エラーチェック (lvl_num はキャラクターレベル)
        req_lv = req_lv_dict[lv]
        if lvl_num < req_lv:
            warning_errors.append(f"⚠️【アビリティ条件未達】{name}Lv{lv}の取得にはキャラクターLv{req_lv}以上が必要です（現在Lv{lvl_num}）。")
        return lv

    # 画面の選択からLv（0〜4）を取得
    sk_lv = check_and_get_lv("技力", val_skill)
    ma_lv = check_and_get_lv("武芸", val_martial)
    cr_lv = check_and_get_lv("工芸", val_craft)

    # 1. 技量（技力）の処理
    if sk_lv == 1: mod_mp += 10; bonus_sp += 10
    elif sk_lv == 2: mod_mp += 15; bonus_sp += 20
    elif sk_lv == 3: mod_mp += 20; bonus_sp += 30
    elif sk_lv == 4: mod_mp += 25; bonus_sp += 40

    # 2. 武芸の処理
    if ma_lv == 1: mod_hp += 5; bonus_sp += 10
    elif ma_lv == 2: mod_hp += 10; bonus_sp += 20
    elif ma_lv == 3: mod_hp += 15; bonus_sp += 30
    elif ma_lv == 4: mod_hp += 16; bonus_sp += 40  # ※武芸Lv4はHP+16

    # 3. 工芸の処理
    if cr_lv == 1: mod_stamina += 1; bonus_sp += 10
    elif cr_lv == 2: mod_stamina += 2; bonus_sp += 20
    elif cr_lv == 3: mod_stamina += 3; bonus_sp += 30
    elif cr_lv == 4: mod_stamina += 4; bonus_sp += 40

    # 技能上限の計算（持っているアビリティの中で最大のLvを参照）
    max_ab_lv = max(sk_lv, ma_lv, cr_lv)
    skill_cap = 70 + (max_ab_lv * 5) if max_ab_lv > 0 else 70
    # ==========================================

    # --- 最終計算 ---
    final_hp = (stats["生命"] + stats["体格"]) // 5 + mod_hp
    final_mp = (stats["知力"] + stats["精神"]) // 5 + mod_mp
    if is_atoning_blood:
        final_hp = int(final_hp * 0.8)
        final_mp = int(final_mp * 0.8)
    if race == "強化演算体": 
        final_hp = int(final_hp * 0.7)
    if race == "演算異常体": 
        final_hp = int(final_hp * 0.7)
    shield_hp_str = ""
    final_stamina = (stats["敏捷"] + stats["生命"]) // 10 + mod_stamina
    if is_blessing_active:
        if blessing_str == "雪神の加護":
            shield_hp_str = f" (＋庇護HP: {int(final_hp * 0.3)})"
        if blessing_str in ["地影神の加護", "風影神の加護"]:
            final_stamina = max(1, final_stamina - 3)
    if race == "炉心異常体": 
        final_stamina //= 2
    # 1. 基礎値（敏捷の50%）
    base_evasion = stats["敏捷"] // 2
    # 2. 通常補正を足して、上限50でストップ
    total_evasion = base_evasion + mod_evasion
    if total_evasion > 50:
        total_evasion = 50    
    # 3. 最後に「突破」分を上乗せする
    final_evasion = total_evasion + eva_limit_break
    luck = min(50, (sum([stats["筋力"], stats["知力"], stats["敏捷"], stats["精神"], stats["体格"], stats["生命"], stats["容姿"]]) // 10) + mod_luck)
    faint = (stats["生命"] + stats["体格"] + stats["精神"]) // 5
    depend = (stats["精神"] + stats["知力"]) // 10
    base_sp = sum([stats["筋力"], stats["知力"], stats["敏捷"], stats["精神"], stats["体格"], stats["生命"], stats["容姿"], stats["芸術"], stats["商才"]])
    final_mental = stats['精神']
    if race in ["強化演算体"]: final_mental -= 15
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
    attr_sys_section = ""
    if attr_sys_texts: attr_sys_section = f"\n【属性特性】\n" + "\n".join(attr_sys_texts) + "\n"

    result_text = f"""【プロフィール】
星: {origin}　|　種族: {race}{sub_text}
属性: {attr_text}　|　家柄: {lineage}
出自: {bg}{bg_sub_text}　|　加護: {blessing}

{race_skill_text}

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
回避: {final_evasion}
気絶点: {faint}
技能上限: {skill_cap} 

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
{fan_sys_section}{noc_sys_section}{sub_section}{attr_sys_section}{blessing_section}{extra_buff_section}"""

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
        # 🌟 ストッパー：直前に読み込んだファイル名と違う時だけ処理をする
        if st.session_state.get("loaded_filename") != uploaded.name:
            try:
                raw = json.load(uploaded)
                for k, v in raw.items():
                    st.session_state[k] = v
                
                # 「このファイルを読み込んだよ」という記録を残す
                st.session_state["loaded_filename"] = uploaded.name
                
                # ここで1回だけ画面をリロードする！
                st.rerun()
                
            except Exception as e:
                st.error(f"読み込みエラー: {e}")
        else:
            # すでに読み込みが終わっている場合は、完了メッセージだけを出し続ける
            st.success("✅ 読み込み完了！")

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
    st.markdown("### 🤝 絆・契約ステータス")
    
    if bg == "淑女":
        st.checkbox("☑ 男性と契約している", value=st.session_state.get('is_lady_contracted', False), key='is_lady_contracted')
    elif bg == "対偶者":
        st.checkbox("☑ 対偶者（パートナー）がいる", value=st.session_state.get('is_partnered', False), key='is_partnered')
    elif bg in ["通常使用人", "戦闘使用人", "使用人"]:
        sm = st.checkbox("☑ 仕える主人がいる", value=st.session_state.get('is_servant_mastered', False), key='is_servant_mastered')
        if sm:
            st.checkbox("☑ 「家令」に任命されている", value=st.session_state.get('is_steward', False), key='is_steward')
        st.checkbox("☑ 対偶者（パートナー）がいる", value=st.session_state.get('is_partnered', False), key='is_partnered')

    list_other_bond = ["(なし)", "誰かの対偶相手", "淑女の契約相手", "使用人の主人", "使用人の主人(家令任命)"]
    st.selectbox("他PCからの関係付与 (自分が相手側の場合)", list_other_bond, index=si('other_bond', list_other_bond), key='other_bond')

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

    if origin == "ファンタジア":
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
    st.markdown("### 🏠 クラン・エシュロン・その他バフ（手入力）")
    st.caption("※クランハウスの家具効果、ハウジングなどのPLや所属によって変動するバフはこちらに入力してください。")

    col_ex1, col_ex2 = st.columns(2)
    with col_ex1:
        st.number_input("追加HP", value=st.session_state.get('extra_hp', 0), step=1, key='extra_hp')
        st.number_input("追加スタミナ", value=st.session_state.get('extra_stamina', 0), step=1, key='extra_stamina')
    with col_ex2:
        st.number_input("追加MP", value=st.session_state.get('extra_mp', 0), step=1, key='extra_mp')
        st.number_input("追加回避（通常）", value=st.session_state.get('extra_evasion', 0), step=1, key='extra_evasion')

    st.text_input("その他追加能力・テキスト", value=st.session_state.get('extra_text', ""), key='extra_text', placeholder="例:クランハウス内でのみ料理技能+30")

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
                       'job1_1', 'job1_1_lv', 'job1_2', 'job1_2_lv','job_craft2', 'job_craft2_lv',
                       'job2', 'job2_lv', 'skill', 'martial', 'craft',
                       'stance', 'stance_lv', 'school',
                       'spec_route', 'spec_1', 'spec_2', 'spec_3', 'spec_4'
                       'is_lady_contracted', 'is_partnered', 'is_servant_mastered', 'is_steward', 'other_bond',
                       'extra_hp', 'extra_mp', 'extra_stamina', 'extra_evasion', 'extra_text',
                       'job_craft1_1', 'job_craft1_1_lv', 'job_craft1_2', 'job_craft1_2_lv', 'job_craft2', 'job_craft2_lv']
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
