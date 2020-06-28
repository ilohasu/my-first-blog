-------------------------------
目標：まず、自分の日記サイトみたいなのをdjangoで作る
-------------------------------

-------------------------------
仮想環境でdjangoを使えるようにする

python -m pip install --upgrade pip

pip install -r requirements.txt
-------------------------------

-------------------------------
プロジェクトの作成
django-admin startproject (プロジェクト名) .

アプリケーション作成
python manage.py startapp (アプリケーション名)

python manage.py migrate
python manage.py makemigrations blog
python manage.py migrate blog
python manage.py createsuperuser

# 管理するファイルまたはアプリケーションのディレクトリで行う
git init
git config --global user.name irohasu
git config --global user.email test@test.com


-------------------------------


-------------------------------
参考サイト
django girlsより
https://tutorial.djangogirls.org/ja/django_start_project/
-------------------------------