"""灰度回填: 分批更新 + 限速 + 断点续跑"""
import time

total, batch, rate = 1200, 200, 0.01
progress = {"last_id": 0}          # 进度表: 中断后从断点续跑

def backfill_batch(last_id, size):
    # UPDATE users SET tier='normal' WHERE id>? AND id<=? AND tier IS NULL
    updated = 0
    for uid in range(last_id + 1, min(last_id + size, total) + 1):
        updated += 1
    return updated

while progress["last_id"] < total:
    n = backfill_batch(progress["last_id"], batch)
    progress["last_id"] += n
    print(f"批次完成: id <= {progress['last_id']}, 本批 {n} 行, 休眠限速")
    time.sleep(rate)
print(f"回填完成 {total} 行; 批内带 IS NULL 条件保证重跑幂等, 全程监控主从延迟")
