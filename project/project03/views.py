from django.shortcuts import render
import pandas as pd
import numpy as np
import sqlite3
# Create your views here.

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