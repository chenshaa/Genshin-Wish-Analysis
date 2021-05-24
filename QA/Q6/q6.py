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
    
    rolls_for_five={}

    for user in range(len(datebase)):
        rolls_count = 0
        rolls_for_five[user]=[]
        for roll in range(len(datebase[user][2])):
            rolls_count+=1
             # 当抽到五星
            if(datebase[user][2][roll][3]=='5'):
                rolls_for_five[user].append(rolls_count)
                # 计数清零
                rolls_count=0

    print(rolls_for_five)

def get_x(date: dict):
    max_len = 0
    for i in date.values():
        dict_len = len(i)
        if(dict_len > max_len):
            max_len = dict_len

    list = []
    for i in range(max_len):
        list.append('第'+str(i+1)+'个')
    return list

from pyecharts.charts import Line
import pyecharts.options as opts

line = Line()
line.add_xaxis(xaxis_data=get_x(rolls_for_five))
for key in rolls_for_five.keys():
    line.add_yaxis(
        series_name="玩家组"+str(int(int(key)/20)),
        y_axis=rolls_for_five[key],
        areastyle_opts=opts.AreaStyleOpts(opacity=0.2),
        label_opts=opts.LabelOpts(is_show=False),
    )

line.set_global_opts(title_opts=opts.TitleOpts(title="抽卡数量表"))
line.render("Q6.html")
