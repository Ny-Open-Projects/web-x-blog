import math
from datetime import datetime

value = 1234567.891
now = datetime(2026, 11, 1, 9, 30)

if __name__ == "__main__":
    print(f"{math.pi:.3f}")                    # 精度
    print(f"{value:,.2f}")                     # 千分位
    print(f"{value:+012.1f}")                  # 宽度 正号 补零
    print(f"{255:x} {255:#06x} {255:b}")       # 进制
    print(f"{now:%Y-%m-%d %H:%M}")             # datetime 指令
    print(f"{'left':<10}|{'right':>10}|{'center':^10}")
    print(f"{value:.2e}")                      # 科学计数
    print(f"{value=:.2f}")                     # 3.8 调试语法
