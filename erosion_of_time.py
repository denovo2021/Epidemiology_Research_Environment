import matplotlib.pyplot as plt

# Style settings: Dark background
plt.style.use('dark_background')

def plot_research_time_pie():
    """
    Slide 7: Erosion of Research Time (FY2023 Data)
    Source: MEXT "Survey on Full-Time Equivalency (FTE) of University Faculty (FY2023)" Table 1.
    """
    # FY2023 Activity Time Allocation Data (%)
    labels = ['Research', 'Education', 'Clinical/Social Contribution', 'Administration']
    sizes = [31.0, 31.0, 20.1, 17.9]
    # #4A6572 can be dark on pure black, so the legend box will provide contrast
    colors = ['#F0455C', '#3498db', '#4A6572', '#95a5a6']
    
    # Explode the 'Research' section to emphasize the erosion
    explode = (0.1, 0, 0, 0) 

    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Pie chart construction
    wedges, texts, autotexts = ax.pie(
        sizes, 
        explode=explode, 
        labels=labels, 
        autopct='%1.1f%%',
        startangle=140, 
        colors=colors,
        textprops={'color': 'white', 'fontsize': 12},
        pctdistance=0.85
    )

    # Convert to donut chart for modern aesthetics
    centre_circle = plt.Circle((0,0), 0.70, fc='black')
    fig.gca().add_artist(centre_circle)

    # Style percentage labels
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_weight('bold')

    ax.set_title("Faculty Time Allocation in Japan (FY2023)\n'The Erosion of Research Time'", 
                 color='white', fontsize=15, fontweight='bold', pad=20)

    # Legend configuration with background box for visibility
    # frameon=True and facecolor help distinguish patches from the background
    ax.legend(wedges, labels, title="Activities", loc="center left", 
              bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12, title_fontsize=13, 
              frameon=True, facecolor='#1A1A1A', edgecolor='#444444')

    plt.tight_layout()
    return fig

if __name__ == "__main__":
    plot_research_time_pie()
    # Path updated as per user request
    plt.savefig("Dataerosion_of_time.png", dpi=600)
    plt.show()