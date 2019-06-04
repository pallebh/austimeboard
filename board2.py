from contextlib import contextmanager

colors = ["#13a538","#954a97","#f39100","#0863b5","#fec600","#bc2122","#6d6e71"]
days   = ['Mandag','Tirsdag','Onsdag','Tordag','Fredag','Lørdag','Søndag']

doc = []
dw = ( 100.0/7 )
doc = []


@contextmanager
def tag(tagname, **kwargs):
    keyvaluepairs = [ '{}="{}"'.format(key.replace("_" , "-"),value )for key, value in kwargs.items() ]
    
    start = ''
    if keyvaluepairs: 
        start = '<{} {}>'.format(tagname, " ".join(keyvaluepairs))
    else:
        start = '<{}>'.format(tagname)
    
    doc.append(start)
    yield
    end = '</{}>'.format(tagname)
    doc.append(end)
    
@contextmanager
def text(text,  **kwargs):
    keyvaluepairs = [ '{}="{}"'.format(key.replace("_" , "-"),value )for key, value in kwargs.items() ]
    
    start = ''
    if keyvaluepairs: 
        start = '<{} {}>'.format('text', " ".join(keyvaluepairs))
    else:
        start = '<{}>'.format('text')

    doc.append(start)
    doc.append(text)
    end = '</{}>'.format('text')
    doc.append(end)
    

width = 5000
height = 7000
jump = 100.0 / 7.0
        

with tag('svg', xmlns="http://www.w3.org/2000/svg", viewBox="0 0 {} {}".format(width,height) ):
     
    with tag('g' , id="weekdayheaders"):
        with tag('svg', x="0%", y="14%", width="100%", height="5%" ):
            day = 0 
            for r in [ jump*r for r in range(7) ]:
                with tag('svg' , x="{}%".format(r) , y="0%", width="{}%".format(jump) , height="100%" ):
                    
                    with tag('rect', x="0%", y="0%", width="13%" , height="100%", fill="#ffffff"  ):
                        pass
                
                    dayColor = colors[day]
                    with tag('rect', x="13%", y="0%", width="84%" , height="100%", fill="{}".format(dayColor) , rx="20%"  ):
                        pass

                    text("hvorfor" , x="20%", y="20%" , font_size="120" , fill="#000000" )  
                     
                    with tag('rect', x="97%", y="0%", width="3%" , height="100%", fill="#ffffff"  ):
                        pass

                day += 1 

    with tag('svg', x="0%", y="20%", width="100%", height="79%" ):
        day = 0 
        for r in [ jump*r for r in range(7) ]:
            with tag('g' , id ="weekday_{}".format(r) ):
                with tag('svg' , x="{}%".format(r) , y="0%", width="{}%".format(jump) , height="100%"    ):
                    
                    with tag('rect', x="0%", y="0%", width="13%" , height="100%", fill="#ffffff" ):
                        pass
                
                    dayColor = colors[day]
                    with tag('rect', x="13%", y="0%", width="84%" , height="98%", fill="{}".format(dayColor) , rx="20%" ,stroke="#000000" , stroke_width="0.4%"  ):
                        pass   
                    
                    for rr in range(1,95,6):
                        with tag('rect', x="33%", y="{}%".format(rr), width="45%" , height="5%", fill="#ffffff", stroke="#000000" , stroke_width="0.5%" , rx="5%"  ):
                             pass

                    with tag('rect', x="97%", y="0%", width="3%" , height="100%", fill="#ffffff"  ):
                        pass
        
                day += 1 


    with tag('g' , id = "bottom"):
        with tag('svg', x="0%", y="99%", width="100%", height="1%" ):
            with tag('rect', x="0%", y="0%", width="100%" , height="100%", fill="#ffffff" ):
                pass    



with open('board.svg','w') as f :
    f.write('\n'.join(doc))

