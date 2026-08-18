# Theory about this code:

# This code demonstrates how to create a Fruit Distribution Dashboard using Matplotlib.
# It creates a Pie Chart and Donut Chart to show the distribution of different fruits.
# The sizes, labels, colors, and explode values are used to customize the charts.
# Percentages, legends, titles, and styling are added to make the visualization more informative.
# The code also calculates the total, percentage, and ranking of each fruit and displays the statistics.
# Overall, it demonstrates how Matplotlib can create professional and detailed data visualization dashboards.



import matplotlib.pyplot as plt
import numpy as np

# Fruit data
sizes = [10, 101, 100, 500]
labels = ["Apples", "Bananas", "Cherries", "Dates"]
colors = ["black", "hotpink", "b", "#4CAF50"]
explode = [0, 0.3, 0, 0]

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Fruit Distribution Dashboard', fontsize=18, weight='bold', y=1.02)

# Pie chart
wedges, texts, autotexts = ax1.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    startangle=90,
    shadow=True,
    wedgeprops={'linewidth': 2, 'edgecolor': 'white'},
    textprops={'fontsize': 12, 'weight': 'bold'},
    pctdistance=0.85
)

for text in texts:
    text.set_color('#2d3748')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
ax1.set_title('Pie Chart - Fruits', fontsize=16, weight='bold', pad=15)

# Donut chart
wedges2, texts2, autotexts2 = ax2.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'linewidth': 2, 'edgecolor': 'white', 'width': 0.5},
    textprops={'fontsize': 11, 'weight': 'bold'}
)

for text in texts2:
    text.set_color('#2d3748')
for autotext in autotexts2:
    autotext.set_color('#2d3748')
    autotext.set_weight('bold')
ax2.set_title('Donut Chart - Fruits', fontsize=16, weight='bold', pad=15)

# Add legend
fig.legend(
    labels,
    loc='lower center',
    ncol=4,
    fontsize=11,
    frameon=True,
    shadow=True,
    bbox_to_anchor=(0.5, -0.05)
)

# Add statistics table
stats_text = "Fruit Statistics:\n"
total = sum(sizes)
sorted_data = sorted(zip(labels, sizes), key=lambda x: x[1], reverse=True)
for label, value in sorted_data:
    percentage = (value / total) * 100
    stats_text += f"{label}: {value} ({percentage:.1f}% of total)\n"

plt.figtext(0.5, -0.15, stats_text, ha='center', fontsize=10, 
            bbox={'facecolor': '#f7fafc', 'alpha': 0.8, 'pad': 10, 'edgecolor': '#e2e8f0'})

plt.tight_layout()
plt.subplots_adjust(bottom=0.25)
plt.show()