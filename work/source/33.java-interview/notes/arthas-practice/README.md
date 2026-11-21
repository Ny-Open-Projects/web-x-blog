# Arthas 本地练习工程 —— 第 12 册的实战沙盘

> 一个单文件 Java 工程（零依赖，JDK8+ 可编译），内置 4 种"刻意埋好的故障"。
> 目标：把第 12 册的 6 大场景从"读过"变成"亲手做过"——面试时你才说得出命令输出长什么样。

## ✅ 环境状态（2026-11-14 已由助手配置并全链路验证）

- **JDK 21.0.2**（OpenJDK GA）：`C:\Users\Administrator\.zcode\tools\jdk-21.0.2`
  - JAVA_HOME 已写入用户环境变量，java/bin 已加入用户 PATH——**新开终端直接可用**
  - 注意：已开启的旧终端不会自动生效，重开或手动 `export PATH="/c/Users/Administrator/.zcode/tools/jdk-21.0.2/bin:$PATH"`
- **Arthas 4.3.5**：`arthas-boot.jar` 在本目录；完整 arthas core 在 `C:\Users\Administrator\.arthas\lib\4.3.5\arthas`
- **已验证的工作记录**（真实输出）：
  - `javac -encoding UTF-8 ArthasPractice.java` ✅
  - 4 种模式全部运行验证 ✅（leak 每秒+1MB、slow 出现 10% 慢调用、deadlock 双线程互等）
  - **attach 成功**：`thread -n 2` 输出 main 线程栈（停在 slowService:110）✅
  - **trace 命中**：`trace ArthasPractice slowService '#cost > 300' -n 2` 抓到 601ms/720ms 两次慢调用 ✅

### ⚠️ Windows Git Bash 的一个坑（真实踩过）

`java ArthasPractice slow &` 后用 `$!` 拿到的是 **Git Bash 伪 PID**（MSYS 命名空间），
Arthas attach 会报 `java.io.IOException: no such process`。
**正确做法：用 `jps -l` 拿真实 Windows PID 再附加**：

```bash
export PATH="/c/Users/Administrator/.zcode/tools/jdk-21.0.2/bin:$PATH"
cd /c/Users/Administrator/Desktop/java-interview/notes/arthas-practice
java ArthasPractice slow > out_slow.txt 2>&1 &
sleep 4
WINPID=$(jps -l | grep ArthasPractice | awk '{print $1}')
timeout 120 java -jar arthas-boot.jar $WINPID -c "trace ArthasPractice slowService '#cost > 300' -n 2"
kill %1    # 结束沙盘
```



## 四个实验（每个 10 分钟）

### 实验 1：CPU 热点（对应第 12 册场景一）

```bash
# 终端 A：启动
java ArthasPractice cpu
# 终端 B：附上 Arthas，选这个进程
java -jar arthas-boot.jar
```

在 Arthas 里依次执行，并对照预期：
```
dashboard          # 观察 cpu-burner 线程 CPU 高
thread -n 3        # 栈顶应指向 ArthasPractice.hotMethod 的具体行号
```
**✅ 通过标准**：你能指着栈顶行号说出"哪一行在烧 CPU"。

### 实验 2：内存泄漏（对应场景三）

```bash
java ArthasPractice leak
```

```
dashboard                  # 看 old 区曲线持续爬升，不回落
memory                     # heap 占用持续增长
getstatic ArthasPractice LEAK   # 实锤：看到 ArrayList 里的 byte[] 在涨
heapdump /tmp/leak.hprof --live  # 导出后用 MAT 打开，Leak Suspects 应指向 LEAK
```
**✅ 通过标准**：MAT 的支配树里能看到 `ArthasPractice.LEAK` 持有几百 MB byte[]。

### 实验 3：慢方法定位（对应场景二）

```bash
java ArthasPractice slow
```

```
trace ArthasPractice slowService '#cost > 300' -n 5
# 预期：只有 10% 的慢调用被打印（sleep 500-800ms 的那次）
watch ArthasPractice slowService '{params, returnObj, #cost}' -x 2 -n 5
tt -t ArthasPractice slowService        # 记录几条
tt -l                                    # 列出
tt -p -i <index>                         # 回放一条，感受"时光机"
```
**✅ 通过标准**：你能解释 `#cost > 300` 单位是毫秒、为什么 watch 要加 `-n` 限制。

### 实验 4：死锁（对应第 13 册题 8）

```bash
java ArthasPractice deadlock
```

```
thread -b                    # 输出 "Found one Java-level deadlock"，指出 t1/t2 与两把锁
thread --state BLOCKED       # 两个 BLOCKED 线程与锁地址
```
**✅ 通过标准**：不查文档你能说出修复方案（统一加锁顺序 A→B），并解释 t1/t2 为什么必须同序。

## 进阶：热修复演练（可选）

1. 在 `slowService` 的 sleep 前加一行 `System.out.println("v2");`；
2. `jad ArthasPractice slowService` 导出源码 → 修改 → `mc` 编译 → `retransform` 加载；
3. 观察输出变化 → **然后立刻重新编译原版还原**——体会"热修复必须 24h 内对齐正式版本"的纪律（第 12 册 12.4）。

## 练习完成后

```bash
# Arthas 会话内
stop           # 必须执行：增强有开销，不要留着过夜
```

## 与面试的关系

做完这 4 个实验，你在面试里说"当时 `thread -n 3` 栈顶指向 hotMethod 第 89 行"时，
面试官追问"输出大概长什么样、下一步接什么命令"，你能秒答——
这就是第 12 册说的"从听说过到信你用过"的分界线。
