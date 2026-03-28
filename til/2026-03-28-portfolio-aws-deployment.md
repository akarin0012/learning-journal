# ポートフォリオ移植と AWS デプロイ

- 日付: 2026-03-28
- カテゴリ: Next.js / AWS / CI/CD

## 学んだこと・やったこと

- 既存ポートフォリオを Next.js 静的エクスポート構成に寄せ、GitHub Actions で S3 へデプロイする流れを通した。
- S3 上ではアセットと HTML/JSON で Cache-Control を分け、CloudFront は必要なパスのみ invalidation する方針を理解した。
- GitHub Secrets（AWS キー、バケット名、CloudFront ディストリビューション ID 等）と AWS 側の IAM・バケット・ディストリビューション設定を対応付けた。
- private / public 公開の切り分け（環境変数と別インフラ）をドキュメントで整理した。

## 参考リンク

- portfolio リポジトリ README（デプロイ・Secrets）
- portfolio/docs/public-private-release.md
- portfolio/docs/aws-cost-investigation-runbook.md
