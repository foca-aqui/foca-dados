from app.factory import make_app


app = make_app()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)