from src.server import create_flask_app

if __name__ == "__main__":
    app = create_flask_app()

    app.run(host="127.0.0.1", port=3001)
