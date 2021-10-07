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
from project03.myanalysis.Myanalysis import Co2


def index(request):

	return render(request, 'index.html')

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

def blog(request):

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

		'title0': title0, 'title1': title1, 'title2': title2, 'title3': title3, 'title4': title4, 'title5': title5,
		'title6': title6, 'title7': title7, 'title8': title8, 'title9': title9,
		'press0': press0, 'press1': press1, 'press2': press2, 'press3': press3, 'press4': press4, 'press5': press5,
		'press6': press6, 'press7': press7, 'press8': press8, 'press9': press9,
		'url0': url0, 'url1': url1, 'url2': url2, 'url3': url3, 'url4': url4, 'url5': url5, 'url6': url6, 'url7': url7,
		'url8': url8, 'url9': url9,

	}
	return render(request, 'blog.html', context)

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

def blog_details(request):
	# global result
	category = request.GET.get('category', None)
	search = request.GET.get('search', None)

	if category == None or search == None:
		return render(request, 'blog_details.html')
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
		# co2_all = (sort['GHG_EMS'].mean()) * (len(sort['GHG_EMS']))
		eng = sort.ENG_CNSM[sort['CORP_NM'] == search].mean()
		eng_mean = sort['ENG_CNSM'].mean()
		eng_min = sort['ENG_CNSM'].min()
		eng_max = sort['ENG_CNSM'].max()
		# eng_all = (sort['ENG_CNSM'].mean()) * (len(sort['ENG_CNSM']))

		co2_loc_mean = (co2_mean / co2_max) * 233
		co2_loc = (co2 / co2_max) * 233
		eng_loc_mean = (eng_mean / eng_max) * 233
		eng_loc = (eng / eng_max) * 233

		result = {'category': category, 'search': search, 'co2': co2, 'co2_mean': co2_mean, 'co2_min': co2_min,
				  'co2_max': co2_max, 'eng': eng, 'eng_mean': eng_mean, 'eng_min': eng_min, 'eng_max': eng_max,
				  'co2_loc_mean': co2_loc_mean, 'co2_loc': co2_loc, 'eng_loc_mean': eng_loc_mean, 'eng_loc': eng_loc}


	return render(request, 'blog_details.html',context=result)

def calculator(request):

	return render(request, 'calculator.html')

def calculator_option(request):
	try:
		user_elec = request.GET.get('elec');
		user_co2 = request.GET.get('co2');
		user_tree = request.GET.get('tree');
		sido = request.GET.get('sido');
		ind = request.GET.get('ind');
		user_select_energy = request.GET.get('user_select_energy')
		saving_technology = request.GET.get('saving_technology')

		data_sorting = Co2().ind_name(ind);
		ind_mean = Co2().graph(ind,sido)

		sort_base = Co2().sol1_alt(ind,user_co2)
		sort_fuel = Co2().sol1_alt_fuel(ind,user_co2,sort_base)
		sort_elec = Co2().sol1_alt_elec(ind,user_co2,sort_base)

		context = {
			'sol1': sort_base[5],
			'sol2': sort_base[6],
			'sol3': sort_base[7],
			'sol4': sort_base[8],
			'sol5': sort_base[9],
			'sol6': sort_fuel[5],
			'sol7': sort_fuel[6],
			'sol8': sort_fuel[7],
			'sol9': sort_fuel[8],
			'sol10': sort_fuel[9],
			'sol11': sort_elec[5],
			'sol12': sort_elec[6],
			'sol13': sort_elec[7],
			'sol14': sort_elec[8],
			'sol15': sort_elec[9],
			'sort' : data_sorting[0],

			'ind': ind,

			'money1': sort_base[10],
			'money2': sort_base[11],
			'money3': sort_base[12],
			'money4': sort_base[13],
			'money5': sort_base[14],
			'money6': sort_fuel[10],
			'money7': sort_fuel[11],
			'money8': sort_fuel[12],
			'money9': sort_fuel[13],
			'money10': sort_fuel[14],
			'money11': sort_elec[10],
			'money12': sort_elec[11],
			'money13': sort_elec[12],
			'money14': sort_elec[13],
			'money15': sort_elec[14],
			'deco1': sort_base[0],
			'deco2': sort_base[1],
			'deco3': sort_base[2],
			'deco4': sort_base[3],
			'deco5': sort_base[4],
			'deco6': sort_fuel[0],
			'deco7': sort_fuel[1],
			'deco8': sort_fuel[2],
			'deco9': sort_fuel[3],
			'deco10': sort_fuel[4],
			'deco11': sort_elec[0],
			'deco12': sort_elec[1],
			'deco13': sort_elec[2],
			'deco14': sort_elec[3],
			'deco15': sort_elec[4],
			'user_elec' : user_elec,
			'user_co2' : user_co2,
			'user_tree' : user_tree,
			'result_sido': sido,
			'user_select_energy': user_select_energy,
			'saving_technology': saving_technology,
			'ind_elec' : ind_mean[0],
			'ind_co2' : ind_mean[1],
			'ind_tree' : ind_mean[2],
			'no1': sort_base[15],
			'no2': sort_base[16],
			'no3': sort_base[17],
			'no4': sort_base[18],
			'no5': sort_base[19],
			'fuel_no1': sort_fuel[15],
			'fuel_no2': sort_fuel[16],
			'fuel_no3': sort_fuel[17],
			'fuel_no4': sort_fuel[18],
			'fuel_no5': sort_fuel[19],
			'elec_no1': sort_elec[15],
			'elec_no2': sort_elec[16],
			'elec_no3': sort_elec[17],
			'elec_no4': sort_elec[18],
			'elec_no5': sort_elec[19],
		};

	except AttributeError:
		return render(request, 'elements.html')
	except ValueError:
		return render(request, 'elements.html')

	return render(request, 'calculator_option.html', context)

def calculator_result(request):
	ind = request.GET.get('ind');
	sido = request.GET.get('user_sido');
	elec = request.GET.get('user_elec');
	co2 = round(float(request.GET.get('user_co2')), 3)
	tree = request.GET.get('user_tree');

	ind_ko = request.GET.get('ind_name');
	try:
		reduce_co2 = round(float(request.GET.get('co2')), 3)
	except ValueError:
		return render(request, 'elements.html')
	reduce_money = request.GET.get('money');

	# def
	in_pl = ind + sido
	db_test = sqlite3.connect('./timeseries.db')
	c = db_test.cursor()
	df = pd.read_sql("SELECT * FROM " + in_pl + "", db_test, index_col=None)
	df = df.replace(np.nan, 'null')
	date = df.date.tolist()
	raw = df.raw.values.tolist()
	lower = df.lower.values.tolist()
	upper = df.upper.values.tolist()
	mean = df['mean'].values.tolist()

	c_competitor = sum(map(float, list(filter(lambda a: a != 'null', df.raw.tolist()))[-12:]))
	c_reduce = (co2 - reduce_co2)
	start = df.loc[df.date == '2017-01-01 00:00:00'].index
	stand = sum(map(float, df.loc[start[0]:start[0] + 11].raw.tolist()))
	c_target = round((stand * (co2 / stand)) * 0.756, 3)
	bar_value = [c_competitor, co2, c_reduce, c_target]

	criteria = (co2 / c_competitor)
	if criteria >= 1:
		ratio = round((co2 / c_competitor) * 100, 3)
		compare = '더 많이'
	else:
		ratio = abs(round((1 - float(co2) / c_competitor) * 100, 3))
		compare = '더 조금'

	value_target = list(map(float, df.target.tolist()))
	my_before = [element * (ratio / 100) for element in value_target]

	my_after = [element * 0.87 for element in my_before]  # example

	context = {
		'ind': ind,
		'sido': sido,
		'elec': elec,
		'tree': tree,
		'co2': co2,

		'ind_ko': ind_ko,
		'reduce_co2': reduce_co2,
		'reduce_money': reduce_money,

		'bar_value': bar_value,

		'ratio': ratio,
		'compare': compare,
		'c_target': c_target,

		'target': in_pl,
		'date': date,
		'raw': raw,
		'lower': lower,
		'upper': upper,
		'mean': mean,

		'my_before': my_before,
		'my_after': my_after,
	}

	return render(request, 'calculator_result.html', context)


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

def elements(request):

	return render(request, 'elements.html')

def calculator_result2(request):

	return render(request, 'calculator_result2.html')
