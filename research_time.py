import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Data Preparation
# Source: MEXT Full-time Equivalent (FTE) Survey on University Faculty
# 2023 Data was released in June 2024.
# Note: "Service/Other" includes Social Service (Clinical practice), Management, etc.
data = {
    'Year': ['2002', '2008', '2013', '2018', '2023'],
    'Research':       [46.5, 36.5, 35.0, 32.9, 32.1], # Continued decline
    'Education':      [23.9, 28.6, 30.6, 33.1, 30.1], # Decreased in 2023
    'Service / Other':[29.6, 34.9, 34.4, 34.0, 37.8]  # Increased significantly
}
df = pd.DataFrame(data)

# 2. Plot Setup (Dark Mode)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 7))

# Ensure total black background
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

bar_width = 0.6

# 3. Create Stacked Bars
# Bottom: Research (The key metric - Cyan/Blue)
p1 = ax.bar(df['Year'], df['Research'], 
            width=bar_width, color='#00E5FF', label='Research', zorder=3)

# Middle: Education (Orange)
p2 = ax.bar(df['Year'], df['Education'], 
            width=bar_width, bottom=df['Research'], 
            color='#FFAB00', label='Education', zorder=3)

# Top: Service / Other (Grey/Slate - includes Clinical for Medics)
bottom_service = np.array(df['Research']) + np.array(df['Education'])
p3 = ax.bar(df['Year'], df['Service / Other'], 
            width=bar_width, bottom=bottom_service, 
            color='#546E7A', label='Service / Other (incl. Clinical)', zorder=3)

# 4. Styling
# Y-axis
ax.set_ylim(0, 100)
ax.set_yticks(np.arange(0, 101, 10))
ax.set_yticklabels([f'{x}%' for x in np.arange(0, 101, 10)], color='white', fontsize=9)
ax.tick_params(axis='y', length=0)

# X-axis
ax.tick_params(axis='x', colors='white', labelsize=11)
ax.set_xlabel('Year', color='white', fontsize=11)

# Grid
ax.yaxis.grid(True, linestyle='-', which='major', color='gray', alpha=0.3, zorder=0)
ax.set_axisbelow(True)

# Spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('white')

# Legend with background box for visibility
# facecolor and frameon ensure the grey category label is legible against the black background
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3, 
          frameon=True, facecolor='#1A1A1A', edgecolor='#444444', labelcolor='white', fontsize=10)

# Title
ax.set_title('Trends in Time Allocation of University Faculty in Japan\n(2002 - 2023)', 
             color='white', fontsize=13, pad=45)

# 5. Add Value Labels for "Research" (Key Insight)
for i, v in enumerate(df['Research']):
    ax.text(i, v/2, f'{v}%', ha='center', va='center', 
            color='black', fontweight='bold', fontsize=10)

# Add Source Note
plt.figtext(0.99, 0.02, 'Source: MEXT Full-time Equivalent (FTE) Data Survey (2024 Release)', 
            horizontalalignment='right', color='gray', fontsize=8)

plt.tight_layout()
plt.savefig("erosion_of_time.png", dpi=600)
plt.show()