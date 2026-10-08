# 909 Go select 深挖

> 覆盖源 9-9 全文：select 底层（scase/selectgo）、特性（随机/阻塞/default）、空 select 优化。主卡已拆成底层结构、特性、空 select 三张，本附录做串联与取舍。

## 思路与架构

```mermaid
graph TD
A[select] --> B[控制结构: 多路IO复用]
A --> C[编译期: case→scase数组(c/element)]
A --> D[运行时: selectgo 遍历就绪]
D --> D1[有就绪→随机执行]
D --> D2[全阻塞+default→default]
D --> D3[全阻塞无default→挂起]
A --> E[空select: 编译转 block 挂起]
```

## 方案取舍
- **随机 vs 顺序**：多 case 就绪随机执行是为公平性（防饥饿），与 switch 的顺序执行不同，是核心易错点。
- **空 select vs for{}**：空 select 编译优化为挂起让出 CPU；for{} 空转耗 CPU，永久等待必用空 select。
- **default 代价**：default 使 select 非阻塞但空转，高并发需配合超时（`time.After`）避免长期空转。

## 答题技巧
- 被问「select 底层」先答「控制结构+多路复用」，再 scase/selectgo，最后特性与空 select 优化 [经验]。
- 主动边界到 `612`(关闭 channel 操作)、`816`(GMP 让出 CPU)，构成 select 全栈 [边界]。
