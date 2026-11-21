try:
    from flask import Flask
except ImportError:
    print("该题演示需要第三方库 flask:pip install flask,原理见正文")
    raise SystemExit(0)

def create_app(config_name: str = 'dev') -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        DEBUG=config_name == 'dev',
        SECRET_KEY='dev-secret',
        DATABASE='app.db',
    )

    @app.get('/health')
    def health():
        return {'status': 'ok', 'env': config_name}

    return app

app = create_app('dev')

if __name__ == '__main__':
    app.run(port=5000)
