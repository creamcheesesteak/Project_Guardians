import tips as tips

import requests
from bs4 import BeautifulSoup
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler

from django.shortcuts import render
import pandas as pd
import numpy as np
import sqlite3
# Create your views here.
# from project03.myanalysis.Myanalysis import Co2


def index(request):

	return render(request, 'index.html')

def blog(request):
	# global result
	category = request.GET.get('category', None)
	search = request.GET.get('search', None)

	if category == None or search == None:
		return render(request, 'blog.html')
	else:
		df = pd.read_csv('../project/ML/ML_c/mean_ghs.csv', encoding='cp949')
		cat = {'석유화학': 'chemistry', '음식료품 · 제조업': 'manufacture', '광업': 'mining', '조선': 'ship', '건물': 'building',
			   '교통': 'transportation', '반도체.디스플레이.전기전자': 'electric',
			   '발전 · 에너지': 'energy', '유리 · 요업': 'glass', '제지': 'paper'}
		df['DSGN_INDS'] = df['DSGN_INDS'].map(cat)
		s = (df['DSGN_INDS'] == category)
		sort = df[s]

		co2 = sort.GHG_EMS[sort['CORP_NM'] == search].mean()
		co2_mean = sort['GHG_EMS'].mean()
		co2_min = sort['GHG_EMS'].min()
		co2_max = sort['GHG_EMS'].max()
		co2_all = (sort['GHG_EMS'].mean())*(len(sort['GHG_EMS']))
		eng = sort.ENG_CNSM[sort['CORP_NM'] == search].mean()
		eng_mean = sort['ENG_CNSM'].mean()
		eng_min = sort['ENG_CNSM'].min()
		eng_max = sort['ENG_CNSM'].max()
		eng_all = (sort['ENG_CNSM'].mean()) * (len(sort['ENG_CNSM']))

		co2_loc_mean=(co2_mean / co2_all) * 233
		co2_loc = (co2 / co2_all) * 233
		eng_loc_mean = (eng_mean / co2_all) * 233
		eng_loc = (eng / co2_all) * 233

		result = {'category': category, 'search': search, 'co2': co2, 'co2_mean': co2_mean, 'co2_min': co2_min, 'co2_all':co2_all,
				  'co2_max': co2_max, 'eng': eng, 'eng_mean': eng_mean, 'eng_min': eng_min, 'eng_max': eng_max, 'eng_all':eng_all,
				  'co2_loc_mean':co2_loc_mean, 'co2_loc':co2_loc, 'eng_loc_mean':eng_loc_mean, 'eng_loc':eng_loc}
		return render(request, 'blog.html', context=result)

url = 'https://search.naver.com/search.naver?query=%EC%98%A8%EC%8B%A4%EA%B0%80%EC%8A%A4&where=news&ie=utf8&sm=nws_hty'
req = requests.get(url)
def get_now():
    soup = BeautifulSoup(req.text, 'html.parser')
    title = soup.select('div.news_wrap.api_ani_send > div > a')
    press = soup.select('a.info.press')

    title_fin = list()
    press_fin = list()
    url_fin = list()
    for data in title:
        news1 = data.get_text().strip()
        title_fin.append(news1)

    for data2 in press:
        news2 = data2.get_text().strip()
        press_fin.append(news2)

    for link in title:
        url_fin.append(link['href'])

    df = pd.DataFrame({'title':title_fin, 'press':press_fin, 'url':url_fin})
    return df

def blog1(request):
	df = get_now()
	title0 = df.loc[0][0]
	title1 = df.loc[1][0]
	title2 = df.loc[2][0]
	title3 = df.loc[3][0]
	title4 = df.loc[4][0]
	title5 = df.loc[5][0]
	title6 = df.loc[6][0]
	title7 = df.loc[7][0]
	title8 = df.loc[8][0]
	title9 = df.loc[9][0]

	press0 = df.loc[0][1]
	press1 = df.loc[1][1]
	press2 = df.loc[2][1]
	press3 = df.loc[3][1]
	press4 = df.loc[4][1]
	press5 = df.loc[5][1]
	press6 = df.loc[6][1]
	press7 = df.loc[7][1]
	press8 = df.loc[8][1]
	press9 = df.loc[9][1]

	url0 = df.loc[0][2]
	url1 = df.loc[1][2]
	url2 = df.loc[2][2]
	url3 = df.loc[3][2]
	url4 = df.loc[4][2]
	url5 = df.loc[5][2]
	url6 = df.loc[6][2]
	url7 = df.loc[7][2]
	url8 = df.loc[8][2]
	url9 = df.loc[9][2]


	context = {

		'title0': title0, 'title1': title1, 'title2': title2, 'title3': title3, 'title4': title4, 'title5': title5, 'title6': title6, 'title7': title7, 'title8': title8, 'title9': title9,
		'press0': press0, 'press1': press1, 'press2': press2, 'press3': press3, 'press4': press4, 'press5': press5, 'press6': press6, 'press7': press7, 'press8': press8, 'press9': press9,
		'url0': url0, 'url1': url1, 'url2': url2, 'url3': url3, 'url4': url4, 'url5': url5, 'url6': url6, 'url7': url7, 'url8': url8, 'url9': url9,

	}
	return render(request, 'blog1.html', context)


def elements(request):

	return render(request, 'elements.html')
def blog_details(request):

	return render(request, 'blog_details.html')

def test(request):
	# industry = request.GET.get('industry')
	# place = request.GET.gt('place')
	# in_pl = str(industry) + str(place)
	in_pl = 'building강원도'
	db_test = sqlite3.connect('./timeseries.db')
	c = db_test.cursor()
	df = pd.read_sql("SELECT * FROM "+in_pl+"", db_test, index_col=None)
	# df = pd.read_excel('./ML/ML_i/test.xls')
	# df = pd.read_excel('./ML/ML_i/sample.xls')
	df = df.replace(np.nan, 'null')
	date = df.date.tolist()
	raw = df.raw.values.tolist()
	lower = df.lower.values.tolist()
	upper = df.upper.values.tolist()
	mean = df['mean'].values.tolist()

	context = {
		'date':date,
		'raw':raw,
		'lower':lower,
		'upper':upper,
		'mean':mean
	}
	return render(request, 'test.html', context)

