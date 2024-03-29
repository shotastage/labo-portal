# python:3.8の公式 image をベースの image として設定
FROM python:3.9.4

# 作業ディレクトリの作成
RUN mkdir /code

# 作業ディレクトリの設定
WORKDIR /code

# カレントディレクトリにある資産をコンテナ上の指定のディレクトリにコピーする
ADD . /code

# pipでrequirements.txtに指定されているパッケージを追加する
RUN pip install pipenv


# 起動（コンテナのポート8002番で受け付けるように起動する）
CMD python3 manage.py runserver 0.0.0.0:8002
