import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as do
from app import app
from data import data_parse
import os

map_token = os.environ.get('MAPBOX_TOKEN')
map_style = os.environ.get('MAPBOX_STYLE')

layout = html.Div(
	[
	dbc.Row([
		dbc.Col([
			dbc.Col(dcc.Graph(id="card1",responsive=True,config={'displayModeBar': False}, style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#ffffff','height':'100%'})
		],style={'height':'20vh'}, md=3),
		dbc.Col([
			dbc.Col(dcc.Graph(id="card2",responsive=True,config={'displayModeBar': False}, style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#ffffff','height':'100%'})
		],style={'height':'20vh'}, md=3),
		dbc.Col([
			dbc.Col(dcc.Graph(id="card3",responsive=True,config={'displayModeBar': False}, style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#ffffff','height':'100%'})
		],style={'height':'20vh'}, md=3),
		dbc.Col([
			dbc.Col(dcc.Graph(id="card4",responsive=True,config={'displayModeBar': False}, style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#ffffff','height':'100%'})
		],style={'height':'20vh'}, md=3),
	]),
	dbc.Row([
		dbc.Col([
			dbc.Col(dbc.Row(dcc.Graph(id='map',config={'displayModeBar': False}, style={'height':'100%','width':'100%'}),style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#ffffff','height':'100%'})
		],style={'height':'45vh'}, md=8),
		dbc.Col([
			dbc.Col(dbc.Row(dcc.Graph(id='mini-table',config={'displayModeBar': False}, style={'height':'100%','width':'100%'}),style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#ffffff','height':'100%'})
		],style={'height':'45vh'}, md=4)
	], className='mt-3'),
	dbc.Row([
		dbc.Col([
			dbc.Col(dbc.Row(dcc.Graph(id='chart1',config={'displayModeBar': False}, style={'height':'100%','width':'100%'}),style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#ffffff','height':'100%'})
		],style={'height':'20vh'}, md=4),
		dbc.Col([
			dbc.Col(dbc.Row(dcc.Graph(id='chart2',config={'displayModeBar': False}, style={'height':'100%','width':'100%'}),style={'height':'100%'})
			,className='rounded-lg shadow-sm',style={'backgroundColor':'#ffffff','height':'100%'})
		],style={'height':'20vh'}, md=4),
		dbc.Col([
			dbc.Col([
				dbc.Row(id='button-desc',className='pt-2 px-auto'),
				dbc.Row([
					dbc.Button("Refresh Dashboard", id="refresh-button", color="info"),
					html.Div(id='dummy',style={"display":"none"})
				],justify='center')
			],style={'backgroundColor':'#dfe6e9','height':'100%'})
		],style={'height':'20vh'}, md=4)
	], className='mt-3')
	]
)

@app.callback(
	[Output('card1','figure'),
	Output('card2','figure'),
	Output('card3','figure'),
	Output('card4','figure'),
	Output('map','figure'),
	Output('button-desc','children'),
	Output('mini-table','figure'),
	Output('chart1','figure'),
	Output('chart2','figure')],
	[Input('refresh-button','n_clicks'),
	Input('dummy','children')]
)
def update_cards(n_clicks, dummy_clicks):
	sum_conf,sum_deat,sum_rec,countries,df_name,df_lat,df_lon,midpoint,df_country,recent,summary,dff_conf,dff_rec = data_parse()
	
	card1 = do.Figure(do.Indicator(
			mode= 'number',
			value= sum_conf,
			number={'valueformat':'.%f', 'font':{'size':30,'family':'Nunito Sans','color':'#d9534f'}},
			title = {"text": 'Confirmed', 'font':{'size':25,'family':'Nunito Sans'}}))
	card1.update_layout(margin= do.layout.Margin(t=35,b=0), plot_bgcolor='#ffffff', paper_bgcolor='#ffffff')
	
	card2 = do.Figure(do.Indicator(
			mode= 'number',
			value= sum_deat,
			number={'valueformat':'.%f', 'font':{'size':30,'family':'Nunito Sans','color':'#d9534f'}},
			title = {"text": 'Deaths', 'font':{'size':25,'family':'Nunito Sans'}}))
	card2.update_layout(margin= do.layout.Margin(t=35,b=0), plot_bgcolor='#ffffff', paper_bgcolor='#ffffff')
	
	card3 = do.Figure(do.Indicator(
			mode= 'number',
			value= sum_rec,
			number={'valueformat':'.%f', 'font':{'size':30,'family':'Nunito Sans','color':'#4bbf73'}},
			title = {"text": 'Recovered', 'font':{'size':25,'family':'Nunito Sans'}}))
	card3.update_layout(margin= do.layout.Margin(t=35,b=0), plot_bgcolor='#ffffff', paper_bgcolor='#ffffff')
	
	card4 = do.Figure(do.Indicator(
			mode= 'number',
			value= len(countries),
			number={'valueformat':'.%f', 'font':{'size':30,'family':'Nunito Sans','color':'#d9534f'}},
			title = {"text": 'Countries with cases', 'font':{'size':20,'family':'Nunito Sans'}}))
	card4.update_layout(margin= do.layout.Margin(t=35,b=0), plot_bgcolor='#ffffff', paper_bgcolor='#ffffff')
	
	hover_text = ['Province/State: '+'{}'.format(x) + '<br>Country: '+'{}'.format(y) + '<br>Confirmed: '+'{}'.format(z) + '<br>Deaths: '+'{}'.format(v) + '<br>Recovered: '+'{}'.format(w) for x,y,z,v,w in zip(df_name,df_country,list(summary['Confirmed']),list(summary['Deaths']),list(summary['Recovered']))]
	
	map1 = do.Figure()
	map1.add_trace(
		do.Scattermapbox(
			lat=df_lat,
			lon=df_lon,
			mode='markers',
			marker=do.scattermapbox.Marker(
				size=5,
				color='#c94631',
				opacity=0.7
				),
			text= hover_text,
			hoverinfo='text',
			showlegend= False
		)
	)
	map1.update_layout(
		mapbox= do.layout.Mapbox(
			accesstoken= map_token,
			center= do.layout.mapbox.Center(
				lat= 30.3753,
				lon= 69.3451
			),
			zoom= 1.3,
			style= map_style
		),
		margin= do.layout.Margin(
			l=0,
			r=0,
			t=0,
			b=0
		)
	)
	
	desc = html.P(["Click 'Refresh' to fetch new data & update charts. Featured data are as of {}.".format(recent)], style={'textAlign':'center'})
	
	table = do.Figure(
		do.Table(
			header={'values':list(summary.columns),'fill':{'color':'#017cbf'},'font':{'family':'Nunito Sans','color':'#ffffff'}},
			cells={'values':[summary.State,summary.Country,summary.Confirmed,summary.Deaths,summary.Recovered],
				'fill':{'color':'#f5f4ef'},'font':{'family':'Nunito Sans'}}
		)
	)
	table.update_layout(margin= do.layout.Margin(t=0,b=0,l=0,r=0), plot_bgcolor='#ffffff', paper_bgcolor='#ffffff')
	
	line1 = do.Figure(
		do.Scatter(
			x= dff_conf.index,
			y= dff_conf[0],
			marker_color='#d9534f',
		)
	)
	line1.update_layout(
		margin= do.layout.Margin(t=35,b=0,l=0,r=0), plot_bgcolor='#ffffff', paper_bgcolor='#ffffff',
		xaxis={'showgrid':False,'showticklabels':False},yaxis={'showgrid':False,'showticklabels':False},
		title={'text':'Confirmed (previous 15-day range)','font':{'family':'Nunito Sans','size':12}}
	)
	
	line2 = do.Figure(
		do.Scatter(
			x= dff_rec.index,
			y= dff_rec[0],
			marker_color='#4bbf73',
		)
	)
	line2.update_layout(
		margin= do.layout.Margin(t=35,b=0,l=0,r=0), plot_bgcolor='#ffffff', paper_bgcolor='#ffffff',
		xaxis={'showgrid':False,'showticklabels':False},yaxis={'showgrid':False,'showticklabels':False},
		title={'text':'Recovered (previous 15-day range)','font':{'family':'Nunito Sans','size':12}}
	)
	
	
	return card1,card2,card3,card4,map1,desc,table,line1,line2

