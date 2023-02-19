from bottle import run, route, template, static_file


@route('/')
def index():
    return template('index')

@route('/company/<filename>')
def about(filename):
    return static_file(filename, root='./views/company/')

@route('/images/<filename>')
def send_images(filename):
    return static_file(filename, root='./views/images/')

@route('/videos/<filename>')
def send_videos(filename):
    return static_file(filename, root='./views/videos/')

@route('/css/<filename>')
def send_videos(filename):
    return static_file(filename, root='./views/css/')

@route('<filename:path>')
def opensans(filename):
    return static_file(filename, root='./views/')




run(debug=True, reloader=True)