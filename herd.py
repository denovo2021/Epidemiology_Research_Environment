import matplotlib.pyplot as plt
import pandas as pd

# 背景を黒に設定
plt.style.use('dark_background')

# データ: 日本の大学研究開発費（HERD）の実質的な停滞を示すシミュレーションデータ
# 米国とドイツを追加し、先進国標準の成長と比較
data = {
    'Year': [2000, 2005, 2010, 2015, 2020, 2023],
    'China (Growth)': [100, 300, 600, 900, 1200, 1500], # 急成長
    'Korea (Growth)': [100, 150, 200, 300, 400, 450],   # 力強い成長
    'USA (Steady)':   [100, 120, 135, 148, 165, 175],   # 堅実な成長 (追加)
    'Germany (Steady)':[100, 115, 130, 145, 160, 170],  # 堅実な成長 (追加)
    'Japan (Flat)':   [100, 102, 101, 103, 102, 101]    # 停滞
}

df = pd.DataFrame(data)

# 図の生成
fig, ax = plt.subplots(figsize=(10, 6))

# プロット
# 他国は寒色系・グレー系で抑え、日本を赤で強調
ax.plot(df['Year'], df['China (Growth)'], label='China', linestyle='--', color='#555555', alpha=0.6)
ax.plot(df['Year'], df['Korea (Growth)'], label='Korea', linestyle='--', color='#777777', alpha=0.6)
ax.plot(df['Year'], df['USA (Steady)'], label='USA', linestyle='-', color='cyan', alpha=0.8, linewidth=2)
ax.plot(df['Year'], df['Germany (Steady)'], label='Germany', linestyle='-', color='lime', alpha=0.8, linewidth=2)
ax.plot(df['Year'], df['Japan (Flat)'], label='Japan', color='#ff4444', linewidth=4, zorder=10)

# タイトルとラベル設定
ax.set_title('The Crisis in Universities: HERD Real Growth Index (2000=100)', fontsize=15, color='white', fontweight='bold')
ax.set_xlabel('Year', fontsize=12, color='white')
ax.set_ylabel('Index (2000 = 100)', fontsize=12, color='white')

# 凡例の設定（背景黒に対応）
ax.legend(facecolor='black', edgecolor='white', loc='upper left')

# グリッド線（控えめに）
ax.grid(True, linestyle=':', alpha=0.3, color='gray')

# 注釈の修正: 重なりを防ぐため、矢印を使ってテキストを離れた位置に配置
# 日本の線は一番下(100付近)にあるため、テキストを上に配置して矢印で指す
ax.annotate('Zero Real Growth\n("The Flatline")',
            xy=(2015, 103),           # 矢印の先端 (データの位置)
            xytext=(2012, 400),       # テキストの位置 (グラフの空白部分へ移動)
            arrowprops=dict(arrowstyle="->", color='#ff4444', lw=1.5),
            color='#ff4444', fontsize=12, fontweight='bold', ha='center')

plt.tight_layout()
plt.savefig("herd.png", dpi=600)
plt.show()