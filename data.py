import pandas as pd
import numpy as np

url_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

def data_parse():

	df_confirmed = pd.read_csv(url_confirmed)
	cur_conf = df_confirmed[df_confirmed.columns[-1]]
	sum_conf = np.sum(cur_conf)

	df_deaths = pd.read_csv(url_deaths)
	cur_deat = df_deaths[df_deaths.columns[-1]]
	sum_deat = np.sum(cur_deat)

	df_recover = pd.read_csv(url_recovered)
	cur_rec = df_recover[df_recover.columns[-1]]
	sum_rec = np.sum(cur_rec)
	
	countries = list(df_confirmed['Country/Region'].unique())
	
	df_name = list(df_confirmed['Province/State'])
	df_lat = list(df_confirmed['Lat'])
	df_lon = list(df_confirmed['Long'])
	midpoint = (np.average(df_confirmed['Lat']), np.average(df_confirmed['Long']))
	df_country = list(df_confirmed['Country/Region'])
	recent = df_confirmed.columns[-1]
	
	summary = pd.concat([df_confirmed['Province/State'],df_confirmed['Country/Region'],cur_conf,cur_deat,cur_rec],axis=1, keys=['State','Country','Confirmed','Deaths','Recovered'])
	#dict_summary = summary.to_dict()
	
	line_conf = df_confirmed[df_confirmed.columns[-15:]]
	dff_conf = pd.DataFrame(line_conf.sum(axis = 0, skipna = True))
	
	line_rec = df_recover[df_recover.columns[-15:]]
	dff_rec = pd.DataFrame(line_rec.sum(axis = 0, skipna = True))
	
	return sum_conf,sum_deat,sum_rec,countries,df_name,df_lat,df_lon,midpoint,df_country,recent,summary,dff_conf,dff_rec





