import gc

def track():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        print("[cleanup] GeneratorExit caught, releasing resource")
        raise                     # 必须重新抛出,让 close 正常收尾

if __name__ == "__main__":
    g = track()
    print(next(g))
    g.close()                     # 显式关闭:清理代码在此执行

    g2 = track()
    print(next(g2))
    del g2                        # CPython 引用归零,立即触发隐式 close
    gc.collect()                  # 其他实现依赖 GC,这里兜底
    print("done")
