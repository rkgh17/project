import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

# 한글
import matplotlib
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False


# 데이터 취합
def count_total_monthly_volume():
    YEARS = ['2017', '2018', '2019', '2020', '2021','2022']
    MONTHS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    count_list, record_date_list = [], []
    for year in YEARS:
        path = 'data/공공자전거 이용정보(월별)/서울특별시 공공자전거 이용정보(월별)_' + str(year) + '.csv'
        df = pd.read_csv(path)

        ## 연도별 다른 포멧으로 공개된 데이터 파싱
        for i in range(len(MONTHS)):
            if year == '2022':
                if i > 5: ## 현재 2022년 6월까지 공개
                    break
                year_month = '{}-{}'.format(2022,MONTHS[i])
                
            elif year == '2021':
                year_month = '{}-{}'.format(2021,MONTHS[i])
            elif year == '2020':
                year_month = '{}-{}'.format(2020,MONTHS[i])
            elif year == '2019':
                year_month = '{}-{}'.format(2019,MONTHS[i])
            elif year == '2018':
                year_month = '{}-{}'.format(2018,MONTHS[i])
            elif year == '2017':
                year_month = '{}-{}'.format(2017,MONTHS[i])
            
            count_list.append(df[df['대여일자'] == year_month]['이용건수'].sum())
            record_date_list.append(year + "-" + MONTHS[i])
    return count_list, record_date_list

# 이용일자 년-월로 나누기
def tabularize_total_monthly_volume(count_by_ten_hundreds_list, record_date_list):
    df = pd.DataFrame({'년-월': record_date_list, '이용자수(만명)': count_by_ten_hundreds_list})
    df['year'] = df['년-월'].apply(lambda x: x.split('-')[0])
    df['month'] = df['년-월'].apply(lambda x: x.split('-')[1])
    return df

# 전체 이용자 수
def all_graph1():
    count_list, record_date_list = count_total_monthly_volume()
    count_by_ten_hundreds_list = [c / 1e4 for c in count_list] ## 가독성을 위해 만 단위로 나눔

    fig = plt.figure(figsize=(20, 12), facecolor='white')
    ax = fig.add_subplot(111)
    ax.set_xlabel('년도-월', fontsize=20)
    ax.set_ylabel('이용자 수 (만명)', fontsize=20)

    plt.plot(record_date_list, count_by_ten_hundreds_list, color = 'green', linewidth = 3)
    ax.set_xticklabels(record_date_list, rotation=70)
    return fig


def all_graph2():
    YEARS = ['2017', '2018', '2019', '2020', '2021','2022']
    count_list, record_date_list = count_total_monthly_volume()
    count_by_ten_hundreds_list = [c / 1e4 for c in count_list] ## 가독성을 위해 만 단위로 나눔
    total_monthly_volume_df = tabularize_total_monthly_volume(count_by_ten_hundreds_list, record_date_list)

    fig = plt.figure(figsize=(12,8),facecolor='white')
    ax = fig.add_subplot(111)
    ax.set_xlabel('월', fontsize = 20)
    ax.set_ylabel('이용자 수 (만명)', fontsize=20)
    for year in YEARS:
        tgt_rows = total_monthly_volume_df[total_monthly_volume_df['year'] == year]
        plt.plot(tgt_rows['month'].astype(int), tgt_rows['이용자수(만명)'], label='{}년'.format(year), marker='o')
    ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    ax.legend(prop={'size':15})
    return fig