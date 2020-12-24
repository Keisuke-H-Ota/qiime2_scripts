# Qiime2 の解析データから細菌の構成率の分布を箱ひげ図で表す方法

このレポジトリには Qiita に投稿した[Qiime2 の解析データから細菌の構成率の分布を箱ひげ図で表す方法](https://qiita.com/keisuke-ota/items/cfd5d0cf835b99d24edd)という記事に公開している script を公開しています。詳細はこちらの記事をご覧ください。

## alt_comp_plot.py について

このプログラムは[Qiime2を用いた 16S rRNA 菌叢解析](https://qiita.com/keisuke-ota/items/6399b2f2f7459cd9e418)で得られた細菌群集データから、*Fimicutes* 門の構成率の分布を可視化することができます。
[Altair](https://altair-viz.github.io/index.html) は python のグラフ作成ライブラリで、[こちらの記事](https://qiita.com/keisuke-ota/items/80d64153c499c8cc4774)にも使用例を載せています。Altair には Pandas の DataFrame で可視化データを入力することで、インターアクティブなグラフを作成することができます。
