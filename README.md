# Karaage - データ分析とプレゼンテーションツール

このリポジトリは、Kindle購入履歴の分析とMarpを使用したプレゼンテーション作成のためのツールとサンプルを含んでいます。

## 概要

このプロジェクトは主に2つの部分から構成されています：
1. Kindleの購入履歴データを分析し、視覚化するPythonスクリプト
2. Marpを使用したマークダウンベースのプレゼンテーション作成サンプル

## Kindle分析ツール

### 機能
- Kindle購入履歴CSVファイルの読み込み
- 年ごとの月別購入冊数の分析
- matplotlib を使用したグラフ作成
- 購入傾向の可視化

### 使用方法
1. Kindleの購入履歴をCSV形式でエクスポート
2. `kindle/analysis_kindle.py` スクリプトを実行
3. 生成されたグラフを確認

### 必要なライブラリ
- pandas
- numpy
- matplotlib
- japanize_matplotlib

### サンプル出力
リポジトリには以下のサンプル出力が含まれています：
- `kindle_count_graph.png`: 購入冊数のグラフ
- `compare_3yr_per_month.png`: 3年間の月別比較グラフ
- `kindle_count_graph_yr.png`: 年別購入冊数グラフ

## Marpプレゼンテーション

### 概要
[Marp](https://marp.app/)を使用したマークダウンベースのプレゼンテーション作成サンプルです。

### 機能
- マークダウン形式でスライド作成
- カスタムテーマの適用
- 数式表示
- コードハイライト
- 背景画像の設定

### サンプルファイル
- `marp/test_marp.md`: 基本的なMarpの使用例
- `marp/style_test.md`: スタイル設定のテスト
- `marp/marp_themes/test.css`: カスタムテーマ定義

### 使用方法
1. Marpをインストール
2. マークダウンファイルを編集
3. Marpを使用してPDFまたはHTMLにエクスポート

## 環境設定

このリポジトリには仮想環境の設定が含まれています：

```bash
# 仮想環境の作成と有効化
python -m venv .venv
source .venv/bin/activate  # Linuxの場合
# または
.venv\Scripts\activate  # Windowsの場合

# 必要なパッケージのインストール
pip install -r requirements.txt
```

## 注意事項

- Kindle分析ツールは個人の購入履歴を分析するためのものです
- サンプルデータは含まれていますが、実際の使用には自身のデータが必要です
- Marpの使用には別途Marpのインストールが必要です

## ライセンス

MIT

## 作者

msyk9038
