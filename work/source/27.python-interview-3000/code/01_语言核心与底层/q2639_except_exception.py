"""except Exception 拦不住 BaseException 直系子类。"""


def risky():
    raise KeyboardInterrupt          # 模拟 Ctrl+C


if __name__ == "__main__":
    # except Exception 放行 KeyboardInterrupt
    try:
        try:
            risky()
        except Exception:
            print("不会打印:Exception 接不住")
    except KeyboardInterrupt:
        print("KeyboardInterrupt 穿透了 except Exception")

    # 最外层收口:必须重新抛出
    try:
        risky()
    except BaseException as exc:
        print("BaseException 收口:", type(exc).__name__, "-> 应该 raise")
        # 正确姿势是 raise,演示进程不退出这里选择不重抛
