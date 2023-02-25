from bottle import run, route, template, static_file


@route('/')
def index():
    return template('index')

@route('/company/<filename>')
def about(filename):
    return static_file(filename, root='./views/company/')

@route('/images/<filename>')
def send_images(filename):
    return static_file(filename, root='./static/images/')

@route('/icons/<filename>')
def send_icons(filename):
    return static_file(filename, root='./static/icons/')

@route('/videos/<filename>')
def send_videos(filename):
    return static_file(filename, root='./static/videos/')

@route('/css/<filename>')
def send_videos(filename):
    return static_file(filename, root='./static/css/')

@route('/js/<filename>')
def send_script(filename):
    return static_file(filename, root='./static/js/')

@route('<filename:path>')
def opensans(filename):
    return static_file(filename, root='./views/')




run(debug=True, reloader=True)