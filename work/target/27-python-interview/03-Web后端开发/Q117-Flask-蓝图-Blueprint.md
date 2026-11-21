---
title: [Q117] Flask 蓝图 Blueprint
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q117 · Flask 蓝图 Blueprint

> 难度:★☆☆ | 标签:Flask, 蓝图

**问**:蓝图解决什么问题?url_prefix 和静态资源怎么配?

**答**:Blueprint 把路由、模板、静态文件按功能模块组织,工厂中 `app.register_blueprint(bp, url_prefix='/api')` 统一挂载;蓝图中 `url_for('bp_name.endpoint')` 生成带前缀的链接,避免硬编码 URL。蓝图不能独立运行,必须注册到 app;大型项目常按 users/orders/auth 等领域各建一个蓝图。

```python
# file: code/03_Web后端开发/q117_blueprint.py
try:
    from flask import Flask, Blueprint, jsonify, url_for
except ImportError:
    print("该题演示需要第三方库 flask:pip install flask,原理见正文")
    raise SystemExit(0)

users_bp = Blueprint('users', __name__, url_prefix='/api/users')

@users_bp.get('')
def list_users():
    return jsonify([{'id': 1, 'name': 'alice'}])

@users_bp.get('/<int:uid>')
def get_user(uid: int):
    return jsonify({'id': uid, 'name': 'alice'})

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(users_bp)
    with app.test_request_context():
        print(url_for('users.get_user', uid=42))  # /api/users/42
    return app

if __name__ == '__main__':
    create_app().run(port=5000)
```

**追问**:
- 蓝图和工厂怎么配合?——工厂 create_app 内 register_blueprint,扩展用 init_app 延迟绑定;测试可反复创建独立 app 实例。
- url_for 在蓝图里怎么写?——`url_for('bp.endpoint')` 带蓝图名前缀,避免硬编码路径;前缀变更时链接自动跟随。
- 蓝图能注册两次吗?——同一 app 上同名蓝图重复注册报错;多实例需求用工厂创建多个 app。
