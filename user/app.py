import flask

user_app = flask.Blueprint(
    name = "user",
    import_name = "user",
    static_folder = "static",
    static_url_path = "/static/",
    template_folder = "templates"
)