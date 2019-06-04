import languages
import json

import translate
translate.google(text='mondag',from_language='en',to_language='da')

#days = ['monday', 'tuesday', 'wednesday', 'thursday' , 'friday', 'saturday', 'sunday']


#weekdays = {} 



#for key,value in languages.LANGUAGES.items():
#	names = []	
#	for day in days:
#		translator = Translator()
#		print( translator.translate(day,dest=key,src='en') )  	
	
#weekdays[key]=names
#with open('weekdays.json','w') as write_file:
#    json.dump(weekdays, write_file)		
	
