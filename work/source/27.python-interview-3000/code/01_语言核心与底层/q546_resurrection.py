import gc

class Phoenix:
    def __del__(self):
        print("__del__ running")
        globals()["keep"] = self          # 复活:重新建立引用

if __name__ == "__main__":
    p = Phoenix()
    del p                                 # 计数归零,触发 __del__
    print("resurrected as:", type(keep).__name__)
    keep = None                           # 再次失去引用
    gc.collect()
    print("behavior after resurrection is implementation-defined — do not rely on it")
