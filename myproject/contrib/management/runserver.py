from ... import create_app


def runserver():
    app = create_app()
    app.run()