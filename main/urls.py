from .settings import main_project
import user, article, home

article.article.add_url_rule(
    rule= '/article/',
    view_func= article.render
)
main_project.register_blueprint(blueprint= article.article)

user.user_app.add_url_rule(
    rule= "/registration/",
    view_func= user.render_registration
)
user.user_app.add_url_rule(
    rule= "/login/",
    view_func= user.render_login
)

main_project.register_blueprint(blueprint= user.user_app)

home.home_app.add_url_rule(
    rule= '/',
    view_func= home.render_home
)
main_project.register_blueprint(blueprint= home.home_app)