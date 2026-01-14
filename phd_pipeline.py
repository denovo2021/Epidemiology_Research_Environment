import matplotlib.pyplot as plt
import pandas as pd

# 背景を黒に設定
plt.style.use('dark_background')

# データ: 人口100万人あたりの博士号取得者数推移 (OECD/NISTEPデータに基づく概算)
# 日本は2008年頃をピークに減少傾向にあるのが特徴的（The "Japan Paradox"）
data = {
    'Year': [2008, 2010, 2012, 2014, 2016, 2018, 2020],
    'Germany': [250, 280, 310, 335, 350, 360, 370],  # 非常に高い伸び
    'UK':      [260, 275, 290, 305, 315, 325, 330],  # 堅調な増加
    'USA':     [220, 230, 240, 255, 265, 275, 285],  # 安定した増加
    'Japan':   [131, 126, 122, 118, 117, 118, 120]   # 減少・停滞 (Peak around 2008)
}

df = pd.DataFrame(data)

# 図の生成
fig, ax = plt.subplots(figsize=(10, 6))

# プロット
# 比較国は寒色系やグレーで表示し、日本を赤で強調
ax.plot(df['Year'], df['Germany'], label='Germany', linestyle='-', color='lime', alpha=0.8, linewidth=2)
ax.plot(df['Year'], df['UK'], label='UK', linestyle='-', color='cyan', alpha=0.8, linewidth=2)
ax.plot(df['Year'], df['USA'], label='USA', linestyle='--', color='white', alpha=0.6, linewidth=1.5)
ax.plot(df['Year'], df['Japan'], label='Japan', color='#ff4444', linewidth=4, marker='o', zorder=10)

# タイトルとラベル設定
ax.set_title('Talent Pipeline: PhD Graduates per Million Population', fontsize=15, color='white', fontweight='bold')
ax.set_xlabel('Year', fontsize=12, color='white')
ax.set_ylabel('PhD Graduates (per million)', fontsize=12, color='white')

# 凡例の設定
ax.legend(facecolor='black', edgecolor='white', loc='upper left')

# グリッド線
ax.grid(True, linestyle=':', alpha=0.3, color='gray')

# 注釈
# 日本の減少傾向を強調 - 位置を線の上に修正
ax.annotate('Peaked ~2008\nDecreasing Trend',
            xy=(2014, 118),           # 矢印の先端 (データ点)
            xytext=(2014, 170),       # テキストの位置 (線の上に配置)
            arrowprops=dict(arrowstyle="->", color='#ff4444', lw=1.5),
            color='#ff4444', fontsize=12, fontweight='bold', ha='center')

plt.tight_layout()
plt.savefig("phd_pipeline.png",dpi=600)
plt.show()