import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. データ準備 
# ユーザー提供のCSVテキスト（表4-1-6）から「分数カウント法・Top10%シェア」を抽出
# ---------------------------------------------------------
# 年次（各期間の中央値）: 2001-03 -> 2002, 2011-13 -> 2012, 2021-23 -> 2022
years = [2002, 2012, 2022]

# データ辞書（CSVから読み取った値をハードコード）
data = {
    'Japan': [5.86, 3.50, 1.67],      # 日本 (#4 -> #7 -> #13)
    'China': [2.94, 11.85, 36.24],    # 中国 (#8 -> #2 -> #1)
    'USA': [40.14, 31.06, 19.00],     # 米国 (#1 -> #1 -> #2)
    'Germany': [6.57, 5.76, 3.33],    # ドイツ (#3 -> #4 -> #5)
    'UK': [7.86, 6.45, 4.86],         # 英国 (#2 -> #3 -> #3)
    'South Korea': [1.33, 2.06, 1.75] # 韓国 (#14 -> #13 -> #9-13圏)
}

# DataFrame化
df = pd.DataFrame(data, index=years)

# ---------------------------------------------------------
# 2. グラフ描画設定 (ダークテーマ仕様)
# ---------------------------------------------------------
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 7), dpi=150)

# --- プロット設定 ---

# A. 注目国（太線・鮮やか）
# Japan: 赤
ax.plot(df.index, df['Japan'], marker='o', color='#FF5252', linewidth=4, label='Japan', zorder=10)
# China: 緑
ax.plot(df.index, df['China'], marker='s', color='#69F0AE', linewidth=3, label='China', zorder=9)
# USA: オレンジ (シェアが高いので目立つ)
ax.plot(df.index, df['USA'], marker='x', linestyle='-', color='#FFB74D', linewidth=3, label='USA', zorder=8)

# B. 比較国（細線・控えめ）
# Germany: 黄
ax.plot(df.index, df['Germany'], linestyle='--', color='#FFFF00', linewidth=1.5, label='Germany', alpha=0.8)
# UK: 紫
ax.plot(df.index, df['UK'], linestyle='--', color='#E040FB', linewidth=1.5, label='UK', alpha=0.8)
# South Korea: 青
ax.plot(df.index, df['South Korea'], linestyle='--', marker='^', color='#40C4FF', linewidth=1.5, label='South Korea', alpha=0.8)

# ---------------------------------------------------------
# 3. 装飾
# ---------------------------------------------------------
ax.set_title('Share of Top 10% Highly Cited Papers (Fractional Counting)', 
             fontsize=16, fontweight='bold', color='white', pad=20)
ax.set_ylabel('Share (%)', fontsize=12, color='white')
ax.set_xlabel('Year (3-year average midpoint)', fontsize=12, color='white')

# X軸の設定 (2002, 2012, 2022のみ表示)
ax.set_xticks(years)
ax.set_xticklabels(['2001-03', '2011-13', '2021-23'], fontsize=10)

# Y軸の範囲設定 (凡例スペース確保のため、最大値を少し余裕を持たせる)
# 中国の最大値36% + 余裕を持たせて45%まで
ax.set_ylim(0, 48)

# グリッド
ax.grid(True, which='major', axis='y', linestyle=':', color='gray', alpha=0.5)

# 凡例の設定 (左上に配置)
# データと重ならないよう、列数(ncol)を使って横長にするなど調整
ax.legend(fontsize=11, loc='upper left', ncol=3, frameon=False, labelcolor='white')

# 値の注釈 (最新値のみ)
for col in df.columns:
    last_val = df[col].iloc[-1]
    # テキストの色: 線と同じ色にする
    line_color = ax.get_lines()[df.columns.get_loc(col)].get_color()
    
    # 位置調整: JapanとKoreaが重なりやすいので微調整
    y_offset = 15
    if col == 'South Korea': y_offset = -20 
    if col == 'Japan': y_offset = -20 

    ax.annotate(f'{last_val}%', xy=(2022, last_val), xytext=(0, y_offset), 
                textcoords='offset points', ha='center', 
                color=line_color, fontweight='bold', fontsize=11)

# ---------------------------------------------------------
# 4. 出力
# ---------------------------------------------------------
plt.tight_layout()

# 画像保存
file_name = 'nistep_csv_plot.png'
plt.savefig(file_name, facecolor=fig.get_facecolor(), edgecolor='none')

plt.show()