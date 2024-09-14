import flask

def render_login():
    return flask.render_template(template_name_or_list = "login.html")

def render_registration():
    return flask.render_template(template_name_or_list = "registration.html")