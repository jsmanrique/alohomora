#/usr/bin/env python

from bottle import Bottle, template, run, request, redirect
import couchdb

app = Bottle()

# Data base init
couch = couchdb.Server()
try:
    db = couch['grimoire-projects']
except couchdb.http.ResourceNotFound:
    db = couch.create('grimoire-projects')

@app.route('/')
@app.route('/projects')
def projects():
    projs = []
    for id in db:
        projs.append({'pid':id, 'pname':db[id]['name']})
    return template('projects', projects=projs)

@app.route('/projects/<pid>/')
@app.route('/project/<pid>/')
def project(pid):
    repos = db[pid]['repositories']
    return template('repos', repositories=repos)

@app.route('/add_project')
def add_project():
    return template('add_project')

@app.route('/add_project', method='POST')
def save_project():
    proj = {'name':request.forms.get('pname'), 'repositories':[]}
    db.save(proj)
    redirect('/projects')

@app.route('/projects/<pid>/add_repo')
@app.route('/project/<pid>/add_repo')
def add_repo(pid):
    #return pid
    return template('add_repo')

@app.route('/projects/<pid>/add_repo', method='POST')
@app.route('/project/<pid>/add_repo', method='POST')
def save_repo(pid):
    repo = {'repo_type':request.forms.get('repo_type'), 'repo_url':request.forms.get('repo_url')}
    proj = db[pid]
    repos = proj['repositories']
    repos.append(repo)
    proj['repositories'] = repos
    db[pid] = proj
    redirect('/project/'+pid+'/')

@app.route('/projects/<pid>/json')
@app.route('/project/<pid>/json')
def add_repo(pid):
    proj = db[pid]
    json = couchdb.json.encode(proj)
    return json

run(app, host='localhost', port=8080)
