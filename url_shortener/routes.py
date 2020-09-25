from flask import render_template, url_for, flash, redirect

from url_shortener import app, db
from url_shortener.models import Link
from url_shortener.forms import AddLinkForm


@app.route('/', methods=['GET', 'POST'])
def home():
    form = AddLinkForm()
    if form.validate_on_submit():
        link = Link(full_link=form.full_link.data,
                    short_link=form.short_link.data)
        db.session.add(link)
        db.session.commit()
        return redirect(url_for('linkadded', id=link.id))

    return render_template('home.html', form=form)


@app.route('/added/<int:id>')
def linkadded(id):
    link = Link.query.get_or_404(id)
    return render_template('added.html', link=link)


@app.route('/<string:url>')
def redirect_user(url):
    u = Link.query.filter_by(short_link=url).first_or_404()
    return redirect(u.full_link)


@app.errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404
