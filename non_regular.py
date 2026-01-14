import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Data Preparation
# Estimated percentages based on the visual data
data = {
    'Age Group': ['Age <35', 'Age 35-39', 'Age 40-44', 'Age 45+'],
    'Fixed-Term': [75, 64, 42, 15],       # Red part (Fixed-Term)
    'Tenured':    [25, 36, 58, 85]        # Blue part (Tenured/Stable)
}
df = pd.DataFrame(data)

# 2. Plot Setup for Dark Background
plt.style.use('dark_background')  # Use built-in dark style
fig, ax = plt.subplots(figsize=(6, 7))

# Explicitly ensure the background is black
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

bar_width = 0.65

# 3. Create Stacked Bars
# Fixed-Term (Bottom: Red)
color_fixed = '#F0455C'
p1 = ax.bar(df['Age Group'], df['Fixed-Term'], 
            width=bar_width, color=color_fixed, label='Fixed-Term Contract', zorder=3)

# Tenured (Top: Blue/Grey)
color_tenured = '#4A6572'
p2 = ax.bar(df['Age Group'], df['Tenured'], 
            width=bar_width, bottom=df['Fixed-Term'], color=color_tenured, label='Tenured / Stable', zorder=3)

# 4. Styling (English Only)
# Y-axis
ax.set_ylim(0, 100)
ax.set_yticks(np.arange(0, 101, 10))
ax.set_yticklabels([f'{x}%' for x in np.arange(0, 101, 10)], color='white')
ax.tick_params(axis='y', length=0) # Hide tick marks

# X-axis
ax.tick_params(axis='x', colors='white')

# Grid
ax.yaxis.grid(True, linestyle='-', which='major', color='gray', alpha=0.3, zorder=0)
ax.set_axisbelow(True)

# Spines (Borders)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('gray')

# Legend with adjusted background for visibility
# frameon=True and facecolor ensure dark categories are legible
ax.legend(loc='upper right', frameon=True, fontsize=12, labelcolor='white', 
          facecolor='#1A1A1A', edgecolor='#444444')

# Title
ax.set_title('University Faculty Tenure Status by Age', color='white', fontsize=12, pad=20)

plt.tight_layout()
plt.savefig("tenure_status_by_age.png", dpi=600)
plt.show()