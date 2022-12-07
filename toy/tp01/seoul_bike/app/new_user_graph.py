import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

# 한글
import matplotlib
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False


# 신규 가입자 데이터 취합
new_user_age_df_raw = pd.read_csv('data/신규가입자 정보(월별)/연령별_전처리.csv')
new_user_age_df = new_user_age_df_raw.fillna(0)
new_user_age_df['datetime'] = new_user_age_df['날짜'].apply(lambda x: datetime.strptime(x, '%y-%b'))
new_user_age_df['year'] = new_user_age_df['datetime'].apply(lambda x: x.year)
new_user_age_df['month'] = new_user_age_df['datetime'].apply(lambda x: x.month)
tgt_ages = ['10대', '20대', '30대', '40대', '50대', '60대', '70대', '기타']
new_user_by_month_cumsum = new_user_age_df[tgt_ages].cumsum().sum(axis=1)
new_user_by_month = new_user_age_df[tgt_ages].sum(axis=1)
datetime_str = new_user_age_df['datetime'].apply(lambda x: x.strftime('%Y-%m'))