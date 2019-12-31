import os

from flask import render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

from app import db, app
from app.posts import bp
from .forms import PostForm
from .models import Post, Tag


def allowed_image(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_EXTENSIONS_IMAGE_POSTS"]:
        return True
    else:
        return False


def allowed_image_filesize(filesize):
    if int(filesize) <= app.config["MAX_CONTENT_LENGTH_IMAGE_POSTS"]:
        return True
    else:
        return False


@bp.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':

        # get images
        if request.files:
            if "filesize" in request.cookies:
                if not allowed_image_filesize(request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    return redirect(request.url)
                image = request.files["image"]
                if image.filename == "":
                    print("No filename")
                    return redirect(request.url)
                if allowed_image(image.filename):
                    filename = secure_filename(image.filename)
                    image.save(os.path.join(app.config["UPLOAD_FOLDER_IMAGE_POSTS"], filename))
                    print("Image saved")
                    return redirect(request.url)
                else:
                    print("That file extension is not allowed")
                    return redirect(request.url)

        title = request.form['title']
        body = request.form['body']
        image = request.files["image"]
        post = Post(title=title, body=body, image=image)

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
    tags = Tag.query

    image = request.files["image"]
    send_from_directory(app.config['UPLOAD_FOLDER'], filename=image.filename)

    return render_template('posts/index.html', posts=posts, pages=pages, tags=tags)


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
