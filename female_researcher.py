import matplotlib.pyplot as plt

# 背景を黒に設定
plt.style.use('dark_background')

# データ: 女性研究者の割合 (OECD比較)
countries = ['Japan', 'Korea', 'EU Average', 'UK', 'USA', 'Latvia (Top)']
# 実際の2021年頃のOECDデータに基づく概算値 (Japan: ~17.5%)
ratios = [17.5, 23.0, 34.0, 38.0, 39.0, 52.0]

# 色設定: 日本を目立つ赤(#ff4444)に、他を落ち着いたグレー(#cccccc)に
colors = ['#ff4444' if x == 'Japan' else '#cccccc' for x in countries]

# 図の生成
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(countries, ratios, color=colors)

# タイトルと軸ラベル
ax.set_title('Diversity: Female Researcher Ratio (OECD, 2021)', fontsize=15, color='white', fontweight='bold')
ax.set_ylabel('Percentage (%)', fontsize=12, color='white')
ax.set_ylim(0, 65) # 矢印のためのスペースを確保するため上限を少し上げる

# 数値ラベルの追加
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}%', 
            ha='center', va='bottom', fontweight='bold', color='white', fontsize=11)

# 注釈の修正: "Lowest in OECD" が "17.5%" と重ならないよう、矢印を使って上部に配置
# xy=(バーの中央X座標, バーの高さ), xytext=(テキスト配置座標)
ax.annotate('Lowest in OECD',
            xy=(0, 20),                # 矢印の先端 (バーの数値ラベルの少し上)
            xytext=(0.5, 35),          # テキストの位置 (右斜め上に配置してスペース確保)
            arrowprops=dict(arrowstyle="->", color='#ff4444', lw=1.5),
            color='#ff4444', fontsize=12, fontweight='bold', ha='center')

# グリッド (Y軸のみ)
ax.grid(axis='y', linestyle=':', alpha=0.3, color='gray')

plt.tight_layout()
plt.savefig("female_researcher.png", dpi=600)
plt.show()