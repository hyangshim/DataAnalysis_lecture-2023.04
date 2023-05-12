import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def Top20():
    df =pd.read_csv('../05.Crawling/data/유튜브 랭킹.csv')
    plt.figure(figsize=(12,8))
    plt.barh(df.채널명.head(20), df.구독자수.head(20))
    plt.title('구독자수 Top 20 채널')
   



def Top10():
    df =pd.read_csv('../05.Crawling/data/유튜브 랭킹.csv')
    df3 = df.카테고리.value_counts().to_frame()
    df.pivot_table('채널명', '카테고리', aggfunc='count').sort_values('채널명', ascending=False).head(10)
    sns.barplot(y=df3.index[:10], x='count', data=df3.head(10))
    plt.title('카테고리별 채널수 Top 10');