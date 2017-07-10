### django入门

* 安装django 
    - pip install Django==1.11.2

* 基本使用
    - 创建 项目    
    ```
    django-admin startproject Hello

    ```
    - 新建一个名为blog的应用 
    ```
    python manage.py startapp blog
    ```
    - 开启 服务器

    ```
    python manage.py runserver 8080
    ```
    在根urls.py中引入include函数
    - 为blog 应用添加urls.py
    在app下创建urls.py文件，内容格式与根urls相同
    在跟urls.py中url函数第二个参数改为include('blog.urls')

    * 注意：根urls.py针对app配置的url名称 ，是该app所有url的总路径*
    * 配置url时注意re ^$和 /
    

    * 数据表生成
    命令行进入manage.py同级目录
    执行python manage.py makemigrations app名(可选)
    再执行python manage.py migrate

    * 查看
    django会自动在app/migrations目录下生成移植文件
    执行python manage.py sqlmigrate 应用名 文件id 参看sql语句

    * 查看并编辑 db.sqlite3
    使用第三方软件
    SQLite Expert Personal  

    添加 数据

    页面呈现数据
    后台步骤
    views.py中import models
    article = models.Article.objects.get(pk=1)//pk --> premary.. key
    render(request, 'blog/index.html', {'article': article})

    * 配置admin

    python manage.py createsuperuser 创建超级用户
    localhost: 8000/admin/
    修改settings.py 中 LANGUAGE_CODE= 'zh_Hans' --> 汉字

    配置应用
    在应用下admin.py 中引入自身的models模块（或里面的模型类）
    编辑 admin.py : admin.site.register(models.Article)

    * 修改数据默认显示名称
    在Article中添加一个方法
    根据python版本选择__str__(self) 或 __unicode__(self)
    return self.title

    django中的超链接
    template中可以使用"{% url 'app_name: url_name' param %}"
    其中app_name 和 url_name 在url中配置

    配置urls.py
    url函数的名称函数
    - 跟urls，写在include（）的第二个参数位置，namespace = 'blog'
    - 应用下则写在url（）的第三个参数位置，name = 'article_page'