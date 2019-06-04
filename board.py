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
        

def day(name,color,x):
    with tag('g',id=name):
        with tag('svg' , width="13%" , height="100%" , y="0%", x="{}%".format(x) ):
            
            with tag('rect', x="0%", y="0%", width="5%" , height="100%", fill="#ffffff" ):
                pass
            
            with tag('rect', x="5%", y="0%", width="90%" , height="100%", fill=color , rx="25%"  ):
                pass

            with tag('rect', x="95%", y="0%", width="5%" , height="100%", fill="#ffffff" ):
                pass


colors = ["#13a538","#954a97","#f39100","#0863b5","#fec600","#bc2122","#6d6e71"]        

with tag('svg', xmlns="http://www.w3.org/2000/svg", viewBox="0 0 {} {}".format(width,height) ):
    
    with tag('g',id="header"):
        with tag('svg' , width="100%" , height="20%" , x="0%", y="0%", ):
            with tag('rect', x="0%", y="0%", width="100%" , height="100%", fill="#99ccff" ):
                pass

    with tag('g',id="body"):
        with tag('svg' , width="100%" , height="75%" , x="0%", y="20%", ):
            [ day(*r) for r in zip( days,colors,[(100.0/7)*r for r in range(0,7)])]

                     
    with tag('g',id="footer"):
        with tag('svg' , width="100%" , height="5%" , x="0%", y="95%", ):
            with tag('rect', x="0%", y="0%", width="100%" , height="100%", fill="#99ccff" ):
                pass

        

with open('board.svg','w') as f :
    f.write('\n'.join(doc))

