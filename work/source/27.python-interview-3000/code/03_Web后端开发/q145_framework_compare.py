DECISION = {
    'Django': {
        '适合': ['管理后台', '内容型网站', '重业务 CRUD', '团队大交付急'],
        '生态': ['Django ORM', 'DRF', 'Admin', 'Celery'],
        '风格': '全家桶 约定优于配置',
    },
    'Flask': {
        '适合': ['中小服务', '原型验证', '需要灵活定制'],
        '生态': ['SQLAlchemy', 'Flask-Login', 'Flask-Migrate'],
        '风格': '微内核 扩展自由组合',
    },
    'FastAPI': {
        '适合': ['高并发 API', '微服务', 'AI 推理服务', '需要自动文档'],
        '生态': ['Pydantic v2', 'Uvicorn', 'SQLAlchemy async', 'ARQ'],
        '风格': '异步优先 类型驱动',
    },
}

for name, info in DECISION.items():
    print(name, '->', info['风格'])
# 结论: 瓶颈多在数据库与外部 IO;先定团队与业务形态,再定框架
