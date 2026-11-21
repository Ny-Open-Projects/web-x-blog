# 第 12 册 Arthas 线上诊断实操手册 —— 从"听说过"到"面试官信你用过"

> 判断一个候选人是否真的排查过线上问题，就看他能不能说出 Arthas 命令的**输出长什么样、
> 下一步接什么命令**。本手册按真实故障场景组织，每个场景给出：命令 → 输出解读 → 下一步。
> 全部命令都可在本机装个 JDK 后实际演练（练习工程见 notes/）。

---

## 12.0 安装与启动（30 秒版）

```bash
# 下载并启动（目标 JVM 需要 JDK 环境；JDK9+ 需加参数）
curl -O https://arthas.aliyun.com/arthas-boot.jar
java -jar arthas-boot.jar          # 交互式选择目标 Java 进程
# JDK 11+ 若 attach 失败：java -jar arthas-boot.jar --select <pid>
# Web 控制台：默认 http://127.0.0.1:8563
```

生产守则（面试可背三条）：
1. Arthas 本身有开销（增强字节码），**用完必须 stop**，不要留着过夜；
2. watch/trace 高频方法要加 `-n 次数` 限制和条件表达式，避免打爆 IO；
3. 改变类状态的命令（redefine/vmoption）要走变更审批——它和改配置同级。

---

## 12.1 场景一：CPU 飙到 100%，定位热点线程

**命令链：dashboard → thread → thread -n 3 → thread -b**

```
dashboard                    # 实时面板：线程、内存、GC 三栏
thread                       # 所有线程及 CPU 占用（第一列是 CPU%）
thread -n 3                  # 最忙的 3 个线程（含堆栈，一步到位）
thread --state BLOCKED       # 只看阻塞线程（死锁初判）
thread -b                    # 直接找死锁（Blocked one another）
```

**输出解读（背这个直觉）**：
- `thread -n 3` 显示某业务线程 CPU 高 → 看栈顶：
  - 栈顶是**业务代码行** → 死循环/低效算法，直接看那行；
  - 栈顶是 `HashMap.getNode` 大量出现 → 可能 hash 碰撞或并发误用；
  - 栈顶是 `Thread.sleep` 却 CPU 高 → 不可能，说明是别的线程在烧（刷新 thread 再看）；
  - 大量 `GC task thread` 忙 → 不是代码热点，是 GC 风暴，转场景三。
- `thread -b` 有输出 → 打印出互相等待的两个线程与锁地址，死锁实锤。

**下一步**：确认代码行后用 `jad 类名` 在线反编译，核对运行中的代码与预期版本是否一致（80% 的"诡异热点"是老版本代码）。

---

## 12.2 场景二：接口偶现超时，想看慢在哪一行

**命令链：trace → watch → tt**

```
trace com.demo.OrderService createOrder '#cost > 200' -n 5
# 只打印耗时超过 200ms 的调用，-n 5 抓 5 次后自动停
```

**输出解读**：树形输出每层方法耗时，`...` 表示中间还有一层，哪个子节点耗时最大一目了然。
- 例：`trace` 显示 `dao.selectUser` 占了 180ms → 下钻 `trace ...OrderDao selectUser`，或直接看 SQL；
- 多次采样对比：偶现超时往往只在特定参数下慢 → 用 `tt`（Time Tunnel）：

```
tt -t com.demo.OrderService createOrder     # 记录每次调用的现场
tt -l                                        # 列出记录
tt -p -i 1003                                # 回放第 1003 号记录（重放现场！）
tt -w '{params[0], throwExp, #cost}' -i 1003 # 查看入参/异常/耗时
```

**watch 看变量**（不想 trace 整链，只看某方法出入参）：

```
watch com.demo.OrderService createOrder '{params, returnObj, throwExp}' -x 3 -n 2
# -x 3 展开对象 3 层；-n 2 两次后退出；条件：'params[0].amount > 1000'
```

**面试话术（可背）**："trace 定位慢在哪个方法，watch 看那个方法的出入参，tt 把偶现问题'存档回放'——三者是一套组合拳，从现象到根因一般 10 分钟内收敛。"

---

## 12.3 场景三：频繁 Full GC / 内存问题

**命令链：dashboard（看 GC 栏）→ memory → heapdump → jvm → vmtool**

```
memory                        # 各内存区实时占用（堆/元空间/直接内存）
jvm                           # JVM 关键参数与汇总（GC 名、堆大小、加载类数）
heapdump /tmp/live.hprof --live   # 只 dump 存活对象（等价 jmap -dump:live）
vmtool --action getInstances --className com.demo.Cache --limit 10
# 直接从堆里捞出 Cache 实例，看看它到底缓存了什么
getstatic com.demo.Cache MAP  # 看静态 Map 的实时内容（泄漏实锤神器）
```

**输出解读**：
- `memory` 里 metaspace 持续涨 → 动态类生成（CGLIB/Groovy），配合 `classloader -t` 看有没有异常数量的加载器；
- `heapdump` 后用 MAT 分析（第 3 章三板斧）；
- `getstatic` 直接确认"只进不出的静态 Map"类泄漏——不用导 dump 就能实锤，面试讲这个细节非常加分。

**Full GC 触发源排查**：
```
vmoption PrintGCDetails true          # 在线开 GC 日志（JDK8；9+ 用 -Xlog）
vmtool --action getInstances --className java.lang.management.GarbageCollectorMXBean
```
- 看是谁调的 System.gc()：`stack java.lang.System gc` —— 有人代码里手动 gc 就现形。

---

## 12.4 场景四：改了一行代码，能不能不重启？（热修复）

```
jad com.demo.RuleEngine       # 在线反编译，确认现状
sc -d com.demo.RuleEngine     # 查类信息（从哪个 jar 加载、类加载器）
mc /tmp/RuleEngine.java -d /tmp   # 内存编译
redefine /tmp/com/demo/RuleEngine.class   # 热替换（老版本命令；新版用 retransform）
retransform /tmp/com/demo/RuleEngine.class
```

**纪律（P10 必说）**：热修复是**止血手段不是发布手段**——替换后必须 24h 内走正常发版对齐，否则重启后回滚成老代码，形成"内存态与磁盘态不一致"的定时炸弹。retransform 需要jad导出的源码改后再编译，且不能改方法结构（只能改方法体）。

---

## 12.5 场景五：方法调用统计与性能基线

```
monitor com.demo.OrderService createOrder -c 60
# 每 60 秒输出一次：调用次数、成功率、平均 RT —— 相当于临时埋点
profiler start                 # async-profiler 集成：开始采样
profiler stop --format html    # 生成火焰图（浏览器打开，一眼定位热点）
profiler stop --format flames  # 交互式火焰图
```

**火焰图怎么看（面试考点）**：横轴 = 采样占比（宽 = 慢/频繁），纵轴 = 调用栈（上=栈顶）。找"平顶山"——宽且顶部的栈就是热点。CPU 火焰图看 on-cpu；内存用 `profiler start --event alloc`。

---

## 12.6 场景六：类加载与依赖冲突（NoClassDefFoundError / NoSuchMethodError）

```
classloader -t                # 列出所有类加载器（看有没有异常数量的 URLClassLoader）
sc -d com.fasterxml.jackson.databind.ObjectMapper   # 类从哪来的
sm java.lang.String valueOf   # 列出一个类的所有方法签名
ognl '@java.lang.System@getProperty("java.class.path")'  # ognl 直接执行任意静态调用
```

**NoSuchMethodError 标准排查**：`sc -d` 看这个类被哪个 jar 提供的（往往同一类有两个版本），`classloader -t` 确认加载器，然后修 maven 依赖树（`mvn dependency:tree -Dincludes=xxx`）。面试金句："依赖冲突的本质是**类加载的单一性原则**被破坏，同一个类全限定名只能有一个赢家。"

---

## 12.7 速查表（打印贴墙版）

| 需求 | 命令 | 关键点 |
|------|------|--------|
| 总览 | dashboard | 线程/内存/GC 三栏 |
| CPU 热点 | thread -n 3 | 栈顶决定下一步 |
| 死锁 | thread -b | 直接定位互相等待 |
| 慢方法 | trace '#cost>200' -n 5 | 树形耗时分解 |
| 看入参出参 | watch '{params,returnObj,throwExp}' -x 3 | 加条件表达式 |
| 偶现问题存档 | tt -t / tt -p -i N | 时光机回放 |
| 内存泄漏 | memory + heapdump --live | MAT 支配树 |
| 静态变量实锤 | getstatic / vmtool getInstances | 免 dump 确认 |
| 热点采样 | profiler start/stop --format html | 火焰图找平顶山 |
| 类来源 | sc -d / classloader -t | 依赖冲突排查 |
| 临时埋点 | monitor -c 60 | 成功率+RT |
| 在线反编译 | jad | 核对运行中代码版本 |
| 热修复 | retransform | 止血用，24h 内正式发版 |
| JVM 参数 | vmoption / sysprop | 在线开关诊断参数 |

## 12.8 面试叙事模板（Arthas 版）

背景：某核心接口 P99 从 80ms 恶化到 1.2s，发布无变更 →
第一步 dashboard 发现 GC 栏异常，jstat 确认 Young GC 频繁但正常 →
第二步 trace 慢在下游查询，watch 发现入参中偶现"超长列表"（运营批量操作）→
第三步 tt 回放确认：一次 5000 个元素的 IN 查询 →
修复：分批 + 索引优化 + 对该入参加限制 →
沉淀：批量接口大小门禁进 CI。
**叙事里必须出现 2~3 个具体命令与输出特征**，这是"真用过"的唯一证据。

---
*下一册：第 13 册 手写代码题全解 —— DCL/LRU/生产者消费者/线程池/TopK，全部可背可写。*
