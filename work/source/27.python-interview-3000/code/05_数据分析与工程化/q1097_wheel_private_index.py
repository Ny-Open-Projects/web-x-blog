import re

WHEEL_RE = re.compile(r"^(?P<name>[^-]+)-(?P<version>[^-]+)-(?P<py>[^-]+)-(?P<abi>[^-]+)-(?P<platform>[^-]+)\.whl$")

def parse_wheel(filename):
    m = WHEEL_RE.match(filename)
    if not m:
        raise ValueError("非法 wheel 文件名")
    return m.groupdict()

if __name__ == "__main__":
    name = "my_pkg-1.2.0-cp312-cp312-manylinux_2_17_x86_64.whl"
    print(parse_wheel(name))
    # 构建:python -m build -> dist/*.whl + *.tar.gz
    # 上传:twine upload --repository-url https://pypi.example.com/simple/ dist/*
    # 安装:uv pip install my-pkg --index-url https://pypi.example.com/simple/
