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
    
    hero_list={}
    switch_five=1
    switch_four=1
    for user in datebase:
        for roll in user[2]:
            if(roll[3]=='5' and switch_five):
                if(roll[1] in hero_list):
                    hero_list[roll[1]]+=1
                else:
                    hero_list[roll[1]]=1
            if(roll[3]=='4' and switch_four):
                if(roll[1] in hero_list):
                    hero_list[roll[1]]+=1
                else:
                    hero_list[roll[1]]=1
    print(hero_list.items())

    from pyecharts import options as opts
    from pyecharts.charts import WordCloud
    
    (
        WordCloud()
        .add(series_name="角色词云", data_pair=hero_list.items())
        .set_global_opts(
            title_opts=opts.TitleOpts(
            title="热点分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("Q2.html")
)

