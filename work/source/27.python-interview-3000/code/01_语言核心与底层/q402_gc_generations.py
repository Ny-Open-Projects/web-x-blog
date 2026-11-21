import gc

print("thresholds:", gc.get_threshold())        # (700, 10, 10) 默认值
print("counts before:", gc.get_count())         # 三个代各自的计数器

class Box:
    pass

boxes = [Box() for _ in range(700)]
gc.collect()                                    # 手动触发,观察计数变化

# 晋升演示:多次回收后,存活对象从 0 代晋升到更高代
for _ in range(5):
    gc.collect()
print("counts after:", gc.get_count())
print("gen2 objects tracked:", len(gc.get_objects(2)))
