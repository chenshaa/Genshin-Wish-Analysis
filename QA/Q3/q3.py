import os
import csv
import time
from itertools import islice


def test(date, hero):
    t_formats = '%Y-%m-%d %H:%M:%S'
    # 1     2      3     4      5       6      7   8      9     10     11
    # 温迪池 可莉池 公子池 钟离池 阿贝多池 甘雨池 魈池 刻晴池 胡桃池 温迪池 公子池
    start_times = ['2020-09-28 00:00:00', '2020-10-20 18:00:00', '2020-11-09 22:00:00', '2020-12-01 18:00:00',
                   '2020-12-22 18:00:00', '2021-01-12 18:00:00', '2021-02-02 18:00:00', '2021-02-17 18:00:00',
                   '2021-03-02 18:00:00', '2021-03-17 06:00:00', '2021-04-06 18:00:00']

    end_times = ['2020-10-18 17:59:59', '2020-11-09 17:59:59', '2020-12-01 15:59:59', '2020-12-22 14:59:59',
                 '2021-01-12 15:59:59', '2021-02-02 14:59:59', '2021-02-17 15:59:59', '2021-03-02 15:59:59',
                 '2021-03-16 14:59:59', '2021-04-06 15:59:59', '2021-04-27 14:59:59']

    up_characters = [['芭芭拉', '菲谢尔', '香菱', '温迪'], ['行秋', '诺艾尔', '砂糖', '可莉'], ['迪奥娜', '北斗', '凝光', '达达利亚'],
                     ['辛焱', '雷泽', '重云', '钟离'], ['菲谢尔', '砂糖',
                                                '班尼特', '阿贝多'], ['香菱', '行秋', '诺艾尔', '甘雨'],
                     ['迪奥娜', '北斗', '辛焱', '魈'], ['凝光', '班尼特',
                                                '芭芭拉', '刻晴'], ['行秋', '重云', '香菱', '胡桃'],
                     ['砂糖', '雷泽', '诺艾尔', '温迪'], ['罗莎莉亚', '芭芭拉', '菲谢尔', '达达利亚']]
    gacha_time = time.strptime(date, t_formats)
    gacha_stamp = int(time.mktime(gacha_time))
    for i in range(len(start_times)):
        start_stamp = int(time.mktime(
            time.strptime(start_times[i], t_formats)))
        end_stamp = int(time.mktime(time.strptime(end_times[i], t_formats)))
        if(gacha_stamp - start_stamp >= 0 and end_stamp-gacha_stamp >= 0):
            if(hero in up_characters[i]):
                return 0
            else:
                return 1


if __name__ == '__main__':
    datebase = []
    base_folder = os.path.join(
        os.getcwd(), 'GI_gacha_dataset-main', 'GI_gacha_dataset_02')
    file_list = os.listdir(base_folder)
    file_names = ['gacha100.csv', 'gacha200.csv',
                  'gacha301.csv', 'gacha302.csv']
    for user_folder in file_list:
        datebase_temp = []
        for roll in file_names:
            folder = os.path.join(base_folder, user_folder, roll)
            if(os.path.exists(folder)):
                f = csv.reader(
                    open(os.path.join(base_folder, user_folder, roll), encoding='UTF-8'))
                rolls_temp = []
                for i in islice(f, 1, None):
                    rolls_temp.append(i)
            datebase_temp.append(rolls_temp)
        datebase.append(datebase_temp)

    hero_list = {}
    switch_weapon = 1
    switch_hero = 1
    for user in datebase:
        for roll in user[2]:
            if(roll[3] == '5' or roll[3] == '4'):
                # 抽出五星/四星
                if(roll[2] == '武器' and switch_weapon):
                    # 筛选武器
                    if(test(roll[0], roll[1])):
                        # 判断是否是歪的
                        if(roll[1] in hero_list):
                            hero_list[roll[1]] += 1
                        else:
                            hero_list[roll[1]] = 1
                if(roll[2] == '角色' and switch_hero):
                    # 筛选角色
                    if(test(roll[0], roll[1])):
                        # 判断是否是歪的
                        if(roll[1] in hero_list):
                            hero_list[roll[1]] += 1
                        else:
                            hero_list[roll[1]] = 1

    print(hero_list)

    from pyecharts import options as opts
    from pyecharts.charts import WordCloud

    (
        WordCloud()
        .add(series_name="数量", data_pair=hero_list.items())
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="常驻统计", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        .render("Q3常驻统计.html")
    )
