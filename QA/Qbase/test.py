from pyecharts.charts import Bar
from pyecharts import options as opts
import os
import csv
from itertools import islice

if __name__ == '__main__':
    datebase = []
    base_folder = os.path.join(
        os.getcwd(), 'GI_gacha_dataset-main', 'GI_gacha_dataset_02')
    file_list = os.listdir(base_folder)
    file_names = ['gacha100.csv', 'gacha200.csv',
                  'gacha301.csv', 'gacha302.csv']
    for user in file_list:
        datebase_temp = []
        for gacha in file_names:
            folder = os.path.join(base_folder, user, gacha)
            if(os.path.exists(folder)):
                f = csv.reader(
                    open(os.path.join(base_folder, user, gacha), encoding='UTF-8'))
                rolls_temp = []
                for i in islice(f,1,None):
                    rolls_temp.append(i)
                datebase_temp.append(rolls_temp)
        datebase.append(datebase_temp)
    #print(datebase)

#file_names = ['gacha100.csv', 'gacha200.csv', 'gacha301.csv', 'gacha302.csv']  # 新手池/常驻池/角色池/武器池
date_list={0: {1: 1540, 2: 725, 3: 1200, 7: 1079, 11: 231, 19: 650, 4: 640, 6: 780, 8: 320, 10: 302, 14: 756, 0: 7023, 5: 1024, 12: 249, 13: 304, 9: 357, 18: 284, 15: 618, 16: 709, 17: 71, 20: 83}, 1: {7: 749, 0: 5004, 5: 405, 9: 70, 12: 425, 13: 532, 17: 590, 15: 376, 16: 233, 1: 523, 2: 282, 4: 333, 8: 72, 10: 256, 3: 505, 6: 491, 11: 1437, 14: 251, 18: 177, 19: 190}, 2: {2: 1612, 9: 538, 10: 235, 14: 483, 15: 304, 1: 5204, 4: 353, 7: 273, 13: 159, 16: 89, 0: 112, 3: 649, 5: 259, 6: 251, 8: 231, 11: 263, 17: 161, 18: 257, 21: 187, 12: 777, 20: 175, 19: 219}, 4: {8: 118, 1: 2040, 3: 380, 4: 269, 10: 289, 15: 48, 5: 317, 6: 77, 2: 833, 9: 331, 11: 337, 13: 80, 17: 133, 19: 314, 20: 93, 0: 3708, 7: 471, 16: 85, 14: 294, 18: 186, 12: 112}, 5: {0: 12058, 2: 825, 1: 467, 3: 447, 6: 761, 8: 131, 9: 1039, 10: 378, 17: 342, 19: 421, 7: 326, 16: 256, 20: 352, 4: 427, 5: 546, 11: 167, 18: 225, 12: 590, 13: 249, 14: 245, 15: 176}, 6: {0: 5562, 1: 2481, 4: 215, 2: 781, 3: 901, 5: 345, 9: 104, 14: 815, 6: 199, 7: 172, 8: 265, 10: 210, 12: 239, 13: 105, 11: 100}, 3: {2: 643, 3: 410, 12: 235, 15: 75, 19: 466, 0: 6670, 20: 386, 1: 633, 4: 417, 5: 918, 6: 814, 7: 152, 9: 817, 10: 360, 11: 827, 18: 706, 8: 269, 13: 129, 14: 29, 16: 163, 17: 161}, 7: {0: 1524, 1: 90, 2: 91, 3: 73, 7: 23, 4: 34, 5: 169, 6: 29, 8: 83, 9: 20, 11: 30, 12: 8, 10: 59}, 8: {0: 3441, 10: 13, 11: 560, 13: 10, 1: 178, 2: 63, 3: 41, 4: 166, 5: 13, 7: 165, 8: 12, 9: 10, 6: 4, 12: 3}, 9: {0: 259, 1: 7, 2: 9, 3: 2, 4: 26, 5: 7, 6: 2}}
import pyecharts.options as opts
from pyecharts.charts import Line

up_characters = [['芭芭拉', '菲谢尔', '香菱', '温迪'], ['行秋', '诺艾尔', '砂糖', '可莉'], ['迪奥娜', '北斗', '凝光', '达达利亚'],
                             ['辛焱', '雷泽', '重云', '钟离'], ['菲谢尔', '砂糖',
                                                        '班尼特', '阿贝多'], ['香菱', '行秋', '诺艾尔', '甘雨'],
                             ['迪奥娜', '北斗', '辛焱', '魈'], ['凝光', '班尼特',
                                                        '芭芭拉', '刻晴'], ['行秋', '重云', '香菱', '胡桃'],
                             ['砂糖', '雷泽', '诺艾尔', '温迪'], ['罗莎莉亚', '芭芭拉', '菲谢尔', '达达利亚']]

x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]

line = Line()
#line.add_xaxis(xaxis_data=x_data)

def sort_(date):
    ret=[]
    for i in sorted(date.items(),key=lambda x:x[0],reverse=False):
        ret.append(i[1])
    return ret

def get_x(date:dict):
    max_len=0
    for i in date.values():
        dict_len=len(i)
        if(dict_len>max_len):
            max_len=dict_len
    
    list=[]
    for i in range(max_len):
        list.append('第'+str(i+1)+'天')
    return list

print(get_x(date_list))
line.add_xaxis(xaxis_data=get_x(date_list))
for key in date_list.keys():
    print(date_list[key])
    print(sort_(date_list[key]))
    #print(date_list[key])
    #print(list(date_list[key].values()))
    line.add_yaxis(
        series_name=up_characters[key][3],
        #stack="总量",
        y_axis=sort_(date_list[key]),
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )

line.set_global_opts(title_opts=opts.TitleOpts(title="抽卡习惯表"))
line.render("Q5抽卡习惯表.html")
