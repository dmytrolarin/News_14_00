import flask

article = flask.Blueprint(
    name= "article",
    import_name= "article",
    template_folder= 'templates',
    static_folder= 'static',
    static_url_path= '/article/'
)