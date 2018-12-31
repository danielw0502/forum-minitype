@main.route('/',methods=['GET','POST'])
def index():
    page = request.args.get('page',1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=10, error_out=False)
    posts = pagination.items
    return render_template('index.html',posts=posts, pagination=pagination)


{% extends "base.html" %}


{% block page_content %}

<div class="container_bg" style="height:800px; width: 800px;">
    <div class="card card-block container_logo" style="width: 700px; height: 100px;">
        <p class="card-text title_font">Hello, 冒险者，为何独自徘徊，加入我们说说你的故事吧。</p>
    </div>

        <ul class="posts">
            {% for post in posts %}
            <li class="post">
                <div >
                    <div>
                        <a href="{{ url_for('.user', username=post.author_post.username) }}">
                            {{ post.author_post.username }} 
                        </a>
                    </div>
                    <div>
                        {{ moment(post.timestamp).fromNow() }}
                    </div>
                    <div>
                        <a href="{{ url_for('.showpost', id=post.id) }}">
                            {{ post.title }}
                        </a>
                    </div>
                    <div>
                        {{ post.body }}
                    </div>
                </div>
            </li>
            {% endfor %}
        </ul>

</div>


{% endblock %}



{% extends "bootstrap/base.html" %}
{% block title %}首页 - 简单 {% endblock %}

{% block head %}
{{ super() }}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/main.css') }}">
{% endblock %}


{% block navbar %}
<nav class="navbar navbar-expand-lg navbar-light bg-light">
        <span class="navbar-brand" id="jd">简单</span>
            <ul class="nav navbar-nav left-container">
                <li class="nav-item active">
                    <a class="nav-link" href="{{ url_for('main.index')}}">首页</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{{ url_for('auth.register')}}">注册</a>
                </li>
            </ul>
        <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">搜索</button>
        </form>

        <ul class="nav navbar-nav right-container">
            <li class="nav-item">
                <a class="nav-link" href="{{ url_for('main.create')}}">写文章</a>
            </li>
            <li class="nav-item">
                {% if current_user.is_authenticated %}
                <a class="nav-link" href="{{ url_for('auth.logout')}}">登出</a>
                {% else %}
                <a class="nav-link" href="{{ url_for('auth.login') }}">登录</a>
                {% endif %}
            </li>
        </ul>
</nav>
{% endblock %}

{% block content %}
<div class="container">
    {% for message in get_flashed_messages() %}
    <div class="alert alert-warning">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        {{ message }}
    </div>
    {% endfor %}
    {% block page_content %}{% endblock %}
</div>
{% endblock %}


{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
{% endblock %}

{% if pagination.has_prev %}<a href="{{ url_for('.index', page=pagination.prev_num) }}">&lt;&lt; Newer posts</a>{% else %}&lt;&lt; Newer posts{% endif %} | 
{% if pagination.has_next %}<a href="{{ url_for('.index', page=pagination.next_num) }}">Older posts &gt;&gt;</a>{% else %}Older posts &gt;&gt;{% endif %}



{% block footer %}
    <footer class="navbar-fixed-bottom text-center" style="width:100%; height:30px; margin-top:-30px; padding:0; border:0; background-color:rgb(196, 112, 35);">
            
        <small style="text-align: center;">
            &copy; 2019|
            <a href="https://github.com/danielw0502" title="fork me on Github">danielw</a>|
            <a href="https://github.com/danielw0502" title="fork me on Github"></a>源码|
            <span style="color:rgb(100, 80, 212)">简单</span>
        </small>
            
    </footer>
    {% endblock %}


{% block footer %}

    
    <footer class="text-center" style="position: absolute; bottom:0; left:0; right:0; height:30px; background-color:rgb(196, 112, 35);">
            
            <small style="text-align: center;">
                &copy; 2019|
                <a href="https://github.com/danielw0502" title="fork me on Github">danielw</a>|
                <a href="https://github.com/danielw0502" title="fork me on Github"></a>源码|
                <span style="color:rgb(100, 80, 212)">简单</span>
            </small>
                
    </footer>

<div class="navbar navbar-default navbar-fixed-bottom">
            <div class="container">
              <p class="navbar-text pull-left">© 2014 - Site Built By Mr. M.
                   <a href="http://tinyurl.com/tbvalid" target="_blank" >HTML 5 Validation</a>
              </p>
        
              <a href="http://youtu.be/zJahlKPCL9g" class="navbar-btn btn-danger btn pull-right">
              <span class="glyphicon glyphicon-star"></span>  Subscribe on YouTube</a>
            </div>
        </div>

    var header = document.getElementById("mydiv");
    var btns = header.getElementsByClassName("nav-item");

    for (var i = 0; i < btns.length; i++) {
        btns[i].addEventListener("click", function() {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
        window.alert(this.className);
        });
    }
</script>

  $('a[href="' + location.pathname + '"]').closest('li').addClass('active'); 
