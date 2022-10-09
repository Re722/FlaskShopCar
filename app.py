import sqlite3
from flask import Flask,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


   

app = Flask(__name__,template_folder = 'templates') 
#app = SQLAlchemy.create_app('sqlite:///foxx.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foxx.db'

db = SQLAlchemy(app)


class Vans(db.Model):
     id = db.Column('id',db.INTEGER, primary_key=True,autoincrement=True)
     owner = db.column(db.String(150))
     colors = db.column(db.String(100))
     models = db.column(db.String(120))
    
def __init__(self,owner,colors,models):    
     self.owner=owner
     self.colors=colors
     self.models=models  
    
     #db.create_all()     
   

@app.route('/')
def index():
     foxx = Vans.query.all()
     return render_template('index.html',foxx=foxx)


@app.route('/add', methods=['GET', 'POST'])
def add():
     if request.method == 'POST':
         foxx = Vans(request.form['owner'], request.form['colors'],request.form['models'])
         db.session.add(foxx)
         db.session.commit()
         return redirect(url_for('index'))
     return render_template('add.html')

@app.route('/edit/<int:id>',methods=['GET', 'POST'])
def edit(id):
     foxx = Vans.query.get(id)
     if request.method == 'POST':
         foxx.owner = request.form['owner']
         foxx.colors = request.form['colors']
         foxx.models = request.form['models']
         db.session.commit()
         return redirect(url_for('index'))
     return render_template('edit.html', foxx=foxx)

@app.route('/delete/<int:id>')
def delete(id):
     foxx = Vans.query.get(id)
     db.session.delete(foxx)
     db.session.commit()
     return redirect(url_for('index'))


if __name__ == '__main__':     
     app.run(debug=True)
     db.create_all()
    