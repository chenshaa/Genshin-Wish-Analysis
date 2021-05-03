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

    skips_number = 0
    skips_weapon = 0
    rolls_for_five = []
    for user in datebase:
        rolls_for_five.append(0)
        skips_count = 0
        empty_excess=0
        for roll in user[2]:
            if(roll[3] == '5'):
                if(skips_number):
                    skips_count += 1
                    if(skips_count <= skips_number):
                        rolls_for_five[-1] = 0
                    else:
                        rolls_for_five.append(0)
                else:
                    rolls_for_five.append(0)
                    empty_excess=0
            rolls_for_five[-1] += 1
            empty_excess=1
        if(empty_excess):
            del rolls_for_five[-1]
    rolls_count = 0

    for nu in rolls_for_five:
        rolls_count += nu
    rolls_aver = rolls_count/len(rolls_for_five)
    print(rolls_aver)

    from pyecharts import options as opts
    from pyecharts.charts import Gauge
    g = (
        Gauge()
        .add("", [("", rolls_aver)])
        .set_global_opts(title_opts=opts.TitleOpts(title="平均五星抽数"))
    )
    g.render('Q1平均五星抽数.html')
