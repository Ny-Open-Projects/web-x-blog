"""以编程方式生成 pyproject.toml,演示现代包元数据。"""
from pathlib import Path

PYPROJECT = '''
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "myutils"
version = "1.2.0"
description = "个人工具集示例包"
requires-python = ">=3.9"
dependencies = ["requests>=2.31,<3"]

[project.optional-dependencies]
dev = ["pytest", "ruff"]

[project.scripts]
myutils-cli = "myutils.cli:main"
'''


def init_package(root="myutils-project"):
    root = Path(root)
    pkg = root / "myutils"
    pkg.mkdir(parents=True, exist_ok=True)
    (pkg / "__init__.py").write_text('__version__ = "1.2.0"\n', encoding="utf-8")
    (pkg / "cli.py").write_text(
        'def main():\n    print("hello from myutils")\n', encoding="utf-8"
    )
    (root / "pyproject.toml").write_text(PYPROJECT, encoding="utf-8")
    return root


if __name__ == "__main__":
    p = init_package("/tmp/myutils-project")
    print("生成完成:", sorted(str(x.relative_to(p)) for x in p.rglob("*")))
    # 发布三步(在项目根目录执行):
    # python -m build          生成 sdist 和 wheel
    # twine check dist/*       校验元数据
    # twine upload dist/*      上传 PyPI 或私有 index
