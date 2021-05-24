from pyecharts.charts import Line
import pyecharts.options as opts
import os
import csv
import time
from itertools import islice

'''
Todo
天数判断
'''

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

    # add
    date_list = {}
    switch_weapon = 0
    switch_hero = 1
    for user in datebase:
        for roll in user[2]:

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
            gacha_time = time.strptime(roll[0], t_formats)
            gacha_stamp = int(time.mktime(gacha_time))
            for i in range(len(start_times)):
                start_stamp = int(time.mktime(
                    time.strptime(start_times[i], t_formats)))
                end_stamp = int(time.mktime(
                    time.strptime(end_times[i], t_formats)))
                if(gacha_stamp - start_stamp >= 0 and end_stamp-gacha_stamp >= 0):
                    # 确定池子
                    diff_time = gacha_stamp-start_stamp
                    days_passed = int(diff_time/86400)
                    # print(diff_time)
                    if(i in date_list):
                        if(days_passed in date_list[i]):
                            date_list[i][days_passed] += 1
                        else:
                            date_list[i][days_passed] = 1
                    else:
                        date_list[i] = {}

    print(date_list)


# 绘制表格

def sort_(date):
    ret = []
    for i in sorted(date.items(), key=lambda x: x[0], reverse=False):
        ret.append(i[1])
    return ret

def get_x(date: dict):
    max_len = 0
    for i in date.values():
        dict_len = len(i)
        if(dict_len > max_len):
            max_len = dict_len

    list = []
    for i in range(max_len):
        list.append('第'+str(i+1)+'天')
    return list

line = Line()
line.add_xaxis(xaxis_data=get_x(date_list))
for key in date_list.keys():
    line.add_yaxis(
        series_name=up_characters[key][3],
        y_axis=sort_(date_list[key]),
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )

line.set_global_opts(title_opts=opts.TitleOpts(title="抽卡数量表"))
line.render("Q5抽卡习惯表.html")
