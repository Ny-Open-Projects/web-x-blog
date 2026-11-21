import logging
import time

def expensive_transform(n):
    time.sleep(0.01)
    return n * 2

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger("demo")

    data = [1, 2, 3]
    log.info("data is %s", data)          # 参数化:级别过滤时不拼字符串
    if log.isEnabledFor(logging.DEBUG):   # 昂贵参数用级别门卫
        log.debug("expensive: %s", expensive_transform(len(data)))

    log.debug("eager: %s" % expensive_transform(3))   # 反面教材:总会求值
    print("done — notice the eager call slept even though DEBUG is off")
