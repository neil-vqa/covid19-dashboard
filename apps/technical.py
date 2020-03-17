import dash_html_components as html
from app import app


layout = html.Div([
	html.H1("Technical Details"),
	html.H4("Global surveillance for COVID-19 disease caused by human infection with the 2019 novel coronavirus (WHO, 27 February 2020)",className='mt-5'),
	html.Hr(),
	html.H5("A suspected case is either:"),
	html.P("A. a patient with acute respiratory illness (that is, fever and at least one sign or symptom of respiratory disease, for example, cough or shortness of breath) AND with no other etiology that fully explains the clinical presentation AND a history of travel to or residence in a country, area or territory that has reported local transmission of COVID-19 disease during the 14 days prior to symptom onset."),
	html.P("B. a patient with any acute respiratory illness AND who has been a contact of a confirmed or probable case of COVID-19 disease during the 14 days prior to the onset of symptoms."),
	html.P("C. a patient with severe acute respiratory infection (that is, fever and at least one sign or symptom of respiratory disease, for example, cough or shortness breath) AND who requires hospitalization AND who has no other etiology that fully explains the clinical presentation."),
	
	html.H5("Probable case"),
	html.P("A probable case is a suspected case for whom the report from laboratory testing for the COVID-19 virus is inconclusive."),
	
	html.H5("Confirmed case"),
	html.P("A confirmed case is a person with laboratory confirmation of infection with the COVID-19 virus, irrespective of clinical signs and symptoms."),
	
	html.H5("Definition of contact"),
	html.P("A contact is a person who is involved in any of the following within 14 days after the onset of symptoms in the patient: (1) providing direct care for patients with COVID-19 disease without using proper personal protective equipment; (2) staying in the same close environment as a COVID-19 patient (including sharing a workplace, classroom or household or being at the same gathering); (3) travelling in close proximity with (that is, having less than 1 m separation from) a COVID-19 patient in any kind of conveyance."),
	
	html.H5("Recommendations for laboratory testing"),
	html.P("Any suspected case should be tested for infection with the COVID-19 virus using a molecular test. However, it is possible to test only a subset of suspected cases, depending on the intensity of the transmission, the number of cases and laboratory capacity."),
	html.P("If resources allow, testing may be done more broadly (for instance, through sentinel surveillance) to better assess the full extent of the circulation of the virus."),
	html.P("Based on clinical judgment, clinicians may opt to order a test for the COVID-19 virus in a patient who does not strictly meet the case definition, for example, if there is acute respiratory illness among a cluster of health care workers or severe acute respiratory infection or pneumonia in families, workplaces or social networks.")
		
],
className='mx-4')
