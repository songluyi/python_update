# -*- coding: utf-8 -*-
# 2016/8/21 12:27
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

from __future__ import with_statement
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,\
     abort,render_template,flash
from contextlib import closing

# configuration
DATABASE = '/home/feng/project/flaskr/flaskr.db'#数据库存储路径
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():#快速连接到指定数据库的方法
    return sqlite3.connect(app.config['DATABASE'])


def init_db():#初始化数据库
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
            db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    g.db.close()


@app.route('/')
def show_entries():#输出函数,会将条目作为字典传递给 show_entries.html 模板，并返回之后的渲染结果
    cur = g.db.execute('select name,email,text from entries order by id desc limit 10')
    entries = [dict(name=row[0], email=row[1], text=row[2]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():#用户添加新的留言信息函数，并只响应 POST 请求，表单显示在 show_entries
    if not session.get('logged_in'):
        abort(401)
    if len(request.form['text']) >50 and len(request.form['text'])<500:#实现控制字数在50到500范围内
        g.db.execute('insert into entries (name,email,text) values (?,?,?)',
                 [request.form['name'],request.form['email'], request.form['text']])
        g.db.commit()
        flash('New entry was successfully posted')
    else:
        flash('The input range must be between 50 and 500 characters ')#如果留言信息不在范围内作出提示
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():#登入函数
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'name error'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'password error'
        else:
            session['logged_in'] = True
            flash('log in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():#退出登录函数
    session.pop('logged_in', None)
    flash('log out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)