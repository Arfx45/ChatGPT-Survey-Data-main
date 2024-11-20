import csv
import matplotlib.pyplot as plt

l= 'GPTResponses.csv'
with open(l) as f:
    vr=csv.reader(f)
    headers = next(vr)
    responses=[]
    
    for i in vr:
        responses.append(i)
    

# Extract the relevant data from the CSV file
faculties = [response[5] for response in responses]
use_gpt = [response[7] for response in responses]


# Create a dictionary to count the number of responses for each faculty and ChatGPT usage
faculty_gpt_counts = {}
for faculty, gpt in zip(faculties, use_gpt):
    if faculty in faculty_gpt_counts:
        if gpt in faculty_gpt_counts[faculty]:
            faculty_gpt_counts[faculty][gpt] += 1
        else:
            faculty_gpt_counts[faculty][gpt] = 1
    else:
        faculty_gpt_counts[faculty] = {gpt: 1}

# Extract the data for the bar chart
#print(faculty_gpt_counts)
yes=[faculty_gpt_counts[key]['Yes'] for key in faculty_gpt_counts if 'Yes'in faculty_gpt_counts[key]]
no=[faculty_gpt_counts[key]['No']if 'No'in faculty_gpt_counts[key] else 0 for key in faculty_gpt_counts  ]
categories= [i.upper() for i in faculty_gpt_counts.keys()]

#print(faculty_gpt_counts)
bar_width = 0.35
r1 = list(range(len(categories)))
r2 = [x + bar_width for x in r1]

plt.bar(r1, yes, color='green', width=bar_width, edgecolor='white', label='Yes')
plt.bar(r2, no, color='red', width=bar_width, edgecolor='white', label='No')
plt.title('Use of ChatGPT in diffrent Fields of Study')
plt.xlabel('Faculties')
plt.ylabel('Responses')
plt.xticks([r + bar_width/2 for r in range(len(categories))], categories)
plt.legend()



