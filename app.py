from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import pandas as pd

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    # セレクトボックスの選択肢
    options = ['dance', 'positive', 'study', 'driving']
    return render_template('index.html', options=options,title="プレイリストを作ります！")

@app.route('/result.html', methods=["POST"])
def result():
    # 選択された値を取得
    selected_value = request.form['select']
    # CSVファイルを読み込む
    data = pd.read_csv('spotify.csv')
    # 必要なカラムのみを抽出
    df = data[['artist', 'name', 'album', 'release_date','feels']]
    # 選択された値に対応するデータを抽出
    selected_data = df[df['feels'] == selected_value]
    # ランダムに20個のデータを抽出
    random_data = selected_data.sample(n=20)
    # HTML形式のテーブルに変換して、リストに格納
    tables = [random_data.to_html(classes='data', header="true", index=False)] 
    return render_template('result.html',tables=tables,titles=random_data.columns.values,title="卒業制作")

if __name__ == '__main__':
    app.run(host='localhost',port=8080, debug=True)
    