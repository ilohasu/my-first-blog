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


python manage.py makemigrations
python manage.py migrate

# 管理するファイルまたはアプリケーションのディレクトリで行う
git init
git config --global user.name irohasu
git config --global user.email test@test.com

git status
git add --all .
git commit -m "[コミットメッセージ]"
git remote add origin https://github.com/ilohasu/my-first-blog.git
git push -u origin master

$ git status
$ git add --all .
$ git status
$ git commit -m "Added view and template for detailed blog post as well as CSS for the site."
$ git push

# サーバへの反映
cd ~/ilohasu.pythonanywhere.com
git pull

# 静的ファイルの更新
workon ilohasu.pythonanywhere.com
(ola.pythonanywhere.com)$ python manage.py collectstatic

9183e93b4f8d6fe0564fa7c8df896a598d6d6126
-------------------------------


-------------------------------
参考サイト
django girlsより
https://tutorial.djangogirls.org/ja/django_start_project/
-------------------------------