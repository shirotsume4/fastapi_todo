# python3.9のイメージをダウンロード
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src

# pipを使ってpoetryをインストール
RUN pip install fastapi sqlalchemy aiomysql

ENTRYPOINT ["fastapi", "dev",  "api/main.py", "--host", "0.0.0.0", "--reload"]