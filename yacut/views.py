from flask import flash, redirect, render_template

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        if form.custom_id.data:
            short = form.custom_id.data
            if URLMap.query.filter_by(short=short).first():
                flash(f'Имя {short} уже занято!')
                return render_template('index.html', form=form)
        else:
            url = URLMap.query.filter_by(
                original=form.original_link.data).order_by(
                    URLMap.timestamp.desc()).first()
            if url:
                return render_template('index.html', form=form,
                                       short_link=url.short)
            short = get_unique_short_id()
        url = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(url)
        db.session.commit()
        return render_template('index.html', form=form, short_link=short)
    return render_template('index.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def get_url_view(short_id):
    return redirect(URLMap.query.filter_by(short=short_id
                                           ).first_or_404().original)