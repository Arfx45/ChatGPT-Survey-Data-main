import matplotlib.pyplot as plt
import csv
import numpy as np

# Read in the CSV file
with open('GPTResponses.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    categories = []
    response_counts = {'Assignments': [], 'Homework': [], 'About 5-10 time a week': [], 'Once a Week': [], '20+ Times per week': []}
    for row in reader:
        category = row[5]  # Use column F for categories
        if category not in categories:
            categories.append(category)
            response_counts['Assignments'].append(0)
            response_counts['Homework'].append(0)
            response_counts['About 5-10 time a week'].append(0)
            response_counts['Once a Week'].append(0)
            response_counts['20+ Times per week'].append(0)
        response = row[8]
        response_counts[response][categories.index(category)] += 1

# Create the figure and axis objects
fig, ax = plt.subplots()

# Set the bar width and position
bar_width = 0.15
bar_position = np.arange(len(categories))

# Create the bar chart
ax.bar(bar_position - bar_width*2, response_counts['Assignments'], width=bar_width, color='green', label='Assignments')
ax.bar(bar_position, response_counts['Homework'], width=bar_width, color='red', label='Homework')
ax.bar(bar_position + bar_width*2, response_counts['About 5-10 time a week'], width=bar_width, color='blue', label='About 5-10 time a week')
ax.bar(bar_position + bar_width, response_counts['Once a Week'], width=bar_width, color='yellow', label='Once a Week')
ax.bar(bar_position - bar_width, response_counts['20+ Times per week'], width=bar_width, color='purple', label='20+ Times per week')


# Add labels and title
ax.set_xticks(bar_position)
ax.set_xticklabels(categories)
ax.set_ylabel('Responses')
ax.set_xlabel('Faculties')
ax.set_title('Responses to "How often do you find yourself using ChatGPT?" by Faculty')
ax.legend()

# Display the plot
plt.show()