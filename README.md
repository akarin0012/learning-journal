# Learning Journal

日々の学習を記録し、成長を振り返るためのリポジトリ。

## ディレクトリ構造

```
learning-journal/
├── til/          # Today I Learned（日付ベースの短いメモ）
├── topics/       # トピック別の学習ノート（深掘り用）
│   ├── programming/  # プログラミング・技術
│   ├── reading/      # 読書メモ・書籍要約
│   └── other/        # 語学・資格など
├── plans/        # 学習計画・目標管理
└── templates/    # 記録テンプレート
```

## 使い方

### TIL（Today I Learned）を書く

1. `templates/til.md` をコピーして `til/` に配置
2. ファイル名は `YYYY-MM-DD-タイトル.md` 形式（例: `2026-02-20-git-rebase.md`）
3. 内容を記入してコミット

### トピック別ノートを書く

1. `templates/topic.md` をコピーして `topics/` の該当カテゴリに配置
2. 言語やフレームワークごとにサブフォルダを作ってもOK
3. 内容を記入してコミット

### 読書メモを書く

1. `templates/reading.md` をコピーして `topics/reading/` に配置
2. ファイル名は書籍名をベースに（例: `pragmatic-programmer.md`）
3. 章ごとにメモを追記していく

### 学習計画を立てる

1. `templates/plan-monthly.md` をコピーして `plans/` に配置
2. ファイル名は `YYYY-MM.md` 形式（例: `2026-02.md`）
3. 月末に振り返りセクションを記入

## コミットメッセージの規約

```
til: Git rebase の使い方を学んだ
topic: Python デコレータのノートを追加
reading: 達人プログラマーの読書メモを追加
plan: 2月の月次計画を作成
plan: 1月の振り返りを記入
```

プレフィックスで種類を区別し、内容を簡潔に書く。
