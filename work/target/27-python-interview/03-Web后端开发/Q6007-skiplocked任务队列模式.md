---
title: [Q6007] select_for_update(skip_locked) 任务队列模式
date: 2026-11-18
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6007 · select_for_update(skip_locked=true) 任务队列模式

> 难度:★★★ | 标签:Django 4.2+, PostgreSQL/MySQL 8+, 任务队列

**问**：没有 Celery 之类的组件，能不能只用数据库表做任务队列？多 worker 认领任务怎么做到互不阻塞、任务不丢？

**答**：可以，核心是 `select_for_update(skip_locked=True)` 的「抢锁不等待」语义：每个 worker 开事务，查 earliest pending 任务并加行锁，**已被其他 worker 锁住的行直接跳过**（不像普通 FOR UPDATE 那样排队等待），认领到就把状态改成 processing 并提交释放锁——锁窗口只覆盖「认领」这一瞬间，不覆盖执行阶段，所以吞吐不受执行时长拖累。任务不丢靠**租约**：processing 任务带 `lease_expires_at`，回收器定时把租约过期（worker 崩溃/卡死）的任务重置回 pending；执行成功改 done、失败按退避改回 pending 加 retry_count。工程细节：1) 索引 `(status, priority, run_at)` 必须有，否则每次认领全表扫；2) 一次认领拿一小批（`LIMIT N`）摊薄事务开销；3) 存量任务重试要有上限进死信；4) SQLite 不支持 FOR UPDATE，单机开发要降级（乐观认领：UPDATE ... WHERE status='pending' 抢更新行数）；5) 对比 NOWAIT：nowait 拿不到立刻报错，适合快速失败场景；skip_locked 适合池化持续消费。DB 队列的适用边界：日百万级以下、不需要复杂路由；更高吞吐或延迟敏感还是上专业 MQ。

```python
# 基线:Django 4.2+/PostgreSQL 或 MySQL 8+(skip_locked)。SQLite 无 FOR UPDATE,降级为乐观认领演示。
try:
    import django
    from django.conf import settings
except ImportError:
    print("需要第三方库 django:pip install django,原理见正文")
    raise SystemExit(0)

settings.configure(DEBUG=True,
                   DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
                   USE_TZ=True)
django.setup()
from django.core.management.color import no_style
from django.db import connection, models, transaction

class Task(models.Model):
    payload = models.CharField(max_length=32)
    status = models.CharField(max_length=16, default="pending")   # pending/processing/done
    lease_at = models.DateTimeField(null=True)
    class Meta:
        app_label = "demo"
        indexes = [models.Index(fields=["status"])]

with connection.schema_editor() as se:
    se.create_model(Task)
Task.objects.bulk_create([Task(payload=f"job-{i}") for i in range(5)])

def claim(worker_id):
    with transaction.atomic():
        try:
            qs = Task.objects.filter(status="pending").order_by("id")
            rows = list(qs.select_for_update(skip_locked=True, nowait=False)[:2])  # PG/MySQL 8: 跳过被锁行
        except Exception as e:
            # SQLite 降级:乐观认领,UPDATE 原子抢行,抢到几条算几条
            print(f"  (worker{worker_id}) 当前引擎不支持 FOR UPDATE({type(e).__name__}),走乐观认领")
            ids = list(Task.objects.filter(status="pending").values_list("id", flat=True)[:2])
            updated = Task.objects.filter(id__in=ids, status="pending").update(status="processing")
            return list(Task.objects.filter(id__in=ids)[:updated])
        for t in rows:
            t.status = "processing"; t.save(update_fields=["status"])
        return rows

claimed = claim(worker_id=1)
print(f"worker1 认领: {[t.payload for t in claimed]}(状态已置 processing,锁随事务提交释放)")
claimed2 = claim(worker_id=2)
print(f"worker2 认领: {[t.payload for t in claimed2]} —— 互不重复,互不等待")
# 生产要点:processing 任务带 lease_at,回收器把租约过期的任务重置 pending(防 worker 崩溃丢任务)
```

**追问**：
1) 为什么锁窗口只覆盖认领、不覆盖执行？——行锁随事务存活，执行阶段可能几分钟，长事务会撑爆连接与锁表、还阻塞回收器；把「认领」和「执行」拆成两个事务，用状态+租约传递所有权，是 DB 队列区别于「一把锁到底」的关键设计。
2) 租约回收会不会和慢执行中的 worker 冲突？——会：worker 只是慢（GC 停顿/网络抖动），租约过期任务被重置后另一个 worker 再执行，就出现双执行。所以任务本身必须幂等（结果表唯一约束兜底），或者租约设计成「心跳续租」：执行中 worker 定期续 lease_at，只有真正失联才被回收。
3) 认领查询为什么可能仍然慢？——`ORDER BY id LIMIT 2 ... FOR UPDATE SKIP LOCKED` 在 PG 上会跳过锁行但仍要沿索引扫到足够的未锁行；pending 大量积压且头部任务被长期锁住时扫描拉长。缓解：减少长锁持有、按分区清理 done 行、必要时 `ORDER BY id` 改为「桶 + 随机偏移」打散。
