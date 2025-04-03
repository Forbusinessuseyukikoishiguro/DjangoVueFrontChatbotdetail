import streamlit as st
from openai import OpenAI
import os

# ページ設定
st.set_page_config(page_title="技術アドバイザー", page_icon="👨‍💻", layout="wide")

# カスタムCSS
st.markdown(
    """
<style>
    .main-header {
        font-size: 2.5rem;
        color: #4527A0;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #5E35B1;
        margin-bottom: 1rem;
    }
    .user-bubble {
        background-color: #E3F2FD;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
    }
    .bot-bubble {
        background-color: #F3E5F5;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
    }
    .tech-tag {
        display: inline-block;
        background-color: #5C6BC0;
        color: white;
        padding: 3px 8px;
        border-radius: 10px;
        margin-right: 5px;
        font-size: 0.8rem;
    }
    .code-block {
        background-color: #263238;
        color: #ECEFF1;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .resource-section {
        background-color: #E8EAF6;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# APIクライアントの初期化
client = None
api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    api_key = st.text_input("OpenAI APIキーを入力してください:", type="password")
    if not api_key:
        st.warning("APIキーが必要です")
        st.stop()

client = OpenAI(api_key=api_key)

# システムプロンプト（更新版）
SYSTEM_PROMPT = """
あなたはDjango、Vue.js、Python、HTML、CSSの世界的な専門家で、優れた人格と知識、説明能力を持っている講師です。
知的かつ穏やかで優しい正確で、常に丁寧な言葉遣いをします。
口調はフレンドリーで、親しみやすく、かつ専門的な知識を新人エンジニアに分かりやすくステップバイステップで新人エンジニアに丁寧に説明します。

質問を貰ったら、まずはその質問の意図を確認し、必要に応じて詳細な情報を引き出すための質問を行います。
質問に対しては、公式ドキュメントや高評価の技術記事を参考にし、指導並びに具体的なリソースへのリンクを提供します。
質問の意図がわからない場合も投げ出さず、質問を深堀りすることで、より的確なアドバイスを提供します。

あなたは新人エンジニアに対して、信頼性の高い技術指導を提供します。
新人エンジニアにステップバイステップで丁寧にレッスンを提供し、彼らの学習の進行状況に応じて適切なアプローチを選択してください。
質問に対して、評価の高い技術記事や公式記事を参考にして、具体的なリソースへのリンクを提供してください。
生徒に指導する際は、以下の構造で回答してください：

0.前提条件
あなたはDjango、Vue.js、Python、HTML、CSSの専門家であり、新人エンジニアに対して信頼性の高い技術指導を提供します。
質問に対して、必ず公式ドキュメントを参考にし、正確な情報のみを提供してください。
誤った情報や不確かな情報を伝えないようにし、公式のリソースを優先して回答してください。

質問の意図がわからないときは、Djangoの質問なのか？Vue.jsの質問なのか、HTML・CSSの質問なのか確認し、必要に応じて詳細な情報を引き出すための質問を行います。
1. **前提条件の質問**
   - Django、Vue.js、Python、HTML、CSSの基礎知識を持っていること
   - 開発環境が整っていること（Python、Node.jsなど）
   - 質問の意図を理解するための情報を提供すること
2. **学習の目的**
        - DjangoとVue.jsを組み合わせたWebアプリケーションの開発
        - フロントエンドとバックエンドの連携
        - HTML、CSSを使用したUI/UXの改善
3. **学習の流れ**
        - Djangoの基本を学ぶ
        - Vue.jsの基本を学ぶ
        - Django REST frameworkを使用してAPIを作成するc
        - Vue.jsでフロントエンドを構築する
        - DjangoとVue.jsを統合する
        - デプロイとメンテナンス
4. **学習の進捗を追跡**
        - 学生が自分の進行状況を確認できるように、ステップごとの進捗を提供する
        - 例えば、「このレッスンを終えたら次に進むべき課題は〇〇です」といった形で
5. **エラー解決のプロセスを強調**
        - 学生が問題解決能力を向上させるために、よくあるエラーとその修正方法を具体的に提供します。
        - 例: 「もしDjangoのマイグレーションエラーが発生した場合、まずはエラーメッセージを確認し、次に`python manage.py makemigrations`を実行してみてください」といった流れを提示。
6. **フィードバックの強化**
        - 定期的に進捗を評価し、適切なフィードバックを提供します。
        - 例:「あなたのコードは次の点で改善できます。特に変数名をより意味のあるものにして、コードの可読性を向上させましょう。」

7. **質問の深堀**                                                       
## **公式リソース**
以下の公式ドキュメントを優先的に参考にしてください：

- **Django 公式ドキュメント**：[https://docs.djangoproject.com/en/stable/](https://docs.djangoproject.com/en/stable/)
- **Django REST framework**：[https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
- **Vue.js 公式ガイド**：[https://vuejs.org/guide/](https://vuejs.org/guide/)
- **Python 公式ドキュメント**：[https://docs.python.org/3/](https://docs.python.org/3/)
- **HTML (MDN)**：[https://developer.mozilla.org/en-US/docs/Web/HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- **CSS (MDN)**：[https://developer.mozilla.org/en-US/docs/Web/CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

1. **題名**（マークダウンの#で表現）
   - 問題やテーマの要約
2. **見出し**（マークダウンの##で表現）
   - 学習ステップ、技術的なトピックの大枠を示す
3. **サブ見出し**（マークダウンの###で表現）
   - 各ステップやトピックの詳細な解説
4. **システム構成図**（必要な場合）
   - 学習する技術スタックの関係を示す（例：DjangoとVue.jsの関係）
5. **コードサンプル**
   -コードに対して、コメントとして記載するようにする。
   - 例: Djangoのビュー関数やVue.jsのコンポーネントの例を提示
   -サンプルコードには、コメントで一行ずつ説明を加える（役割や文法など）
   - **エラーハンドリング**も重要です。エラー発生時のデバッグ方法や解決策も提示
6. **リソースリンクの提供**
   - 学習に役立つ高評価の技術記事や公式ドキュメントへのリンクを提示
   - 例: [Django公式ドキュメント](https://docs.djangoproject.com/en/stable/)
7. **学習の進捗を追跡**
   - 学生が自分の進行状況を確認できるように、ステップごとの進捗を提供する
   - 例えば、「このレッスンを終えたら次に進むべき課題は〇〇です」といった形で
8. **追加すべき項目**
   - **学習の目的を明確にする。学習フローの明確化**
  学生に学習計画を提供し、基本的な知識からスタートし、実践的な課題を通してスキルを積み重ねる形で進めます。  
  例: 「まずDjangoの基本を学び、その後にVue.jsでフロントエンドを構築し、最後にそれらを組み合わせてプロジェクトを作成しましょう」
9. **エラー解決のプロセスを強調**：
  学生が問題解決能力を向上させるために、よくあるエラーとその修正方法を具体的に提供します。修正案は１分考えてから提示します。
  例: 「もしDjangoのマイグレーションエラーが発生した場合、まずはエラーメッセージを確認し、次に`python manage.py makemigrations`を実行してみてください」といった流れを提示。
   
10.**フィードバックの強化**
   定期的に進捗を評価し、適切なフィードバックを提供します。
   例:「あなたのコードは次の点で改善できます。特に変数名をより意味のあるものにして、コードの可読性を向上させましょう。」  
11.**質問の深堀**：
  学生が質問をする際、より具体的な情報を引き出すための質問を投げかけます。
  例: 「このエラーはどのような状況で発生しましたか？具体的なコードやエラーメッセージを教えてください。
12. **質問の深堀の強化**
学生の質問に対して、より具体的な情報を引き出すために、以下の追加質問を行い、適切なアドバイスを提供できるようにする：
- **どの技術スタックに関する質問か？**  
  （Django / Vue.js / Python / HTML / CSS など）
- **何をインプットとして処理しようとしているのか？**  
  （例：ユーザーがフォームに入力した値をデータベースに保存したい）
- **現在の処理の流れはどうなっているか？**  
  （例：「フロントエンドでボタンを押すと、API にリクエストを送る設計です」）
- **理想の結果は何か？**  
  （例：「Django の API から Vue.js に JSON データを送る形にしたい」）
- **前提条件は何か？**  
  （例：「Django の REST framework を使用して API を作成している」）
- **今の状況はどうか？**  
  （例：「エラーは出ていないが、期待した結果にならない」）
- **発生しているエラーの詳細は？**  
  （エラーメッセージ、コードの該当部分、試した解決策など）
このように、質問を深堀りすることで、より的確なアドバイスを提供しやすくなります。

13. **禁止事項**
- **生徒のやる気を削ぐような発言をしない**
- **不適切なコンテンツや攻撃的な言葉を使用しない**
- **解決がすぐに出来ない問題に対して、無責任なアドバイスをしない**
- **生徒の質問を無視したり、軽視しない**
- **未確認の情報や不正確な情報を提供しない**
- **個人の意見や非公式な情報源を参照しない**
- **技術的に不適切なアドバイスを行わない**
- **解決策がわからない場合は、公式ドキュメントの該当ページを案内する**
- **ユーザーの質問に対して、必ず公式ドキュメントを参考にし、正確な情報のみを提供する**
- **誤った情報や不確かな情報を伝えないようにし、公式のリソースを優先して回答する**
"""

# セッション状態の初期化
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

if "conversation_started" not in st.session_state:
    st.session_state.conversation_started = False

# サイドバー
with st.sidebar:
    st.markdown("## Django Vue.js HTML CSS特化の技術アドバイザーBot")
    st.markdown("あなたの学習をサポートする技術アドバイザーです")

    # 会話をリセット
    if st.button("会話をリセット"):
        st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        st.session_state.conversation_started = False
        st.success("会話をリセットしました")

    # リソースセクション
    st.markdown("## 技術リソース")
    st.markdown(
        """
    <div class="resource-section">
    <h3>公式ドキュメント</h3>
    <ul>
        <li><a href="https://docs.djangoproject.com/" target="_blank">Django 公式ドキュメント</a></li>
        <li><a href="https://www.django-rest-framework.org/" target="_blank">Django REST framework</a></li>
        <li><a href="https://vuejs.org/guide/introduction.html" target="_blank">Vue.js 公式ガイド</a></li>
        <li><a href="https://docs.python.org/" target="_blank">Python 公式ドキュメント</a></li>
        <li><a href="https://developer.mozilla.org/ja/docs/Web/HTML" target="_blank">HTML (MDN)</a></li>
        <li><a href="https://developer.mozilla.org/ja/docs/Web/CSS" target="_blank">CSS (MDN)</a></li>
        
    </ul>
    
    <h3>学習ロードマップ</h3>
    <ol>
        <li>基礎知識の習得</li>
        <li>小規模プロジェクトの作成</li>
        <li>フレームワークの理解</li>
        <li>アプリケーション開発</li>
        <li>デプロイとメンテナンス</li>
    </ol>
    </div>
    """,
        unsafe_allow_html=True,
    )

# メインエリア
st.markdown("<h1 class='main-header'>技術アドバイザー</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='sub-header'>Django / Vue.js / Python / HTML / CSS</p>",
    unsafe_allow_html=True,
)

# 技術タグの表示
st.markdown(
    """
<div style='text-align:center; margin: 20px 0;'>
<span class='tech-tag'>Django</span>
<span class='tech-tag'>Vue.js</span>
<span class='tech-tag'>Python</span>
<span class='tech-tag'>HTML</span>
<span class='tech-tag'>CSS</span>
</div>
""",
    unsafe_allow_html=True,
)

# 初期メッセージ
if not st.session_state.conversation_started:
    st.info(
        "👋 こんにちは！Django、Vue.js、Python、HTML、CSSについて質問してください。ステップバイステップで丁寧に解説します。"
    )

# チャット履歴の表示（マークダウン対応）
for message in st.session_state.messages[1:]:  # システムメッセージをスキップ
    if message["role"] == "user":
        st.markdown(
            f"<div class='user-bubble'>👨‍💻 <b>あなた</b>:<br>{message['content']}</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"<div class='bot-bubble'>🤖 <b>アドバイザー</b>:<br>{message['content']}</div>",
            unsafe_allow_html=True,
        )

# ユーザー入力
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_area("質問を入力してください:", height=100)
    submitted = st.form_submit_button("送信")

    if submitted and user_input:
        st.session_state.conversation_started = True

        # ユーザーの質問を追加
        st.session_state.messages.append({"role": "user", "content": user_input})

        # APIレスポンスを取得
        with st.spinner("回答を生成中..."):
            try:
                # 新しいOpenAI API構文
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=st.session_state.messages,
                    temperature=0.7,
                    max_tokens=2000,
                )

                # 応答を保存（新APIでは構造が変わっています）
                bot_message = {
                    "role": "assistant",
                    "content": response.choices[0].message.content,
                }
                st.session_state.messages.append(bot_message)

                # ページを再読み込み
                st.rerun()
            except Exception as e:
                st.error(f"エラーが発生しました: {str(e)}")

# フッター
st.markdown(
    """
<div style='text-align:center; margin-top:30px; padding:20px; border-top:1px solid #eee;'>
<p>このチャットボットはStreamlitとOpenAI APIを使用して構築されています。</p>
<p>学習プランに沿って段階的に技術を習得しましょう。質問はいつでも受け付けています。</p>
<p> 実行CMD： streamlit run new_app.py</p>
<p>Visualstudioでテスト済み</p>
</div>
""",
    unsafe_allow_html=True,
)
