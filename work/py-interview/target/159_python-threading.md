# 159. Python 多线程：threading 模块

> 分类：并发 | 难度：L2 | 题型：工程题 | 频率：高 | 关键词：**threading.Thread** / **start** / **join** / **Lock**
> 原文锚点：第 66~73 段「用 threading 模块的 Thread 类创建线程，start 启动，join 等待」

## 一句话总述
Python 多线程用 **`threading.Thread`** 创建，`start()` 启动、`join()` 等待结束；配合 **`threading.Lock`** 保护共享数据，适合 **IO 密集型** 任务。

## 面试官视角
- **考察意图**：会不会实际写多线程，以及是否知道它适合什么场景（IO 密集而非 CPU 密集）。
- **P5** 会 `Thread(target=...)` + `start` + `join` / **P6** 能解释 `join` 的阻塞等待语义、守护线程 `daemon` / **P7** 能说出多线程在 CPU 密集下受 GIL 限制、应换多进程；以及线程数并非越多越好。
- **红旗**：用多线程跑密集计算还指望加速；或不 `join` 导致主线程提前退出。
- **惊艳点**：`threading` 与 `multiprocessing` 的 **API 几乎一致**（都是 `Thread/Process` + `start/join`），迁移成本极低 —— 验证：同一段逻辑只改 import 即切换 `[经验]`。

## 主问答
**Q（面试官原话）：** Python 里怎么写多线程？要注意什么？

**A · 标准答案骨架：**
1. **先给结论**：用 **`threading.Thread`** 创建线程，`start()` 启动、`join()` 等它结束。
2. **再给机制**：`target` 传函数，`args` 传参；`join()` 阻塞主线程直到子线程完成；共享数据用 **`Lock`** 包临界区。
3. **最后给边界**：多线程适合 **IO 密集**（等待时释放 GIL）；**CPU 密集**请换 **多进程**，否则反而更慢。

**加分层**：线程不是越多越好——上下文切换与锁竞争会抵消收益，IO 场景通常按"并发连接数"而非"核数"定线程数 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 怎么创建线程 | 基本认知 | Thread + start | 换题 → 不及格 |
| L2 | join 干嘛用 | 是否背的 | 等待子线程结束 | 判 P5 |
| L3 | 多线程适合什么场景 | 有没有真理解 | IO 密集、受 GIL 限 | 判 P6 |
| L4 | 和 multiprocessing 区别 | 架构判断 | 线程共享/进程隔离 | 判 P6+ |
| L5 | 你调过线程池吗 | 实战经验 | ThreadPoolExecutor 用法 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 3.x | 无 | `threading` API 稳定；3.2+ 推荐 `concurrent.futures.ThreadPoolExecutor` 管理池 |

## 关键代码
```python
import threading
def task(n):
    print("run", n)

t = threading.Thread(target=task, args=(1,))
t.start()          # 启动线程
t.join()           # 阻塞等待其结束 [实测]
```

## ⚠️ 原文纠错
原文第 66~72 段将模块名拼为「**threed**」「**threed模模块**」，正确为 **`threading`**；第 72 段「**pythstarlock**」应为 **`threading.Lock`**。概念（Thread/start/join/锁）论述正确。核对范围：第 66~73 段 threading 多线程示例。

## 总结与追问预判
- `threading.Thread` + `start`/`join` + `Lock`；适合 IO 密集，CPU 密集换多进程。
- 顺势会问：**多进程（见 160 卡）**、**GIL（见 153 卡）**。
