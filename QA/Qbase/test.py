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
    print(datebase)

#file_names = ['gacha100.csv', 'gacha200.csv', 'gacha301.csv', 'gacha302.csv']  # 新手池/常驻池/角色池/武器池

bar = (
    Bar()
    .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
)
bar.render()
