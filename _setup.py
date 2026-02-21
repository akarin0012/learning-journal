import os

BASE = os.path.dirname(os.path.abspath(__file__))

files = {
    "README.md": """# Learning Journal

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
""",

    os.path.join("templates", "til.md"): """# タイトル

- 日付: YYYY-MM-DD
- カテゴリ: （例: Python / Git / ネットワーク）

## 学んだこと

（ここに内容を書く）

## 参考リンク

- [リンクタイトル](URL)
""",

    os.path.join("templates", "topic.md"): """# トピックタイトル

- カテゴリ: （例: Python / TypeScript / Docker）
- 最終更新: YYYY-MM-DD

## 概要

（このトピックの概要を書く）

## 詳細

### セクション1

（内容）

### セクション2

（内容）

## メモ・Tips

- （気づいたことや覚えておきたいこと）

## 参考リンク

- [リンクタイトル](URL)
""",

    os.path.join("templates", "reading.md"): """# 書籍タイトル

- 著者:
- 読了日:
- 評価: ★★★☆☆

## 要約

（全体の要約）

## 章ごとのメモ

### 第1章: タイトル

（メモ）

## 感想・学び

（自分の言葉でまとめる）

## 印象に残ったフレーズ

> （引用）

## 参考リンク

- [リンクタイトル](URL)
""",

    os.path.join("templates", "plan-monthly.md"): """# YYYY年MM月 学習計画

## 今月の目標

- [ ] 目標1
- [ ] 目標2
- [ ] 目標3

## 週次の予定

### Week 1（MM/DD - MM/DD）

- [ ] タスク

### Week 2（MM/DD - MM/DD）

- [ ] タスク

### Week 3（MM/DD - MM/DD）

- [ ] タスク

### Week 4（MM/DD - MM/DD）

- [ ] タスク

## 振り返り

（月末に記入）

### できたこと

-

### 課題・改善点

-

### 来月に向けて

-
""",

    os.path.join("til", "README.md"): """# TIL (Today I Learned)

日々学んだことの短いメモ。1ファイル = 1トピック。

## ファイル命名規則

`YYYY-MM-DD-タイトル.md`（例: `2026-02-20-git-rebase.md`）

## 一覧

<!-- 新しい TIL を追加したらここにリンクを追記する -->
<!-- - [タイトル](YYYY-MM-DD-タイトル.md) - YYYY-MM-DD -->
""",

    os.path.join("topics", "programming", "README.md"): """# Programming / 技術ノート

プログラミングや技術に関する学習ノート。言語・フレームワークごとにサブフォルダを作成して整理する。

## カテゴリ例

- `python/` - Python 関連
- `typescript/` - TypeScript / JavaScript 関連
- `git/` - Git / バージョン管理
- `docker/` - Docker / コンテナ技術
- `web/` - Web 技術全般

## ノート一覧

<!-- 新しいノートを追加したらここにリンクを追記する -->
""",

    os.path.join("topics", "reading", "README.md"): """# 読書メモ

書籍の要約・感想・学びをまとめる。

## ファイル命名規則

書籍タイトルをベースにしたファイル名（例: `pragmatic-programmer.md`）

## 読書リスト

<!-- 新しい読書メモを追加したらここにリンクを追記する -->
<!-- - [書籍タイトル](ファイル名.md) - ★★★☆☆ -->
""",

    os.path.join("topics", "other", "README.md"): """# その他の学習

語学、資格、その他技術以外の学習ノート。

## ノート一覧

<!-- 新しいノートを追加したらここにリンクを追記する -->
""",

    os.path.join("plans", "README.md"): """# 学習計画

年間目標と月次計画で学習の方向性を管理する。

## ファイル構成

- `YYYY-yearly-goals.md` - 年間目標
- `YYYY-MM.md` - 月次計画（目標 + 振り返り）

## 計画一覧

### 2026年

- [2026年 年間目標](2026-yearly-goals.md)
- [2026年2月](2026-02.md)
""",

    os.path.join("plans", "2026-yearly-goals.md"): """# 2026年 年間目標

## 大目標

- [ ] （例: Web 開発の基礎を固める）
- [ ] （例: 技術書を6冊読む）
- [ ] （例: 英語力を向上させる）

## 四半期ごとの方針

### Q1（1月 - 3月）

- [ ] 目標

### Q2（4月 - 6月）

- [ ] 目標

### Q3（7月 - 9月）

- [ ] 目標

### Q4（10月 - 12月）

- [ ] 目標

## 年末の振り返り

（年末に記入）
""",

    os.path.join("plans", "2026-02.md"): """# 2026年2月 学習計画

## 今月の目標

- [ ] 目標1
- [ ] 目標2
- [ ] 目標3

## 週次の予定

### Week 1（02/02 - 02/08）

- [ ] タスク

### Week 2（02/09 - 02/15）

- [ ] タスク

### Week 3（02/16 - 02/22）

- [ ] タスク

### Week 4（02/23 - 02/28）

- [ ] タスク

## 振り返り

（月末に記入）

### できたこと

-

### 課題・改善点

-

### 来月に向けて

-
""",

    ".gitignore": """# OS generated files
.DS_Store
Thumbs.db
Desktop.ini

# Editor
.vscode/
*.swp
*.swo
*~

# Cursor
.cursor/
""",
}

for rel_path, content in files.items():
    full_path = os.path.join(BASE, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {rel_path}")

print("Done!")
