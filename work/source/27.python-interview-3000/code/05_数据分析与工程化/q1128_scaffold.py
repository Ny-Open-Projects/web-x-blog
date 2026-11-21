import os
import tempfile

TEMPLATE = {
    "pyproject.toml": "[project]\nname = '{{name}}'\nrequires-python = '>=3.12'\n",
    "src/{{name}}/__init__.py": "__version__ = '0.1.0'\n",
    "src/{{name}}/main.py": "def main():\n    print('hello {{name}}')\n",
    ".github/workflows/ci.yml": "name: ci\non: [push]\njobs:\n  test:\n    runs-on: ubuntu-latest\n",
    "Dockerfile": "FROM python:3.12-slim\nCOPY src /app/src\n",
}

def scaffold(root, name):
    created = []
    for rel, content in TEMPLATE.items():
        path = os.path.join(root, rel.replace("{{name}}", name))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content.replace("{{name}}", name))
        created.append(os.path.relpath(path, root))
    return created

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as root:
        for p in scaffold(root, "inventory"):
            print("生成", p)
    print("脚手架由平台组版本化维护,服务声明基于模板 vX")
