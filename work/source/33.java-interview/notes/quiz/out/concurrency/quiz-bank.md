# 笔试题库 · 并发编程（知识点 110 条）

**Qconcurrency-1000（单选·正向·内存语义）** 关于「volatile」的说法，正确的是？
- A. volatile 能保证 i++ 的原子性
- B. volatile 完全替代 synchronized
- C. volatile 保证可见性与有序性，但不保证原子性
- D. volatile 变量读写有锁开销与 synchronized 相当
**答案：C**
**解析：** volatile 保证可见性与有序性，但不保证原子性。原因：JMM 对 volatile 写强制刷新到主存、读强制从主存加载，并通过内存屏障禁止特定重排；但 i++ 这类复合操作仍是读-改-写三步。
**来源：** JC-001 · volatile（JLS 17.4）

**Qconcurrency-1001（判断·内存语义）** volatile 保证可见性与有序性，但不保证原子性
**答案：对。** 解析：JMM 对 volatile 写强制刷新到主存、读强制从主存加载，并通过内存屏障禁止特定重排；但 i++ 这类复合操作仍是读-改-写三步

**Qconcurrency-1002（判断·内存语义）** volatile 能保证 i++ 的原子性
**答案：错。** 正确表述：volatile 保证可见性与有序性，但不保证原子性。原因：JMM 对 volatile 写强制刷新到主存、读强制从主存加载，并通过内存屏障禁止特定重排；但 i++ 这类复合操作仍是读-改-写三步

**Qconcurrency-1003（判断·内存语义）** volatile 完全替代 synchronized
**答案：错。** 正确表述：volatile 保证可见性与有序性，但不保证原子性。原因：JMM 对 volatile 写强制刷新到主存、读强制从主存加载，并通过内存屏障禁止特定重排；但 i++ 这类复合操作仍是读-改-写三步

**Qconcurrency-1004（判断·内存语义）** volatile 变量读写有锁开销与 synchronized 相当
**答案：错。** 正确表述：volatile 保证可见性与有序性，但不保证原子性。原因：JMM 对 volatile 写强制刷新到主存、读强制从主存加载，并通过内存屏障禁止特定重排；但 i++ 这类复合操作仍是读-改-写三步

**Qconcurrency-1005（场景单选·内存语义）** 在工程实践中关于「volatile」，下列做法符合推荐实践的是？
- A. volatile 完全替代 synchronized
- B. volatile 变量读写有锁开销与 synchronized 相当
- C. 状态标志位、一写多读的配置开关
- D. volatile 能保证 i++ 的原子性
**答案：C**
**解析：** 推荐实践：状态标志位、一写多读的配置开关。事实依据：volatile 保证可见性与有序性，但不保证原子性。

**Qconcurrency-1006（场景判断·内存语义）** 推荐实践：状态标志位、一写多读的配置开关
**答案：对。** 解析：volatile 保证可见性与有序性，但不保证原子性。原因：JMM 对 volatile 写强制刷新到主存、读强制从主存加载，并通过内存屏障禁止特定重排；但 i++ 这类复合操作仍是读-改-写三步

**Qconcurrency-1007（填空·内存语义）** ______ 保证可见性与有序性，但不保证原子性
**答案：volatile**。解析：JMM 对 volatile 写强制刷新到主存、读强制从主存加载，并通过内存屏障禁止特定重排；但 i++ 这类复合操作仍是读-改-写三步

**Qconcurrency-1008（简答·内存语义）** 请说明「volatile」中volatile的机制与使用要点。
**要点（标准答案）**：① volatile 保证可见性与有序性，但不保证原子性；② 原理：JMM 对 volatile 写强制刷新到主存、读强制从主存加载，并通过内存屏障禁止特定重排；但 i++ 这类复合操作仍是读-改-写三步；③ 使用要点：状态标志位、一写多读的配置开关。版本锚点：JLS 17.4。

**Qconcurrency-1009（单选·正向·原子性）** 关于「volatile」的说法，正确的是？
- A. i++ 丢失更新只发生在解释执行时
- B. 用 AtomicLong 与 volatile long 行为完全一样
- C. i++ 即使变量声明为 volatile 也不是线程安全的
- D. 加 volatile 后自增就安全了
**答案：C**
**解析：** i++ 即使变量声明为 volatile 也不是线程安全的。原因：i++ 是读取、加一、写回三个操作，两个线程交错执行会丢失更新，实测丢失可达数万次。
**来源：** JC-002 · volatile（JLS 17.7）

**Qconcurrency-1010（判断·原子性）** i++ 即使变量声明为 volatile 也不是线程安全的
**答案：对。** 解析：i++ 是读取、加一、写回三个操作，两个线程交错执行会丢失更新，实测丢失可达数万次

**Qconcurrency-1011（判断·原子性）** 加 volatile 后自增就安全了
**答案：错。** 正确表述：i++ 即使变量声明为 volatile 也不是线程安全的。原因：i++ 是读取、加一、写回三个操作，两个线程交错执行会丢失更新，实测丢失可达数万次

**Qconcurrency-1012（判断·原子性）** i++ 丢失更新只发生在解释执行时
**答案：错。** 正确表述：i++ 即使变量声明为 volatile 也不是线程安全的。原因：i++ 是读取、加一、写回三个操作，两个线程交错执行会丢失更新，实测丢失可达数万次

**Qconcurrency-1013（判断·原子性）** 用 AtomicLong 与 volatile long 行为完全一样
**答案：错。** 正确表述：i++ 即使变量声明为 volatile 也不是线程安全的。原因：i++ 是读取、加一、写回三个操作，两个线程交错执行会丢失更新，实测丢失可达数万次

**Qconcurrency-1014（场景单选·原子性）** 在工程实践中关于「i++」，下列做法符合推荐实践的是？
- A. 计数场景改用 AtomicLong 或加锁
- B. i++ 丢失更新只发生在解释执行时
- C. 加 volatile 后自增就安全了
- D. 用 AtomicLong 与 volatile long 行为完全一样
**答案：A**
**解析：** 推荐实践：计数场景改用 AtomicLong 或加锁。事实依据：i++ 即使变量声明为 volatile 也不是线程安全的。

**Qconcurrency-1015（场景判断·原子性）** 推荐实践：计数场景改用 AtomicLong 或加锁
**答案：对。** 解析：i++ 即使变量声明为 volatile 也不是线程安全的。原因：i++ 是读取、加一、写回三个操作，两个线程交错执行会丢失更新，实测丢失可达数万次

**Qconcurrency-1016（填空·原子性）** ______ 即使变量声明为 volatile 也不是线程安全的
**答案：i++**。解析：i++ 是读取、加一、写回三个操作，两个线程交错执行会丢失更新，实测丢失可达数万次

**Qconcurrency-1017（简答·原子性）** 请说明「volatile」中i++的机制与使用要点。
**要点（标准答案）**：① i++ 即使变量声明为 volatile 也不是线程安全的；② 原理：i++ 是读取、加一、写回三个操作，两个线程交错执行会丢失更新，实测丢失可达数万次；③ 使用要点：计数场景改用 AtomicLong 或加锁。版本锚点：JLS 17.7。

**Qconcurrency-1018（单选·正向·内存语义）** 关于「volatile」的说法，正确的是？
- A. volatile 的有序性靠编译器在读写前后插入内存屏障实现
- B. volatile 有序性靠 CPU 自动完成无需屏障
- C. 所有屏障都插入在 volatile 读之前
- D. volatile 修饰后代码不再有任何重排包括非 volatile 部分
**答案：A**
**解析：** volatile 的有序性靠编译器在读写前后插入内存屏障实现。原因：volatile 写之后插入 StoreLoad 屏障（最重的屏障），读之后插入 LoadLoad 与 LoadSrc 屏障，阻止跨屏障重排。
**来源：** JC-003 · volatile（JSR-133）

**Qconcurrency-1019（判断·内存语义）** volatile 的有序性靠编译器在读写前后插入内存屏障实现
**答案：对。** 解析：volatile 写之后插入 StoreLoad 屏障（最重的屏障），读之后插入 LoadLoad 与 LoadSrc 屏障，阻止跨屏障重排

**Qconcurrency-1020（判断·内存语义）** volatile 有序性靠 CPU 自动完成无需屏障
**答案：错。** 正确表述：volatile 的有序性靠编译器在读写前后插入内存屏障实现。原因：volatile 写之后插入 StoreLoad 屏障（最重的屏障），读之后插入 LoadLoad 与 LoadSrc 屏障，阻止跨屏障重排

**Qconcurrency-1021（判断·内存语义）** 所有屏障都插入在 volatile 读之前
**答案：错。** 正确表述：volatile 的有序性靠编译器在读写前后插入内存屏障实现。原因：volatile 写之后插入 StoreLoad 屏障（最重的屏障），读之后插入 LoadLoad 与 LoadSrc 屏障，阻止跨屏障重排

**Qconcurrency-1022（判断·内存语义）** volatile 修饰后代码不再有任何重排包括非 volatile 部分
**答案：错。** 正确表述：volatile 的有序性靠编译器在读写前后插入内存屏障实现。原因：volatile 写之后插入 StoreLoad 屏障（最重的屏障），读之后插入 LoadLoad 与 LoadSrc 屏障，阻止跨屏障重排

**Qconcurrency-1023（场景单选·内存语义）** 在工程实践中关于「内存屏障」，下列做法符合推荐实践的是？
- A. volatile 修饰后代码不再有任何重排包括非 volatile 部分
- B. 所有屏障都插入在 volatile 读之前
- C. volatile 有序性靠 CPU 自动完成无需屏障
- D. 理解 JMM 时用屏障模型推演可见性
**答案：D**
**解析：** 推荐实践：理解 JMM 时用屏障模型推演可见性。事实依据：volatile 的有序性靠编译器在读写前后插入内存屏障实现。

**Qconcurrency-1024（场景判断·内存语义）** 推荐实践：理解 JMM 时用屏障模型推演可见性
**答案：对。** 解析：volatile 的有序性靠编译器在读写前后插入内存屏障实现。原因：volatile 写之后插入 StoreLoad 屏障（最重的屏障），读之后插入 LoadLoad 与 LoadSrc 屏障，阻止跨屏障重排

**Qconcurrency-1025（填空·内存语义）** volatile 的有序性靠编译器在读写前后插入______实现
**答案：内存屏障**。解析：volatile 写之后插入 StoreLoad 屏障（最重的屏障），读之后插入 LoadLoad 与 LoadSrc 屏障，阻止跨屏障重排

**Qconcurrency-1026（简答·内存语义）** 请说明「volatile」中内存屏障的机制与使用要点。
**要点（标准答案）**：① volatile 的有序性靠编译器在读写前后插入内存屏障实现；② 原理：volatile 写之后插入 StoreLoad 屏障（最重的屏障），读之后插入 LoadLoad 与 LoadSrc 屏障，阻止跨屏障重排；③ 使用要点：理解 JMM 时用屏障模型推演可见性。版本锚点：JSR-133。

**Qconcurrency-1027（单选·正向·happens-before）** 关于「JMM」的说法，正确的是？
- A. happens-before 是判断两个操作是否可见的核心规则而非时间先后
- B. happens-before 就是代码执行的先后顺序
- C. happens-before 只适用于 volatile
- D. 没有 happens-before 关系就一定看不到
**答案：A**
**解析：** happens-before 是判断两个操作是否可见的核心规则而非时间先后。原因：A happens-before B 意味着 A 的结果对 B 可见；程序顺序规则、锁的解锁加锁、volatile 写读、线程 start 与 join 都天然构成 happens-before。
**来源：** JC-004 · JMM（JLS 17.4.5）

**Qconcurrency-1028（判断·happens-before）** happens-before 是判断两个操作是否可见的核心规则而非时间先后
**答案：对。** 解析：A happens-before B 意味着 A 的结果对 B 可见；程序顺序规则、锁的解锁加锁、volatile 写读、线程 start 与 join 都天然构成 happens-before

**Qconcurrency-1029（判断·happens-before）** happens-before 就是代码执行的先后顺序
**答案：错。** 正确表述：happens-before 是判断两个操作是否可见的核心规则而非时间先后。原因：A happens-before B 意味着 A 的结果对 B 可见；程序顺序规则、锁的解锁加锁、volatile 写读、线程 start 与 join 都天然构成 happens-before

**Qconcurrency-1030（判断·happens-before）** 没有 happens-before 关系就一定看不到
**答案：错。** 正确表述：happens-before 是判断两个操作是否可见的核心规则而非时间先后。原因：A happens-before B 意味着 A 的结果对 B 可见；程序顺序规则、锁的解锁加锁、volatile 写读、线程 start 与 join 都天然构成 happens-before

**Qconcurrency-1031（判断·happens-before）** happens-before 只适用于 volatile
**答案：错。** 正确表述：happens-before 是判断两个操作是否可见的核心规则而非时间先后。原因：A happens-before B 意味着 A 的结果对 B 可见；程序顺序规则、锁的解锁加锁、volatile 写读、线程 start 与 join 都天然构成 happens-before

**Qconcurrency-1032（场景单选·happens-before）** 在工程实践中关于「happens-before」，下列做法符合推荐实践的是？
- A. 没有 happens-before 关系就一定看不到
- B. 并发正确性论证一律用 happens-before 推导
- C. happens-before 只适用于 volatile
- D. happens-before 就是代码执行的先后顺序
**答案：B**
**解析：** 推荐实践：并发正确性论证一律用 happens-before 推导。事实依据：happens-before 是判断两个操作是否可见的核心规则而非时间先后。

**Qconcurrency-1033（场景判断·happens-before）** 推荐实践：并发正确性论证一律用 happens-before 推导
**答案：对。** 解析：happens-before 是判断两个操作是否可见的核心规则而非时间先后。原因：A happens-before B 意味着 A 的结果对 B 可见；程序顺序规则、锁的解锁加锁、volatile 写读、线程 start 与 join 都天然构成 happens-before

**Qconcurrency-1034（填空·happens-before）** ______ 是判断两个操作是否可见的核心规则而非时间先后
**答案：happens-before**。解析：A happens-before B 意味着 A 的结果对 B 可见；程序顺序规则、锁的解锁加锁、volatile 写读、线程 start 与 join 都天然构成 happens-before

**Qconcurrency-1035（简答·happens-before）** 请说明「JMM」中happens-before的机制与使用要点。
**要点（标准答案）**：① happens-before 是判断两个操作是否可见的核心规则而非时间先后；② 原理：A happens-before B 意味着 A 的结果对 B 可见；程序顺序规则、锁的解锁加锁、volatile 写读、线程 start 与 join 都天然构成 happens-before；③ 使用要点：并发正确性论证一律用 happens-before 推导。版本锚点：JLS 17.4.5。

**Qconcurrency-1036（单选·正向·happens-before）** 关于「JMM」的说法，正确的是？
- A. 只在单线程内有传递性
- B. 传递性在 JMM 中不成立
- C. happens-before 具有传递性可串起长链推理
- D. 传递性需要显式声明才生效
**答案：C**
**解析：** happens-before 具有传递性可串起长链推理。原因：volatile 写 hb 后续读、写 hb 前面的程序顺序操作，链式推导可证明跨线程可见性，这是判断数据竞争的根本工具。
**来源：** JC-005 · JMM（JLS 17.4.5）

**Qconcurrency-1037（判断·happens-before）** happens-before 具有传递性可串起长链推理
**答案：对。** 解析：volatile 写 hb 后续读、写 hb 前面的程序顺序操作，链式推导可证明跨线程可见性，这是判断数据竞争的根本工具

**Qconcurrency-1038（判断·happens-before）** 传递性在 JMM 中不成立
**答案：错。** 正确表述：happens-before 具有传递性可串起长链推理。原因：volatile 写 hb 后续读、写 hb 前面的程序顺序操作，链式推导可证明跨线程可见性，这是判断数据竞争的根本工具

**Qconcurrency-1039（判断·happens-before）** 只在单线程内有传递性
**答案：错。** 正确表述：happens-before 具有传递性可串起长链推理。原因：volatile 写 hb 后续读、写 hb 前面的程序顺序操作，链式推导可证明跨线程可见性，这是判断数据竞争的根本工具

**Qconcurrency-1040（判断·happens-before）** 传递性需要显式声明才生效
**答案：错。** 正确表述：happens-before 具有传递性可串起长链推理。原因：volatile 写 hb 后续读、写 hb 前面的程序顺序操作，链式推导可证明跨线程可见性，这是判断数据竞争的根本工具

**Qconcurrency-1041（场景单选·happens-before）** 在工程实践中关于「传递性」，下列做法符合推荐实践的是？
- A. 传递性需要显式声明才生效
- B. 只在单线程内有传递性
- C. 复杂可见性 bug 复盘时按链推导
- D. 传递性在 JMM 中不成立
**答案：C**
**解析：** 推荐实践：复杂可见性 bug 复盘时按链推导。事实依据：happens-before 具有传递性可串起长链推理。

**Qconcurrency-1042（场景判断·happens-before）** 推荐实践：复杂可见性 bug 复盘时按链推导
**答案：对。** 解析：happens-before 具有传递性可串起长链推理。原因：volatile 写 hb 后续读、写 hb 前面的程序顺序操作，链式推导可证明跨线程可见性，这是判断数据竞争的根本工具

**Qconcurrency-1043（填空·happens-before）** happens-before 具有______可串起长链推理
**答案：传递性**。解析：volatile 写 hb 后续读、写 hb 前面的程序顺序操作，链式推导可证明跨线程可见性，这是判断数据竞争的根本工具

**Qconcurrency-1044（简答·happens-before）** 请说明「JMM」中传递性的机制与使用要点。
**要点（标准答案）**：① happens-before 具有传递性可串起长链推理；② 原理：volatile 写 hb 后续读、写 hb 前面的程序顺序操作，链式推导可证明跨线程可见性，这是判断数据竞争的根本工具；③ 使用要点：复杂可见性 bug 复盘时按链推导。版本锚点：JLS 17.4.5。

**Qconcurrency-1045（单选·正向·锁机制）** 关于「synchronized」的说法，正确的是？
- A. synchronized 是 JVM 层完全独立于对象头的机制
- B. monitorenter 是 Java 方法字节码
- C. synchronized 基于对象头的 monitor 机制实现互斥与可见性
- D. synchronized 只保证互斥不保证可见性
**答案：C**
**解析：** synchronized 基于对象头的 monitor 机制实现互斥与可见性。原因：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应。
**来源：** JC-006 · synchronized（JLS 17.x）

**Qconcurrency-1046（判断·锁机制）** synchronized 基于对象头的 monitor 机制实现互斥与可见性
**答案：对。** 解析：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应

**Qconcurrency-1047（判断·锁机制）** synchronized 只保证互斥不保证可见性
**答案：错。** 正确表述：synchronized 基于对象头的 monitor 机制实现互斥与可见性。原因：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应

**Qconcurrency-1048（判断·锁机制）** synchronized 是 JVM 层完全独立于对象头的机制
**答案：错。** 正确表述：synchronized 基于对象头的 monitor 机制实现互斥与可见性。原因：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应

**Qconcurrency-1049（判断·锁机制）** monitorenter 是 Java 方法字节码
**答案：错。** 正确表述：synchronized 基于对象头的 monitor 机制实现互斥与可见性。原因：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应

**Qconcurrency-1050（场景单选·锁机制）** 在工程实践中关于「monitor」，下列做法符合推荐实践的是？
- A. monitorenter 是 Java 方法字节码
- B. synchronized 是 JVM 层完全独立于对象头的机制
- C. 互斥与可见性需求同时存在时首选 synchronized
- D. synchronized 只保证互斥不保证可见性
**答案：C**
**解析：** 推荐实践：互斥与可见性需求同时存在时首选 synchronized。事实依据：synchronized 基于对象头的 monitor 机制实现互斥与可见性。

**Qconcurrency-1051（场景判断·锁机制）** 推荐实践：互斥与可见性需求同时存在时首选 synchronized
**答案：对。** 解析：synchronized 基于对象头的 monitor 机制实现互斥与可见性。原因：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应

**Qconcurrency-1052（填空·锁机制）** synchronized 基于对象头的 ______ 机制实现互斥与可见性
**答案：monitor**。解析：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应

**Qconcurrency-1053（简答·锁机制）** 请说明「synchronized」中monitor的机制与使用要点。
**要点（标准答案）**：① synchronized 基于对象头的 monitor 机制实现互斥与可见性；② 原理：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应；③ 使用要点：互斥与可见性需求同时存在时首选 synchronized。版本锚点：JLS 17.x。

**Qconcurrency-1054（单选·正向·可重入）** 关于「synchronized」的说法，正确的是？
- A. 可重入是指可以同时被多个线程持有
- B. 子类同步方法调用父类同步方法会死锁
- C. synchronized 不可重入
- D. synchronized 是可重入锁同一线程可重复获取同一把锁
**答案：D**
**解析：** synchronized 是可重入锁同一线程可重复获取同一把锁。原因：monitor 内部维护持有线程与重入计数，嵌套同步块不会自死锁。
**来源：** JC-007 · synchronized（HotSpot 实现细节）

**Qconcurrency-1055（判断·可重入）** synchronized 是可重入锁同一线程可重复获取同一把锁
**答案：对。** 解析：monitor 内部维护持有线程与重入计数，嵌套同步块不会自死锁

**Qconcurrency-1056（判断·可重入）** synchronized 不可重入
**答案：错。** 正确表述：synchronized 是可重入锁同一线程可重复获取同一把锁。原因：monitor 内部维护持有线程与重入计数，嵌套同步块不会自死锁

**Qconcurrency-1057（判断·可重入）** 可重入是指可以同时被多个线程持有
**答案：错。** 正确表述：synchronized 是可重入锁同一线程可重复获取同一把锁。原因：monitor 内部维护持有线程与重入计数，嵌套同步块不会自死锁

**Qconcurrency-1058（判断·可重入）** 子类同步方法调用父类同步方法会死锁
**答案：错。** 正确表述：synchronized 是可重入锁同一线程可重复获取同一把锁。原因：monitor 内部维护持有线程与重入计数，嵌套同步块不会自死锁

**Qconcurrency-1059（场景单选·可重入）** 在工程实践中关于「可重入」，下列做法符合推荐实践的是？
- A. 子类同步方法调用父类同步方法会死锁
- B. synchronized 不可重入
- C. 可重入是指可以同时被多个线程持有
- D. 同步方法间相互调用无需担心自锁
**答案：D**
**解析：** 推荐实践：同步方法间相互调用无需担心自锁。事实依据：synchronized 是可重入锁同一线程可重复获取同一把锁。

**Qconcurrency-1060（场景判断·可重入）** 推荐实践：同步方法间相互调用无需担心自锁
**答案：对。** 解析：synchronized 是可重入锁同一线程可重复获取同一把锁。原因：monitor 内部维护持有线程与重入计数，嵌套同步块不会自死锁

**Qconcurrency-1061（填空·可重入）** synchronized 是______锁同一线程可重复获取同一把锁
**答案：可重入**。解析：monitor 内部维护持有线程与重入计数，嵌套同步块不会自死锁

**Qconcurrency-1062（简答·可重入）** 请说明「synchronized」中可重入的机制与使用要点。
**要点（标准答案）**：① synchronized 是可重入锁同一线程可重复获取同一把锁；② 原理：monitor 内部维护持有线程与重入计数，嵌套同步块不会自死锁；③ 使用要点：同步方法间相互调用无需担心自锁。版本锚点：HotSpot 实现细节。

**Qconcurrency-1063（单选·正向·锁机制）** 关于「synchronized」的说法，正确的是？
- A. Class 锁可以保护实例字段
- B. static synchronized 方法锁的是 Class 对象与实例锁互不冲突
- C. 静态锁比实例锁性能更差
- D. static synchronized 与实例方法锁同一把锁
**答案：B**
**解析：** static synchronized 方法锁的是 Class 对象与实例锁互不冲突。原因：类的所有实例共享同一把 Class 锁，静态与实例同步方法可并发执行。
**来源：** JC-008 · synchronized（JLS 8.4.3.6）

**Qconcurrency-1064（判断·锁机制）** static synchronized 方法锁的是 Class 对象与实例锁互不冲突
**答案：对。** 解析：类的所有实例共享同一把 Class 锁，静态与实例同步方法可并发执行

**Qconcurrency-1065（判断·锁机制）** static synchronized 与实例方法锁同一把锁
**答案：错。** 正确表述：static synchronized 方法锁的是 Class 对象与实例锁互不冲突。原因：类的所有实例共享同一把 Class 锁，静态与实例同步方法可并发执行

**Qconcurrency-1066（判断·锁机制）** Class 锁可以保护实例字段
**答案：错。** 正确表述：static synchronized 方法锁的是 Class 对象与实例锁互不冲突。原因：类的所有实例共享同一把 Class 锁，静态与实例同步方法可并发执行

**Qconcurrency-1067（判断·锁机制）** 静态锁比实例锁性能更差
**答案：错。** 正确表述：static synchronized 方法锁的是 Class 对象与实例锁互不冲突。原因：类的所有实例共享同一把 Class 锁，静态与实例同步方法可并发执行

**Qconcurrency-1068（场景单选·锁机制）** 在工程实践中关于「Class 对象」，下列做法符合推荐实践的是？
- A. 静态锁比实例锁性能更差
- B. Class 锁可以保护实例字段
- C. 保护静态状态用 Class 锁或专用锁对象
- D. static synchronized 与实例方法锁同一把锁
**答案：C**
**解析：** 推荐实践：保护静态状态用 Class 锁或专用锁对象。事实依据：static synchronized 方法锁的是 Class 对象与实例锁互不冲突。

**Qconcurrency-1069（场景判断·锁机制）** 推荐实践：保护静态状态用 Class 锁或专用锁对象
**答案：对。** 解析：static synchronized 方法锁的是 Class 对象与实例锁互不冲突。原因：类的所有实例共享同一把 Class 锁，静态与实例同步方法可并发执行

**Qconcurrency-1070（填空·锁机制）** static synchronized 方法锁的是 ______与实例锁互不冲突
**答案：Class 对象**。解析：类的所有实例共享同一把 Class 锁，静态与实例同步方法可并发执行

**Qconcurrency-1071（简答·锁机制）** 请说明「synchronized」中Class 对象的机制与使用要点。
**要点（标准答案）**：① static synchronized 方法锁的是 Class 对象与实例锁互不冲突；② 原理：类的所有实例共享同一把 Class 锁，静态与实例同步方法可并发执行；③ 使用要点：保护静态状态用 Class 锁或专用锁对象。版本锚点：JLS 8.4.3.6。

**Qconcurrency-1072（单选·正向·协作机制）** 关于「wait/notify」的说法，正确的是？
- A. 任何线程都可以对任意对象调用 wait
- B. 在 synchronized 块外调用 wait 只是无效不报错
- C. notify 与 wait 可以不加锁配对使用
- D. wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException
**答案：D**
**解析：** wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException。原因：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常。
**来源：** JC-009 · wait/notify（JLS 17.2）

**Qconcurrency-1073（判断·协作机制）** wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException
**答案：对。** 解析：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常

**Qconcurrency-1074（判断·协作机制）** 任何线程都可以对任意对象调用 wait
**答案：错。** 正确表述：wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException。原因：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常

**Qconcurrency-1075（判断·协作机制）** 在 synchronized 块外调用 wait 只是无效不报错
**答案：错。** 正确表述：wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException。原因：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常

**Qconcurrency-1076（判断·协作机制）** notify 与 wait 可以不加锁配对使用
**答案：错。** 正确表述：wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException。原因：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常

**Qconcurrency-1077（场景单选·协作机制）** 在工程实践中关于「IllegalMonitorStateException」，下列做法符合推荐实践的是？
- A. 永远在 synchronized(obj) 内配对使用 wait 与 notify
- B. notify 与 wait 可以不加锁配对使用
- C. 在 synchronized 块外调用 wait 只是无效不报错
- D. 任何线程都可以对任意对象调用 wait
**答案：A**
**解析：** 推荐实践：永远在 synchronized(obj) 内配对使用 wait 与 notify。事实依据：wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException。

**Qconcurrency-1078（场景判断·协作机制）** 推荐实践：永远在 synchronized(obj) 内配对使用 wait 与 notify
**答案：对。** 解析：wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException。原因：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常

**Qconcurrency-1079（填空·协作机制）** wait 与 notify 必须在持有对象 monitor 时调用否则抛 ______
**答案：IllegalMonitorStateException**。解析：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常

**Qconcurrency-1080（简答·协作机制）** 请说明「wait/notify」中IllegalMonitorStateException的机制与使用要点。
**要点（标准答案）**：① wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException；② 原理：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常；③ 使用要点：永远在 synchronized(obj) 内配对使用 wait 与 notify。版本锚点：JLS 17.2。

**Qconcurrency-1081（单选·正向·锁行为）** 关于「wait/notify」的说法，正确的是？
- A. sleep 也会释放锁
- B. wait 不释放锁只是等待
- C. 两者释放锁的行为取决于 JVM 实现
- D. wait 会释放当前持有的 monitor 而 Thread.sleep 不会释放任何锁
**答案：D**
**解析：** wait 会释放当前持有的 monitor 而 Thread.sleep 不会释放任何锁。原因：sleep 只是定时暂停，锁所有权不变，持锁 sleep 会拖死其他线程。
**来源：** JC-010 · wait/notify（JLS 17.2）

**Qconcurrency-1082（判断·锁行为）** wait 会释放当前持有的 monitor 而 Thread.sleep 不会释放任何锁
**答案：对。** 解析：sleep 只是定时暂停，锁所有权不变，持锁 sleep 会拖死其他线程

**Qconcurrency-1083（判断·锁行为）** sleep 也会释放锁
**答案：错。** 正确表述：wait 会释放当前持有的 monitor 而 Thread.sleep 不会释放任何锁。原因：sleep 只是定时暂停，锁所有权不变，持锁 sleep 会拖死其他线程

**Qconcurrency-1084（判断·锁行为）** wait 不释放锁只是等待
**答案：错。** 正确表述：wait 会释放当前持有的 monitor 而 Thread.sleep 不会释放任何锁。原因：sleep 只是定时暂停，锁所有权不变，持锁 sleep 会拖死其他线程

**Qconcurrency-1085（判断·锁行为）** 两者释放锁的行为取决于 JVM 实现
**答案：错。** 正确表述：wait 会释放当前持有的 monitor 而 Thread.sleep 不会释放任何锁。原因：sleep 只是定时暂停，锁所有权不变，持锁 sleep 会拖死其他线程

**Qconcurrency-1086（场景单选·锁行为）** 在工程实践中关于「释放锁」，下列做法符合推荐实践的是？
- A. 两者释放锁的行为取决于 JVM 实现
- B. sleep 也会释放锁
- C. 需要短暂暂停且持有锁时绝不使用 sleep
- D. wait 不释放锁只是等待
**答案：C**
**解析：** 推荐实践：需要短暂暂停且持有锁时绝不使用 sleep。事实依据：wait 会释放当前持有的 monitor 而 Thread.sleep 不会释放任何锁。

**Qconcurrency-1087（场景判断·锁行为）** 推荐实践：需要短暂暂停且持有锁时绝不使用 sleep
**答案：对。** 解析：wait 会释放当前持有的 monitor 而 Thread.sleep 不会释放任何锁。原因：sleep 只是定时暂停，锁所有权不变，持锁 sleep 会拖死其他线程

**Qconcurrency-1088（简答·锁行为）** 请说明「wait/notify」中释放锁的机制与使用要点。
**要点（标准答案）**：① wait 会释放当前持有的 monitor 而 Thread.sleep 不会释放任何锁；② 原理：sleep 只是定时暂停，锁所有权不变，持锁 sleep 会拖死其他线程；③ 使用要点：需要短暂暂停且持有锁时绝不使用 sleep。版本锚点：JLS 17.2。

**Qconcurrency-1089（单选·正向·误用）** 关于「wait/notify」的说法，正确的是？
- A. 虚假唤醒是 Myth 实际不存在
- B. 等待条件必须用 while 循环判断而不能用 if 以防虚假唤醒
- C. if 与 while 在等待条件时等价
- D. 虚假唤醒只发生在 Linux 平台
**答案：B**
**解析：** 等待条件必须用 while 循环判断而不能用 if 以防虚假唤醒。原因：OS 或 notifyAll 唤醒后条件可能已被其他线程消费，while 在唤醒后重新检查条件，JLS 明确允许虚假唤醒存在。
**来源：** JC-011 · wait/notify（JLS 17.2.3）

**Qconcurrency-1090（判断·误用）** 等待条件必须用 while 循环判断而不能用 if 以防虚假唤醒
**答案：对。** 解析：OS 或 notifyAll 唤醒后条件可能已被其他线程消费，while 在唤醒后重新检查条件，JLS 明确允许虚假唤醒存在

**Qconcurrency-1091（判断·误用）** 虚假唤醒是 Myth 实际不存在
**答案：错。** 正确表述：等待条件必须用 while 循环判断而不能用 if 以防虚假唤醒。原因：OS 或 notifyAll 唤醒后条件可能已被其他线程消费，while 在唤醒后重新检查条件，JLS 明确允许虚假唤醒存在

**Qconcurrency-1092（判断·误用）** if 与 while 在等待条件时等价
**答案：错。** 正确表述：等待条件必须用 while 循环判断而不能用 if 以防虚假唤醒。原因：OS 或 notifyAll 唤醒后条件可能已被其他线程消费，while 在唤醒后重新检查条件，JLS 明确允许虚假唤醒存在

**Qconcurrency-1093（判断·误用）** 虚假唤醒只发生在 Linux 平台
**答案：错。** 正确表述：等待条件必须用 while 循环判断而不能用 if 以防虚假唤醒。原因：OS 或 notifyAll 唤醒后条件可能已被其他线程消费，while 在唤醒后重新检查条件，JLS 明确允许虚假唤醒存在

**Qconcurrency-1094（场景单选·误用）** 在工程实践中关于「虚假唤醒」，下列做法符合推荐实践的是？
- A. 虚假唤醒是 Myth 实际不存在
- B. if 与 while 在等待条件时等价
- C. 虚假唤醒只发生在 Linux 平台
- D. 所有条件等待统一写 while(条件不满足) wait
**答案：D**
**解析：** 推荐实践：所有条件等待统一写 while(条件不满足) wait。事实依据：等待条件必须用 while 循环判断而不能用 if 以防虚假唤醒。

**Qconcurrency-1095（场景判断·误用）** 推荐实践：所有条件等待统一写 while(条件不满足) wait
**答案：对。** 解析：等待条件必须用 while 循环判断而不能用 if 以防虚假唤醒。原因：OS 或 notifyAll 唤醒后条件可能已被其他线程消费，while 在唤醒后重新检查条件，JLS 明确允许虚假唤醒存在

**Qconcurrency-1096（填空·误用）** 等待条件必须用 while 循环判断而不能用 if 以防______
**答案：虚假唤醒**。解析：OS 或 notifyAll 唤醒后条件可能已被其他线程消费，while 在唤醒后重新检查条件，JLS 明确允许虚假唤醒存在

**Qconcurrency-1097（简答·误用）** 请说明「wait/notify」中虚假唤醒的机制与使用要点。
**要点（标准答案）**：① 等待条件必须用 while 循环判断而不能用 if 以防虚假唤醒；② 原理：OS 或 notifyAll 唤醒后条件可能已被其他线程消费，while 在唤醒后重新检查条件，JLS 明确允许虚假唤醒存在；③ 使用要点：所有条件等待统一写 while(条件不满足) wait。版本锚点：JLS 17.2.3。

**Qconcurrency-1098（单选·正向·协作机制）** 关于「wait/notify」的说法，正确的是？
- A. notify 保证唤醒的是等待最久的线程
- B. notify 只随机唤醒一个等待线程无法指定目标
- C. notify 会唤醒所有等待线程
- D. notify 比 notifyAll 在任何场景都更快
**答案：B**
**解析：** notify 只随机唤醒一个等待线程无法指定目标。原因：多个线程等待不同条件时可能唤醒错误的线程导致所有线程永久等待，多条件场景必须 notifyAll。
**来源：** JC-012 · wait/notify（实战经验）

**Qconcurrency-1099（判断·协作机制）** notify 只随机唤醒一个等待线程无法指定目标
**答案：对。** 解析：多个线程等待不同条件时可能唤醒错误的线程导致所有线程永久等待，多条件场景必须 notifyAll

**Qconcurrency-1100（判断·协作机制）** notify 会唤醒所有等待线程
**答案：错。** 正确表述：notify 只随机唤醒一个等待线程无法指定目标。原因：多个线程等待不同条件时可能唤醒错误的线程导致所有线程永久等待，多条件场景必须 notifyAll

**Qconcurrency-1101（判断·协作机制）** notify 保证唤醒的是等待最久的线程
**答案：错。** 正确表述：notify 只随机唤醒一个等待线程无法指定目标。原因：多个线程等待不同条件时可能唤醒错误的线程导致所有线程永久等待，多条件场景必须 notifyAll

**Qconcurrency-1102（判断·协作机制）** notify 比 notifyAll 在任何场景都更快
**答案：错。** 正确表述：notify 只随机唤醒一个等待线程无法指定目标。原因：多个线程等待不同条件时可能唤醒错误的线程导致所有线程永久等待，多条件场景必须 notifyAll

**Qconcurrency-1103（场景单选·协作机制）** 在工程实践中关于「notifyAll」，下列做法符合推荐实践的是？
- A. notify 保证唤醒的是等待最久的线程
- B. 多条件共用一个锁对象时用 notifyAll 或拆分锁
- C. notify 比 notifyAll 在任何场景都更快
- D. notify 会唤醒所有等待线程
**答案：B**
**解析：** 推荐实践：多条件共用一个锁对象时用 notifyAll 或拆分锁。事实依据：notify 只随机唤醒一个等待线程无法指定目标。

**Qconcurrency-1104（场景判断·协作机制）** 推荐实践：多条件共用一个锁对象时用 notifyAll 或拆分锁
**答案：对。** 解析：notify 只随机唤醒一个等待线程无法指定目标。原因：多个线程等待不同条件时可能唤醒错误的线程导致所有线程永久等待，多条件场景必须 notifyAll

**Qconcurrency-1105（简答·协作机制）** 请说明「wait/notify」中notifyAll的机制与使用要点。
**要点（标准答案）**：① notify 只随机唤醒一个等待线程无法指定目标；② 原理：多个线程等待不同条件时可能唤醒错误的线程导致所有线程永久等待，多条件场景必须 notifyAll；③ 使用要点：多条件共用一个锁对象时用 notifyAll 或拆分锁。版本锚点：实战经验。

**Qconcurrency-1106（单选·正向·锁升级）** 关于「synchronized」的说法，正确的是？
- A. 偏向锁被移除是因为有 bug
- B. 锁升级路径仍从偏向锁开始
- C. 偏向锁已在 JDK15 标记废弃并于 JDK21 彻底移除
- D. JDK21 仍支持偏向锁
**答案：C**
**解析：** 偏向锁已在 JDK15 标记废弃并于 JDK21 彻底移除。原因：现代应用中撤销偏向锁的昂的操作超过收益，JDK21 中 -XX:+UseBiasedLocking 直接报 Unrecognized VM option（本机 JDK 21.0.2 实测）。
**来源：** JC-013 · synchronized（JEP 369 与 JDK21）

**Qconcurrency-1107（判断·锁升级）** 偏向锁已在 JDK15 标记废弃并于 JDK21 彻底移除
**答案：对。** 解析：现代应用中撤销偏向锁的昂的操作超过收益，JDK21 中 -XX:+UseBiasedLocking 直接报 Unrecognized VM option（本机 JDK 21.0.2 实测）

**Qconcurrency-1108（判断·锁升级）** JDK21 仍支持偏向锁
**答案：错。** 正确表述：偏向锁已在 JDK15 标记废弃并于 JDK21 彻底移除。原因：现代应用中撤销偏向锁的昂的操作超过收益，JDK21 中 -XX:+UseBiasedLocking 直接报 Unrecognized VM option（本机 JDK 21.0.2 实测）

**Qconcurrency-1109（判断·锁升级）** 偏向锁被移除是因为有 bug
**答案：错。** 正确表述：偏向锁已在 JDK15 标记废弃并于 JDK21 彻底移除。原因：现代应用中撤销偏向锁的昂的操作超过收益，JDK21 中 -XX:+UseBiasedLocking 直接报 Unrecognized VM option（本机 JDK 21.0.2 实测）

**Qconcurrency-1110（判断·锁升级）** 锁升级路径仍从偏向锁开始
**答案：错。** 正确表述：偏向锁已在 JDK15 标记废弃并于 JDK21 彻底移除。原因：现代应用中撤销偏向锁的昂的操作超过收益，JDK21 中 -XX:+UseBiasedLocking 直接报 Unrecognized VM option（本机 JDK 21.0.2 实测）

**Qconcurrency-1111（场景单选·锁升级）** 在工程实践中关于「偏向锁」，下列做法符合推荐实践的是？
- A. JDK21 仍支持偏向锁
- B. 描述锁升级时按当前 JDK 说无锁到轻量级到重量级
- C. 偏向锁被移除是因为有 bug
- D. 锁升级路径仍从偏向锁开始
**答案：B**
**解析：** 推荐实践：描述锁升级时按当前 JDK 说无锁到轻量级到重量级。事实依据：偏向锁已在 JDK15 标记废弃并于 JDK21 彻底移除。

**Qconcurrency-1112（场景判断·锁升级）** 推荐实践：描述锁升级时按当前 JDK 说无锁到轻量级到重量级
**答案：对。** 解析：偏向锁已在 JDK15 标记废弃并于 JDK21 彻底移除。原因：现代应用中撤销偏向锁的昂的操作超过收益，JDK21 中 -XX:+UseBiasedLocking 直接报 Unrecognized VM option（本机 JDK 21.0.2 实测）

**Qconcurrency-1113（填空·锁升级）** ______已在 JDK15 标记废弃并于 JDK21 彻底移除
**答案：偏向锁**。解析：现代应用中撤销偏向锁的昂的操作超过收益，JDK21 中 -XX:+UseBiasedLocking 直接报 Unrecognized VM option（本机 JDK 21.0.2 实测）

**Qconcurrency-1114（简答·锁升级）** 请说明「synchronized」中偏向锁的机制与使用要点。
**要点（标准答案）**：① 偏向锁已在 JDK15 标记废弃并于 JDK21 彻底移除；② 原理：现代应用中撤销偏向锁的昂的操作超过收益，JDK21 中 -XX:+UseBiasedLocking 直接报 Unrecognized VM option（本机 JDK 21.0.2 实测）；③ 使用要点：描述锁升级时按当前 JDK 说无锁到轻量级到重量级。版本锚点：JEP 369 与 JDK21。

**Qconcurrency-1115（单选·正向·锁升级）** 关于「synchronized」的说法，正确的是？
- A. 无竞争时 synchronized 通过 CAS 获取轻量级锁避免重量级开销
- B. 轻量级锁靠自旋等待获取
- C. 锁一旦膨胀就永久无法降级
- D. 重量级锁不涉及系统调用
**答案：A**
**解析：** 无竞争时 synchronized 通过 CAS 获取轻量级锁避免重量级开销。原因：轻量级锁在栈帧建立 Lock Record 并 CAS 替换对象头 Mark Word，失败则膨胀为重量级（OS mutex，涉及用户态内核态切换）。
**来源：** JC-014 · synchronized（HotSpot 内部机制）

**Qconcurrency-1116（判断·锁升级）** 无竞争时 synchronized 通过 CAS 获取轻量级锁避免重量级开销
**答案：对。** 解析：轻量级锁在栈帧建立 Lock Record 并 CAS 替换对象头 Mark Word，失败则膨胀为重量级（OS mutex，涉及用户态内核态切换）

**Qconcurrency-1117（判断·锁升级）** 轻量级锁靠自旋等待获取
**答案：错。** 正确表述：无竞争时 synchronized 通过 CAS 获取轻量级锁避免重量级开销。原因：轻量级锁在栈帧建立 Lock Record 并 CAS 替换对象头 Mark Word，失败则膨胀为重量级（OS mutex，涉及用户态内核态切换）

**Qconcurrency-1118（判断·锁升级）** 重量级锁不涉及系统调用
**答案：错。** 正确表述：无竞争时 synchronized 通过 CAS 获取轻量级锁避免重量级开销。原因：轻量级锁在栈帧建立 Lock Record 并 CAS 替换对象头 Mark Word，失败则膨胀为重量级（OS mutex，涉及用户态内核态切换）

**Qconcurrency-1119（判断·锁升级）** 锁一旦膨胀就永久无法降级
**答案：错。** 正确表述：无竞争时 synchronized 通过 CAS 获取轻量级锁避免重量级开销。原因：轻量级锁在栈帧建立 Lock Record 并 CAS 替换对象头 Mark Word，失败则膨胀为重量级（OS mutex，涉及用户态内核态切换）

**Qconcurrency-1120（场景单选·锁升级）** 在工程实践中关于「轻量级锁」，下列做法符合推荐实践的是？
- A. 轻量级锁靠自旋等待获取
- B. 低竞争短临界区用 synchronized 性能很好
- C. 锁一旦膨胀就永久无法降级
- D. 重量级锁不涉及系统调用
**答案：B**
**解析：** 推荐实践：低竞争短临界区用 synchronized 性能很好。事实依据：无竞争时 synchronized 通过 CAS 获取轻量级锁避免重量级开销。

**Qconcurrency-1121（场景判断·锁升级）** 推荐实践：低竞争短临界区用 synchronized 性能很好
**答案：对。** 解析：无竞争时 synchronized 通过 CAS 获取轻量级锁避免重量级开销。原因：轻量级锁在栈帧建立 Lock Record 并 CAS 替换对象头 Mark Word，失败则膨胀为重量级（OS mutex，涉及用户态内核态切换）

**Qconcurrency-1122（填空·锁升级）** 无竞争时 synchronized 通过 CAS 获取______避免重量级开销
**答案：轻量级锁**。解析：轻量级锁在栈帧建立 Lock Record 并 CAS 替换对象头 Mark Word，失败则膨胀为重量级（OS mutex，涉及用户态内核态切换）

**Qconcurrency-1123（简答·锁升级）** 请说明「synchronized」中轻量级锁的机制与使用要点。
**要点（标准答案）**：① 无竞争时 synchronized 通过 CAS 获取轻量级锁避免重量级开销；② 原理：轻量级锁在栈帧建立 Lock Record 并 CAS 替换对象头 Mark Word，失败则膨胀为重量级（OS mutex，涉及用户态内核态切换）；③ 使用要点：低竞争短临界区用 synchronized 性能很好。版本锚点：HotSpot 内部机制。

**Qconcurrency-1124（单选·正向·安全发布）** 关于「单例模式」的说法，正确的是？
- A. DCL 问题是性能问题不影响正确性
- B. DCL 只要有 synchronized 就不需要 volatile
- C. 静态工厂方法天然线程安全无需 volatile
- D. 双重检查锁单例的实例字段必须声明为 volatile
**答案：D**
**解析：** 双重检查锁单例的实例字段必须声明为 volatile。原因：new 对象包含分配、构造、赋引用三步可能被重排，其他线程可能拿到未初始化完成的引用，volatile 禁止该重排。
**来源：** JC-015 · 单例模式（JSR-133 案例）

**Qconcurrency-1125（判断·安全发布）** 双重检查锁单例的实例字段必须声明为 volatile
**答案：对。** 解析：new 对象包含分配、构造、赋引用三步可能被重排，其他线程可能拿到未初始化完成的引用，volatile 禁止该重排

**Qconcurrency-1126（判断·安全发布）** DCL 只要有 synchronized 就不需要 volatile
**答案：错。** 正确表述：双重检查锁单例的实例字段必须声明为 volatile。原因：new 对象包含分配、构造、赋引用三步可能被重排，其他线程可能拿到未初始化完成的引用，volatile 禁止该重排

**Qconcurrency-1127（判断·安全发布）** DCL 问题是性能问题不影响正确性
**答案：错。** 正确表述：双重检查锁单例的实例字段必须声明为 volatile。原因：new 对象包含分配、构造、赋引用三步可能被重排，其他线程可能拿到未初始化完成的引用，volatile 禁止该重排

**Qconcurrency-1128（判断·安全发布）** 静态工厂方法天然线程安全无需 volatile
**答案：错。** 正确表述：双重检查锁单例的实例字段必须声明为 volatile。原因：new 对象包含分配、构造、赋引用三步可能被重排，其他线程可能拿到未初始化完成的引用，volatile 禁止该重排

**Qconcurrency-1129（场景单选·安全发布）** 在工程实践中关于「双重检查锁」，下列做法符合推荐实践的是？
- A. DCL 问题是性能问题不影响正确性
- B. 静态工厂方法天然线程安全无需 volatile
- C. DCL 只要有 synchronized 就不需要 volatile
- D. 懒加载单例标准写法：volatile + 双重检查
**答案：D**
**解析：** 推荐实践：懒加载单例标准写法：volatile + 双重检查。事实依据：双重检查锁单例的实例字段必须声明为 volatile。

**Qconcurrency-1130（场景判断·安全发布）** 推荐实践：懒加载单例标准写法：volatile + 双重检查
**答案：对。** 解析：双重检查锁单例的实例字段必须声明为 volatile。原因：new 对象包含分配、构造、赋引用三步可能被重排，其他线程可能拿到未初始化完成的引用，volatile 禁止该重排

**Qconcurrency-1131（填空·安全发布）** ______单例的实例字段必须声明为 volatile
**答案：双重检查锁**。解析：new 对象包含分配、构造、赋引用三步可能被重排，其他线程可能拿到未初始化完成的引用，volatile 禁止该重排

**Qconcurrency-1132（简答·安全发布）** 请说明「单例模式」中双重检查锁的机制与使用要点。
**要点（标准答案）**：① 双重检查锁单例的实例字段必须声明为 volatile；② 原理：new 对象包含分配、构造、赋引用三步可能被重排，其他线程可能拿到未初始化完成的引用，volatile 禁止该重排；③ 使用要点：懒加载单例标准写法：volatile + 双重检查。版本锚点：JSR-133 案例。

**Qconcurrency-1133（单选·正向·安全发布）** 关于「单例模式」的说法，正确的是？
- A. 静态内部类单例需要额外加锁
- B. Holder 方式在多线程下需要双重检查
- C. 静态内部类 Holder 单例利用类初始化锁天然线程安全且懒加载
- D. 类加载时机是 JVM 启动时全部加载
**答案：C**
**解析：** 静态内部类 Holder 单例利用类初始化锁天然线程安全且懒加载。原因：JVM 保证类初始化由锁保护且只执行一次，首次访问 Holder 类时才触发初始化。
**来源：** JC-016 · 单例模式（JLS 12.4）

**Qconcurrency-1134（判断·安全发布）** 静态内部类 Holder 单例利用类初始化锁天然线程安全且懒加载
**答案：对。** 解析：JVM 保证类初始化由锁保护且只执行一次，首次访问 Holder 类时才触发初始化

**Qconcurrency-1135（判断·安全发布）** 静态内部类单例需要额外加锁
**答案：错。** 正确表述：静态内部类 Holder 单例利用类初始化锁天然线程安全且懒加载。原因：JVM 保证类初始化由锁保护且只执行一次，首次访问 Holder 类时才触发初始化

**Qconcurrency-1136（判断·安全发布）** Holder 方式在多线程下需要双重检查
**答案：错。** 正确表述：静态内部类 Holder 单例利用类初始化锁天然线程安全且懒加载。原因：JVM 保证类初始化由锁保护且只执行一次，首次访问 Holder 类时才触发初始化

**Qconcurrency-1137（判断·安全发布）** 类加载时机是 JVM 启动时全部加载
**答案：错。** 正确表述：静态内部类 Holder 单例利用类初始化锁天然线程安全且懒加载。原因：JVM 保证类初始化由锁保护且只执行一次，首次访问 Holder 类时才触发初始化

**Qconcurrency-1138（场景单选·安全发布）** 在工程实践中关于「静态内部类」，下列做法符合推荐实践的是？
- A. 推荐的无锁懒加载单例写法
- B. 静态内部类单例需要额外加锁
- C. 类加载时机是 JVM 启动时全部加载
- D. Holder 方式在多线程下需要双重检查
**答案：A**
**解析：** 推荐实践：推荐的无锁懒加载单例写法。事实依据：静态内部类 Holder 单例利用类初始化锁天然线程安全且懒加载。

**Qconcurrency-1139（场景判断·安全发布）** 推荐实践：推荐的无锁懒加载单例写法
**答案：对。** 解析：静态内部类 Holder 单例利用类初始化锁天然线程安全且懒加载。原因：JVM 保证类初始化由锁保护且只执行一次，首次访问 Holder 类时才触发初始化

**Qconcurrency-1140（填空·安全发布）** ______ Holder 单例利用类初始化锁天然线程安全且懒加载
**答案：静态内部类**。解析：JVM 保证类初始化由锁保护且只执行一次，首次访问 Holder 类时才触发初始化

**Qconcurrency-1141（简答·安全发布）** 请说明「单例模式」中静态内部类的机制与使用要点。
**要点（标准答案）**：① 静态内部类 Holder 单例利用类初始化锁天然线程安全且懒加载；② 原理：JVM 保证类初始化由锁保护且只执行一次，首次访问 Holder 类时才触发初始化；③ 使用要点：推荐的无锁懒加载单例写法。版本锚点：JLS 12.4。

**Qconcurrency-1142（单选·正向·线程状态）** 关于「线程基础」的说法，正确的是？
- A. RUNNABLE 的线程一定在 CPU 上执行
- B. 线程状态共 5 种
- C. BLOCKED 包括等 Condition
- D. Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同
**答案：D**
**解析：** Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同。原因：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版。
**来源：** JC-017 · 线程基础（Thread.State）

**Qconcurrency-1143（判断·线程状态）** Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同
**答案：对。** 解析：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版

**Qconcurrency-1144（判断·线程状态）** RUNNABLE 的线程一定在 CPU 上执行
**答案：错。** 正确表述：Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同。原因：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版

**Qconcurrency-1145（判断·线程状态）** BLOCKED 包括等 Condition
**答案：错。** 正确表述：Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同。原因：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版

**Qconcurrency-1146（判断·线程状态）** 线程状态共 5 种
**答案：错。** 正确表述：Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同。原因：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版

**Qconcurrency-1147（场景单选·线程状态）** 在工程实践中关于「BLOCKED」，下列做法符合推荐实践的是？
- A. 线程状态共 5 种
- B. dump 分析时区分 BLOCKED 与 WAITING 定位问题
- C. RUNNABLE 的线程一定在 CPU 上执行
- D. BLOCKED 包括等 Condition
**答案：B**
**解析：** 推荐实践：dump 分析时区分 BLOCKED 与 WAITING 定位问题。事实依据：Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同。

**Qconcurrency-1148（场景判断·线程状态）** 推荐实践：dump 分析时区分 BLOCKED 与 WAITING 定位问题
**答案：对。** 解析：Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同。原因：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版

**Qconcurrency-1149（填空·线程状态）** Java 线程有 6 种状态 ______ 与 WAITING 语义不同
**答案：BLOCKED**。解析：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版

**Qconcurrency-1150（简答·线程状态）** 请说明「线程基础」中BLOCKED的机制与使用要点。
**要点（标准答案）**：① Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同；② 原理：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版；③ 使用要点：dump 分析时区分 BLOCKED 与 WAITING 定位问题。版本锚点：Thread.State。

**Qconcurrency-1151（单选·正向·中断）** 关于「线程基础」的说法，正确的是？
- A. 对运行中的线程调用 interrupt 只是设置中断标志不会真正停止
- B. interrupt 会立刻杀死线程
- C. interrupt 只对阻塞中的线程有效
- D. 循环中检查中断会降低性能
**答案：A**
**解析：** 对运行中的线程调用 interrupt 只是设置中断标志不会真正停止。原因：Java 的协作式中断：线程需要自行检查 isInterrupted 或在阻塞点抛 InterruptedException 响应。
**来源：** JC-018 · 线程基础（Thread.interrupt javadoc）

**Qconcurrency-1152（判断·中断）** 对运行中的线程调用 interrupt 只是设置中断标志不会真正停止
**答案：对。** 解析：Java 的协作式中断：线程需要自行检查 isInterrupted 或在阻塞点抛 InterruptedException 响应

**Qconcurrency-1153（判断·中断）** interrupt 会立刻杀死线程
**答案：错。** 正确表述：对运行中的线程调用 interrupt 只是设置中断标志不会真正停止。原因：Java 的协作式中断：线程需要自行检查 isInterrupted 或在阻塞点抛 InterruptedException 响应

**Qconcurrency-1154（判断·中断）** interrupt 只对阻塞中的线程有效
**答案：错。** 正确表述：对运行中的线程调用 interrupt 只是设置中断标志不会真正停止。原因：Java 的协作式中断：线程需要自行检查 isInterrupted 或在阻塞点抛 InterruptedException 响应

**Qconcurrency-1155（判断·中断）** 循环中检查中断会降低性能
**答案：错。** 正确表述：对运行中的线程调用 interrupt 只是设置中断标志不会真正停止。原因：Java 的协作式中断：线程需要自行检查 isInterrupted 或在阻塞点抛 InterruptedException 响应

**Qconcurrency-1156（场景单选·中断）** 在工程实践中关于「interrupt」，下列做法符合推荐实践的是？
- A. interrupt 会立刻杀死线程
- B. 任务循环内定期检查 Thread.currentThread().isInterrupted()
- C. 循环中检查中断会降低性能
- D. interrupt 只对阻塞中的线程有效
**答案：B**
**解析：** 推荐实践：任务循环内定期检查 Thread.currentThread().isInterrupted()。事实依据：对运行中的线程调用 interrupt 只是设置中断标志不会真正停止。

**Qconcurrency-1157（场景判断·中断）** 推荐实践：任务循环内定期检查 Thread.currentThread().isInterrupted()
**答案：对。** 解析：对运行中的线程调用 interrupt 只是设置中断标志不会真正停止。原因：Java 的协作式中断：线程需要自行检查 isInterrupted 或在阻塞点抛 InterruptedException 响应

**Qconcurrency-1158（填空·中断）** 对运行中的线程调用 ______ 只是设置中断标志不会真正停止
**答案：interrupt**。解析：Java 的协作式中断：线程需要自行检查 isInterrupted 或在阻塞点抛 InterruptedException 响应

**Qconcurrency-1159（简答·中断）** 请说明「线程基础」中interrupt的机制与使用要点。
**要点（标准答案）**：① 对运行中的线程调用 interrupt 只是设置中断标志不会真正停止；② 原理：Java 的协作式中断：线程需要自行检查 isInterrupted 或在阻塞点抛 InterruptedException 响应；③ 使用要点：任务循环内定期检查 Thread.currentThread().isInterrupted()。版本锚点：Thread.interrupt javadoc。

**Qconcurrency-1160（单选·正向·中断）** 关于「线程基础」的说法，正确的是？
- A. 中断标志自动保留无需恢复
- B. catch 后什么都不做是最安全的
- C. 捕获 InterruptedException 后必须恢复中断标志或继续向上抛
- D. InterruptedException 应转为运行时异常直接打日志了事
**答案：C**
**解析：** 捕获 InterruptedException 后必须恢复中断标志或继续向上抛。原因：异常被吞掉后中断信号丢失，上层无法再感知停止请求，这是阿里手册明确条款（恢复用 Thread.currentThread().interrupt()）。
**来源：** JC-019 · 线程基础（C1.5 手册）

**Qconcurrency-1161（判断·中断）** 捕获 InterruptedException 后必须恢复中断标志或继续向上抛
**答案：对。** 解析：异常被吞掉后中断信号丢失，上层无法再感知停止请求，这是阿里手册明确条款（恢复用 Thread.currentThread().interrupt()）

**Qconcurrency-1162（判断·中断）** catch 后什么都不做是最安全的
**答案：错。** 正确表述：捕获 InterruptedException 后必须恢复中断标志或继续向上抛。原因：异常被吞掉后中断信号丢失，上层无法再感知停止请求，这是阿里手册明确条款（恢复用 Thread.currentThread().interrupt()）

**Qconcurrency-1163（判断·中断）** InterruptedException 应转为运行时异常直接打日志了事
**答案：错。** 正确表述：捕获 InterruptedException 后必须恢复中断标志或继续向上抛。原因：异常被吞掉后中断信号丢失，上层无法再感知停止请求，这是阿里手册明确条款（恢复用 Thread.currentThread().interrupt()）

**Qconcurrency-1164（判断·中断）** 中断标志自动保留无需恢复
**答案：错。** 正确表述：捕获 InterruptedException 后必须恢复中断标志或继续向上抛。原因：异常被吞掉后中断信号丢失，上层无法再感知停止请求，这是阿里手册明确条款（恢复用 Thread.currentThread().interrupt()）

**Qconcurrency-1165（场景单选·中断）** 在工程实践中关于「InterruptedException」，下列做法符合推荐实践的是？
- A. 吞异常必须注释说明理由并恢复标志位
- B. catch 后什么都不做是最安全的
- C. InterruptedException 应转为运行时异常直接打日志了事
- D. 中断标志自动保留无需恢复
**答案：A**
**解析：** 推荐实践：吞异常必须注释说明理由并恢复标志位。事实依据：捕获 InterruptedException 后必须恢复中断标志或继续向上抛。

**Qconcurrency-1166（场景判断·中断）** 推荐实践：吞异常必须注释说明理由并恢复标志位
**答案：对。** 解析：捕获 InterruptedException 后必须恢复中断标志或继续向上抛。原因：异常被吞掉后中断信号丢失，上层无法再感知停止请求，这是阿里手册明确条款（恢复用 Thread.currentThread().interrupt()）

**Qconcurrency-1167（填空·中断）** 捕获 ______ 后必须恢复中断标志或继续向上抛
**答案：InterruptedException**。解析：异常被吞掉后中断信号丢失，上层无法再感知停止请求，这是阿里手册明确条款（恢复用 Thread.currentThread().interrupt()）

**Qconcurrency-1168（简答·中断）** 请说明「线程基础」中InterruptedException的机制与使用要点。
**要点（标准答案）**：① 捕获 InterruptedException 后必须恢复中断标志或继续向上抛；② 原理：异常被吞掉后中断信号丢失，上层无法再感知停止请求，这是阿里手册明确条款（恢复用 Thread.currentThread().interrupt()）；③ 使用要点：吞异常必须注释说明理由并恢复标志位。版本锚点：C1.5 手册。

**Qconcurrency-1169（单选·正向·中断）** 关于「线程基础」的说法，正确的是？
- A. isInterrupted 也会清除标志
- B. interrupted 与 isInterrupted 完全等价
- C. 静态方法操作的是当前线程以外的线程
- D. 静态 Thread.interrupted 会清除中断标志而实例方法 isInterrupted 不会
**答案：D**
**解析：** 静态 Thread.interrupted 会清除中断标志而实例方法 isInterrupted 不会。原因：interrupted 设计给线程自查并消费信号，误用会丢失他人设置的中断状态。
**来源：** JC-020 · 线程基础（Thread 源码）

**Qconcurrency-1170（判断·中断）** 静态 Thread.interrupted 会清除中断标志而实例方法 isInterrupted 不会
**答案：对。** 解析：interrupted 设计给线程自查并消费信号，误用会丢失他人设置的中断状态

**Qconcurrency-1171（判断·中断）** interrupted 与 isInterrupted 完全等价
**答案：错。** 正确表述：静态 Thread.interrupted 会清除中断标志而实例方法 isInterrupted 不会。原因：interrupted 设计给线程自查并消费信号，误用会丢失他人设置的中断状态

**Qconcurrency-1172（判断·中断）** isInterrupted 也会清除标志
**答案：错。** 正确表述：静态 Thread.interrupted 会清除中断标志而实例方法 isInterrupted 不会。原因：interrupted 设计给线程自查并消费信号，误用会丢失他人设置的中断状态

**Qconcurrency-1173（判断·中断）** 静态方法操作的是当前线程以外的线程
**答案：错。** 正确表述：静态 Thread.interrupted 会清除中断标志而实例方法 isInterrupted 不会。原因：interrupted 设计给线程自查并消费信号，误用会丢失他人设置的中断状态

**Qconcurrency-1174（场景单选·中断）** 在工程实践中关于「interrupted」，下列做法符合推荐实践的是？
- A. isInterrupted 也会清除标志
- B. 静态方法操作的是当前线程以外的线程
- C. 自查循环里用 interrupted 消费信号
- D. interrupted 与 isInterrupted 完全等价
**答案：C**
**解析：** 推荐实践：自查循环里用 interrupted 消费信号。事实依据：静态 Thread.interrupted 会清除中断标志而实例方法 isInterrupted 不会。

**Qconcurrency-1175（场景判断·中断）** 推荐实践：自查循环里用 interrupted 消费信号
**答案：对。** 解析：静态 Thread.interrupted 会清除中断标志而实例方法 isInterrupted 不会。原因：interrupted 设计给线程自查并消费信号，误用会丢失他人设置的中断状态

**Qconcurrency-1176（填空·中断）** 静态 Thread.______ 会清除中断标志而实例方法 isInterrupted 不会
**答案：interrupted**。解析：interrupted 设计给线程自查并消费信号，误用会丢失他人设置的中断状态

**Qconcurrency-1177（简答·中断）** 请说明「线程基础」中interrupted的机制与使用要点。
**要点（标准答案）**：① 静态 Thread.interrupted 会清除中断标志而实例方法 isInterrupted 不会；② 原理：interrupted 设计给线程自查并消费信号，误用会丢失他人设置的中断状态；③ 使用要点：自查循环里用 interrupted 消费信号。版本锚点：Thread 源码。

**Qconcurrency-1178（单选·正向·协作）** 关于「线程基础」的说法，正确的是？
- A. join 不提供内存可见性保证
- B. join 与 wait 语义无关
- C. 线程 A 调用 B.join() 会等待 B 终止且建立 happens-before
- D. join 会立即返回无论线程是否结束
**答案：C**
**解析：** 线程 A 调用 B.join() 会等待 B 终止且建立 happens-before。原因：join 内部是 B.isAlive() 的 wait 循环，B 终止时 notify，A 恢复后能看到 B 的全部结果。
**来源：** JC-021 · 线程基础（JLS 17.2.3）

**Qconcurrency-1179（判断·协作）** 线程 A 调用 B.join() 会等待 B 终止且建立 happens-before
**答案：对。** 解析：join 内部是 B.isAlive() 的 wait 循环，B 终止时 notify，A 恢复后能看到 B 的全部结果

**Qconcurrency-1180（判断·协作）** join 会立即返回无论线程是否结束
**答案：错。** 正确表述：线程 A 调用 B.join() 会等待 B 终止且建立 happens-before。原因：join 内部是 B.isAlive() 的 wait 循环，B 终止时 notify，A 恢复后能看到 B 的全部结果

**Qconcurrency-1181（判断·协作）** join 不提供内存可见性保证
**答案：错。** 正确表述：线程 A 调用 B.join() 会等待 B 终止且建立 happens-before。原因：join 内部是 B.isAlive() 的 wait 循环，B 终止时 notify，A 恢复后能看到 B 的全部结果

**Qconcurrency-1182（判断·协作）** join 与 wait 语义无关
**答案：错。** 正确表述：线程 A 调用 B.join() 会等待 B 终止且建立 happens-before。原因：join 内部是 B.isAlive() 的 wait 循环，B 终止时 notify，A 恢复后能看到 B 的全部结果

**Qconcurrency-1183（场景单选·协作）** 在工程实践中关于「join」，下列做法符合推荐实践的是？
- A. join 会立即返回无论线程是否结束
- B. join 与 wait 语义无关
- C. 主线程收集并行结果用 join 或 Future
- D. join 不提供内存可见性保证
**答案：C**
**解析：** 推荐实践：主线程收集并行结果用 join 或 Future。事实依据：线程 A 调用 B.join() 会等待 B 终止且建立 happens-before。

**Qconcurrency-1184（场景判断·协作）** 推荐实践：主线程收集并行结果用 join 或 Future
**答案：对。** 解析：线程 A 调用 B.join() 会等待 B 终止且建立 happens-before。原因：join 内部是 B.isAlive() 的 wait 循环，B 终止时 notify，A 恢复后能看到 B 的全部结果

**Qconcurrency-1185（填空·协作）** 线程 A 调用 B.______() 会等待 B 终止且建立 happens-before
**答案：join**。解析：join 内部是 B.isAlive() 的 wait 循环，B 终止时 notify，A 恢复后能看到 B 的全部结果

**Qconcurrency-1186（简答·协作）** 请说明「线程基础」中join的机制与使用要点。
**要点（标准答案）**：① 线程 A 调用 B.join() 会等待 B 终止且建立 happens-before；② 原理：join 内部是 B.isAlive() 的 wait 循环，B 终止时 notify，A 恢复后能看到 B 的全部结果；③ 使用要点：主线程收集并行结果用 join 或 Future。版本锚点：JLS 17.2.3。

**Qconcurrency-1187（单选·正向·线程属性）** 关于「线程基础」的说法，正确的是？
- A. main 线程默认是守护线程
- B. 守护线程会阻止 JVM 退出
- C. 守护线程退出前会执行 finally
- D. JVM 退出只看是否还有非守护线程
**答案：D**
**解析：** JVM 退出只看是否还有非守护线程。原因：main 线程结束后若只剩守护线程（如 GC 线程），JVM 直接退出且守护线程被硬杀不做清理。
**来源：** JC-022 · 线程基础（Thread.setDaemon javadoc）

**Qconcurrency-1188（判断·线程属性）** JVM 退出只看是否还有非守护线程
**答案：对。** 解析：main 线程结束后若只剩守护线程（如 GC 线程），JVM 直接退出且守护线程被硬杀不做清理

**Qconcurrency-1189（判断·线程属性）** 守护线程会阻止 JVM 退出
**答案：错。** 正确表述：JVM 退出只看是否还有非守护线程。原因：main 线程结束后若只剩守护线程（如 GC 线程），JVM 直接退出且守护线程被硬杀不做清理

**Qconcurrency-1190（判断·线程属性）** main 线程默认是守护线程
**答案：错。** 正确表述：JVM 退出只看是否还有非守护线程。原因：main 线程结束后若只剩守护线程（如 GC 线程），JVM 直接退出且守护线程被硬杀不做清理

**Qconcurrency-1191（判断·线程属性）** 守护线程退出前会执行 finally
**答案：错。** 正确表述：JVM 退出只看是否还有非守护线程。原因：main 线程结束后若只剩守护线程（如 GC 线程），JVM 直接退出且守护线程被硬杀不做清理

**Qconcurrency-1192（场景单选·线程属性）** 在工程实践中关于「守护线程」，下列做法符合推荐实践的是？
- A. main 线程默认是守护线程
- B. 守护线程退出前会执行 finally
- C. 守护线程会阻止 JVM 退出
- D. 后台监控、心跳类任务设为 daemon 并接受被硬杀
**答案：D**
**解析：** 推荐实践：后台监控、心跳类任务设为 daemon 并接受被硬杀。事实依据：JVM 退出只看是否还有非守护线程。

**Qconcurrency-1193（场景判断·线程属性）** 推荐实践：后台监控、心跳类任务设为 daemon 并接受被硬杀
**答案：对。** 解析：JVM 退出只看是否还有非守护线程。原因：main 线程结束后若只剩守护线程（如 GC 线程），JVM 直接退出且守护线程被硬杀不做清理

**Qconcurrency-1194（填空·线程属性）** JVM 退出只看是否还有非______
**答案：守护线程**。解析：main 线程结束后若只剩守护线程（如 GC 线程），JVM 直接退出且守护线程被硬杀不做清理

**Qconcurrency-1195（简答·线程属性）** 请说明「线程基础」中守护线程的机制与使用要点。
**要点（标准答案）**：① JVM 退出只看是否还有非守护线程；② 原理：main 线程结束后若只剩守护线程（如 GC 线程），JVM 直接退出且守护线程被硬杀不做清理；③ 使用要点：后台监控、心跳类任务设为 daemon 并接受被硬杀。版本锚点：Thread.setDaemon javadoc。

**Qconcurrency-1196（单选·正向·内存语义）** 关于「ThreadLocal」的说法，正确的是？
- A. 每个 Thread 内部持有 ThreadLocalMap 以 ThreadLocal 为 key
- B. ThreadLocal 数据存在 ThreadLocal 对象里
- C. ThreadLocalMap 是 HashMap 的子类
- D. ThreadLocal 通过加锁实现线程隔离
**答案：A**
**解析：** 每个 Thread 内部持有 ThreadLocalMap 以 ThreadLocal 为 key。原因：数据实际存在线程对象里，多个线程访问同一个 ThreadLocal 变量读到的是各自的副本，天然隔离。
**来源：** JC-023 · ThreadLocal（JDK 源码 Thread）

**Qconcurrency-1197（判断·内存语义）** 每个 Thread 内部持有 ThreadLocalMap 以 ThreadLocal 为 key
**答案：对。** 解析：数据实际存在线程对象里，多个线程访问同一个 ThreadLocal 变量读到的是各自的副本，天然隔离

**Qconcurrency-1198（判断·内存语义）** ThreadLocal 数据存在 ThreadLocal 对象里
**答案：错。** 正确表述：每个 Thread 内部持有 ThreadLocalMap 以 ThreadLocal 为 key。原因：数据实际存在线程对象里，多个线程访问同一个 ThreadLocal 变量读到的是各自的副本，天然隔离

**Qconcurrency-1199（判断·内存语义）** ThreadLocalMap 是 HashMap 的子类
**答案：错。** 正确表述：每个 Thread 内部持有 ThreadLocalMap 以 ThreadLocal 为 key。原因：数据实际存在线程对象里，多个线程访问同一个 ThreadLocal 变量读到的是各自的副本，天然隔离

**Qconcurrency-1200（判断·内存语义）** ThreadLocal 通过加锁实现线程隔离
**答案：错。** 正确表述：每个 Thread 内部持有 ThreadLocalMap 以 ThreadLocal 为 key。原因：数据实际存在线程对象里，多个线程访问同一个 ThreadLocal 变量读到的是各自的副本，天然隔离

**Qconcurrency-1201（场景单选·内存语义）** 在工程实践中关于「ThreadLocalMap」，下列做法符合推荐实践的是？
- A. ThreadLocalMap 是 HashMap 的子类
- B. ThreadLocal 数据存在 ThreadLocal 对象里
- C. ThreadLocal 通过加锁实现线程隔离
- D. 上下文传递（登录用户、traceId）首选 ThreadLocal
**答案：D**
**解析：** 推荐实践：上下文传递（登录用户、traceId）首选 ThreadLocal。事实依据：每个 Thread 内部持有 ThreadLocalMap 以 ThreadLocal 为 key。

**Qconcurrency-1202（场景判断·内存语义）** 推荐实践：上下文传递（登录用户、traceId）首选 ThreadLocal
**答案：对。** 解析：每个 Thread 内部持有 ThreadLocalMap 以 ThreadLocal 为 key。原因：数据实际存在线程对象里，多个线程访问同一个 ThreadLocal 变量读到的是各自的副本，天然隔离

**Qconcurrency-1203（填空·内存语义）** 每个 Thread 内部持有 ______ 以 ThreadLocal 为 key
**答案：ThreadLocalMap**。解析：数据实际存在线程对象里，多个线程访问同一个 ThreadLocal 变量读到的是各自的副本，天然隔离

**Qconcurrency-1204（简答·内存语义）** 请说明「ThreadLocal」中ThreadLocalMap的机制与使用要点。
**要点（标准答案）**：① 每个 Thread 内部持有 ThreadLocalMap 以 ThreadLocal 为 key；② 原理：数据实际存在线程对象里，多个线程访问同一个 ThreadLocal 变量读到的是各自的副本，天然隔离；③ 使用要点：上下文传递（登录用户、traceId）首选 ThreadLocal。版本锚点：JDK 源码 Thread。

**Qconcurrency-1205（单选·正向·内存语义）** 关于「ThreadLocal」的说法，正确的是？
- A. 有 cleanUp 机制所以绝不泄漏
- B. ThreadLocalMap 的 key 是弱引用 value 是强引用
- C. key 与 value 都是弱引用
- D. 内存泄漏只发生在 ThreadLocal 是局部变量时
**答案：B**
**解析：** ThreadLocalMap 的 key 是弱引用 value 是强引用。原因：ThreadLocal 外部引用消失后 key 会被 GC 回裂为 null，但 value 仍被线程强引用无法回收，线程池场景线程长存导致泄漏，必须 finally remove。
**来源：** JC-024 · ThreadLocal（JDK 源码）

**Qconcurrency-1206（判断·内存语义）** ThreadLocalMap 的 key 是弱引用 value 是强引用
**答案：对。** 解析：ThreadLocal 外部引用消失后 key 会被 GC 回裂为 null，但 value 仍被线程强引用无法回收，线程池场景线程长存导致泄漏，必须 finally remove

**Qconcurrency-1207（判断·内存语义）** key 与 value 都是弱引用
**答案：错。** 正确表述：ThreadLocalMap 的 key 是弱引用 value 是强引用。原因：ThreadLocal 外部引用消失后 key 会被 GC 回裂为 null，但 value 仍被线程强引用无法回收，线程池场景线程长存导致泄漏，必须 finally remove

**Qconcurrency-1208（判断·内存语义）** 有 cleanUp 机制所以绝不泄漏
**答案：错。** 正确表述：ThreadLocalMap 的 key 是弱引用 value 是强引用。原因：ThreadLocal 外部引用消失后 key 会被 GC 回裂为 null，但 value 仍被线程强引用无法回收，线程池场景线程长存导致泄漏，必须 finally remove

**Qconcurrency-1209（判断·内存语义）** 内存泄漏只发生在 ThreadLocal 是局部变量时
**答案：错。** 正确表述：ThreadLocalMap 的 key 是弱引用 value 是强引用。原因：ThreadLocal 外部引用消失后 key 会被 GC 回裂为 null，但 value 仍被线程强引用无法回收，线程池场景线程长存导致泄漏，必须 finally remove

**Qconcurrency-1210（场景单选·内存语义）** 在工程实践中关于「弱引用」，下列做法符合推荐实践的是？
- A. 内存泄漏只发生在 ThreadLocal 是局部变量时
- B. key 与 value 都是弱引用
- C. 线程池中用完必须 remove() 写进代码规范
- D. 有 cleanUp 机制所以绝不泄漏
**答案：C**
**解析：** 推荐实践：线程池中用完必须 remove() 写进代码规范。事实依据：ThreadLocalMap 的 key 是弱引用 value 是强引用。

**Qconcurrency-1211（场景判断·内存语义）** 推荐实践：线程池中用完必须 remove() 写进代码规范
**答案：对。** 解析：ThreadLocalMap 的 key 是弱引用 value 是强引用。原因：ThreadLocal 外部引用消失后 key 会被 GC 回裂为 null，但 value 仍被线程强引用无法回收，线程池场景线程长存导致泄漏，必须 finally remove

**Qconcurrency-1212（填空·内存语义）** ThreadLocalMap 的 key 是______ value 是强引用
**答案：弱引用**。解析：ThreadLocal 外部引用消失后 key 会被 GC 回裂为 null，但 value 仍被线程强引用无法回收，线程池场景线程长存导致泄漏，必须 finally remove

**Qconcurrency-1213（简答·内存语义）** 请说明「ThreadLocal」中弱引用的机制与使用要点。
**要点（标准答案）**：① ThreadLocalMap 的 key 是弱引用 value 是强引用；② 原理：ThreadLocal 外部引用消失后 key 会被 GC 回裂为 null，但 value 仍被线程强引用无法回收，线程池场景线程长存导致泄漏，必须 finally remove；③ 使用要点：线程池中用完必须 remove() 写进代码规范。版本锚点：JDK 源码。

**Qconcurrency-1214（单选·正向·误用）** 关于「ThreadLocal」的说法，正确的是？
- A. 子线程修改会同步回父线程
- B. TTL 是 JDK 内置类
- C. InheritableThreadLocal 只在子线程创建时拷贝一次在线程池场景失效
- D. InheritableThreadLocal 能跟随线程池任务传递
**答案：C**
**解析：** InheritableThreadLocal 只在子线程创建时拷贝一次在线程池场景失效。原因：线程池线程是复用的不会重新创建，后续任务拿到的是首次创建时的快照，需用阿里开源的 TransmittableThreadLocal 配 TTL 包装线程池。
**来源：** JC-025 · ThreadLocal（开源 TTL）

**Qconcurrency-1215（判断·误用）** InheritableThreadLocal 只在子线程创建时拷贝一次在线程池场景失效
**答案：对。** 解析：线程池线程是复用的不会重新创建，后续任务拿到的是首次创建时的快照，需用阿里开源的 TransmittableThreadLocal 配 TTL 包装线程池

**Qconcurrency-1216（判断·误用）** InheritableThreadLocal 能跟随线程池任务传递
**答案：错。** 正确表述：InheritableThreadLocal 只在子线程创建时拷贝一次在线程池场景失效。原因：线程池线程是复用的不会重新创建，后续任务拿到的是首次创建时的快照，需用阿里开源的 TransmittableThreadLocal 配 TTL 包装线程池

**Qconcurrency-1217（判断·误用）** TTL 是 JDK 内置类
**答案：错。** 正确表述：InheritableThreadLocal 只在子线程创建时拷贝一次在线程池场景失效。原因：线程池线程是复用的不会重新创建，后续任务拿到的是首次创建时的快照，需用阿里开源的 TransmittableThreadLocal 配 TTL 包装线程池

**Qconcurrency-1218（判断·误用）** 子线程修改会同步回父线程
**答案：错。** 正确表述：InheritableThreadLocal 只在子线程创建时拷贝一次在线程池场景失效。原因：线程池线程是复用的不会重新创建，后续任务拿到的是首次创建时的快照，需用阿里开源的 TransmittableThreadLocal 配 TTL 包装线程池

**Qconcurrency-1219（场景单选·误用）** 在工程实践中关于「InheritableThreadLocal」，下列做法符合推荐实践的是？
- A. 跨线程池传递上下文用 TransmittableThreadLocal
- B. TTL 是 JDK 内置类
- C. InheritableThreadLocal 能跟随线程池任务传递
- D. 子线程修改会同步回父线程
**答案：A**
**解析：** 推荐实践：跨线程池传递上下文用 TransmittableThreadLocal。事实依据：InheritableThreadLocal 只在子线程创建时拷贝一次在线程池场景失效。

**Qconcurrency-1220（场景判断·误用）** 推荐实践：跨线程池传递上下文用 TransmittableThreadLocal
**答案：对。** 解析：InheritableThreadLocal 只在子线程创建时拷贝一次在线程池场景失效。原因：线程池线程是复用的不会重新创建，后续任务拿到的是首次创建时的快照，需用阿里开源的 TransmittableThreadLocal 配 TTL 包装线程池

**Qconcurrency-1221（填空·误用）** ______ 只在子线程创建时拷贝一次在线程池场景失效
**答案：InheritableThreadLocal**。解析：线程池线程是复用的不会重新创建，后续任务拿到的是首次创建时的快照，需用阿里开源的 TransmittableThreadLocal 配 TTL 包装线程池

**Qconcurrency-1222（简答·误用）** 请说明「ThreadLocal」中InheritableThreadLocal的机制与使用要点。
**要点（标准答案）**：① InheritableThreadLocal 只在子线程创建时拷贝一次在线程池场景失效；② 原理：线程池线程是复用的不会重新创建，后续任务拿到的是首次创建时的快照，需用阿里开源的 TransmittableThreadLocal 配 TTL 包装线程池；③ 使用要点：跨线程池传递上下文用 TransmittableThreadLocal。版本锚点：开源 TTL。

**Qconcurrency-1223（单选·正向·实现细节）** 关于「ThreadLocal」的说法，正确的是？
- A. ThreadLocalMap 的哈希增量是魔数 0x61c88647（斐波那契散列）
- B. 魔数是随机选的
- C. 0x61c88647 是 MD5 截断
- D. 斐波那契散列适合所有场景
**答案：A**
**解析：** ThreadLocalMap 的哈希增量是魔数 0x61c88647（斐波那契散列）。原因：相邻 ThreadLocal 的 hash 以黄金分割数递增，2 的幂容量下能均匀散列减少冲突。
**来源：** JC-026 · ThreadLocal（JDK 源码）

**Qconcurrency-1224（判断·实现细节）** ThreadLocalMap 的哈希增量是魔数 0x61c88647（斐波那契散列）
**答案：对。** 解析：相邻 ThreadLocal 的 hash 以黄金分割数递增，2 的幂容量下能均匀散列减少冲突

**Qconcurrency-1225（判断·实现细节）** 魔数是随机选的
**答案：错。** 正确表述：ThreadLocalMap 的哈希增量是魔数 0x61c88647（斐波那契散列）。原因：相邻 ThreadLocal 的 hash 以黄金分割数递增，2 的幂容量下能均匀散列减少冲突

**Qconcurrency-1226（判断·实现细节）** 0x61c88647 是 MD5 截断
**答案：错。** 正确表述：ThreadLocalMap 的哈希增量是魔数 0x61c88647（斐波那契散列）。原因：相邻 ThreadLocal 的 hash 以黄金分割数递增，2 的幂容量下能均匀散列减少冲突

**Qconcurrency-1227（判断·实现细节）** 斐波那契散列适合所有场景
**答案：错。** 正确表述：ThreadLocalMap 的哈希增量是魔数 0x61c88647（斐波那契散列）。原因：相邻 ThreadLocal 的 hash 以黄金分割数递增，2 的幂容量下能均匀散列减少冲突

**Qconcurrency-1228（场景单选·实现细节）** 在工程实践中关于「0x61c88647」，下列做法符合推荐实践的是？
- A. 面试谈 ThreadLocal 冲突优化时引用此数
- B. 0x61c88647 是 MD5 截断
- C. 斐波那契散列适合所有场景
- D. 魔数是随机选的
**答案：A**
**解析：** 推荐实践：面试谈 ThreadLocal 冲突优化时引用此数。事实依据：ThreadLocalMap 的哈希增量是魔数 0x61c88647（斐波那契散列）。

**Qconcurrency-1229（场景判断·实现细节）** 推荐实践：面试谈 ThreadLocal 冲突优化时引用此数
**答案：对。** 解析：ThreadLocalMap 的哈希增量是魔数 0x61c88647（斐波那契散列）。原因：相邻 ThreadLocal 的 hash 以黄金分割数递增，2 的幂容量下能均匀散列减少冲突

**Qconcurrency-1230（填空·实现细节）** ThreadLocalMap 的哈希增量是魔数 ______（斐波那契散列）
**答案：0x61c88647**。解析：相邻 ThreadLocal 的 hash 以黄金分割数递增，2 的幂容量下能均匀散列减少冲突

**Qconcurrency-1231（简答·实现细节）** 请说明「ThreadLocal」中0x61c88647的机制与使用要点。
**要点（标准答案）**：① ThreadLocalMap 的哈希增量是魔数 0x61c88647（斐波那契散列）；② 原理：相邻 ThreadLocal 的 hash 以黄金分割数递增，2 的幂容量下能均匀散列减少冲突；③ 使用要点：面试谈 ThreadLocal 冲突优化时引用此数。版本锚点：JDK 源码。

**Qconcurrency-1232（单选·正向·参数）** 关于「线程池」的说法，正确的是？
- A. keepAliveTime 对核心线程默认也生效
- B. threadFactory 参数可有可无
- C. 线程池标准构造有 7 个参数：corePoolSize、maximumPoolSize、keepAliveTime、unit、workQueue、threadFactory、handler
- D. 线程池只有核心与非核心线程两个参数
**答案：C**
**解析：** 线程池标准构造有 7 个参数：corePoolSize、maximumPoolSize、keepAliveTime、unit、workQueue、threadFactory、handler。原因：这是任务调度策略的全部输入，任何 Executors 快捷方法都是对它的包装且各有陷阱。
**来源：** JC-027 · 线程池（JDK 文档）

**Qconcurrency-1233（判断·参数）** 线程池标准构造有 7 个参数：corePoolSize、maximumPoolSize、keepAliveTime、unit、workQueue、threadFactory、handler
**答案：对。** 解析：这是任务调度策略的全部输入，任何 Executors 快捷方法都是对它的包装且各有陷阱

**Qconcurrency-1234（判断·参数）** 线程池只有核心与非核心线程两个参数
**答案：错。** 正确表述：线程池标准构造有 7 个参数：corePoolSize、maximumPoolSize、keepAliveTime、unit、workQueue、threadFactory、handler。原因：这是任务调度策略的全部输入，任何 Executors 快捷方法都是对它的包装且各有陷阱

**Qconcurrency-1235（判断·参数）** keepAliveTime 对核心线程默认也生效
**答案：错。** 正确表述：线程池标准构造有 7 个参数：corePoolSize、maximumPoolSize、keepAliveTime、unit、workQueue、threadFactory、handler。原因：这是任务调度策略的全部输入，任何 Executors 快捷方法都是对它的包装且各有陷阱

**Qconcurrency-1236（判断·参数）** threadFactory 参数可有可无
**答案：错。** 正确表述：线程池标准构造有 7 个参数：corePoolSize、maximumPoolSize、keepAliveTime、unit、workQueue、threadFactory、handler。原因：这是任务调度策略的全部输入，任何 Executors 快捷方法都是对它的包装且各有陷阱

**Qconcurrency-1237（场景单选·参数）** 在工程实践中关于「ThreadPoolExecutor」，下列做法符合推荐实践的是？
- A. keepAliveTime 对核心线程默认也生效
- B. 线程池只有核心与非核心线程两个参数
- C. threadFactory 参数可有可无
- D. 生产环境一律手动 new ThreadPoolExecutor
**答案：D**
**解析：** 推荐实践：生产环境一律手动 new ThreadPoolExecutor。事实依据：线程池标准构造有 7 个参数：corePoolSize、maximumPoolSize、keepAliveTime、unit、workQueue、threadFactory、handler。

**Qconcurrency-1238（场景判断·参数）** 推荐实践：生产环境一律手动 new ThreadPoolExecutor
**答案：对。** 解析：线程池标准构造有 7 个参数：corePoolSize、maximumPoolSize、keepAliveTime、unit、workQueue、threadFactory、handler。原因：这是任务调度策略的全部输入，任何 Executors 快捷方法都是对它的包装且各有陷阱

**Qconcurrency-1239（简答·参数）** 请说明「线程池」中ThreadPoolExecutor的机制与使用要点。
**要点（标准答案）**：① 线程池标准构造有 7 个参数：corePoolSize、maximumPoolSize、keepAliveTime、unit、workQueue、threadFactory、handler；② 原理：这是任务调度策略的全部输入，任何 Executors 快捷方法都是对它的包装且各有陷阱；③ 使用要点：生产环境一律手动 new ThreadPoolExecutor。版本锚点：JDK 文档。

**Qconcurrency-1240（单选·正向·调度顺序）** 关于「线程池」的说法，正确的是？
- A. 队列满了立即创建最大线程
- B. 先创建非核心线程再入队
- C. 拒绝策略在队列满之前触发
- D. 任务提交顺序是：核心线程未满则创建核心线程，满了先入队，队列满了才扩到最大线程，再满才拒绝
**答案：D**
**解析：** 任务提交顺序是：核心线程未满则创建核心线程，满了先入队，队列满了才扩到最大线程，再满才拒绝。原因：注意是先入队后扩容而非先扩容，实测提交阻塞任务验证：4 核心队列容量 2 最大 8 时第 3、4 个任务入队第 5 个才创建非核心线程。
**来源：** JC-028 · 线程池（ThreadPoolExecutor javadoc 实测）

**Qconcurrency-1241（判断·调度顺序）** 任务提交顺序是：核心线程未满则创建核心线程，满了先入队，队列满了才扩到最大线程，再满才拒绝
**答案：对。** 解析：注意是先入队后扩容而非先扩容，实测提交阻塞任务验证：4 核心队列容量 2 最大 8 时第 3、4 个任务入队第 5 个才创建非核心线程

**Qconcurrency-1242（判断·调度顺序）** 队列满了立即创建最大线程
**答案：错。** 正确表述：任务提交顺序是：核心线程未满则创建核心线程，满了先入队，队列满了才扩到最大线程，再满才拒绝。原因：注意是先入队后扩容而非先扩容，实测提交阻塞任务验证：4 核心队列容量 2 最大 8 时第 3、4 个任务入队第 5 个才创建非核心线程

**Qconcurrency-1243（判断·调度顺序）** 先创建非核心线程再入队
**答案：错。** 正确表述：任务提交顺序是：核心线程未满则创建核心线程，满了先入队，队列满了才扩到最大线程，再满才拒绝。原因：注意是先入队后扩容而非先扩容，实测提交阻塞任务验证：4 核心队列容量 2 最大 8 时第 3、4 个任务入队第 5 个才创建非核心线程

**Qconcurrency-1244（判断·调度顺序）** 拒绝策略在队列满之前触发
**答案：错。** 正确表述：任务提交顺序是：核心线程未满则创建核心线程，满了先入队，队列满了才扩到最大线程，再满才拒绝。原因：注意是先入队后扩容而非先扩容，实测提交阻塞任务验证：4 核心队列容量 2 最大 8 时第 3、4 个任务入队第 5 个才创建非核心线程

**Qconcurrency-1245（场景单选·调度顺序）** 在工程实践中关于「入队」，下列做法符合推荐实践的是？
- A. 容量规划必须同时算队列与最大线程
- B. 拒绝策略在队列满之前触发
- C. 队列满了立即创建最大线程
- D. 先创建非核心线程再入队
**答案：A**
**解析：** 推荐实践：容量规划必须同时算队列与最大线程。事实依据：任务提交顺序是：核心线程未满则创建核心线程，满了先入队，队列满了才扩到最大线程，再满才拒绝。

**Qconcurrency-1246（场景判断·调度顺序）** 推荐实践：容量规划必须同时算队列与最大线程
**答案：对。** 解析：任务提交顺序是：核心线程未满则创建核心线程，满了先入队，队列满了才扩到最大线程，再满才拒绝。原因：注意是先入队后扩容而非先扩容，实测提交阻塞任务验证：4 核心队列容量 2 最大 8 时第 3、4 个任务入队第 5 个才创建非核心线程

**Qconcurrency-1247（填空·调度顺序）** 任务提交顺序是：核心线程未满则创建核心线程，满了先______，队列满了才扩到最大线程，再满才拒绝
**答案：入队**。解析：注意是先入队后扩容而非先扩容，实测提交阻塞任务验证：4 核心队列容量 2 最大 8 时第 3、4 个任务入队第 5 个才创建非核心线程

**Qconcurrency-1248（简答·调度顺序）** 请说明「线程池」中入队的机制与使用要点。
**要点（标准答案）**：① 任务提交顺序是：核心线程未满则创建核心线程，满了先入队，队列满了才扩到最大线程，再满才拒绝；② 原理：注意是先入队后扩容而非先扩容，实测提交阻塞任务验证：4 核心队列容量 2 最大 8 时第 3、4 个任务入队第 5 个才创建非核心线程；③ 使用要点：容量规划必须同时算队列与最大线程。版本锚点：ThreadPoolExecutor javadoc 实测。

**Qconcurrency-1249（单选·正向·误用）** 关于「线程池」的说法，正确的是？
- A. newFixedThreadPool 会自动拒绝多余任务
- B. 队列满了会扩容线程
- C. OOM 风险只在任务执行慢时不存在
- D. Executors.newFixedThreadPool 使用无界 LinkedBlockingQueue 可能堆积任务导致 OOM
**答案：D**
**解析：** Executors.newFixedThreadPool 使用无界 LinkedBlockingQueue 可能堆积任务导致 OOM。原因：队列容量是 Integer.MAX_VALUE，下游变慢时任务无限堆积，阿里手册明确禁止使用 Executors 创建线程池。
**来源：** JC-029 · 线程池（阿里手册）

**Qconcurrency-1250（判断·误用）** Executors.newFixedThreadPool 使用无界 LinkedBlockingQueue 可能堆积任务导致 OOM
**答案：对。** 解析：队列容量是 Integer.MAX_VALUE，下游变慢时任务无限堆积，阿里手册明确禁止使用 Executors 创建线程池

**Qconcurrency-1251（判断·误用）** newFixedThreadPool 会自动拒绝多余任务
**答案：错。** 正确表述：Executors.newFixedThreadPool 使用无界 LinkedBlockingQueue 可能堆积任务导致 OOM。原因：队列容量是 Integer.MAX_VALUE，下游变慢时任务无限堆积，阿里手册明确禁止使用 Executors 创建线程池

**Qconcurrency-1252（判断·误用）** 队列满了会扩容线程
**答案：错。** 正确表述：Executors.newFixedThreadPool 使用无界 LinkedBlockingQueue 可能堆积任务导致 OOM。原因：队列容量是 Integer.MAX_VALUE，下游变慢时任务无限堆积，阿里手册明确禁止使用 Executors 创建线程池

**Qconcurrency-1253（判断·误用）** OOM 风险只在任务执行慢时不存在
**答案：错。** 正确表述：Executors.newFixedThreadPool 使用无界 LinkedBlockingQueue 可能堆积任务导致 OOM。原因：队列容量是 Integer.MAX_VALUE，下游变慢时任务无限堆积，阿里手册明确禁止使用 Executors 创建线程池

**Qconcurrency-1254（场景单选·误用）** 在工程实践中关于「newFixedThreadPool」，下列做法符合推荐实践的是？
- A. 生产用 new ThreadPoolExecutor 加有界队列
- B. OOM 风险只在任务执行慢时不存在
- C. newFixedThreadPool 会自动拒绝多余任务
- D. 队列满了会扩容线程
**答案：A**
**解析：** 推荐实践：生产用 new ThreadPoolExecutor 加有界队列。事实依据：Executors.newFixedThreadPool 使用无界 LinkedBlockingQueue 可能堆积任务导致 OOM。

**Qconcurrency-1255（场景判断·误用）** 推荐实践：生产用 new ThreadPoolExecutor 加有界队列
**答案：对。** 解析：Executors.newFixedThreadPool 使用无界 LinkedBlockingQueue 可能堆积任务导致 OOM。原因：队列容量是 Integer.MAX_VALUE，下游变慢时任务无限堆积，阿里手册明确禁止使用 Executors 创建线程池

**Qconcurrency-1256（填空·误用）** Executors.______ 使用无界 LinkedBlockingQueue 可能堆积任务导致 OOM
**答案：newFixedThreadPool**。解析：队列容量是 Integer.MAX_VALUE，下游变慢时任务无限堆积，阿里手册明确禁止使用 Executors 创建线程池

**Qconcurrency-1257（简答·误用）** 请说明「线程池」中newFixedThreadPool的机制与使用要点。
**要点（标准答案）**：① Executors.newFixedThreadPool 使用无界 LinkedBlockingQueue 可能堆积任务导致 OOM；② 原理：队列容量是 Integer.MAX_VALUE，下游变慢时任务无限堆积，阿里手册明确禁止使用 Executors 创建线程池；③ 使用要点：生产用 new ThreadPoolExecutor 加有界队列。版本锚点：阿里手册。

**Qconcurrency-1258（单选·正向·误用）** 关于「线程池」的说法，正确的是？
- A. 线程数上限是 CPU 核数
- B. 它内部队列是 LinkedBlockingQueue
- C. newCachedThreadPool 有默认 10 个线程上限
- D. Executors.newCachedThreadPool 最大线程数是 Integer.MAX_VALUE 可无限创建线程
**答案：D**
**解析：** Executors.newCachedThreadPool 最大线程数是 Integer.MAX_VALUE 可无限创建线程。原因：SynchronousQueue 无容量不排队，来一个任务必建一个新线程，高并发瞬间创建数万线程耗尽内存与线程句柄。
**来源：** JC-030 · 线程池（阿里手册）

**Qconcurrency-1259（判断·误用）** Executors.newCachedThreadPool 最大线程数是 Integer.MAX_VALUE 可无限创建线程
**答案：对。** 解析：SynchronousQueue 无容量不排队，来一个任务必建一个新线程，高并发瞬间创建数万线程耗尽内存与线程句柄

**Qconcurrency-1260（判断·误用）** newCachedThreadPool 有默认 10 个线程上限
**答案：错。** 正确表述：Executors.newCachedThreadPool 最大线程数是 Integer.MAX_VALUE 可无限创建线程。原因：SynchronousQueue 无容量不排队，来一个任务必建一个新线程，高并发瞬间创建数万线程耗尽内存与线程句柄

**Qconcurrency-1261（判断·误用）** 它内部队列是 LinkedBlockingQueue
**答案：错。** 正确表述：Executors.newCachedThreadPool 最大线程数是 Integer.MAX_VALUE 可无限创建线程。原因：SynchronousQueue 无容量不排队，来一个任务必建一个新线程，高并发瞬间创建数万线程耗尽内存与线程句柄

**Qconcurrency-1262（判断·误用）** 线程数上限是 CPU 核数
**答案：错。** 正确表述：Executors.newCachedThreadPool 最大线程数是 Integer.MAX_VALUE 可无限创建线程。原因：SynchronousQueue 无容量不排队，来一个任务必建一个新线程，高并发瞬间创建数万线程耗尽内存与线程句柄

**Qconcurrency-1263（场景单选·误用）** 在工程实践中关于「newCachedThreadPool」，下列做法符合推荐实践的是？
- A. 突发可容忍时可用但要压测线程峰值
- B. 线程数上限是 CPU 核数
- C. 它内部队列是 LinkedBlockingQueue
- D. newCachedThreadPool 有默认 10 个线程上限
**答案：A**
**解析：** 推荐实践：突发可容忍时可用但要压测线程峰值。事实依据：Executors.newCachedThreadPool 最大线程数是 Integer.MAX_VALUE 可无限创建线程。

**Qconcurrency-1264（场景判断·误用）** 推荐实践：突发可容忍时可用但要压测线程峰值
**答案：对。** 解析：Executors.newCachedThreadPool 最大线程数是 Integer.MAX_VALUE 可无限创建线程。原因：SynchronousQueue 无容量不排队，来一个任务必建一个新线程，高并发瞬间创建数万线程耗尽内存与线程句柄

**Qconcurrency-1265（填空·误用）** Executors.______ 最大线程数是 Integer.MAX_VALUE 可无限创建线程
**答案：newCachedThreadPool**。解析：SynchronousQueue 无容量不排队，来一个任务必建一个新线程，高并发瞬间创建数万线程耗尽内存与线程句柄

**Qconcurrency-1266（简答·误用）** 请说明「线程池」中newCachedThreadPool的机制与使用要点。
**要点（标准答案）**：① Executors.newCachedThreadPool 最大线程数是 Integer.MAX_VALUE 可无限创建线程；② 原理：SynchronousQueue 无容量不排队，来一个任务必建一个新线程，高并发瞬间创建数万线程耗尽内存与线程句柄；③ 使用要点：突发可容忍时可用但要压测线程峰值。版本锚点：阿里手册。

**Qconcurrency-1267（单选·正向·拒绝策略）** 关于「线程池」的说法，正确的是？
- A. 默认策略是静默丢弃
- B. 拒绝策略可以自动重试任务
- C. ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException
- D. 默认策略是调用者执行
**答案：C**
**解析：** ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException。原因：四种策略：Abort 抛异常、CallerRuns 由提交线程执行、Discard 静默丢弃、DiscardOldest 丢队首再提交，默认抛异常逼迫调用方处理。
**来源：** JC-031 · 线程池（JDK 源码）

**Qconcurrency-1268（判断·拒绝策略）** ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException
**答案：对。** 解析：四种策略：Abort 抛异常、CallerRuns 由提交线程执行、Discard 静默丢弃、DiscardOldest 丢队首再提交，默认抛异常逼迫调用方处理

**Qconcurrency-1269（判断·拒绝策略）** 默认策略是静默丢弃
**答案：错。** 正确表述：ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException。原因：四种策略：Abort 抛异常、CallerRuns 由提交线程执行、Discard 静默丢弃、DiscardOldest 丢队首再提交，默认抛异常逼迫调用方处理

**Qconcurrency-1270（判断·拒绝策略）** 默认策略是调用者执行
**答案：错。** 正确表述：ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException。原因：四种策略：Abort 抛异常、CallerRuns 由提交线程执行、Discard 静默丢弃、DiscardOldest 丢队首再提交，默认抛异常逼迫调用方处理

**Qconcurrency-1271（判断·拒绝策略）** 拒绝策略可以自动重试任务
**答案：错。** 正确表述：ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException。原因：四种策略：Abort 抛异常、CallerRuns 由提交线程执行、Discard 静默丢弃、DiscardOldest 丢队首再提交，默认抛异常逼迫调用方处理

**Qconcurrency-1272（场景单选·拒绝策略）** 在工程实践中关于「AbortPolicy」，下列做法符合推荐实践的是？
- A. 拒绝策略可以自动重试任务
- B. 默认策略是静默丢弃
- C. 重要任务用 CallerRuns 降速反压
- D. 默认策略是调用者执行
**答案：C**
**解析：** 推荐实践：重要任务用 CallerRuns 降速反压。事实依据：ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException。

**Qconcurrency-1273（场景判断·拒绝策略）** 推荐实践：重要任务用 CallerRuns 降速反压
**答案：对。** 解析：ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException。原因：四种策略：Abort 抛异常、CallerRuns 由提交线程执行、Discard 静默丢弃、DiscardOldest 丢队首再提交，默认抛异常逼迫调用方处理

**Qconcurrency-1274（填空·拒绝策略）** ThreadPoolExecutor 默认拒绝策略是 ______ 即抛 RejectedExecutionException
**答案：AbortPolicy**。解析：四种策略：Abort 抛异常、CallerRuns 由提交线程执行、Discard 静默丢弃、DiscardOldest 丢队首再提交，默认抛异常逼迫调用方处理

**Qconcurrency-1275（简答·拒绝策略）** 请说明「线程池」中AbortPolicy的机制与使用要点。
**要点（标准答案）**：① ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException；② 原理：四种策略：Abort 抛异常、CallerRuns 由提交线程执行、Discard 静默丢弃、DiscardOldest 丢队首再提交，默认抛异常逼迫调用方处理；③ 使用要点：重要任务用 CallerRuns 降速反压。版本锚点：JDK 源码。

**Qconcurrency-1276（单选·正向·拒绝策略）** 关于「线程池」的说法，正确的是？
- A. CallerRunsPolicy 让提交任务的线程自己执行以实现反压
- B. 它不会阻塞提交线程
- C. 它把任务放回队列头部
- D. CallerRunsPolicy 把任务转给空闲线程执行
**答案：A**
**解析：** CallerRunsPolicy 让提交任务的线程自己执行以实现反压。原因：执行期间提交线程被占用，上游生产速度被迫降速，是简洁的背压手段但会阻塞调用方。
**来源：** JC-032 · 线程池（实战经验）

**Qconcurrency-1277（判断·拒绝策略）** CallerRunsPolicy 让提交任务的线程自己执行以实现反压
**答案：对。** 解析：执行期间提交线程被占用，上游生产速度被迫降速，是简洁的背压手段但会阻塞调用方

**Qconcurrency-1278（判断·拒绝策略）** CallerRunsPolicy 把任务转给空闲线程执行
**答案：错。** 正确表述：CallerRunsPolicy 让提交任务的线程自己执行以实现反压。原因：执行期间提交线程被占用，上游生产速度被迫降速，是简洁的背压手段但会阻塞调用方

**Qconcurrency-1279（判断·拒绝策略）** 它把任务放回队列头部
**答案：错。** 正确表述：CallerRunsPolicy 让提交任务的线程自己执行以实现反压。原因：执行期间提交线程被占用，上游生产速度被迫降速，是简洁的背压手段但会阻塞调用方

**Qconcurrency-1280（判断·拒绝策略）** 它不会阻塞提交线程
**答案：错。** 正确表述：CallerRunsPolicy 让提交任务的线程自己执行以实现反压。原因：执行期间提交线程被占用，上游生产速度被迫降速，是简洁的背压手段但会阻塞调用方

**Qconcurrency-1281（场景单选·拒绝策略）** 在工程实践中关于「CallerRunsPolicy」，下列做法符合推荐实践的是？
- A. CallerRunsPolicy 把任务转给空闲线程执行
- B. 它不会阻塞提交线程
- C. 非核心链路可接受，支付链路慎用
- D. 它把任务放回队列头部
**答案：C**
**解析：** 推荐实践：非核心链路可接受，支付链路慎用。事实依据：CallerRunsPolicy 让提交任务的线程自己执行以实现反压。

**Qconcurrency-1282（场景判断·拒绝策略）** 推荐实践：非核心链路可接受，支付链路慎用
**答案：对。** 解析：CallerRunsPolicy 让提交任务的线程自己执行以实现反压。原因：执行期间提交线程被占用，上游生产速度被迫降速，是简洁的背压手段但会阻塞调用方

**Qconcurrency-1283（填空·拒绝策略）** ______ 让提交任务的线程自己执行以实现反压
**答案：CallerRunsPolicy**。解析：执行期间提交线程被占用，上游生产速度被迫降速，是简洁的背压手段但会阻塞调用方

**Qconcurrency-1284（简答·拒绝策略）** 请说明「线程池」中CallerRunsPolicy的机制与使用要点。
**要点（标准答案）**：① CallerRunsPolicy 让提交任务的线程自己执行以实现反压；② 原理：执行期间提交线程被占用，上游生产速度被迫降速，是简洁的背压手段但会阻塞调用方；③ 使用要点：非核心链路可接受，支付链路慎用。版本锚点：实战经验。

**Qconcurrency-1285（单选·正向·参数）** 关于「线程池」的说法，正确的是？
- A. 开启后线程池最少保留 1 个线程
- B. 该参数只对非核心线程生效
- C. allowCoreThreadTimeOut(true) 可让核心线程在空闲超过 keepAliveTime 后被回收
- D. 核心线程在任何配置下都不会回收
**答案：C**
**解析：** allowCoreThreadTimeOut(true) 可让核心线程在空闲超过 keepAliveTime 后被回收。原因：默认核心线程不回收常驻内存，流量低谷期可用该参数释放资源，回收后新任务重新建线程。
**来源：** JC-033 · 线程池（JDK 文档）

**Qconcurrency-1286（判断·参数）** allowCoreThreadTimeOut(true) 可让核心线程在空闲超过 keepAliveTime 后被回收
**答案：对。** 解析：默认核心线程不回收常驻内存，流量低谷期可用该参数释放资源，回收后新任务重新建线程

**Qconcurrency-1287（判断·参数）** 核心线程在任何配置下都不会回收
**答案：错。** 正确表述：allowCoreThreadTimeOut(true) 可让核心线程在空闲超过 keepAliveTime 后被回收。原因：默认核心线程不回收常驻内存，流量低谷期可用该参数释放资源，回收后新任务重新建线程

**Qconcurrency-1288（判断·参数）** 该参数只对非核心线程生效
**答案：错。** 正确表述：allowCoreThreadTimeOut(true) 可让核心线程在空闲超过 keepAliveTime 后被回收。原因：默认核心线程不回收常驻内存，流量低谷期可用该参数释放资源，回收后新任务重新建线程

**Qconcurrency-1289（判断·参数）** 开启后线程池最少保留 1 个线程
**答案：错。** 正确表述：allowCoreThreadTimeOut(true) 可让核心线程在空闲超过 keepAliveTime 后被回收。原因：默认核心线程不回收常驻内存，流量低谷期可用该参数释放资源，回收后新任务重新建线程

**Qconcurrency-1290（场景单选·参数）** 在工程实践中关于「allowCoreThreadTimeOut」，下列做法符合推荐实践的是？
- A. 突发流量型服务低谷缩容
- B. 该参数只对非核心线程生效
- C. 核心线程在任何配置下都不会回收
- D. 开启后线程池最少保留 1 个线程
**答案：A**
**解析：** 推荐实践：突发流量型服务低谷缩容。事实依据：allowCoreThreadTimeOut(true) 可让核心线程在空闲超过 keepAliveTime 后被回收。

**Qconcurrency-1291（场景判断·参数）** 推荐实践：突发流量型服务低谷缩容
**答案：对。** 解析：allowCoreThreadTimeOut(true) 可让核心线程在空闲超过 keepAliveTime 后被回收。原因：默认核心线程不回收常驻内存，流量低谷期可用该参数释放资源，回收后新任务重新建线程

**Qconcurrency-1292（填空·参数）** ______(true) 可让核心线程在空闲超过 keepAliveTime 后被回收
**答案：allowCoreThreadTimeOut**。解析：默认核心线程不回收常驻内存，流量低谷期可用该参数释放资源，回收后新任务重新建线程

**Qconcurrency-1293（简答·参数）** 请说明「线程池」中allowCoreThreadTimeOut的机制与使用要点。
**要点（标准答案）**：① allowCoreThreadTimeOut(true) 可让核心线程在空闲超过 keepAliveTime 后被回收；② 原理：默认核心线程不回收常驻内存，流量低谷期可用该参数释放资源，回收后新任务重新建线程；③ 使用要点：突发流量型服务低谷缩容。版本锚点：JDK 文档。

**Qconcurrency-1294（单选·正向·调优）** 关于「线程池」的说法，正确的是？
- A. 2N 是所有场景的标准答案
- B. 线程数经验公式：CPU 密集型约 N+1，IO 密集型约 N×(1+等待时间/计算时间)
- C. IO 密集型线程数越少越好
- D. 线程数一律设为 CPU 核数最优
**答案：B**
**解析：** 线程数经验公式：CPU 密集型约 N+1，IO 密集型约 N×(1+等待时间/计算时间)。原因：CPU 密集多一个线程用于缺页等暂停；IO 密集等待期间可切换线程提高吞吐，实际以压测为准。
**来源：** JC-034 · 线程池（Java Concurrency in Practice）

**Qconcurrency-1295（判断·调优）** 线程数经验公式：CPU 密集型约 N+1，IO 密集型约 N×(1+等待时间/计算时间)
**答案：对。** 解析：CPU 密集多一个线程用于缺页等暂停；IO 密集等待期间可切换线程提高吞吐，实际以压测为准

**Qconcurrency-1296（判断·调优）** 线程数一律设为 CPU 核数最优
**答案：错。** 正确表述：线程数经验公式：CPU 密集型约 N+1，IO 密集型约 N×(1+等待时间/计算时间)。原因：CPU 密集多一个线程用于缺页等暂停；IO 密集等待期间可切换线程提高吞吐，实际以压测为准

**Qconcurrency-1297（判断·调优）** IO 密集型线程数越少越好
**答案：错。** 正确表述：线程数经验公式：CPU 密集型约 N+1，IO 密集型约 N×(1+等待时间/计算时间)。原因：CPU 密集多一个线程用于缺页等暂停；IO 密集等待期间可切换线程提高吞吐，实际以压测为准

**Qconcurrency-1298（判断·调优）** 2N 是所有场景的标准答案
**答案：错。** 正确表述：线程数经验公式：CPU 密集型约 N+1，IO 密集型约 N×(1+等待时间/计算时间)。原因：CPU 密集多一个线程用于缺页等暂停；IO 密集等待期间可切换线程提高吞吐，实际以压测为准

**Qconcurrency-1299（场景单选·调优）** 在工程实践中关于「线程数公式」，下列做法符合推荐实践的是？
- A. 按业务类型给初值再压测微调
- B. 2N 是所有场景的标准答案
- C. IO 密集型线程数越少越好
- D. 线程数一律设为 CPU 核数最优
**答案：A**
**解析：** 推荐实践：按业务类型给初值再压测微调。事实依据：线程数经验公式：CPU 密集型约 N+1，IO 密集型约 N×(1+等待时间/计算时间)。

**Qconcurrency-1300（场景判断·调优）** 推荐实践：按业务类型给初值再压测微调
**答案：对。** 解析：线程数经验公式：CPU 密集型约 N+1，IO 密集型约 N×(1+等待时间/计算时间)。原因：CPU 密集多一个线程用于缺页等暂停；IO 密集等待期间可切换线程提高吞吐，实际以压测为准

**Qconcurrency-1301（简答·调优）** 请说明「线程池」中线程数公式的机制与使用要点。
**要点（标准答案）**：① 线程数经验公式：CPU 密集型约 N+1，IO 密集型约 N×(1+等待时间/计算时间)；② 原理：CPU 密集多一个线程用于缺页等暂停；IO 密集等待期间可切换线程提高吞吐，实际以压测为准；③ 使用要点：按业务类型给初值再压测微调。版本锚点：Java Concurrency in Practice。

**Qconcurrency-1302（单选·正向·误用）** 关于「线程池」的说法，正确的是？
- A. submit 会自动打印堆栈
- B. submit 与 execute 异常行为一致
- C. 异常会传播到线程池
- D. submit 提交的任务抛出的异常被 Future 吞掉不打印
**答案：D**
**解析：** submit 提交的任务抛出的异常被 Future 吞掉不打印。原因：execute 直接走线程的 uncaughtExceptionHandler，submit 把异常包进 Future 只有 get 时才拿到，漏 get 则异常静默。
**来源：** JC-035 · 线程池（JDK 源码实测）

**Qconcurrency-1303（判断·误用）** submit 提交的任务抛出的异常被 Future 吞掉不打印
**答案：对。** 解析：execute 直接走线程的 uncaughtExceptionHandler，submit 把异常包进 Future 只有 get 时才拿到，漏 get 则异常静默

**Qconcurrency-1304（判断·误用）** submit 与 execute 异常行为一致
**答案：错。** 正确表述：submit 提交的任务抛出的异常被 Future 吞掉不打印。原因：execute 直接走线程的 uncaughtExceptionHandler，submit 把异常包进 Future 只有 get 时才拿到，漏 get 则异常静默

**Qconcurrency-1305（判断·误用）** submit 会自动打印堆栈
**答案：错。** 正确表述：submit 提交的任务抛出的异常被 Future 吞掉不打印。原因：execute 直接走线程的 uncaughtExceptionHandler，submit 把异常包进 Future 只有 get 时才拿到，漏 get 则异常静默

**Qconcurrency-1306（判断·误用）** 异常会传播到线程池
**答案：错。** 正确表述：submit 提交的任务抛出的异常被 Future 吞掉不打印。原因：execute 直接走线程的 uncaughtExceptionHandler，submit 把异常包进 Future 只有 get 时才拿到，漏 get 则异常静默

**Qconcurrency-1307（场景单选·误用）** 在工程实践中关于「submit」，下列做法符合推荐实践的是？
- A. 有 get 才用 submit，否则 execute 加 UEH 打日志
- B. submit 与 execute 异常行为一致
- C. 异常会传播到线程池
- D. submit 会自动打印堆栈
**答案：A**
**解析：** 推荐实践：有 get 才用 submit，否则 execute 加 UEH 打日志。事实依据：submit 提交的任务抛出的异常被 Future 吞掉不打印。

**Qconcurrency-1308（场景判断·误用）** 推荐实践：有 get 才用 submit，否则 execute 加 UEH 打日志
**答案：对。** 解析：submit 提交的任务抛出的异常被 Future 吞掉不打印。原因：execute 直接走线程的 uncaughtExceptionHandler，submit 把异常包进 Future 只有 get 时才拿到，漏 get 则异常静默

**Qconcurrency-1309（填空·误用）** ______ 提交的任务抛出的异常被 Future 吞掉不打印
**答案：submit**。解析：execute 直接走线程的 uncaughtExceptionHandler，submit 把异常包进 Future 只有 get 时才拿到，漏 get 则异常静默

**Qconcurrency-1310（简答·误用）** 请说明「线程池」中submit的机制与使用要点。
**要点（标准答案）**：① submit 提交的任务抛出的异常被 Future 吞掉不打印；② 原理：execute 直接走线程的 uncaughtExceptionHandler，submit 把异常包进 Future 只有 get 时才拿到，漏 get 则异常静默；③ 使用要点：有 get 才用 submit，否则 execute 加 UEH 打日志。版本锚点：JDK 源码实测。

**Qconcurrency-1311（单选·正向·生命周期）** 关于「线程池」的说法，正确的是？
- A. 调用 shutdown 后线程池立即不可用
- B. shutdownNow 保证所有任务停止
- C. shutdown 会立即中断所有任务
- D. shutdown 后已提交任务继续执行完而 shutdownNow 尝试中断并返回未执行任务
**答案：D**
**解析：** shutdown 后已提交任务继续执行完而 shutdownNow 尝试中断并返回未执行任务。原因：shutdown 拒绝新任务但处理完队列，shutdownNow 遍历中断工作线程，两者都不等任务真正结束，需配合 awaitTermination。
**来源：** JC-036 · 线程池（JDK 文档）

**Qconcurrency-1312（判断·生命周期）** shutdown 后已提交任务继续执行完而 shutdownNow 尝试中断并返回未执行任务
**答案：对。** 解析：shutdown 拒绝新任务但处理完队列，shutdownNow 遍历中断工作线程，两者都不等任务真正结束，需配合 awaitTermination

**Qconcurrency-1313（判断·生命周期）** shutdown 会立即中断所有任务
**答案：错。** 正确表述：shutdown 后已提交任务继续执行完而 shutdownNow 尝试中断并返回未执行任务。原因：shutdown 拒绝新任务但处理完队列，shutdownNow 遍历中断工作线程，两者都不等任务真正结束，需配合 awaitTermination

**Qconcurrency-1314（判断·生命周期）** shutdownNow 保证所有任务停止
**答案：错。** 正确表述：shutdown 后已提交任务继续执行完而 shutdownNow 尝试中断并返回未执行任务。原因：shutdown 拒绝新任务但处理完队列，shutdownNow 遍历中断工作线程，两者都不等任务真正结束，需配合 awaitTermination

**Qconcurrency-1315（判断·生命周期）** 调用 shutdown 后线程池立即不可用
**答案：错。** 正确表述：shutdown 后已提交任务继续执行完而 shutdownNow 尝试中断并返回未执行任务。原因：shutdown 拒绝新任务但处理完队列，shutdownNow 遍历中断工作线程，两者都不等任务真正结束，需配合 awaitTermination

**Qconcurrency-1316（场景单选·生命周期）** 在工程实践中关于「shutdown」，下列做法符合推荐实践的是？
- A. 调用 shutdown 后线程池立即不可用
- B. 优雅停机顺序：shutdown、awaitTermination、shutdownNow 兜底
- C. shutdownNow 保证所有任务停止
- D. shutdown 会立即中断所有任务
**答案：B**
**解析：** 推荐实践：优雅停机顺序：shutdown、awaitTermination、shutdownNow 兜底。事实依据：shutdown 后已提交任务继续执行完而 shutdownNow 尝试中断并返回未执行任务。

**Qconcurrency-1317（场景判断·生命周期）** 推荐实践：优雅停机顺序：shutdown、awaitTermination、shutdownNow 兜底
**答案：对。** 解析：shutdown 后已提交任务继续执行完而 shutdownNow 尝试中断并返回未执行任务。原因：shutdown 拒绝新任务但处理完队列，shutdownNow 遍历中断工作线程，两者都不等任务真正结束，需配合 awaitTermination

**Qconcurrency-1318（填空·生命周期）** ______ 后已提交任务继续执行完而 shutdownNow 尝试中断并返回未执行任务
**答案：shutdown**。解析：shutdown 拒绝新任务但处理完队列，shutdownNow 遍历中断工作线程，两者都不等任务真正结束，需配合 awaitTermination

**Qconcurrency-1319（简答·生命周期）** 请说明「线程池」中shutdown的机制与使用要点。
**要点（标准答案）**：① shutdown 后已提交任务继续执行完而 shutdownNow 尝试中断并返回未执行任务；② 原理：shutdown 拒绝新任务但处理完队列，shutdownNow 遍历中断工作线程，两者都不等任务真正结束，需配合 awaitTermination；③ 使用要点：优雅停机顺序：shutdown、awaitTermination、shutdownNow 兜底。版本锚点：JDK 文档。

**Qconcurrency-1320（单选·正向·运维）** 关于「线程池」的说法，正确的是？
- A. 线程池参数可运行时动态调整（setCorePoolSize 与 setMaximumPoolSize）
- B. setMaximumPoolSize 可以小于当前核心数
- C. 线程池参数创建后不可修改
- D. 动态修改需重启生效
**答案：A**
**解析：** 线程池参数可运行时动态调整（setCorePoolSize 与 setMaximumPoolSize）。原因：ThreadPoolExecutor 内部用 volatile 存参数并支持运行时修改，美团据此实现动态线程池应对大促。
**来源：** JC-037 · 线程池（美团技术博客）

**Qconcurrency-1321（判断·运维）** 线程池参数可运行时动态调整（setCorePoolSize 与 setMaximumPoolSize）
**答案：对。** 解析：ThreadPoolExecutor 内部用 volatile 存参数并支持运行时修改，美团据此实现动态线程池应对大促

**Qconcurrency-1322（判断·运维）** 线程池参数创建后不可修改
**答案：错。** 正确表述：线程池参数可运行时动态调整（setCorePoolSize 与 setMaximumPoolSize）。原因：ThreadPoolExecutor 内部用 volatile 存参数并支持运行时修改，美团据此实现动态线程池应对大促

**Qconcurrency-1323（判断·运维）** 动态修改需重启生效
**答案：错。** 正确表述：线程池参数可运行时动态调整（setCorePoolSize 与 setMaximumPoolSize）。原因：ThreadPoolExecutor 内部用 volatile 存参数并支持运行时修改，美团据此实现动态线程池应对大促

**Qconcurrency-1324（判断·运维）** setMaximumPoolSize 可以小于当前核心数
**答案：错。** 正确表述：线程池参数可运行时动态调整（setCorePoolSize 与 setMaximumPoolSize）。原因：ThreadPoolExecutor 内部用 volatile 存参数并支持运行时修改，美团据此实现动态线程池应对大促

**Qconcurrency-1325（场景单选·运维）** 在工程实践中关于「动态调参」，下列做法符合推荐实践的是？
- A. 线程池参数创建后不可修改
- B. 动态修改需重启生效
- C. 配置中心推送阈值动态伸缩
- D. setMaximumPoolSize 可以小于当前核心数
**答案：C**
**解析：** 推荐实践：配置中心推送阈值动态伸缩。事实依据：线程池参数可运行时动态调整（setCorePoolSize 与 setMaximumPoolSize）。

**Qconcurrency-1326（场景判断·运维）** 推荐实践：配置中心推送阈值动态伸缩
**答案：对。** 解析：线程池参数可运行时动态调整（setCorePoolSize 与 setMaximumPoolSize）。原因：ThreadPoolExecutor 内部用 volatile 存参数并支持运行时修改，美团据此实现动态线程池应对大促

**Qconcurrency-1327（简答·运维）** 请说明「线程池」中动态调参的机制与使用要点。
**要点（标准答案）**：① 线程池参数可运行时动态调整（setCorePoolSize 与 setMaximumPoolSize）；② 原理：ThreadPoolExecutor 内部用 volatile 存参数并支持运行时修改，美团据此实现动态线程池应对大促；③ 使用要点：配置中心推送阈值动态伸缩。版本锚点：美团技术博客。

**Qconcurrency-1328（单选·正向·运维）** 关于「线程池」的说法，正确的是？
- A. 线程池监控看活跃线程数、队列长度与拒绝次数三个核心指标
- B. 线程池监控只需要看线程总数
- C. 队列长度无法获取
- D. 拒绝次数 JDK 自带统计
**答案：A**
**解析：** 线程池监控看活跃线程数、队列长度与拒绝次数三个核心指标。原因：getActiveCount、getQueue().size()、拒绝策略计数（需自行埋点）构成健康度画像，队列增长斜率是过载前兆。
**来源：** JC-038 · 线程池（实战经验）

**Qconcurrency-1329（判断·运维）** 线程池监控看活跃线程数、队列长度与拒绝次数三个核心指标
**答案：对。** 解析：getActiveCount、getQueue().size()、拒绝策略计数（需自行埋点）构成健康度画像，队列增长斜率是过载前兆

**Qconcurrency-1330（判断·运维）** 线程池监控只需要看线程总数
**答案：错。** 正确表述：线程池监控看活跃线程数、队列长度与拒绝次数三个核心指标。原因：getActiveCount、getQueue().size()、拒绝策略计数（需自行埋点）构成健康度画像，队列增长斜率是过载前兆

**Qconcurrency-1331（判断·运维）** 队列长度无法获取
**答案：错。** 正确表述：线程池监控看活跃线程数、队列长度与拒绝次数三个核心指标。原因：getActiveCount、getQueue().size()、拒绝策略计数（需自行埋点）构成健康度画像，队列增长斜率是过载前兆

**Qconcurrency-1332（判断·运维）** 拒绝次数 JDK 自带统计
**答案：错。** 正确表述：线程池监控看活跃线程数、队列长度与拒绝次数三个核心指标。原因：getActiveCount、getQueue().size()、拒绝策略计数（需自行埋点）构成健康度画像，队列增长斜率是过载前兆

**Qconcurrency-1333（场景单选·运维）** 在工程实践中关于「监控」，下列做法符合推荐实践的是？
- A. 队列长度无法获取
- B. 拒绝次数 JDK 自带统计
- C. 线程池监控只需要看线程总数
- D. 接入监控大盘告警队列积压
**答案：D**
**解析：** 推荐实践：接入监控大盘告警队列积压。事实依据：线程池监控看活跃线程数、队列长度与拒绝次数三个核心指标。

**Qconcurrency-1334（场景判断·运维）** 推荐实践：接入监控大盘告警队列积压
**答案：对。** 解析：线程池监控看活跃线程数、队列长度与拒绝次数三个核心指标。原因：getActiveCount、getQueue().size()、拒绝策略计数（需自行埋点）构成健康度画像，队列增长斜率是过载前兆

**Qconcurrency-1335（填空·运维）** 线程池______看活跃线程数、队列长度与拒绝次数三个核心指标
**答案：监控**。解析：getActiveCount、getQueue().size()、拒绝策略计数（需自行埋点）构成健康度画像，队列增长斜率是过载前兆

**Qconcurrency-1336（简答·运维）** 请说明「线程池」中监控的机制与使用要点。
**要点（标准答案）**：① 线程池监控看活跃线程数、队列长度与拒绝次数三个核心指标；② 原理：getActiveCount、getQueue().size()、拒绝策略计数（需自行埋点）构成健康度画像，队列增长斜率是过载前兆；③ 使用要点：接入监控大盘告警队列积压。版本锚点：实战经验。

**Qconcurrency-1337（单选·正向·误用）** 关于「线程池」的说法，正确的是？
- A. 线程名默认包含业务信息
- B. ThreadFactory 参数可传 null
- C. 线程池必须通过 ThreadFactory 给线程命名
- D. 命名只是美观不影响排查
**答案：C**
**解析：** 线程池必须通过 ThreadFactory 给线程命名。原因：默认线程名 pool-1-thread-N 无法定位问题，命名规则建议业务-pool-序号，dump 分析时一眼归因。
**来源：** JC-039 · 线程池（阿里手册）

**Qconcurrency-1338（判断·误用）** 线程池必须通过 ThreadFactory 给线程命名
**答案：对。** 解析：默认线程名 pool-1-thread-N 无法定位问题，命名规则建议业务-pool-序号，dump 分析时一眼归因

**Qconcurrency-1339（判断·误用）** 线程名默认包含业务信息
**答案：错。** 正确表述：线程池必须通过 ThreadFactory 给线程命名。原因：默认线程名 pool-1-thread-N 无法定位问题，命名规则建议业务-pool-序号，dump 分析时一眼归因

**Qconcurrency-1340（判断·误用）** 命名只是美观不影响排查
**答案：错。** 正确表述：线程池必须通过 ThreadFactory 给线程命名。原因：默认线程名 pool-1-thread-N 无法定位问题，命名规则建议业务-pool-序号，dump 分析时一眼归因

**Qconcurrency-1341（判断·误用）** ThreadFactory 参数可传 null
**答案：错。** 正确表述：线程池必须通过 ThreadFactory 给线程命名。原因：默认线程名 pool-1-thread-N 无法定位问题，命名规则建议业务-pool-序号，dump 分析时一眼归因

**Qconcurrency-1342（场景单选·误用）** 在工程实践中关于「ThreadFactory」，下列做法符合推荐实践的是？
- A. 线程名默认包含业务信息
- B. 所有线程池统一命名规范
- C. ThreadFactory 参数可传 null
- D. 命名只是美观不影响排查
**答案：B**
**解析：** 推荐实践：所有线程池统一命名规范。事实依据：线程池必须通过 ThreadFactory 给线程命名。

**Qconcurrency-1343（场景判断·误用）** 推荐实践：所有线程池统一命名规范
**答案：对。** 解析：线程池必须通过 ThreadFactory 给线程命名。原因：默认线程名 pool-1-thread-N 无法定位问题，命名规则建议业务-pool-序号，dump 分析时一眼归因

**Qconcurrency-1344（填空·误用）** 线程池必须通过 ______ 给线程命名
**答案：ThreadFactory**。解析：默认线程名 pool-1-thread-N 无法定位问题，命名规则建议业务-pool-序号，dump 分析时一眼归因

**Qconcurrency-1345（简答·误用）** 请说明「线程池」中ThreadFactory的机制与使用要点。
**要点（标准答案）**：① 线程池必须通过 ThreadFactory 给线程命名；② 原理：默认线程名 pool-1-thread-N 无法定位问题，命名规则建议业务-pool-序号，dump 分析时一眼归因；③ 使用要点：所有线程池统一命名规范。版本锚点：阿里手册。

**Qconcurrency-1346（单选·正向·实现）** 关于「阻塞队列」的说法，正确的是？
- A. 它默认有界
- B. 无界时队列满会拒绝任务
- C. LinkedBlockingQueue 不传容量参数时容量为 Integer.MAX_VALUE
- D. LinkedBlockingQueue 默认容量是 10
**答案：C**
**解析：** LinkedBlockingQueue 不传容量参数时容量为 Integer.MAX_VALUE。原因：两把锁分离读写提高并发但默认容量形同无界，用在 newFixedThreadPool 就是 OOM 根源。
**来源：** JC-040 · 阻塞队列（JDK 源码）

**Qconcurrency-1347（判断·实现）** LinkedBlockingQueue 不传容量参数时容量为 Integer.MAX_VALUE
**答案：对。** 解析：两把锁分离读写提高并发但默认容量形同无界，用在 newFixedThreadPool 就是 OOM 根源

**Qconcurrency-1348（判断·实现）** LinkedBlockingQueue 默认容量是 10
**答案：错。** 正确表述：LinkedBlockingQueue 不传容量参数时容量为 Integer.MAX_VALUE。原因：两把锁分离读写提高并发但默认容量形同无界，用在 newFixedThreadPool 就是 OOM 根源

**Qconcurrency-1349（判断·实现）** 它默认有界
**答案：错。** 正确表述：LinkedBlockingQueue 不传容量参数时容量为 Integer.MAX_VALUE。原因：两把锁分离读写提高并发但默认容量形同无界，用在 newFixedThreadPool 就是 OOM 根源

**Qconcurrency-1350（判断·实现）** 无界时队列满会拒绝任务
**答案：错。** 正确表述：LinkedBlockingQueue 不传容量参数时容量为 Integer.MAX_VALUE。原因：两把锁分离读写提高并发但默认容量形同无界，用在 newFixedThreadPool 就是 OOM 根源

**Qconcurrency-1351（场景单选·实现）** 在工程实践中关于「LinkedBlockingQueue」，下列做法符合推荐实践的是？
- A. 无界时队列满会拒绝任务
- B. 当业务队列必须显式传容量
- C. LinkedBlockingQueue 默认容量是 10
- D. 它默认有界
**答案：B**
**解析：** 推荐实践：当业务队列必须显式传容量。事实依据：LinkedBlockingQueue 不传容量参数时容量为 Integer.MAX_VALUE。

**Qconcurrency-1352（场景判断·实现）** 推荐实践：当业务队列必须显式传容量
**答案：对。** 解析：LinkedBlockingQueue 不传容量参数时容量为 Integer.MAX_VALUE。原因：两把锁分离读写提高并发但默认容量形同无界，用在 newFixedThreadPool 就是 OOM 根源

**Qconcurrency-1353（填空·实现）** ______ 不传容量参数时容量为 Integer.MAX_VALUE
**答案：LinkedBlockingQueue**。解析：两把锁分离读写提高并发但默认容量形同无界，用在 newFixedThreadPool 就是 OOM 根源

**Qconcurrency-1354（简答·实现）** 请说明「阻塞队列」中LinkedBlockingQueue的机制与使用要点。
**要点（标准答案）**：① LinkedBlockingQueue 不传容量参数时容量为 Integer.MAX_VALUE；② 原理：两把锁分离读写提高并发但默认容量形同无界，用在 newFixedThreadPool 就是 OOM 根源；③ 使用要点：当业务队列必须显式传容量。版本锚点：JDK 源码。

**Qconcurrency-1355（单选·正向·实现）** 关于「阻塞队列」的说法，正确的是？
- A. 它比 LinkedBlockingQueue 并发更高
- B. ArrayBlockingQueue 读写两把锁
- C. 容量可以动态增长
- D. ArrayBlockingQueue 是单锁有界数组队列
**答案：D**
**解析：** ArrayBlockingQueue 是单锁有界数组队列。原因：读写共用一把锁，容量构造时固定，支持公平模式，与 Linked 双锁版本并发度不同。
**来源：** JC-041 · 阻塞队列（JDK 源码）

**Qconcurrency-1356（判断·实现）** ArrayBlockingQueue 是单锁有界数组队列
**答案：对。** 解析：读写共用一把锁，容量构造时固定，支持公平模式，与 Linked 双锁版本并发度不同

**Qconcurrency-1357（判断·实现）** ArrayBlockingQueue 读写两把锁
**答案：错。** 正确表述：ArrayBlockingQueue 是单锁有界数组队列。原因：读写共用一把锁，容量构造时固定，支持公平模式，与 Linked 双锁版本并发度不同

**Qconcurrency-1358（判断·实现）** 容量可以动态增长
**答案：错。** 正确表述：ArrayBlockingQueue 是单锁有界数组队列。原因：读写共用一把锁，容量构造时固定，支持公平模式，与 Linked 双锁版本并发度不同

**Qconcurrency-1359（判断·实现）** 它比 LinkedBlockingQueue 并发更高
**答案：错。** 正确表述：ArrayBlockingQueue 是单锁有界数组队列。原因：读写共用一把锁，容量构造时固定，支持公平模式，与 Linked 双锁版本并发度不同

**Qconcurrency-1360（场景单选·实现）** 在工程实践中关于「ArrayBlockingQueue」，下列做法符合推荐实践的是？
- A. 它比 LinkedBlockingQueue 并发更高
- B. ArrayBlockingQueue 读写两把锁
- C. 容量可以动态增长
- D. 有界队列首选之一，容量固定场景
**答案：D**
**解析：** 推荐实践：有界队列首选之一，容量固定场景。事实依据：ArrayBlockingQueue 是单锁有界数组队列。

**Qconcurrency-1361（场景判断·实现）** 推荐实践：有界队列首选之一，容量固定场景
**答案：对。** 解析：ArrayBlockingQueue 是单锁有界数组队列。原因：读写共用一把锁，容量构造时固定，支持公平模式，与 Linked 双锁版本并发度不同

**Qconcurrency-1362（填空·实现）** ______ 是单锁有界数组队列
**答案：ArrayBlockingQueue**。解析：读写共用一把锁，容量构造时固定，支持公平模式，与 Linked 双锁版本并发度不同

**Qconcurrency-1363（简答·实现）** 请说明「阻塞队列」中ArrayBlockingQueue的机制与使用要点。
**要点（标准答案）**：① ArrayBlockingQueue 是单锁有界数组队列；② 原理：读写共用一把锁，容量构造时固定，支持公平模式，与 Linked 双锁版本并发度不同；③ 使用要点：有界队列首选之一，容量固定场景。版本锚点：JDK 源码。

**Qconcurrency-1364（单选·正向·实现）** 关于「阻塞队列」的说法，正确的是？
- A. put 会先暂存在队列中
- B. 适合任务缓冲场景
- C. SynchronousQueue 容量是 1
- D. SynchronousQueue 没有容量每个 put 必须等 take 直接交接
**答案：D**
**解析：** SynchronousQueue 没有容量每个 put 必须等 take 直接交接。原因：不存储元素，newCachedThreadPool 用它实现来一个任务建一个线程的设计。
**来源：** JC-042 · 阻塞队列（JDK 文档）

**Qconcurrency-1365（判断·实现）** SynchronousQueue 没有容量每个 put 必须等 take 直接交接
**答案：对。** 解析：不存储元素，newCachedThreadPool 用它实现来一个任务建一个线程的设计

**Qconcurrency-1366（判断·实现）** SynchronousQueue 容量是 1
**答案：错。** 正确表述：SynchronousQueue 没有容量每个 put 必须等 take 直接交接。原因：不存储元素，newCachedThreadPool 用它实现来一个任务建一个线程的设计

**Qconcurrency-1367（判断·实现）** put 会先暂存在队列中
**答案：错。** 正确表述：SynchronousQueue 没有容量每个 put 必须等 take 直接交接。原因：不存储元素，newCachedThreadPool 用它实现来一个任务建一个线程的设计

**Qconcurrency-1368（判断·实现）** 适合任务缓冲场景
**答案：错。** 正确表述：SynchronousQueue 没有容量每个 put 必须等 take 直接交接。原因：不存储元素，newCachedThreadPool 用它实现来一个任务建一个线程的设计

**Qconcurrency-1369（场景单选·实现）** 在工程实践中关于「SynchronousQueue」，下列做法符合推荐实践的是？
- A. put 会先暂存在队列中
- B. 适合任务缓冲场景
- C. SynchronousQueue 容量是 1
- D. 线程池需要快速扩张时选用
**答案：D**
**解析：** 推荐实践：线程池需要快速扩张时选用。事实依据：SynchronousQueue 没有容量每个 put 必须等 take 直接交接。

**Qconcurrency-1370（场景判断·实现）** 推荐实践：线程池需要快速扩张时选用
**答案：对。** 解析：SynchronousQueue 没有容量每个 put 必须等 take 直接交接。原因：不存储元素，newCachedThreadPool 用它实现来一个任务建一个线程的设计

**Qconcurrency-1371（填空·实现）** ______ 没有容量每个 put 必须等 take 直接交接
**答案：SynchronousQueue**。解析：不存储元素，newCachedThreadPool 用它实现来一个任务建一个线程的设计

**Qconcurrency-1372（简答·实现）** 请说明「阻塞队列」中SynchronousQueue的机制与使用要点。
**要点（标准答案）**：① SynchronousQueue 没有容量每个 put 必须等 take 直接交接；② 原理：不存储元素，newCachedThreadPool 用它实现来一个任务建一个线程的设计；③ 使用要点：线程池需要快速扩张时选用。版本锚点：JDK 文档。

**Qconcurrency-1373（单选·正向·实现）** 关于「阻塞队列」的说法，正确的是？
- A. 元素自动在到期时被删除
- B. DelayQueue 按到期时间出队元素必须实现 Delayed 接口
- C. DelayQueue 按 FIFO 出队
- D. 不需要实现任何接口
**答案：B**
**解析：** DelayQueue 按到期时间出队元素必须实现 Delayed 接口。原因：内部优先堆按剩余延迟排序，take 阻塞到队首到期，用于订单超时关单等延迟任务（小规模方案，大规模用时间轮或 RocketMQ 延迟消息）。
**来源：** JC-043 · 阻塞队列（JDK 文档）

**Qconcurrency-1374（判断·实现）** DelayQueue 按到期时间出队元素必须实现 Delayed 接口
**答案：对。** 解析：内部优先堆按剩余延迟排序，take 阻塞到队首到期，用于订单超时关单等延迟任务（小规模方案，大规模用时间轮或 RocketMQ 延迟消息）

**Qconcurrency-1375（判断·实现）** DelayQueue 按 FIFO 出队
**答案：错。** 正确表述：DelayQueue 按到期时间出队元素必须实现 Delayed 接口。原因：内部优先堆按剩余延迟排序，take 阻塞到队首到期，用于订单超时关单等延迟任务（小规模方案，大规模用时间轮或 RocketMQ 延迟消息）

**Qconcurrency-1376（判断·实现）** 元素自动在到期时被删除
**答案：错。** 正确表述：DelayQueue 按到期时间出队元素必须实现 Delayed 接口。原因：内部优先堆按剩余延迟排序，take 阻塞到队首到期，用于订单超时关单等延迟任务（小规模方案，大规模用时间轮或 RocketMQ 延迟消息）

**Qconcurrency-1377（判断·实现）** 不需要实现任何接口
**答案：错。** 正确表述：DelayQueue 按到期时间出队元素必须实现 Delayed 接口。原因：内部优先堆按剩余延迟排序，take 阻塞到队首到期，用于订单超时关单等延迟任务（小规模方案，大规模用时间轮或 RocketMQ 延迟消息）

**Qconcurrency-1378（场景单选·实现）** 在工程实践中关于「DelayQueue」，下列做法符合推荐实践的是？
- A. DelayQueue 按 FIFO 出队
- B. 订单超时关闭的小规模实现
- C. 元素自动在到期时被删除
- D. 不需要实现任何接口
**答案：B**
**解析：** 推荐实践：订单超时关闭的小规模实现。事实依据：DelayQueue 按到期时间出队元素必须实现 Delayed 接口。

**Qconcurrency-1379（场景判断·实现）** 推荐实践：订单超时关闭的小规模实现
**答案：对。** 解析：DelayQueue 按到期时间出队元素必须实现 Delayed 接口。原因：内部优先堆按剩余延迟排序，take 阻塞到队首到期，用于订单超时关单等延迟任务（小规模方案，大规模用时间轮或 RocketMQ 延迟消息）

**Qconcurrency-1380（填空·实现）** ______ 按到期时间出队元素必须实现 Delayed 接口
**答案：DelayQueue**。解析：内部优先堆按剩余延迟排序，take 阻塞到队首到期，用于订单超时关单等延迟任务（小规模方案，大规模用时间轮或 RocketMQ 延迟消息）

**Qconcurrency-1381（简答·实现）** 请说明「阻塞队列」中DelayQueue的机制与使用要点。
**要点（标准答案）**：① DelayQueue 按到期时间出队元素必须实现 Delayed 接口；② 原理：内部优先堆按剩余延迟排序，take 阻塞到队首到期，用于订单超时关单等延迟任务（小规模方案，大规模用时间轮或 RocketMQ 延迟消息）；③ 使用要点：订单超时关闭的小规模实现。版本锚点：JDK 文档。

**Qconcurrency-1382（单选·正向·原子性）** 关于「CAS」的说法，正确的是？
- A. CAS 依赖 CPU 的原子比较交换指令（x86 上 cmpxchg 配 lock 前缀）
- B. CAS 需要操作系统内核参与
- C. cmpxchg 单独使用不带 lock 前缀也是原子的
- D. CAS 是 JVM 软件实现的锁机制
**答案：A**
**解析：** CAS 依赖 CPU 的原子比较交换指令（x86 上 cmpxchg 配 lock 前缀）。原因：Java 通过 Unsafe 调用硬件原子指令，失败则自旋重试，全程无锁，JDK9 后推荐 VarHandle。
**来源：** JC-044 · CAS（x86 手册）

**Qconcurrency-1383（判断·原子性）** CAS 依赖 CPU 的原子比较交换指令（x86 上 cmpxchg 配 lock 前缀）
**答案：对。** 解析：Java 通过 Unsafe 调用硬件原子指令，失败则自旋重试，全程无锁，JDK9 后推荐 VarHandle

**Qconcurrency-1384（判断·原子性）** CAS 是 JVM 软件实现的锁机制
**答案：错。** 正确表述：CAS 依赖 CPU 的原子比较交换指令（x86 上 cmpxchg 配 lock 前缀）。原因：Java 通过 Unsafe 调用硬件原子指令，失败则自旋重试，全程无锁，JDK9 后推荐 VarHandle

**Qconcurrency-1385（判断·原子性）** CAS 需要操作系统内核参与
**答案：错。** 正确表述：CAS 依赖 CPU 的原子比较交换指令（x86 上 cmpxchg 配 lock 前缀）。原因：Java 通过 Unsafe 调用硬件原子指令，失败则自旋重试，全程无锁，JDK9 后推荐 VarHandle

**Qconcurrency-1386（判断·原子性）** cmpxchg 单独使用不带 lock 前缀也是原子的
**答案：错。** 正确表述：CAS 依赖 CPU 的原子比较交换指令（x86 上 cmpxchg 配 lock 前缀）。原因：Java 通过 Unsafe 调用硬件原子指令，失败则自旋重试，全程无锁，JDK9 后推荐 VarHandle

**Qconcurrency-1387（场景单选·原子性）** 在工程实践中关于「cmpxchg」，下列做法符合推荐实践的是？
- A. CAS 是 JVM 软件实现的锁机制
- B. cmpxchg 单独使用不带 lock 前缀也是原子的
- C. CAS 需要操作系统内核参与
- D. 谈无锁编程先落到硬件原子指令
**答案：D**
**解析：** 推荐实践：谈无锁编程先落到硬件原子指令。事实依据：CAS 依赖 CPU 的原子比较交换指令（x86 上 cmpxchg 配 lock 前缀）。

**Qconcurrency-1388（场景判断·原子性）** 推荐实践：谈无锁编程先落到硬件原子指令
**答案：对。** 解析：CAS 依赖 CPU 的原子比较交换指令（x86 上 cmpxchg 配 lock 前缀）。原因：Java 通过 Unsafe 调用硬件原子指令，失败则自旋重试，全程无锁，JDK9 后推荐 VarHandle

**Qconcurrency-1389（填空·原子性）** CAS 依赖 CPU 的原子比较交换指令（x86 上 ______ 配 lock 前缀）
**答案：cmpxchg**。解析：Java 通过 Unsafe 调用硬件原子指令，失败则自旋重试，全程无锁，JDK9 后推荐 VarHandle

**Qconcurrency-1390（简答·原子性）** 请说明「CAS」中cmpxchg的机制与使用要点。
**要点（标准答案）**：① CAS 依赖 CPU 的原子比较交换指令（x86 上 cmpxchg 配 lock 前缀）；② 原理：Java 通过 Unsafe 调用硬件原子指令，失败则自旋重试，全程无锁，JDK9 后推荐 VarHandle；③ 使用要点：谈无锁编程先落到硬件原子指令。版本锚点：x86 手册。

**Qconcurrency-1391（单选·正向·误用）** 关于「CAS」的说法，正确的是？
- A. AtomicReference 天然防 ABA
- B. AtomicLong 能解决 ABA
- C. CAS 存在 ABA 问题：值从 A 改回 A 时 CAS 无法察觉
- D. ABA 在 Java 中不可能发生
**答案：C**
**解析：** CAS 存在 ABA 问题：值从 A 改回 A 时 CAS 无法察觉。原因：解决方式是加版本号，AtomicStampedReference 维护引用加 stamp 二元组，数据库乐观锁 version 字段同理。
**来源：** JC-045 · CAS（学术与实战共识）

**Qconcurrency-1392（判断·误用）** CAS 存在 ABA 问题：值从 A 改回 A 时 CAS 无法察觉
**答案：对。** 解析：解决方式是加版本号，AtomicStampedReference 维护引用加 stamp 二元组，数据库乐观锁 version 字段同理

**Qconcurrency-1393（判断·误用）** AtomicLong 能解决 ABA
**答案：错。** 正确表述：CAS 存在 ABA 问题：值从 A 改回 A 时 CAS 无法察觉。原因：解决方式是加版本号，AtomicStampedReference 维护引用加 stamp 二元组，数据库乐观锁 version 字段同理

**Qconcurrency-1394（判断·误用）** ABA 在 Java 中不可能发生
**答案：错。** 正确表述：CAS 存在 ABA 问题：值从 A 改回 A 时 CAS 无法察觉。原因：解决方式是加版本号，AtomicStampedReference 维护引用加 stamp 二元组，数据库乐观锁 version 字段同理

**Qconcurrency-1395（判断·误用）** AtomicReference 天然防 ABA
**答案：错。** 正确表述：CAS 存在 ABA 问题：值从 A 改回 A 时 CAS 无法察觉。原因：解决方式是加版本号，AtomicStampedReference 维护引用加 stamp 二元组，数据库乐观锁 version 字段同理

**Qconcurrency-1396（场景单选·误用）** 在工程实践中关于「ABA」，下列做法符合推荐实践的是？
- A. AtomicReference 天然防 ABA
- B. AtomicLong 能解决 ABA
- C. ABA 在 Java 中不可能发生
- D. 链表类无锁结构必须防 ABA
**答案：D**
**解析：** 推荐实践：链表类无锁结构必须防 ABA。事实依据：CAS 存在 ABA 问题：值从 A 改回 A 时 CAS 无法察觉。

**Qconcurrency-1397（场景判断·误用）** 推荐实践：链表类无锁结构必须防 ABA
**答案：对。** 解析：CAS 存在 ABA 问题：值从 A 改回 A 时 CAS 无法察觉。原因：解决方式是加版本号，AtomicStampedReference 维护引用加 stamp 二元组，数据库乐观锁 version 字段同理

**Qconcurrency-1398（填空·误用）** CAS 存在 ______ 问题：值从 A 改回 A 时 CAS 无法察觉
**答案：ABA**。解析：解决方式是加版本号，AtomicStampedReference 维护引用加 stamp 二元组，数据库乐观锁 version 字段同理

**Qconcurrency-1399（简答·误用）** 请说明「CAS」中ABA的机制与使用要点。
**要点（标准答案）**：① CAS 存在 ABA 问题：值从 A 改回 A 时 CAS 无法察觉；② 原理：解决方式是加版本号，AtomicStampedReference 维护引用加 stamp 二元组，数据库乐观锁 version 字段同理；③ 使用要点：链表类无锁结构必须防 ABA。版本锚点：学术与实战共识。

**Qconcurrency-1400（单选·正向·性能）** 关于「原子类」的说法，正确的是？
- A. LongAdder 在任何场景都快于 AtomicLong
- B. LongAdder 也能 replace 原子读改写
- C. 高竞争计数用 LongAdder 而非 AtomicLong
- D. LongAdder 的 sum 是精确强一致快照
**答案：C**
**解析：** 高竞争计数用 LongAdder 而非 AtomicLong。原因：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级。
**来源：** JC-046 · 原子类（JDK 文档）

**Qconcurrency-1401（判断·性能）** 高竞争计数用 LongAdder 而非 AtomicLong
**答案：对。** 解析：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级

**Qconcurrency-1402（判断·性能）** LongAdder 在任何场景都快于 AtomicLong
**答案：错。** 正确表述：高竞争计数用 LongAdder 而非 AtomicLong。原因：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级

**Qconcurrency-1403（判断·性能）** LongAdder 的 sum 是精确强一致快照
**答案：错。** 正确表述：高竞争计数用 LongAdder 而非 AtomicLong。原因：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级

**Qconcurrency-1404（判断·性能）** LongAdder 也能 replace 原子读改写
**答案：错。** 正确表述：高竞争计数用 LongAdder 而非 AtomicLong。原因：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级

**Qconcurrency-1405（场景单选·性能）** 在工程实践中关于「LongAdder」，下列做法符合推荐实践的是？
- A. 纯计数（QPS 统计）用 LongAdder
- B. LongAdder 的 sum 是精确强一致快照
- C. LongAdder 也能 replace 原子读改写
- D. LongAdder 在任何场景都快于 AtomicLong
**答案：A**
**解析：** 推荐实践：纯计数（QPS 统计）用 LongAdder。事实依据：高竞争计数用 LongAdder 而非 AtomicLong。

**Qconcurrency-1406（场景判断·性能）** 推荐实践：纯计数（QPS 统计）用 LongAdder
**答案：对。** 解析：高竞争计数用 LongAdder 而非 AtomicLong。原因：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级

**Qconcurrency-1407（填空·性能）** 高竞争计数用 ______ 而非 AtomicLong
**答案：LongAdder**。解析：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级

**Qconcurrency-1408（简答·性能）** 请说明「原子类」中LongAdder的机制与使用要点。
**要点（标准答案）**：① 高竞争计数用 LongAdder 而非 AtomicLong；② 原理：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级；③ 使用要点：纯计数（QPS 统计）用 LongAdder。版本锚点：JDK 文档。

**Qconcurrency-1409（单选·正向·语义）** 关于「原子类」的说法，正确的是？
- A. VarHandle 与 AtomicInteger 能力不同级
- B. JDK9 引入 VarHandle 替代 Unsafe 提供安全的字段级原子操作
- C. Unsafe 在 JDK9 后被删除
- D. VarHandle 只能读写字段
**答案：B**
**解析：** JDK9 引入 VarHandle 替代 Unsafe 提供安全的字段级原子操作。原因：提供 getAndSet、compareAndSet、getAndAddRelease 等带内存语义的方法，且模块系统下不依赖内部 API。
**来源：** JC-047 · 原子类（JEP 193）

**Qconcurrency-1410（判断·语义）** JDK9 引入 VarHandle 替代 Unsafe 提供安全的字段级原子操作
**答案：对。** 解析：提供 getAndSet、compareAndSet、getAndAddRelease 等带内存语义的方法，且模块系统下不依赖内部 API

**Qconcurrency-1411（判断·语义）** VarHandle 只能读写字段
**答案：错。** 正确表述：JDK9 引入 VarHandle 替代 Unsafe 提供安全的字段级原子操作。原因：提供 getAndSet、compareAndSet、getAndAddRelease 等带内存语义的方法，且模块系统下不依赖内部 API

**Qconcurrency-1412（判断·语义）** Unsafe 在 JDK9 后被删除
**答案：错。** 正确表述：JDK9 引入 VarHandle 替代 Unsafe 提供安全的字段级原子操作。原因：提供 getAndSet、compareAndSet、getAndAddRelease 等带内存语义的方法，且模块系统下不依赖内部 API

**Qconcurrency-1413（判断·语义）** VarHandle 与 AtomicInteger 能力不同级
**答案：错。** 正确表述：JDK9 引入 VarHandle 替代 Unsafe 提供安全的字段级原子操作。原因：提供 getAndSet、compareAndSet、getAndAddRelease 等带内存语义的方法，且模块系统下不依赖内部 API

**Qconcurrency-1414（场景单选·语义）** 在工程实践中关于「VarHandle」，下列做法符合推荐实践的是？
- A. 新代码用 VarHandle 与 MethodHandles
- B. VarHandle 只能读写字段
- C. VarHandle 与 AtomicInteger 能力不同级
- D. Unsafe 在 JDK9 后被删除
**答案：A**
**解析：** 推荐实践：新代码用 VarHandle 与 MethodHandles。事实依据：JDK9 引入 VarHandle 替代 Unsafe 提供安全的字段级原子操作。

**Qconcurrency-1415（场景判断·语义）** 推荐实践：新代码用 VarHandle 与 MethodHandles
**答案：对。** 解析：JDK9 引入 VarHandle 替代 Unsafe 提供安全的字段级原子操作。原因：提供 getAndSet、compareAndSet、getAndAddRelease 等带内存语义的方法，且模块系统下不依赖内部 API

**Qconcurrency-1416（填空·语义）** JDK9 引入 ______ 替代 Unsafe 提供安全的字段级原子操作
**答案：VarHandle**。解析：提供 getAndSet、compareAndSet、getAndAddRelease 等带内存语义的方法，且模块系统下不依赖内部 API

**Qconcurrency-1417（简答·语义）** 请说明「原子类」中VarHandle的机制与使用要点。
**要点（标准答案）**：① JDK9 引入 VarHandle 替代 Unsafe 提供安全的字段级原子操作；② 原理：提供 getAndSet、compareAndSet、getAndAddRelease 等带内存语义的方法，且模块系统下不依赖内部 API；③ 使用要点：新代码用 VarHandle 与 MethodHandles。版本锚点：JEP 193。

**Qconcurrency-1418（单选·正向·实现）** 关于「AQS」的说法，正确的是？
- A. AQS 核心是一个 volatile int state 加 CLH 变体等待队列
- B. AQS 的队列是无锁链表
- C. state 是普通 int 不需要 volatile
- D. AQS 内部用 HashMap 管理等待线程
**答案：A**
**解析：** AQS 核心是一个 volatile int state 加 CLH 变体等待队列。原因：获取失败的线程封装成 Node 入队 park，释放时唤醒队首后继；state 语义由子类定义（重入次数、许可数、闩计数）。
**来源：** JC-048 · AQS（JDK 源码）

**Qconcurrency-1419（判断·实现）** AQS 核心是一个 volatile int state 加 CLH 变体等待队列
**答案：对。** 解析：获取失败的线程封装成 Node 入队 park，释放时唤醒队首后继；state 语义由子类定义（重入次数、许可数、闩计数）

**Qconcurrency-1420（判断·实现）** AQS 内部用 HashMap 管理等待线程
**答案：错。** 正确表述：AQS 核心是一个 volatile int state 加 CLH 变体等待队列。原因：获取失败的线程封装成 Node 入队 park，释放时唤醒队首后继；state 语义由子类定义（重入次数、许可数、闩计数）

**Qconcurrency-1421（判断·实现）** AQS 的队列是无锁链表
**答案：错。** 正确表述：AQS 核心是一个 volatile int state 加 CLH 变体等待队列。原因：获取失败的线程封装成 Node 入队 park，释放时唤醒队首后继；state 语义由子类定义（重入次数、许可数、闩计数）

**Qconcurrency-1422（判断·实现）** state 是普通 int 不需要 volatile
**答案：错。** 正确表述：AQS 核心是一个 volatile int state 加 CLH 变体等待队列。原因：获取失败的线程封装成 Node 入队 park，释放时唤醒队首后继；state 语义由子类定义（重入次数、许可数、闩计数）

**Qconcurrency-1423（场景单选·实现）** 在工程实践中关于「state」，下列做法符合推荐实践的是？
- A. AQS 的队列是无锁链表
- B. AQS 内部用 HashMap 管理等待线程
- C. state 是普通 int 不需要 volatile
- D. 实现自定义同步器直接复用 AQS
**答案：D**
**解析：** 推荐实践：实现自定义同步器直接复用 AQS。事实依据：AQS 核心是一个 volatile int state 加 CLH 变体等待队列。

**Qconcurrency-1424（场景判断·实现）** 推荐实践：实现自定义同步器直接复用 AQS
**答案：对。** 解析：AQS 核心是一个 volatile int state 加 CLH 变体等待队列。原因：获取失败的线程封装成 Node 入队 park，释放时唤醒队首后继；state 语义由子类定义（重入次数、许可数、闩计数）

**Qconcurrency-1425（填空·实现）** AQS 核心是一个 volatile int ______ 加 CLH 变体等待队列
**答案：state**。解析：获取失败的线程封装成 Node 入队 park，释放时唤醒队首后继；state 语义由子类定义（重入次数、许可数、闩计数）

**Qconcurrency-1426（简答·实现）** 请说明「AQS」中state的机制与使用要点。
**要点（标准答案）**：① AQS 核心是一个 volatile int state 加 CLH 变体等待队列；② 原理：获取失败的线程封装成 Node 入队 park，释放时唤醒队首后继；state 语义由子类定义（重入次数、许可数、闩计数）；③ 使用要点：实现自定义同步器直接复用 AQS。版本锚点：JDK 源码。

**Qconcurrency-1427（单选·正向·版本）** 关于「AQS」的说法，正确的是？
- A. AQS 在 JDK15 完成内部重构对外语义不变
- B. AQS 从未重构过
- C. 重构导致 ReentrantLock 语义变化
- D. JDK15 重构改变了 AQS 的对外 API
**答案：A**
**解析：** AQS 在 JDK15 完成内部重构对外语义不变。原因：新实现简化等待节点状态机与唤醒路径，性能与可维护性提升，网络流传的旧版源码逐行讲解已过时。
**来源：** JC-049 · AQS（JDK 15 release notes）

**Qconcurrency-1428（判断·版本）** AQS 在 JDK15 完成内部重构对外语义不变
**答案：对。** 解析：新实现简化等待节点状态机与唤醒路径，性能与可维护性提升，网络流传的旧版源码逐行讲解已过时

**Qconcurrency-1429（判断·版本）** AQS 从未重构过
**答案：错。** 正确表述：AQS 在 JDK15 完成内部重构对外语义不变。原因：新实现简化等待节点状态机与唤醒路径，性能与可维护性提升，网络流传的旧版源码逐行讲解已过时

**Qconcurrency-1430（判断·版本）** JDK15 重构改变了 AQS 的对外 API
**答案：错。** 正确表述：AQS 在 JDK15 完成内部重构对外语义不变。原因：新实现简化等待节点状态机与唤醒路径，性能与可维护性提升，网络流传的旧版源码逐行讲解已过时

**Qconcurrency-1431（判断·版本）** 重构导致 ReentrantLock 语义变化
**答案：错。** 正确表述：AQS 在 JDK15 完成内部重构对外语义不变。原因：新实现简化等待节点状态机与唤醒路径，性能与可维护性提升，网络流传的旧版源码逐行讲解已过时

**Qconcurrency-1432（场景单选·版本）** 在工程实践中关于「JDK15」，下列做法符合推荐实践的是？
- A. 讲源码前先确认 JDK 版本
- B. AQS 从未重构过
- C. JDK15 重构改变了 AQS 的对外 API
- D. 重构导致 ReentrantLock 语义变化
**答案：A**
**解析：** 推荐实践：讲源码前先确认 JDK 版本。事实依据：AQS 在 JDK15 完成内部重构对外语义不变。

**Qconcurrency-1433（场景判断·版本）** 推荐实践：讲源码前先确认 JDK 版本
**答案：对。** 解析：AQS 在 JDK15 完成内部重构对外语义不变。原因：新实现简化等待节点状态机与唤醒路径，性能与可维护性提升，网络流传的旧版源码逐行讲解已过时

**Qconcurrency-1434（填空·版本）** AQS 在 ______ 完成内部重构对外语义不变
**答案：JDK15**。解析：新实现简化等待节点状态机与唤醒路径，性能与可维护性提升，网络流传的旧版源码逐行讲解已过时

**Qconcurrency-1435（简答·版本）** 请说明「AQS」中JDK15的机制与使用要点。
**要点（标准答案）**：① AQS 在 JDK15 完成内部重构对外语义不变；② 原理：新实现简化等待节点状态机与唤醒路径，性能与可维护性提升，网络流传的旧版源码逐行讲解已过时；③ 使用要点：讲源码前先确认 JDK 版本。版本锚点：JDK 15 release notes。

**Qconcurrency-1436（单选·正向·公平性）** 关于「显式锁」的说法，正确的是？
- A. 默认是公平锁
- B. 非公平锁可能导致某些线程饿死但语义正确
- C. ReentrantLock 默认非公平锁吞吐更高
- D. 公平锁性能总是更优
**答案：C**
**解析：** ReentrantLock 默认非公平锁吞吐更高。原因：非公平允许新请求直接抢锁减少线程切换，公平锁按队列顺序避免饥饿但吞吐低，可构造函数选择。
**来源：** JC-050 · 显式锁（JDK 文档）

**Qconcurrency-1437（判断·公平性）** ReentrantLock 默认非公平锁吞吐更高
**答案：对。** 解析：非公平允许新请求直接抢锁减少线程切换，公平锁按队列顺序避免饥饿但吞吐低，可构造函数选择

**Qconcurrency-1438（判断·公平性）** 默认是公平锁
**答案：错。** 正确表述：ReentrantLock 默认非公平锁吞吐更高。原因：非公平允许新请求直接抢锁减少线程切换，公平锁按队列顺序避免饥饿但吞吐低，可构造函数选择

**Qconcurrency-1439（判断·公平性）** 公平锁性能总是更优
**答案：错。** 正确表述：ReentrantLock 默认非公平锁吞吐更高。原因：非公平允许新请求直接抢锁减少线程切换，公平锁按队列顺序避免饥饿但吞吐低，可构造函数选择

**Qconcurrency-1440（判断·公平性）** 非公平锁可能导致某些线程饿死但语义正确
**答案：错。** 正确表述：ReentrantLock 默认非公平锁吞吐更高。原因：非公平允许新请求直接抢锁减少线程切换，公平锁按队列顺序避免饥饿但吞吐低，可构造函数选择

**Qconcurrency-1441（场景单选·公平性）** 在工程实践中关于「ReentrantLock」，下列做法符合推荐实践的是？
- A. 公平锁性能总是更优
- B. 非公平锁可能导致某些线程饿死但语义正确
- C. 默认用非公平，公平需求明确才显式选
- D. 默认是公平锁
**答案：C**
**解析：** 推荐实践：默认用非公平，公平需求明确才显式选。事实依据：ReentrantLock 默认非公平锁吞吐更高。

**Qconcurrency-1442（场景判断·公平性）** 推荐实践：默认用非公平，公平需求明确才显式选
**答案：对。** 解析：ReentrantLock 默认非公平锁吞吐更高。原因：非公平允许新请求直接抢锁减少线程切换，公平锁按队列顺序避免饥饿但吞吐低，可构造函数选择

**Qconcurrency-1443（填空·公平性）** ______ 默认非公平锁吞吐更高
**答案：ReentrantLock**。解析：非公平允许新请求直接抢锁减少线程切换，公平锁按队列顺序避免饥饿但吞吐低，可构造函数选择

**Qconcurrency-1444（简答·公平性）** 请说明「显式锁」中ReentrantLock的机制与使用要点。
**要点（标准答案）**：① ReentrantLock 默认非公平锁吞吐更高；② 原理：非公平允许新请求直接抢锁减少线程切换，公平锁按队列顺序避免饥饿但吞吐低，可构造函数选择；③ 使用要点：默认用非公平，公平需求明确才显式选。版本锚点：JDK 文档。

**Qconcurrency-1445（单选·正向·能力）** 关于「显式锁」的说法，正确的是？
- A. synchronized 也支持中断等待
- B. Condition 与 wait 必须配对在同一把锁上
- C. ReentrantLock 相比 synchronized 增加可中断、超时与公平能力
- D. tryLock 获取不到会一直重试
**答案：C**
**解析：** ReentrantLock 相比 synchronized 增加可中断、超时与公平能力。原因：lockInterruptibly 等锁时响应中断、tryLock(time) 限时获取、多 Condition 条件队列，synchronized 全都不支持。
**来源：** JC-051 · 显式锁（JDK 文档）

**Qconcurrency-1446（判断·能力）** ReentrantLock 相比 synchronized 增加可中断、超时与公平能力
**答案：对。** 解析：lockInterruptibly 等锁时响应中断、tryLock(time) 限时获取、多 Condition 条件队列，synchronized 全都不支持

**Qconcurrency-1447（判断·能力）** synchronized 也支持中断等待
**答案：错。** 正确表述：ReentrantLock 相比 synchronized 增加可中断、超时与公平能力。原因：lockInterruptibly 等锁时响应中断、tryLock(time) 限时获取、多 Condition 条件队列，synchronized 全都不支持

**Qconcurrency-1448（判断·能力）** tryLock 获取不到会一直重试
**答案：错。** 正确表述：ReentrantLock 相比 synchronized 增加可中断、超时与公平能力。原因：lockInterruptibly 等锁时响应中断、tryLock(time) 限时获取、多 Condition 条件队列，synchronized 全都不支持

**Qconcurrency-1449（判断·能力）** Condition 与 wait 必须配对在同一把锁上
**答案：错。** 正确表述：ReentrantLock 相比 synchronized 增加可中断、超时与公平能力。原因：lockInterruptibly 等锁时响应中断、tryLock(time) 限时获取、多 Condition 条件队列，synchronized 全都不支持

**Qconcurrency-1450（场景单选·能力）** 在工程实践中关于「lockInterruptibly」，下列做法符合推荐实践的是？
- A. synchronized 也支持中断等待
- B. tryLock 获取不到会一直重试
- C. Condition 与 wait 必须配对在同一把锁上
- D. 需要中断响应与限时获取的场景选 ReentrantLock
**答案：D**
**解析：** 推荐实践：需要中断响应与限时获取的场景选 ReentrantLock。事实依据：ReentrantLock 相比 synchronized 增加可中断、超时与公平能力。

**Qconcurrency-1451（场景判断·能力）** 推荐实践：需要中断响应与限时获取的场景选 ReentrantLock
**答案：对。** 解析：ReentrantLock 相比 synchronized 增加可中断、超时与公平能力。原因：lockInterruptibly 等锁时响应中断、tryLock(time) 限时获取、多 Condition 条件队列，synchronized 全都不支持

**Qconcurrency-1452（简答·能力）** 请说明「显式锁」中lockInterruptibly的机制与使用要点。
**要点（标准答案）**：① ReentrantLock 相比 synchronized 增加可中断、超时与公平能力；② 原理：lockInterruptibly 等锁时响应中断、tryLock(time) 限时获取、多 Condition 条件队列，synchronized 全都不支持；③ 使用要点：需要中断响应与限时获取的场景选 ReentrantLock。版本锚点：JDK 文档。

**Qconcurrency-1453（单选·正向·读写锁）** 关于「显式锁」的说法，正确的是？
- A. ReentrantReadWriteLock 允许读共享写独占且支持写锁降级为读锁
- B. 读锁也是互斥的
- C. 降级是指先释放写锁再拿读锁
- D. 读写锁支持锁升级
**答案：A**
**解析：** ReentrantReadWriteLock 允许读共享写独占且支持写锁降级为读锁。原因：持有写锁时可再获取读锁后释放写（降级安全），升级（持读再取写）会死锁，适合读多写少的缓存场景。
**来源：** JC-052 · 显式锁（JDK 文档）

**Qconcurrency-1454（判断·读写锁）** ReentrantReadWriteLock 允许读共享写独占且支持写锁降级为读锁
**答案：对。** 解析：持有写锁时可再获取读锁后释放写（降级安全），升级（持读再取写）会死锁，适合读多写少的缓存场景

**Qconcurrency-1455（判断·读写锁）** 读写锁支持锁升级
**答案：错。** 正确表述：ReentrantReadWriteLock 允许读共享写独占且支持写锁降级为读锁。原因：持有写锁时可再获取读锁后释放写（降级安全），升级（持读再取写）会死锁，适合读多写少的缓存场景

**Qconcurrency-1456（判断·读写锁）** 读锁也是互斥的
**答案：错。** 正确表述：ReentrantReadWriteLock 允许读共享写独占且支持写锁降级为读锁。原因：持有写锁时可再获取读锁后释放写（降级安全），升级（持读再取写）会死锁，适合读多写少的缓存场景

**Qconcurrency-1457（判断·读写锁）** 降级是指先释放写锁再拿读锁
**答案：错。** 正确表述：ReentrantReadWriteLock 允许读共享写独占且支持写锁降级为读锁。原因：持有写锁时可再获取读锁后释放写（降级安全），升级（持读再取写）会死锁，适合读多写少的缓存场景

**Qconcurrency-1458（场景单选·读写锁）** 在工程实践中关于「ReentrantReadWriteLock」，下列做法符合推荐实践的是？
- A. 缓存刷新：写锁改数据降级读锁再校验
- B. 降级是指先释放写锁再拿读锁
- C. 读写锁支持锁升级
- D. 读锁也是互斥的
**答案：A**
**解析：** 推荐实践：缓存刷新：写锁改数据降级读锁再校验。事实依据：ReentrantReadWriteLock 允许读共享写独占且支持写锁降级为读锁。

**Qconcurrency-1459（场景判断·读写锁）** 推荐实践：缓存刷新：写锁改数据降级读锁再校验
**答案：对。** 解析：ReentrantReadWriteLock 允许读共享写独占且支持写锁降级为读锁。原因：持有写锁时可再获取读锁后释放写（降级安全），升级（持读再取写）会死锁，适合读多写少的缓存场景

**Qconcurrency-1460（填空·读写锁）** ______ 允许读共享写独占且支持写锁降级为读锁
**答案：ReentrantReadWriteLock**。解析：持有写锁时可再获取读锁后释放写（降级安全），升级（持读再取写）会死锁，适合读多写少的缓存场景

**Qconcurrency-1461（简答·读写锁）** 请说明「显式锁」中ReentrantReadWriteLock的机制与使用要点。
**要点（标准答案）**：① ReentrantReadWriteLock 允许读共享写独占且支持写锁降级为读锁；② 原理：持有写锁时可再获取读锁后释放写（降级安全），升级（持读再取写）会死锁，适合读多写少的缓存场景；③ 使用要点：缓存刷新：写锁改数据降级读锁再校验。版本锚点：JDK 文档。

**Qconcurrency-1462（单选·正向·乐观读）** 关于「显式锁」的说法，正确的是？
- A. StampedLock 完全替代 ReentrantReadWriteLock
- B. 乐观读失败会自动重试无需处理
- C. StampedLock 支持可重入
- D. StampedLock 提供乐观读：读时不加锁事后 validate 校验
**答案：D**
**解析：** StampedLock 提供乐观读：读时不加锁事后 validate 校验。原因：乐观读返回一个 stamp，读完后 validate 判断期间是否有写，失败升级为悲观读锁；吞吐高于读写锁，但不可重入且不支持 Condition。
**来源：** JC-053 · 显式锁（JDK 文档）

**Qconcurrency-1463（判断·乐观读）** StampedLock 提供乐观读：读时不加锁事后 validate 校验
**答案：对。** 解析：乐观读返回一个 stamp，读完后 validate 判断期间是否有写，失败升级为悲观读锁；吞吐高于读写锁，但不可重入且不支持 Condition

**Qconcurrency-1464（判断·乐观读）** StampedLock 支持可重入
**答案：错。** 正确表述：StampedLock 提供乐观读：读时不加锁事后 validate 校验。原因：乐观读返回一个 stamp，读完后 validate 判断期间是否有写，失败升级为悲观读锁；吞吐高于读写锁，但不可重入且不支持 Condition

**Qconcurrency-1465（判断·乐观读）** 乐观读失败会自动重试无需处理
**答案：错。** 正确表述：StampedLock 提供乐观读：读时不加锁事后 validate 校验。原因：乐观读返回一个 stamp，读完后 validate 判断期间是否有写，失败升级为悲观读锁；吞吐高于读写锁，但不可重入且不支持 Condition

**Qconcurrency-1466（判断·乐观读）** StampedLock 完全替代 ReentrantReadWriteLock
**答案：错。** 正确表述：StampedLock 提供乐观读：读时不加锁事后 validate 校验。原因：乐观读返回一个 stamp，读完后 validate 判断期间是否有写，失败升级为悲观读锁；吞吐高于读写锁，但不可重入且不支持 Condition

**Qconcurrency-1467（场景单选·乐观读）** 在工程实践中关于「StampedLock」，下列做法符合推荐实践的是？
- A. StampedLock 完全替代 ReentrantReadWriteLock
- B. 热点缓存读路径优化
- C. 乐观读失败会自动重试无需处理
- D. StampedLock 支持可重入
**答案：B**
**解析：** 推荐实践：热点缓存读路径优化。事实依据：StampedLock 提供乐观读：读时不加锁事后 validate 校验。

**Qconcurrency-1468（场景判断·乐观读）** 推荐实践：热点缓存读路径优化
**答案：对。** 解析：StampedLock 提供乐观读：读时不加锁事后 validate 校验。原因：乐观读返回一个 stamp，读完后 validate 判断期间是否有写，失败升级为悲观读锁；吞吐高于读写锁，但不可重入且不支持 Condition

**Qconcurrency-1469（填空·乐观读）** ______ 提供乐观读：读时不加锁事后 validate 校验
**答案：StampedLock**。解析：乐观读返回一个 stamp，读完后 validate 判断期间是否有写，失败升级为悲观读锁；吞吐高于读写锁，但不可重入且不支持 Condition

**Qconcurrency-1470（简答·乐观读）** 请说明「显式锁」中StampedLock的机制与使用要点。
**要点（标准答案）**：① StampedLock 提供乐观读：读时不加锁事后 validate 校验；② 原理：乐观读返回一个 stamp，读完后 validate 判断期间是否有写，失败升级为悲观读锁；吞吐高于读写锁，但不可重入且不支持 Condition；③ 使用要点：热点缓存读路径优化。版本锚点：JDK 文档。

**Qconcurrency-1471（单选·正向·CountDownLatch）** 关于「协作工具」的说法，正确的是？
- A. 计数到零后 countDown 抛异常
- B. CountDownLatch 计数不可重置用完即弃
- C. countDown 可以把计数加回来
- D. CountDownLatch 可 reset 复用
**答案：B**
**解析：** CountDownLatch 计数不可重置用完即弃。原因：await 等计数到零，countDown 递减，构造时固定 count，重复使用需重建对象或改用 CyclicBarrier。
**来源：** JC-054 · 协作工具（JDK 文档）

**Qconcurrency-1472（判断·CountDownLatch）** CountDownLatch 计数不可重置用完即弃
**答案：对。** 解析：await 等计数到零，countDown 递减，构造时固定 count，重复使用需重建对象或改用 CyclicBarrier

**Qconcurrency-1473（判断·CountDownLatch）** CountDownLatch 可 reset 复用
**答案：错。** 正确表述：CountDownLatch 计数不可重置用完即弃。原因：await 等计数到零，countDown 递减，构造时固定 count，重复使用需重建对象或改用 CyclicBarrier

**Qconcurrency-1474（判断·CountDownLatch）** countDown 可以把计数加回来
**答案：错。** 正确表述：CountDownLatch 计数不可重置用完即弃。原因：await 等计数到零，countDown 递减，构造时固定 count，重复使用需重建对象或改用 CyclicBarrier

**Qconcurrency-1475（判断·CountDownLatch）** 计数到零后 countDown 抛异常
**答案：错。** 正确表述：CountDownLatch 计数不可重置用完即弃。原因：await 等计数到零，countDown 递减，构造时固定 count，重复使用需重建对象或改用 CyclicBarrier

**Qconcurrency-1476（场景单选·CountDownLatch）** 在工程实践中关于「countDown」，下列做法符合推荐实践的是？
- A. 并行任务汇合点（多服务预加载后继续）
- B. countDown 可以把计数加回来
- C. 计数到零后 countDown 抛异常
- D. CountDownLatch 可 reset 复用
**答案：A**
**解析：** 推荐实践：并行任务汇合点（多服务预加载后继续）。事实依据：CountDownLatch 计数不可重置用完即弃。

**Qconcurrency-1477（场景判断·CountDownLatch）** 推荐实践：并行任务汇合点（多服务预加载后继续）
**答案：对。** 解析：CountDownLatch 计数不可重置用完即弃。原因：await 等计数到零，countDown 递减，构造时固定 count，重复使用需重建对象或改用 CyclicBarrier

**Qconcurrency-1478（简答·CountDownLatch）** 请说明「协作工具」中countDown的机制与使用要点。
**要点（标准答案）**：① CountDownLatch 计数不可重置用完即弃；② 原理：await 等计数到零，countDown 递减，构造时固定 count，重复使用需重建对象或改用 CyclicBarrier；③ 使用要点：并行任务汇合点（多服务预加载后继续）。版本锚点：JDK 文档。

**Qconcurrency-1479（单选·正向·CyclicBarrier）** 关于「协作工具」的说法，正确的是？
- A. CyclicBarrier 可重复使用且支持 barrierAction 回调
- B. barrierAction 在主线程执行
- C. CyclicBarrier 也是一次性的
- D. CyclicBarrier 基于AQS 的 count 不可重置
**答案：A**
**解析：** CyclicBarrier 可重复使用且支持 barrierAction 回调。原因：计数归零后自动重置进入下一轮，与 CountDownLatch 的单次性形成对比，适合分批同步场景。
**来源：** JC-055 · 协作工具（JDK 文档）

**Qconcurrency-1480（判断·CyclicBarrier）** CyclicBarrier 可重复使用且支持 barrierAction 回调
**答案：对。** 解析：计数归零后自动重置进入下一轮，与 CountDownLatch 的单次性形成对比，适合分批同步场景

**Qconcurrency-1481（判断·CyclicBarrier）** CyclicBarrier 也是一次性的
**答案：错。** 正确表述：CyclicBarrier 可重复使用且支持 barrierAction 回调。原因：计数归零后自动重置进入下一轮，与 CountDownLatch 的单次性形成对比，适合分批同步场景

**Qconcurrency-1482（判断·CyclicBarrier）** barrierAction 在主线程执行
**答案：错。** 正确表述：CyclicBarrier 可重复使用且支持 barrierAction 回调。原因：计数归零后自动重置进入下一轮，与 CountDownLatch 的单次性形成对比，适合分批同步场景

**Qconcurrency-1483（判断·CyclicBarrier）** CyclicBarrier 基于AQS 的 count 不可重置
**答案：错。** 正确表述：CyclicBarrier 可重复使用且支持 barrierAction 回调。原因：计数归零后自动重置进入下一轮，与 CountDownLatch 的单次性形成对比，适合分批同步场景

**Qconcurrency-1484（场景单选·CyclicBarrier）** 在工程实践中关于「复用」，下列做法符合推荐实践的是？
- A. CyclicBarrier 基于AQS 的 count 不可重置
- B. CyclicBarrier 也是一次性的
- C. 多轮分阶段并行计算
- D. barrierAction 在主线程执行
**答案：C**
**解析：** 推荐实践：多轮分阶段并行计算。事实依据：CyclicBarrier 可重复使用且支持 barrierAction 回调。

**Qconcurrency-1485（场景判断·CyclicBarrier）** 推荐实践：多轮分阶段并行计算
**答案：对。** 解析：CyclicBarrier 可重复使用且支持 barrierAction 回调。原因：计数归零后自动重置进入下一轮，与 CountDownLatch 的单次性形成对比，适合分批同步场景

**Qconcurrency-1486（简答·CyclicBarrier）** 请说明「协作工具」中复用的机制与使用要点。
**要点（标准答案）**：① CyclicBarrier 可重复使用且支持 barrierAction 回调；② 原理：计数归零后自动重置进入下一轮，与 CountDownLatch 的单次性形成对比，适合分批同步场景；③ 使用要点：多轮分阶段并行计算。版本锚点：JDK 文档。

**Qconcurrency-1487（单选·正向·Semaphore）** 关于「协作工具」的说法，正确的是？
- A. Semaphore 维护许可数用于限流与资源池
- B. Semaphore 的许可是资源本身
- C. Semaphore 默认公平
- D. release 可以使许可超过初始值（默认不允许）
**答案：A**
**解析：** Semaphore 维护许可数用于限流与资源池。原因：acquire 获取 release 归还，公平模式可选，典型场景：数据库连接池上限、接口并发限流。
**来源：** JC-056 · 协作工具（JDK 文档）

**Qconcurrency-1488（判断·Semaphore）** Semaphore 维护许可数用于限流与资源池
**答案：对。** 解析：acquire 获取 release 归还，公平模式可选，典型场景：数据库连接池上限、接口并发限流

**Qconcurrency-1489（判断·Semaphore）** Semaphore 的许可是资源本身
**答案：错。** 正确表述：Semaphore 维护许可数用于限流与资源池。原因：acquire 获取 release 归还，公平模式可选，典型场景：数据库连接池上限、接口并发限流

**Qconcurrency-1490（判断·Semaphore）** release 可以使许可超过初始值（默认不允许）
**答案：错。** 正确表述：Semaphore 维护许可数用于限流与资源池。原因：acquire 获取 release 归还，公平模式可选，典型场景：数据库连接池上限、接口并发限流

**Qconcurrency-1491（判断·Semaphore）** Semaphore 默认公平
**答案：错。** 正确表述：Semaphore 维护许可数用于限流与资源池。原因：acquire 获取 release 归还，公平模式可选，典型场景：数据库连接池上限、接口并发限流

**Qconcurrency-1492（场景单选·Semaphore）** 在工程实践中关于「许可」，下列做法符合推荐实践的是？
- A. release 可以使许可超过初始值（默认不允许）
- B. Semaphore 默认公平
- C. Semaphore 的许可是资源本身
- D. 接口并发数控制首选
**答案：D**
**解析：** 推荐实践：接口并发数控制首选。事实依据：Semaphore 维护许可数用于限流与资源池。

**Qconcurrency-1493（场景判断·Semaphore）** 推荐实践：接口并发数控制首选
**答案：对。** 解析：Semaphore 维护许可数用于限流与资源池。原因：acquire 获取 release 归还，公平模式可选，典型场景：数据库连接池上限、接口并发限流

**Qconcurrency-1494（填空·Semaphore）** Semaphore 维护______数用于限流与资源池
**答案：许可**。解析：acquire 获取 release 归还，公平模式可选，典型场景：数据库连接池上限、接口并发限流

**Qconcurrency-1495（简答·Semaphore）** 请说明「协作工具」中许可的机制与使用要点。
**要点（标准答案）**：① Semaphore 维护许可数用于限流与资源池；② 原理：acquire 获取 release 归还，公平模式可选，典型场景：数据库连接池上限、接口并发限流；③ 使用要点：接口并发数控制首选。版本锚点：JDK 文档。

**Qconcurrency-1496（单选·正向·CHM）** 关于「并发容器」的说法，正确的是？
- A. JDK8 的 ConcurrentHashMap 用 CAS 初始化与首节点插入加 synchronized 锁 bin 头实现分段写
- B. CHM 使用 ReentrantLock 分段锁（那是 JDK7）
- C. JDK8 的 CHM 锁粒度是 Segment
- D. CHM 全表一把锁
**答案：A**
**解析：** JDK8 的 ConcurrentHashMap 用 CAS 初始化与首节点插入加 synchronized 锁 bin 头实现分段写。原因：桶为空时 CAS 直接放节点，非空时 synchronized 锁住该 bin 首节点，锁粒度到桶，并发度等于桶数。
**来源：** JC-057 · 并发容器（JDK8 源码）

**Qconcurrency-1497（判断·CHM）** JDK8 的 ConcurrentHashMap 用 CAS 初始化与首节点插入加 synchronized 锁 bin 头实现分段写
**答案：对。** 解析：桶为空时 CAS 直接放节点，非空时 synchronized 锁住该 bin 首节点，锁粒度到桶，并发度等于桶数

**Qconcurrency-1498（判断·CHM）** CHM 使用 ReentrantLock 分段锁（那是 JDK7）
**答案：错。** 正确表述：JDK8 的 ConcurrentHashMap 用 CAS 初始化与首节点插入加 synchronized 锁 bin 头实现分段写。原因：桶为空时 CAS 直接放节点，非空时 synchronized 锁住该 bin 首节点，锁粒度到桶，并发度等于桶数

**Qconcurrency-1499（判断·CHM）** CHM 全表一把锁
**答案：错。** 正确表述：JDK8 的 ConcurrentHashMap 用 CAS 初始化与首节点插入加 synchronized 锁 bin 头实现分段写。原因：桶为空时 CAS 直接放节点，非空时 synchronized 锁住该 bin 首节点，锁粒度到桶，并发度等于桶数

**Qconcurrency-1500（判断·CHM）** JDK8 的 CHM 锁粒度是 Segment
**答案：错。** 正确表述：JDK8 的 ConcurrentHashMap 用 CAS 初始化与首节点插入加 synchronized 锁 bin 头实现分段写。原因：桶为空时 CAS 直接放节点，非空时 synchronized 锁住该 bin 首节点，锁粒度到桶，并发度等于桶数

**Qconcurrency-1501（场景单选·CHM）** 在工程实践中关于「CAS+synchronized」，下列做法符合推荐实践的是？
- A. 回答 CHM 原理必须分 JDK 版本
- B. JDK8 的 CHM 锁粒度是 Segment
- C. CHM 全表一把锁
- D. CHM 使用 ReentrantLock 分段锁（那是 JDK7）
**答案：A**
**解析：** 推荐实践：回答 CHM 原理必须分 JDK 版本。事实依据：JDK8 的 ConcurrentHashMap 用 CAS 初始化与首节点插入加 synchronized 锁 bin 头实现分段写。

**Qconcurrency-1502（场景判断·CHM）** 推荐实践：回答 CHM 原理必须分 JDK 版本
**答案：对。** 解析：JDK8 的 ConcurrentHashMap 用 CAS 初始化与首节点插入加 synchronized 锁 bin 头实现分段写。原因：桶为空时 CAS 直接放节点，非空时 synchronized 锁住该 bin 首节点，锁粒度到桶，并发度等于桶数

**Qconcurrency-1503（简答·CHM）** 请说明「并发容器」中CAS+synchronized的机制与使用要点。
**要点（标准答案）**：① JDK8 的 ConcurrentHashMap 用 CAS 初始化与首节点插入加 synchronized 锁 bin 头实现分段写；② 原理：桶为空时 CAS 直接放节点，非空时 synchronized 锁住该 bin 首节点，锁粒度到桶，并发度等于桶数；③ 使用要点：回答 CHM 原理必须分 JDK 版本。版本锚点：JDK8 源码。

**Qconcurrency-1504（单选·正向·CHM）** 关于「并发容器」的说法，正确的是？
- A. ConcurrentHashMap 不允许 null 键与 null 值
- B. TreeMap 也不允许 null 键
- C. CHM 可以存 null 值
- D. 禁止 null 是性能原因
**答案：A**
**解析：** ConcurrentHashMap 不允许 null 键与 null 值。原因：并发下 get 返回 null 无法区分"键不存在"与"值就是 null"，HashMap 单线程可用 containsKey 二次确认，CHM 不行所以直接禁止。
**来源：** JC-058 · 并发容器（JDK 文档）

**Qconcurrency-1505（判断·CHM）** ConcurrentHashMap 不允许 null 键与 null 值
**答案：对。** 解析：并发下 get 返回 null 无法区分"键不存在"与"值就是 null"，HashMap 单线程可用 containsKey 二次确认，CHM 不行所以直接禁止

**Qconcurrency-1506（判断·CHM）** CHM 可以存 null 值
**答案：错。** 正确表述：ConcurrentHashMap 不允许 null 键与 null 值。原因：并发下 get 返回 null 无法区分"键不存在"与"值就是 null"，HashMap 单线程可用 containsKey 二次确认，CHM 不行所以直接禁止

**Qconcurrency-1507（判断·CHM）** 禁止 null 是性能原因
**答案：错。** 正确表述：ConcurrentHashMap 不允许 null 键与 null 值。原因：并发下 get 返回 null 无法区分"键不存在"与"值就是 null"，HashMap 单线程可用 containsKey 二次确认，CHM 不行所以直接禁止

**Qconcurrency-1508（判断·CHM）** TreeMap 也不允许 null 键
**答案：错。** 正确表述：ConcurrentHashMap 不允许 null 键与 null 值。原因：并发下 get 返回 null 无法区分"键不存在"与"值就是 null"，HashMap 单线程可用 containsKey 二次确认，CHM 不行所以直接禁止

**Qconcurrency-1509（场景单选·CHM）** 在工程实践中关于「null」，下列做法符合推荐实践的是？
- A. TreeMap 也不允许 null 键
- B. 禁止 null 是性能原因
- C. 向 CHM put null 编译不报错运行时 NPE
- D. CHM 可以存 null 值
**答案：C**
**解析：** 推荐实践：向 CHM put null 编译不报错运行时 NPE。事实依据：ConcurrentHashMap 不允许 null 键与 null 值。

**Qconcurrency-1510（场景判断·CHM）** 推荐实践：向 CHM put null 编译不报错运行时 NPE
**答案：对。** 解析：ConcurrentHashMap 不允许 null 键与 null 值。原因：并发下 get 返回 null 无法区分"键不存在"与"值就是 null"，HashMap 单线程可用 containsKey 二次确认，CHM 不行所以直接禁止

**Qconcurrency-1511（填空·CHM）** ConcurrentHashMap 不允许 ______ 键与 null 值
**答案：null**。解析：并发下 get 返回 null 无法区分"键不存在"与"值就是 null"，HashMap 单线程可用 containsKey 二次确认，CHM 不行所以直接禁止

**Qconcurrency-1512（简答·CHM）** 请说明「并发容器」中null的机制与使用要点。
**要点（标准答案）**：① ConcurrentHashMap 不允许 null 键与 null 值；② 原理：并发下 get 返回 null 无法区分"键不存在"与"值就是 null"，HashMap 单线程可用 containsKey 二次确认，CHM 不行所以直接禁止；③ 使用要点：向 CHM put null 编译不报错运行时 NPE。版本锚点：JDK 文档。

**Qconcurrency-1513（单选·正向·CHM）** 关于「并发容器」的说法，正确的是？
- A. size 计算全程加锁
- B. CounterCell 与 LongAdder 无关
- C. CHM 的 size 通过 baseCount 加 CounterCell 数组汇总且是弱一致值
- D. CHM.size() 是精确值
**答案：C**
**解析：** CHM 的 size 通过 baseCount 加 CounterCell 数组汇总且是弱一致值。原因：写路径 CAS baseCount 失败则分散累加到 CounterCell 减少竞争，size 是采样汇总无强一致快照，精确计数要用外部锁或 LongAdder 思路。
**来源：** JC-059 · 并发容器（JDK8 源码）

**Qconcurrency-1514（判断·CHM）** CHM 的 size 通过 baseCount 加 CounterCell 数组汇总且是弱一致值
**答案：对。** 解析：写路径 CAS baseCount 失败则分散累加到 CounterCell 减少竞争，size 是采样汇总无强一致快照，精确计数要用外部锁或 LongAdder 思路

**Qconcurrency-1515（判断·CHM）** CHM.size() 是精确值
**答案：错。** 正确表述：CHM 的 size 通过 baseCount 加 CounterCell 数组汇总且是弱一致值。原因：写路径 CAS baseCount 失败则分散累加到 CounterCell 减少竞争，size 是采样汇总无强一致快照，精确计数要用外部锁或 LongAdder 思路

**Qconcurrency-1516（判断·CHM）** size 计算全程加锁
**答案：错。** 正确表述：CHM 的 size 通过 baseCount 加 CounterCell 数组汇总且是弱一致值。原因：写路径 CAS baseCount 失败则分散累加到 CounterCell 减少竞争，size 是采样汇总无强一致快照，精确计数要用外部锁或 LongAdder 思路

**Qconcurrency-1517（判断·CHM）** CounterCell 与 LongAdder 无关
**答案：错。** 正确表述：CHM 的 size 通过 baseCount 加 CounterCell 数组汇总且是弱一致值。原因：写路径 CAS baseCount 失败则分散累加到 CounterCell 减少竞争，size 是采样汇总无强一致快照，精确计数要用外部锁或 LongAdder 思路

**Qconcurrency-1518（场景单选·CHM）** 在工程实践中关于「CounterCell」，下列做法符合推荐实践的是？
- A. size 计算全程加锁
- B. CHM.size() 是精确值
- C. 需要精确 size 就换数据结构
- D. CounterCell 与 LongAdder 无关
**答案：C**
**解析：** 推荐实践：需要精确 size 就换数据结构。事实依据：CHM 的 size 通过 baseCount 加 CounterCell 数组汇总且是弱一致值。

**Qconcurrency-1519（场景判断·CHM）** 推荐实践：需要精确 size 就换数据结构
**答案：对。** 解析：CHM 的 size 通过 baseCount 加 CounterCell 数组汇总且是弱一致值。原因：写路径 CAS baseCount 失败则分散累加到 CounterCell 减少竞争，size 是采样汇总无强一致快照，精确计数要用外部锁或 LongAdder 思路

**Qconcurrency-1520（填空·CHM）** CHM 的 size 通过 baseCount 加 ______ 数组汇总且是弱一致值
**答案：CounterCell**。解析：写路径 CAS baseCount 失败则分散累加到 CounterCell 减少竞争，size 是采样汇总无强一致快照，精确计数要用外部锁或 LongAdder 思路

**Qconcurrency-1521（简答·CHM）** 请说明「并发容器」中CounterCell的机制与使用要点。
**要点（标准答案）**：① CHM 的 size 通过 baseCount 加 CounterCell 数组汇总且是弱一致值；② 原理：写路径 CAS baseCount 失败则分散累加到 CounterCell 减少竞争，size 是采样汇总无强一致快照，精确计数要用外部锁或 LongAdder 思路；③ 使用要点：需要精确 size 就换数据结构。版本锚点：JDK8 源码。

**Qconcurrency-1522（单选·正向·CHM）** 关于「并发容器」的说法，正确的是？
- A. 协助扩容只在 HashMap 中存在
- B. 扩容期间读写全部阻塞
- C. CHM 支持多线程协助扩容（helping transfer）
- D. CHM 扩容是单线程完成的
**答案：C**
**解析：** CHM 支持多线程协助扩容（helping transfer）。原因：扩容时其他线程 put 会先帮忙迁移部分桶再完成自己的写，这是 CHM 高并发的关键设计之一，单线程扩容会成瓶颈。
**来源：** JC-060 · 并发容器（JDK8 源码）

**Qconcurrency-1523（判断·CHM）** CHM 支持多线程协助扩容（helping transfer）
**答案：对。** 解析：扩容时其他线程 put 会先帮忙迁移部分桶再完成自己的写，这是 CHM 高并发的关键设计之一，单线程扩容会成瓶颈

**Qconcurrency-1524（判断·CHM）** CHM 扩容是单线程完成的
**答案：错。** 正确表述：CHM 支持多线程协助扩容（helping transfer）。原因：扩容时其他线程 put 会先帮忙迁移部分桶再完成自己的写，这是 CHM 高并发的关键设计之一，单线程扩容会成瓶颈

**Qconcurrency-1525（判断·CHM）** 扩容期间读写全部阻塞
**答案：错。** 正确表述：CHM 支持多线程协助扩容（helping transfer）。原因：扩容时其他线程 put 会先帮忙迁移部分桶再完成自己的写，这是 CHM 高并发的关键设计之一，单线程扩容会成瓶颈

**Qconcurrency-1526（判断·CHM）** 协助扩容只在 HashMap 中存在
**答案：错。** 正确表述：CHM 支持多线程协助扩容（helping transfer）。原因：扩容时其他线程 put 会先帮忙迁移部分桶再完成自己的写，这是 CHM 高并发的关键设计之一，单线程扩容会成瓶颈

**Qconcurrency-1527（场景单选·CHM）** 在工程实践中关于「扩容」，下列做法符合推荐实践的是？
- A. CHM 扩容是单线程完成的
- B. 谈 CHM 性能必提协助扩容
- C. 协助扩容只在 HashMap 中存在
- D. 扩容期间读写全部阻塞
**答案：B**
**解析：** 推荐实践：谈 CHM 性能必提协助扩容。事实依据：CHM 支持多线程协助扩容（helping transfer）。

**Qconcurrency-1528（场景判断·CHM）** 推荐实践：谈 CHM 性能必提协助扩容
**答案：对。** 解析：CHM 支持多线程协助扩容（helping transfer）。原因：扩容时其他线程 put 会先帮忙迁移部分桶再完成自己的写，这是 CHM 高并发的关键设计之一，单线程扩容会成瓶颈

**Qconcurrency-1529（填空·CHM）** CHM 支持多线程协助______（helping transfer）
**答案：扩容**。解析：扩容时其他线程 put 会先帮忙迁移部分桶再完成自己的写，这是 CHM 高并发的关键设计之一，单线程扩容会成瓶颈

**Qconcurrency-1530（简答·CHM）** 请说明「并发容器」中扩容的机制与使用要点。
**要点（标准答案）**：① CHM 支持多线程协助扩容（helping transfer）；② 原理：扩容时其他线程 put 会先帮忙迁移部分桶再完成自己的写，这是 CHM 高并发的关键设计之一，单线程扩容会成瓶颈；③ 使用要点：谈 CHM 性能必提协助扩容。版本锚点：JDK8 源码。

**Qconcurrency-1531（单选·正向·CHM）** 关于「并发容器」的说法，正确的是？
- A. CHM 的 get 完全不加锁
- B. get 偶尔会升级为加锁读
- C. volatile 只在写路径起作用
- D. get 需要读锁
**答案：A**
**解析：** CHM 的 get 完全不加锁。原因：Node 的 val 与 next 用 volatile 保证可见，读路径无锁无 CAS 是 CHM 读性能高的根源。
**来源：** JC-061 · 并发容器（JDK8 源码）

**Qconcurrency-1532（判断·CHM）** CHM 的 get 完全不加锁
**答案：对。** 解析：Node 的 val 与 next 用 volatile 保证可见，读路径无锁无 CAS 是 CHM 读性能高的根源

**Qconcurrency-1533（判断·CHM）** get 需要读锁
**答案：错。** 正确表述：CHM 的 get 完全不加锁。原因：Node 的 val 与 next 用 volatile 保证可见，读路径无锁无 CAS 是 CHM 读性能高的根源

**Qconcurrency-1534（判断·CHM）** get 偶尔会升级为加锁读
**答案：错。** 正确表述：CHM 的 get 完全不加锁。原因：Node 的 val 与 next 用 volatile 保证可见，读路径无锁无 CAS 是 CHM 读性能高的根源

**Qconcurrency-1535（判断·CHM）** volatile 只在写路径起作用
**答案：错。** 正确表述：CHM 的 get 完全不加锁。原因：Node 的 val 与 next 用 volatile 保证可见，读路径无锁无 CAS 是 CHM 读性能高的根源

**Qconcurrency-1536（场景单选·CHM）** 在工程实践中关于「读无锁」，下列做法符合推荐实践的是？
- A. get 需要读锁
- B. 高并发读场景 CHM 优于读写锁包裹的 HashMap
- C. get 偶尔会升级为加锁读
- D. volatile 只在写路径起作用
**答案：B**
**解析：** 推荐实践：高并发读场景 CHM 优于读写锁包裹的 HashMap。事实依据：CHM 的 get 完全不加锁。

**Qconcurrency-1537（场景判断·CHM）** 推荐实践：高并发读场景 CHM 优于读写锁包裹的 HashMap
**答案：对。** 解析：CHM 的 get 完全不加锁。原因：Node 的 val 与 next 用 volatile 保证可见，读路径无锁无 CAS 是 CHM 读性能高的根源

**Qconcurrency-1538（简答·CHM）** 请说明「并发容器」中读无锁的机制与使用要点。
**要点（标准答案）**：① CHM 的 get 完全不加锁；② 原理：Node 的 val 与 next 用 volatile 保证可见，读路径无锁无 CAS 是 CHM 读性能高的根源；③ 使用要点：高并发读场景 CHM 优于读写锁包裹的 HashMap。版本锚点：JDK8 源码。

**Qconcurrency-1539（单选·正向·CHM）** 关于「并发容器」的说法，正确的是？
- A. CHM 树化条件与 HashMap 一致：bin 中已有 8 个节点时插入第 9 个触发且表长需不小于 64
- B. 链表到 8 个就立即树化
- C. 树化只看链长与表长无关
- D. 表长 64 以下也会树化
**答案：A**
**解析：** CHM 树化条件与 HashMap 一致：bin 中已有 8 个节点时插入第 9 个触发且表长需不小于 64。原因：MIN_TREEIFY_CAPACITY=64，表太小时优先扩容而非树化；8 语义是"bin 已有 8 个节点"而非"链长到 8 才树化"。
**来源：** JC-062 · 并发容器（JDK8 源码实测）

**Qconcurrency-1540（判断·CHM）** CHM 树化条件与 HashMap 一致：bin 中已有 8 个节点时插入第 9 个触发且表长需不小于 64
**答案：对。** 解析：MIN_TREEIFY_CAPACITY=64，表太小时优先扩容而非树化；8 语义是"bin 已有 8 个节点"而非"链长到 8 才树化"

**Qconcurrency-1541（判断·CHM）** 链表到 8 个就立即树化
**答案：错。** 正确表述：CHM 树化条件与 HashMap 一致：bin 中已有 8 个节点时插入第 9 个触发且表长需不小于 64。原因：MIN_TREEIFY_CAPACITY=64，表太小时优先扩容而非树化；8 语义是"bin 已有 8 个节点"而非"链长到 8 才树化"

**Qconcurrency-1542（判断·CHM）** 树化只看链长与表长无关
**答案：错。** 正确表述：CHM 树化条件与 HashMap 一致：bin 中已有 8 个节点时插入第 9 个触发且表长需不小于 64。原因：MIN_TREEIFY_CAPACITY=64，表太小时优先扩容而非树化；8 语义是"bin 已有 8 个节点"而非"链长到 8 才树化"

**Qconcurrency-1543（判断·CHM）** 表长 64 以下也会树化
**答案：错。** 正确表述：CHM 树化条件与 HashMap 一致：bin 中已有 8 个节点时插入第 9 个触发且表长需不小于 64。原因：MIN_TREEIFY_CAPACITY=64，表太小时优先扩容而非树化；8 语义是"bin 已有 8 个节点"而非"链长到 8 才树化"

**Qconcurrency-1544（场景单选·CHM）** 在工程实践中关于「树化」，下列做法符合推荐实践的是？
- A. 表长 64 以下也会树化
- B. 树化只看链长与表长无关
- C. 链表到 8 个就立即树化
- D. 两处树化语义常考常错，以源码为准
**答案：D**
**解析：** 推荐实践：两处树化语义常考常错，以源码为准。事实依据：CHM 树化条件与 HashMap 一致：bin 中已有 8 个节点时插入第 9 个触发且表长需不小于 64。

**Qconcurrency-1545（场景判断·CHM）** 推荐实践：两处树化语义常考常错，以源码为准
**答案：对。** 解析：CHM 树化条件与 HashMap 一致：bin 中已有 8 个节点时插入第 9 个触发且表长需不小于 64。原因：MIN_TREEIFY_CAPACITY=64，表太小时优先扩容而非树化；8 语义是"bin 已有 8 个节点"而非"链长到 8 才树化"

**Qconcurrency-1546（填空·CHM）** CHM ______条件与 HashMap 一致：bin 中已有 8 个节点时插入第 9 个触发且表长需不小于 64
**答案：树化**。解析：MIN_TREEIFY_CAPACITY=64，表太小时优先扩容而非树化；8 语义是"bin 已有 8 个节点"而非"链长到 8 才树化"

**Qconcurrency-1547（简答·CHM）** 请说明「并发容器」中树化的机制与使用要点。
**要点（标准答案）**：① CHM 树化条件与 HashMap 一致：bin 中已有 8 个节点时插入第 9 个触发且表长需不小于 64；② 原理：MIN_TREEIFY_CAPACITY=64，表太小时优先扩容而非树化；8 语义是"bin 已有 8 个节点"而非"链长到 8 才树化"；③ 使用要点：两处树化语义常考常错，以源码为准。版本锚点：JDK8 源码实测。

**Qconcurrency-1548（单选·正向·CHM）** 关于「并发容器」的说法，正确的是？
- A. get 后再 putIfAbsent 与 computeIfAbsent 等价
- B. putIfAbsent 失败说明 key 必然被删除过
- C. computeIfAbsent 会在锁外计算
- D. CHM 的 putIfAbsent 与 computeIfAbsent 是原子复合操作
**答案：D**
**解析：** CHM 的 putIfAbsent 与 computeIfAbsent 是原子复合操作。原因：先 get 后 put 在并发下有竞态，原子方法一次完成检查与写入，本地缓存加载双重检查首选 computeIfAbsent。
**来源：** JC-063 · 并发容器（JDK 文档）

**Qconcurrency-1549（判断·CHM）** CHM 的 putIfAbsent 与 computeIfAbsent 是原子复合操作
**答案：对。** 解析：先 get 后 put 在并发下有竞态，原子方法一次完成检查与写入，本地缓存加载双重检查首选 computeIfAbsent

**Qconcurrency-1550（判断·CHM）** get 后再 putIfAbsent 与 computeIfAbsent 等价
**答案：错。** 正确表述：CHM 的 putIfAbsent 与 computeIfAbsent 是原子复合操作。原因：先 get 后 put 在并发下有竞态，原子方法一次完成检查与写入，本地缓存加载双重检查首选 computeIfAbsent

**Qconcurrency-1551（判断·CHM）** computeIfAbsent 会在锁外计算
**答案：错。** 正确表述：CHM 的 putIfAbsent 与 computeIfAbsent 是原子复合操作。原因：先 get 后 put 在并发下有竞态，原子方法一次完成检查与写入，本地缓存加载双重检查首选 computeIfAbsent

**Qconcurrency-1552（判断·CHM）** putIfAbsent 失败说明 key 必然被删除过
**答案：错。** 正确表述：CHM 的 putIfAbsent 与 computeIfAbsent 是原子复合操作。原因：先 get 后 put 在并发下有竞态，原子方法一次完成检查与写入，本地缓存加载双重检查首选 computeIfAbsent

**Qconcurrency-1553（场景单选·CHM）** 在工程实践中关于「复合操作」，下列做法符合推荐实践的是？
- A. get 后再 putIfAbsent 与 computeIfAbsent 等价
- B. 缓存防击穿用 computeIfAbsent
- C. computeIfAbsent 会在锁外计算
- D. putIfAbsent 失败说明 key 必然被删除过
**答案：B**
**解析：** 推荐实践：缓存防击穿用 computeIfAbsent。事实依据：CHM 的 putIfAbsent 与 computeIfAbsent 是原子复合操作。

**Qconcurrency-1554（场景判断·CHM）** 推荐实践：缓存防击穿用 computeIfAbsent
**答案：对。** 解析：CHM 的 putIfAbsent 与 computeIfAbsent 是原子复合操作。原因：先 get 后 put 在并发下有竞态，原子方法一次完成检查与写入，本地缓存加载双重检查首选 computeIfAbsent

**Qconcurrency-1555（填空·CHM）** CHM 的 putIfAbsent 与 computeIfAbsent 是原子______
**答案：复合操作**。解析：先 get 后 put 在并发下有竞态，原子方法一次完成检查与写入，本地缓存加载双重检查首选 computeIfAbsent

**Qconcurrency-1556（简答·CHM）** 请说明「并发容器」中复合操作的机制与使用要点。
**要点（标准答案）**：① CHM 的 putIfAbsent 与 computeIfAbsent 是原子复合操作；② 原理：先 get 后 put 在并发下有竞态，原子方法一次完成检查与写入，本地缓存加载双重检查首选 computeIfAbsent；③ 使用要点：缓存防击穿用 computeIfAbsent。版本锚点：JDK 文档。

**Qconcurrency-1557（单选·正向·CHM）** 关于「并发容器」的说法，正确的是？
- A. CHM 默认容量是 256
- B. CHM 负载因子是 1.0
- C. CHM 默认初始容量 16 负载因子 0.75 与 HashMap 相同
- D. CHM 不支持自定义负载因子
**答案：C**
**解析：** CHM 默认初始容量 16 负载因子 0.75 与 HashMap 相同。原因：可传 initialSize 与 loadFactor 构造参数，预估条数设 initialSize=预期/负载因子避免扩容抖动。
**来源：** JC-064 · 并发容器（JDK 文档）

**Qconcurrency-1558（判断·CHM）** CHM 默认初始容量 16 负载因子 0.75 与 HashMap 相同
**答案：对。** 解析：可传 initialSize 与 loadFactor 构造参数，预估条数设 initialSize=预期/负载因子避免扩容抖动

**Qconcurrency-1559（判断·CHM）** CHM 默认容量是 256
**答案：错。** 正确表述：CHM 默认初始容量 16 负载因子 0.75 与 HashMap 相同。原因：可传 initialSize 与 loadFactor 构造参数，预估条数设 initialSize=预期/负载因子避免扩容抖动

**Qconcurrency-1560（判断·CHM）** CHM 负载因子是 1.0
**答案：错。** 正确表述：CHM 默认初始容量 16 负载因子 0.75 与 HashMap 相同。原因：可传 initialSize 与 loadFactor 构造参数，预估条数设 initialSize=预期/负载因子避免扩容抖动

**Qconcurrency-1561（判断·CHM）** CHM 不支持自定义负载因子
**答案：错。** 正确表述：CHM 默认初始容量 16 负载因子 0.75 与 HashMap 相同。原因：可传 initialSize 与 loadFactor 构造参数，预估条数设 initialSize=预期/负载因子避免扩容抖动

**Qconcurrency-1562（场景单选·CHM）** 在工程实践中关于「参数」，下列做法符合推荐实践的是？
- A. CHM 不支持自定义负载因子
- B. 大缓存初始化时给足容量
- C. CHM 负载因子是 1.0
- D. CHM 默认容量是 256
**答案：B**
**解析：** 推荐实践：大缓存初始化时给足容量。事实依据：CHM 默认初始容量 16 负载因子 0.75 与 HashMap 相同。

**Qconcurrency-1563（场景判断·CHM）** 推荐实践：大缓存初始化时给足容量
**答案：对。** 解析：CHM 默认初始容量 16 负载因子 0.75 与 HashMap 相同。原因：可传 initialSize 与 loadFactor 构造参数，预估条数设 initialSize=预期/负载因子避免扩容抖动

**Qconcurrency-1564（简答·CHM）** 请说明「并发容器」中参数的机制与使用要点。
**要点（标准答案）**：① CHM 默认初始容量 16 负载因子 0.75 与 HashMap 相同；② 原理：可传 initialSize 与 loadFactor 构造参数，预估条数设 initialSize=预期/负载因子避免扩容抖动；③ 使用要点：大缓存初始化时给足容量。版本锚点：JDK 文档。

**Qconcurrency-1565（单选·正向·COW）** 关于「并发容器」的说法，正确的是？
- A. COW 适合大列表高频写
- B. COW 迭代器支持并发修改
- C. CopyOnWriteArrayList 写时复制整份数组读完全无锁
- D. COW 写性能优于 ArrayList
**答案：C**
**解析：** CopyOnWriteArrayList 写时复制整份数组读完全无锁。原因：修改时复制新数组替换引用（volatile 数组），迭代器是快照不支持 remove，适合读极多写极少的小列表（监听器列表）。
**来源：** JC-065 · 并发容器（JDK 源码）

**Qconcurrency-1566（判断·COW）** CopyOnWriteArrayList 写时复制整份数组读完全无锁
**答案：对。** 解析：修改时复制新数组替换引用（volatile 数组），迭代器是快照不支持 remove，适合读极多写极少的小列表（监听器列表）

**Qconcurrency-1567（判断·COW）** COW 写性能优于 ArrayList
**答案：错。** 正确表述：CopyOnWriteArrayList 写时复制整份数组读完全无锁。原因：修改时复制新数组替换引用（volatile 数组），迭代器是快照不支持 remove，适合读极多写极少的小列表（监听器列表）

**Qconcurrency-1568（判断·COW）** COW 迭代器支持并发修改
**答案：错。** 正确表述：CopyOnWriteArrayList 写时复制整份数组读完全无锁。原因：修改时复制新数组替换引用（volatile 数组），迭代器是快照不支持 remove，适合读极多写极少的小列表（监听器列表）

**Qconcurrency-1569（判断·COW）** COW 适合大列表高频写
**答案：错。** 正确表述：CopyOnWriteArrayList 写时复制整份数组读完全无锁。原因：修改时复制新数组替换引用（volatile 数组），迭代器是快照不支持 remove，适合读极多写极少的小列表（监听器列表）

**Qconcurrency-1570（场景单选·COW）** 在工程实践中关于「CopyOnWriteArrayList」，下列做法符合推荐实践的是？
- A. 监听器注册场景标准选择
- B. COW 适合大列表高频写
- C. COW 写性能优于 ArrayList
- D. COW 迭代器支持并发修改
**答案：A**
**解析：** 推荐实践：监听器注册场景标准选择。事实依据：CopyOnWriteArrayList 写时复制整份数组读完全无锁。

**Qconcurrency-1571（场景判断·COW）** 推荐实践：监听器注册场景标准选择
**答案：对。** 解析：CopyOnWriteArrayList 写时复制整份数组读完全无锁。原因：修改时复制新数组替换引用（volatile 数组），迭代器是快照不支持 remove，适合读极多写极少的小列表（监听器列表）

**Qconcurrency-1572（填空·COW）** ______ 写时复制整份数组读完全无锁
**答案：CopyOnWriteArrayList**。解析：修改时复制新数组替换引用（volatile 数组），迭代器是快照不支持 remove，适合读极多写极少的小列表（监听器列表）

**Qconcurrency-1573（简答·COW）** 请说明「并发容器」中CopyOnWriteArrayList的机制与使用要点。
**要点（标准答案）**：① CopyOnWriteArrayList 写时复制整份数组读完全无锁；② 原理：修改时复制新数组替换引用（volatile 数组），迭代器是快照不支持 remove，适合读极多写极少的小列表（监听器列表）；③ 使用要点：监听器注册场景标准选择。版本锚点：JDK 源码。

**Qconcurrency-1574（单选·正向·无锁）** 关于「并发容器」的说法，正确的是？
- A. 入队出队需要加锁
- B. ConcurrentLinkedQueue 是 CAS 无锁非阻塞队列
- C. 它实现 BlockingQueue 接口
- D. size() 是 O(1) 精确值
**答案：B**
**解析：** ConcurrentLinkedQueue 是 CAS 无锁非阻塞队列。原因：基于 Michael-Scott 无锁算法，size() 是 O(n) 弱一致遍历，适合无界并发生产消费但不是 BlockingQueue。
**来源：** JC-066 · 并发容器（JDK 源码）

**Qconcurrency-1575（判断·无锁）** ConcurrentLinkedQueue 是 CAS 无锁非阻塞队列
**答案：对。** 解析：基于 Michael-Scott 无锁算法，size() 是 O(n) 弱一致遍历，适合无界并发生产消费但不是 BlockingQueue

**Qconcurrency-1576（判断·无锁）** 它实现 BlockingQueue 接口
**答案：错。** 正确表述：ConcurrentLinkedQueue 是 CAS 无锁非阻塞队列。原因：基于 Michael-Scott 无锁算法，size() 是 O(n) 弱一致遍历，适合无界并发生产消费但不是 BlockingQueue

**Qconcurrency-1577（判断·无锁）** size() 是 O(1) 精确值
**答案：错。** 正确表述：ConcurrentLinkedQueue 是 CAS 无锁非阻塞队列。原因：基于 Michael-Scott 无锁算法，size() 是 O(n) 弱一致遍历，适合无界并发生产消费但不是 BlockingQueue

**Qconcurrency-1578（判断·无锁）** 入队出队需要加锁
**答案：错。** 正确表述：ConcurrentLinkedQueue 是 CAS 无锁非阻塞队列。原因：基于 Michael-Scott 无锁算法，size() 是 O(n) 弱一致遍历，适合无界并发生产消费但不是 BlockingQueue

**Qconcurrency-1579（场景单选·无锁）** 在工程实践中关于「ConcurrentLinkedQueue」，下列做法符合推荐实践的是？
- A. size() 是 O(1) 精确值
- B. 高吞吐异步任务传递
- C. 它实现 BlockingQueue 接口
- D. 入队出队需要加锁
**答案：B**
**解析：** 推荐实践：高吞吐异步任务传递。事实依据：ConcurrentLinkedQueue 是 CAS 无锁非阻塞队列。

**Qconcurrency-1580（场景判断·无锁）** 推荐实践：高吞吐异步任务传递
**答案：对。** 解析：ConcurrentLinkedQueue 是 CAS 无锁非阻塞队列。原因：基于 Michael-Scott 无锁算法，size() 是 O(n) 弱一致遍历，适合无界并发生产消费但不是 BlockingQueue

**Qconcurrency-1581（填空·无锁）** ______ 是 CAS 无锁非阻塞队列
**答案：ConcurrentLinkedQueue**。解析：基于 Michael-Scott 无锁算法，size() 是 O(n) 弱一致遍历，适合无界并发生产消费但不是 BlockingQueue

**Qconcurrency-1582（简答·无锁）** 请说明「并发容器」中ConcurrentLinkedQueue的机制与使用要点。
**要点（标准答案）**：① ConcurrentLinkedQueue 是 CAS 无锁非阻塞队列；② 原理：基于 Michael-Scott 无锁算法，size() 是 O(n) 弱一致遍历，适合无界并发生产消费但不是 BlockingQueue；③ 使用要点：高吞吐异步任务传递。版本锚点：JDK 源码。

**Qconcurrency-1583（单选·正向·模型）** 关于「JMM」的说法，正确的是？
- A. Java 变量直接操作主内存
- B. 工作内存就是 CPU 缓存本身（它是抽象模型）
- C. JMM 是内存物理结构规范
- D. JMM 抽象为主内存与线程工作内存每线程有本地副本
**答案：D**
**解析：** JMM 抽象为主内存与线程工作内存每线程有本地副本。原因：线程操作的是副本，何时刷回主存未定义，需要 volatile、锁或 final 等同步动作建立可见性通道，这是可见性问题的根源。
**来源：** JC-067 · JMM（JSR-133）

**Qconcurrency-1584（判断·模型）** JMM 抽象为主内存与线程工作内存每线程有本地副本
**答案：对。** 解析：线程操作的是副本，何时刷回主存未定义，需要 volatile、锁或 final 等同步动作建立可见性通道，这是可见性问题的根源

**Qconcurrency-1585（判断·模型）** Java 变量直接操作主内存
**答案：错。** 正确表述：JMM 抽象为主内存与线程工作内存每线程有本地副本。原因：线程操作的是副本，何时刷回主存未定义，需要 volatile、锁或 final 等同步动作建立可见性通道，这是可见性问题的根源

**Qconcurrency-1586（判断·模型）** 工作内存就是 CPU 缓存本身（它是抽象模型）
**答案：错。** 正确表述：JMM 抽象为主内存与线程工作内存每线程有本地副本。原因：线程操作的是副本，何时刷回主存未定义，需要 volatile、锁或 final 等同步动作建立可见性通道，这是可见性问题的根源

**Qconcurrency-1587（判断·模型）** JMM 是内存物理结构规范
**答案：错。** 正确表述：JMM 抽象为主内存与线程工作内存每线程有本地副本。原因：线程操作的是副本，何时刷回主存未定义，需要 volatile、锁或 final 等同步动作建立可见性通道，这是可见性问题的根源

**Qconcurrency-1588（场景单选·模型）** 在工程实践中关于「工作内存」，下列做法符合推荐实践的是？
- A. 工作内存就是 CPU 缓存本身（它是抽象模型）
- B. Java 变量直接操作主内存
- C. 从模型层面解释可见性 bug
- D. JMM 是内存物理结构规范
**答案：C**
**解析：** 推荐实践：从模型层面解释可见性 bug。事实依据：JMM 抽象为主内存与线程工作内存每线程有本地副本。

**Qconcurrency-1589（场景判断·模型）** 推荐实践：从模型层面解释可见性 bug
**答案：对。** 解析：JMM 抽象为主内存与线程工作内存每线程有本地副本。原因：线程操作的是副本，何时刷回主存未定义，需要 volatile、锁或 final 等同步动作建立可见性通道，这是可见性问题的根源

**Qconcurrency-1590（填空·模型）** JMM 抽象为主内存与线程______每线程有本地副本
**答案：工作内存**。解析：线程操作的是副本，何时刷回主存未定义，需要 volatile、锁或 final 等同步动作建立可见性通道，这是可见性问题的根源

**Qconcurrency-1591（简答·模型）** 请说明「JMM」中工作内存的机制与使用要点。
**要点（标准答案）**：① JMM 抽象为主内存与线程工作内存每线程有本地副本；② 原理：线程操作的是副本，何时刷回主存未定义，需要 volatile、锁或 final 等同步动作建立可见性通道，这是可见性问题的根源；③ 使用要点：从模型层面解释可见性 bug。版本锚点：JSR-133。

**Qconcurrency-1592（单选·正向·重排）** 关于「JMM」的说法，正确的是？
- A. 重排在单线程也会出错
- B. CPU 不做任何重排
- C. 单线程内程序表现为串行语义（as-if-serial）编译器与 CPU 可自由重排
- D. as-if-serial 是多线程语义
**答案：C**
**解析：** 单线程内程序表现为串行语义（as-if-serial）编译器与 CPU 可自由重排。原因：重排只在不改变单线程结果的前提下进行，多线程下重排导致可见性问题，需要 happens-before 约束。
**来源：** JC-068 · JMM（JLS 17.4）

**Qconcurrency-1593（判断·重排）** 单线程内程序表现为串行语义（as-if-serial）编译器与 CPU 可自由重排
**答案：对。** 解析：重排只在不改变单线程结果的前提下进行，多线程下重排导致可见性问题，需要 happens-before 约束

**Qconcurrency-1594（判断·重排）** 重排在单线程也会出错
**答案：错。** 正确表述：单线程内程序表现为串行语义（as-if-serial）编译器与 CPU 可自由重排。原因：重排只在不改变单线程结果的前提下进行，多线程下重排导致可见性问题，需要 happens-before 约束

**Qconcurrency-1595（判断·重排）** CPU 不做任何重排
**答案：错。** 正确表述：单线程内程序表现为串行语义（as-if-serial）编译器与 CPU 可自由重排。原因：重排只在不改变单线程结果的前提下进行，多线程下重排导致可见性问题，需要 happens-before 约束

**Qconcurrency-1596（判断·重排）** as-if-serial 是多线程语义
**答案：错。** 正确表述：单线程内程序表现为串行语义（as-if-serial）编译器与 CPU 可自由重排。原因：重排只在不改变单线程结果的前提下进行，多线程下重排导致可见性问题，需要 happens-before 约束

**Qconcurrency-1597（场景单选·重排）** 在工程实践中关于「as-if-serial」，下列做法符合推荐实践的是？
- A. as-if-serial 是多线程语义
- B. CPU 不做任何重排
- C. 重排在单线程也会出错
- D. 判断重排问题时先看是否跨线程
**答案：D**
**解析：** 推荐实践：判断重排问题时先看是否跨线程。事实依据：单线程内程序表现为串行语义（as-if-serial）编译器与 CPU 可自由重排。

**Qconcurrency-1598（场景判断·重排）** 推荐实践：判断重排问题时先看是否跨线程
**答案：对。** 解析：单线程内程序表现为串行语义（as-if-serial）编译器与 CPU 可自由重排。原因：重排只在不改变单线程结果的前提下进行，多线程下重排导致可见性问题，需要 happens-before 约束

**Qconcurrency-1599（填空·重排）** 单线程内程序表现为串行语义（______）编译器与 CPU 可自由重排
**答案：as-if-serial**。解析：重排只在不改变单线程结果的前提下进行，多线程下重排导致可见性问题，需要 happens-before 约束

**Qconcurrency-1600（简答·重排）** 请说明「JMM」中as-if-serial的机制与使用要点。
**要点（标准答案）**：① 单线程内程序表现为串行语义（as-if-serial）编译器与 CPU 可自由重排；② 原理：重排只在不改变单线程结果的前提下进行，多线程下重排导致可见性问题，需要 happens-before 约束；③ 使用要点：判断重排问题时先看是否跨线程。版本锚点：JLS 17.4。

**Qconcurrency-1601（单选·正向·安全发布）** 关于「JMM」的说法，正确的是？
- A. final 字段也需要 volatile 才可见
- B. 任何情况下读 final 字段都能立即看到
- C. final 字段在构造器内赋值后无需同步即可被其他线程安全读取
- D. String 的不可变与 final 无关
**答案：C**
**解析：** final 字段在构造器内赋值后无需同步即可被其他线程安全读取。原因：JMM 对 final 有特殊保证：构造器内写 final 与随后把引用发布给其他线程之间有 happens-before，this 不逸出是前提。
**来源：** JC-069 · JMM（JLS 17.5）

**Qconcurrency-1602（判断·安全发布）** final 字段在构造器内赋值后无需同步即可被其他线程安全读取
**答案：对。** 解析：JMM 对 final 有特殊保证：构造器内写 final 与随后把引用发布给其他线程之间有 happens-before，this 不逸出是前提

**Qconcurrency-1603（判断·安全发布）** final 字段也需要 volatile 才可见
**答案：错。** 正确表述：final 字段在构造器内赋值后无需同步即可被其他线程安全读取。原因：JMM 对 final 有特殊保证：构造器内写 final 与随后把引用发布给其他线程之间有 happens-before，this 不逸出是前提

**Qconcurrency-1604（判断·安全发布）** 任何情况下读 final 字段都能立即看到
**答案：错。** 正确表述：final 字段在构造器内赋值后无需同步即可被其他线程安全读取。原因：JMM 对 final 有特殊保证：构造器内写 final 与随后把引用发布给其他线程之间有 happens-before，this 不逸出是前提

**Qconcurrency-1605（判断·安全发布）** String 的不可变与 final 无关
**答案：错。** 正确表述：final 字段在构造器内赋值后无需同步即可被其他线程安全读取。原因：JMM 对 final 有特殊保证：构造器内写 final 与随后把引用发布给其他线程之间有 happens-before，this 不逸出是前提

**Qconcurrency-1606（场景单选·安全发布）** 在工程实践中关于「final」，下列做法符合推荐实践的是？
- A. final 字段也需要 volatile 才可见
- B. 不可变对象（值对象、配置）用 final 构建
- C. String 的不可变与 final 无关
- D. 任何情况下读 final 字段都能立即看到
**答案：B**
**解析：** 推荐实践：不可变对象（值对象、配置）用 final 构建。事实依据：final 字段在构造器内赋值后无需同步即可被其他线程安全读取。

**Qconcurrency-1607（场景判断·安全发布）** 推荐实践：不可变对象（值对象、配置）用 final 构建
**答案：对。** 解析：final 字段在构造器内赋值后无需同步即可被其他线程安全读取。原因：JMM 对 final 有特殊保证：构造器内写 final 与随后把引用发布给其他线程之间有 happens-before，this 不逸出是前提

**Qconcurrency-1608（填空·安全发布）** ______ 字段在构造器内赋值后无需同步即可被其他线程安全读取
**答案：final**。解析：JMM 对 final 有特殊保证：构造器内写 final 与随后把引用发布给其他线程之间有 happens-before，this 不逸出是前提

**Qconcurrency-1609（简答·安全发布）** 请说明「JMM」中final的机制与使用要点。
**要点（标准答案）**：① final 字段在构造器内赋值后无需同步即可被其他线程安全读取；② 原理：JMM 对 final 有特殊保证：构造器内写 final 与随后把引用发布给其他线程之间有 happens-before，this 不逸出是前提；③ 使用要点：不可变对象（值对象、配置）用 final 构建。版本锚点：JLS 17.5。

**Qconcurrency-1610（单选·正向·误用）** 关于「安全发布」的说法，正确的是？
- A. 构造器中把 this 交给外部（注册监听器、启动线程）导致未构造完成的对象被并发访问
- B. final 字段可以防止 this 逸出问题
- C. 构造器内启动线程是安全的
- D. this 逸出只影响性能
**答案：A**
**解析：** 构造器中把 this 交给外部（注册监听器、启动线程）导致未构造完成的对象被并发访问。原因：发布时 final 字段尚未赋值，其他线程可能读到默认值，修复：构造完成后统一发布或用静态工厂。
**来源：** JC-070 · 安全发布（JCiP 4.3）

**Qconcurrency-1611（判断·误用）** 构造器中把 this 交给外部（注册监听器、启动线程）导致未构造完成的对象被并发访问
**答案：对。** 解析：发布时 final 字段尚未赋值，其他线程可能读到默认值，修复：构造完成后统一发布或用静态工厂

**Qconcurrency-1612（判断·误用）** 构造器内启动线程是安全的
**答案：错。** 正确表述：构造器中把 this 交给外部（注册监听器、启动线程）导致未构造完成的对象被并发访问。原因：发布时 final 字段尚未赋值，其他线程可能读到默认值，修复：构造完成后统一发布或用静态工厂

**Qconcurrency-1613（判断·误用）** this 逸出只影响性能
**答案：错。** 正确表述：构造器中把 this 交给外部（注册监听器、启动线程）导致未构造完成的对象被并发访问。原因：发布时 final 字段尚未赋值，其他线程可能读到默认值，修复：构造完成后统一发布或用静态工厂

**Qconcurrency-1614（判断·误用）** final 字段可以防止 this 逸出问题
**答案：错。** 正确表述：构造器中把 this 交给外部（注册监听器、启动线程）导致未构造完成的对象被并发访问。原因：发布时 final 字段尚未赋值，其他线程可能读到默认值，修复：构造完成后统一发布或用静态工厂

**Qconcurrency-1615（场景单选·误用）** 在工程实践中关于「this 逸出」，下列做法符合推荐实践的是？
- A. this 逸出只影响性能
- B. final 字段可以防止 this 逸出问题
- C. 构造器内启动线程是安全的
- D. 监听器注册放构造后或工厂方法内
**答案：D**
**解析：** 推荐实践：监听器注册放构造后或工厂方法内。事实依据：构造器中把 this 交给外部（注册监听器、启动线程）导致未构造完成的对象被并发访问。

**Qconcurrency-1616（场景判断·误用）** 推荐实践：监听器注册放构造后或工厂方法内
**答案：对。** 解析：构造器中把 this 交给外部（注册监听器、启动线程）导致未构造完成的对象被并发访问。原因：发布时 final 字段尚未赋值，其他线程可能读到默认值，修复：构造完成后统一发布或用静态工厂

**Qconcurrency-1617（简答·误用）** 请说明「安全发布」中this 逸出的机制与使用要点。
**要点（标准答案）**：① 构造器中把 this 交给外部（注册监听器、启动线程）导致未构造完成的对象被并发访问；② 原理：发布时 final 字段尚未赋值，其他线程可能读到默认值，修复：构造完成后统一发布或用静态工厂；③ 使用要点：监听器注册放构造后或工厂方法内。版本锚点：JCiP 4.3。

**Qconcurrency-1618（单选·正向·不可变）** 关于「安全发布」的说法，正确的是？
- A. 不可变对象（所有字段 final 且无可变状态）天然线程安全
- B. 不可变对象仍需要加锁保护
- C. 不可变对象创建后仍可被修改
- D. String 可变所以线程不安全
**答案：A**
**解析：** 不可变对象（所有字段 final 且无可变状态）天然线程安全。原因：String、包装类等不可变类型可自由共享无需同步，设计线程安全的第一选择是造不可变对象。
**来源：** JC-071 · 安全发布（JCiP 4.x）

**Qconcurrency-1619（判断·不可变）** 不可变对象（所有字段 final 且无可变状态）天然线程安全
**答案：对。** 解析：String、包装类等不可变类型可自由共享无需同步，设计线程安全的第一选择是造不可变对象

**Qconcurrency-1620（判断·不可变）** 不可变对象仍需要加锁保护
**答案：错。** 正确表述：不可变对象（所有字段 final 且无可变状态）天然线程安全。原因：String、包装类等不可变类型可自由共享无需同步，设计线程安全的第一选择是造不可变对象

**Qconcurrency-1621（判断·不可变）** String 可变所以线程不安全
**答案：错。** 正确表述：不可变对象（所有字段 final 且无可变状态）天然线程安全。原因：String、包装类等不可变类型可自由共享无需同步，设计线程安全的第一选择是造不可变对象

**Qconcurrency-1622（判断·不可变）** 不可变对象创建后仍可被修改
**答案：错。** 正确表述：不可变对象（所有字段 final 且无可变状态）天然线程安全。原因：String、包装类等不可变类型可自由共享无需同步，设计线程安全的第一选择是造不可变对象

**Qconcurrency-1623（场景单选·不可变）** 在工程实践中关于「不可变对象」，下列做法符合推荐实践的是？
- A. 不可变对象创建后仍可被修改
- B. 共享配置、常量集合用不可变设计
- C. 不可变对象仍需要加锁保护
- D. String 可变所以线程不安全
**答案：B**
**解析：** 推荐实践：共享配置、常量集合用不可变设计。事实依据：不可变对象（所有字段 final 且无可变状态）天然线程安全。

**Qconcurrency-1624（场景判断·不可变）** 推荐实践：共享配置、常量集合用不可变设计
**答案：对。** 解析：不可变对象（所有字段 final 且无可变状态）天然线程安全。原因：String、包装类等不可变类型可自由共享无需同步，设计线程安全的第一选择是造不可变对象

**Qconcurrency-1625（填空·不可变）** ______（所有字段 final 且无可变状态）天然线程安全
**答案：不可变对象**。解析：String、包装类等不可变类型可自由共享无需同步，设计线程安全的第一选择是造不可变对象

**Qconcurrency-1626（简答·不可变）** 请说明「安全发布」中不可变对象的机制与使用要点。
**要点（标准答案）**：① 不可变对象（所有字段 final 且无可变状态）天然线程安全；② 原理：String、包装类等不可变类型可自由共享无需同步，设计线程安全的第一选择是造不可变对象；③ 使用要点：共享配置、常量集合用不可变设计。版本锚点：JCiP 4.x。

**Qconcurrency-1627（单选·正向·模式）** 关于「线程封闭」的说法，正确的是？
- A. Service 单例必须为每个方法加锁
- B. 局部变量天然线程封闭是实现线程安全的最简方式
- C. 栈封闭需要加锁保证
- D. 局部变量也可能被并发修改
**答案：B**
**解析：** 局部变量天然线程封闭是实现线程安全的最简方式。原因：变量只存在于栈帧不被共享，无状态 Service 的并发安全正来源于此。
**来源：** JC-072 · 线程封闭（JCiP 3.x）

**Qconcurrency-1628（判断·模式）** 局部变量天然线程封闭是实现线程安全的最简方式
**答案：对。** 解析：变量只存在于栈帧不被共享，无状态 Service 的并发安全正来源于此

**Qconcurrency-1629（判断·模式）** 局部变量也可能被并发修改
**答案：错。** 正确表述：局部变量天然线程封闭是实现线程安全的最简方式。原因：变量只存在于栈帧不被共享，无状态 Service 的并发安全正来源于此

**Qconcurrency-1630（判断·模式）** 栈封闭需要加锁保证
**答案：错。** 正确表述：局部变量天然线程封闭是实现线程安全的最简方式。原因：变量只存在于栈帧不被共享，无状态 Service 的并发安全正来源于此

**Qconcurrency-1631（判断·模式）** Service 单例必须为每个方法加锁
**答案：错。** 正确表述：局部变量天然线程封闭是实现线程安全的最简方式。原因：变量只存在于栈帧不被共享，无状态 Service 的并发安全正来源于此

**Qconcurrency-1632（场景单选·模式）** 在工程实践中关于「栈封闭」，下列做法符合推荐实践的是？
- A. 局部变量也可能被并发修改
- B. 栈封闭需要加锁保证
- C. Spring 单例 Service 无状态的并发安全性来源
- D. Service 单例必须为每个方法加锁
**答案：C**
**解析：** 推荐实践：Spring 单例 Service 无状态的并发安全性来源。事实依据：局部变量天然线程封闭是实现线程安全的最简方式。

**Qconcurrency-1633（场景判断·模式）** 推荐实践：Spring 单例 Service 无状态的并发安全性来源
**答案：对。** 解析：局部变量天然线程封闭是实现线程安全的最简方式。原因：变量只存在于栈帧不被共享，无状态 Service 的并发安全正来源于此

**Qconcurrency-1634（简答·模式）** 请说明「线程封闭」中栈封闭的机制与使用要点。
**要点（标准答案）**：① 局部变量天然线程封闭是实现线程安全的最简方式；② 原理：变量只存在于栈帧不被共享，无状态 Service 的并发安全正来源于此；③ 使用要点：Spring 单例 Service 无状态的并发安全性来源。版本锚点：JCiP 3.x。

**Qconcurrency-1635（单选·正向·CompletableFuture）** 关于「异步」的说法，正确的是？
- A. CompletableFuture 未指定线程时回调在完成线程或调用线程执行
- B. CF 有自己的内部线程池
- C. 所有回调默认在新线程
- D. thenApply 总是在主线程执行
**答案：A**
**解析：** CompletableFuture 未指定线程时回调在完成线程或调用线程执行。原因：thenApply 不带 Async 由完成线程直接执行，thenApplyAsync(fn) 落到 ForkJoinPool.commonPool，IO 回调务必显式指定自定义线程池。
**来源：** JC-073 · 异步（JDK 文档）

**Qconcurrency-1636（判断·CompletableFuture）** CompletableFuture 未指定线程时回调在完成线程或调用线程执行
**答案：对。** 解析：thenApply 不带 Async 由完成线程直接执行，thenApplyAsync(fn) 落到 ForkJoinPool.commonPool，IO 回调务必显式指定自定义线程池

**Qconcurrency-1637（判断·CompletableFuture）** thenApply 总是在主线程执行
**答案：错。** 正确表述：CompletableFuture 未指定线程时回调在完成线程或调用线程执行。原因：thenApply 不带 Async 由完成线程直接执行，thenApplyAsync(fn) 落到 ForkJoinPool.commonPool，IO 回调务必显式指定自定义线程池

**Qconcurrency-1638（判断·CompletableFuture）** 所有回调默认在新线程
**答案：错。** 正确表述：CompletableFuture 未指定线程时回调在完成线程或调用线程执行。原因：thenApply 不带 Async 由完成线程直接执行，thenApplyAsync(fn) 落到 ForkJoinPool.commonPool，IO 回调务必显式指定自定义线程池

**Qconcurrency-1639（判断·CompletableFuture）** CF 有自己的内部线程池
**答案：错。** 正确表述：CompletableFuture 未指定线程时回调在完成线程或调用线程执行。原因：thenApply 不带 Async 由完成线程直接执行，thenApplyAsync(fn) 落到 ForkJoinPool.commonPool，IO 回调务必显式指定自定义线程池

**Qconcurrency-1640（场景单选·CompletableFuture）** 在工程实践中关于「回调线程」，下列做法符合推荐实践的是？
- A. 回调线程归属决定线程上下文是否丢失
- B. thenApply 总是在主线程执行
- C. 所有回调默认在新线程
- D. CF 有自己的内部线程池
**答案：A**
**解析：** 推荐实践：回调线程归属决定线程上下文是否丢失。事实依据：CompletableFuture 未指定线程时回调在完成线程或调用线程执行。

**Qconcurrency-1641（场景判断·CompletableFuture）** 推荐实践：回调线程归属决定线程上下文是否丢失
**答案：对。** 解析：CompletableFuture 未指定线程时回调在完成线程或调用线程执行。原因：thenApply 不带 Async 由完成线程直接执行，thenApplyAsync(fn) 落到 ForkJoinPool.commonPool，IO 回调务必显式指定自定义线程池

**Qconcurrency-1642（简答·CompletableFuture）** 请说明「异步」中回调线程的机制与使用要点。
**要点（标准答案）**：① CompletableFuture 未指定线程时回调在完成线程或调用线程执行；② 原理：thenApply 不带 Async 由完成线程直接执行，thenApplyAsync(fn) 落到 ForkJoinPool.commonPool，IO 回调务必显式指定自定义线程池；③ 使用要点：回调线程归属决定线程上下文是否丢失。版本锚点：JDK 文档。

**Qconcurrency-1643（单选·正向·CompletableFuture）** 关于「异步」的说法，正确的是？
- A. commonPool 是 CF 专属线程池
- B. commonPool 并行度等于 CPU 核数
- C. 默认池隔离了不同业务
- D. supplyAsync 默认线程池是 ForkJoinPool.commonPool
**答案：D**
**解析：** supplyAsync 默认线程池是 ForkJoinPool.commonPool。原因：commonPool 并行度为 CPU 核减一且全 JVM 共享，IO 任务占满会拖垮其他并行流任务，生产环境必须传自定义 Executor。
**来源：** JC-074 · 异步（JDK8 文档）

**Qconcurrency-1644（判断·CompletableFuture）** supplyAsync 默认线程池是 ForkJoinPool.commonPool
**答案：对。** 解析：commonPool 并行度为 CPU 核减一且全 JVM 共享，IO 任务占满会拖垮其他并行流任务，生产环境必须传自定义 Executor

**Qconcurrency-1645（判断·CompletableFuture）** commonPool 是 CF 专属线程池
**答案：错。** 正确表述：supplyAsync 默认线程池是 ForkJoinPool.commonPool。原因：commonPool 并行度为 CPU 核减一且全 JVM 共享，IO 任务占满会拖垮其他并行流任务，生产环境必须传自定义 Executor

**Qconcurrency-1646（判断·CompletableFuture）** commonPool 并行度等于 CPU 核数
**答案：错。** 正确表述：supplyAsync 默认线程池是 ForkJoinPool.commonPool。原因：commonPool 并行度为 CPU 核减一且全 JVM 共享，IO 任务占满会拖垮其他并行流任务，生产环境必须传自定义 Executor

**Qconcurrency-1647（判断·CompletableFuture）** 默认池隔离了不同业务
**答案：错。** 正确表述：supplyAsync 默认线程池是 ForkJoinPool.commonPool。原因：commonPool 并行度为 CPU 核减一且全 JVM 共享，IO 任务占满会拖垮其他并行流任务，生产环境必须传自定义 Executor

**Qconcurrency-1648（场景单选·CompletableFuture）** 在工程实践中关于「commonPool」，下列做法符合推荐实践的是？
- A. commonPool 是 CF 专属线程池
- B. 默认池隔离了不同业务
- C. commonPool 并行度等于 CPU 核数
- D. CF 的异步任务统一换自定义池
**答案：D**
**解析：** 推荐实践：CF 的异步任务统一换自定义池。事实依据：supplyAsync 默认线程池是 ForkJoinPool.commonPool。

**Qconcurrency-1649（场景判断·CompletableFuture）** 推荐实践：CF 的异步任务统一换自定义池
**答案：对。** 解析：supplyAsync 默认线程池是 ForkJoinPool.commonPool。原因：commonPool 并行度为 CPU 核减一且全 JVM 共享，IO 任务占满会拖垮其他并行流任务，生产环境必须传自定义 Executor

**Qconcurrency-1650（填空·CompletableFuture）** supplyAsync 默认线程池是 ForkJoinPool.______
**答案：commonPool**。解析：commonPool 并行度为 CPU 核减一且全 JVM 共享，IO 任务占满会拖垮其他并行流任务，生产环境必须传自定义 Executor

**Qconcurrency-1651（简答·CompletableFuture）** 请说明「异步」中commonPool的机制与使用要点。
**要点（标准答案）**：① supplyAsync 默认线程池是 ForkJoinPool.commonPool；② 原理：commonPool 并行度为 CPU 核减一且全 JVM 共享，IO 任务占满会拖垮其他并行流任务，生产环境必须传自定义 Executor；③ 使用要点：CF 的异步任务统一换自定义池。版本锚点：JDK8 文档。

**Qconcurrency-1652（单选·正向·CompletableFuture）** 关于「异步」的说法，正确的是？
- A. anyOf 等待全部完成
- B. allOf 直接返回结果列表
- C. join 与 get 语义完全相同
- D. allOf 等全部完成 anyOf 任一完成 join/get 阻塞取结果
**答案：D**
**解析：** allOf 等全部完成 anyOf 任一完成 join/get 阻塞取结果。原因：allOf 返回的 CF 需再 join 拿各任务结果，anyOf 用于多源竞速（多缓存源取最快）。
**来源：** JC-075 · 异步（JDK 文档）

**Qconcurrency-1653（判断·CompletableFuture）** allOf 等全部完成 anyOf 任一完成 join/get 阻塞取结果
**答案：对。** 解析：allOf 返回的 CF 需再 join 拿各任务结果，anyOf 用于多源竞速（多缓存源取最快）

**Qconcurrency-1654（判断·CompletableFuture）** allOf 直接返回结果列表
**答案：错。** 正确表述：allOf 等全部完成 anyOf 任一完成 join/get 阻塞取结果。原因：allOf 返回的 CF 需再 join 拿各任务结果，anyOf 用于多源竞速（多缓存源取最快）

**Qconcurrency-1655（判断·CompletableFuture）** anyOf 等待全部完成
**答案：错。** 正确表述：allOf 等全部完成 anyOf 任一完成 join/get 阻塞取结果。原因：allOf 返回的 CF 需再 join 拿各任务结果，anyOf 用于多源竞速（多缓存源取最快）

**Qconcurrency-1656（判断·CompletableFuture）** join 与 get 语义完全相同
**答案：错。** 正确表述：allOf 等全部完成 anyOf 任一完成 join/get 阻塞取结果。原因：allOf 返回的 CF 需再 join 拿各任务结果，anyOf 用于多源竞速（多缓存源取最快）

**Qconcurrency-1657（场景单选·CompletableFuture）** 在工程实践中关于「组合」，下列做法符合推荐实践的是？
- A. 并行聚合（多下游并发调用）标准写法
- B. anyOf 等待全部完成
- C. join 与 get 语义完全相同
- D. allOf 直接返回结果列表
**答案：A**
**解析：** 推荐实践：并行聚合（多下游并发调用）标准写法。事实依据：allOf 等全部完成 anyOf 任一完成 join/get 阻塞取结果。

**Qconcurrency-1658（场景判断·CompletableFuture）** 推荐实践：并行聚合（多下游并发调用）标准写法
**答案：对。** 解析：allOf 等全部完成 anyOf 任一完成 join/get 阻塞取结果。原因：allOf 返回的 CF 需再 join 拿各任务结果，anyOf 用于多源竞速（多缓存源取最快）

**Qconcurrency-1659（简答·CompletableFuture）** 请说明「异步」中组合的机制与使用要点。
**要点（标准答案）**：① allOf 等全部完成 anyOf 任一完成 join/get 阻塞取结果；② 原理：allOf 返回的 CF 需再 join 拿各任务结果，anyOf 用于多源竞速（多缓存源取最快）；③ 使用要点：并行聚合（多下游并发调用）标准写法。版本锚点：JDK 文档。

**Qconcurrency-1660（单选·正向·CompletableFuture）** 关于「异步」的说法，正确的是？
- A. exceptionally 只处理正常路径
- B. CF 的异常不自动传播调用方，链上用 exceptionally 或 handle 恢复
- C. CF 异常自动抛给调用者
- D. 每一步回调都要 try-catch
**答案：B**
**解析：** CF 的异常不自动传播调用方，链上用 exceptionally 或 handle 恢复。原因：异常沿依赖链传播使下游跳过，get 时包装成 ExecutionException 抛出；handle 同时处理正常与异常路径。
**来源：** JC-076 · 异步（JDK 文档）

**Qconcurrency-1661（判断·CompletableFuture）** CF 的异常不自动传播调用方，链上用 exceptionally 或 handle 恢复
**答案：对。** 解析：异常沿依赖链传播使下游跳过，get 时包装成 ExecutionException 抛出；handle 同时处理正常与异常路径

**Qconcurrency-1662（判断·CompletableFuture）** CF 异常自动抛给调用者
**答案：错。** 正确表述：CF 的异常不自动传播调用方，链上用 exceptionally 或 handle 恢复。原因：异常沿依赖链传播使下游跳过，get 时包装成 ExecutionException 抛出；handle 同时处理正常与异常路径

**Qconcurrency-1663（判断·CompletableFuture）** exceptionally 只处理正常路径
**答案：错。** 正确表述：CF 的异常不自动传播调用方，链上用 exceptionally 或 handle 恢复。原因：异常沿依赖链传播使下游跳过，get 时包装成 ExecutionException 抛出；handle 同时处理正常与异常路径

**Qconcurrency-1664（判断·CompletableFuture）** 每一步回调都要 try-catch
**答案：错。** 正确表述：CF 的异常不自动传播调用方，链上用 exceptionally 或 handle 恢复。原因：异常沿依赖链传播使下游跳过，get 时包装成 ExecutionException 抛出；handle 同时处理正常与异常路径

**Qconcurrency-1665（场景单选·CompletableFuture）** 在工程实践中关于「异常」，下列做法符合推荐实践的是？
- A. 每一步回调都要 try-catch
- B. 链式调用末端统一 exceptionally 兜底
- C. exceptionally 只处理正常路径
- D. CF 异常自动抛给调用者
**答案：B**
**解析：** 推荐实践：链式调用末端统一 exceptionally 兜底。事实依据：CF 的异常不自动传播调用方，链上用 exceptionally 或 handle 恢复。

**Qconcurrency-1666（场景判断·CompletableFuture）** 推荐实践：链式调用末端统一 exceptionally 兜底
**答案：对。** 解析：CF 的异常不自动传播调用方，链上用 exceptionally 或 handle 恢复。原因：异常沿依赖链传播使下游跳过，get 时包装成 ExecutionException 抛出；handle 同时处理正常与异常路径

**Qconcurrency-1667（填空·CompletableFuture）** CF 的______不自动传播调用方，链上用 exceptionally 或 handle 恢复
**答案：异常**。解析：异常沿依赖链传播使下游跳过，get 时包装成 ExecutionException 抛出；handle 同时处理正常与异常路径

**Qconcurrency-1668（简答·CompletableFuture）** 请说明「异步」中异常的机制与使用要点。
**要点（标准答案）**：① CF 的异常不自动传播调用方，链上用 exceptionally 或 handle 恢复；② 原理：异常沿依赖链传播使下游跳过，get 时包装成 ExecutionException 抛出；handle 同时处理正常与异常路径；③ 使用要点：链式调用末端统一 exceptionally 兜底。版本锚点：JDK 文档。

**Qconcurrency-1669（单选·正向·版本）** 关于「虚拟线程」的说法，正确的是？
- A. 虚拟线程是 JDK21 正式特性由 JVM 调度到少量载体线程
- B. 虚拟线程比平台线程运行更快
- C. 虚拟线程需要线程池管理
- D. 虚拟线程能加速 CPU 计算任务
**答案：A**
**解析：** 虚拟线程是 JDK21 正式特性由 JVM 调度到少量载体线程。原因：创建成本极低（栈在堆上）可开百万级，阻塞时让出载体线程由 JVM 换入下一个虚拟线程，面向 IO 密集高并发。
**来源：** JC-077 · 虚拟线程（JEP 444）

**Qconcurrency-1670（判断·版本）** 虚拟线程是 JDK21 正式特性由 JVM 调度到少量载体线程
**答案：对。** 解析：创建成本极低（栈在堆上）可开百万级，阻塞时让出载体线程由 JVM 换入下一个虚拟线程，面向 IO 密集高并发

**Qconcurrency-1671（判断·版本）** 虚拟线程能加速 CPU 计算任务
**答案：错。** 正确表述：虚拟线程是 JDK21 正式特性由 JVM 调度到少量载体线程。原因：创建成本极低（栈在堆上）可开百万级，阻塞时让出载体线程由 JVM 换入下一个虚拟线程，面向 IO 密集高并发

**Qconcurrency-1672（判断·版本）** 虚拟线程比平台线程运行更快
**答案：错。** 正确表述：虚拟线程是 JDK21 正式特性由 JVM 调度到少量载体线程。原因：创建成本极低（栈在堆上）可开百万级，阻塞时让出载体线程由 JVM 换入下一个虚拟线程，面向 IO 密集高并发

**Qconcurrency-1673（判断·版本）** 虚拟线程需要线程池管理
**答案：错。** 正确表述：虚拟线程是 JDK21 正式特性由 JVM 调度到少量载体线程。原因：创建成本极低（栈在堆上）可开百万级，阻塞时让出载体线程由 JVM 换入下一个虚拟线程，面向 IO 密集高并发

**Qconcurrency-1674（场景单选·版本）** 在工程实践中关于「JDK21」，下列做法符合推荐实践的是？
- A. 虚拟线程需要线程池管理
- B. 虚拟线程能加速 CPU 计算任务
- C. 虚拟线程比平台线程运行更快
- D. IO 密集微服务高并发吞吐利器
**答案：D**
**解析：** 推荐实践：IO 密集微服务高并发吞吐利器。事实依据：虚拟线程是 JDK21 正式特性由 JVM 调度到少量载体线程。

**Qconcurrency-1675（场景判断·版本）** 推荐实践：IO 密集微服务高并发吞吐利器
**答案：对。** 解析：虚拟线程是 JDK21 正式特性由 JVM 调度到少量载体线程。原因：创建成本极低（栈在堆上）可开百万级，阻塞时让出载体线程由 JVM 换入下一个虚拟线程，面向 IO 密集高并发

**Qconcurrency-1676（填空·版本）** 虚拟线程是 ______ 正式特性由 JVM 调度到少量载体线程
**答案：JDK21**。解析：创建成本极低（栈在堆上）可开百万级，阻塞时让出载体线程由 JVM 换入下一个虚拟线程，面向 IO 密集高并发

**Qconcurrency-1677（简答·版本）** 请说明「虚拟线程」中JDK21的机制与使用要点。
**要点（标准答案）**：① 虚拟线程是 JDK21 正式特性由 JVM 调度到少量载体线程；② 原理：创建成本极低（栈在堆上）可开百万级，阻塞时让出载体线程由 JVM 换入下一个虚拟线程，面向 IO 密集高并发；③ 使用要点：IO 密集微服务高并发吞吐利器。版本锚点：JEP 444。

**Qconcurrency-1678（单选·正向·误用）** 关于「虚拟线程」的说法，正确的是？
- A. pinning 问题在 JDK21 已修复
- B. JDK21-23 中虚拟线程在 synchronized 块内阻塞会 pin 载体线程
- C. ReentrantLock 也会 pin 载体线程
- D. pinning 只影响性能不影响正确性所以无需关注
**答案：B**
**解析：** JDK21-23 中虚拟线程在 synchronized 块内阻塞会 pin 载体线程。原因：被 pin 的载体无法释放导致吞吐退化，JDK24 JEP 491 已修复（synchronized 不再 pin）；过渡期热点路径可换 ReentrantLock。
**来源：** JC-078 · 虚拟线程（JEP 491）

**Qconcurrency-1679（判断·误用）** JDK21-23 中虚拟线程在 synchronized 块内阻塞会 pin 载体线程
**答案：对。** 解析：被 pin 的载体无法释放导致吞吐退化，JDK24 JEP 491 已修复（synchronized 不再 pin）；过渡期热点路径可换 ReentrantLock

**Qconcurrency-1680（判断·误用）** pinning 问题在 JDK21 已修复
**答案：错。** 正确表述：JDK21-23 中虚拟线程在 synchronized 块内阻塞会 pin 载体线程。原因：被 pin 的载体无法释放导致吞吐退化，JDK24 JEP 491 已修复（synchronized 不再 pin）；过渡期热点路径可换 ReentrantLock

**Qconcurrency-1681（判断·误用）** pinning 只影响性能不影响正确性所以无需关注
**答案：错。** 正确表述：JDK21-23 中虚拟线程在 synchronized 块内阻塞会 pin 载体线程。原因：被 pin 的载体无法释放导致吞吐退化，JDK24 JEP 491 已修复（synchronized 不再 pin）；过渡期热点路径可换 ReentrantLock

**Qconcurrency-1682（判断·误用）** ReentrantLock 也会 pin 载体线程
**答案：错。** 正确表述：JDK21-23 中虚拟线程在 synchronized 块内阻塞会 pin 载体线程。原因：被 pin 的载体无法释放导致吞吐退化，JDK24 JEP 491 已修复（synchronized 不再 pin）；过渡期热点路径可换 ReentrantLock

**Qconcurrency-1683（场景单选·误用）** 在工程实践中关于「pinning」，下列做法符合推荐实践的是？
- A. pinning 问题在 JDK21 已修复
- B. pinning 只影响性能不影响正确性所以无需关注
- C. JDK21 服务排查吞吐退化先查 pin
- D. ReentrantLock 也会 pin 载体线程
**答案：C**
**解析：** 推荐实践：JDK21 服务排查吞吐退化先查 pin。事实依据：JDK21-23 中虚拟线程在 synchronized 块内阻塞会 pin 载体线程。

**Qconcurrency-1684（场景判断·误用）** 推荐实践：JDK21 服务排查吞吐退化先查 pin
**答案：对。** 解析：JDK21-23 中虚拟线程在 synchronized 块内阻塞会 pin 载体线程。原因：被 pin 的载体无法释放导致吞吐退化，JDK24 JEP 491 已修复（synchronized 不再 pin）；过渡期热点路径可换 ReentrantLock

**Qconcurrency-1685（简答·误用）** 请说明「虚拟线程」中pinning的机制与使用要点。
**要点（标准答案）**：① JDK21-23 中虚拟线程在 synchronized 块内阻塞会 pin 载体线程；② 原理：被 pin 的载体无法释放导致吞吐退化，JDK24 JEP 491 已修复（synchronized 不再 pin）；过渡期热点路径可换 ReentrantLock；③ 使用要点：JDK21 服务排查吞吐退化先查 pin。版本锚点：JEP 491。

**Qconcurrency-1686（单选·正向·误用）** 关于「虚拟线程」的说法，正确的是？
- A. 虚拟线程创建成本与平台线程相同
- B. 虚拟线程也应该放进线程池
- C. Semaphore 不能用于虚拟线程限流
- D. 虚拟线程不应池化每次任务新建一个
**答案：D**
**解析：** 虚拟线程不应池化每次任务新建一个。原因：池化的意义（复用昂贵资源）对虚拟线程不成立，限流应该用 Semaphore 控制并发数而非限制线程数。
**来源：** JC-079 · 虚拟线程（JDK 文档）

**Qconcurrency-1687（判断·误用）** 虚拟线程不应池化每次任务新建一个
**答案：对。** 解析：池化的意义（复用昂贵资源）对虚拟线程不成立，限流应该用 Semaphore 控制并发数而非限制线程数

**Qconcurrency-1688（判断·误用）** 虚拟线程也应该放进线程池
**答案：错。** 正确表述：虚拟线程不应池化每次任务新建一个。原因：池化的意义（复用昂贵资源）对虚拟线程不成立，限流应该用 Semaphore 控制并发数而非限制线程数

**Qconcurrency-1689（判断·误用）** 虚拟线程创建成本与平台线程相同
**答案：错。** 正确表述：虚拟线程不应池化每次任务新建一个。原因：池化的意义（复用昂贵资源）对虚拟线程不成立，限流应该用 Semaphore 控制并发数而非限制线程数

**Qconcurrency-1690（判断·误用）** Semaphore 不能用于虚拟线程限流
**答案：错。** 正确表述：虚拟线程不应池化每次任务新建一个。原因：池化的意义（复用昂贵资源）对虚拟线程不成立，限流应该用 Semaphore 控制并发数而非限制线程数

**Qconcurrency-1691（场景单选·误用）** 在工程实践中关于「池化」，下列做法符合推荐实践的是？
- A. Semaphore 不能用于虚拟线程限流
- B. 虚拟线程也应该放进线程池
- C. 虚拟线程创建成本与平台线程相同
- D. newVirtualThreadPerTaskExecutor 直接用
**答案：D**
**解析：** 推荐实践：newVirtualThreadPerTaskExecutor 直接用。事实依据：虚拟线程不应池化每次任务新建一个。

**Qconcurrency-1692（场景判断·误用）** 推荐实践：newVirtualThreadPerTaskExecutor 直接用
**答案：对。** 解析：虚拟线程不应池化每次任务新建一个。原因：池化的意义（复用昂贵资源）对虚拟线程不成立，限流应该用 Semaphore 控制并发数而非限制线程数

**Qconcurrency-1693（填空·误用）** 虚拟线程不应______每次任务新建一个
**答案：池化**。解析：池化的意义（复用昂贵资源）对虚拟线程不成立，限流应该用 Semaphore 控制并发数而非限制线程数

**Qconcurrency-1694（简答·误用）** 请说明「虚拟线程」中池化的机制与使用要点。
**要点（标准答案）**：① 虚拟线程不应池化每次任务新建一个；② 原理：池化的意义（复用昂贵资源）对虚拟线程不成立，限流应该用 Semaphore 控制并发数而非限制线程数；③ 使用要点：newVirtualThreadPerTaskExecutor 直接用。版本锚点：JDK 文档。

**Qconcurrency-1695（单选·正向·API）** 关于「虚拟线程」的说法，正确的是？
- A. 必须用专门框架才能创建
- B. 开启后所有线程自动变虚拟
- C. 虚拟线程是新的线程类型接口与 Thread 无关
- D. 创建虚拟线程的 API 是 Thread.ofVirtual().start() 或 Executors.newVirtualThreadPerTaskExecutor()
**答案：D**
**解析：** 创建虚拟线程的 API 是 Thread.ofVirtual().start() 或 Executors.newVirtualThreadPerTaskExecutor()。原因：与平台线程同一 Thread 抽象，可加名字便于排查，Spring Boot 3.2 开 spring.threads.virtual.enabled 一键切换。
**来源：** JC-080 · 虚拟线程（Spring Boot 3.2）

**Qconcurrency-1696（判断·API）** 创建虚拟线程的 API 是 Thread.ofVirtual().start() 或 Executors.newVirtualThreadPerTaskExecutor()
**答案：对。** 解析：与平台线程同一 Thread 抽象，可加名字便于排查，Spring Boot 3.2 开 spring.threads.virtual.enabled 一键切换

**Qconcurrency-1697（判断·API）** 虚拟线程是新的线程类型接口与 Thread 无关
**答案：错。** 正确表述：创建虚拟线程的 API 是 Thread.ofVirtual().start() 或 Executors.newVirtualThreadPerTaskExecutor()。原因：与平台线程同一 Thread 抽象，可加名字便于排查，Spring Boot 3.2 开 spring.threads.virtual.enabled 一键切换

**Qconcurrency-1698（判断·API）** 必须用专门框架才能创建
**答案：错。** 正确表述：创建虚拟线程的 API 是 Thread.ofVirtual().start() 或 Executors.newVirtualThreadPerTaskExecutor()。原因：与平台线程同一 Thread 抽象，可加名字便于排查，Spring Boot 3.2 开 spring.threads.virtual.enabled 一键切换

**Qconcurrency-1699（判断·API）** 开启后所有线程自动变虚拟
**答案：错。** 正确表述：创建虚拟线程的 API 是 Thread.ofVirtual().start() 或 Executors.newVirtualThreadPerTaskExecutor()。原因：与平台线程同一 Thread 抽象，可加名字便于排查，Spring Boot 3.2 开 spring.threads.virtual.enabled 一键切换

**Qconcurrency-1700（场景单选·API）** 在工程实践中关于「Thread.ofVirtual」，下列做法符合推荐实践的是？
- A. Tomcat 请求线程与 @Async 池切换虚拟线程
- B. 虚拟线程是新的线程类型接口与 Thread 无关
- C. 必须用专门框架才能创建
- D. 开启后所有线程自动变虚拟
**答案：A**
**解析：** 推荐实践：Tomcat 请求线程与 @Async 池切换虚拟线程。事实依据：创建虚拟线程的 API 是 Thread.ofVirtual().start() 或 Executors.newVirtualThreadPerTaskExecutor()。

**Qconcurrency-1701（场景判断·API）** 推荐实践：Tomcat 请求线程与 @Async 池切换虚拟线程
**答案：对。** 解析：创建虚拟线程的 API 是 Thread.ofVirtual().start() 或 Executors.newVirtualThreadPerTaskExecutor()。原因：与平台线程同一 Thread 抽象，可加名字便于排查，Spring Boot 3.2 开 spring.threads.virtual.enabled 一键切换

**Qconcurrency-1702（填空·API）** 创建虚拟线程的 API 是 ______().start() 或 Executors.newVirtualThreadPerTaskExecutor()
**答案：Thread.ofVirtual**。解析：与平台线程同一 Thread 抽象，可加名字便于排查，Spring Boot 3.2 开 spring.threads.virtual.enabled 一键切换

**Qconcurrency-1703（简答·API）** 请说明「虚拟线程」中Thread.ofVirtual的机制与使用要点。
**要点（标准答案）**：① 创建虚拟线程的 API 是 Thread.ofVirtual().start() 或 Executors.newVirtualThreadPerTaskExecutor()；② 原理：与平台线程同一 Thread 抽象，可加名字便于排查，Spring Boot 3.2 开 spring.threads.virtual.enabled 一键切换；③ 使用要点：Tomcat 请求线程与 @Async 池切换虚拟线程。版本锚点：Spring Boot 3.2。

**Qconcurrency-1704（单选·正向·排查）** 关于「死锁」的说法，正确的是？
- A. 死锁只有循环等待一个条件
- B. 死锁四条件：互斥、占有且等待、不可剥夺、循环等待
- C. 死锁会自动解除
- D. synchronized 不会发生死锁
**答案：B**
**解析：** 死锁四条件：互斥、占有且等待、不可剥夺、循环等待。原因：破坏任一条件即可预防：按序加锁破坏循环等待、tryLock 超时破坏占有等待，jstack 可直接检出死锁。
**来源：** JC-081 · 死锁（理论共识）

**Qconcurrency-1705（判断·排查）** 死锁四条件：互斥、占有且等待、不可剥夺、循环等待
**答案：对。** 解析：破坏任一条件即可预防：按序加锁破坏循环等待、tryLock 超时破坏占有等待，jstack 可直接检出死锁

**Qconcurrency-1706（判断·排查）** 死锁只有循环等待一个条件
**答案：错。** 正确表述：死锁四条件：互斥、占有且等待、不可剥夺、循环等待。原因：破坏任一条件即可预防：按序加锁破坏循环等待、tryLock 超时破坏占有等待，jstack 可直接检出死锁

**Qconcurrency-1707（判断·排查）** 死锁会自动解除
**答案：错。** 正确表述：死锁四条件：互斥、占有且等待、不可剥夺、循环等待。原因：破坏任一条件即可预防：按序加锁破坏循环等待、tryLock 超时破坏占有等待，jstack 可直接检出死锁

**Qconcurrency-1708（判断·排查）** synchronized 不会发生死锁
**答案：错。** 正确表述：死锁四条件：互斥、占有且等待、不可剥夺、循环等待。原因：破坏任一条件即可预防：按序加锁破坏循环等待、tryLock 超时破坏占有等待，jstack 可直接检出死锁

**Qconcurrency-1709（场景单选·排查）** 在工程实践中关于「死锁四条件」，下列做法符合推荐实践的是？
- A. 死锁只有循环等待一个条件
- B. synchronized 不会发生死锁
- C. 死锁会自动解除
- D. 转账互转场景必须按账户 ID 排序加锁
**答案：D**
**解析：** 推荐实践：转账互转场景必须按账户 ID 排序加锁。事实依据：死锁四条件：互斥、占有且等待、不可剥夺、循环等待。

**Qconcurrency-1710（场景判断·排查）** 推荐实践：转账互转场景必须按账户 ID 排序加锁
**答案：对。** 解析：死锁四条件：互斥、占有且等待、不可剥夺、循环等待。原因：破坏任一条件即可预防：按序加锁破坏循环等待、tryLock 超时破坏占有等待，jstack 可直接检出死锁

**Qconcurrency-1711（填空·排查）** ______：互斥、占有且等待、不可剥夺、循环等待
**答案：死锁四条件**。解析：破坏任一条件即可预防：按序加锁破坏循环等待、tryLock 超时破坏占有等待，jstack 可直接检出死锁

**Qconcurrency-1712（简答·排查）** 请说明「死锁」中死锁四条件的机制与使用要点。
**要点（标准答案）**：① 死锁四条件：互斥、占有且等待、不可剥夺、循环等待；② 原理：破坏任一条件即可预防：按序加锁破坏循环等待、tryLock 超时破坏占有等待，jstack 可直接检出死锁；③ 使用要点：转账互转场景必须按账户 ID 排序加锁。版本锚点：理论共识。

**Qconcurrency-1713（单选·正向·排查）** 关于「死锁」的说法，正确的是？
- A. 死锁需要人工分析才能发现
- B. jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁
- C. jstack 无法检测 ReentrantLock 死锁
- D. 发现死锁必须重启才能解除
**答案：B**
**解析：** jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁。原因：JVM 自动检测 monitor 与 JUC 锁的死锁，Arthas thread -b 一条命令定位死锁源头，ThreadMXBean.findDeadlockedThreads 可编程检测。
**来源：** JC-082 · 死锁（工具文档）

**Qconcurrency-1714（判断·排查）** jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁
**答案：对。** 解析：JVM 自动检测 monitor 与 JUC 锁的死锁，Arthas thread -b 一条命令定位死锁源头，ThreadMXBean.findDeadlockedThreads 可编程检测

**Qconcurrency-1715（判断·排查）** 死锁需要人工分析才能发现
**答案：错。** 正确表述：jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁。原因：JVM 自动检测 monitor 与 JUC 锁的死锁，Arthas thread -b 一条命令定位死锁源头，ThreadMXBean.findDeadlockedThreads 可编程检测

**Qconcurrency-1716（判断·排查）** jstack 无法检测 ReentrantLock 死锁
**答案：错。** 正确表述：jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁。原因：JVM 自动检测 monitor 与 JUC 锁的死锁，Arthas thread -b 一条命令定位死锁源头，ThreadMXBean.findDeadlockedThreads 可编程检测

**Qconcurrency-1717（判断·排查）** 发现死锁必须重启才能解除
**答案：错。** 正确表述：jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁。原因：JVM 自动检测 monitor 与 JUC 锁的死锁，Arthas thread -b 一条命令定位死锁源头，ThreadMXBean.findDeadlockedThreads 可编程检测

**Qconcurrency-1718（场景单选·排查）** 在工程实践中关于「jstack」，下列做法符合推荐实践的是？
- A. 生产 dump 排查第一入口
- B. 发现死锁必须重启才能解除
- C. jstack 无法检测 ReentrantLock 死锁
- D. 死锁需要人工分析才能发现
**答案：A**
**解析：** 推荐实践：生产 dump 排查第一入口。事实依据：jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁。

**Qconcurrency-1719（场景判断·排查）** 推荐实践：生产 dump 排查第一入口
**答案：对。** 解析：jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁。原因：JVM 自动检测 monitor 与 JUC 锁的死锁，Arthas thread -b 一条命令定位死锁源头，ThreadMXBean.findDeadlockedThreads 可编程检测

**Qconcurrency-1720（填空·排查）** ______ 输出末尾直接报告 Java-level deadlock 及涉及的锁
**答案：jstack**。解析：JVM 自动检测 monitor 与 JUC 锁的死锁，Arthas thread -b 一条命令定位死锁源头，ThreadMXBean.findDeadlockedThreads 可编程检测

**Qconcurrency-1721（简答·排查）** 请说明「死锁」中jstack的机制与使用要点。
**要点（标准答案）**：① jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁；② 原理：JVM 自动检测 monitor 与 JUC 锁的死锁，Arthas thread -b 一条命令定位死锁源头，ThreadMXBean.findDeadlockedThreads 可编程检测；③ 使用要点：生产 dump 排查第一入口。版本锚点：工具文档。

**Qconcurrency-1722（单选·正向·误用）** 关于「死锁」的说法，正确的是？
- A. String 常量做锁是常见推荐写法
- B. synchronized 的锁对象不能是字符串常量、包装类缓存值或可变引用
- C. 锁对象可以是任意对象随意选
- D. new String 做锁与常量等价
**答案：B**
**解析：** synchronized 的锁对象不能是字符串常量、包装类缓存值或可变引用。原因：字符串常量全局共享可能锁到别人的锁，Integer 缓存 -128~127 不同代码锁同一对象，可变引用被替换后两线程锁不同对象形同虚设。
**来源：** JC-083 · 死锁（实战教训）

**Qconcurrency-1723（判断·误用）** synchronized 的锁对象不能是字符串常量、包装类缓存值或可变引用
**答案：对。** 解析：字符串常量全局共享可能锁到别人的锁，Integer 缓存 -128~127 不同代码锁同一对象，可变引用被替换后两线程锁不同对象形同虚设

**Qconcurrency-1724（判断·误用）** 锁对象可以是任意对象随意选
**答案：错。** 正确表述：synchronized 的锁对象不能是字符串常量、包装类缓存值或可变引用。原因：字符串常量全局共享可能锁到别人的锁，Integer 缓存 -128~127 不同代码锁同一对象，可变引用被替换后两线程锁不同对象形同虚设

**Qconcurrency-1725（判断·误用）** String 常量做锁是常见推荐写法
**答案：错。** 正确表述：synchronized 的锁对象不能是字符串常量、包装类缓存值或可变引用。原因：字符串常量全局共享可能锁到别人的锁，Integer 缓存 -128~127 不同代码锁同一对象，可变引用被替换后两线程锁不同对象形同虚设

**Qconcurrency-1726（判断·误用）** new String 做锁与常量等价
**答案：错。** 正确表述：synchronized 的锁对象不能是字符串常量、包装类缓存值或可变引用。原因：字符串常量全局共享可能锁到别人的锁，Integer 缓存 -128~127 不同代码锁同一对象，可变引用被替换后两线程锁不同对象形同虚设

**Qconcurrency-1727（场景单选·误用）** 在工程实践中关于「锁对象」，下列做法符合推荐实践的是？
- A. new String 做锁与常量等价
- B. 锁对象可以是任意对象随意选
- C. 锁对象专用 final 字段（new Object 或专用锁类）
- D. String 常量做锁是常见推荐写法
**答案：C**
**解析：** 推荐实践：锁对象专用 final 字段（new Object 或专用锁类）。事实依据：synchronized 的锁对象不能是字符串常量、包装类缓存值或可变引用。

**Qconcurrency-1728（场景判断·误用）** 推荐实践：锁对象专用 final 字段（new Object 或专用锁类）
**答案：对。** 解析：synchronized 的锁对象不能是字符串常量、包装类缓存值或可变引用。原因：字符串常量全局共享可能锁到别人的锁，Integer 缓存 -128~127 不同代码锁同一对象，可变引用被替换后两线程锁不同对象形同虚设

**Qconcurrency-1729（填空·误用）** synchronized 的______不能是字符串常量、包装类缓存值或可变引用
**答案：锁对象**。解析：字符串常量全局共享可能锁到别人的锁，Integer 缓存 -128~127 不同代码锁同一对象，可变引用被替换后两线程锁不同对象形同虚设

**Qconcurrency-1730（简答·误用）** 请说明「死锁」中锁对象的机制与使用要点。
**要点（标准答案）**：① synchronized 的锁对象不能是字符串常量、包装类缓存值或可变引用；② 原理：字符串常量全局共享可能锁到别人的锁，Integer 缓存 -128~127 不同代码锁同一对象，可变引用被替换后两线程锁不同对象形同虚设；③ 使用要点：锁对象专用 final 字段（new Object 或专用锁类）。版本锚点：实战教训。

**Qconcurrency-1731（单选·正向·优化）** 关于「JIT」的说法，正确的是？
- A. 锁粗化会把一次锁拆成多次
- B. JIT 逃逸分析可做锁消除与锁粗化
- C. 锁消除是 JVM 运行时自动检测死锁
- D. 逃逸分析只是理论没有实际优化
**答案：B**
**解析：** JIT 逃逸分析可做锁消除与锁粗化。原因：对象不逃逸时其上的同步被整体删除（StringBuffer 局部使用场景），循环内反复加锁会被合并为一次，都是无感知的性能优化。
**来源：** JC-084 · JIT（HotSpot 文档）

**Qconcurrency-1732（判断·优化）** JIT 逃逸分析可做锁消除与锁粗化
**答案：对。** 解析：对象不逃逸时其上的同步被整体删除（StringBuffer 局部使用场景），循环内反复加锁会被合并为一次，都是无感知的性能优化

**Qconcurrency-1733（判断·优化）** 锁消除是 JVM 运行时自动检测死锁
**答案：错。** 正确表述：JIT 逃逸分析可做锁消除与锁粗化。原因：对象不逃逸时其上的同步被整体删除（StringBuffer 局部使用场景），循环内反复加锁会被合并为一次，都是无感知的性能优化

**Qconcurrency-1734（判断·优化）** 逃逸分析只是理论没有实际优化
**答案：错。** 正确表述：JIT 逃逸分析可做锁消除与锁粗化。原因：对象不逃逸时其上的同步被整体删除（StringBuffer 局部使用场景），循环内反复加锁会被合并为一次，都是无感知的性能优化

**Qconcurrency-1735（判断·优化）** 锁粗化会把一次锁拆成多次
**答案：错。** 正确表述：JIT 逃逸分析可做锁消除与锁粗化。原因：对象不逃逸时其上的同步被整体删除（StringBuffer 局部使用场景），循环内反复加锁会被合并为一次，都是无感知的性能优化

**Qconcurrency-1736（场景单选·优化）** 在工程实践中关于「锁消除」，下列做法符合推荐实践的是？
- A. 逃逸分析只是理论没有实际优化
- B. 锁消除是 JVM 运行时自动检测死锁
- C. 锁粗化会把一次锁拆成多次
- D. 性能分析时知道 JIT 会消除局部同步
**答案：D**
**解析：** 推荐实践：性能分析时知道 JIT 会消除局部同步。事实依据：JIT 逃逸分析可做锁消除与锁粗化。

**Qconcurrency-1737（场景判断·优化）** 推荐实践：性能分析时知道 JIT 会消除局部同步
**答案：对。** 解析：JIT 逃逸分析可做锁消除与锁粗化。原因：对象不逃逸时其上的同步被整体删除（StringBuffer 局部使用场景），循环内反复加锁会被合并为一次，都是无感知的性能优化

**Qconcurrency-1738（填空·优化）** JIT 逃逸分析可做______与锁粗化
**答案：锁消除**。解析：对象不逃逸时其上的同步被整体删除（StringBuffer 局部使用场景），循环内反复加锁会被合并为一次，都是无感知的性能优化

**Qconcurrency-1739（简答·优化）** 请说明「JIT」中锁消除的机制与使用要点。
**要点（标准答案）**：① JIT 逃逸分析可做锁消除与锁粗化；② 原理：对象不逃逸时其上的同步被整体删除（StringBuffer 局部使用场景），循环内反复加锁会被合并为一次，都是无感知的性能优化；③ 使用要点：性能分析时知道 JIT 会消除局部同步。版本锚点：HotSpot 文档。

**Qconcurrency-1740（单选·正向·选型）** 关于「并发容器」的说法，正确的是？
- A. CHM 不保证复合操作原子所以不如 synchronizedMap 安全
- B. Collections.synchronizedMap 全表一把锁性能远低于 ConcurrentHashMap
- C. synchronizedMap 与 CHM 性能相当
- D. synchronizedMap 读也无需锁
**答案：B**
**解析：** Collections.synchronizedMap 全表一把锁性能远低于 ConcurrentHashMap。原因：每次读写锁整表，复合操作仍需外部同步，CHM 桶级锁读无锁完胜，遗留代码迁移首选 CHM。
**来源：** JC-085 · 并发容器（JDK 文档）

**Qconcurrency-1741（判断·选型）** Collections.synchronizedMap 全表一把锁性能远低于 ConcurrentHashMap
**答案：对。** 解析：每次读写锁整表，复合操作仍需外部同步，CHM 桶级锁读无锁完胜，遗留代码迁移首选 CHM

**Qconcurrency-1742（判断·选型）** synchronizedMap 与 CHM 性能相当
**答案：错。** 正确表述：Collections.synchronizedMap 全表一把锁性能远低于 ConcurrentHashMap。原因：每次读写锁整表，复合操作仍需外部同步，CHM 桶级锁读无锁完胜，遗留代码迁移首选 CHM

**Qconcurrency-1743（判断·选型）** synchronizedMap 读也无需锁
**答案：错。** 正确表述：Collections.synchronizedMap 全表一把锁性能远低于 ConcurrentHashMap。原因：每次读写锁整表，复合操作仍需外部同步，CHM 桶级锁读无锁完胜，遗留代码迁移首选 CHM

**Qconcurrency-1744（判断·选型）** CHM 不保证复合操作原子所以不如 synchronizedMap 安全
**答案：错。** 正确表述：Collections.synchronizedMap 全表一把锁性能远低于 ConcurrentHashMap。原因：每次读写锁整表，复合操作仍需外部同步，CHM 桶级锁读无锁完胜，遗留代码迁移首选 CHM

**Qconcurrency-1745（场景单选·选型）** 在工程实践中关于「synchronizedMap」，下列做法符合推荐实践的是？
- A. synchronizedMap 读也无需锁
- B. CHM 不保证复合操作原子所以不如 synchronizedMap 安全
- C. 老代码 review 时识别并替换
- D. synchronizedMap 与 CHM 性能相当
**答案：C**
**解析：** 推荐实践：老代码 review 时识别并替换。事实依据：Collections.synchronizedMap 全表一把锁性能远低于 ConcurrentHashMap。

**Qconcurrency-1746（场景判断·选型）** 推荐实践：老代码 review 时识别并替换
**答案：对。** 解析：Collections.synchronizedMap 全表一把锁性能远低于 ConcurrentHashMap。原因：每次读写锁整表，复合操作仍需外部同步，CHM 桶级锁读无锁完胜，遗留代码迁移首选 CHM

**Qconcurrency-1747（填空·选型）** Collections.______ 全表一把锁性能远低于 ConcurrentHashMap
**答案：synchronizedMap**。解析：每次读写锁整表，复合操作仍需外部同步，CHM 桶级锁读无锁完胜，遗留代码迁移首选 CHM

**Qconcurrency-1748（简答·选型）** 请说明「并发容器」中synchronizedMap的机制与使用要点。
**要点（标准答案）**：① Collections.synchronizedMap 全表一把锁性能远低于 ConcurrentHashMap；② 原理：每次读写锁整表，复合操作仍需外部同步，CHM 桶级锁读无锁完胜，遗留代码迁移首选 CHM；③ 使用要点：老代码 review 时识别并替换。版本锚点：JDK 文档。

**Qconcurrency-1749（单选·正向·选型）** 关于「并发容器」的说法，正确的是？
- A. 跳表不支持范围查询
- B. 需要排序的并发 Map 用 ConcurrentSkipListMap（跳表）
- C. 跳表比红黑树内存更省
- D. ConcurrentSkipListMap 是 TreeMap 的线程安全版
**答案：B**
**解析：** 需要排序的并发 Map 用 ConcurrentSkipListMap（跳表）。原因：TreeMap 线程不安全，加锁 TreeMap 退化为全局锁，跳表天然支持无锁读与范围查询，Redis ZSet 同款结构。
**来源：** JC-086 · 并发容器（JDK 文档）

**Qconcurrency-1750（判断·选型）** 需要排序的并发 Map 用 ConcurrentSkipListMap（跳表）
**答案：对。** 解析：TreeMap 线程不安全，加锁 TreeMap 退化为全局锁，跳表天然支持无锁读与范围查询，Redis ZSet 同款结构

**Qconcurrency-1751（判断·选型）** ConcurrentSkipListMap 是 TreeMap 的线程安全版
**答案：错。** 正确表述：需要排序的并发 Map 用 ConcurrentSkipListMap（跳表）。原因：TreeMap 线程不安全，加锁 TreeMap 退化为全局锁，跳表天然支持无锁读与范围查询，Redis ZSet 同款结构

**Qconcurrency-1752（判断·选型）** 跳表比红黑树内存更省
**答案：错。** 正确表述：需要排序的并发 Map 用 ConcurrentSkipListMap（跳表）。原因：TreeMap 线程不安全，加锁 TreeMap 退化为全局锁，跳表天然支持无锁读与范围查询，Redis ZSet 同款结构

**Qconcurrency-1753（判断·选型）** 跳表不支持范围查询
**答案：错。** 正确表述：需要排序的并发 Map 用 ConcurrentSkipListMap（跳表）。原因：TreeMap 线程不安全，加锁 TreeMap 退化为全局锁，跳表天然支持无锁读与范围查询，Redis ZSet 同款结构

**Qconcurrency-1754（场景单选·选型）** 在工程实践中关于「ConcurrentSkipListMap」，下列做法符合推荐实践的是？
- A. 跳表比红黑树内存更省
- B. ConcurrentSkipListMap 是 TreeMap 的线程安全版
- C. 跳表不支持范围查询
- D. 并发+有序+范围查询场景
**答案：D**
**解析：** 推荐实践：并发+有序+范围查询场景。事实依据：需要排序的并发 Map 用 ConcurrentSkipListMap（跳表）。

**Qconcurrency-1755（场景判断·选型）** 推荐实践：并发+有序+范围查询场景
**答案：对。** 解析：需要排序的并发 Map 用 ConcurrentSkipListMap（跳表）。原因：TreeMap 线程不安全，加锁 TreeMap 退化为全局锁，跳表天然支持无锁读与范围查询，Redis ZSet 同款结构

**Qconcurrency-1756（填空·选型）** 需要排序的并发 Map 用 ______（跳表）
**答案：ConcurrentSkipListMap**。解析：TreeMap 线程不安全，加锁 TreeMap 退化为全局锁，跳表天然支持无锁读与范围查询，Redis ZSet 同款结构

**Qconcurrency-1757（简答·选型）** 请说明「并发容器」中ConcurrentSkipListMap的机制与使用要点。
**要点（标准答案）**：① 需要排序的并发 Map 用 ConcurrentSkipListMap（跳表）；② 原理：TreeMap 线程不安全，加锁 TreeMap 退化为全局锁，跳表天然支持无锁读与范围查询，Redis ZSet 同款结构；③ 使用要点：并发+有序+范围查询场景。版本锚点：JDK 文档。

**Qconcurrency-1758（单选·正向·LockSupport）** 关于「协作」的说法，正确的是？
- A. LockSupport.park 与 unpark 是 JUC 阻塞的底层原语
- B. LockSupport 与线程池强绑定
- C. park 会抛 InterruptedException
- D. unpark 必须在 park 之后调用才有效
**答案：A**
**解析：** LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。原因：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它。
**来源：** JC-087 · 协作（JDK 源码）

**Qconcurrency-1759（判断·LockSupport）** LockSupport.park 与 unpark 是 JUC 阻塞的底层原语
**答案：对。** 解析：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它

**Qconcurrency-1760（判断·LockSupport）** unpark 必须在 park 之后调用才有效
**答案：错。** 正确表述：LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。原因：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它

**Qconcurrency-1761（判断·LockSupport）** park 会抛 InterruptedException
**答案：错。** 正确表述：LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。原因：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它

**Qconcurrency-1762（判断·LockSupport）** LockSupport 与线程池强绑定
**答案：错。** 正确表述：LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。原因：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它

**Qconcurrency-1763（场景单选·LockSupport）** 在工程实践中关于「park」，下列做法符合推荐实践的是？
- A. 自定义同步器时使用
- B. park 会抛 InterruptedException
- C. LockSupport 与线程池强绑定
- D. unpark 必须在 park 之后调用才有效
**答案：A**
**解析：** 推荐实践：自定义同步器时使用。事实依据：LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。

**Qconcurrency-1764（场景判断·LockSupport）** 推荐实践：自定义同步器时使用
**答案：对。** 解析：LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。原因：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它

**Qconcurrency-1765（填空·LockSupport）** LockSupport.______ 与 unpark 是 JUC 阻塞的底层原语
**答案：park**。解析：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它

**Qconcurrency-1766（简答·LockSupport）** 请说明「协作」中park的机制与使用要点。
**要点（标准答案）**：① LockSupport.park 与 unpark 是 JUC 阻塞的底层原语；② 原理：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它；③ 使用要点：自定义同步器时使用。版本锚点：JDK 源码。

**Qconcurrency-1767（单选·正向·优先级）** 关于「线程基础」的说法，正确的是？
- A. 设置优先级可以解决饥饿
- B. 优先级高的线程一定先执行
- C. 优先级在 Linux 上完全无效
- D. 线程优先级只是提示不可作为正确性工具
**答案：D**
**解析：** 线程优先级只是提示不可作为正确性工具。原因：优先级映射到 OS 线程优先级但 JVM 不保证严格生效，跨平台行为不一致，正确性永远靠同步原语。
**来源：** JC-088 · 线程基础（JCiP）

**Qconcurrency-1768（判断·优先级）** 线程优先级只是提示不可作为正确性工具
**答案：对。** 解析：优先级映射到 OS 线程优先级但 JVM 不保证严格生效，跨平台行为不一致，正确性永远靠同步原语

**Qconcurrency-1769（判断·优先级）** 优先级高的线程一定先执行
**答案：错。** 正确表述：线程优先级只是提示不可作为正确性工具。原因：优先级映射到 OS 线程优先级但 JVM 不保证严格生效，跨平台行为不一致，正确性永远靠同步原语

**Qconcurrency-1770（判断·优先级）** 设置优先级可以解决饥饿
**答案：错。** 正确表述：线程优先级只是提示不可作为正确性工具。原因：优先级映射到 OS 线程优先级但 JVM 不保证严格生效，跨平台行为不一致，正确性永远靠同步原语

**Qconcurrency-1771（判断·优先级）** 优先级在 Linux 上完全无效
**答案：错。** 正确表述：线程优先级只是提示不可作为正确性工具。原因：优先级映射到 OS 线程优先级但 JVM 不保证严格生效，跨平台行为不一致，正确性永远靠同步原语

**Qconcurrency-1772（场景单选·优先级）** 在工程实践中关于「priority」，下列做法符合推荐实践的是？
- A. 设置优先级可以解决饥饿
- B. 优先级在 Linux 上完全无效
- C. 不要用优先级做业务调度
- D. 优先级高的线程一定先执行
**答案：C**
**解析：** 推荐实践：不要用优先级做业务调度。事实依据：线程优先级只是提示不可作为正确性工具。

**Qconcurrency-1773（场景判断·优先级）** 推荐实践：不要用优先级做业务调度
**答案：对。** 解析：线程优先级只是提示不可作为正确性工具。原因：优先级映射到 OS 线程优先级但 JVM 不保证严格生效，跨平台行为不一致，正确性永远靠同步原语

**Qconcurrency-1774（简答·优先级）** 请说明「线程基础」中priority的机制与使用要点。
**要点（标准答案）**：① 线程优先级只是提示不可作为正确性工具；② 原理：优先级映射到 OS 线程优先级但 JVM 不保证严格生效，跨平台行为不一致，正确性永远靠同步原语；③ 使用要点：不要用优先级做业务调度。版本锚点：JCiP。

**Qconcurrency-1775（单选·正向·yield）** 关于「线程基础」的说法，正确的是？
- A. yield 会释放持有的锁
- B. yield 只是提示调度器让出当前 CPU 无任何保证
- C. yield 保证低优先级线程执行
- D. yield 与 sleep 效果相同
**答案：B**
**解析：** yield 只是提示调度器让出当前 CPU 无任何保证。原因：可能立即被再次调度，也不保证让给谁，测试中用于模拟竞争但生产代码不依赖其语义。
**来源：** JC-089 · 线程基础（JDK 文档）

**Qconcurrency-1776（判断·yield）** yield 只是提示调度器让出当前 CPU 无任何保证
**答案：对。** 解析：可能立即被再次调度，也不保证让给谁，测试中用于模拟竞争但生产代码不依赖其语义

**Qconcurrency-1777（判断·yield）** yield 会释放持有的锁
**答案：错。** 正确表述：yield 只是提示调度器让出当前 CPU 无任何保证。原因：可能立即被再次调度，也不保证让给谁，测试中用于模拟竞争但生产代码不依赖其语义

**Qconcurrency-1778（判断·yield）** yield 保证低优先级线程执行
**答案：错。** 正确表述：yield 只是提示调度器让出当前 CPU 无任何保证。原因：可能立即被再次调度，也不保证让给谁，测试中用于模拟竞争但生产代码不依赖其语义

**Qconcurrency-1779（判断·yield）** yield 与 sleep 效果相同
**答案：错。** 正确表述：yield 只是提示调度器让出当前 CPU 无任何保证。原因：可能立即被再次调度，也不保证让给谁，测试中用于模拟竞争但生产代码不依赖其语义

**Qconcurrency-1780（场景单选·yield）** 在工程实践中关于「yield」，下列做法符合推荐实践的是？
- A. yield 保证低优先级线程执行
- B. 了解即可不用于业务逻辑
- C. yield 与 sleep 效果相同
- D. yield 会释放持有的锁
**答案：B**
**解析：** 推荐实践：了解即可不用于业务逻辑。事实依据：yield 只是提示调度器让出当前 CPU 无任何保证。

**Qconcurrency-1781（场景判断·yield）** 推荐实践：了解即可不用于业务逻辑
**答案：对。** 解析：yield 只是提示调度器让出当前 CPU 无任何保证。原因：可能立即被再次调度，也不保证让给谁，测试中用于模拟竞争但生产代码不依赖其语义

**Qconcurrency-1782（填空·yield）** ______ 只是提示调度器让出当前 CPU 无任何保证
**答案：yield**。解析：可能立即被再次调度，也不保证让给谁，测试中用于模拟竞争但生产代码不依赖其语义

**Qconcurrency-1783（简答·yield）** 请说明「线程基础」中yield的机制与使用要点。
**要点（标准答案）**：① yield 只是提示调度器让出当前 CPU 无任何保证；② 原理：可能立即被再次调度，也不保证让给谁，测试中用于模拟竞争但生产代码不依赖其语义；③ 使用要点：了解即可不用于业务逻辑。版本锚点：JDK 文档。

**Qconcurrency-1784（单选·正向·字段更新）** 关于「原子类」的说法，正确的是？
- A. AtomicIntegerFieldUpdater 反射式对普通 volatile 字段做原子操作
- B. private 字段也能更新
- C. 它比 AtomicReference 更慢
- D. 它能把普通字段变成原子字段无需 volatile
**答案：A**
**解析：** AtomicIntegerFieldUpdater 反射式对普通 volatile 字段做原子操作。原因：字段必须 volatile 且非 static 非 private，避免为每个对象包一层 AtomicReference 的内存开销，大批量对象（如节点）场景省内存。
**来源：** JC-090 · 原子类（JDK 文档）

**Qconcurrency-1785（判断·字段更新）** AtomicIntegerFieldUpdater 反射式对普通 volatile 字段做原子操作
**答案：对。** 解析：字段必须 volatile 且非 static 非 private，避免为每个对象包一层 AtomicReference 的内存开销，大批量对象（如节点）场景省内存

**Qconcurrency-1786（判断·字段更新）** 它能把普通字段变成原子字段无需 volatile
**答案：错。** 正确表述：AtomicIntegerFieldUpdater 反射式对普通 volatile 字段做原子操作。原因：字段必须 volatile 且非 static 非 private，避免为每个对象包一层 AtomicReference 的内存开销，大批量对象（如节点）场景省内存

**Qconcurrency-1787（判断·字段更新）** private 字段也能更新
**答案：错。** 正确表述：AtomicIntegerFieldUpdater 反射式对普通 volatile 字段做原子操作。原因：字段必须 volatile 且非 static 非 private，避免为每个对象包一层 AtomicReference 的内存开销，大批量对象（如节点）场景省内存

**Qconcurrency-1788（判断·字段更新）** 它比 AtomicReference 更慢
**答案：错。** 正确表述：AtomicIntegerFieldUpdater 反射式对普通 volatile 字段做原子操作。原因：字段必须 volatile 且非 static 非 private，避免为每个对象包一层 AtomicReference 的内存开销，大批量对象（如节点）场景省内存

**Qconcurrency-1789（场景单选·字段更新）** 在工程实践中关于「AtomicIntegerFieldUpdater」，下列做法符合推荐实践的是？
- A. 海量小对象内字段原子更新
- B. private 字段也能更新
- C. 它能把普通字段变成原子字段无需 volatile
- D. 它比 AtomicReference 更慢
**答案：A**
**解析：** 推荐实践：海量小对象内字段原子更新。事实依据：AtomicIntegerFieldUpdater 反射式对普通 volatile 字段做原子操作。

**Qconcurrency-1790（场景判断·字段更新）** 推荐实践：海量小对象内字段原子更新
**答案：对。** 解析：AtomicIntegerFieldUpdater 反射式对普通 volatile 字段做原子操作。原因：字段必须 volatile 且非 static 非 private，避免为每个对象包一层 AtomicReference 的内存开销，大批量对象（如节点）场景省内存

**Qconcurrency-1791（填空·字段更新）** ______ 反射式对普通 volatile 字段做原子操作
**答案：AtomicIntegerFieldUpdater**。解析：字段必须 volatile 且非 static 非 private，避免为每个对象包一层 AtomicReference 的内存开销，大批量对象（如节点）场景省内存

**Qconcurrency-1792（简答·字段更新）** 请说明「原子类」中AtomicIntegerFieldUpdater的机制与使用要点。
**要点（标准答案）**：① AtomicIntegerFieldUpdater 反射式对普通 volatile 字段做原子操作；② 原理：字段必须 volatile 且非 static 非 private，避免为每个对象包一层 AtomicReference 的内存开销，大批量对象（如节点）场景省内存；③ 使用要点：海量小对象内字段原子更新。版本锚点：JDK 文档。

**Qconcurrency-1793（单选·正向·预热线程）** 关于「线程池」的说法，正确的是？
- A. prestartAllCoreThreads 可提前创建所有核心线程避免冷启动抖动
- B. 核心线程在提交前就已全部创建
- C. 预热会降低内存使用
- D. 该方法是 Executors 快捷方法自带的
**答案：A**
**解析：** prestartAllCoreThreads 可提前创建所有核心线程避免冷启动抖动。原因：默认核心线程懒创建（来任务才建），突发流量首请求建线程有延迟，网关类服务可预热。
**来源：** JC-091 · 线程池（JDK 文档）

**Qconcurrency-1794（判断·预热线程）** prestartAllCoreThreads 可提前创建所有核心线程避免冷启动抖动
**答案：对。** 解析：默认核心线程懒创建（来任务才建），突发流量首请求建线程有延迟，网关类服务可预热

**Qconcurrency-1795（判断·预热线程）** 核心线程在提交前就已全部创建
**答案：错。** 正确表述：prestartAllCoreThreads 可提前创建所有核心线程避免冷启动抖动。原因：默认核心线程懒创建（来任务才建），突发流量首请求建线程有延迟，网关类服务可预热

**Qconcurrency-1796（判断·预热线程）** 该方法是 Executors 快捷方法自带的
**答案：错。** 正确表述：prestartAllCoreThreads 可提前创建所有核心线程避免冷启动抖动。原因：默认核心线程懒创建（来任务才建），突发流量首请求建线程有延迟，网关类服务可预热

**Qconcurrency-1797（判断·预热线程）** 预热会降低内存使用
**答案：错。** 正确表述：prestartAllCoreThreads 可提前创建所有核心线程避免冷启动抖动。原因：默认核心线程懒创建（来任务才建），突发流量首请求建线程有延迟，网关类服务可预热

**Qconcurrency-1798（场景单选·预热线程）** 在工程实践中关于「prestartAllCoreThreads」，下列做法符合推荐实践的是？
- A. 预热会降低内存使用
- B. 低延迟网关线程池预热
- C. 核心线程在提交前就已全部创建
- D. 该方法是 Executors 快捷方法自带的
**答案：B**
**解析：** 推荐实践：低延迟网关线程池预热。事实依据：prestartAllCoreThreads 可提前创建所有核心线程避免冷启动抖动。

**Qconcurrency-1799（场景判断·预热线程）** 推荐实践：低延迟网关线程池预热
**答案：对。** 解析：prestartAllCoreThreads 可提前创建所有核心线程避免冷启动抖动。原因：默认核心线程懒创建（来任务才建），突发流量首请求建线程有延迟，网关类服务可预热

**Qconcurrency-1800（填空·预热线程）** ______ 可提前创建所有核心线程避免冷启动抖动
**答案：prestartAllCoreThreads**。解析：默认核心线程懒创建（来任务才建），突发流量首请求建线程有延迟，网关类服务可预热

**Qconcurrency-1801（简答·预热线程）** 请说明「线程池」中prestartAllCoreThreads的机制与使用要点。
**要点（标准答案）**：① prestartAllCoreThreads 可提前创建所有核心线程避免冷启动抖动；② 原理：默认核心线程懒创建（来任务才建），突发流量首请求建线程有延迟，网关类服务可预热；③ 使用要点：低延迟网关线程池预热。版本锚点：JDK 文档。

**Qconcurrency-1802（单选·正向·64 位）** 关于「JMM」的说法，正确的是？
- A. long 撕裂会导致崩溃
- B. 所有基本类型读写都是原子的
- C. long 读写撕裂只在 32 位 JVM 发生
- D. 非 volatile 的 long 与 double 读写可能不是原子的（字撕裂）
**答案：D**
**解析：** 非 volatile 的 long 与 double 读写可能不是原子的（字撕裂）。原因：JLS 允许 64 位读写分两半执行，并发下可能读到高 32 位新值加低 32 位旧值，声明 volatile 即可保证原子性。
**来源：** JC-092 · JMM（JLS 17.7）

**Qconcurrency-1803（判断·64 位）** 非 volatile 的 long 与 double 读写可能不是原子的（字撕裂）
**答案：对。** 解析：JLS 允许 64 位读写分两半执行，并发下可能读到高 32 位新值加低 32 位旧值，声明 volatile 即可保证原子性

**Qconcurrency-1804（判断·64 位）** 所有基本类型读写都是原子的
**答案：错。** 正确表述：非 volatile 的 long 与 double 读写可能不是原子的（字撕裂）。原因：JLS 允许 64 位读写分两半执行，并发下可能读到高 32 位新值加低 32 位旧值，声明 volatile 即可保证原子性

**Qconcurrency-1805（判断·64 位）** long 读写撕裂只在 32 位 JVM 发生
**答案：错。** 正确表述：非 volatile 的 long 与 double 读写可能不是原子的（字撕裂）。原因：JLS 允许 64 位读写分两半执行，并发下可能读到高 32 位新值加低 32 位旧值，声明 volatile 即可保证原子性

**Qconcurrency-1806（判断·64 位）** long 撕裂会导致崩溃
**答案：错。** 正确表述：非 volatile 的 long 与 double 读写可能不是原子的（字撕裂）。原因：JLS 允许 64 位读写分两半执行，并发下可能读到高 32 位新值加低 32 位旧值，声明 volatile 即可保证原子性

**Qconcurrency-1807（场景单选·64 位）** 在工程实践中关于「double」，下列做法符合推荐实践的是？
- A. long 读写撕裂只在 32 位 JVM 发生
- B. 跨线程共享的 long 计数加 volatile
- C. 所有基本类型读写都是原子的
- D. long 撕裂会导致崩溃
**答案：B**
**解析：** 推荐实践：跨线程共享的 long 计数加 volatile。事实依据：非 volatile 的 long 与 double 读写可能不是原子的（字撕裂）。

**Qconcurrency-1808（场景判断·64 位）** 推荐实践：跨线程共享的 long 计数加 volatile
**答案：对。** 解析：非 volatile 的 long 与 double 读写可能不是原子的（字撕裂）。原因：JLS 允许 64 位读写分两半执行，并发下可能读到高 32 位新值加低 32 位旧值，声明 volatile 即可保证原子性

**Qconcurrency-1809（填空·64 位）** 非 volatile 的 long 与 ______ 读写可能不是原子的（字撕裂）
**答案：double**。解析：JLS 允许 64 位读写分两半执行，并发下可能读到高 32 位新值加低 32 位旧值，声明 volatile 即可保证原子性

**Qconcurrency-1810（简答·64 位）** 请说明「JMM」中double的机制与使用要点。
**要点（标准答案）**：① 非 volatile 的 long 与 double 读写可能不是原子的（字撕裂）；② 原理：JLS 允许 64 位读写分两半执行，并发下可能读到高 32 位新值加低 32 位旧值，声明 volatile 即可保证原子性；③ 使用要点：跨线程共享的 long 计数加 volatile。版本锚点：JLS 17.7。

**Qconcurrency-1811（单选·正向·Future）** 关于「异步」的说法，正确的是？
- A. get 阻塞时会自动释放线程池线程
- B. Future.get 默认有 30 秒超时
- C. Future.get 不传超时参数会无限阻塞
- D. 超时后任务自动取消
**答案：C**
**解析：** Future.get 不传超时参数会无限阻塞。原因：下游挂死则调用线程永久卡住，必须 get(timeout) 并处理 TimeoutException，或整体改 CF 加 orTimeout（JDK9+）。
**来源：** JC-093 · 异步（JDK 文档）

**Qconcurrency-1812（判断·Future）** Future.get 不传超时参数会无限阻塞
**答案：对。** 解析：下游挂死则调用线程永久卡住，必须 get(timeout) 并处理 TimeoutException，或整体改 CF 加 orTimeout（JDK9+）

**Qconcurrency-1813（判断·Future）** Future.get 默认有 30 秒超时
**答案：错。** 正确表述：Future.get 不传超时参数会无限阻塞。原因：下游挂死则调用线程永久卡住，必须 get(timeout) 并处理 TimeoutException，或整体改 CF 加 orTimeout（JDK9+）

**Qconcurrency-1814（判断·Future）** get 阻塞时会自动释放线程池线程
**答案：错。** 正确表述：Future.get 不传超时参数会无限阻塞。原因：下游挂死则调用线程永久卡住，必须 get(timeout) 并处理 TimeoutException，或整体改 CF 加 orTimeout（JDK9+）

**Qconcurrency-1815（判断·Future）** 超时后任务自动取消
**答案：错。** 正确表述：Future.get 不传超时参数会无限阻塞。原因：下游挂死则调用线程永久卡住，必须 get(timeout) 并处理 TimeoutException，或整体改 CF 加 orTimeout（JDK9+）

**Qconcurrency-1816（场景单选·Future）** 在工程实践中关于「get」，下列做法符合推荐实践的是？
- A. 所有远程调用 Future 必须带超时
- B. 超时后任务自动取消
- C. get 阻塞时会自动释放线程池线程
- D. Future.get 默认有 30 秒超时
**答案：A**
**解析：** 推荐实践：所有远程调用 Future 必须带超时。事实依据：Future.get 不传超时参数会无限阻塞。

**Qconcurrency-1817（场景判断·Future）** 推荐实践：所有远程调用 Future 必须带超时
**答案：对。** 解析：Future.get 不传超时参数会无限阻塞。原因：下游挂死则调用线程永久卡住，必须 get(timeout) 并处理 TimeoutException，或整体改 CF 加 orTimeout（JDK9+）

**Qconcurrency-1818（填空·Future）** Future.______ 不传超时参数会无限阻塞
**答案：get**。解析：下游挂死则调用线程永久卡住，必须 get(timeout) 并处理 TimeoutException，或整体改 CF 加 orTimeout（JDK9+）

**Qconcurrency-1819（简答·Future）** 请说明「异步」中get的机制与使用要点。
**要点（标准答案）**：① Future.get 不传超时参数会无限阻塞；② 原理：下游挂死则调用线程永久卡住，必须 get(timeout) 并处理 TimeoutException，或整体改 CF 加 orTimeout（JDK9+）；③ 使用要点：所有远程调用 Future 必须带超时。版本锚点：JDK 文档。

**Qconcurrency-1820（单选·正向·CompletableFuture）** 关于「异步」的说法，正确的是？
- A. JDK8 就有 orTimeout
- B. orTimeout 会中断正在执行的任务
- C. JDK9 引入 orTimeout 与 completeOnTimeout 给 CF 加超时
- D. 超时后底层任务立即停止
**答案：C**
**解析：** JDK9 引入 orTimeout 与 completeOnTimeout 给 CF 加超时。原因：超时不取消底层任务只是让 CF 以异常或默认值完成，任务线程仍可能在跑，彻底取消需要 cancel 配合任务自身响应中断。
**来源：** JC-094 · 异步（JDK9）

**Qconcurrency-1821（判断·CompletableFuture）** JDK9 引入 orTimeout 与 completeOnTimeout 给 CF 加超时
**答案：对。** 解析：超时不取消底层任务只是让 CF 以异常或默认值完成，任务线程仍可能在跑，彻底取消需要 cancel 配合任务自身响应中断

**Qconcurrency-1822（判断·CompletableFuture）** orTimeout 会中断正在执行的任务
**答案：错。** 正确表述：JDK9 引入 orTimeout 与 completeOnTimeout 给 CF 加超时。原因：超时不取消底层任务只是让 CF 以异常或默认值完成，任务线程仍可能在跑，彻底取消需要 cancel 配合任务自身响应中断

**Qconcurrency-1823（判断·CompletableFuture）** JDK8 就有 orTimeout
**答案：错。** 正确表述：JDK9 引入 orTimeout 与 completeOnTimeout 给 CF 加超时。原因：超时不取消底层任务只是让 CF 以异常或默认值完成，任务线程仍可能在跑，彻底取消需要 cancel 配合任务自身响应中断

**Qconcurrency-1824（判断·CompletableFuture）** 超时后底层任务立即停止
**答案：错。** 正确表述：JDK9 引入 orTimeout 与 completeOnTimeout 给 CF 加超时。原因：超时不取消底层任务只是让 CF 以异常或默认值完成，任务线程仍可能在跑，彻底取消需要 cancel 配合任务自身响应中断

**Qconcurrency-1825（场景单选·CompletableFuture）** 在工程实践中关于「orTimeout」，下列做法符合推荐实践的是？
- A. 超时后底层任务立即停止
- B. orTimeout 会中断正在执行的任务
- C. CF 链统一超时兜底
- D. JDK8 就有 orTimeout
**答案：C**
**解析：** 推荐实践：CF 链统一超时兜底。事实依据：JDK9 引入 orTimeout 与 completeOnTimeout 给 CF 加超时。

**Qconcurrency-1826（场景判断·CompletableFuture）** 推荐实践：CF 链统一超时兜底
**答案：对。** 解析：JDK9 引入 orTimeout 与 completeOnTimeout 给 CF 加超时。原因：超时不取消底层任务只是让 CF 以异常或默认值完成，任务线程仍可能在跑，彻底取消需要 cancel 配合任务自身响应中断

**Qconcurrency-1827（填空·CompletableFuture）** JDK9 引入 ______ 与 completeOnTimeout 给 CF 加超时
**答案：orTimeout**。解析：超时不取消底层任务只是让 CF 以异常或默认值完成，任务线程仍可能在跑，彻底取消需要 cancel 配合任务自身响应中断

**Qconcurrency-1828（简答·CompletableFuture）** 请说明「异步」中orTimeout的机制与使用要点。
**要点（标准答案）**：① JDK9 引入 orTimeout 与 completeOnTimeout 给 CF 加超时；② 原理：超时不取消底层任务只是让 CF 以异常或默认值完成，任务线程仍可能在跑，彻底取消需要 cancel 配合任务自身响应中断；③ 使用要点：CF 链统一超时兜底。版本锚点：JDK9。

**Qconcurrency-1829（单选·正向·Phaser）** 关于「协作」的说法，正确的是？
- A. Phaser 是更灵活的多阶段同步器可替代 CyclicBarrier 与 CountDownLatch
- B. Phaser 只能替代 CountDownLatch
- C. Phaser 参与方数量固定不可变
- D. Phaser 是 JDK21 新增
**答案：A**
**解析：** Phaser 是更灵活的多阶段同步器可替代 CyclicBarrier 与 CountDownLatch。原因：支持动态注册与注销参与方（一代一批），多阶段栅栏，JDK7 引入，了解层级低于前两者。
**来源：** JC-095 · 协作（JDK7）

**Qconcurrency-1830（判断·Phaser）** Phaser 是更灵活的多阶段同步器可替代 CyclicBarrier 与 CountDownLatch
**答案：对。** 解析：支持动态注册与注销参与方（一代一批），多阶段栅栏，JDK7 引入，了解层级低于前两者

**Qconcurrency-1831（判断·Phaser）** Phaser 只能替代 CountDownLatch
**答案：错。** 正确表述：Phaser 是更灵活的多阶段同步器可替代 CyclicBarrier 与 CountDownLatch。原因：支持动态注册与注销参与方（一代一批），多阶段栅栏，JDK7 引入，了解层级低于前两者

**Qconcurrency-1832（判断·Phaser）** Phaser 参与方数量固定不可变
**答案：错。** 正确表述：Phaser 是更灵活的多阶段同步器可替代 CyclicBarrier 与 CountDownLatch。原因：支持动态注册与注销参与方（一代一批），多阶段栅栏，JDK7 引入，了解层级低于前两者

**Qconcurrency-1833（判断·Phaser）** Phaser 是 JDK21 新增
**答案：错。** 正确表述：Phaser 是更灵活的多阶段同步器可替代 CyclicBarrier 与 CountDownLatch。原因：支持动态注册与注销参与方（一代一批），多阶段栅栏，JDK7 引入，了解层级低于前两者

**Qconcurrency-1834（场景单选·Phaser）** 在工程实践中关于「阶段」，下列做法符合推荐实践的是？
- A. Phaser 只能替代 CountDownLatch
- B. 动态成员的阶段性并行任务
- C. Phaser 是 JDK21 新增
- D. Phaser 参与方数量固定不可变
**答案：B**
**解析：** 推荐实践：动态成员的阶段性并行任务。事实依据：Phaser 是更灵活的多阶段同步器可替代 CyclicBarrier 与 CountDownLatch。

**Qconcurrency-1835（场景判断·Phaser）** 推荐实践：动态成员的阶段性并行任务
**答案：对。** 解析：Phaser 是更灵活的多阶段同步器可替代 CyclicBarrier 与 CountDownLatch。原因：支持动态注册与注销参与方（一代一批），多阶段栅栏，JDK7 引入，了解层级低于前两者

**Qconcurrency-1836（填空·Phaser）** Phaser 是更灵活的多______同步器可替代 CyclicBarrier 与 CountDownLatch
**答案：阶段**。解析：支持动态注册与注销参与方（一代一批），多阶段栅栏，JDK7 引入，了解层级低于前两者

**Qconcurrency-1837（简答·Phaser）** 请说明「协作」中阶段的机制与使用要点。
**要点（标准答案）**：① Phaser 是更灵活的多阶段同步器可替代 CyclicBarrier 与 CountDownLatch；② 原理：支持动态注册与注销参与方（一代一批），多阶段栅栏，JDK7 引入，了解层级低于前两者；③ 使用要点：动态成员的阶段性并行任务。版本锚点：JDK7。

**Qconcurrency-1838（单选·正向·ConcurrentLinkedDeque）** 关于「并发容器」的说法，正确的是？
- A. ConcurrentLinkedDeque 提供 CAS 无锁双端队列
- B. 只能单端操作
- C. 它是 BlockingDeque 实现
- D. 入队出队会阻塞
**答案：A**
**解析：** ConcurrentLinkedDeque 提供 CAS 无锁双端队列。原因：工作窃取、栈式 LIFO 并发场景，与 ConcurrentLinkedQueue 同为非阻塞族。
**来源：** JC-096 · 并发容器（JDK 文档）

**Qconcurrency-1839（判断·ConcurrentLinkedDeque）** ConcurrentLinkedDeque 提供 CAS 无锁双端队列
**答案：对。** 解析：工作窃取、栈式 LIFO 并发场景，与 ConcurrentLinkedQueue 同为非阻塞族

**Qconcurrency-1840（判断·ConcurrentLinkedDeque）** 它是 BlockingDeque 实现
**答案：错。** 正确表述：ConcurrentLinkedDeque 提供 CAS 无锁双端队列。原因：工作窃取、栈式 LIFO 并发场景，与 ConcurrentLinkedQueue 同为非阻塞族

**Qconcurrency-1841（判断·ConcurrentLinkedDeque）** 入队出队会阻塞
**答案：错。** 正确表述：ConcurrentLinkedDeque 提供 CAS 无锁双端队列。原因：工作窃取、栈式 LIFO 并发场景，与 ConcurrentLinkedQueue 同为非阻塞族

**Qconcurrency-1842（判断·ConcurrentLinkedDeque）** 只能单端操作
**答案：错。** 正确表述：ConcurrentLinkedDeque 提供 CAS 无锁双端队列。原因：工作窃取、栈式 LIFO 并发场景，与 ConcurrentLinkedQueue 同为非阻塞族

**Qconcurrency-1843（场景单选·ConcurrentLinkedDeque）** 在工程实践中关于「双端」，下列做法符合推荐实践的是？
- A. 非阻塞双端消费场景
- B. 它是 BlockingDeque 实现
- C. 入队出队会阻塞
- D. 只能单端操作
**答案：A**
**解析：** 推荐实践：非阻塞双端消费场景。事实依据：ConcurrentLinkedDeque 提供 CAS 无锁双端队列。

**Qconcurrency-1844（场景判断·ConcurrentLinkedDeque）** 推荐实践：非阻塞双端消费场景
**答案：对。** 解析：ConcurrentLinkedDeque 提供 CAS 无锁双端队列。原因：工作窃取、栈式 LIFO 并发场景，与 ConcurrentLinkedQueue 同为非阻塞族

**Qconcurrency-1845（填空·ConcurrentLinkedDeque）** ConcurrentLinkedDeque 提供 CAS 无锁______队列
**答案：双端**。解析：工作窃取、栈式 LIFO 并发场景，与 ConcurrentLinkedQueue 同为非阻塞族

**Qconcurrency-1846（简答·ConcurrentLinkedDeque）** 请说明「并发容器」中双端的机制与使用要点。
**要点（标准答案）**：① ConcurrentLinkedDeque 提供 CAS 无锁双端队列；② 原理：工作窃取、栈式 LIFO 并发场景，与 ConcurrentLinkedQueue 同为非阻塞族；③ 使用要点：非阻塞双端消费场景。版本锚点：JDK 文档。

**Qconcurrency-1847（单选·正向·队列选择）** 关于「线程池」的说法，正确的是？
- A. 拒绝策略选 Discard 最安全
- B. 生产线程池必须用有界队列加显式拒绝策略
- C. 无界队列吞吐更高所以更优
- D. 有界队列会导致线程频繁创建销毁
**答案：B**
**解析：** 生产线程池必须用有界队列加显式拒绝策略。原因：无界队列让 maximumPoolSize 与拒绝策略形同虚设，过载信号被延迟到 OOM 才暴露，有界队列+拒绝策略构成完整反压。
**来源：** JC-097 · 线程池（JCiP 8.x）

**Qconcurrency-1848（判断·队列选择）** 生产线程池必须用有界队列加显式拒绝策略
**答案：对。** 解析：无界队列让 maximumPoolSize 与拒绝策略形同虚设，过载信号被延迟到 OOM 才暴露，有界队列+拒绝策略构成完整反压

**Qconcurrency-1849（判断·队列选择）** 无界队列吞吐更高所以更优
**答案：错。** 正确表述：生产线程池必须用有界队列加显式拒绝策略。原因：无界队列让 maximumPoolSize 与拒绝策略形同虚设，过载信号被延迟到 OOM 才暴露，有界队列+拒绝策略构成完整反压

**Qconcurrency-1850（判断·队列选择）** 有界队列会导致线程频繁创建销毁
**答案：错。** 正确表述：生产线程池必须用有界队列加显式拒绝策略。原因：无界队列让 maximumPoolSize 与拒绝策略形同虚设，过载信号被延迟到 OOM 才暴露，有界队列+拒绝策略构成完整反压

**Qconcurrency-1851（判断·队列选择）** 拒绝策略选 Discard 最安全
**答案：错。** 正确表述：生产线程池必须用有界队列加显式拒绝策略。原因：无界队列让 maximumPoolSize 与拒绝策略形同虚设，过载信号被延迟到 OOM 才暴露，有界队列+拒绝策略构成完整反压

**Qconcurrency-1852（场景单选·队列选择）** 在工程实践中关于「有界」，下列做法符合推荐实践的是？
- A. 容量=峰值 QPS×可容忍延迟
- B. 拒绝策略选 Discard 最安全
- C. 有界队列会导致线程频繁创建销毁
- D. 无界队列吞吐更高所以更优
**答案：A**
**解析：** 推荐实践：容量=峰值 QPS×可容忍延迟。事实依据：生产线程池必须用有界队列加显式拒绝策略。

**Qconcurrency-1853（场景判断·队列选择）** 推荐实践：容量=峰值 QPS×可容忍延迟
**答案：对。** 解析：生产线程池必须用有界队列加显式拒绝策略。原因：无界队列让 maximumPoolSize 与拒绝策略形同虚设，过载信号被延迟到 OOM 才暴露，有界队列+拒绝策略构成完整反压

**Qconcurrency-1854（填空·队列选择）** 生产线程池必须用______队列加显式拒绝策略
**答案：有界**。解析：无界队列让 maximumPoolSize 与拒绝策略形同虚设，过载信号被延迟到 OOM 才暴露，有界队列+拒绝策略构成完整反压

**Qconcurrency-1855（简答·队列选择）** 请说明「线程池」中有界的机制与使用要点。
**要点（标准答案）**：① 生产线程池必须用有界队列加显式拒绝策略；② 原理：无界队列让 maximumPoolSize 与拒绝策略形同虚设，过载信号被延迟到 OOM 才暴露，有界队列+拒绝策略构成完整反压；③ 使用要点：容量=峰值 QPS×可容忍延迟。版本锚点：JCiP 8.x。

**Qconcurrency-1856（单选·正向·条件队列）** 关于「协作」的说法，正确的是？
- A. Condition 的 signal 不需要持有锁
- B. Condition 将等待队列从锁对象解耦支持一个锁多个条件队列
- C. Condition 与 Object.wait 可以混用
- D. 一个 ReentrantLock 只能有一个 Condition
**答案：B**
**解析：** Condition 将等待队列从锁对象解耦支持一个锁多个条件队列。原因：synchronized 只有一套 wait/notify，多条件必须 notifyAll 全员唤醒，ReentrantLock 多个 Condition 精准唤醒对应等待者，有界队列 ArrayBlockingQueue 即 notFull/notEmpty 双条件。
**来源：** JC-098 · 协作（JDK 源码）

**Qconcurrency-1857（判断·条件队列）** Condition 将等待队列从锁对象解耦支持一个锁多个条件队列
**答案：对。** 解析：synchronized 只有一套 wait/notify，多条件必须 notifyAll 全员唤醒，ReentrantLock 多个 Condition 精准唤醒对应等待者，有界队列 ArrayBlockingQueue 即 notFull/notEmpty 双条件

**Qconcurrency-1858（判断·条件队列）** 一个 ReentrantLock 只能有一个 Condition
**答案：错。** 正确表述：Condition 将等待队列从锁对象解耦支持一个锁多个条件队列。原因：synchronized 只有一套 wait/notify，多条件必须 notifyAll 全员唤醒，ReentrantLock 多个 Condition 精准唤醒对应等待者，有界队列 ArrayBlockingQueue 即 notFull/notEmpty 双条件

**Qconcurrency-1859（判断·条件队列）** Condition 的 signal 不需要持有锁
**答案：错。** 正确表述：Condition 将等待队列从锁对象解耦支持一个锁多个条件队列。原因：synchronized 只有一套 wait/notify，多条件必须 notifyAll 全员唤醒，ReentrantLock 多个 Condition 精准唤醒对应等待者，有界队列 ArrayBlockingQueue 即 notFull/notEmpty 双条件

**Qconcurrency-1860（判断·条件队列）** Condition 与 Object.wait 可以混用
**答案：错。** 正确表述：Condition 将等待队列从锁对象解耦支持一个锁多个条件队列。原因：synchronized 只有一套 wait/notify，多条件必须 notifyAll 全员唤醒，ReentrantLock 多个 Condition 精准唤醒对应等待者，有界队列 ArrayBlockingQueue 即 notFull/notEmpty 双条件

**Qconcurrency-1861（场景单选·条件队列）** 在工程实践中关于「Condition」，下列做法符合推荐实践的是？
- A. Condition 的 signal 不需要持有锁
- B. 生产者消费者分开唤醒用双 Condition
- C. 一个 ReentrantLock 只能有一个 Condition
- D. Condition 与 Object.wait 可以混用
**答案：B**
**解析：** 推荐实践：生产者消费者分开唤醒用双 Condition。事实依据：Condition 将等待队列从锁对象解耦支持一个锁多个条件队列。

**Qconcurrency-1862（场景判断·条件队列）** 推荐实践：生产者消费者分开唤醒用双 Condition
**答案：对。** 解析：Condition 将等待队列从锁对象解耦支持一个锁多个条件队列。原因：synchronized 只有一套 wait/notify，多条件必须 notifyAll 全员唤醒，ReentrantLock 多个 Condition 精准唤醒对应等待者，有界队列 ArrayBlockingQueue 即 notFull/notEmpty 双条件

**Qconcurrency-1863（填空·条件队列）** ______ 将等待队列从锁对象解耦支持一个锁多个条件队列
**答案：Condition**。解析：synchronized 只有一套 wait/notify，多条件必须 notifyAll 全员唤醒，ReentrantLock 多个 Condition 精准唤醒对应等待者，有界队列 ArrayBlockingQueue 即 notFull/notEmpty 双条件

**Qconcurrency-1864（简答·条件队列）** 请说明「协作」中Condition的机制与使用要点。
**要点（标准答案）**：① Condition 将等待队列从锁对象解耦支持一个锁多个条件队列；② 原理：synchronized 只有一套 wait/notify，多条件必须 notifyAll 全员唤醒，ReentrantLock 多个 Condition 精准唤醒对应等待者，有界队列 ArrayBlockingQueue 即 notFull/notEmpty 双条件；③ 使用要点：生产者消费者分开唤醒用双 Condition。版本锚点：JDK 源码。

**Qconcurrency-1865（单选·正向·Deque）** 关于「并发容器」的说法，正确的是？
- A. ArrayDeque 有容量上限不可扩容
- B. LinkedList 做队列性能最优
- C. ArrayDeque 是循环数组双端队列性能优于 Stack 与 LinkedList
- D. Stack 是推荐的栈实现
**答案：C**
**解析：** ArrayDeque 是循环数组双端队列性能优于 Stack 与 LinkedList。原因：官方明确推荐替代 Stack（Stack 继承 Vector 带锁开销），做队列也优于 LinkedList（缓存友好）。
**来源：** JC-099 · 并发容器（JDK 文档）

**Qconcurrency-1866（判断·Deque）** ArrayDeque 是循环数组双端队列性能优于 Stack 与 LinkedList
**答案：对。** 解析：官方明确推荐替代 Stack（Stack 继承 Vector 带锁开销），做队列也优于 LinkedList（缓存友好）

**Qconcurrency-1867（判断·Deque）** Stack 是推荐的栈实现
**答案：错。** 正确表述：ArrayDeque 是循环数组双端队列性能优于 Stack 与 LinkedList。原因：官方明确推荐替代 Stack（Stack 继承 Vector 带锁开销），做队列也优于 LinkedList（缓存友好）

**Qconcurrency-1868（判断·Deque）** ArrayDeque 有容量上限不可扩容
**答案：错。** 正确表述：ArrayDeque 是循环数组双端队列性能优于 Stack 与 LinkedList。原因：官方明确推荐替代 Stack（Stack 继承 Vector 带锁开销），做队列也优于 LinkedList（缓存友好）

**Qconcurrency-1869（判断·Deque）** LinkedList 做队列性能最优
**答案：错。** 正确表述：ArrayDeque 是循环数组双端队列性能优于 Stack 与 LinkedList。原因：官方明确推荐替代 Stack（Stack 继承 Vector 带锁开销），做队列也优于 LinkedList（缓存友好）

**Qconcurrency-1870（场景单选·Deque）** 在工程实践中关于「ArrayDeque」，下列做法符合推荐实践的是？
- A. LinkedList 做队列性能最优
- B. 栈一律 ArrayDeque
- C. ArrayDeque 有容量上限不可扩容
- D. Stack 是推荐的栈实现
**答案：B**
**解析：** 推荐实践：栈一律 ArrayDeque。事实依据：ArrayDeque 是循环数组双端队列性能优于 Stack 与 LinkedList。

**Qconcurrency-1871（场景判断·Deque）** 推荐实践：栈一律 ArrayDeque
**答案：对。** 解析：ArrayDeque 是循环数组双端队列性能优于 Stack 与 LinkedList。原因：官方明确推荐替代 Stack（Stack 继承 Vector 带锁开销），做队列也优于 LinkedList（缓存友好）

**Qconcurrency-1872（填空·Deque）** ______ 是循环数组双端队列性能优于 Stack 与 LinkedList
**答案：ArrayDeque**。解析：官方明确推荐替代 Stack（Stack 继承 Vector 带锁开销），做队列也优于 LinkedList（缓存友好）

**Qconcurrency-1873（简答·Deque）** 请说明「并发容器」中ArrayDeque的机制与使用要点。
**要点（标准答案）**：① ArrayDeque 是循环数组双端队列性能优于 Stack 与 LinkedList；② 原理：官方明确推荐替代 Stack（Stack 继承 Vector 带锁开销），做队列也优于 LinkedList（缓存友好）；③ 使用要点：栈一律 ArrayDeque。版本锚点：JDK 文档。

**Qconcurrency-1874（单选·正向·双重检查）** 关于「误用」的说法，正确的是？
- A. 无 volatile 的 DCL 在重排下可能发布半初始化对象
- B. JIT 不会做这种重排
- C. 半初始化问题只在老 JVM 存在
- D. DCL 加了 synchronized 就绝对安全
**答案：A**
**解析：** 无 volatile 的 DCL 在重排下可能发布半初始化对象。原因：new 的引用赋值可能先于构造执行，第二个线程首次判空后直接使用未初始化字段，加 volatile 禁止该重排。
**来源：** JC-100 · 误用（JSR-133）

**Qconcurrency-1875（判断·双重检查）** 无 volatile 的 DCL 在重排下可能发布半初始化对象
**答案：对。** 解析：new 的引用赋值可能先于构造执行，第二个线程首次判空后直接使用未初始化字段，加 volatile 禁止该重排

**Qconcurrency-1876（判断·双重检查）** DCL 加了 synchronized 就绝对安全
**答案：错。** 正确表述：无 volatile 的 DCL 在重排下可能发布半初始化对象。原因：new 的引用赋值可能先于构造执行，第二个线程首次判空后直接使用未初始化字段，加 volatile 禁止该重排

**Qconcurrency-1877（判断·双重检查）** 半初始化问题只在老 JVM 存在
**答案：错。** 正确表述：无 volatile 的 DCL 在重排下可能发布半初始化对象。原因：new 的引用赋值可能先于构造执行，第二个线程首次判空后直接使用未初始化字段，加 volatile 禁止该重排

**Qconcurrency-1878（判断·双重检查）** JIT 不会做这种重排
**答案：错。** 正确表述：无 volatile 的 DCL 在重排下可能发布半初始化对象。原因：new 的引用赋值可能先于构造执行，第二个线程首次判空后直接使用未初始化字段，加 volatile 禁止该重排

**Qconcurrency-1879（场景单选·双重检查）** 在工程实践中关于「volatile 缺失」，下列做法符合推荐实践的是？
- A. review 单例代码必查 volatile
- B. DCL 加了 synchronized 就绝对安全
- C. 半初始化问题只在老 JVM 存在
- D. JIT 不会做这种重排
**答案：A**
**解析：** 推荐实践：review 单例代码必查 volatile。事实依据：无 volatile 的 DCL 在重排下可能发布半初始化对象。

**Qconcurrency-1880（场景判断·双重检查）** 推荐实践：review 单例代码必查 volatile
**答案：对。** 解析：无 volatile 的 DCL 在重排下可能发布半初始化对象。原因：new 的引用赋值可能先于构造执行，第二个线程首次判空后直接使用未初始化字段，加 volatile 禁止该重排

**Qconcurrency-1881（简答·双重检查）** 请说明「误用」中volatile 缺失的机制与使用要点。
**要点（标准答案）**：① 无 volatile 的 DCL 在重排下可能发布半初始化对象；② 原理：new 的引用赋值可能先于构造执行，第二个线程首次判空后直接使用未初始化字段，加 volatile 禁止该重排；③ 使用要点：review 单例代码必查 volatile。版本锚点：JSR-133。

**Qconcurrency-1882（单选·正向·线程上下文）** 关于「异步」的说法，正确的是？
- A. 异步任务会丢失 ThreadLocal 上下文（traceId、用户态）
- B. traceId 天然跨线程
- C. InheritableThreadLocal 能解决线程池场景
- D. 线程池会自动复制 ThreadLocal
**答案：A**
**解析：** 异步任务会丢失 ThreadLocal 上下文（traceId、用户态）。原因：任务在池线程执行，ThreadLocal 停留在提交线程，需要显式捕获传递（阿里 TTL、Micrometer context-propagation）或改造为参数传递。
**来源：** JC-101 · 异步（实战经验）

**Qconcurrency-1883（判断·线程上下文）** 异步任务会丢失 ThreadLocal 上下文（traceId、用户态）
**答案：对。** 解析：任务在池线程执行，ThreadLocal 停留在提交线程，需要显式捕获传递（阿里 TTL、Micrometer context-propagation）或改造为参数传递

**Qconcurrency-1884（判断·线程上下文）** 线程池会自动复制 ThreadLocal
**答案：错。** 正确表述：异步任务会丢失 ThreadLocal 上下文（traceId、用户态）。原因：任务在池线程执行，ThreadLocal 停留在提交线程，需要显式捕获传递（阿里 TTL、Micrometer context-propagation）或改造为参数传递

**Qconcurrency-1885（判断·线程上下文）** InheritableThreadLocal 能解决线程池场景
**答案：错。** 正确表述：异步任务会丢失 ThreadLocal 上下文（traceId、用户态）。原因：任务在池线程执行，ThreadLocal 停留在提交线程，需要显式捕获传递（阿里 TTL、Micrometer context-propagation）或改造为参数传递

**Qconcurrency-1886（判断·线程上下文）** traceId 天然跨线程
**答案：错。** 正确表述：异步任务会丢失 ThreadLocal 上下文（traceId、用户态）。原因：任务在池线程执行，ThreadLocal 停留在提交线程，需要显式捕获传递（阿里 TTL、Micrometer context-propagation）或改造为参数传递

**Qconcurrency-1887（场景单选·线程上下文）** 在工程实践中关于「传递」，下列做法符合推荐实践的是？
- A. traceId 天然跨线程
- B. 埋点日志组件必须处理上下文传递
- C. 线程池会自动复制 ThreadLocal
- D. InheritableThreadLocal 能解决线程池场景
**答案：B**
**解析：** 推荐实践：埋点日志组件必须处理上下文传递。事实依据：异步任务会丢失 ThreadLocal 上下文（traceId、用户态）。

**Qconcurrency-1888（场景判断·线程上下文）** 推荐实践：埋点日志组件必须处理上下文传递
**答案：对。** 解析：异步任务会丢失 ThreadLocal 上下文（traceId、用户态）。原因：任务在池线程执行，ThreadLocal 停留在提交线程，需要显式捕获传递（阿里 TTL、Micrometer context-propagation）或改造为参数传递

**Qconcurrency-1889（简答·线程上下文）** 请说明「异步」中传递的机制与使用要点。
**要点（标准答案）**：① 异步任务会丢失 ThreadLocal 上下文（traceId、用户态）；② 原理：任务在池线程执行，ThreadLocal 停留在提交线程，需要显式捕获传递（阿里 TTL、Micrometer context-propagation）或改造为参数传递；③ 使用要点：埋点日志组件必须处理上下文传递。版本锚点：实战经验。

**Qconcurrency-1890（单选·正向·Snapshot）** 关于「并发容器」的说法，正确的是？
- A. 并发容器迭代器是弱一致的不抛 ConcurrentModificationException
- B. 弱一致等于错误数据必须加锁
- C. COW 与 CHM 迭代语义相同
- D. 并发容器迭代器会 fail-fast
**答案：A**
**解析：** 并发容器迭代器是弱一致的不抛 ConcurrentModificationException。原因：CHM/COW 的迭代器反映创建时或创建后的某状态，不保证看到后续修改，COW 是严格快照，CHM 是弱一致。
**来源：** JC-102 · 并发容器（JDK 文档）

**Qconcurrency-1891（判断·Snapshot）** 并发容器迭代器是弱一致的不抛 ConcurrentModificationException
**答案：对。** 解析：CHM/COW 的迭代器反映创建时或创建后的某状态，不保证看到后续修改，COW 是严格快照，CHM 是弱一致

**Qconcurrency-1892（判断·Snapshot）** 并发容器迭代器会 fail-fast
**答案：错。** 正确表述：并发容器迭代器是弱一致的不抛 ConcurrentModificationException。原因：CHM/COW 的迭代器反映创建时或创建后的某状态，不保证看到后续修改，COW 是严格快照，CHM 是弱一致

**Qconcurrency-1893（判断·Snapshot）** 弱一致等于错误数据必须加锁
**答案：错。** 正确表述：并发容器迭代器是弱一致的不抛 ConcurrentModificationException。原因：CHM/COW 的迭代器反映创建时或创建后的某状态，不保证看到后续修改，COW 是严格快照，CHM 是弱一致

**Qconcurrency-1894（判断·Snapshot）** COW 与 CHM 迭代语义相同
**答案：错。** 正确表述：并发容器迭代器是弱一致的不抛 ConcurrentModificationException。原因：CHM/COW 的迭代器反映创建时或创建后的某状态，不保证看到后续修改，COW 是严格快照，CHM 是弱一致

**Qconcurrency-1895（场景单选·Snapshot）** 在工程实践中关于「迭代器弱一致」，下列做法符合推荐实践的是？
- A. 弱一致等于错误数据必须加锁
- B. COW 与 CHM 迭代语义相同
- C. 并发容器迭代器会 fail-fast
- D. 遍历并发容器时理解弱一致语义即可
**答案：D**
**解析：** 推荐实践：遍历并发容器时理解弱一致语义即可。事实依据：并发容器迭代器是弱一致的不抛 ConcurrentModificationException。

**Qconcurrency-1896（场景判断·Snapshot）** 推荐实践：遍历并发容器时理解弱一致语义即可
**答案：对。** 解析：并发容器迭代器是弱一致的不抛 ConcurrentModificationException。原因：CHM/COW 的迭代器反映创建时或创建后的某状态，不保证看到后续修改，COW 是严格快照，CHM 是弱一致

**Qconcurrency-1897（简答·Snapshot）** 请说明「并发容器」中迭代器弱一致的机制与使用要点。
**要点（标准答案）**：① 并发容器迭代器是弱一致的不抛 ConcurrentModificationException；② 原理：CHM/COW 的迭代器反映创建时或创建后的某状态，不保证看到后续修改，COW 是严格快照，CHM 是弱一致；③ 使用要点：遍历并发容器时理解弱一致语义即可。版本锚点：JDK 文档。

**Qconcurrency-1898（单选·正向·隔离）** 关于「线程池」的说法，正确的是？
- A. 一个服务一个全局线程池最优
- B. 线程池隔离只对 CPU 密集任务有意义
- C. 不同业务的线程池必须隔离（舱壁模式）避免相互拖垮
- D. 隔离池数量越少越好
**答案：C**
**解析：** 不同业务的线程池必须隔离（舱壁模式）避免相互拖垮。原因：共用线程池时一个慢业务占满队列殃及全服务，按下游/重要性拆池（核心池、非核心池），配合 Hystrix/Sentinel 语义。
**来源：** JC-103 · 线程池（舱壁模式）

**Qconcurrency-1899（判断·隔离）** 不同业务的线程池必须隔离（舱壁模式）避免相互拖垮
**答案：对。** 解析：共用线程池时一个慢业务占满队列殃及全服务，按下游/重要性拆池（核心池、非核心池），配合 Hystrix/Sentinel 语义

**Qconcurrency-1900（判断·隔离）** 一个服务一个全局线程池最优
**答案：错。** 正确表述：不同业务的线程池必须隔离（舱壁模式）避免相互拖垮。原因：共用线程池时一个慢业务占满队列殃及全服务，按下游/重要性拆池（核心池、非核心池），配合 Hystrix/Sentinel 语义

**Qconcurrency-1901（判断·隔离）** 线程池隔离只对 CPU 密集任务有意义
**答案：错。** 正确表述：不同业务的线程池必须隔离（舱壁模式）避免相互拖垮。原因：共用线程池时一个慢业务占满队列殃及全服务，按下游/重要性拆池（核心池、非核心池），配合 Hystrix/Sentinel 语义

**Qconcurrency-1902（判断·隔离）** 隔离池数量越少越好
**答案：错。** 正确表述：不同业务的线程池必须隔离（舱壁模式）避免相互拖垮。原因：共用线程池时一个慢业务占满队列殃及全服务，按下游/重要性拆池（核心池、非核心池），配合 Hystrix/Sentinel 语义

**Qconcurrency-1903（场景单选·隔离）** 在工程实践中关于「舱壁」，下列做法符合推荐实践的是？
- A. 线程池隔离只对 CPU 密集任务有意义
- B. 一个服务一个全局线程池最优
- C. 核心交易与边缘任务分池
- D. 隔离池数量越少越好
**答案：C**
**解析：** 推荐实践：核心交易与边缘任务分池。事实依据：不同业务的线程池必须隔离（舱壁模式）避免相互拖垮。

**Qconcurrency-1904（场景判断·隔离）** 推荐实践：核心交易与边缘任务分池
**答案：对。** 解析：不同业务的线程池必须隔离（舱壁模式）避免相互拖垮。原因：共用线程池时一个慢业务占满队列殃及全服务，按下游/重要性拆池（核心池、非核心池），配合 Hystrix/Sentinel 语义

**Qconcurrency-1905（填空·隔离）** 不同业务的线程池必须隔离（______模式）避免相互拖垮
**答案：舱壁**。解析：共用线程池时一个慢业务占满队列殃及全服务，按下游/重要性拆池（核心池、非核心池），配合 Hystrix/Sentinel 语义

**Qconcurrency-1906（简答·隔离）** 请说明「线程池」中舱壁的机制与使用要点。
**要点（标准答案）**：① 不同业务的线程池必须隔离（舱壁模式）避免相互拖垮；② 原理：共用线程池时一个慢业务占满队列殃及全服务，按下游/重要性拆池（核心池、非核心池），配合 Hystrix/Sentinel 语义；③ 使用要点：核心交易与边缘任务分池。版本锚点：舱壁模式。

**Qconcurrency-1907（单选·正向·调度）** 关于「虚拟线程」的说法，正确的是？
- A. 调度器是平台线程池需手动创建
- B. 载体线程数等于虚拟线程数
- C. 并行度默认是 1
- D. 虚拟线程默认调度器是专用 ForkJoinPool（FIFO 模式）并行度默认 CPU 核数
**答案：D**
**解析：** 虚拟线程默认调度器是专用 ForkJoinPool（FIFO 模式）并行度默认 CPU 核数。原因：可用 jdk.virtualThreadScheduler.parallelism 调整，载体线程数少于虚拟线程数百万级，阻塞 IO 时载体立即被复用。
**来源：** JC-104 · 虚拟线程（JDK21 文档）

**Qconcurrency-1908（判断·调度）** 虚拟线程默认调度器是专用 ForkJoinPool（FIFO 模式）并行度默认 CPU 核数
**答案：对。** 解析：可用 jdk.virtualThreadScheduler.parallelism 调整，载体线程数少于虚拟线程数百万级，阻塞 IO 时载体立即被复用

**Qconcurrency-1909（判断·调度）** 载体线程数等于虚拟线程数
**答案：错。** 正确表述：虚拟线程默认调度器是专用 ForkJoinPool（FIFO 模式）并行度默认 CPU 核数。原因：可用 jdk.virtualThreadScheduler.parallelism 调整，载体线程数少于虚拟线程数百万级，阻塞 IO 时载体立即被复用

**Qconcurrency-1910（判断·调度）** 调度器是平台线程池需手动创建
**答案：错。** 正确表述：虚拟线程默认调度器是专用 ForkJoinPool（FIFO 模式）并行度默认 CPU 核数。原因：可用 jdk.virtualThreadScheduler.parallelism 调整，载体线程数少于虚拟线程数百万级，阻塞 IO 时载体立即被复用

**Qconcurrency-1911（判断·调度）** 并行度默认是 1
**答案：错。** 正确表述：虚拟线程默认调度器是专用 ForkJoinPool（FIFO 模式）并行度默认 CPU 核数。原因：可用 jdk.virtualThreadScheduler.parallelism 调整，载体线程数少于虚拟线程数百万级，阻塞 IO 时载体立即被复用

**Qconcurrency-1912（场景单选·调度）** 在工程实践中关于「carrier」，下列做法符合推荐实践的是？
- A. 调度器是平台线程池需手动创建
- B. 调优虚拟线程吞吐先调载体数
- C. 载体线程数等于虚拟线程数
- D. 并行度默认是 1
**答案：B**
**解析：** 推荐实践：调优虚拟线程吞吐先调载体数。事实依据：虚拟线程默认调度器是专用 ForkJoinPool（FIFO 模式）并行度默认 CPU 核数。

**Qconcurrency-1913（场景判断·调度）** 推荐实践：调优虚拟线程吞吐先调载体数
**答案：对。** 解析：虚拟线程默认调度器是专用 ForkJoinPool（FIFO 模式）并行度默认 CPU 核数。原因：可用 jdk.virtualThreadScheduler.parallelism 调整，载体线程数少于虚拟线程数百万级，阻塞 IO 时载体立即被复用

**Qconcurrency-1914（简答·调度）** 请说明「虚拟线程」中carrier的机制与使用要点。
**要点（标准答案）**：① 虚拟线程默认调度器是专用 ForkJoinPool（FIFO 模式）并行度默认 CPU 核数；② 原理：可用 jdk.virtualThreadScheduler.parallelism 调整，载体线程数少于虚拟线程数百万级，阻塞 IO 时载体立即被复用；③ 使用要点：调优虚拟线程吞吐先调载体数。版本锚点：JDK21 文档。

**Qconcurrency-1915（单选·正向·限流）** 关于「虚拟线程」的说法，正确的是？
- A. 限制虚拟线程数量即可限流
- B. Semaphore 与虚拟线程不兼容
- C. 限流只能靠网关
- D. 虚拟线程并发限流标准做法是 Semaphore
**答案：D**
**解析：** 虚拟线程并发限流标准做法是 Semaphore。原因：虚拟线程可无限创建，下游（数据库连接池）承受不了无限并发，acquire 许可形成背压，连接池本身就是天然限流器。
**来源：** JC-105 · 虚拟线程（JDK 文档）

**Qconcurrency-1916（判断·限流）** 虚拟线程并发限流标准做法是 Semaphore
**答案：对。** 解析：虚拟线程可无限创建，下游（数据库连接池）承受不了无限并发，acquire 许可形成背压，连接池本身就是天然限流器

**Qconcurrency-1917（判断·限流）** 限制虚拟线程数量即可限流
**答案：错。** 正确表述：虚拟线程并发限流标准做法是 Semaphore。原因：虚拟线程可无限创建，下游（数据库连接池）承受不了无限并发，acquire 许可形成背压，连接池本身就是天然限流器

**Qconcurrency-1918（判断·限流）** Semaphore 与虚拟线程不兼容
**答案：错。** 正确表述：虚拟线程并发限流标准做法是 Semaphore。原因：虚拟线程可无限创建，下游（数据库连接池）承受不了无限并发，acquire 许可形成背压，连接池本身就是天然限流器

**Qconcurrency-1919（判断·限流）** 限流只能靠网关
**答案：错。** 正确表述：虚拟线程并发限流标准做法是 Semaphore。原因：虚拟线程可无限创建，下游（数据库连接池）承受不了无限并发，acquire 许可形成背压，连接池本身就是天然限流器

**Qconcurrency-1920（场景单选·限流）** 在工程实践中关于「Semaphore」，下列做法符合推荐实践的是？
- A. Semaphore 与虚拟线程不兼容
- B. 限流只能靠网关
- C. 限制虚拟线程数量即可限流
- D. 虚拟线程 + Semaphore 是官方推荐组合
**答案：D**
**解析：** 推荐实践：虚拟线程 + Semaphore 是官方推荐组合。事实依据：虚拟线程并发限流标准做法是 Semaphore。

**Qconcurrency-1921（场景判断·限流）** 推荐实践：虚拟线程 + Semaphore 是官方推荐组合
**答案：对。** 解析：虚拟线程并发限流标准做法是 Semaphore。原因：虚拟线程可无限创建，下游（数据库连接池）承受不了无限并发，acquire 许可形成背压，连接池本身就是天然限流器

**Qconcurrency-1922（填空·限流）** 虚拟线程并发限流标准做法是 ______
**答案：Semaphore**。解析：虚拟线程可无限创建，下游（数据库连接池）承受不了无限并发，acquire 许可形成背压，连接池本身就是天然限流器

**Qconcurrency-1923（简答·限流）** 请说明「虚拟线程」中Semaphore的机制与使用要点。
**要点（标准答案）**：① 虚拟线程并发限流标准做法是 Semaphore；② 原理：虚拟线程可无限创建，下游（数据库连接池）承受不了无限并发，acquire 许可形成背压，连接池本身就是天然限流器；③ 使用要点：虚拟线程 + Semaphore 是官方推荐组合。版本锚点：JDK 文档。

**Qconcurrency-1924（单选·正向·getAndIncrement）** 关于「原子类」的说法，正确的是？
- A. AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）
- B. 它内部用了 synchronized
- C. 自旋次数有上限自动降级
- D. getAndIncrement 失败会阻塞等待
**答案：A**
**解析：** AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）。原因：高竞争下大量自旋浪费 CPU，这是 LongAdder 分段设计的动机，自旋次数可用性能工具观察。
**来源：** JC-106 · 原子类（JDK 源码）

**Qconcurrency-1925（判断·getAndIncrement）** AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）
**答案：对。** 解析：高竞争下大量自旋浪费 CPU，这是 LongAdder 分段设计的动机，自旋次数可用性能工具观察

**Qconcurrency-1926（判断·getAndIncrement）** getAndIncrement 失败会阻塞等待
**答案：错。** 正确表述：AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）。原因：高竞争下大量自旋浪费 CPU，这是 LongAdder 分段设计的动机，自旋次数可用性能工具观察

**Qconcurrency-1927（判断·getAndIncrement）** 它内部用了 synchronized
**答案：错。** 正确表述：AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）。原因：高竞争下大量自旋浪费 CPU，这是 LongAdder 分段设计的动机，自旋次数可用性能工具观察

**Qconcurrency-1928（判断·getAndIncrement）** 自旋次数有上限自动降级
**答案：错。** 正确表述：AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）。原因：高竞争下大量自旋浪费 CPU，这是 LongAdder 分段设计的动机，自旋次数可用性能工具观察

**Qconcurrency-1929（场景单选·getAndIncrement）** 在工程实践中关于「自旋」，下列做法符合推荐实践的是？
- A. 自旋次数有上限自动降级
- B. 理解无锁与阻塞的本质区别
- C. getAndIncrement 失败会阻塞等待
- D. 它内部用了 synchronized
**答案：B**
**解析：** 推荐实践：理解无锁与阻塞的本质区别。事实依据：AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）。

**Qconcurrency-1930（场景判断·getAndIncrement）** 推荐实践：理解无锁与阻塞的本质区别
**答案：对。** 解析：AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）。原因：高竞争下大量自旋浪费 CPU，这是 LongAdder 分段设计的动机，自旋次数可用性能工具观察

**Qconcurrency-1931（填空·getAndIncrement）** AtomicLong.getAndIncrement 失败后______重试（do-while CAS）
**答案：自旋**。解析：高竞争下大量自旋浪费 CPU，这是 LongAdder 分段设计的动机，自旋次数可用性能工具观察

**Qconcurrency-1932（简答·getAndIncrement）** 请说明「原子类」中自旋的机制与使用要点。
**要点（标准答案）**：① AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）；② 原理：高竞争下大量自旋浪费 CPU，这是 LongAdder 分段设计的动机，自旋次数可用性能工具观察；③ 使用要点：理解无锁与阻塞的本质区别。版本锚点：JDK 源码。

**Qconcurrency-1933（单选·正向·共享模式）** 关于「AQS」的说法，正确的是？
- A. 共享模式与独占模式不能共存
- B. AQS 支持独占与共享两种获取模式
- C. AQS 只支持独占锁
- D. CountDownLatch 是独占模式
**答案：B**
**解析：** AQS 支持独占与共享两种获取模式。原因：独占（ReentrantLock）一次一个线程，共享（Semaphore、CountDownLatch、读锁）可多个线程同时通过，tryAcquireShared 返回剩余量决定传播。
**来源：** JC-107 · AQS（JDK 源码）

**Qconcurrency-1934（判断·共享模式）** AQS 支持独占与共享两种获取模式
**答案：对。** 解析：独占（ReentrantLock）一次一个线程，共享（Semaphore、CountDownLatch、读锁）可多个线程同时通过，tryAcquireShared 返回剩余量决定传播

**Qconcurrency-1935（判断·共享模式）** AQS 只支持独占锁
**答案：错。** 正确表述：AQS 支持独占与共享两种获取模式。原因：独占（ReentrantLock）一次一个线程，共享（Semaphore、CountDownLatch、读锁）可多个线程同时通过，tryAcquireShared 返回剩余量决定传播

**Qconcurrency-1936（判断·共享模式）** 共享模式与独占模式不能共存
**答案：错。** 正确表述：AQS 支持独占与共享两种获取模式。原因：独占（ReentrantLock）一次一个线程，共享（Semaphore、CountDownLatch、读锁）可多个线程同时通过，tryAcquireShared 返回剩余量决定传播

**Qconcurrency-1937（判断·共享模式）** CountDownLatch 是独占模式
**答案：错。** 正确表述：AQS 支持独占与共享两种获取模式。原因：独占（ReentrantLock）一次一个线程，共享（Semaphore、CountDownLatch、读锁）可多个线程同时通过，tryAcquireShared 返回剩余量决定传播

**Qconcurrency-1938（场景单选·共享模式）** 在工程实践中关于「共享」，下列做法符合推荐实践的是？
- A. AQS 只支持独占锁
- B. 共享模式与独占模式不能共存
- C. CountDownLatch 是独占模式
- D. 区分读写锁与 CountDownLatch 的 AQS 用法
**答案：D**
**解析：** 推荐实践：区分读写锁与 CountDownLatch 的 AQS 用法。事实依据：AQS 支持独占与共享两种获取模式。

**Qconcurrency-1939（场景判断·共享模式）** 推荐实践：区分读写锁与 CountDownLatch 的 AQS 用法
**答案：对。** 解析：AQS 支持独占与共享两种获取模式。原因：独占（ReentrantLock）一次一个线程，共享（Semaphore、CountDownLatch、读锁）可多个线程同时通过，tryAcquireShared 返回剩余量决定传播

**Qconcurrency-1940（填空·共享模式）** AQS 支持独占与______两种获取模式
**答案：共享**。解析：独占（ReentrantLock）一次一个线程，共享（Semaphore、CountDownLatch、读锁）可多个线程同时通过，tryAcquireShared 返回剩余量决定传播

**Qconcurrency-1941（简答·共享模式）** 请说明「AQS」中共享的机制与使用要点。
**要点（标准答案）**：① AQS 支持独占与共享两种获取模式；② 原理：独占（ReentrantLock）一次一个线程，共享（Semaphore、CountDownLatch、读锁）可多个线程同时通过，tryAcquireShared 返回剩余量决定传播；③ 使用要点：区分读写锁与 CountDownLatch 的 AQS 用法。版本锚点：JDK 源码。

**Qconcurrency-1942（单选·正向·ConcurrentHashMap）** 关于「并发容器」的说法，正确的是？
- A. 并行遍历会修改容器
- B. bulk 操作默认串行
- C. CHM 遍历必须加锁
- D. CHM 支持并行 forEach 与 search 等 bulk 操作（JDK8+）
**答案：D**
**解析：** CHM 支持并行 forEach 与 search 等 bulk 操作（JDK8+）。原因：forEach(parallelismThreshold, action) 超过阈值的条目并行处理，search/findAny 语义，大数据量遍历可用。
**来源：** JC-108 · 并发容器（JDK8 文档）

**Qconcurrency-1943（判断·ConcurrentHashMap）** CHM 支持并行 forEach 与 search 等 bulk 操作（JDK8+）
**答案：对。** 解析：forEach(parallelismThreshold, action) 超过阈值的条目并行处理，search/findAny 语义，大数据量遍历可用

**Qconcurrency-1944（判断·ConcurrentHashMap）** CHM 遍历必须加锁
**答案：错。** 正确表述：CHM 支持并行 forEach 与 search 等 bulk 操作（JDK8+）。原因：forEach(parallelismThreshold, action) 超过阈值的条目并行处理，search/findAny 语义，大数据量遍历可用

**Qconcurrency-1945（判断·ConcurrentHashMap）** bulk 操作默认串行
**答案：错。** 正确表述：CHM 支持并行 forEach 与 search 等 bulk 操作（JDK8+）。原因：forEach(parallelismThreshold, action) 超过阈值的条目并行处理，search/findAny 语义，大数据量遍历可用

**Qconcurrency-1946（判断·ConcurrentHashMap）** 并行遍历会修改容器
**答案：错。** 正确表述：CHM 支持并行 forEach 与 search 等 bulk 操作（JDK8+）。原因：forEach(parallelismThreshold, action) 超过阈值的条目并行处理，search/findAny 语义，大数据量遍历可用

**Qconcurrency-1947（场景单选·ConcurrentHashMap）** 在工程实践中关于「foreach」，下列做法符合推荐实践的是？
- A. bulk 操作默认串行
- B. 离线统计任务用并行遍历
- C. CHM 遍历必须加锁
- D. 并行遍历会修改容器
**答案：B**
**解析：** 推荐实践：离线统计任务用并行遍历。事实依据：CHM 支持并行 forEach 与 search 等 bulk 操作（JDK8+）。

**Qconcurrency-1948（场景判断·ConcurrentHashMap）** 推荐实践：离线统计任务用并行遍历
**答案：对。** 解析：CHM 支持并行 forEach 与 search 等 bulk 操作（JDK8+）。原因：forEach(parallelismThreshold, action) 超过阈值的条目并行处理，search/findAny 语义，大数据量遍历可用

**Qconcurrency-1949（简答·ConcurrentHashMap）** 请说明「并发容器」中foreach的机制与使用要点。
**要点（标准答案）**：① CHM 支持并行 forEach 与 search 等 bulk 操作（JDK8+）；② 原理：forEach(parallelismThreshold, action) 超过阈值的条目并行处理，search/findAny 语义，大数据量遍历可用；③ 使用要点：离线统计任务用并行遍历。版本锚点：JDK8 文档。

**Qconcurrency-1950（单选·正向·预防）** 关于「死锁」的说法，正确的是？
- A. 死锁主要靠检测和恢复解决
- B. 按获取时间排序最有效
- C. ReentrantLock 天然防死锁
- D. 预防死锁最实用手段是全局一致的锁获取顺序
**答案：D**
**解析：** 预防死锁最实用手段是全局一致的锁获取顺序。原因：按业务键排序（账户 ID 从小到大）转账互转不再死锁，tryLock 超时回退是补充手段，这两招覆盖绝大多数死锁。
**来源：** JC-109 · 死锁（JCiP 10.x）

**Qconcurrency-1951（判断·预防）** 预防死锁最实用手段是全局一致的锁获取顺序
**答案：对。** 解析：按业务键排序（账户 ID 从小到大）转账互转不再死锁，tryLock 超时回退是补充手段，这两招覆盖绝大多数死锁

**Qconcurrency-1952（判断·预防）** 死锁主要靠检测和恢复解决
**答案：错。** 正确表述：预防死锁最实用手段是全局一致的锁获取顺序。原因：按业务键排序（账户 ID 从小到大）转账互转不再死锁，tryLock 超时回退是补充手段，这两招覆盖绝大多数死锁

**Qconcurrency-1953（判断·预防）** 按获取时间排序最有效
**答案：错。** 正确表述：预防死锁最实用手段是全局一致的锁获取顺序。原因：按业务键排序（账户 ID 从小到大）转账互转不再死锁，tryLock 超时回退是补充手段，这两招覆盖绝大多数死锁

**Qconcurrency-1954（判断·预防）** ReentrantLock 天然防死锁
**答案：错。** 正确表述：预防死锁最实用手段是全局一致的锁获取顺序。原因：按业务键排序（账户 ID 从小到大）转账互转不再死锁，tryLock 超时回退是补充手段，这两招覆盖绝大多数死锁

**Qconcurrency-1955（场景单选·预防）** 在工程实践中关于「锁排序」，下列做法符合推荐实践的是？
- A. 按获取时间排序最有效
- B. ReentrantLock 天然防死锁
- C. 死锁主要靠检测和恢复解决
- D. 转账、库存扣减等双资源场景
**答案：D**
**解析：** 推荐实践：转账、库存扣减等双资源场景。事实依据：预防死锁最实用手段是全局一致的锁获取顺序。

**Qconcurrency-1956（场景判断·预防）** 推荐实践：转账、库存扣减等双资源场景
**答案：对。** 解析：预防死锁最实用手段是全局一致的锁获取顺序。原因：按业务键排序（账户 ID 从小到大）转账互转不再死锁，tryLock 超时回退是补充手段，这两招覆盖绝大多数死锁

**Qconcurrency-1957（简答·预防）** 请说明「死锁」中锁排序的机制与使用要点。
**要点（标准答案）**：① 预防死锁最实用手段是全局一致的锁获取顺序；② 原理：按业务键排序（账户 ID 从小到大）转账互转不再死锁，tryLock 超时回退是补充手段，这两招覆盖绝大多数死锁；③ 使用要点：转账、库存扣减等双资源场景。版本锚点：JCiP 10.x。

**Qconcurrency-1958（单选·正向·CopyOnWriteArraySet）** 关于「并发容器」的说法，正确的是？
- A. 它底层是 HashMap
- B. 适合大集合高频写
- C. CopyOnWriteArraySet 内部是 CopyOnWriteArrayList 加 contains 去重
- D. contains 是 O(1)
**答案：C**
**解析：** CopyOnWriteArraySet 内部是 CopyOnWriteArrayList 加 contains 去重。原因：contains 是 O(n) 线性扫描，元素多时写与查询都慢，只适合极小且读极多的监听器集合。
**来源：** JC-110 · 并发容器（JDK 源码）

**Qconcurrency-1959（判断·CopyOnWriteArraySet）** CopyOnWriteArraySet 内部是 CopyOnWriteArrayList 加 contains 去重
**答案：对。** 解析：contains 是 O(n) 线性扫描，元素多时写与查询都慢，只适合极小且读极多的监听器集合

**Qconcurrency-1960（判断·CopyOnWriteArraySet）** 它底层是 HashMap
**答案：错。** 正确表述：CopyOnWriteArraySet 内部是 CopyOnWriteArrayList 加 contains 去重。原因：contains 是 O(n) 线性扫描，元素多时写与查询都慢，只适合极小且读极多的监听器集合

**Qconcurrency-1961（判断·CopyOnWriteArraySet）** contains 是 O(1)
**答案：错。** 正确表述：CopyOnWriteArraySet 内部是 CopyOnWriteArrayList 加 contains 去重。原因：contains 是 O(n) 线性扫描，元素多时写与查询都慢，只适合极小且读极多的监听器集合

**Qconcurrency-1962（判断·CopyOnWriteArraySet）** 适合大集合高频写
**答案：错。** 正确表述：CopyOnWriteArraySet 内部是 CopyOnWriteArrayList 加 contains 去重。原因：contains 是 O(n) 线性扫描，元素多时写与查询都慢，只适合极小且读极多的监听器集合

**Qconcurrency-1963（场景单选·CopyOnWriteArraySet）** 在工程实践中关于「实现」，下列做法符合推荐实践的是？
- A. contains 是 O(1)
- B. 适合大集合高频写
- C. 它底层是 HashMap
- D. 监听器、观察者集合
**答案：D**
**解析：** 推荐实践：监听器、观察者集合。事实依据：CopyOnWriteArraySet 内部是 CopyOnWriteArrayList 加 contains 去重。

**Qconcurrency-1964（场景判断·CopyOnWriteArraySet）** 推荐实践：监听器、观察者集合
**答案：对。** 解析：CopyOnWriteArraySet 内部是 CopyOnWriteArrayList 加 contains 去重。原因：contains 是 O(n) 线性扫描，元素多时写与查询都慢，只适合极小且读极多的监听器集合

**Qconcurrency-1965（简答·CopyOnWriteArraySet）** 请说明「并发容器」中实现的机制与使用要点。
**要点（标准答案）**：① CopyOnWriteArraySet 内部是 CopyOnWriteArrayList 加 contains 去重；② 原理：contains 是 O(n) 线性扫描，元素多时写与查询都慢，只适合极小且读极多的监听器集合；③ 使用要点：监听器、观察者集合。版本锚点：JDK 源码。

**Qconcurrency-1966（单选·反向·volatile）** 以下关于「volatile」的说法，**错误**的是？
- A. volatile 保证可见性与有序性，但不保证原子性
- B. volatile 的有序性靠编译器在读写前后插入内存屏障实现
- C. volatile 能保证 i++ 的原子性
- D. i++ 即使变量声明为 volatile 也不是线程安全的
**答案：C**
**解析：** 正确表述应为——volatile 保证可见性与有序性，但不保证原子性。原因：JMM 对 volatile 写强制刷新到主存、读强制从主存加载，并通过内存屏障禁止特定重排；但 i++ 这类复合操作仍是读-改-写三步。

**Qconcurrency-1967（单选·反向·JMM）** 以下关于「JMM」的说法，**错误**的是？
- A. happens-before 具有传递性可串起长链推理
- B. JMM 抽象为主内存与线程工作内存每线程有本地副本
- C. happens-before 是判断两个操作是否可见的核心规则而非时间先后
- D. happens-before 就是代码执行的先后顺序
**答案：D**
**解析：** 正确表述应为——happens-before 是判断两个操作是否可见的核心规则而非时间先后。原因：A happens-before B 意味着 A 的结果对 B 可见；程序顺序规则、锁的解锁加锁、volatile 写读、线程 start 与 join 都天然构成 happens-before。

**Qconcurrency-1968（单选·反向·synchronized）** 以下关于「synchronized」的说法，**错误**的是？
- A. synchronized 基于对象头的 monitor 机制实现互斥与可见性
- B. static synchronized 方法锁的是 Class 对象与实例锁互不冲突
- C. synchronized 是可重入锁同一线程可重复获取同一把锁
- D. synchronized 只保证互斥不保证可见性
**答案：D**
**解析：** 正确表述应为——synchronized 基于对象头的 monitor 机制实现互斥与可见性。原因：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应。

**Qconcurrency-1969（单选·反向·wait/notify）** 以下关于「wait/notify」的说法，**错误**的是？
- A. 任何线程都可以对任意对象调用 wait
- B. 等待条件必须用 while 循环判断而不能用 if 以防虚假唤醒
- C. wait 会释放当前持有的 monitor 而 Thread.sleep 不会释放任何锁
- D. wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException
**答案：A**
**解析：** 正确表述应为——wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException。原因：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常。

**Qconcurrency-1970（单选·反向·线程基础）** 以下关于「线程基础」的说法，**错误**的是？
- A. 对运行中的线程调用 interrupt 只是设置中断标志不会真正停止
- B. Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同
- C. 捕获 InterruptedException 后必须恢复中断标志或继续向上抛
- D. RUNNABLE 的线程一定在 CPU 上执行
**答案：D**
**解析：** 正确表述应为——Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同。原因：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版。

**Qconcurrency-1971（单选·反向·ThreadLocal）** 以下关于「ThreadLocal」的说法，**错误**的是？
- A. ThreadLocal 数据存在 ThreadLocal 对象里
- B. 每个 Thread 内部持有 ThreadLocalMap 以 ThreadLocal 为 key
- C. ThreadLocalMap 的 key 是弱引用 value 是强引用
- D. InheritableThreadLocal 只在子线程创建时拷贝一次在线程池场景失效
**答案：A**
**解析：** 正确表述应为——每个 Thread 内部持有 ThreadLocalMap 以 ThreadLocal 为 key。原因：数据实际存在线程对象里，多个线程访问同一个 ThreadLocal 变量读到的是各自的副本，天然隔离。

**Qconcurrency-1972（单选·反向·线程池）** 以下关于「线程池」的说法，**错误**的是？
- A. 任务提交顺序是：核心线程未满则创建核心线程，满了先入队，队列满了才扩到最大线程，再满才拒绝
- B. 线程池标准构造有 7 个参数：corePoolSize、maximumPoolSize、keepAliveTime、unit、workQueue、threadFactory、handler
- C. Executors.newFixedThreadPool 使用无界 LinkedBlockingQueue 可能堆积任务导致 OOM
- D. 线程池只有核心与非核心线程两个参数
**答案：D**
**解析：** 正确表述应为——线程池标准构造有 7 个参数：corePoolSize、maximumPoolSize、keepAliveTime、unit、workQueue、threadFactory、handler。原因：这是任务调度策略的全部输入，任何 Executors 快捷方法都是对它的包装且各有陷阱。

**Qconcurrency-1973（单选·反向·阻塞队列）** 以下关于「阻塞队列」的说法，**错误**的是？
- A. SynchronousQueue 没有容量每个 put 必须等 take 直接交接
- B. LinkedBlockingQueue 默认容量是 10
- C. ArrayBlockingQueue 是单锁有界数组队列
- D. LinkedBlockingQueue 不传容量参数时容量为 Integer.MAX_VALUE
**答案：B**
**解析：** 正确表述应为——LinkedBlockingQueue 不传容量参数时容量为 Integer.MAX_VALUE。原因：两把锁分离读写提高并发但默认容量形同无界，用在 newFixedThreadPool 就是 OOM 根源。

**Qconcurrency-1974（单选·反向·原子类）** 以下关于「原子类」的说法，**错误**的是？
- A. AtomicIntegerFieldUpdater 反射式对普通 volatile 字段做原子操作
- B. JDK9 引入 VarHandle 替代 Unsafe 提供安全的字段级原子操作
- C. 高竞争计数用 LongAdder 而非 AtomicLong
- D. LongAdder 在任何场景都快于 AtomicLong
**答案：D**
**解析：** 正确表述应为——高竞争计数用 LongAdder 而非 AtomicLong。原因：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级。

**Qconcurrency-1975（单选·反向·AQS）** 以下关于「AQS」的说法，**错误**的是？
- A. AQS 支持独占与共享两种获取模式
- B. AQS 在 JDK15 完成内部重构对外语义不变
- C. AQS 内部用 HashMap 管理等待线程
- D. AQS 核心是一个 volatile int state 加 CLH 变体等待队列
**答案：C**
**解析：** 正确表述应为——AQS 核心是一个 volatile int state 加 CLH 变体等待队列。原因：获取失败的线程封装成 Node 入队 park，释放时唤醒队首后继；state 语义由子类定义（重入次数、许可数、闩计数）。

**Qconcurrency-1976（单选·反向·显式锁）** 以下关于「显式锁」的说法，**错误**的是？
- A. ReentrantLock 相比 synchronized 增加可中断、超时与公平能力
- B. 默认是公平锁
- C. ReentrantReadWriteLock 允许读共享写独占且支持写锁降级为读锁
- D. ReentrantLock 默认非公平锁吞吐更高
**答案：B**
**解析：** 正确表述应为——ReentrantLock 默认非公平锁吞吐更高。原因：非公平允许新请求直接抢锁减少线程切换，公平锁按队列顺序避免饥饿但吞吐低，可构造函数选择。

**Qconcurrency-1977（单选·反向·协作工具）** 以下关于「协作工具」的说法，**错误**的是？
- A. CyclicBarrier 可重复使用且支持 barrierAction 回调
- B. CountDownLatch 计数不可重置用完即弃
- C. Semaphore 维护许可数用于限流与资源池
- D. CountDownLatch 可 reset 复用
**答案：D**
**解析：** 正确表述应为——CountDownLatch 计数不可重置用完即弃。原因：await 等计数到零，countDown 递减，构造时固定 count，重复使用需重建对象或改用 CyclicBarrier。

**Qconcurrency-1978（单选·反向·并发容器）** 以下关于「并发容器」的说法，**错误**的是？
- A. JDK8 的 ConcurrentHashMap 用 CAS 初始化与首节点插入加 synchronized 锁 bin 头实现分段写
- B. ConcurrentHashMap 不允许 null 键与 null 值
- C. CHM 的 size 通过 baseCount 加 CounterCell 数组汇总且是弱一致值
- D. CHM 使用 ReentrantLock 分段锁（那是 JDK7）
**答案：D**
**解析：** 正确表述应为——JDK8 的 ConcurrentHashMap 用 CAS 初始化与首节点插入加 synchronized 锁 bin 头实现分段写。原因：桶为空时 CAS 直接放节点，非空时 synchronized 锁住该 bin 首节点，锁粒度到桶，并发度等于桶数。

**Qconcurrency-1979（单选·反向·异步）** 以下关于「异步」的说法，**错误**的是？
- A. CompletableFuture 未指定线程时回调在完成线程或调用线程执行
- B. allOf 等全部完成 anyOf 任一完成 join/get 阻塞取结果
- C. supplyAsync 默认线程池是 ForkJoinPool.commonPool
- D. thenApply 总是在主线程执行
**答案：D**
**解析：** 正确表述应为——CompletableFuture 未指定线程时回调在完成线程或调用线程执行。原因：thenApply 不带 Async 由完成线程直接执行，thenApplyAsync(fn) 落到 ForkJoinPool.commonPool，IO 回调务必显式指定自定义线程池。

**Qconcurrency-1980（单选·反向·虚拟线程）** 以下关于「虚拟线程」的说法，**错误**的是？
- A. JDK21-23 中虚拟线程在 synchronized 块内阻塞会 pin 载体线程
- B. 虚拟线程能加速 CPU 计算任务
- C. 虚拟线程是 JDK21 正式特性由 JVM 调度到少量载体线程
- D. 虚拟线程不应池化每次任务新建一个
**答案：B**
**解析：** 正确表述应为——虚拟线程是 JDK21 正式特性由 JVM 调度到少量载体线程。原因：创建成本极低（栈在堆上）可开百万级，阻塞时让出载体线程由 JVM 换入下一个虚拟线程，面向 IO 密集高并发。

**Qconcurrency-1981（单选·反向·死锁）** 以下关于「死锁」的说法，**错误**的是？
- A. jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁
- B. 死锁四条件：互斥、占有且等待、不可剥夺、循环等待
- C. 死锁只有循环等待一个条件
- D. synchronized 的锁对象不能是字符串常量、包装类缓存值或可变引用
**答案：C**
**解析：** 正确表述应为——死锁四条件：互斥、占有且等待、不可剥夺、循环等待。原因：破坏任一条件即可预防：按序加锁破坏循环等待、tryLock 超时破坏占有等待，jstack 可直接检出死锁。

**Qconcurrency-1982（单选·反向·协作）** 以下关于「协作」的说法，**错误**的是？
- A. LockSupport.park 与 unpark 是 JUC 阻塞的底层原语
- B. Condition 将等待队列从锁对象解耦支持一个锁多个条件队列
- C. Phaser 是更灵活的多阶段同步器可替代 CyclicBarrier 与 CountDownLatch
- D. unpark 必须在 park 之后调用才有效
**答案：D**
**解析：** 正确表述应为——LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。原因：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它。

