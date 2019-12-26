from flask import render_template, request, redirect, url_for

from app import db
from app.posts import bp
from .forms import PostForm
from .models import Post, Tag


@bp.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        post = Post(title=title, body=body)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@bp.route('/')
def index():
    search = request.args.get('search')
    if search:
        posts = Post.query.filter(Post.title.contains(search) | Post.body.contains(search)).all()
    else:
        posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)


@bp.route('/<url_slug>')
def post_detail(url_slug):
    post = Post.query.filter(Post.slug == url_slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@bp.route('/tag/<url_slug>')
def tag_detail(url_slug):
    tag = Tag.query.filter(Tag.slug == url_slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)
