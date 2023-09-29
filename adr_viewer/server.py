from bottle import Bottle, run


def run_server(content, port) -> None:
    print(f"Starting server at http://localhost:{port}/")
    app = Bottle()
    app.route("/", "GET", lambda: content)
    run(app, host="localhost", port=port, quiet=True)
