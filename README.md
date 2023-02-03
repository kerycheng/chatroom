# 網路聊天室 Online Chat Room  

[網頁DEMO連結](https://marginlmanchatroom.ddns.net/)  


* [概述](#overview)  
  * [專案引用](#site)  
* [套件安裝](#install)  
* [使用說明](#use)  
 * [網站伺服器開啟](#runserver)
 * [資料庫重新創建](#database)
 * [第三方快速登入](#thirdpartylogin)
 * [TODO](#TODO)
  

<h2 id"overview">概述</h2>

具有用戶註冊、第三方快速登入功能，可在聊天室上發布文章並在底下進行回覆。


<h3 id"site">專案引用</h3>

本網站主要參考[StudyBud](https://github.com/divanov11/StudyBud/)這個專案，並加以修改、完善。

<br>

<h2 id"install">套件安裝</h2>  

一鍵安裝套件  

```bash
pip3 install -r requirements.txt
```

<br>

<h2 id"use">使用說明</h2>

<h4 id="#runserver">網站伺服器開啟</h4>

```bash
# for https:
python manage.py sslrunserver
# for http:
python manage.py runserver
```
<br>

<h4 id="#database">資料庫重新創建(並創建管理員帳號)，請按照以下步驟執行：</h4>

```
#1 將bd.sqlite3與migrations的0001_initial.py刪除
```

```
#2 /到models.py
   /USERNAME_FIELD = 'email' --> 將這行註解掉
```

```
#3 /輸入"python manage.py makemigrations"
   /輸入"python manage.py"
```

```
#4 /輸入"python manage.py createsuperuser"
   /創建管理員帳號
```

```
#5 /打開可修改SQL資料庫的工具(如:DB Browser(SQLite))
   /打開base_user
   /將管理員帳號的"email"欄位填上email(如:XXXX@email.com)
```

```
#6 將models.py的USERNAME_FIELD = 'email'註解刪除
```

```
#7 /輸入"python manage.py makemigrations"
   /輸入"python manage.py "
```
<br>

做這些步驟的原因是因為我們後續創建User帳戶的時候是使用email與password作為登入選項  
但是如果不先修改models.py的USERNAME_FIELD的話，在創建管理員帳戶的時候會缺少username這個選項  
進而導致帳戶創建失敗，於是必須先透過以上步驟來進行修改才能創建管理員帳戶  

<br>

<h4 id="#thirdpartylogin">關於第三方帳號快速登入的設定</h4>

需要先至[Google Cloud](https://console.cloud.google.com/welcome?project=modified-badge-272616&hl=zh-tw)與[GitHub Develpers](https://github.com/settings/developers)申請OAuth apps

關於如何申請Google的API可以參考這篇文章的前半部分： [[ASP.NET] 如何串接 Google Api 帳戶登入](https://blog.hungwin.com.tw/aspnet-google-login/)

GitHub可以參考這篇文章： [Day30 : Django 第三方登入 - 以Github為例](https://ithelp.ithome.com.tw/articles/10206389)


<h4 id="#TODO">TODO</h4>

* 文章換行  
* 增加忘記密碼功能  
