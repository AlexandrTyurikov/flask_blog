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


@bp.route('/<url_slug>/update', methods=['POST', 'GET'])
def update_post(url_slug):
    post = Post.query.filter(Post.slug == url_slug).first()
    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for('posts.post_detail', url_slug=post.slug))

    form = PostForm(obj=post)
    return render_template('posts/update_post.html', post=post, form=form)


@bp.route('/')
def index():
    search = request.args.get('search')
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    if search:
        posts = Post.query.filter(Post.title.contains(search) | Post.body.contains(search))  # .all()
    else:
        posts = Post.query.order_by(Post.created_date.desc())
    pages = posts.paginate(page=page, per_page=4)
    return render_template('posts/index.html', posts=posts, pages=pages)


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
