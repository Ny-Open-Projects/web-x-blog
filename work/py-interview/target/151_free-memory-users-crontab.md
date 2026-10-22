# 151. 内存查看 / 用户组 / 定时任务：free / useradd / crontab

> 分类：操作系统/Linux | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**free** / **内存排查** / **useradd** / **crontab**
> 原文锚点：第 57~59, 69~71, 80 段「free 看可用内存（各列含义）；useradd/usermod/groupadd/groupdel 管用户组；crontab 定时任务」

## 一句话总述
**`free -h`** 看系统内存（重点看可用 `available` 与缓存）；用户/组用 **`useradd`/`usermod`/`groupadd`/`groupdel`**；**`crontab -e`** 配置定时任务——这些偏运维，但内存排查与定时任务是后端常碰到的。

## 面试官视角
- **考察意图**：考你能否用 `free` 判断"内存是否泄露/不足"，以及基础运维命令。
- **P5** 能说出 `free` 看内存、`useradd` 加用户、`crontab` 定时 / **P6** 能讲清 `free` 里 `available`（真正可用）与 `buff/cache`（可回收缓存）的区别，并写出 crontab 五段式 / **P7** 能指出 `free` 的 `available` 才是"还能拿来用的内存"（不是看 `free` 列），以及 crontab 时区/环境变量的坑 `[经验]`。
- **红旗**：① 以为 `free` 列很小就是内存不够（实际看 `available`）；② 把 `buff/cache` 当"已用"紧张；③ crontab 五段式写错（分 时 日 月 周）。
- **惊艳点**：`free -h` 的 `available` ≈ `free + buff/cache 可回收部分`，是判断内存压力的可靠指标。验证：`free -h` 对比 `top` 的可用内存 `[实测]`。

## 主问答
**Q：怎么判断服务器内存不够？怎么加定时任务？**
**A：**
1. **结论**：用 **`free -h`** 看内存，关键看 **`available`**（真正可用），不是看 `free` 列；定时任务用 **`crontab -e`** 配五段式。
2. **机制**：`buff/cache` 是内核可回收的缓存，不算"紧张"；`available` 才是进程还能申请的内存。crontab 五段 = `分 时 日 月 周 命令`。
3. **边界**：`useradd`/`usermod` 管用户、`groupadd`/`groupdel` 管组（普通开发少碰）；crontab 注意**环境变量为空**、路径用绝对路径。
**加分层**：内存持续上涨且 `available` 趋零，结合 `top` 定位进程，疑似泄露再用 memory profiler 分析。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 看内存命令 | 基础 | free -h | 换题 → 不及格 |
| L2 | available 含义 | 机制 | 真正可用 | 判 P5 |
| L3 | crontab 格式 | 细节 | 五段式 | 判 P6 |
| L4 | buff/cache 误判 | 辨析 | 可回收 | 判 P6+ |
| L5 | 泄露定位 | 深入 | profiler | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 各 Unix/Linux | free 列一致 | 看 available |
| free | -h 人类可读 | 旧版无 available |
| cron | 五段式 | 注意环境/时区 |

## 关键代码
```bash
free -h                 # 看内存，重点 available
top                     # 实时定位吃内存的进程
useradd dev && usermod -aG docker dev
crontab -e              # 五段式：分 时 日 月 周 命令
# 例：0 2 * * * /opt/backup.sh
```

```python
import shutil, subprocess
print(shutil.which("crontab"))              # 查 crontab 是否在 PATH
subprocess.run(["free", "-h"], check=True)  # 等价 free -h
```

## ⚠️ 原文纠错
原文"free 看系统可用内存（需了解各列含义，便于排查内存泄露）；useradd/usermod 增改用户、groupadd/groupdel 增删组；crontab 定时任务"——准确（机翻"crowntab"=**crontab**，"groupprde/groupremode"=**groupadd/groupdel**，"useradd/usermode"=**useradd/usermod**）。原文未强调"available 才是真正可用、buff/cache 可回收"，以及"macOS 无 free 命令"（原文提及 Mac 无 free），已在机制与 P7 补充 `[经验]`。无事实错误，仅术语音译需还原。

## 总结与追问预判
- free -h 看 available；crontab 五段式定时。
- 下一题：**进程 vs 线程**（152）、**网络命令**（150）。
