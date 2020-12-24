import os
import altair as alt
import pandas as pd

# 分類階級の指定。Phylum は level 2 である。
l_select = 'L2' 

# カレントディレクトリ取得
cwd = os.getcwd()

# カウントデータの取得
count_path = [l_select,'table.tsv'] 
count_file = os.path.join(cwd, *count_path)
count = pd.read_table(count_file, sep='\t', index_col=0 ,header=1).T # header=1に注意

# 組成データに変換
comp = count.apply(lambda x: x/sum(x), axis=1)

# メタデータの取得
md_path = ['metadata.tsv']
md_file = os.path.join(cwd, *md_path)
md = pd.read_table(md_file, sep='\t', index_col=0 ,header=0)

# 行名を str 型に変換（今回の行名は数字のため int型で処理されてしまっている）
comp.index = comp.index.astype(str)
md.index = md.index.astype(str)

# カウントデータとメタデータを結合。（行名が str 型でなければ結合しない）
df = pd.concat([comp,md], axis=1)

# 今回は Ileum （回腸）と Rectum （直腸）の菌叢を調べる。（他の部位はサンプル数が少なかったため）
df = df[df['biopsy_location'].isin(['Ileum','Rectum'])]

# Altair の実行
boxplot = alt.Chart(df).mark_boxplot(size=100,ticks=alt.MarkConfig(width=30), median=alt.MarkConfig(color='black',size=100)).encode(
        alt.X('diagnosis',sort = alt.Sort(['CD','UC','nonIBD']), axis=alt.Axis(labelFontSize=15, ticks=True, titleFontSize=18, title='Diagnosis')),
        alt.Y('D_0__Bacteria;D_1__Firmicutes', axis=alt.Axis(format='%', labelFontSize=15, ticks=True, titleFontSize=18, grid=False,domain=True, title='Firmicutes'), scale=alt.Scale(domain=[0,0.02])),
        alt.Color('diagnosis'),
        alt.Column('biopsy_location', header=alt.Header(labelFontSize=15, titleFontSize=18), sort = alt.Sort(['Ileum','Rectum']), title='Biopsy')
    ).properties(
        width=600,
        height=500,
    )

# 図の表示
boxplot.show()