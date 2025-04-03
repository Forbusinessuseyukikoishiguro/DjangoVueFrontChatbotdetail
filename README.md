# Django & Vue.js 技術アドバイザーチャットボット

技術的な質問に対して構造化された回答を提供する、AI搭載の学習支援チャットボットです。Django、Vue.js、Python、HTML、CSSの開発について専門的な知識と丁寧な解説を提供します。

## 概要

このチャットボットは、Python + Streamlit + OpenAI APIを使用して構築されており、初級〜中級レベルの開発者に向けた技術支援ツールとして機能します。構造化された回答と公式ドキュメントへの参照を自動的に提供します。

## 特徴

- **専門分野**: Django、Vue.js、Python、HTML、CSS
- **構造化された回答**: 題名、見出し、サブ見出し、コードサンプルを含む体系的な説明
- **公式リソースの参照**: 回答に関連する公式ドキュメントへのリンクを自動提供
- **学習プランの提案**: 段階的な学習プロセスのガイダンス
- **エラー解決のサポート**: 一般的なエラーとその解決方法を提供

## セットアップ手順

### 環境構築

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化（Windows）
venv\Scripts\activate

# 必要なパッケージのインストール
pip install streamlit openai python-dotenv markdown
```

### アプリ実行

```bash
# アプリの起動
streamlit run new_app.py

# 起動成功時のメッセージ例
# You can now view your Streamlit app in your browser.
# Local URL: http://localhost:8501
# Network URL: http://192.168.43.229:8501
```

## 使用方法

1. アプリケーションを起動
2. OpenAI APIキーを入力（初回のみ）
3. 質問入力欄に技術的な質問を入力
4. 「送信」ボタンをクリック
5. 構造化された回答を受け取る

## 実行コマンド一覧

```bash
# 仮想環境の有効化
venv\Scripts\activate

# アプリの起動
streamlit run new_app.py

# pipのアップデート（オプション）
python.exe -m pip install --upgrade pip
```

## 将来の改善計画

1. **知識の資産化を円滑にする**
   - 調べた情報の自動取得機能の実装
2. **ユーザーの学習進捗の可視化**
   - 学習履歴のトラッキングと適切なアドバイス提示
3. **カスタマイズ機能の拡張**
   - UIデザインの改善
   - チャット履歴の保存機能
   - テーマ切り替え機能
4. **クラウドデプロイメント**
   - Streamlit Cloudへのデプロイ

## 注意事項

- OpenAI APIの使用料金に注意してください（GPT-3.5は比較的安価ですが、頻繁に使用すると料金が発生）
- 変更を加えた場合、ファイル保存時に自動的にアプリが更新されます
- 問題発生時はブラウザの更新またはアプリの再起動をお試しください

## 技術スタック

- **バックエンド**: Python, OpenAI API
- **フロントエンド**: Streamlit
- **依存関係管理**: venv, pip, requirements.txt

---

© 2025 技術アドバイザーチャットボット - Made with Streamlit and OpenAI

#Django #Vue.js #AI教育 #チャットボット #Python #HTML #CSS

*************************************************
altair==5.5.0
annotated-types==0.7.0
anyio==4.9.0
attrs==25.3.0
blinker==1.9.0
cachetools==5.5.2
certifi==2025.1.31
charset-normalizer==3.4.1
click==8.1.8
colorama==0.4.6
distro==1.9.0
gitdb==4.0.12
GitPython==3.1.44
h11==0.14.0
httpcore==1.0.7
httpx==0.28.1
idna==3.10
Jinja2==3.1.6
jiter==0.9.0
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
Markdown==3.7
MarkupSafe==3.0.2
narwhals==1.33.0
numpy==2.2.4
openai==1.70.0
packaging==24.2
pandas==2.2.3
pillow==11.1.0
protobuf==5.29.4
pyarrow==19.0.1
pydantic==2.11.2
pydantic_core==2.33.1
pydeck==0.9.1
python-dateutil==2.9.0.post0
python-dotenv==1.1.0
pytz==2025.2
referencing==0.36.2
requests==2.32.3
rpds-py==0.24.0
six==1.17.0
smmap==5.0.2
sniffio==1.3.1
streamlit==1.44.1
tenacity==9.1.2
tk==0.1.0
toml==0.10.2
tornado==6.4.2
tqdm==4.67.1
typing-inspection==0.4.0
typing_extensions==4.13.0
tzdata==2025.2
urllib3==2.3.0
watchdog==6.0.0
***************************************************
0414更新
