# import necessary libraries
import pandas as pd
import xml.dom.minidom

# change working directory

# parse go_obo.xml into a DOM document object
DOMTree=xml.dom.minidom.parse('go_obo.xml')
# find root element
go=DOMTree.documentElement
# a list of 'terms' elements
terms=go.getElementsByTagName('term')
defs=[]
is_a=[]
al={}
#Read all the data given in the original file
for term in terms:
    defs_2=term.getElementsByTagName('def')
    ids_2=term.getElementsByTagName('id')[0]
    is_as=term.getElementsByTagName('is_a')
    for x in is_as:
        is_a.append(x.childNodes[0].data)
    al[ids_2.childNodes[0].data]=is_a[:]
    is_a.clear()
    for def_2 in defs_2:
        defstr=def_2.getElementsByTagName('defstr')[0]
        defs.append(defstr.childNodes[0].data)    
p=[]
#Search for all the 'autophagosome' title
for x in range(len(defs)):
    if 'autophagosome' in defs[x]:
        p.append(x)
ids=[]
names=[]
d=[]
#Do the preparation of calculating the childnode
for i in p:
    ids_2=terms.item(i).getElementsByTagName('id')[0]
    ids.append(ids_2.childNodes[0].data)
    names_2=terms.item(i).getElementsByTagName('name')[0]
    names.append(names_2.childNodes[0].data)
    d.append(defs[i])
#Calculat the childnode of each code
childnode = []
for i in ids:
    m = []
    count = 0
    for j in al:
        if i in al[j]:
            count += 1
            m.append (j)
    n = m[:]
    inc = count
    while inc != 0 :
        m = []
        inc = 0
        for k in n:
            for j in al:
                if k in al[j]:
                    count += 1
                    inc += 1
                    m.append (j)
        n = m[:]
    childnode.append (count)
# write into the excel
xfile=pd.DataFrame({'id':ids,'name':names,'definition':d,'childnodes':childnode})
xfile.to_excel('Autophagosome.xlsx',
               sheet_name='Autophagosome',
               columns=['id','name','definition','childnodes'])
