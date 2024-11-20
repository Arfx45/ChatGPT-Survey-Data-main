import matplotlib.pyplot as flt
import csv

l= 'GPTResponses.csv'
with open(l) as f:
    vr=csv.reader(f)
    headers = next(vr)
    responses=[]
    
    for i in vr:
        responses.append(i)
forWhat= [i[11].split(", ") for i in responses]
faculties = [response[5] for response in responses]
#print(forWhat)
UFW= {}


#print(forWhat)

for i,j in zip(faculties,forWhat):
    if i in UFW.keys():
        for f in j:
            if f in UFW[i].keys():
                UFW[i][f]+=1
            else:
                UFW[i][f]=0
                UFW[i][f]+=1
    else:
        UFW[i] = {}
        for f in j:
            UFW[i][f]=0
            UFW[i][f]+=1
        
bar_width = 0.05

fac= UFW.keys()
categories = list(set([j for i in UFW for j in UFW[i].keys()]))
#print(UFW)
r1 = list(range(len(fac)))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]
r6 = [x + bar_width for x in r5]
r7 = [x + bar_width for x in r6]
r8 = [x + bar_width for x in r7]
r9 = [x + bar_width for x in r8]
r10 = [x + bar_width for x in r9]
r11 = [x + bar_width for x in r10]


#print(r1)
categories[:] = [x for x in categories if x != '']
fac=[i.upper() for i in fac]  
Essay= [UFW[key]['Essays']if 'Essays'in UFW[key] else 0 for key in UFW ]
Research= [UFW[key]['Research']if 'Research'in UFW[key] else 0 for key in UFW ]
Math= [UFW[key]['Math Problem']if 'Math Problem'in UFW[key] else 0 for key in UFW ]
jobFind= [UFW[key]['Resumed and job search'] if 'Resumed and job search'in UFW[key] else 0 for key in UFW ]
dont= [UFW[key]["Don't really use it"]if "Don't really use it" in UFW[key] else 0 for key in UFW ]
Ideas= [UFW[key]['Ideas/ Brain storming?']if 'Ideas/ Brain storming?' in UFW[key] else 0 for key in UFW ]
Phys= [UFW[key]['Physics/Chemsitry Calculations']if 'Physics/Chemsitry Calculations' in UFW[key] else 0 for key in UFW ]
code= [UFW[key]['Coding Solutions']if 'Coding Solutions' in UFW[key] else 0 for key in UFW ]
SCM= [UFW[key]['Social Media postings']if 'Social Media postings' in UFW[key]else 0 for key in UFW ]
computing= [UFW[key]['Computing Problems'] if 'Computing Problems' in UFW[key] else 0 for key in UFW ]
Entertainment= [UFW[key]['Entertainment?']if 'Entertainment?' in UFW[key] else 0 for key in UFW ]
flt.bar(r1, Essay, color='blue', width=bar_width, edgecolor='white', label='Essay')
flt.bar(r2, Research, color='grey', width=bar_width, edgecolor='white', label='Research')
flt.bar(r3, Math, color='green', width=bar_width, edgecolor='white', label='Math')
flt.bar(r4, jobFind, color='pink', width=bar_width, edgecolor='white', label='Resume and job search')
flt.bar(r5, dont, color='red', width=bar_width, edgecolor='white', label='Dont Really Use it')
flt.bar(r6, Ideas, color='yellow', width=bar_width, edgecolor='white', label='Ideas')
flt.bar(r7, Phys, color='turquoise', width=bar_width, edgecolor='white', label='Physics/Chemsitry Problems')
flt.bar(r8, code, color='teal', width=bar_width, edgecolor='white', label='Coding Solutions')
flt.bar(r9, computing, color='orange', width=bar_width, edgecolor='white', label='Programing')
flt.bar(r10, SCM, color='purple', width=bar_width, edgecolor='white', label='Social Media Postings')
flt.bar(r11, Entertainment, color='purple', width=bar_width, edgecolor='white', label='Personal Entertainment')

flt.title('Use of ChatGPT in different Fields of Study')
flt.xlabel('Faculties')
flt.ylabel('Responses')
flt.xticks([r + bar_width/2 for r in range(len(fac))], fac)
flt.legend()

flt.show()