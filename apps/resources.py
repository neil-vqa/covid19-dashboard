import dash_html_components as html
from app import app


layout = html.Div([
	html.H1("Resources and Basic Facts"),
	html.H4("What is COVID-19?",className='mt-5'),
	html.P("COVID-19 is a disease caused by a new strain of coronavirus. ‘CO’ stands for corona, ‘VI’ for virus, and ‘D’ for disease. Formerly, this disease was referred to as ‘2019 novel coronavirus’ or ‘2019-nCoV.’The COVID-19 virus is a new virus linked to the same family of viruses as Severe Acute Respiratory Syndrome (SARS) and some types of common cold. (WHO, March 2020)"),
	
	html.H4("What are the symptoms of COVID-19?",className='mt-4'),
	html.P("Symptoms can include fever, cough and shortness of breath. In more severe cases, infection can cause pneumonia or breathing difficulties. More rarely, the disease can be fatal.These symptoms are similar to the flu (influenza) or the common cold, which are a lot more common than COVID-19. This is why testing is required to confirm if someone has COVID-19. (WHO, March 2020)"),
	
	html.H4("How does COVID-19 spread?",className='mt-4'),
	html.P("The virus is transmitted through direct contact with respiratory droplets of an infected person (generated through coughing and sneezing). Individuals can also be infected fromand touching surfaces contaminated with the virusand touching their face (e.g., eyes, nose, mouth). The COVID-19 virus may survive on surfaces for several hours, but simple disinfectants can kill it. (WHO, March 2020)"),
	
	html.H4("What is the treatment for COVID-19?",className='mt-4'),
	html.P("There is nocurrently availablevaccineforCOVID-19. However, many of the symptoms can be treatedandgetting early care from a healthcare provider can make the disease less dangerous.There are several clinical trials that are being conducted to evaluate potential therapeutics for COVID-19. (WHO, March 2020)"),
	
	html.H4("Who is most at risk?",className='mt-4'),
	html.P("We are learning more about how COVID-19 affects people every day.  Older people, and people with chronic medical conditions, such as diabetes and heart disease, appear to be more at risk of developing severe symptoms.  As this is a new virus, we are still learning about how it affects children. We know it is possible for people of any age to be infected with thevirus, but so far there arerelatively few cases of COVID-19 reported among children. This is a new virus and we need to learn more about how it affects children. The virus can be fatal in rare cases, so far mainly among older people with pre-existing medical conditions. (WHO, March 2020)"),
	
	html.Hr(),
	
	html.H6("Data Sources"),
	html.P("All data are pulled from Johns Hopkins CSSE Data Repository. (https://github.com/CSSEGISandData/COVID-19)"),
	html.P("Articles in the TECHNICAL and RESOURCES section are taken from the World Health Organization. (https://www.who.int/emergencies/diseases/novel-coronavirus-2019)"),
	
	html.H6("Disclaimer"),
	html.P("This dashboard is a custom and independent dashboard. This dashboard and the designer/maintainer/developer are in no way connected to Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)."),
	
	html.H6("Terms of Use"),
	html.P("This dashboard should only be used for educational purposes. Commercial and medical use are strictly prohibited."),
	
	html.H6("Contact"),
	html.P("For projects, comments, reactions, complaints, and/or suggestions, please email the developer: nvqa.business@gmail.com")
	
], 
className='mx-4')
