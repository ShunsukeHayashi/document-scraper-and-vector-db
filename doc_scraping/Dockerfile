# ベースイメージとしてPythonを使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトのコードをコンテナにコピー
COPY . .

# コンテナ起動時に実行するコマンドを指定
CMD ["python", "run_all.py"]