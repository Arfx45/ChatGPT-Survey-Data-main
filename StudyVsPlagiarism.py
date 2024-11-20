import matplotlib.pyplot as plt
import csv
import numpy as np

# Read in the CSV file
with open('GPTResponses.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    categories = []
    response_counts = {'Yes': [], 'No': []}
    for row in reader:
        category = row[5]  # Use column F for categories
        if category not in categories:
            categories.append(category)
            response_counts['Yes'].append(0)
            response_counts['No'].append(0)
        response = row[9]
        response_counts[response][categories.index(category)] += 1

# Create the figure and axis objects
fig, ax = plt.subplots()

# Set the bar width and position
bar_width = 0.35
bar_position = np.arange(len(categories))

# Create the bar chart
ax.bar(bar_position - bar_width/2, response_counts['Yes'], width=bar_width, color='green', label='Yes')
ax.bar(bar_position + bar_width/2, response_counts['No'], width=bar_width, color='red', label='No')

# Add labels and title
ax.set_xticks(bar_position)
ax.set_xticklabels(categories)
ax.set_ylabel('Yes/No Count')
ax.set_xlabel('Faculties')
ax.set_title('Yes/No Responses to "Do you believe the use of ChatGPT condones plagiarism?" by Faculty')
ax.legend()

# Display the plot
plt.show()