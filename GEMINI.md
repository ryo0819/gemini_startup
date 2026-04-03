# Project Context:FastAPIによるAPIの実装

## Goals
- REST APIでGETリクエストに対して「Hello World」とレスポンスを返す
- REST APIでPOSTリクエストとリクエストボディに対して「Hello World, ${受け取ったリクエストボディ}」とレスポンスを返す

## Tech Stack
- Python 3.12+
- FastAPI
- Pydantic v2 (for validation)

## Development Rules
- Type Hints: すべての関数と変数に型ヒントを必須とする。`mypy` でエラーが出ない書き方をする
- Lint: Flake8に違反しないコードの書き方をする
- Pydantic Models: リクエストとレスポンスのスキーマは必ず Pydantic モデルで定義し、`app/schemas/` に配置する

## Directory Structure
- `/app/api/`: エンドポイント

## Instructions
- .gitignoreファイルを作成して、「.」から始まるファイルをgitにプッシュしないようにしてください
- 複雑なロジックを書く前に、まず「実行プラン」を提示して私の承認を得てください
- 新しいエンドポイントを追加する際は、必ず `pytest` を用いたテストコードの案も提示してください
