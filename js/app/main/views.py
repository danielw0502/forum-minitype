from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from flask import Blueprint
from . import main
from .forms import PostForm, CommentForm
from app.models import db,User,Post,Comment
from flask import request
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime


#main page
@main.route('/',methods=['GET','POST'])
def index():
    page = request.args.get('page',1,type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=10, error_out=False)
    posts = pagination.items
    return render_template('index.html', posts=posts, pagination=pagination)
    # original
    #posts = Post.query.order_by(Post.timestamp.desc()).all()
    #return render_template('index.html',posts=posts)

#create new blog
@main.route('/create',methods=['GET','POST'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        post = Post(title=title,body=body,author_post=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        #to do list
        #return to detailed page
        return redirect(url_for('.index'))
    return render_template('create.html',form=form)

#show the detailed blog
@main.route('/post/<int:id>',methods=['GET','POST'])
def showpost(id):
    post = Post.query.filter_by(id=id).first()
    user = post.author_post
    form = CommentForm()    
    if form.validate_on_submit():
        #提交评论需要登录
        body = form.body.data
        comment = Comment(body=body,post=post,author_comment=current_user._get_current_object())
        db.session.add(comment)
        db.session.commit()
        flash('评论已提交')
        return redirect(url_for('.showpost',id=id))
    # to do list
    # consider multiple comments
    #page = request.args.get('page',1,type=int)
    #if page == -1:
    #form.body.data = post.comments.order_by(Comment.timestamp.asc())
    comments = post.comments.order_by(Comment.timestamp.desc())
    return render_template('blog.html',post=post,form=form,comments=comments,user=user)

#edit the blog
#how to confirm if the user is the post author
@main.route('/edit/<int:id>',methods=['GET','POST'])
@login_required
def edit(id):
    post = Post.query.filter_by(id=id).first()
    form = PostForm()
    
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        post.timestamp = datetime.utcnow()
        db.session.add(post)
        db.session.commit()
        flash('The post has been updated')
        return redirect(url_for('.showpost',id=id))
    form.title.data = post.title
    form.body.data = post.body
    return render_template('edit_post.html',form=form)

#delete the blog
@main.route('/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete(id):
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    flash('The post has been deleted')
    return redirect(url_for('main.index'))

@main.route('/user/<username>',methods=['GET','POST'])
def user(username):
    user = User.query.filter_by(username=username).first()
    posts_main = user.posts.order_by(Post.timestamp.desc())
    page = request.args.get('page',1,type=int)
    pagination = posts_main.paginate(page, per_page=8, error_out=False)
    posts = pagination.items
    t = posts_main.first().timestamp
    return render_template('user.html',user=user,posts=posts,t=t, pagination=pagination)