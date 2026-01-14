import matplotlib.pyplot as plt
import pandas as pd

# Style settings: Dark background for slide presentations
plt.style.use('dark_background')

def plot_investment_stagnation_bar():
    """
    Slide 8: Investment Stagnation (International Comparison)
    Source: NISTEP "Science and Technology Indicators 2024" Figure 4-2-4.
    Refers to the Growth Index of Higher Education Expenditure on R&D (HERD), 
    where the year 2000 is indexed at 100.
    """
    # Growth index values circa 2021/2022 (Base year 2000 = 100)
    # Japan shows near-zero real growth compared to the significant expansion in other nations.
    data = {
        'Country': ['Japan', 'Germany', 'USA', 'China'],
        'Index': [104, 210, 230, 1700]
    }
    df = pd.DataFrame(data)
    
    # Color palette optimized for dark backgrounds
    colors = ['#95a5a6', '#f1c40f', '#2980b9', '#e74c3c']

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Bar chart construction
    bars = ax.bar(df['Country'], df['Index'], color=colors, alpha=0.9, width=0.6)

    # Display precise index values on top of the bars for clarity
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 20,
                f'{int(height)}', ha='center', va='bottom', 
                color='white', fontsize=12, fontweight='bold')

    ax.set_title("Higher Education Expenditure on R&D (HERD)\nGrowth Index Comparison (2000=100)", 
                 color='white', fontsize=14, fontweight='bold', pad=30)
    ax.set_ylabel("Growth Index (Year 2000 = 100)", color='white', fontsize=12)
    
    # Grid and spine styling
    ax.yaxis.grid(True, linestyle='--', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_alpha(0.3)
    ax.spines['bottom'].set_alpha(0.3)

    # Annotation to emphasize Japan's stagnation ("Quiet Crisis")
    ax.annotate('Japan: Stagnant (+4%)', 
                xy=(0, 104), xytext=(0.5, 600),
                arrowprops=dict(facecolor='white', shrink=0.05, width=1, headwidth=8),
                fontsize=12, color='white', fontweight='bold')

    # Legend for country identification with larger font as requested
    ax.legend(bars, df['Country'], loc='upper left', fontsize=12, frameon=False)

    plt.tight_layout()
    return fig

if __name__ == "__main__":
    plot_investment_stagnation_bar()
    plt.savefig("/Users/tk/Documents/TMDU/疫学会若手の会/Slides/Data/investment_stagnation.png", dpi=600)
    plt.show()