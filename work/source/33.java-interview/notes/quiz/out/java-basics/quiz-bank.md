# 笔试题库 · Java基础（知识点 110 条）

**Qjava-basics-1000（单选·正向·语法语义）** 关于「String」的说法，正确的是？
- A. String 因为不可变所以性能一定比 StringBuilder 差。
- B. String 是不可变类：内部 value 数组为 final 且不提供修改方法。
- C. String 提供 setCharAt 方法可以原地修改字符。
- D. String 的 + 拼接在任何场景都等价于 StringBuilder。
**答案：B**
**解析：** String 是不可变类：内部 value 数组为 final 且不提供修改方法。。原因：不可变保证常量池安全共享、hashCode 可缓存、天然线程安全。。
**来源：** JB-001 · String（JDK9+ 底层从 char[] 改为 byte[]+coder（Compact Strings）。）

**Qjava-basics-1001（判断·语法语义）** String 是不可变类：内部 value 数组为 final 且不提供修改方法。
**答案：对。** 解析：不可变保证常量池安全共享、hashCode 可缓存、天然线程安全。

**Qjava-basics-1002（判断·语法语义）** String 提供 setCharAt 方法可以原地修改字符。
**答案：错。** 正确表述：String 是不可变类：内部 value 数组为 final 且不提供修改方法。。原因：不可变保证常量池安全共享、hashCode 可缓存、天然线程安全。

**Qjava-basics-1003（判断·语法语义）** String 因为不可变所以性能一定比 StringBuilder 差。
**答案：错。** 正确表述：String 是不可变类：内部 value 数组为 final 且不提供修改方法。。原因：不可变保证常量池安全共享、hashCode 可缓存、天然线程安全。

**Qjava-basics-1004（判断·语法语义）** String 的 + 拼接在任何场景都等价于 StringBuilder。
**答案：错。** 正确表述：String 是不可变类：内部 value 数组为 final 且不提供修改方法。。原因：不可变保证常量池安全共享、hashCode 可缓存、天然线程安全。

**Qjava-basics-1005（场景单选·语法语义）** 在工程实践中关于「不可变」，下列做法符合推荐实践的是？
- A. String 因为不可变所以性能一定比 StringBuilder 差。
- B. String 的 + 拼接在任何场景都等价于 StringBuilder。
- C. String 提供 setCharAt 方法可以原地修改字符。
- D. 防御式编程：对外暴露的字段如果是 String 可免防御性拷贝。
**答案：D**
**解析：** 推荐实践：防御式编程：对外暴露的字段如果是 String 可免防御性拷贝。。事实依据：String 是不可变类：内部 value 数组为 final 且不提供修改方法。。

**Qjava-basics-1006（场景判断·语法语义）** 推荐实践：防御式编程：对外暴露的字段如果是 String 可免防御性拷贝。
**答案：对。** 解析：String 是不可变类：内部 value 数组为 final 且不提供修改方法。。原因：不可变保证常量池安全共享、hashCode 可缓存、天然线程安全。

**Qjava-basics-1007（填空·语法语义）** String 是______类：内部 value 数组为 final 且不提供修改方法。
**答案：不可变**。解析：不可变保证常量池安全共享、hashCode 可缓存、天然线程安全。

**Qjava-basics-1008（简答·语法语义）** 请说明「String」中不可变的机制与使用要点。
**要点（标准答案）**：① String 是不可变类：内部 value 数组为 final 且不提供修改方法。；② 原理：不可变保证常量池安全共享、hashCode 可缓存、天然线程安全。；③ 使用要点：防御式编程：对外暴露的字段如果是 String 可免防御性拷贝。。版本锚点：JDK9+ 底层从 char[] 改为 byte[]+coder（Compact Strings）。。

**Qjava-basics-1009（单选·正向·内存）** 关于「String」的说法，正确的是？
- A. String 的 hashCode 在首次计算后缓存到内部 hash 字段，后续调用直接返回缓存值。
- B. String 的 hashCode 缓存需要手动开启。
- C. String 缓存 hashCode 会导致内存泄漏。
- D. String 的 hashCode 每次调用都会重新计算。
**答案：A**
**解析：** String 的 hashCode 在首次计算后缓存到内部 hash 字段，后续调用直接返回缓存值。。原因：String 不可变所以 hash 不会变化，缓存是安全的；作为 HashMap key 时避免重复计算。。
**来源：** JB-002 · String（JDK 8+ String 源码）

**Qjava-basics-1010（判断·内存）** String 的 hashCode 在首次计算后缓存到内部 hash 字段，后续调用直接返回缓存值。
**答案：对。** 解析：String 不可变所以 hash 不会变化，缓存是安全的；作为 HashMap key 时避免重复计算。

**Qjava-basics-1011（判断·内存）** String 的 hashCode 每次调用都会重新计算。
**答案：错。** 正确表述：String 的 hashCode 在首次计算后缓存到内部 hash 字段，后续调用直接返回缓存值。。原因：String 不可变所以 hash 不会变化，缓存是安全的；作为 HashMap key 时避免重复计算。

**Qjava-basics-1012（判断·内存）** String 的 hashCode 缓存需要手动开启。
**答案：错。** 正确表述：String 的 hashCode 在首次计算后缓存到内部 hash 字段，后续调用直接返回缓存值。。原因：String 不可变所以 hash 不会变化，缓存是安全的；作为 HashMap key 时避免重复计算。

**Qjava-basics-1013（判断·内存）** String 缓存 hashCode 会导致内存泄漏。
**答案：错。** 正确表述：String 的 hashCode 在首次计算后缓存到内部 hash 字段，后续调用直接返回缓存值。。原因：String 不可变所以 hash 不会变化，缓存是安全的；作为 HashMap key 时避免重复计算。

**Qjava-basics-1014（场景单选·内存）** 在工程实践中关于「hashCode缓存」，下列做法符合推荐实践的是？
- A. String 缓存 hashCode 会导致内存泄漏。
- B. 把不变对象作 HashMap key 的核心收益之一。
- C. String 的 hashCode 缓存需要手动开启。
- D. String 的 hashCode 每次调用都会重新计算。
**答案：B**
**解析：** 推荐实践：把不变对象作 HashMap key 的核心收益之一。。事实依据：String 的 hashCode 在首次计算后缓存到内部 hash 字段，后续调用直接返回缓存值。。

**Qjava-basics-1015（场景判断·内存）** 推荐实践：把不变对象作 HashMap key 的核心收益之一。
**答案：对。** 解析：String 的 hashCode 在首次计算后缓存到内部 hash 字段，后续调用直接返回缓存值。。原因：String 不可变所以 hash 不会变化，缓存是安全的；作为 HashMap key 时避免重复计算。

**Qjava-basics-1016（简答·内存）** 请说明「String」中hashCode缓存的机制与使用要点。
**要点（标准答案）**：① String 的 hashCode 在首次计算后缓存到内部 hash 字段，后续调用直接返回缓存值。；② 原理：String 不可变所以 hash 不会变化，缓存是安全的；作为 HashMap key 时避免重复计算。；③ 使用要点：把不变对象作 HashMap key 的核心收益之一。。版本锚点：JDK 8+ String 源码。

**Qjava-basics-1017（单选·正向·内存）** 关于「String」的说法，正确的是？
- A. 字符串常量池在 JDK7 后被彻底移除。
- B. 字符串常量池从 JDK7 起位于堆中，JDK6 及之前位于永久代。
- C. 字符串常量池位于栈内存。
- D. 字符串常量池在 JDK8 之后位于元空间。
**答案：B**
**解析：** 字符串常量池从 JDK7 起位于堆中，JDK6 及之前位于永久代。。原因：常量池入堆后可被 GC 回收，缓解永久代 OOM 问题。。
**来源：** JB-003 · String（JDK 7（常量池移入堆））

**Qjava-basics-1018（判断·内存）** 字符串常量池从 JDK7 起位于堆中，JDK6 及之前位于永久代。
**答案：对。** 解析：常量池入堆后可被 GC 回收，缓解永久代 OOM 问题。

**Qjava-basics-1019（判断·内存）** 字符串常量池在 JDK8 之后位于元空间。
**答案：错。** 正确表述：字符串常量池从 JDK7 起位于堆中，JDK6 及之前位于永久代。。原因：常量池入堆后可被 GC 回收，缓解永久代 OOM 问题。

**Qjava-basics-1020（判断·内存）** 字符串常量池位于栈内存。
**答案：错。** 正确表述：字符串常量池从 JDK7 起位于堆中，JDK6 及之前位于永久代。。原因：常量池入堆后可被 GC 回收，缓解永久代 OOM 问题。

**Qjava-basics-1021（判断·内存）** 字符串常量池在 JDK7 后被彻底移除。
**答案：错。** 正确表述：字符串常量池从 JDK7 起位于堆中，JDK6 及之前位于永久代。。原因：常量池入堆后可被 GC 回收，缓解永久代 OOM 问题。

**Qjava-basics-1022（场景单选·内存）** 在工程实践中关于「字符串常量池」，下列做法符合推荐实践的是？
- A. new String("x") 时字面量 x 入池、堆上另有副本对象。
- B. 字符串常量池在 JDK7 后被彻底移除。
- C. 字符串常量池在 JDK8 之后位于元空间。
- D. 字符串常量池位于栈内存。
**答案：A**
**解析：** 推荐实践：new String("x") 时字面量 x 入池、堆上另有副本对象。。事实依据：字符串常量池从 JDK7 起位于堆中，JDK6 及之前位于永久代。。

**Qjava-basics-1023（场景判断·内存）** 推荐实践：new String("x") 时字面量 x 入池、堆上另有副本对象。
**答案：对。** 解析：字符串常量池从 JDK7 起位于堆中，JDK6 及之前位于永久代。。原因：常量池入堆后可被 GC 回收，缓解永久代 OOM 问题。

**Qjava-basics-1024（填空·内存）** ______从 JDK7 起位于堆中，JDK6 及之前位于永久代。
**答案：字符串常量池**。解析：常量池入堆后可被 GC 回收，缓解永久代 OOM 问题。

**Qjava-basics-1025（简答·内存）** 请说明「String」中字符串常量池的机制与使用要点。
**要点（标准答案）**：① 字符串常量池从 JDK7 起位于堆中，JDK6 及之前位于永久代。；② 原理：常量池入堆后可被 GC 回收，缓解永久代 OOM 问题。；③ 使用要点：new String("x") 时字面量 x 入池、堆上另有副本对象。。版本锚点：JDK 7（常量池移入堆）。

**Qjava-basics-1026（单选·正向·内存）** 关于「String」的说法，正确的是？
- A. JDK7+ 的 intern() 对堆中已存在的等值字符串返回其自身引用（不再拷贝到池）。
- B. intern() 只对字面量有效，对拼接结果无效。
- C. intern() 会创建一个新的 String 对象。
- D. JDK7+ 的 intern() 一定会返回常量池中的新拷贝对象。
**答案：A**
**解析：** JDK7+ 的 intern() 对堆中已存在的等值字符串返回其自身引用（不再拷贝到池）。。原因：JDK6 intern 是拷贝进永久代所以返回值不同，JDK7 改为池中保存堆引用。。
**来源：** JB-004 · String（JDK7+）

**Qjava-basics-1027（判断·内存）** JDK7+ 的 intern() 对堆中已存在的等值字符串返回其自身引用（不再拷贝到池）。
**答案：对。** 解析：JDK6 intern 是拷贝进永久代所以返回值不同，JDK7 改为池中保存堆引用。

**Qjava-basics-1028（判断·内存）** JDK7+ 的 intern() 一定会返回常量池中的新拷贝对象。
**答案：错。** 正确表述：JDK7+ 的 intern() 对堆中已存在的等值字符串返回其自身引用（不再拷贝到池）。。原因：JDK6 intern 是拷贝进永久代所以返回值不同，JDK7 改为池中保存堆引用。

**Qjava-basics-1029（判断·内存）** intern() 会创建一个新的 String 对象。
**答案：错。** 正确表述：JDK7+ 的 intern() 对堆中已存在的等值字符串返回其自身引用（不再拷贝到池）。。原因：JDK6 intern 是拷贝进永久代所以返回值不同，JDK7 改为池中保存堆引用。

**Qjava-basics-1030（判断·内存）** intern() 只对字面量有效，对拼接结果无效。
**答案：错。** 正确表述：JDK7+ 的 intern() 对堆中已存在的等值字符串返回其自身引用（不再拷贝到池）。。原因：JDK6 intern 是拷贝进永久代所以返回值不同，JDK7 改为池中保存堆引用。

**Qjava-basics-1031（场景单选·内存）** 在工程实践中关于「intern」，下列做法符合推荐实践的是？
- A. 海量重复字符串场景 intern 可显著省内存（需评估 GC 压力）。
- B. intern() 会创建一个新的 String 对象。
- C. JDK7+ 的 intern() 一定会返回常量池中的新拷贝对象。
- D. intern() 只对字面量有效，对拼接结果无效。
**答案：A**
**解析：** 推荐实践：海量重复字符串场景 intern 可显著省内存（需评估 GC 压力）。。事实依据：JDK7+ 的 intern() 对堆中已存在的等值字符串返回其自身引用（不再拷贝到池）。。

**Qjava-basics-1032（场景判断·内存）** 推荐实践：海量重复字符串场景 intern 可显著省内存（需评估 GC 压力）。
**答案：对。** 解析：JDK7+ 的 intern() 对堆中已存在的等值字符串返回其自身引用（不再拷贝到池）。。原因：JDK6 intern 是拷贝进永久代所以返回值不同，JDK7 改为池中保存堆引用。

**Qjava-basics-1033（填空·内存）** JDK7+ 的 ______() 对堆中已存在的等值字符串返回其自身引用（不再拷贝到池）。
**答案：intern**。解析：JDK6 intern 是拷贝进永久代所以返回值不同，JDK7 改为池中保存堆引用。

**Qjava-basics-1034（简答·内存）** 请说明「String」中intern的机制与使用要点。
**要点（标准答案）**：① JDK7+ 的 intern() 对堆中已存在的等值字符串返回其自身引用（不再拷贝到池）。；② 原理：JDK6 intern 是拷贝进永久代所以返回值不同，JDK7 改为池中保存堆引用。；③ 使用要点：海量重复字符串场景 intern 可显著省内存（需评估 GC 压力）。。版本锚点：JDK7+。

**Qjava-basics-1035（单选·正向·版本）** 关于「String」的说法，正确的是？
- A. Compact Strings 会改变 String 的 hashCode 值。
- B. Compact Strings 改变了 String 不可变的语义。
- C. JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。
- D. JDK9 后 String 内部仍是 char 数组。
**答案：C**
**解析：** JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。。原因：纯拉丁字符存储只需 1 字节每字符，内存占用约省一半。。
**来源：** JB-005 · String（JDK9+）

**Qjava-basics-1036（判断·版本）** JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。
**答案：对。** 解析：纯拉丁字符存储只需 1 字节每字符，内存占用约省一半。

**Qjava-basics-1037（判断·版本）** JDK9 后 String 内部仍是 char 数组。
**答案：错。** 正确表述：JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。。原因：纯拉丁字符存储只需 1 字节每字符，内存占用约省一半。

**Qjava-basics-1038（判断·版本）** Compact Strings 改变了 String 不可变的语义。
**答案：错。** 正确表述：JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。。原因：纯拉丁字符存储只需 1 字节每字符，内存占用约省一半。

**Qjava-basics-1039（判断·版本）** Compact Strings 会改变 String 的 hashCode 值。
**答案：错。** 正确表述：JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。。原因：纯拉丁字符存储只需 1 字节每字符，内存占用约省一半。

**Qjava-basics-1040（场景单选·版本）** 在工程实践中关于「CompactStrings」，下列做法符合推荐实践的是？
- A. 纯 ASCII 内容大量存储时升级 JDK9+ 有可观内存收益。
- B. Compact Strings 会改变 String 的 hashCode 值。
- C. Compact Strings 改变了 String 不可变的语义。
- D. JDK9 后 String 内部仍是 char 数组。
**答案：A**
**解析：** 推荐实践：纯 ASCII 内容大量存储时升级 JDK9+ 有可观内存收益。。事实依据：JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。。

**Qjava-basics-1041（场景判断·版本）** 推荐实践：纯 ASCII 内容大量存储时升级 JDK9+ 有可观内存收益。
**答案：对。** 解析：JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。。原因：纯拉丁字符存储只需 1 字节每字符，内存占用约省一半。

**Qjava-basics-1042（填空·版本）** JDK9 引入 ______：String 底层从 char[] 改为 byte[] 加 coder 编码标记。
**答案：CompactStrings**。解析：纯拉丁字符存储只需 1 字节每字符，内存占用约省一半。

**Qjava-basics-1043（简答·版本）** 请说明「String」中CompactStrings的机制与使用要点。
**要点（标准答案）**：① JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。；② 原理：纯拉丁字符存储只需 1 字节每字符，内存占用约省一半。；③ 使用要点：纯 ASCII 内容大量存储时升级 JDK9+ 有可观内存收益。。版本锚点：JDK9+。

**Qjava-basics-1044（单选·正向·语法语义）** 关于「String」的说法，正确的是？
- A. String 的 hashCode 乘数是 131。
- B. String 的 hashCode 与内容顺序无关。
- C. 空字符串的 hashCode 是 -1。
- D. String 的 hashCode 算法为 s[0]*31^(n-1)+...+s[n-1]，乘数是 31。
**答案：D**
**解析：** String 的 hashCode 算法为 s[0]*31^(n-1)+...+s[n-1]，乘数是 31。。原因：31 是奇素数且 31*i 可优化为 (i<<5)-i 位运算；散列分布经大量字符串验证。。
**来源：** JB-006 · String（JDK 8+ 源码（31 乘子））

**Qjava-basics-1045（判断·语法语义）** String 的 hashCode 算法为 s[0]*31^(n-1)+...+s[n-1]，乘数是 31。
**答案：对。** 解析：31 是奇素数且 31*i 可优化为 (i<<5)-i 位运算；散列分布经大量字符串验证。

**Qjava-basics-1046（判断·语法语义）** String 的 hashCode 乘数是 131。
**答案：错。** 正确表述：String 的 hashCode 算法为 s[0]*31^(n-1)+...+s[n-1]，乘数是 31。。原因：31 是奇素数且 31*i 可优化为 (i<<5)-i 位运算；散列分布经大量字符串验证。

**Qjava-basics-1047（判断·语法语义）** String 的 hashCode 与内容顺序无关。
**答案：错。** 正确表述：String 的 hashCode 算法为 s[0]*31^(n-1)+...+s[n-1]，乘数是 31。。原因：31 是奇素数且 31*i 可优化为 (i<<5)-i 位运算；散列分布经大量字符串验证。

**Qjava-basics-1048（判断·语法语义）** 空字符串的 hashCode 是 -1。
**答案：错。** 正确表述：String 的 hashCode 算法为 s[0]*31^(n-1)+...+s[n-1]，乘数是 31。。原因：31 是奇素数且 31*i 可优化为 (i<<5)-i 位运算；散列分布经大量字符串验证。

**Qjava-basics-1049（场景单选·语法语义）** 在工程实践中关于「hashCode算法」，下列做法符合推荐实践的是？
- A. String 的 hashCode 乘数是 131。
- B. 面试可现场推 "abc"=97*31*31+98*31+99=96354。
- C. 空字符串的 hashCode 是 -1。
- D. String 的 hashCode 与内容顺序无关。
**答案：B**
**解析：** 推荐实践：面试可现场推 "abc"=97*31*31+98*31+99=96354。。事实依据：String 的 hashCode 算法为 s[0]*31^(n-1)+...+s[n-1]，乘数是 31。。

**Qjava-basics-1050（场景判断·语法语义）** 推荐实践：面试可现场推 "abc"=97*31*31+98*31+99=96354。
**答案：对。** 解析：String 的 hashCode 算法为 s[0]*31^(n-1)+...+s[n-1]，乘数是 31。。原因：31 是奇素数且 31*i 可优化为 (i<<5)-i 位运算；散列分布经大量字符串验证。

**Qjava-basics-1051（填空·语法语义）** String 的 ______为 s[0]*31^(n-1)+...+s[n-1]，乘数是 31。
**答案：hashCode算法**。解析：31 是奇素数且 31*i 可优化为 (i<<5)-i 位运算；散列分布经大量字符串验证。

**Qjava-basics-1052（简答·语法语义）** 请说明「String」中hashCode算法的机制与使用要点。
**要点（标准答案）**：① String 的 hashCode 算法为 s[0]*31^(n-1)+...+s[n-1]，乘数是 31。；② 原理：31 是奇素数且 31*i 可优化为 (i<<5)-i 位运算；散列分布经大量字符串验证。；③ 使用要点：面试可现场推 "abc"=97*31*31+98*31+99=96354。。版本锚点：JDK 8+ 源码（31 乘子）。

**Qjava-basics-1053（单选·正向·误用）** 关于「String」的说法，正确的是？
- A. equals 比较 String 会抛空指针且无法避免。
- B. == 对 String 内容相同就一定返回 true。
- C. 字符串比较用 == 是官方推荐写法。
- D. 比较 String 内容必须用 equals，== 只比较引用地址。
**答案：D**
**解析：** 比较 String 内容必须用 equals，== 只比较引用地址。。原因：== 在两个相同字面量（同入常量池）时碰巧为 true，造成"有时对有时错"的隐蔽 bug。。
**来源：** JB-007 · String（阿里手册强制条款）

**Qjava-basics-1054（判断·误用）** 比较 String 内容必须用 equals，== 只比较引用地址。
**答案：对。** 解析：== 在两个相同字面量（同入常量池）时碰巧为 true，造成"有时对有时错"的隐蔽 bug。

**Qjava-basics-1055（判断·误用）** == 对 String 内容相同就一定返回 true。
**答案：错。** 正确表述：比较 String 内容必须用 equals，== 只比较引用地址。。原因：== 在两个相同字面量（同入常量池）时碰巧为 true，造成"有时对有时错"的隐蔽 bug。

**Qjava-basics-1056（判断·误用）** equals 比较 String 会抛空指针且无法避免。
**答案：错。** 正确表述：比较 String 内容必须用 equals，== 只比较引用地址。。原因：== 在两个相同字面量（同入常量池）时碰巧为 true，造成"有时对有时错"的隐蔽 bug。

**Qjava-basics-1057（判断·误用）** 字符串比较用 == 是官方推荐写法。
**答案：错。** 正确表述：比较 String 内容必须用 equals，== 只比较引用地址。。原因：== 在两个相同字面量（同入常量池）时碰巧为 true，造成"有时对有时错"的隐蔽 bug。

**Qjava-basics-1058（场景单选·误用）** 在工程实践中关于「字符串比较」，下列做法符合推荐实践的是？
- A. 字符串比较用 == 是官方推荐写法。
- B. 方法入参接收外部字符串时一律 equals 且常量在前。
- C. == 对 String 内容相同就一定返回 true。
- D. equals 比较 String 会抛空指针且无法避免。
**答案：B**
**解析：** 推荐实践：方法入参接收外部字符串时一律 equals 且常量在前。。事实依据：比较 String 内容必须用 equals，== 只比较引用地址。。

**Qjava-basics-1059（场景判断·误用）** 推荐实践：方法入参接收外部字符串时一律 equals 且常量在前。
**答案：对。** 解析：比较 String 内容必须用 equals，== 只比较引用地址。。原因：== 在两个相同字面量（同入常量池）时碰巧为 true，造成"有时对有时错"的隐蔽 bug。

**Qjava-basics-1060（简答·误用）** 请说明「String」中字符串比较的机制与使用要点。
**要点（标准答案）**：① 比较 String 内容必须用 equals，== 只比较引用地址。；② 原理：== 在两个相同字面量（同入常量池）时碰巧为 true，造成"有时对有时错"的隐蔽 bug。；③ 使用要点：方法入参接收外部字符串时一律 equals 且常量在前。。版本锚点：阿里手册强制条款。

**Qjava-basics-1061（单选·正向·性能）** 关于「String」的说法，正确的是？
- A. 编译器会把循环内的 + 拼接优化成一个 StringBuilder 复用。
- B. 循环体内拼接字符串必须手动使用 StringBuilder（在循环外创建）。
- C. 循环拼接字符串对性能没有影响。
- D. StringBuffer 在单线程下比 StringBuilder 更快。
**答案：B**
**解析：** 循环体内拼接字符串必须手动使用 StringBuilder（在循环外创建）。。原因：循环内即使编译器改写，每轮也会新建 Builder 对象，产生大量临时对象与 GC 压力。。
**来源：** JB-008 · String（JDK9+）

**Qjava-basics-1062（判断·性能）** 循环体内拼接字符串必须手动使用 StringBuilder（在循环外创建）。
**答案：对。** 解析：循环内即使编译器改写，每轮也会新建 Builder 对象，产生大量临时对象与 GC 压力。

**Qjava-basics-1063（判断·性能）** 编译器会把循环内的 + 拼接优化成一个 StringBuilder 复用。
**答案：错。** 正确表述：循环体内拼接字符串必须手动使用 StringBuilder（在循环外创建）。。原因：循环内即使编译器改写，每轮也会新建 Builder 对象，产生大量临时对象与 GC 压力。

**Qjava-basics-1064（判断·性能）** 循环拼接字符串对性能没有影响。
**答案：错。** 正确表述：循环体内拼接字符串必须手动使用 StringBuilder（在循环外创建）。。原因：循环内即使编译器改写，每轮也会新建 Builder 对象，产生大量临时对象与 GC 压力。

**Qjava-basics-1065（判断·性能）** StringBuffer 在单线程下比 StringBuilder 更快。
**答案：错。** 正确表述：循环体内拼接字符串必须手动使用 StringBuilder（在循环外创建）。。原因：循环内即使编译器改写，每轮也会新建 Builder 对象，产生大量临时对象与 GC 压力。

**Qjava-basics-1066（场景单选·性能）** 在工程实践中关于「循环拼接」，下列做法符合推荐实践的是？
- A. JDK9+ 单行拼接走 StringConcatFactory，循环仍需手动 Builder。
- B. 循环拼接字符串对性能没有影响。
- C. 编译器会把循环内的 + 拼接优化成一个 StringBuilder 复用。
- D. StringBuffer 在单线程下比 StringBuilder 更快。
**答案：A**
**解析：** 推荐实践：JDK9+ 单行拼接走 StringConcatFactory，循环仍需手动 Builder。。事实依据：循环体内拼接字符串必须手动使用 StringBuilder（在循环外创建）。。

**Qjava-basics-1067（场景判断·性能）** 推荐实践：JDK9+ 单行拼接走 StringConcatFactory，循环仍需手动 Builder。
**答案：对。** 解析：循环体内拼接字符串必须手动使用 StringBuilder（在循环外创建）。。原因：循环内即使编译器改写，每轮也会新建 Builder 对象，产生大量临时对象与 GC 压力。

**Qjava-basics-1068（简答·性能）** 请说明「String」中循环拼接的机制与使用要点。
**要点（标准答案）**：① 循环体内拼接字符串必须手动使用 StringBuilder（在循环外创建）。；② 原理：循环内即使编译器改写，每轮也会新建 Builder 对象，产生大量临时对象与 GC 压力。；③ 使用要点：JDK9+ 单行拼接走 StringConcatFactory，循环仍需手动 Builder。。版本锚点：JDK9+。

**Qjava-basics-1069（单选·正向·版本）** 关于「String」的说法，正确的是？
- A. JDK9 之后字符串拼接退化成了手工 StringBuilder。
- B. JDK9+ 的字符串拼接由 javac 编译为 invokedynamic 调用 StringConcatFactory，运行时按拼接形态选择最优策略。
- C. 字符串拼接在 JDK9+ 全部变成了运行时反射调用。
- D. StringConcatFactory 只用于常量折叠。
**答案：B**
**解析：** JDK9+ 的字符串拼接由 javac 编译为 invokedynamic 调用 StringConcatFactory，运行时按拼接形态选择最优策略。。原因：相比 JDK8 固定生成 StringBuilder 链，策略化实现可预估长度、避免多余拷贝，基准更快。。
**来源：** JB-009 · String（JDK9+）

**Qjava-basics-1070（判断·版本）** JDK9+ 的字符串拼接由 javac 编译为 invokedynamic 调用 StringConcatFactory，运行时按拼接形态选择最优策略。
**答案：对。** 解析：相比 JDK8 固定生成 StringBuilder 链，策略化实现可预估长度、避免多余拷贝，基准更快。

**Qjava-basics-1071（判断·版本）** JDK9 之后字符串拼接退化成了手工 StringBuilder。
**答案：错。** 正确表述：JDK9+ 的字符串拼接由 javac 编译为 invokedynamic 调用 StringConcatFactory，运行时按拼接形态选择最优策略。。原因：相比 JDK8 固定生成 StringBuilder 链，策略化实现可预估长度、避免多余拷贝，基准更快。

**Qjava-basics-1072（判断·版本）** 字符串拼接在 JDK9+ 全部变成了运行时反射调用。
**答案：错。** 正确表述：JDK9+ 的字符串拼接由 javac 编译为 invokedynamic 调用 StringConcatFactory，运行时按拼接形态选择最优策略。。原因：相比 JDK8 固定生成 StringBuilder 链，策略化实现可预估长度、避免多余拷贝，基准更快。

**Qjava-basics-1073（判断·版本）** StringConcatFactory 只用于常量折叠。
**答案：错。** 正确表述：JDK9+ 的字符串拼接由 javac 编译为 invokedynamic 调用 StringConcatFactory，运行时按拼接形态选择最优策略。。原因：相比 JDK8 固定生成 StringBuilder 链，策略化实现可预估长度、避免多余拷贝，基准更快。

**Qjava-basics-1074（场景单选·版本）** 在工程实践中关于「字符串拼接底层」，下列做法符合推荐实践的是？
- A. StringConcatFactory 只用于常量折叠。
- B. 单行拼接不必手写 StringBuilder 的底层依据。
- C. 字符串拼接在 JDK9+ 全部变成了运行时反射调用。
- D. JDK9 之后字符串拼接退化成了手工 StringBuilder。
**答案：B**
**解析：** 推荐实践：单行拼接不必手写 StringBuilder 的底层依据。。事实依据：JDK9+ 的字符串拼接由 javac 编译为 invokedynamic 调用 StringConcatFactory，运行时按拼接形态选择最优策略。。

**Qjava-basics-1075（场景判断·版本）** 推荐实践：单行拼接不必手写 StringBuilder 的底层依据。
**答案：对。** 解析：JDK9+ 的字符串拼接由 javac 编译为 invokedynamic 调用 StringConcatFactory，运行时按拼接形态选择最优策略。。原因：相比 JDK8 固定生成 StringBuilder 链，策略化实现可预估长度、避免多余拷贝，基准更快。

**Qjava-basics-1076（简答·版本）** 请说明「String」中字符串拼接底层的机制与使用要点。
**要点（标准答案）**：① JDK9+ 的字符串拼接由 javac 编译为 invokedynamic 调用 StringConcatFactory，运行时按拼接形态选择最优策略。；② 原理：相比 JDK8 固定生成 StringBuilder 链，策略化实现可预估长度、避免多余拷贝，基准更快。；③ 使用要点：单行拼接不必手写 StringBuilder 的底层依据。。版本锚点：JDK9+。

**Qjava-basics-1077（单选·正向·误用）** 关于「String」的说法，正确的是？
- A. new String("abc") 在字面量已入池时额外创建 1 个堆对象，未入池时创建 2 个。
- B. new String 不涉及常量池。
- C. new String("abc") 只创建 1 个对象。
- D. new String("abc") 创建 3 个对象。
**答案：A**
**解析：** new String("abc") 在字面量已入池时额外创建 1 个堆对象，未入池时创建 2 个。。原因：字面量入池 + new 强制堆上新建副本，两者独立。。
**来源：** JB-010 · String（Java 语言通用语义）

**Qjava-basics-1078（判断·误用）** new String("abc") 在字面量已入池时额外创建 1 个堆对象，未入池时创建 2 个。
**答案：对。** 解析：字面量入池 + new 强制堆上新建副本，两者独立。

**Qjava-basics-1079（判断·误用）** new String("abc") 只创建 1 个对象。
**答案：错。** 正确表述：new String("abc") 在字面量已入池时额外创建 1 个堆对象，未入池时创建 2 个。。原因：字面量入池 + new 强制堆上新建副本，两者独立。

**Qjava-basics-1080（判断·误用）** new String("abc") 创建 3 个对象。
**答案：错。** 正确表述：new String("abc") 在字面量已入池时额外创建 1 个堆对象，未入池时创建 2 个。。原因：字面量入池 + new 强制堆上新建副本，两者独立。

**Qjava-basics-1081（判断·误用）** new String 不涉及常量池。
**答案：错。** 正确表述：new String("abc") 在字面量已入池时额外创建 1 个堆对象，未入池时创建 2 个。。原因：字面量入池 + new 强制堆上新建副本，两者独立。

**Qjava-basics-1082（场景单选·误用）** 在工程实践中关于「new String」，下列做法符合推荐实践的是？
- A. 代码里出现 new String(字面量) 基本都是误用，review 直接标记。
- B. new String("abc") 只创建 1 个对象。
- C. new String 不涉及常量池。
- D. new String("abc") 创建 3 个对象。
**答案：A**
**解析：** 推荐实践：代码里出现 new String(字面量) 基本都是误用，review 直接标记。。事实依据：new String("abc") 在字面量已入池时额外创建 1 个堆对象，未入池时创建 2 个。。

**Qjava-basics-1083（场景判断·误用）** 推荐实践：代码里出现 new String(字面量) 基本都是误用，review 直接标记。
**答案：对。** 解析：new String("abc") 在字面量已入池时额外创建 1 个堆对象，未入池时创建 2 个。。原因：字面量入池 + new 强制堆上新建副本，两者独立。

**Qjava-basics-1084（填空·误用）** ______("abc") 在字面量已入池时额外创建 1 个堆对象，未入池时创建 2 个。
**答案：new String**。解析：字面量入池 + new 强制堆上新建副本，两者独立。

**Qjava-basics-1085（简答·误用）** 请说明「String」中new String的机制与使用要点。
**要点（标准答案）**：① new String("abc") 在字面量已入池时额外创建 1 个堆对象，未入池时创建 2 个。；② 原理：字面量入池 + new 强制堆上新建副本，两者独立。；③ 使用要点：代码里出现 new String(字面量) 基本都是误用，review 直接标记。。版本锚点：Java 语言通用语义。

**Qjava-basics-1086（单选·正向·线程）** 关于「String」的说法，正确的是？
- A. String 拼接必须加锁。
- B. String 天然线程安全：不可变对象无并发修改风险。
- C. String 的 intern() 操作是线程不安全的。
- D. String 需要配合 synchronized 才能多线程使用。
**答案：B**
**解析：** String 天然线程安全：不可变对象无并发修改风险。。原因：不可变对象发布后任何线程都无法修改其状态。。
**来源：** JB-011 · String（JLS 17.5（不可变））

**Qjava-basics-1087（判断·线程）** String 天然线程安全：不可变对象无并发修改风险。
**答案：对。** 解析：不可变对象发布后任何线程都无法修改其状态。

**Qjava-basics-1088（判断·线程）** String 需要配合 synchronized 才能多线程使用。
**答案：错。** 正确表述：String 天然线程安全：不可变对象无并发修改风险。。原因：不可变对象发布后任何线程都无法修改其状态。

**Qjava-basics-1089（判断·线程）** String 的 intern() 操作是线程不安全的。
**答案：错。** 正确表述：String 天然线程安全：不可变对象无并发修改风险。。原因：不可变对象发布后任何线程都无法修改其状态。

**Qjava-basics-1090（判断·线程）** String 拼接必须加锁。
**答案：错。** 正确表述：String 天然线程安全：不可变对象无并发修改风险。。原因：不可变对象发布后任何线程都无法修改其状态。

**Qjava-basics-1091（场景单选·线程）** 在工程实践中关于「线程安全」，下列做法符合推荐实践的是？
- A. String 需要配合 synchronized 才能多线程使用。
- B. String 的 intern() 操作是线程不安全的。
- C. 不可变对象是多线程共享数据的默认选择。
- D. String 拼接必须加锁。
**答案：C**
**解析：** 推荐实践：不可变对象是多线程共享数据的默认选择。。事实依据：String 天然线程安全：不可变对象无并发修改风险。。

**Qjava-basics-1092（场景判断·线程）** 推荐实践：不可变对象是多线程共享数据的默认选择。
**答案：对。** 解析：String 天然线程安全：不可变对象无并发修改风险。。原因：不可变对象发布后任何线程都无法修改其状态。

**Qjava-basics-1093（填空·线程）** String 天然______：不可变对象无并发修改风险。
**答案：线程安全**。解析：不可变对象发布后任何线程都无法修改其状态。

**Qjava-basics-1094（简答·线程）** 请说明「String」中线程安全的机制与使用要点。
**要点（标准答案）**：① String 天然线程安全：不可变对象无并发修改风险。；② 原理：不可变对象发布后任何线程都无法修改其状态。；③ 使用要点：不可变对象是多线程共享数据的默认选择。。版本锚点：JLS 17.5（不可变）。

**Qjava-basics-1095（单选·正向·语法语义）** 关于「StringBuilder」的说法，正确的是？
- A. StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。
- B. StringBuilder 是线程安全的。
- C. StringBuffer 在 JDK9 后被废弃。
- D. 两者底层存储结构完全不同。
**答案：A**
**解析：** StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。。原因：StringBuffer 牺牲锁开销换取安全，单线程场景 StringBuilder 更快。。
**来源：** JB-012 · StringBuilder（StringBuilder javadoc（非同步））

**Qjava-basics-1096（判断·语法语义）** StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。
**答案：对。** 解析：StringBuffer 牺牲锁开销换取安全，单线程场景 StringBuilder 更快。

**Qjava-basics-1097（判断·语法语义）** StringBuilder 是线程安全的。
**答案：错。** 正确表述：StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。。原因：StringBuffer 牺牲锁开销换取安全，单线程场景 StringBuilder 更快。

**Qjava-basics-1098（判断·语法语义）** StringBuffer 在 JDK9 后被废弃。
**答案：错。** 正确表述：StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。。原因：StringBuffer 牺牲锁开销换取安全，单线程场景 StringBuilder 更快。

**Qjava-basics-1099（判断·语法语义）** 两者底层存储结构完全不同。
**答案：错。** 正确表述：StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。。原因：StringBuffer 牺牲锁开销换取安全，单线程场景 StringBuilder 更快。

**Qjava-basics-1100（场景单选·语法语义）** 在工程实践中关于「线程安全」，下列做法符合推荐实践的是？
- A. 两者底层存储结构完全不同。
- B. StringBuilder 是线程安全的。
- C. 方法局部变量拼串用 StringBuilder；极少出现需要共享可变拼串的场景。
- D. StringBuffer 在 JDK9 后被废弃。
**答案：C**
**解析：** 推荐实践：方法局部变量拼串用 StringBuilder；极少出现需要共享可变拼串的场景。。事实依据：StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。。

**Qjava-basics-1101（场景判断·语法语义）** 推荐实践：方法局部变量拼串用 StringBuilder；极少出现需要共享可变拼串的场景。
**答案：对。** 解析：StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。。原因：StringBuffer 牺牲锁开销换取安全，单线程场景 StringBuilder 更快。

**Qjava-basics-1102（填空·语法语义）** StringBuilder 非______，StringBuffer 的主要方法加了 synchronized。
**答案：线程安全**。解析：StringBuffer 牺牲锁开销换取安全，单线程场景 StringBuilder 更快。

**Qjava-basics-1103（简答·语法语义）** 请说明「StringBuilder」中线程安全的机制与使用要点。
**要点（标准答案）**：① StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。；② 原理：StringBuffer 牺牲锁开销换取安全，单线程场景 StringBuilder 更快。；③ 使用要点：方法局部变量拼串用 StringBuilder；极少出现需要共享可变拼串的场景。。版本锚点：StringBuilder javadoc（非同步）。

**Qjava-basics-1104（单选·正向·语法语义）** 关于「包装类」的说法，正确的是？
- A. Long 没有缓存机制。
- B. Integer 缓存范围是 0~255。
- C. 所有整数值的包装类都有缓存。
- D. Integer/Long/Short/Byte 的缓存范围是 -128~127，Character 是 0~127，Boolean 缓存 true/false。
**答案：D**
**解析：** Integer/Long/Short/Byte 的缓存范围是 -128~127，Character 是 0~127，Boolean 缓存 true/false。。原因：缓存由 valueOf 触发，超出范围的值每次都新建对象。。
**来源：** JB-013 · 包装类（缓存上限可用 -XX:AutoBoxCacheMax 调整（仅 Integer）。）

**Qjava-basics-1105（判断·语法语义）** Integer/Long/Short/Byte 的缓存范围是 -128~127，Character 是 0~127，Boolean 缓存 true/false。
**答案：对。** 解析：缓存由 valueOf 触发，超出范围的值每次都新建对象。

**Qjava-basics-1106（判断·语法语义）** 所有整数值的包装类都有缓存。
**答案：错。** 正确表述：Integer/Long/Short/Byte 的缓存范围是 -128~127，Character 是 0~127，Boolean 缓存 true/false。。原因：缓存由 valueOf 触发，超出范围的值每次都新建对象。

**Qjava-basics-1107（判断·语法语义）** Integer 缓存范围是 0~255。
**答案：错。** 正确表述：Integer/Long/Short/Byte 的缓存范围是 -128~127，Character 是 0~127，Boolean 缓存 true/false。。原因：缓存由 valueOf 触发，超出范围的值每次都新建对象。

**Qjava-basics-1108（判断·语法语义）** Long 没有缓存机制。
**答案：错。** 正确表述：Integer/Long/Short/Byte 的缓存范围是 -128~127，Character 是 0~127，Boolean 缓存 true/false。。原因：缓存由 valueOf 触发，超出范围的值每次都新建对象。

**Qjava-basics-1109（场景单选·语法语义）** 在工程实践中关于「缓存范围」，下列做法符合推荐实践的是？
- A. 所有整数值的包装类都有缓存。
- B. Integer 缓存范围是 0~255。
- C. Long 没有缓存机制。
- D. 包装类比较一律用 equals，避开缓存边界陷阱。
**答案：D**
**解析：** 推荐实践：包装类比较一律用 equals，避开缓存边界陷阱。。事实依据：Integer/Long/Short/Byte 的缓存范围是 -128~127，Character 是 0~127，Boolean 缓存 true/false。。

**Qjava-basics-1110（场景判断·语法语义）** 推荐实践：包装类比较一律用 equals，避开缓存边界陷阱。
**答案：对。** 解析：Integer/Long/Short/Byte 的缓存范围是 -128~127，Character 是 0~127，Boolean 缓存 true/false。。原因：缓存由 valueOf 触发，超出范围的值每次都新建对象。

**Qjava-basics-1111（填空·语法语义）** Integer/Long/Short/Byte 的______是 -128~127，Character 是 0~127，Boolean 缓存 true/false。
**答案：缓存范围**。解析：缓存由 valueOf 触发，超出范围的值每次都新建对象。

**Qjava-basics-1112（简答·语法语义）** 请说明「包装类」中缓存范围的机制与使用要点。
**要点（标准答案）**：① Integer/Long/Short/Byte 的缓存范围是 -128~127，Character 是 0~127，Boolean 缓存 true/false。；② 原理：缓存由 valueOf 触发，超出范围的值每次都新建对象。；③ 使用要点：包装类比较一律用 equals，避开缓存边界陷阱。。版本锚点：缓存上限可用 -XX:AutoBoxCacheMax 调整（仅 Integer）。。

**Qjava-basics-1113（单选·正向·误用）** 关于「包装类」的说法，正确的是？
- A. 对值为 null 的包装类做自动拆箱会抛 NullPointerException。
- B. Integer 与 int 混用编译器会报错。
- C. null 包装类自动拆箱会得到默认值 0。
- D. 自动拆箱永远不会抛异常。
**答案：A**
**解析：** 对值为 null 的包装类做自动拆箱会抛 NullPointerException。。原因：拆箱编译为 xxxValue() 调用，null 调用即 NPE；三目运算符两侧类型不一致时也会触发隐式拆箱。。
**来源：** JB-014 · 包装类（阿里手册强制：POJO 属性统一用包装类。）

**Qjava-basics-1114（判断·误用）** 对值为 null 的包装类做自动拆箱会抛 NullPointerException。
**答案：对。** 解析：拆箱编译为 xxxValue() 调用，null 调用即 NPE；三目运算符两侧类型不一致时也会触发隐式拆箱。

**Qjava-basics-1115（判断·误用）** null 包装类自动拆箱会得到默认值 0。
**答案：错。** 正确表述：对值为 null 的包装类做自动拆箱会抛 NullPointerException。。原因：拆箱编译为 xxxValue() 调用，null 调用即 NPE；三目运算符两侧类型不一致时也会触发隐式拆箱。

**Qjava-basics-1116（判断·误用）** 自动拆箱永远不会抛异常。
**答案：错。** 正确表述：对值为 null 的包装类做自动拆箱会抛 NullPointerException。。原因：拆箱编译为 xxxValue() 调用，null 调用即 NPE；三目运算符两侧类型不一致时也会触发隐式拆箱。

**Qjava-basics-1117（判断·误用）** Integer 与 int 混用编译器会报错。
**答案：错。** 正确表述：对值为 null 的包装类做自动拆箱会抛 NullPointerException。。原因：拆箱编译为 xxxValue() 调用，null 调用即 NPE；三目运算符两侧类型不一致时也会触发隐式拆箱。

**Qjava-basics-1118（场景单选·误用）** 在工程实践中关于「拆箱NPE」，下列做法符合推荐实践的是？
- A. null 包装类自动拆箱会得到默认值 0。
- B. 三目运算 boolean ? intVal : intWrapper 是真实 NPE 事故源。
- C. Integer 与 int 混用编译器会报错。
- D. 自动拆箱永远不会抛异常。
**答案：B**
**解析：** 推荐实践：三目运算 boolean ? intVal : intWrapper 是真实 NPE 事故源。。事实依据：对值为 null 的包装类做自动拆箱会抛 NullPointerException。。

**Qjava-basics-1119（场景判断·误用）** 推荐实践：三目运算 boolean ? intVal : intWrapper 是真实 NPE 事故源。
**答案：对。** 解析：对值为 null 的包装类做自动拆箱会抛 NullPointerException。。原因：拆箱编译为 xxxValue() 调用，null 调用即 NPE；三目运算符两侧类型不一致时也会触发隐式拆箱。

**Qjava-basics-1120（简答·误用）** 请说明「包装类」中拆箱NPE的机制与使用要点。
**要点（标准答案）**：① 对值为 null 的包装类做自动拆箱会抛 NullPointerException。；② 原理：拆箱编译为 xxxValue() 调用，null 调用即 NPE；三目运算符两侧类型不一致时也会触发隐式拆箱。；③ 使用要点：三目运算 boolean ? intVal : intWrapper 是真实 NPE 事故源。。版本锚点：阿里手册强制：POJO 属性统一用包装类。。

**Qjava-basics-1121（单选·正向·误用）** 关于「包装类」的说法，正确的是？
- A. Long 的 == 与 equals 语义相同。
- B. Long 缓存范围是 -128~255。
- C. Long 类型用 == 比较，超出缓存范围（-128~127）时即使值相等也返回 false。
- D. Long 用 == 比较值相等就一定 true。
**答案：C**
**解析：** Long 类型用 == 比较，超出缓存范围（-128~127）时即使值相等也返回 false。。原因：== 比较引用，超缓存范围的 Long 是不同对象。。
**来源：** JB-015 · 包装类（JLS 5.1.7（缓存 -128~127））

**Qjava-basics-1122（判断·误用）** Long 类型用 == 比较，超出缓存范围（-128~127）时即使值相等也返回 false。
**答案：对。** 解析：== 比较引用，超缓存范围的 Long 是不同对象。

**Qjava-basics-1123（判断·误用）** Long 用 == 比较值相等就一定 true。
**答案：错。** 正确表述：Long 类型用 == 比较，超出缓存范围（-128~127）时即使值相等也返回 false。。原因：== 比较引用，超缓存范围的 Long 是不同对象。

**Qjava-basics-1124（判断·误用）** Long 缓存范围是 -128~255。
**答案：错。** 正确表述：Long 类型用 == 比较，超出缓存范围（-128~127）时即使值相等也返回 false。。原因：== 比较引用，超缓存范围的 Long 是不同对象。

**Qjava-basics-1125（判断·误用）** Long 的 == 与 equals 语义相同。
**答案：错。** 正确表述：Long 类型用 == 比较，超出缓存范围（-128~127）时即使值相等也返回 false。。原因：== 比较引用，超缓存范围的 Long 是不同对象。

**Qjava-basics-1126（场景单选·误用）** 在工程实践中关于「Long比较」，下列做法符合推荐实践的是？
- A. Long 用 == 比较值相等就一定 true。
- B. 电商订单号等大数值 Long 比较必须用 equals——经典线上事故源。
- C. Long 缓存范围是 -128~255。
- D. Long 的 == 与 equals 语义相同。
**答案：B**
**解析：** 推荐实践：电商订单号等大数值 Long 比较必须用 equals——经典线上事故源。。事实依据：Long 类型用 == 比较，超出缓存范围（-128~127）时即使值相等也返回 false。。

**Qjava-basics-1127（场景判断·误用）** 推荐实践：电商订单号等大数值 Long 比较必须用 equals——经典线上事故源。
**答案：对。** 解析：Long 类型用 == 比较，超出缓存范围（-128~127）时即使值相等也返回 false。。原因：== 比较引用，超缓存范围的 Long 是不同对象。

**Qjava-basics-1128（简答·误用）** 请说明「包装类」中Long比较的机制与使用要点。
**要点（标准答案）**：① Long 类型用 == 比较，超出缓存范围（-128~127）时即使值相等也返回 false。；② 原理：== 比较引用，超缓存范围的 Long 是不同对象。；③ 使用要点：电商订单号等大数值 Long 比较必须用 equals——经典线上事故源。。版本锚点：JLS 5.1.7（缓存 -128~127）。

**Qjava-basics-1129（单选·正向·语法语义）** 关于「equals体系」的说法，正确的是？
- A. 重写 equals 必须满足自反、对称、传递、一致、非空（对 null 返回 false）五条。
- B. equals 可以对 null 返回 true。
- C. hashCode 不在 equals 契约范围内。
- D. equals 只需要满足对称性。
**答案：A**
**解析：** 重写 equals 必须满足自反、对称、传递、一致、非空（对 null 返回 false）五条。。原因：违反任何一条都会导致该对象在集合中的行为异常。。
**来源：** JB-016 · equals体系（Effective Java Item 10）

**Qjava-basics-1130（判断·语法语义）** 重写 equals 必须满足自反、对称、传递、一致、非空（对 null 返回 false）五条。
**答案：对。** 解析：违反任何一条都会导致该对象在集合中的行为异常。

**Qjava-basics-1131（判断·语法语义）** equals 只需要满足对称性。
**答案：错。** 正确表述：重写 equals 必须满足自反、对称、传递、一致、非空（对 null 返回 false）五条。。原因：违反任何一条都会导致该对象在集合中的行为异常。

**Qjava-basics-1132（判断·语法语义）** hashCode 不在 equals 契约范围内。
**答案：错。** 正确表述：重写 equals 必须满足自反、对称、传递、一致、非空（对 null 返回 false）五条。。原因：违反任何一条都会导致该对象在集合中的行为异常。

**Qjava-basics-1133（判断·语法语义）** equals 可以对 null 返回 true。
**答案：错。** 正确表述：重写 equals 必须满足自反、对称、传递、一致、非空（对 null 返回 false）五条。。原因：违反任何一条都会导致该对象在集合中的行为异常。

**Qjava-basics-1134（场景单选·语法语义）** 在工程实践中关于「五大契约」，下列做法符合推荐实践的是？
- A. hashCode 不在 equals 契约范围内。
- B. 《Effective Java》Item 10 是权威参考。
- C. equals 只需要满足对称性。
- D. equals 可以对 null 返回 true。
**答案：B**
**解析：** 推荐实践：《Effective Java》Item 10 是权威参考。。事实依据：重写 equals 必须满足自反、对称、传递、一致、非空（对 null 返回 false）五条。。

**Qjava-basics-1135（场景判断·语法语义）** 推荐实践：《Effective Java》Item 10 是权威参考。
**答案：对。** 解析：重写 equals 必须满足自反、对称、传递、一致、非空（对 null 返回 false）五条。。原因：违反任何一条都会导致该对象在集合中的行为异常。

**Qjava-basics-1136（简答·语法语义）** 请说明「equals体系」中五大契约的机制与使用要点。
**要点（标准答案）**：① 重写 equals 必须满足自反、对称、传递、一致、非空（对 null 返回 false）五条。；② 原理：违反任何一条都会导致该对象在集合中的行为异常。；③ 使用要点：《Effective Java》Item 10 是权威参考。。版本锚点：Effective Java Item 10。

**Qjava-basics-1137（单选·正向·误用）** 关于「equals体系」的说法，正确的是？
- A. hashCode 相同则 equals 必须相同。
- B. 重写 equals 不重写 hashCode 会导致该对象在 HashMap/HashSet 中"找不到"。
- C. 重写 hashCode 不影响 HashMap。
- D. IDE 自动生成的 equals 不需要同时生成 hashCode。
**答案：B**
**解析：** 重写 equals 不重写 hashCode 会导致该对象在 HashMap/HashSet 中"找不到"。。原因：HashMap 先用 hash 定桶再用 equals 精确匹配，缺 hashCode 的对象默认用对象地址。。
**来源：** JB-017 · equals体系（Object.hashCode javadoc）

**Qjava-basics-1138（判断·误用）** 重写 equals 不重写 hashCode 会导致该对象在 HashMap/HashSet 中"找不到"。
**答案：对。** 解析：HashMap 先用 hash 定桶再用 equals 精确匹配，缺 hashCode 的对象默认用对象地址。

**Qjava-basics-1139（判断·误用）** IDE 自动生成的 equals 不需要同时生成 hashCode。
**答案：错。** 正确表述：重写 equals 不重写 hashCode 会导致该对象在 HashMap/HashSet 中"找不到"。。原因：HashMap 先用 hash 定桶再用 equals 精确匹配，缺 hashCode 的对象默认用对象地址。

**Qjava-basics-1140（判断·误用）** hashCode 相同则 equals 必须相同。
**答案：错。** 正确表述：重写 equals 不重写 hashCode 会导致该对象在 HashMap/HashSet 中"找不到"。。原因：HashMap 先用 hash 定桶再用 equals 精确匹配，缺 hashCode 的对象默认用对象地址。

**Qjava-basics-1141（判断·误用）** 重写 hashCode 不影响 HashMap。
**答案：错。** 正确表述：重写 equals 不重写 hashCode 会导致该对象在 HashMap/HashSet 中"找不到"。。原因：HashMap 先用 hash 定桶再用 equals 精确匹配，缺 hashCode 的对象默认用对象地址。

**Qjava-basics-1142（场景单选·误用）** 在工程实践中关于「hashCode契约」，下列做法符合推荐实践的是？
- A. hashCode 相同则 equals 必须相同。
- B. IDE 自动生成的 equals 不需要同时生成 hashCode。
- C. 重写 hashCode 不影响 HashMap。
- D. 阿里手册：重写 equals 必须重写 hashCode。
**答案：D**
**解析：** 推荐实践：阿里手册：重写 equals 必须重写 hashCode。。事实依据：重写 equals 不重写 hashCode 会导致该对象在 HashMap/HashSet 中"找不到"。。

**Qjava-basics-1143（场景判断·误用）** 推荐实践：阿里手册：重写 equals 必须重写 hashCode。
**答案：对。** 解析：重写 equals 不重写 hashCode 会导致该对象在 HashMap/HashSet 中"找不到"。。原因：HashMap 先用 hash 定桶再用 equals 精确匹配，缺 hashCode 的对象默认用对象地址。

**Qjava-basics-1144（简答·误用）** 请说明「equals体系」中hashCode契约的机制与使用要点。
**要点（标准答案）**：① 重写 equals 不重写 hashCode 会导致该对象在 HashMap/HashSet 中"找不到"。；② 原理：HashMap 先用 hash 定桶再用 equals 精确匹配，缺 hashCode 的对象默认用对象地址。；③ 使用要点：阿里手册：重写 equals 必须重写 hashCode。。版本锚点：Object.hashCode javadoc。

**Qjava-basics-1145（单选·正向·语法语义）** 关于「equals体系」的说法，正确的是？
- A. 31 作为乘数会导致严重散列冲突。
- B. hashCode 必须使用密码学哈希。
- C. 31 是随机选的数字，没有特别原因。
- D. hashCode 计算选用 31 作乘数：奇素数散列分布好，且 31*i 可被 JVM 优化为 (i<<5)-i。
**答案：D**
**解析：** hashCode 计算选用 31 作乘数：奇素数散列分布好，且 31*i 可被 JVM 优化为 (i<<5)-i。。原因：31 经过大量字符串实验验证，分布均匀性和计算成本平衡最佳。。
**来源：** JB-018 · equals体系（JDK 源码惯例）

**Qjava-basics-1146（判断·语法语义）** hashCode 计算选用 31 作乘数：奇素数散列分布好，且 31*i 可被 JVM 优化为 (i<<5)-i。
**答案：对。** 解析：31 经过大量字符串实验验证，分布均匀性和计算成本平衡最佳。

**Qjava-basics-1147（判断·语法语义）** 31 是随机选的数字，没有特别原因。
**答案：错。** 正确表述：hashCode 计算选用 31 作乘数：奇素数散列分布好，且 31*i 可被 JVM 优化为 (i<<5)-i。。原因：31 经过大量字符串实验验证，分布均匀性和计算成本平衡最佳。

**Qjava-basics-1148（判断·语法语义）** 31 作为乘数会导致严重散列冲突。
**答案：错。** 正确表述：hashCode 计算选用 31 作乘数：奇素数散列分布好，且 31*i 可被 JVM 优化为 (i<<5)-i。。原因：31 经过大量字符串实验验证，分布均匀性和计算成本平衡最佳。

**Qjava-basics-1149（判断·语法语义）** hashCode 必须使用密码学哈希。
**答案：错。** 正确表述：hashCode 计算选用 31 作乘数：奇素数散列分布好，且 31*i 可被 JVM 优化为 (i<<5)-i。。原因：31 经过大量字符串实验验证，分布均匀性和计算成本平衡最佳。

**Qjava-basics-1150（场景单选·语法语义）** 在工程实践中关于「31乘子」，下列做法符合推荐实践的是？
- A. 31 是随机选的数字，没有特别原因。
- B. hashCode 必须使用密码学哈希。
- C. "abc".hashCode()=96354 可现场推导（已实测）。
- D. 31 作为乘数会导致严重散列冲突。
**答案：C**
**解析：** 推荐实践："abc".hashCode()=96354 可现场推导（已实测）。。事实依据：hashCode 计算选用 31 作乘数：奇素数散列分布好，且 31*i 可被 JVM 优化为 (i<<5)-i。。

**Qjava-basics-1151（场景判断·语法语义）** 推荐实践："abc".hashCode()=96354 可现场推导（已实测）。
**答案：对。** 解析：hashCode 计算选用 31 作乘数：奇素数散列分布好，且 31*i 可被 JVM 优化为 (i<<5)-i。。原因：31 经过大量字符串实验验证，分布均匀性和计算成本平衡最佳。

**Qjava-basics-1152（简答·语法语义）** 请说明「equals体系」中31乘子的机制与使用要点。
**要点（标准答案）**：① hashCode 计算选用 31 作乘数：奇素数散列分布好，且 31*i 可被 JVM 优化为 (i<<5)-i。；② 原理：31 经过大量字符串实验验证，分布均匀性和计算成本平衡最佳。；③ 使用要点："abc".hashCode()=96354 可现场推导（已实测）。。版本锚点：JDK 源码惯例。

**Qjava-basics-1153（单选·正向·误用）** 关于「equals体系」的说法，正确的是？
- A. 可变对象做 key 是官方推荐。
- B. key 丢失后调用 remove 可以删除旧条目。
- C. 修改对象字段后 HashMap 会自动重新计算它的位置。
- D. 把可变字段参与 hashCode 计算的对象放入 HashMap 后修改字段，会导致 key"丢失"（get 返回 null 且无法 remove）。
**答案：D**
**解析：** 把可变字段参与 hashCode 计算的对象放入 HashMap 后修改字段，会导致 key"丢失"（get 返回 null 且无法 remove）。。原因：hash 已按旧字段计算定桶，字段变化后再 get 用新 hash 定位到不同的桶。。
**来源：** JB-019 · equals体系（HashMap 源码语义）

**Qjava-basics-1154（判断·误用）** 把可变字段参与 hashCode 计算的对象放入 HashMap 后修改字段，会导致 key"丢失"（get 返回 null 且无法 remove）。
**答案：对。** 解析：hash 已按旧字段计算定桶，字段变化后再 get 用新 hash 定位到不同的桶。

**Qjava-basics-1155（判断·误用）** 修改对象字段后 HashMap 会自动重新计算它的位置。
**答案：错。** 正确表述：把可变字段参与 hashCode 计算的对象放入 HashMap 后修改字段，会导致 key"丢失"（get 返回 null 且无法 remove）。。原因：hash 已按旧字段计算定桶，字段变化后再 get 用新 hash 定位到不同的桶。

**Qjava-basics-1156（判断·误用）** key 丢失后调用 remove 可以删除旧条目。
**答案：错。** 正确表述：把可变字段参与 hashCode 计算的对象放入 HashMap 后修改字段，会导致 key"丢失"（get 返回 null 且无法 remove）。。原因：hash 已按旧字段计算定桶，字段变化后再 get 用新 hash 定位到不同的桶。

**Qjava-basics-1157（判断·误用）** 可变对象做 key 是官方推荐。
**答案：错。** 正确表述：把可变字段参与 hashCode 计算的对象放入 HashMap 后修改字段，会导致 key"丢失"（get 返回 null 且无法 remove）。。原因：hash 已按旧字段计算定桶，字段变化后再 get 用新 hash 定位到不同的桶。

**Qjava-basics-1158（场景单选·误用）** 在工程实践中关于「可变key」，下列做法符合推荐实践的是？
- A. 修改对象字段后 HashMap 会自动重新计算它的位置。
- B. 可变对象做 key 是官方推荐。
- C. key 丢失后调用 remove 可以删除旧条目。
- D. value 泄漏 + 业务读不到数据，是真实事故类型。
**答案：D**
**解析：** 推荐实践：value 泄漏 + 业务读不到数据，是真实事故类型。。事实依据：把可变字段参与 hashCode 计算的对象放入 HashMap 后修改字段，会导致 key"丢失"（get 返回 null 且无法 remove）。。

**Qjava-basics-1159（场景判断·误用）** 推荐实践：value 泄漏 + 业务读不到数据，是真实事故类型。
**答案：对。** 解析：把可变字段参与 hashCode 计算的对象放入 HashMap 后修改字段，会导致 key"丢失"（get 返回 null 且无法 remove）。。原因：hash 已按旧字段计算定桶，字段变化后再 get 用新 hash 定位到不同的桶。

**Qjava-basics-1160（简答·误用）** 请说明「equals体系」中可变key的机制与使用要点。
**要点（标准答案）**：① 把可变字段参与 hashCode 计算的对象放入 HashMap 后修改字段，会导致 key"丢失"（get 返回 null 且无法 remove）。；② 原理：hash 已按旧字段计算定桶，字段变化后再 get 用新 hash 定位到不同的桶。；③ 使用要点：value 泄漏 + 业务读不到数据，是真实事故类型。。版本锚点：HashMap 源码语义。

**Qjava-basics-1161（单选·正向·语法语义）** 关于「equals体系」的说法，正确的是？
- A. 传递性违反不影响集合行为。
- B. instanceof 不会造成对称性问题。
- C. instanceof 是 equals 的标准写法。
- D. equals 中使用 instanceof 会破坏传递性：子类与父类互比可能不对称。
**答案：D**
**解析：** equals 中使用 instanceof 会破坏传递性：子类与父类互比可能不对称。。原因：《Effective Java》推荐 getClass 精确比较或把类设计为 final。。
**来源：** JB-020 · equals体系（JLS 15.20.2）

**Qjava-basics-1162（判断·语法语义）** equals 中使用 instanceof 会破坏传递性：子类与父类互比可能不对称。
**答案：对。** 解析：《Effective Java》推荐 getClass 精确比较或把类设计为 final。

**Qjava-basics-1163（判断·语法语义）** instanceof 是 equals 的标准写法。
**答案：错。** 正确表述：equals 中使用 instanceof 会破坏传递性：子类与父类互比可能不对称。。原因：《Effective Java》推荐 getClass 精确比较或把类设计为 final。

**Qjava-basics-1164（判断·语法语义）** instanceof 不会造成对称性问题。
**答案：错。** 正确表述：equals 中使用 instanceof 会破坏传递性：子类与父类互比可能不对称。。原因：《Effective Java》推荐 getClass 精确比较或把类设计为 final。

**Qjava-basics-1165（判断·语法语义）** 传递性违反不影响集合行为。
**答案：错。** 正确表述：equals 中使用 instanceof 会破坏传递性：子类与父类互比可能不对称。。原因：《Effective Java》推荐 getClass 精确比较或把类设计为 final。

**Qjava-basics-1166（场景单选·语法语义）** 在工程实践中关于「instanceof陷阱」，下列做法符合推荐实践的是？
- A. instanceof 不会造成对称性问题。
- B. instanceof 是 equals 的标准写法。
- C. 传递性违反不影响集合行为。
- D. P10 层会追问 getClass 与 instanceof 的取舍条件。
**答案：D**
**解析：** 推荐实践：P10 层会追问 getClass 与 instanceof 的取舍条件。。事实依据：equals 中使用 instanceof 会破坏传递性：子类与父类互比可能不对称。。

**Qjava-basics-1167（场景判断·语法语义）** 推荐实践：P10 层会追问 getClass 与 instanceof 的取舍条件。
**答案：对。** 解析：equals 中使用 instanceof 会破坏传递性：子类与父类互比可能不对称。。原因：《Effective Java》推荐 getClass 精确比较或把类设计为 final。

**Qjava-basics-1168（简答·语法语义）** 请说明「equals体系」中instanceof陷阱的机制与使用要点。
**要点（标准答案）**：① equals 中使用 instanceof 会破坏传递性：子类与父类互比可能不对称。；② 原理：《Effective Java》推荐 getClass 精确比较或把类设计为 final。；③ 使用要点：P10 层会追问 getClass 与 instanceof 的取舍条件。。版本锚点：JLS 15.20.2。

**Qjava-basics-1169（单选·正向·内存）** 关于「ArrayList」的说法，正确的是？
- A. new ArrayList() 立即分配容量为 10 的数组。
- B. ArrayList 底层是链表结构。
- C. new ArrayList() 不分配数组，首次 add 时才分配容量 10 的数组。
- D. new ArrayList() 的默认容量是 0 且永远不会增长。
**答案：C**
**解析：** new ArrayList() 不分配数组，首次 add 时才分配容量 10 的数组。。原因：节省空集合的内存占用。。
**来源：** JB-021 · ArrayList（JDK 8+ 源码）

**Qjava-basics-1170（判断·内存）** new ArrayList() 不分配数组，首次 add 时才分配容量 10 的数组。
**答案：对。** 解析：节省空集合的内存占用。

**Qjava-basics-1171（判断·内存）** new ArrayList() 立即分配容量为 10 的数组。
**答案：错。** 正确表述：new ArrayList() 不分配数组，首次 add 时才分配容量 10 的数组。。原因：节省空集合的内存占用。

**Qjava-basics-1172（判断·内存）** new ArrayList() 的默认容量是 0 且永远不会增长。
**答案：错。** 正确表述：new ArrayList() 不分配数组，首次 add 时才分配容量 10 的数组。。原因：节省空集合的内存占用。

**Qjava-basics-1173（判断·内存）** ArrayList 底层是链表结构。
**答案：错。** 正确表述：new ArrayList() 不分配数组，首次 add 时才分配容量 10 的数组。。原因：节省空集合的内存占用。

**Qjava-basics-1174（场景单选·内存）** 在工程实践中关于「懒初始化」，下列做法符合推荐实践的是？
- A. ArrayList 底层是链表结构。
- B. 本机反射验证：首插后 elementData.length==10。
- C. new ArrayList() 的默认容量是 0 且永远不会增长。
- D. new ArrayList() 立即分配容量为 10 的数组。
**答案：B**
**解析：** 推荐实践：本机反射验证：首插后 elementData.length==10。。事实依据：new ArrayList() 不分配数组，首次 add 时才分配容量 10 的数组。。

**Qjava-basics-1175（场景判断·内存）** 推荐实践：本机反射验证：首插后 elementData.length==10。
**答案：对。** 解析：new ArrayList() 不分配数组，首次 add 时才分配容量 10 的数组。。原因：节省空集合的内存占用。

**Qjava-basics-1176（简答·内存）** 请说明「ArrayList」中懒初始化的机制与使用要点。
**要点（标准答案）**：① new ArrayList() 不分配数组，首次 add 时才分配容量 10 的数组。；② 原理：节省空集合的内存占用。；③ 使用要点：本机反射验证：首插后 elementData.length==10。。版本锚点：JDK 8+ 源码。

**Qjava-basics-1177（单选·正向·性能）** 关于「ArrayList」的说法，正确的是？
- A. ArrayList 扩容为新容量的 1.5 倍（oldCapacity + oldCapacity >> 1）：10→15→22。
- B. ArrayList 每次扩容为原来的 2 倍。
- C. ArrayList 扩容是容量加 10。
- D. ArrayList 扩容不会拷贝原数组。
**答案：A**
**解析：** ArrayList 扩容为新容量的 1.5 倍（oldCapacity + oldCapacity >> 1）：10→15→22。。原因：1.5 倍平衡扩容次数与内存浪费；2 倍浪费内存，1.1 倍扩容太频繁。。
**来源：** JB-022 · ArrayList（JDK 8+ 源码（本项目实测））

**Qjava-basics-1178（判断·性能）** ArrayList 扩容为新容量的 1.5 倍（oldCapacity + oldCapacity >> 1）：10→15→22。
**答案：对。** 解析：1.5 倍平衡扩容次数与内存浪费；2 倍浪费内存，1.1 倍扩容太频繁。

**Qjava-basics-1179（判断·性能）** ArrayList 每次扩容为原来的 2 倍。
**答案：错。** 正确表述：ArrayList 扩容为新容量的 1.5 倍（oldCapacity + oldCapacity >> 1）：10→15→22。。原因：1.5 倍平衡扩容次数与内存浪费；2 倍浪费内存，1.1 倍扩容太频繁。

**Qjava-basics-1180（判断·性能）** ArrayList 扩容是容量加 10。
**答案：错。** 正确表述：ArrayList 扩容为新容量的 1.5 倍（oldCapacity + oldCapacity >> 1）：10→15→22。。原因：1.5 倍平衡扩容次数与内存浪费；2 倍浪费内存，1.1 倍扩容太频繁。

**Qjava-basics-1181（判断·性能）** ArrayList 扩容不会拷贝原数组。
**答案：错。** 正确表述：ArrayList 扩容为新容量的 1.5 倍（oldCapacity + oldCapacity >> 1）：10→15→22。。原因：1.5 倍平衡扩容次数与内存浪费；2 倍浪费内存，1.1 倍扩容太频繁。

**Qjava-basics-1182（场景单选·性能）** 在工程实践中关于「1.5倍扩容」，下列做法符合推荐实践的是？
- A. ArrayList 每次扩容为原来的 2 倍。
- B. ArrayList 扩容是容量加 10。
- C. 预估容量可用 new ArrayList<>(n) 避免多次扩容。
- D. ArrayList 扩容不会拷贝原数组。
**答案：C**
**解析：** 推荐实践：预估容量可用 new ArrayList<>(n) 避免多次扩容。。事实依据：ArrayList 扩容为新容量的 1.5 倍（oldCapacity + oldCapacity >> 1）：10→15→22。。

**Qjava-basics-1183（场景判断·性能）** 推荐实践：预估容量可用 new ArrayList<>(n) 避免多次扩容。
**答案：对。** 解析：ArrayList 扩容为新容量的 1.5 倍（oldCapacity + oldCapacity >> 1）：10→15→22。。原因：1.5 倍平衡扩容次数与内存浪费；2 倍浪费内存，1.1 倍扩容太频繁。

**Qjava-basics-1184（简答·性能）** 请说明「ArrayList」中1.5倍扩容的机制与使用要点。
**要点（标准答案）**：① ArrayList 扩容为新容量的 1.5 倍（oldCapacity + oldCapacity >> 1）：10→15→22。；② 原理：1.5 倍平衡扩容次数与内存浪费；2 倍浪费内存，1.1 倍扩容太频繁。；③ 使用要点：预估容量可用 new ArrayList<>(n) 避免多次扩容。。版本锚点：JDK 8+ 源码（本项目实测）。

**Qjava-basics-1185（单选·正向·性能）** 关于「ArrayList」的说法，正确的是？
- A. 两者 get 性能相同只是写法不同。
- B. ArrayList get(i) 是 O(1)（数组直接寻址），LinkedList get(i) 是 O(n)。
- C. ArrayList 中间插入是 O(1)。
- D. LinkedList 的 get(i) 也是 O(1)。
**答案：B**
**解析：** ArrayList get(i) 是 O(1)（数组直接寻址），LinkedList get(i) 是 O(n)。。原因：数组支持随机访问，链表必须从头或尾遍历。。
**来源：** JB-023 · ArrayList（List javadoc）

**Qjava-basics-1186（判断·性能）** ArrayList get(i) 是 O(1)（数组直接寻址），LinkedList get(i) 是 O(n)。
**答案：对。** 解析：数组支持随机访问，链表必须从头或尾遍历。

**Qjava-basics-1187（判断·性能）** LinkedList 的 get(i) 也是 O(1)。
**答案：错。** 正确表述：ArrayList get(i) 是 O(1)（数组直接寻址），LinkedList get(i) 是 O(n)。。原因：数组支持随机访问，链表必须从头或尾遍历。

**Qjava-basics-1188（判断·性能）** ArrayList 中间插入是 O(1)。
**答案：错。** 正确表述：ArrayList get(i) 是 O(1)（数组直接寻址），LinkedList get(i) 是 O(n)。。原因：数组支持随机访问，链表必须从头或尾遍历。

**Qjava-basics-1189（判断·性能）** 两者 get 性能相同只是写法不同。
**答案：错。** 正确表述：ArrayList get(i) 是 O(1)（数组直接寻址），LinkedList get(i) 是 O(n)。。原因：数组支持随机访问，链表必须从头或尾遍历。

**Qjava-basics-1190（场景单选·性能）** 在工程实践中关于「随机访问」，下列做法符合推荐实践的是？
- A. 随机读为主的场景选 ArrayList 的依据。
- B. LinkedList 的 get(i) 也是 O(1)。
- C. ArrayList 中间插入是 O(1)。
- D. 两者 get 性能相同只是写法不同。
**答案：A**
**解析：** 推荐实践：随机读为主的场景选 ArrayList 的依据。。事实依据：ArrayList get(i) 是 O(1)（数组直接寻址），LinkedList get(i) 是 O(n)。。

**Qjava-basics-1191（场景判断·性能）** 推荐实践：随机读为主的场景选 ArrayList 的依据。
**答案：对。** 解析：ArrayList get(i) 是 O(1)（数组直接寻址），LinkedList get(i) 是 O(n)。。原因：数组支持随机访问，链表必须从头或尾遍历。

**Qjava-basics-1192（简答·性能）** 请说明「ArrayList」中随机访问的机制与使用要点。
**要点（标准答案）**：① ArrayList get(i) 是 O(1)（数组直接寻址），LinkedList get(i) 是 O(n)。；② 原理：数组支持随机访问，链表必须从头或尾遍历。；③ 使用要点：随机读为主的场景选 ArrayList 的依据。。版本锚点：List javadoc。

**Qjava-basics-1193（单选·正向·性能）** 关于「ArrayList」的说法，正确的是？
- A. ArrayList 尾部插入是 O(n)。
- B. ArrayList 中间插入/删除是 O(n)（后续元素整体移动），尾部追加均摊 O(1)。
- C. ArrayList 在任意位置插入都是 O(1)。
- D. LinkedList 插入一定比 ArrayList 快。
**答案：B**
**解析：** ArrayList 中间插入/删除是 O(n)（后续元素整体移动），尾部追加均摊 O(1)。。原因：System.arraycopy 移动后续元素的成本随规模线性增长。。
**来源：** JB-024 · ArrayList（List javadoc）

**Qjava-basics-1194（判断·性能）** ArrayList 中间插入/删除是 O(n)（后续元素整体移动），尾部追加均摊 O(1)。
**答案：对。** 解析：System.arraycopy 移动后续元素的成本随规模线性增长。

**Qjava-basics-1195（判断·性能）** ArrayList 在任意位置插入都是 O(1)。
**答案：错。** 正确表述：ArrayList 中间插入/删除是 O(n)（后续元素整体移动），尾部追加均摊 O(1)。。原因：System.arraycopy 移动后续元素的成本随规模线性增长。

**Qjava-basics-1196（判断·性能）** ArrayList 尾部插入是 O(n)。
**答案：错。** 正确表述：ArrayList 中间插入/删除是 O(n)（后续元素整体移动），尾部追加均摊 O(1)。。原因：System.arraycopy 移动后续元素的成本随规模线性增长。

**Qjava-basics-1197（判断·性能）** LinkedList 插入一定比 ArrayList 快。
**答案：错。** 正确表述：ArrayList 中间插入/删除是 O(n)（后续元素整体移动），尾部追加均摊 O(1)。。原因：System.arraycopy 移动后续元素的成本随规模线性增长。

**Qjava-basics-1198（场景单选·性能）** 在工程实践中关于「中间插入」，下列做法符合推荐实践的是？
- A. LinkedList 插入一定比 ArrayList 快。
- B. 频繁中间插入的场景考虑 LinkedList 或改数据结构。
- C. ArrayList 尾部插入是 O(n)。
- D. ArrayList 在任意位置插入都是 O(1)。
**答案：B**
**解析：** 推荐实践：频繁中间插入的场景考虑 LinkedList 或改数据结构。。事实依据：ArrayList 中间插入/删除是 O(n)（后续元素整体移动），尾部追加均摊 O(1)。。

**Qjava-basics-1199（场景判断·性能）** 推荐实践：频繁中间插入的场景考虑 LinkedList 或改数据结构。
**答案：对。** 解析：ArrayList 中间插入/删除是 O(n)（后续元素整体移动），尾部追加均摊 O(1)。。原因：System.arraycopy 移动后续元素的成本随规模线性增长。

**Qjava-basics-1200（填空·性能）** ArrayList ______/删除是 O(n)（后续元素整体移动），尾部追加均摊 O(1)。
**答案：中间插入**。解析：System.arraycopy 移动后续元素的成本随规模线性增长。

**Qjava-basics-1201（简答·性能）** 请说明「ArrayList」中中间插入的机制与使用要点。
**要点（标准答案）**：① ArrayList 中间插入/删除是 O(n)（后续元素整体移动），尾部追加均摊 O(1)。；② 原理：System.arraycopy 移动后续元素的成本随规模线性增长。；③ 使用要点：频繁中间插入的场景考虑 LinkedList 或改数据结构。。版本锚点：List javadoc。

**Qjava-basics-1202（单选·正向·误用）** 关于「ArrayList」的说法，正确的是？
- A. subList 修改不影响原列表。
- B. subList 返回的是独立的拷贝列表。
- C. subList 是线程安全的。
- D. List.subList(from,to) 返回的是原列表的视图，修改原列表结构会使其失效。
**答案：D**
**解析：** List.subList(from,to) 返回的是原列表的视图，修改原列表结构会使其失效。。原因：视图直接操作底层数组，非拷贝——修改 subList 会同步影响原列表。。
**来源：** JB-025 · ArrayList（List javadoc（视图语义））

**Qjava-basics-1203（判断·误用）** List.subList(from,to) 返回的是原列表的视图，修改原列表结构会使其失效。
**答案：对。** 解析：视图直接操作底层数组，非拷贝——修改 subList 会同步影响原列表。

**Qjava-basics-1204（判断·误用）** subList 返回的是独立的拷贝列表。
**答案：错。** 正确表述：List.subList(from,to) 返回的是原列表的视图，修改原列表结构会使其失效。。原因：视图直接操作底层数组，非拷贝——修改 subList 会同步影响原列表。

**Qjava-basics-1205（判断·误用）** subList 修改不影响原列表。
**答案：错。** 正确表述：List.subList(from,to) 返回的是原列表的视图，修改原列表结构会使其失效。。原因：视图直接操作底层数组，非拷贝——修改 subList 会同步影响原列表。

**Qjava-basics-1206（判断·误用）** subList 是线程安全的。
**答案：错。** 正确表述：List.subList(from,to) 返回的是原列表的视图，修改原列表结构会使其失效。。原因：视图直接操作底层数组，非拷贝——修改 subList 会同步影响原列表。

**Qjava-basics-1207（场景单选·误用）** 在工程实践中关于「subList视图」，下列做法符合推荐实践的是？
- A. subList 返回的是独立的拷贝列表。
- B. subList 修改不影响原列表。
- C. subList 是线程安全的。
- D. 返回 subList 给调用方存在"泄露内部表示"的封装风险。
**答案：D**
**解析：** 推荐实践：返回 subList 给调用方存在"泄露内部表示"的封装风险。。事实依据：List.subList(from,to) 返回的是原列表的视图，修改原列表结构会使其失效。。

**Qjava-basics-1208（场景判断·误用）** 推荐实践：返回 subList 给调用方存在"泄露内部表示"的封装风险。
**答案：对。** 解析：List.subList(from,to) 返回的是原列表的视图，修改原列表结构会使其失效。。原因：视图直接操作底层数组，非拷贝——修改 subList 会同步影响原列表。

**Qjava-basics-1209（简答·误用）** 请说明「ArrayList」中subList视图的机制与使用要点。
**要点（标准答案）**：① List.subList(from,to) 返回的是原列表的视图，修改原列表结构会使其失效。；② 原理：视图直接操作底层数组，非拷贝——修改 subList 会同步影响原列表。；③ 使用要点：返回 subList 给调用方存在"泄露内部表示"的封装风险。。版本锚点：List javadoc（视图语义）。

**Qjava-basics-1210（单选·正向·误用）** 关于「ArrayList」的说法，正确的是？
- A. Arrays.asList 返回定长列表，add/remove 会抛 UnsupportedOperationException。
- B. Arrays.asList 返回普通 ArrayList 可自由增删。
- C. Arrays.asList(null 参数) 会返回空列表。
- D. Arrays.asList 的修改会同步到原数组——事实上会，但结构修改不支持。
**答案：A**
**解析：** Arrays.asList 返回定长列表，add/remove 会抛 UnsupportedOperationException。。原因：其内部是同类型数组包装，不支持结构修改。。
**来源：** JB-026 · ArrayList（JDK 文档（定长列表））

**Qjava-basics-1211（判断·误用）** Arrays.asList 返回定长列表，add/remove 会抛 UnsupportedOperationException。
**答案：对。** 解析：其内部是同类型数组包装，不支持结构修改。

**Qjava-basics-1212（判断·误用）** Arrays.asList 返回普通 ArrayList 可自由增删。
**答案：错。** 正确表述：Arrays.asList 返回定长列表，add/remove 会抛 UnsupportedOperationException。。原因：其内部是同类型数组包装，不支持结构修改。

**Qjava-basics-1213（判断·误用）** Arrays.asList 的修改会同步到原数组——事实上会，但结构修改不支持。
**答案：错。** 正确表述：Arrays.asList 返回定长列表，add/remove 会抛 UnsupportedOperationException。。原因：其内部是同类型数组包装，不支持结构修改。

**Qjava-basics-1214（判断·误用）** Arrays.asList(null 参数) 会返回空列表。
**答案：错。** 正确表述：Arrays.asList 返回定长列表，add/remove 会抛 UnsupportedOperationException。。原因：其内部是同类型数组包装，不支持结构修改。

**Qjava-basics-1215（场景单选·误用）** 在工程实践中关于「Arrays.asList」，下列做法符合推荐实践的是？
- A. Arrays.asList(null 参数) 会返回空列表。
- B. 返回值如果要可变需 new ArrayList<>(Arrays.asList(...)) 包装。
- C. Arrays.asList 返回普通 ArrayList 可自由增删。
- D. Arrays.asList 的修改会同步到原数组——事实上会，但结构修改不支持。
**答案：B**
**解析：** 推荐实践：返回值如果要可变需 new ArrayList<>(Arrays.asList(...)) 包装。。事实依据：Arrays.asList 返回定长列表，add/remove 会抛 UnsupportedOperationException。。

**Qjava-basics-1216（场景判断·误用）** 推荐实践：返回值如果要可变需 new ArrayList<>(Arrays.asList(...)) 包装。
**答案：对。** 解析：Arrays.asList 返回定长列表，add/remove 会抛 UnsupportedOperationException。。原因：其内部是同类型数组包装，不支持结构修改。

**Qjava-basics-1217（填空·误用）** ______ 返回定长列表，add/remove 会抛 UnsupportedOperationException。
**答案：Arrays.asList**。解析：其内部是同类型数组包装，不支持结构修改。

**Qjava-basics-1218（简答·误用）** 请说明「ArrayList」中Arrays.asList的机制与使用要点。
**要点（标准答案）**：① Arrays.asList 返回定长列表，add/remove 会抛 UnsupportedOperationException。；② 原理：其内部是同类型数组包装，不支持结构修改。；③ 使用要点：返回值如果要可变需 new ArrayList<>(Arrays.asList(...)) 包装。。版本锚点：JDK 文档（定长列表）。

**Qjava-basics-1219（单选·正向·线程）** 关于「ArrayList」的说法，正确的是？
- A. ArrayList 并发修改只会静默失败不会抛异常。
- B. ArrayList 非线程安全：并发结构修改会抛 ConcurrentModificationException 或数据丢失。
- C. Vector 是 ArrayList 的现代替代品。
- D. ArrayList 通过 synchronized 保证线程安全。
**答案：B**
**解析：** ArrayList 非线程安全：并发结构修改会抛 ConcurrentModificationException 或数据丢失。。原因：多线程共享时用 CopyOnWriteArrayList 或 Collections.synchronizedList。。
**来源：** JB-027 · ArrayList（fail-fast 已实测：迭代中 put 抛 CME。）

**Qjava-basics-1220（判断·线程）** ArrayList 非线程安全：并发结构修改会抛 ConcurrentModificationException 或数据丢失。
**答案：对。** 解析：多线程共享时用 CopyOnWriteArrayList 或 Collections.synchronizedList。

**Qjava-basics-1221（判断·线程）** ArrayList 通过 synchronized 保证线程安全。
**答案：错。** 正确表述：ArrayList 非线程安全：并发结构修改会抛 ConcurrentModificationException 或数据丢失。。原因：多线程共享时用 CopyOnWriteArrayList 或 Collections.synchronizedList。

**Qjava-basics-1222（判断·线程）** ArrayList 并发修改只会静默失败不会抛异常。
**答案：错。** 正确表述：ArrayList 非线程安全：并发结构修改会抛 ConcurrentModificationException 或数据丢失。。原因：多线程共享时用 CopyOnWriteArrayList 或 Collections.synchronizedList。

**Qjava-basics-1223（判断·线程）** Vector 是 ArrayList 的现代替代品。
**答案：错。** 正确表述：ArrayList 非线程安全：并发结构修改会抛 ConcurrentModificationException 或数据丢失。。原因：多线程共享时用 CopyOnWriteArrayList 或 Collections.synchronizedList。

**Qjava-basics-1224（场景单选·线程）** 在工程实践中关于「线程安全」，下列做法符合推荐实践的是？
- A. Vector 是 ArrayList 的现代替代品。
- B. ArrayList 并发修改只会静默失败不会抛异常。
- C. ArrayList 通过 synchronized 保证线程安全。
- D. Vector 全方法 synchronized 性能差，现代代码不再使用。
**答案：D**
**解析：** 推荐实践：Vector 全方法 synchronized 性能差，现代代码不再使用。。事实依据：ArrayList 非线程安全：并发结构修改会抛 ConcurrentModificationException 或数据丢失。。

**Qjava-basics-1225（场景判断·线程）** 推荐实践：Vector 全方法 synchronized 性能差，现代代码不再使用。
**答案：对。** 解析：ArrayList 非线程安全：并发结构修改会抛 ConcurrentModificationException 或数据丢失。。原因：多线程共享时用 CopyOnWriteArrayList 或 Collections.synchronizedList。

**Qjava-basics-1226（填空·线程）** ArrayList 非______：并发结构修改会抛 ConcurrentModificationException 或数据丢失。
**答案：线程安全**。解析：多线程共享时用 CopyOnWriteArrayList 或 Collections.synchronizedList。

**Qjava-basics-1227（简答·线程）** 请说明「ArrayList」中线程安全的机制与使用要点。
**要点（标准答案）**：① ArrayList 非线程安全：并发结构修改会抛 ConcurrentModificationException 或数据丢失。；② 原理：多线程共享时用 CopyOnWriteArrayList 或 Collections.synchronizedList。；③ 使用要点：Vector 全方法 synchronized 性能差，现代代码不再使用。。版本锚点：fail-fast 已实测：迭代中 put 抛 CME。。

**Qjava-basics-1228（单选·正向·语法语义）** 关于「ArrayList」的说法，正确的是？
- A. JDK8+ 用 removeIf(lambda) 安全地按条件删除元素，内部处理了移位与 modCount。
- B. removeIf 不支持条件删除。
- C. 循环中 list.remove(i) 删除元素是完全安全的。
- D. removeIf 是第三方工具类的方法。
**答案：A**
**解析：** JDK8+ 用 removeIf(lambda) 安全地按条件删除元素，内部处理了移位与 modCount。。原因：手写循环删除会因索引移动漏删元素。。
**来源：** JB-028 · ArrayList（JDK 8）

**Qjava-basics-1229（判断·语法语义）** JDK8+ 用 removeIf(lambda) 安全地按条件删除元素，内部处理了移位与 modCount。
**答案：对。** 解析：手写循环删除会因索引移动漏删元素。

**Qjava-basics-1230（判断·语法语义）** 循环中 list.remove(i) 删除元素是完全安全的。
**答案：错。** 正确表述：JDK8+ 用 removeIf(lambda) 安全地按条件删除元素，内部处理了移位与 modCount。。原因：手写循环删除会因索引移动漏删元素。

**Qjava-basics-1231（判断·语法语义）** removeIf 是第三方工具类的方法。
**答案：错。** 正确表述：JDK8+ 用 removeIf(lambda) 安全地按条件删除元素，内部处理了移位与 modCount。。原因：手写循环删除会因索引移动漏删元素。

**Qjava-basics-1232（判断·语法语义）** removeIf 不支持条件删除。
**答案：错。** 正确表述：JDK8+ 用 removeIf(lambda) 安全地按条件删除元素，内部处理了移位与 modCount。。原因：手写循环删除会因索引移动漏删元素。

**Qjava-basics-1233（场景单选·语法语义）** 在工程实践中关于「removeIf」，下列做法符合推荐实践的是？
- A. removeIf 是第三方工具类的方法。
- B. 漏删是"遍历中删除"的最高频 bug——验证过 index 前移导致跳元素。
- C. removeIf 不支持条件删除。
- D. 循环中 list.remove(i) 删除元素是完全安全的。
**答案：B**
**解析：** 推荐实践：漏删是"遍历中删除"的最高频 bug——验证过 index 前移导致跳元素。。事实依据：JDK8+ 用 removeIf(lambda) 安全地按条件删除元素，内部处理了移位与 modCount。。

**Qjava-basics-1234（场景判断·语法语义）** 推荐实践：漏删是"遍历中删除"的最高频 bug——验证过 index 前移导致跳元素。
**答案：对。** 解析：JDK8+ 用 removeIf(lambda) 安全地按条件删除元素，内部处理了移位与 modCount。。原因：手写循环删除会因索引移动漏删元素。

**Qjava-basics-1235（填空·语法语义）** JDK8+ 用 ______(lambda) 安全地按条件删除元素，内部处理了移位与 modCount。
**答案：removeIf**。解析：手写循环删除会因索引移动漏删元素。

**Qjava-basics-1236（简答·语法语义）** 请说明「ArrayList」中removeIf的机制与使用要点。
**要点（标准答案）**：① JDK8+ 用 removeIf(lambda) 安全地按条件删除元素，内部处理了移位与 modCount。；② 原理：手写循环删除会因索引移动漏删元素。；③ 使用要点：漏删是"遍历中删除"的最高频 bug——验证过 index 前移导致跳元素。。版本锚点：JDK 8。

**Qjava-basics-1237（单选·正向·语法语义）** 关于「HashMap」的说法，正确的是？
- A. HashMap 在 new 时就分配了数组。
- B. new HashMap<>() 首次 put 时分配容量 16 的表（threshold=12）。
- C. HashMap 默认容量是 8。
- D. new HashMap() 首次 put 分配容量 12 的表。
**答案：B**
**解析：** new HashMap<>() 首次 put 时分配容量 16 的表（threshold=12）。。原因：16 是 2 的幂，支撑 (n-1)&hash 定位；0.75 负载下 12 个即扩容。。
**来源：** JB-029 · HashMap（JDK 8+ 源码）

**Qjava-basics-1238（判断·语法语义）** new HashMap<>() 首次 put 时分配容量 16 的表（threshold=12）。
**答案：对。** 解析：16 是 2 的幂，支撑 (n-1)&hash 定位；0.75 负载下 12 个即扩容。

**Qjava-basics-1239（判断·语法语义）** new HashMap() 首次 put 分配容量 12 的表。
**答案：错。** 正确表述：new HashMap<>() 首次 put 时分配容量 16 的表（threshold=12）。。原因：16 是 2 的幂，支撑 (n-1)&hash 定位；0.75 负载下 12 个即扩容。

**Qjava-basics-1240（判断·语法语义）** HashMap 在 new 时就分配了数组。
**答案：错。** 正确表述：new HashMap<>() 首次 put 时分配容量 16 的表（threshold=12）。。原因：16 是 2 的幂，支撑 (n-1)&hash 定位；0.75 负载下 12 个即扩容。

**Qjava-basics-1241（判断·语法语义）** HashMap 默认容量是 8。
**答案：错。** 正确表述：new HashMap<>() 首次 put 时分配容量 16 的表（threshold=12）。。原因：16 是 2 的幂，支撑 (n-1)&hash 定位；0.75 负载下 12 个即扩容。

**Qjava-basics-1242（场景单选·语法语义）** 在工程实践中关于「默认容量」，下列做法符合推荐实践的是？
- A. 本机反射验证：首插后 table.length==16。
- B. HashMap 在 new 时就分配了数组。
- C. HashMap 默认容量是 8。
- D. new HashMap() 首次 put 分配容量 12 的表。
**答案：A**
**解析：** 推荐实践：本机反射验证：首插后 table.length==16。。事实依据：new HashMap<>() 首次 put 时分配容量 16 的表（threshold=12）。。

**Qjava-basics-1243（场景判断·语法语义）** 推荐实践：本机反射验证：首插后 table.length==16。
**答案：对。** 解析：new HashMap<>() 首次 put 时分配容量 16 的表（threshold=12）。。原因：16 是 2 的幂，支撑 (n-1)&hash 定位；0.75 负载下 12 个即扩容。

**Qjava-basics-1244（简答·语法语义）** 请说明「HashMap」中默认容量的机制与使用要点。
**要点（标准答案）**：① new HashMap<>() 首次 put 时分配容量 16 的表（threshold=12）。；② 原理：16 是 2 的幂，支撑 (n-1)&hash 定位；0.75 负载下 12 个即扩容。；③ 使用要点：本机反射验证：首插后 table.length==16。。版本锚点：JDK 8+ 源码。

**Qjava-basics-1245（单选·正向·语法语义）** 关于「HashMap」的说法，正确的是？
- A. HashMap 扩容后容量可能变成非 2 的幂。
- B. HashMap 元素数超过 threshold（容量×0.75）时扩容为原来的 2 倍并重排元素。
- C. HashMap 扩容时所有元素 hash 会全部重新计算。
- D. HashMap 扩容为原来的 1.5 倍。
**答案：B**
**解析：** HashMap 元素数超过 threshold（容量×0.75）时扩容为原来的 2 倍并重排元素。。原因：2 倍保证容量始终是 2 的幂，位运算定位继续有效。。
**来源：** JB-030 · HashMap（JDK 8+ 源码）

**Qjava-basics-1246（判断·语法语义）** HashMap 元素数超过 threshold（容量×0.75）时扩容为原来的 2 倍并重排元素。
**答案：对。** 解析：2 倍保证容量始终是 2 的幂，位运算定位继续有效。

**Qjava-basics-1247（判断·语法语义）** HashMap 扩容为原来的 1.5 倍。
**答案：错。** 正确表述：HashMap 元素数超过 threshold（容量×0.75）时扩容为原来的 2 倍并重排元素。。原因：2 倍保证容量始终是 2 的幂，位运算定位继续有效。

**Qjava-basics-1248（判断·语法语义）** HashMap 扩容后容量可能变成非 2 的幂。
**答案：错。** 正确表述：HashMap 元素数超过 threshold（容量×0.75）时扩容为原来的 2 倍并重排元素。。原因：2 倍保证容量始终是 2 的幂，位运算定位继续有效。

**Qjava-basics-1249（判断·语法语义）** HashMap 扩容时所有元素 hash 会全部重新计算。
**答案：错。** 正确表述：HashMap 元素数超过 threshold（容量×0.75）时扩容为原来的 2 倍并重排元素。。原因：2 倍保证容量始终是 2 的幂，位运算定位继续有效。

**Qjava-basics-1250（场景单选·语法语义）** 在工程实践中关于「扩容翻倍」，下列做法符合推荐实践的是？
- A. HashMap 扩容为原来的 1.5 倍。
- B. HashMap 扩容后容量可能变成非 2 的幂。
- C. JDK8 优化：hash&oldCap 判断原位或 i+oldCap，不重算 hash。
- D. HashMap 扩容时所有元素 hash 会全部重新计算。
**答案：C**
**解析：** 推荐实践：JDK8 优化：hash&oldCap 判断原位或 i+oldCap，不重算 hash。。事实依据：HashMap 元素数超过 threshold（容量×0.75）时扩容为原来的 2 倍并重排元素。。

**Qjava-basics-1251（场景判断·语法语义）** 推荐实践：JDK8 优化：hash&oldCap 判断原位或 i+oldCap，不重算 hash。
**答案：对。** 解析：HashMap 元素数超过 threshold（容量×0.75）时扩容为原来的 2 倍并重排元素。。原因：2 倍保证容量始终是 2 的幂，位运算定位继续有效。

**Qjava-basics-1252（简答·语法语义）** 请说明「HashMap」中扩容翻倍的机制与使用要点。
**要点（标准答案）**：① HashMap 元素数超过 threshold（容量×0.75）时扩容为原来的 2 倍并重排元素。；② 原理：2 倍保证容量始终是 2 的幂，位运算定位继续有效。；③ 使用要点：JDK8 优化：hash&oldCap 判断原位或 i+oldCap，不重算 hash。。版本锚点：JDK 8+ 源码。

**Qjava-basics-1253（单选·正向·语法语义）** 关于「HashMap」的说法，正确的是？
- A. HashMap 用 (h = key.hashCode()) ^ (h >>> 16) 做扰动，让高位参与低位运算。
- B. HashMap 直接使用 hashCode 原值定位。
- C. 扰动函数是为了加密 hash。
- D. 扰动会把 hash 变成负数导致错误。
**答案：A**
**解析：** HashMap 用 (h = key.hashCode()) ^ (h >>> 16) 做扰动，让高位参与低位运算。。原因：容量小时只有低位参与 (n-1)&hash，不扰动高位差异会丢失。。
**来源：** JB-031 · HashMap（JDK 8+ 源码）

**Qjava-basics-1254（判断·语法语义）** HashMap 用 (h = key.hashCode()) ^ (h >>> 16) 做扰动，让高位参与低位运算。
**答案：对。** 解析：容量小时只有低位参与 (n-1)&hash，不扰动高位差异会丢失。

**Qjava-basics-1255（判断·语法语义）** HashMap 直接使用 hashCode 原值定位。
**答案：错。** 正确表述：HashMap 用 (h = key.hashCode()) ^ (h >>> 16) 做扰动，让高位参与低位运算。。原因：容量小时只有低位参与 (n-1)&hash，不扰动高位差异会丢失。

**Qjava-basics-1256（判断·语法语义）** 扰动函数是为了加密 hash。
**答案：错。** 正确表述：HashMap 用 (h = key.hashCode()) ^ (h >>> 16) 做扰动，让高位参与低位运算。。原因：容量小时只有低位参与 (n-1)&hash，不扰动高位差异会丢失。

**Qjava-basics-1257（判断·语法语义）** 扰动会把 hash 变成负数导致错误。
**答案：错。** 正确表述：HashMap 用 (h = key.hashCode()) ^ (h >>> 16) 做扰动，让高位参与低位运算。。原因：容量小时只有低位参与 (n-1)&hash，不扰动高位差异会丢失。

**Qjava-basics-1258（场景单选·语法语义）** 在工程实践中关于「扰动函数」，下列做法符合推荐实践的是？
- A. 扰动会把 hash 变成负数导致错误。
- B. 面试可写扰动公式：hash = h ^ (h >>> 16)。
- C. HashMap 直接使用 hashCode 原值定位。
- D. 扰动函数是为了加密 hash。
**答案：B**
**解析：** 推荐实践：面试可写扰动公式：hash = h ^ (h >>> 16)。。事实依据：HashMap 用 (h = key.hashCode()) ^ (h >>> 16) 做扰动，让高位参与低位运算。。

**Qjava-basics-1259（场景判断·语法语义）** 推荐实践：面试可写扰动公式：hash = h ^ (h >>> 16)。
**答案：对。** 解析：HashMap 用 (h = key.hashCode()) ^ (h >>> 16) 做扰动，让高位参与低位运算。。原因：容量小时只有低位参与 (n-1)&hash，不扰动高位差异会丢失。

**Qjava-basics-1260（简答·语法语义）** 请说明「HashMap」中扰动函数的机制与使用要点。
**要点（标准答案）**：① HashMap 用 (h = key.hashCode()) ^ (h >>> 16) 做扰动，让高位参与低位运算。；② 原理：容量小时只有低位参与 (n-1)&hash，不扰动高位差异会丢失。；③ 使用要点：面试可写扰动公式：hash = h ^ (h >>> 16)。。版本锚点：JDK 8+ 源码。

**Qjava-basics-1261（单选·正向·语法语义）** 关于「HashMap」的说法，正确的是？
- A. bin 中第 8 个节点插入时立即树化。
- B. 树化后链表节点对象会被全部替换重建。
- C. 只要链表超过 8 个就一定树化而与表容量无关。
- D. 树化在 bin 已有 8 个节点时的下一次插入（第 9 个）触发，且表长度 ≥64 才真正树化，否则先扩容。
**答案：D**
**解析：** 树化在 bin 已有 8 个节点时的下一次插入（第 9 个）触发，且表长度 ≥64 才真正树化，否则先扩容。。原因：binCount 计遍历过的非头节点数，≥7 即 bin 已有 8 个；容量<64 树化会退化为扩容。。
**来源：** JB-032 · HashMap（JDK 8+ 源码（本项目实测））

**Qjava-basics-1262（判断·语法语义）** 树化在 bin 已有 8 个节点时的下一次插入（第 9 个）触发，且表长度 ≥64 才真正树化，否则先扩容。
**答案：对。** 解析：binCount 计遍历过的非头节点数，≥7 即 bin 已有 8 个；容量<64 树化会退化为扩容。

**Qjava-basics-1263（判断·语法语义）** bin 中第 8 个节点插入时立即树化。
**答案：错。** 正确表述：树化在 bin 已有 8 个节点时的下一次插入（第 9 个）触发，且表长度 ≥64 才真正树化，否则先扩容。。原因：binCount 计遍历过的非头节点数，≥7 即 bin 已有 8 个；容量<64 树化会退化为扩容。

**Qjava-basics-1264（判断·语法语义）** 只要链表超过 8 个就一定树化而与表容量无关。
**答案：错。** 正确表述：树化在 bin 已有 8 个节点时的下一次插入（第 9 个）触发，且表长度 ≥64 才真正树化，否则先扩容。。原因：binCount 计遍历过的非头节点数，≥7 即 bin 已有 8 个；容量<64 树化会退化为扩容。

**Qjava-basics-1265（判断·语法语义）** 树化后链表节点对象会被全部替换重建。
**答案：错。** 正确表述：树化在 bin 已有 8 个节点时的下一次插入（第 9 个）触发，且表长度 ≥64 才真正树化，否则先扩容。。原因：binCount 计遍历过的非头节点数，≥7 即 bin 已有 8 个；容量<64 树化会退化为扩容。

**Qjava-basics-1266（场景单选·语法语义）** 在工程实践中关于「树化精确触发」，下列做法符合推荐实践的是？
- A. bin 中第 8 个节点插入时立即树化。
- B. 本机实测：64 容量表插 8 个同桶键仍是 Node，第 9 个转 TreeNode。
- C. 树化后链表节点对象会被全部替换重建。
- D. 只要链表超过 8 个就一定树化而与表容量无关。
**答案：B**
**解析：** 推荐实践：本机实测：64 容量表插 8 个同桶键仍是 Node，第 9 个转 TreeNode。。事实依据：树化在 bin 已有 8 个节点时的下一次插入（第 9 个）触发，且表长度 ≥64 才真正树化，否则先扩容。。

**Qjava-basics-1267（场景判断·语法语义）** 推荐实践：本机实测：64 容量表插 8 个同桶键仍是 Node，第 9 个转 TreeNode。
**答案：对。** 解析：树化在 bin 已有 8 个节点时的下一次插入（第 9 个）触发，且表长度 ≥64 才真正树化，否则先扩容。。原因：binCount 计遍历过的非头节点数，≥7 即 bin 已有 8 个；容量<64 树化会退化为扩容。

**Qjava-basics-1268（简答·语法语义）** 请说明「HashMap」中树化精确触发的机制与使用要点。
**要点（标准答案）**：① 树化在 bin 已有 8 个节点时的下一次插入（第 9 个）触发，且表长度 ≥64 才真正树化，否则先扩容。；② 原理：binCount 计遍历过的非头节点数，≥7 即 bin 已有 8 个；容量<64 树化会退化为扩容。；③ 使用要点：本机实测：64 容量表插 8 个同桶键仍是 Node，第 9 个转 TreeNode。。版本锚点：JDK 8+ 源码（本项目实测）。

**Qjava-basics-1269（单选·正向·语法语义）** 关于「HashMap」的说法，正确的是？
- A. 退化阈值是 7。
- B. 退化阈值也是 8。
- C. 红黑树节点数减到 6（UNTREEIFY_THRESHOLD）时退化回链表。
- D. 树一旦形成永远不会退化回链表。
**答案：C**
**解析：** 红黑树节点数减到 6（UNTREEIFY_THRESHOLD）时退化回链表。。原因：留 2 的缓冲（8 与 6 之间）防止在阈值附近插入删除导致树↔链表来回抖动。。
**来源：** JB-033 · HashMap（JDK 8+ 源码）

**Qjava-basics-1270（判断·语法语义）** 红黑树节点数减到 6（UNTREEIFY_THRESHOLD）时退化回链表。
**答案：对。** 解析：留 2 的缓冲（8 与 6 之间）防止在阈值附近插入删除导致树↔链表来回抖动。

**Qjava-basics-1271（判断·语法语义）** 退化阈值也是 8。
**答案：错。** 正确表述：红黑树节点数减到 6（UNTREEIFY_THRESHOLD）时退化回链表。。原因：留 2 的缓冲（8 与 6 之间）防止在阈值附近插入删除导致树↔链表来回抖动。

**Qjava-basics-1272（判断·语法语义）** 退化阈值是 7。
**答案：错。** 正确表述：红黑树节点数减到 6（UNTREEIFY_THRESHOLD）时退化回链表。。原因：留 2 的缓冲（8 与 6 之间）防止在阈值附近插入删除导致树↔链表来回抖动。

**Qjava-basics-1273（判断·语法语义）** 树一旦形成永远不会退化回链表。
**答案：错。** 正确表述：红黑树节点数减到 6（UNTREEIFY_THRESHOLD）时退化回链表。。原因：留 2 的缓冲（8 与 6 之间）防止在阈值附近插入删除导致树↔链表来回抖动。

**Qjava-basics-1274（场景单选·语法语义）** 在工程实践中关于「退化阈值」，下列做法符合推荐实践的是？
- A. 退化阈值是 7。
- B. 树一旦形成永远不会退化回链表。
- C. 退化阈值也是 8。
- D. resize 迁移时树会被拆分，数量≤6 转回链表。
**答案：D**
**解析：** 推荐实践：resize 迁移时树会被拆分，数量≤6 转回链表。。事实依据：红黑树节点数减到 6（UNTREEIFY_THRESHOLD）时退化回链表。。

**Qjava-basics-1275（场景判断·语法语义）** 推荐实践：resize 迁移时树会被拆分，数量≤6 转回链表。
**答案：对。** 解析：红黑树节点数减到 6（UNTREEIFY_THRESHOLD）时退化回链表。。原因：留 2 的缓冲（8 与 6 之间）防止在阈值附近插入删除导致树↔链表来回抖动。

**Qjava-basics-1276（简答·语法语义）** 请说明「HashMap」中退化阈值的机制与使用要点。
**要点（标准答案）**：① 红黑树节点数减到 6（UNTREEIFY_THRESHOLD）时退化回链表。；② 原理：留 2 的缓冲（8 与 6 之间）防止在阈值附近插入删除导致树↔链表来回抖动。；③ 使用要点：resize 迁移时树会被拆分，数量≤6 转回链表。。版本锚点：JDK 8+ 源码。

**Qjava-basics-1277（单选·正向·版本）** 关于「HashMap」的说法，正确的是？
- A. JDK7 并发扩容只会丢数据不会死循环。
- B. JDK7 与 JDK8 的插入策略相同。
- C. JDK7 的 HashMap 扩容迁移用头插法，并发扩容会形成环形链表导致 CPU 100%。
- D. 头插法在任何场景都比尾插快因此被保留。
**答案：C**
**解析：** JDK7 的 HashMap 扩容迁移用头插法，并发扩容会形成环形链表导致 CPU 100%。。原因：两线程同时迁移时指针交换顺序错乱成环；JDK8 改为尾插并保持顺序。。
**来源：** JB-034 · HashMap（JDK 7→8 版本史）

**Qjava-basics-1278（判断·版本）** JDK7 的 HashMap 扩容迁移用头插法，并发扩容会形成环形链表导致 CPU 100%。
**答案：对。** 解析：两线程同时迁移时指针交换顺序错乱成环；JDK8 改为尾插并保持顺序。

**Qjava-basics-1279（判断·版本）** JDK7 与 JDK8 的插入策略相同。
**答案：错。** 正确表述：JDK7 的 HashMap 扩容迁移用头插法，并发扩容会形成环形链表导致 CPU 100%。。原因：两线程同时迁移时指针交换顺序错乱成环；JDK8 改为尾插并保持顺序。

**Qjava-basics-1280（判断·版本）** JDK7 并发扩容只会丢数据不会死循环。
**答案：错。** 正确表述：JDK7 的 HashMap 扩容迁移用头插法，并发扩容会形成环形链表导致 CPU 100%。。原因：两线程同时迁移时指针交换顺序错乱成环；JDK8 改为尾插并保持顺序。

**Qjava-basics-1281（判断·版本）** 头插法在任何场景都比尾插快因此被保留。
**答案：错。** 正确表述：JDK7 的 HashMap 扩容迁移用头插法，并发扩容会形成环形链表导致 CPU 100%。。原因：两线程同时迁移时指针交换顺序错乱成环；JDK8 改为尾插并保持顺序。

**Qjava-basics-1282（场景单选·版本）** 在工程实践中关于「JDK7头插」，下列做法符合推荐实践的是？
- A. JDK7 并发扩容只会丢数据不会死循环。
- B. "HashMap 并发死循环 CPU 100%"是真实生产事故类型。
- C. JDK7 与 JDK8 的插入策略相同。
- D. 头插法在任何场景都比尾插快因此被保留。
**答案：B**
**解析：** 推荐实践："HashMap 并发死循环 CPU 100%"是真实生产事故类型。。事实依据：JDK7 的 HashMap 扩容迁移用头插法，并发扩容会形成环形链表导致 CPU 100%。。

**Qjava-basics-1283（场景判断·版本）** 推荐实践："HashMap 并发死循环 CPU 100%"是真实生产事故类型。
**答案：对。** 解析：JDK7 的 HashMap 扩容迁移用头插法，并发扩容会形成环形链表导致 CPU 100%。。原因：两线程同时迁移时指针交换顺序错乱成环；JDK8 改为尾插并保持顺序。

**Qjava-basics-1284（简答·版本）** 请说明「HashMap」中JDK7头插的机制与使用要点。
**要点（标准答案）**：① JDK7 的 HashMap 扩容迁移用头插法，并发扩容会形成环形链表导致 CPU 100%。；② 原理：两线程同时迁移时指针交换顺序错乱成环；JDK8 改为尾插并保持顺序。；③ 使用要点："HashMap 并发死循环 CPU 100%"是真实生产事故类型。。版本锚点：JDK 7→8 版本史。

**Qjava-basics-1285（单选·正向·语法语义）** 关于「HashMap」的说法，正确的是？
- A. HashMap 允许最多一个 null 键（放在 table[0] 桶），null 值不限。
- B. HashMap 的 null 键会抛 NPE。
- C. HashMap 不允许 null 键。
- D. HashMap 允许多个 null 键。
**答案：A**
**解析：** HashMap 允许最多一个 null 键（放在 table[0] 桶），null 值不限。。原因：hash(null) 返回 0，直接落在 0 号桶。。
**来源：** JB-035 · HashMap（JDK 8+ 源码）

**Qjava-basics-1286（判断·语法语义）** HashMap 允许最多一个 null 键（放在 table[0] 桶），null 值不限。
**答案：对。** 解析：hash(null) 返回 0，直接落在 0 号桶。

**Qjava-basics-1287（判断·语法语义）** HashMap 不允许 null 键。
**答案：错。** 正确表述：HashMap 允许最多一个 null 键（放在 table[0] 桶），null 值不限。。原因：hash(null) 返回 0，直接落在 0 号桶。

**Qjava-basics-1288（判断·语法语义）** HashMap 允许多个 null 键。
**答案：错。** 正确表述：HashMap 允许最多一个 null 键（放在 table[0] 桶），null 值不限。。原因：hash(null) 返回 0，直接落在 0 号桶。

**Qjava-basics-1289（判断·语法语义）** HashMap 的 null 键会抛 NPE。
**答案：错。** 正确表述：HashMap 允许最多一个 null 键（放在 table[0] 桶），null 值不限。。原因：hash(null) 返回 0，直接落在 0 号桶。

**Qjava-basics-1290（场景单选·语法语义）** 在工程实践中关于「null键」，下列做法符合推荐实践的是？
- A. HashMap 的 null 键会抛 NPE。
- B. HashMap 允许多个 null 键。
- C. HashMap 不允许 null 键。
- D. 对比：Hashtable 与 CHM 都拒绝 null 键。
**答案：D**
**解析：** 推荐实践：对比：Hashtable 与 CHM 都拒绝 null 键。。事实依据：HashMap 允许最多一个 null 键（放在 table[0] 桶），null 值不限。。

**Qjava-basics-1291（场景判断·语法语义）** 推荐实践：对比：Hashtable 与 CHM 都拒绝 null 键。
**答案：对。** 解析：HashMap 允许最多一个 null 键（放在 table[0] 桶），null 值不限。。原因：hash(null) 返回 0，直接落在 0 号桶。

**Qjava-basics-1292（填空·语法语义）** HashMap 允许最多一个 ______（放在 table[0] 桶），null 值不限。
**答案：null键**。解析：hash(null) 返回 0，直接落在 0 号桶。

**Qjava-basics-1293（简答·语法语义）** 请说明「HashMap」中null键的机制与使用要点。
**要点（标准答案）**：① HashMap 允许最多一个 null 键（放在 table[0] 桶），null 值不限。；② 原理：hash(null) 返回 0，直接落在 0 号桶。；③ 使用要点：对比：Hashtable 与 CHM 都拒绝 null 键。。版本锚点：JDK 8+ 源码。

**Qjava-basics-1294（单选·正向·误用）** 关于「HashMap」的说法，正确的是？
- A. 迭代中修改集合是完全安全的。
- B. ConcurrentModificationException 只在多线程出现。
- C. fail-fast 保证修改一定不生效。
- D. 迭代 HashMap 期间结构性修改（put/remove）会抛 ConcurrentModificationException。
**答案：D**
**解析：** 迭代 HashMap 期间结构性修改（put/remove）会抛 ConcurrentModificationException。。原因：modCount 与 expectedModCount 比对触发 fail-fast，是"尽早失败"设计。。
**来源：** JB-036 · HashMap（Iterator javadoc（fail-fast 语义））

**Qjava-basics-1295（判断·误用）** 迭代 HashMap 期间结构性修改（put/remove）会抛 ConcurrentModificationException。
**答案：对。** 解析：modCount 与 expectedModCount 比对触发 fail-fast，是"尽早失败"设计。

**Qjava-basics-1296（判断·误用）** 迭代中修改集合是完全安全的。
**答案：错。** 正确表述：迭代 HashMap 期间结构性修改（put/remove）会抛 ConcurrentModificationException。。原因：modCount 与 expectedModCount 比对触发 fail-fast，是"尽早失败"设计。

**Qjava-basics-1297（判断·误用）** fail-fast 保证修改一定不生效。
**答案：错。** 正确表述：迭代 HashMap 期间结构性修改（put/remove）会抛 ConcurrentModificationException。。原因：modCount 与 expectedModCount 比对触发 fail-fast，是"尽早失败"设计。

**Qjava-basics-1298（判断·误用）** ConcurrentModificationException 只在多线程出现。
**答案：错。** 正确表述：迭代 HashMap 期间结构性修改（put/remove）会抛 ConcurrentModificationException。。原因：modCount 与 expectedModCount 比对触发 fail-fast，是"尽早失败"设计。

**Qjava-basics-1299（场景单选·误用）** 在工程实践中关于「fail-fast」，下列做法符合推荐实践的是？
- A. 单线程迭代中修改同样抛 CME（本机实测）。
- B. ConcurrentModificationException 只在多线程出现。
- C. fail-fast 保证修改一定不生效。
- D. 迭代中修改集合是完全安全的。
**答案：A**
**解析：** 推荐实践：单线程迭代中修改同样抛 CME（本机实测）。。事实依据：迭代 HashMap 期间结构性修改（put/remove）会抛 ConcurrentModificationException。。

**Qjava-basics-1300（场景判断·误用）** 推荐实践：单线程迭代中修改同样抛 CME（本机实测）。
**答案：对。** 解析：迭代 HashMap 期间结构性修改（put/remove）会抛 ConcurrentModificationException。。原因：modCount 与 expectedModCount 比对触发 fail-fast，是"尽早失败"设计。

**Qjava-basics-1301（简答·误用）** 请说明「HashMap」中fail-fast的机制与使用要点。
**要点（标准答案）**：① 迭代 HashMap 期间结构性修改（put/remove）会抛 ConcurrentModificationException。；② 原理：modCount 与 expectedModCount 比对触发 fail-fast，是"尽早失败"设计。；③ 使用要点：单线程迭代中修改同样抛 CME（本机实测）。。版本锚点：Iterator javadoc（fail-fast 语义）。

**Qjava-basics-1302（单选·正向·语法语义）** 关于「HashMap」的说法，正确的是？
- A. LinkedHashMap 与 HashMap 无继承关系。
- B. LinkedHashMap 继承 HashMap 并用双向链表维护顺序：插入序或访问序（accessOrder=true 即 LRU）。
- C. LinkedHashMap 的 accessOrder 默认就是 true。
- D. LinkedHashMap 只能保持插入顺序。
**答案：B**
**解析：** LinkedHashMap 继承 HashMap 并用双向链表维护顺序：插入序或访问序（accessOrder=true 即 LRU）。。原因：节点自带 prev/next 链，afterNodeAccess/afterNodeInsertion 是 HashMap 预留钩子。。
**来源：** JB-037 · HashMap（JDK 8+ 源码）

**Qjava-basics-1303（判断·语法语义）** LinkedHashMap 继承 HashMap 并用双向链表维护顺序：插入序或访问序（accessOrder=true 即 LRU）。
**答案：对。** 解析：节点自带 prev/next 链，afterNodeAccess/afterNodeInsertion 是 HashMap 预留钩子。

**Qjava-basics-1304（判断·语法语义）** LinkedHashMap 只能保持插入顺序。
**答案：错。** 正确表述：LinkedHashMap 继承 HashMap 并用双向链表维护顺序：插入序或访问序（accessOrder=true 即 LRU）。。原因：节点自带 prev/next 链，afterNodeAccess/afterNodeInsertion 是 HashMap 预留钩子。

**Qjava-basics-1305（判断·语法语义）** LinkedHashMap 的 accessOrder 默认就是 true。
**答案：错。** 正确表述：LinkedHashMap 继承 HashMap 并用双向链表维护顺序：插入序或访问序（accessOrder=true 即 LRU）。。原因：节点自带 prev/next 链，afterNodeAccess/afterNodeInsertion 是 HashMap 预留钩子。

**Qjava-basics-1306（判断·语法语义）** LinkedHashMap 与 HashMap 无继承关系。
**答案：错。** 正确表述：LinkedHashMap 继承 HashMap 并用双向链表维护顺序：插入序或访问序（accessOrder=true 即 LRU）。。原因：节点自带 prev/next 链，afterNodeAccess/afterNodeInsertion 是 HashMap 预留钩子。

**Qjava-basics-1307（场景单选·语法语义）** 在工程实践中关于「LinkedHashMap」，下列做法符合推荐实践的是？
- A. LinkedHashMap 的 accessOrder 默认就是 true。
- B. accessOrder=true + removeEldestEntry 即 LRU 缓存。
- C. LinkedHashMap 只能保持插入顺序。
- D. LinkedHashMap 与 HashMap 无继承关系。
**答案：B**
**解析：** 推荐实践：accessOrder=true + removeEldestEntry 即 LRU 缓存。。事实依据：LinkedHashMap 继承 HashMap 并用双向链表维护顺序：插入序或访问序（accessOrder=true 即 LRU）。。

**Qjava-basics-1308（场景判断·语法语义）** 推荐实践：accessOrder=true + removeEldestEntry 即 LRU 缓存。
**答案：对。** 解析：LinkedHashMap 继承 HashMap 并用双向链表维护顺序：插入序或访问序（accessOrder=true 即 LRU）。。原因：节点自带 prev/next 链，afterNodeAccess/afterNodeInsertion 是 HashMap 预留钩子。

**Qjava-basics-1309（填空·语法语义）** ______ 继承 HashMap 并用双向链表维护顺序：插入序或访问序（accessOrder=true 即 LRU）。
**答案：LinkedHashMap**。解析：节点自带 prev/next 链，afterNodeAccess/afterNodeInsertion 是 HashMap 预留钩子。

**Qjava-basics-1310（简答·语法语义）** 请说明「HashMap」中LinkedHashMap的机制与使用要点。
**要点（标准答案）**：① LinkedHashMap 继承 HashMap 并用双向链表维护顺序：插入序或访问序（accessOrder=true 即 LRU）。；② 原理：节点自带 prev/next 链，afterNodeAccess/afterNodeInsertion 是 HashMap 预留钩子。；③ 使用要点：accessOrder=true + removeEldestEntry 即 LRU 缓存。。版本锚点：JDK 8+ 源码。

**Qjava-basics-1311（单选·正向·语法语义）** 关于「CHM」的说法，正确的是？
- A. CHM 使用 ReentrantLock 锁定每个桶。
- B. CHM 的所有读操作都需要加锁。
- C. JDK8 的 CHM 全表只有一把全局锁。
- D. JDK8 的 ConcurrentHashMap 用 CAS + synchronized 锁单个桶头节点实现线程安全。
**答案：D**
**解析：** JDK8 的 ConcurrentHashMap 用 CAS + synchronized 锁单个桶头节点实现线程安全。。原因：锁粒度细到桶级，冲突概率低时 synchronized（锁升级后）开销小且免额外内存。。
**来源：** JB-038 · CHM（JDK 8 源码）

**Qjava-basics-1312（判断·语法语义）** JDK8 的 ConcurrentHashMap 用 CAS + synchronized 锁单个桶头节点实现线程安全。
**答案：对。** 解析：锁粒度细到桶级，冲突概率低时 synchronized（锁升级后）开销小且免额外内存。

**Qjava-basics-1313（判断·语法语义）** JDK8 的 CHM 全表只有一把全局锁。
**答案：错。** 正确表述：JDK8 的 ConcurrentHashMap 用 CAS + synchronized 锁单个桶头节点实现线程安全。。原因：锁粒度细到桶级，冲突概率低时 synchronized（锁升级后）开销小且免额外内存。

**Qjava-basics-1314（判断·语法语义）** CHM 的所有读操作都需要加锁。
**答案：错。** 正确表述：JDK8 的 ConcurrentHashMap 用 CAS + synchronized 锁单个桶头节点实现线程安全。。原因：锁粒度细到桶级，冲突概率低时 synchronized（锁升级后）开销小且免额外内存。

**Qjava-basics-1315（判断·语法语义）** CHM 使用 ReentrantLock 锁定每个桶。
**答案：错。** 正确表述：JDK8 的 ConcurrentHashMap 用 CAS + synchronized 锁单个桶头节点实现线程安全。。原因：锁粒度细到桶级，冲突概率低时 synchronized（锁升级后）开销小且免额外内存。

**Qjava-basics-1316（场景单选·语法语义）** 在工程实践中关于「JDK8并发方案」，下列做法符合推荐实践的是？
- A. JDK7 是 Segment 分段锁（默认 16 段），JDK8 彻底重构。
- B. CHM 使用 ReentrantLock 锁定每个桶。
- C. JDK8 的 CHM 全表只有一把全局锁。
- D. CHM 的所有读操作都需要加锁。
**答案：A**
**解析：** 推荐实践：JDK7 是 Segment 分段锁（默认 16 段），JDK8 彻底重构。。事实依据：JDK8 的 ConcurrentHashMap 用 CAS + synchronized 锁单个桶头节点实现线程安全。。

**Qjava-basics-1317（场景判断·语法语义）** 推荐实践：JDK7 是 Segment 分段锁（默认 16 段），JDK8 彻底重构。
**答案：对。** 解析：JDK8 的 ConcurrentHashMap 用 CAS + synchronized 锁单个桶头节点实现线程安全。。原因：锁粒度细到桶级，冲突概率低时 synchronized（锁升级后）开销小且免额外内存。

**Qjava-basics-1318（简答·语法语义）** 请说明「CHM」中JDK8并发方案的机制与使用要点。
**要点（标准答案）**：① JDK8 的 ConcurrentHashMap 用 CAS + synchronized 锁单个桶头节点实现线程安全。；② 原理：锁粒度细到桶级，冲突概率低时 synchronized（锁升级后）开销小且免额外内存。；③ 使用要点：JDK7 是 Segment 分段锁（默认 16 段），JDK8 彻底重构。。版本锚点：JDK 8 源码。

**Qjava-basics-1319（单选·正向·误用）** 关于「CHM」的说法，正确的是？
- A. CHM 允许一个 null key 与多个 null 值。
- B. CHM 的 null 处理与 HashMap 完全相同。
- C. ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。
- D. CHM 会把 null 转换为默认值存储。
**答案：C**
**解析：** ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。。原因：并发环境下 get 返回 null 存在"不存在"与"值为 null"的二义性。。
**来源：** JB-039 · CHM（CHM javadoc）

**Qjava-basics-1320（判断·误用）** ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。
**答案：对。** 解析：并发环境下 get 返回 null 存在"不存在"与"值为 null"的二义性。

**Qjava-basics-1321（判断·误用）** CHM 允许一个 null key 与多个 null 值。
**答案：错。** 正确表述：ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。。原因：并发环境下 get 返回 null 存在"不存在"与"值为 null"的二义性。

**Qjava-basics-1322（判断·误用）** CHM 的 null 处理与 HashMap 完全相同。
**答案：错。** 正确表述：ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。。原因：并发环境下 get 返回 null 存在"不存在"与"值为 null"的二义性。

**Qjava-basics-1323（判断·误用）** CHM 会把 null 转换为默认值存储。
**答案：错。** 正确表述：ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。。原因：并发环境下 get 返回 null 存在"不存在"与"值为 null"的二义性。

**Qjava-basics-1324（场景单选·误用）** 在工程实践中关于「null拒绝」，下列做法符合推荐实践的是？
- A. CHM 会把 null 转换为默认值存储。
- B. CHM 的 null 处理与 HashMap 完全相同。
- C. CHM 允许一个 null key 与多个 null 值。
- D. 二义性论证是二面高频考点。
**答案：D**
**解析：** 推荐实践：二义性论证是二面高频考点。。事实依据：ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。。

**Qjava-basics-1325（场景判断·误用）** 推荐实践：二义性论证是二面高频考点。
**答案：对。** 解析：ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。。原因：并发环境下 get 返回 null 存在"不存在"与"值为 null"的二义性。

**Qjava-basics-1326（简答·误用）** 请说明「CHM」中null拒绝的机制与使用要点。
**要点（标准答案）**：① ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。；② 原理：并发环境下 get 返回 null 存在"不存在"与"值为 null"的二义性。；③ 使用要点：二义性论证是二面高频考点。。版本锚点：CHM javadoc。

**Qjava-basics-1327（单选·正向·语法语义）** 关于「CHM」的说法，正确的是？
- A. CHM 的 size() 返回精确值。
- B. CHM 的 size 通过 baseCount + CounterCell[] 分段计数，返回的是近似值。
- C. CHM 的 size 计算需要加全局锁。
- D. CHM 用一个 volatile int 记录 size。
**答案：B**
**解析：** CHM 的 size 通过 baseCount + CounterCell[] 分段计数，返回的是近似值。。原因：计数分散避免单点 CAS 热点（LongAdder 同源思想）。。
**来源：** JB-040 · CHM（JDK 8 源码）

**Qjava-basics-1328（判断·语法语义）** CHM 的 size 通过 baseCount + CounterCell[] 分段计数，返回的是近似值。
**答案：对。** 解析：计数分散避免单点 CAS 热点（LongAdder 同源思想）。

**Qjava-basics-1329（判断·语法语义）** CHM 的 size() 返回精确值。
**答案：错。** 正确表述：CHM 的 size 通过 baseCount + CounterCell[] 分段计数，返回的是近似值。。原因：计数分散避免单点 CAS 热点（LongAdder 同源思想）。

**Qjava-basics-1330（判断·语法语义）** CHM 用一个 volatile int 记录 size。
**答案：错。** 正确表述：CHM 的 size 通过 baseCount + CounterCell[] 分段计数，返回的是近似值。。原因：计数分散避免单点 CAS 热点（LongAdder 同源思想）。

**Qjava-basics-1331（判断·语法语义）** CHM 的 size 计算需要加全局锁。
**答案：错。** 正确表述：CHM 的 size 通过 baseCount + CounterCell[] 分段计数，返回的是近似值。。原因：计数分散避免单点 CAS 热点（LongAdder 同源思想）。

**Qjava-basics-1332（场景单选·语法语义）** 在工程实践中关于「size计数」，下列做法符合推荐实践的是？
- A. CHM 的 size() 返回精确值。
- B. CHM 用一个 volatile int 记录 size。
- C. CHM 的 size 计算需要加全局锁。
- D. 强一致 size 需求要自行加锁或换数据结构。
**答案：D**
**解析：** 推荐实践：强一致 size 需求要自行加锁或换数据结构。。事实依据：CHM 的 size 通过 baseCount + CounterCell[] 分段计数，返回的是近似值。。

**Qjava-basics-1333（场景判断·语法语义）** 推荐实践：强一致 size 需求要自行加锁或换数据结构。
**答案：对。** 解析：CHM 的 size 通过 baseCount + CounterCell[] 分段计数，返回的是近似值。。原因：计数分散避免单点 CAS 热点（LongAdder 同源思想）。

**Qjava-basics-1334（简答·语法语义）** 请说明「CHM」中size计数的机制与使用要点。
**要点（标准答案）**：① CHM 的 size 通过 baseCount + CounterCell[] 分段计数，返回的是近似值。；② 原理：计数分散避免单点 CAS 热点（LongAdder 同源思想）。；③ 使用要点：强一致 size 需求要自行加锁或换数据结构。。版本锚点：JDK 8 源码。

**Qjava-basics-1335（单选·正向·线程）** 关于「CHM」的说法，正确的是？
- A. CHM 的迭代器是弱一致的：不抛 CME，但可能读到过期数据，且不保证反映迭代期间的修改。
- B. CHM 迭代器保证看到迭代期间的所有修改。
- C. CHM 迭代中修改会抛 ConcurrentModificationException。
- D. CHM 弱一致迭代是 bug。
**答案：A**
**解析：** CHM 的迭代器是弱一致的：不抛 CME，但可能读到过期数据，且不保证反映迭代期间的修改。。原因：弱一致换取无锁读；fail-fast 是 HashMap 的行为，CHM 不是。。
**来源：** JB-041 · CHM（CHM javadoc）

**Qjava-basics-1336（判断·线程）** CHM 的迭代器是弱一致的：不抛 CME，但可能读到过期数据，且不保证反映迭代期间的修改。
**答案：对。** 解析：弱一致换取无锁读；fail-fast 是 HashMap 的行为，CHM 不是。

**Qjava-basics-1337（判断·线程）** CHM 迭代中修改会抛 ConcurrentModificationException。
**答案：错。** 正确表述：CHM 的迭代器是弱一致的：不抛 CME，但可能读到过期数据，且不保证反映迭代期间的修改。。原因：弱一致换取无锁读；fail-fast 是 HashMap 的行为，CHM 不是。

**Qjava-basics-1338（判断·线程）** CHM 迭代器保证看到迭代期间的所有修改。
**答案：错。** 正确表述：CHM 的迭代器是弱一致的：不抛 CME，但可能读到过期数据，且不保证反映迭代期间的修改。。原因：弱一致换取无锁读；fail-fast 是 HashMap 的行为，CHM 不是。

**Qjava-basics-1339（判断·线程）** CHM 弱一致迭代是 bug。
**答案：错。** 正确表述：CHM 的迭代器是弱一致的：不抛 CME，但可能读到过期数据，且不保证反映迭代期间的修改。。原因：弱一致换取无锁读；fail-fast 是 HashMap 的行为，CHM 不是。

**Qjava-basics-1340（场景单选·线程）** 在工程实践中关于「弱一致迭代」，下列做法符合推荐实践的是？
- A. CHM 弱一致迭代是 bug。
- B. 弱一致 vs fail-fast 的区别是并发容器面试必答。
- C. CHM 迭代中修改会抛 ConcurrentModificationException。
- D. CHM 迭代器保证看到迭代期间的所有修改。
**答案：B**
**解析：** 推荐实践：弱一致 vs fail-fast 的区别是并发容器面试必答。。事实依据：CHM 的迭代器是弱一致的：不抛 CME，但可能读到过期数据，且不保证反映迭代期间的修改。。

**Qjava-basics-1341（场景判断·线程）** 推荐实践：弱一致 vs fail-fast 的区别是并发容器面试必答。
**答案：对。** 解析：CHM 的迭代器是弱一致的：不抛 CME，但可能读到过期数据，且不保证反映迭代期间的修改。。原因：弱一致换取无锁读；fail-fast 是 HashMap 的行为，CHM 不是。

**Qjava-basics-1342（简答·线程）** 请说明「CHM」中弱一致迭代的机制与使用要点。
**要点（标准答案）**：① CHM 的迭代器是弱一致的：不抛 CME，但可能读到过期数据，且不保证反映迭代期间的修改。；② 原理：弱一致换取无锁读；fail-fast 是 HashMap 的行为，CHM 不是。；③ 使用要点：弱一致 vs fail-fast 的区别是并发容器面试必答。。版本锚点：CHM javadoc。

**Qjava-basics-1343（单选·正向·版本）** 关于「CHM」的说法，正确的是？
- A. JDK7 与 JDK8 的实现完全相同。
- B. JDK7 的 CHM 没有任何锁。
- C. JDK7 的 CHM 用 Segment 分段锁（默认 16 段，段继承 ReentrantLock），并发度等于段数。
- D. JDK7 的 CHM 并发度等于数组长度。
**答案：C**
**解析：** JDK7 的 CHM 用 Segment 分段锁（默认 16 段，段继承 ReentrantLock），并发度等于段数。。原因：分段把锁竞争分散，但并发度上限固定、hash 到同段的操作仍串行。。
**来源：** JB-042 · CHM（JDK 7→8 版本史）

**Qjava-basics-1344（判断·版本）** JDK7 的 CHM 用 Segment 分段锁（默认 16 段，段继承 ReentrantLock），并发度等于段数。
**答案：对。** 解析：分段把锁竞争分散，但并发度上限固定、hash 到同段的操作仍串行。

**Qjava-basics-1345（判断·版本）** JDK7 的 CHM 没有任何锁。
**答案：错。** 正确表述：JDK7 的 CHM 用 Segment 分段锁（默认 16 段，段继承 ReentrantLock），并发度等于段数。。原因：分段把锁竞争分散，但并发度上限固定、hash 到同段的操作仍串行。

**Qjava-basics-1346（判断·版本）** JDK7 的 CHM 并发度等于数组长度。
**答案：错。** 正确表述：JDK7 的 CHM 用 Segment 分段锁（默认 16 段，段继承 ReentrantLock），并发度等于段数。。原因：分段把锁竞争分散，但并发度上限固定、hash 到同段的操作仍串行。

**Qjava-basics-1347（判断·版本）** JDK7 与 JDK8 的实现完全相同。
**答案：错。** 正确表述：JDK7 的 CHM 用 Segment 分段锁（默认 16 段，段继承 ReentrantLock），并发度等于段数。。原因：分段把锁竞争分散，但并发度上限固定、hash 到同段的操作仍串行。

**Qjava-basics-1348（场景单选·版本）** 在工程实践中关于「JDK7分段锁」，下列做法符合推荐实践的是？
- A. JDK7 的 CHM 并发度等于数组长度。
- B. JDK7 的 CHM 没有任何锁。
- C. "JDK7→8 重构原因"是并发面试的分水岭题。
- D. JDK7 与 JDK8 的实现完全相同。
**答案：C**
**解析：** 推荐实践："JDK7→8 重构原因"是并发面试的分水岭题。。事实依据：JDK7 的 CHM 用 Segment 分段锁（默认 16 段，段继承 ReentrantLock），并发度等于段数。。

**Qjava-basics-1349（场景判断·版本）** 推荐实践："JDK7→8 重构原因"是并发面试的分水岭题。
**答案：对。** 解析：JDK7 的 CHM 用 Segment 分段锁（默认 16 段，段继承 ReentrantLock），并发度等于段数。。原因：分段把锁竞争分散，但并发度上限固定、hash 到同段的操作仍串行。

**Qjava-basics-1350（简答·版本）** 请说明「CHM」中JDK7分段锁的机制与使用要点。
**要点（标准答案）**：① JDK7 的 CHM 用 Segment 分段锁（默认 16 段，段继承 ReentrantLock），并发度等于段数。；② 原理：分段把锁竞争分散，但并发度上限固定、hash 到同段的操作仍串行。；③ 使用要点："JDK7→8 重构原因"是并发面试的分水岭题。。版本锚点：JDK 7→8 版本史。

**Qjava-basics-1351（单选·正向·语法语义）** 关于「TreeMap」的说法，正确的是？
- A. TreeMap 底层是红黑树，按 key 排序（自然序或 Comparator），基本操作 O(log n)。
- B. TreeMap 的基本操作是 O(1)。
- C. TreeMap 不支持排序遍历。
- D. TreeMap 底层是哈希表。
**答案：A**
**解析：** TreeMap 底层是红黑树，按 key 排序（自然序或 Comparator），基本操作 O(log n)。。原因：红黑树通过旋转与染色维持近似平衡。。
**来源：** JB-043 · TreeMap（TreeMap 源码）

**Qjava-basics-1352（判断·语法语义）** TreeMap 底层是红黑树，按 key 排序（自然序或 Comparator），基本操作 O(log n)。
**答案：对。** 解析：红黑树通过旋转与染色维持近似平衡。

**Qjava-basics-1353（判断·语法语义）** TreeMap 底层是哈希表。
**答案：错。** 正确表述：TreeMap 底层是红黑树，按 key 排序（自然序或 Comparator），基本操作 O(log n)。。原因：红黑树通过旋转与染色维持近似平衡。

**Qjava-basics-1354（判断·语法语义）** TreeMap 的基本操作是 O(1)。
**答案：错。** 正确表述：TreeMap 底层是红黑树，按 key 排序（自然序或 Comparator），基本操作 O(log n)。。原因：红黑树通过旋转与染色维持近似平衡。

**Qjava-basics-1355（判断·语法语义）** TreeMap 不支持排序遍历。
**答案：错。** 正确表述：TreeMap 底层是红黑树，按 key 排序（自然序或 Comparator），基本操作 O(log n)。。原因：红黑树通过旋转与染色维持近似平衡。

**Qjava-basics-1356（场景单选·语法语义）** 在工程实践中关于「红黑树」，下列做法符合推荐实践的是？
- A. 需要按 key 范围查询/有序遍历时选 TreeMap。
- B. TreeMap 的基本操作是 O(1)。
- C. TreeMap 不支持排序遍历。
- D. TreeMap 底层是哈希表。
**答案：A**
**解析：** 推荐实践：需要按 key 范围查询/有序遍历时选 TreeMap。。事实依据：TreeMap 底层是红黑树，按 key 排序（自然序或 Comparator），基本操作 O(log n)。。

**Qjava-basics-1357（场景判断·语法语义）** 推荐实践：需要按 key 范围查询/有序遍历时选 TreeMap。
**答案：对。** 解析：TreeMap 底层是红黑树，按 key 排序（自然序或 Comparator），基本操作 O(log n)。。原因：红黑树通过旋转与染色维持近似平衡。

**Qjava-basics-1358（填空·语法语义）** TreeMap 底层是______，按 key 排序（自然序或 Comparator），基本操作 O(log n)。
**答案：红黑树**。解析：红黑树通过旋转与染色维持近似平衡。

**Qjava-basics-1359（简答·语法语义）** 请说明「TreeMap」中红黑树的机制与使用要点。
**要点（标准答案）**：① TreeMap 底层是红黑树，按 key 排序（自然序或 Comparator），基本操作 O(log n)。；② 原理：红黑树通过旋转与染色维持近似平衡。；③ 使用要点：需要按 key 范围查询/有序遍历时选 TreeMap。。版本锚点：TreeMap 源码。

**Qjava-basics-1360（单选·正向·语法语义）** 关于「TreeMap」的说法，正确的是？
- A. TreeMap 的 get 是 O(1)。
- B. TreeMap 换来有序性但牺牲 O(1) 访问与无序性约束（key 必须可比较）。
- C. TreeMap 允许 null 键。
- D. TreeMap 在任何场景都优于 HashMap。
**答案：B**
**解析：** TreeMap 换来有序性但牺牲 O(1) 访问与无序性约束（key 必须可比较）。。原因：HashMap O(1) 但无序；按需求选型是集合面试的核心判断。。
**来源：** JB-044 · TreeMap（集合选型通用）

**Qjava-basics-1361（判断·语法语义）** TreeMap 换来有序性但牺牲 O(1) 访问与无序性约束（key 必须可比较）。
**答案：对。** 解析：HashMap O(1) 但无序；按需求选型是集合面试的核心判断。

**Qjava-basics-1362（判断·语法语义）** TreeMap 在任何场景都优于 HashMap。
**答案：错。** 正确表述：TreeMap 换来有序性但牺牲 O(1) 访问与无序性约束（key 必须可比较）。。原因：HashMap O(1) 但无序；按需求选型是集合面试的核心判断。

**Qjava-basics-1363（判断·语法语义）** TreeMap 的 get 是 O(1)。
**答案：错。** 正确表述：TreeMap 换来有序性但牺牲 O(1) 访问与无序性约束（key 必须可比较）。。原因：HashMap O(1) 但无序；按需求选型是集合面试的核心判断。

**Qjava-basics-1364（判断·语法语义）** TreeMap 允许 null 键。
**答案：错。** 正确表述：TreeMap 换来有序性但牺牲 O(1) 访问与无序性约束（key 必须可比较）。。原因：HashMap O(1) 但无序；按需求选型是集合面试的核心判断。

**Qjava-basics-1365（场景单选·语法语义）** 在工程实践中关于「与HashMap选型」，下列做法符合推荐实践的是？
- A. TreeMap 在任何场景都优于 HashMap。
- B. TreeMap 允许 null 键。
- C. TreeMap 的 get 是 O(1)。
- D. 范围查询 headMap/tailMap/subMap 是 TreeMap 独有能力。
**答案：D**
**解析：** 推荐实践：范围查询 headMap/tailMap/subMap 是 TreeMap 独有能力。。事实依据：TreeMap 换来有序性但牺牲 O(1) 访问与无序性约束（key 必须可比较）。。

**Qjava-basics-1366（场景判断·语法语义）** 推荐实践：范围查询 headMap/tailMap/subMap 是 TreeMap 独有能力。
**答案：对。** 解析：TreeMap 换来有序性但牺牲 O(1) 访问与无序性约束（key 必须可比较）。。原因：HashMap O(1) 但无序；按需求选型是集合面试的核心判断。

**Qjava-basics-1367（简答·语法语义）** 请说明「TreeMap」中与HashMap选型的机制与使用要点。
**要点（标准答案）**：① TreeMap 换来有序性但牺牲 O(1) 访问与无序性约束（key 必须可比较）。；② 原理：HashMap O(1) 但无序；按需求选型是集合面试的核心判断。；③ 使用要点：范围查询 headMap/tailMap/subMap 是 TreeMap 独有能力。。版本锚点：集合选型通用。

**Qjava-basics-1368（单选·正向·语法语义）** 关于「ConcurrentSkipListMap」的说法，正确的是？
- A. ConcurrentSkipListMap 底层是红黑树。
- B. ConcurrentSkipListMap 的读操作需要加锁。
- C. 它是有序并发场景的替代品这一说法是错的。
- D. ConcurrentSkipListMap 用跳表（多级索引链表）实现有序 + 高并发，基本操作 O(log n)。
**答案：D**
**解析：** ConcurrentSkipListMap 用跳表（多级索引链表）实现有序 + 高并发，基本操作 O(log n)。。原因：跳表无需旋转即可维持平衡，天然适合无锁化并发读。。
**来源：** JB-045 · ConcurrentSkipListMap（JDK 6+ ConcurrentSkipListMap）

**Qjava-basics-1369（判断·语法语义）** ConcurrentSkipListMap 用跳表（多级索引链表）实现有序 + 高并发，基本操作 O(log n)。
**答案：对。** 解析：跳表无需旋转即可维持平衡，天然适合无锁化并发读。

**Qjava-basics-1370（判断·语法语义）** ConcurrentSkipListMap 底层是红黑树。
**答案：错。** 正确表述：ConcurrentSkipListMap 用跳表（多级索引链表）实现有序 + 高并发，基本操作 O(log n)。。原因：跳表无需旋转即可维持平衡，天然适合无锁化并发读。

**Qjava-basics-1371（判断·语法语义）** ConcurrentSkipListMap 的读操作需要加锁。
**答案：错。** 正确表述：ConcurrentSkipListMap 用跳表（多级索引链表）实现有序 + 高并发，基本操作 O(log n)。。原因：跳表无需旋转即可维持平衡，天然适合无锁化并发读。

**Qjava-basics-1372（判断·语法语义）** 它是有序并发场景的替代品这一说法是错的。
**答案：错。** 正确表述：ConcurrentSkipListMap 用跳表（多级索引链表）实现有序 + 高并发，基本操作 O(log n)。。原因：跳表无需旋转即可维持平衡，天然适合无锁化并发读。

**Qjava-basics-1373（场景单选·语法语义）** 在工程实践中关于「跳表」，下列做法符合推荐实践的是？
- A. 它是有序并发场景的替代品这一说法是错的。
- B. ConcurrentSkipListMap 底层是红黑树。
- C. ConcurrentSkipListMap 的读操作需要加锁。
- D. 有序 + 高并发（如排行榜）场景用它替代 TreeMap+Synchronized。
**答案：D**
**解析：** 推荐实践：有序 + 高并发（如排行榜）场景用它替代 TreeMap+Synchronized。。事实依据：ConcurrentSkipListMap 用跳表（多级索引链表）实现有序 + 高并发，基本操作 O(log n)。。

**Qjava-basics-1374（场景判断·语法语义）** 推荐实践：有序 + 高并发（如排行榜）场景用它替代 TreeMap+Synchronized。
**答案：对。** 解析：ConcurrentSkipListMap 用跳表（多级索引链表）实现有序 + 高并发，基本操作 O(log n)。。原因：跳表无需旋转即可维持平衡，天然适合无锁化并发读。

**Qjava-basics-1375（填空·语法语义）** ConcurrentSkipListMap 用______（多级索引链表）实现有序 + 高并发，基本操作 O(log n)。
**答案：跳表**。解析：跳表无需旋转即可维持平衡，天然适合无锁化并发读。

**Qjava-basics-1376（简答·语法语义）** 请说明「ConcurrentSkipListMap」中跳表的机制与使用要点。
**要点（标准答案）**：① ConcurrentSkipListMap 用跳表（多级索引链表）实现有序 + 高并发，基本操作 O(log n)。；② 原理：跳表无需旋转即可维持平衡，天然适合无锁化并发读。；③ 使用要点：有序 + 高并发（如排行榜）场景用它替代 TreeMap+Synchronized。。版本锚点：JDK 6+ ConcurrentSkipListMap。

**Qjava-basics-1377（单选·正向·语法语义）** 关于「泛型」的说法，正确的是？
- A. List<String> 运行时携带 String 类型信息。
- B. 泛型检查发生在运行期。
- C. 擦除意味着泛型完全没有任何运行时痕迹。
- D. Java 泛型是编译期检查、运行时擦除：List<String> 与 List<Integer> 运行时是同一个类。
**答案：D**
**解析：** Java 泛型是编译期检查、运行时擦除：List<String> 与 List<Integer> 运行时是同一个类。。原因：向后兼容 JDK5 之前的字节码；泛型信息仅保留在 Signature 属性供反射读取。。
**来源：** JB-046 · 泛型（JLS 4.6（擦除））

**Qjava-basics-1378（判断·语法语义）** Java 泛型是编译期检查、运行时擦除：List<String> 与 List<Integer> 运行时是同一个类。
**答案：对。** 解析：向后兼容 JDK5 之前的字节码；泛型信息仅保留在 Signature 属性供反射读取。

**Qjava-basics-1379（判断·语法语义）** List<String> 运行时携带 String 类型信息。
**答案：错。** 正确表述：Java 泛型是编译期检查、运行时擦除：List<String> 与 List<Integer> 运行时是同一个类。。原因：向后兼容 JDK5 之前的字节码；泛型信息仅保留在 Signature 属性供反射读取。

**Qjava-basics-1380（判断·语法语义）** 擦除意味着泛型完全没有任何运行时痕迹。
**答案：错。** 正确表述：Java 泛型是编译期检查、运行时擦除：List<String> 与 List<Integer> 运行时是同一个类。。原因：向后兼容 JDK5 之前的字节码；泛型信息仅保留在 Signature 属性供反射读取。

**Qjava-basics-1381（判断·语法语义）** 泛型检查发生在运行期。
**答案：错。** 正确表述：Java 泛型是编译期检查、运行时擦除：List<String> 与 List<Integer> 运行时是同一个类。。原因：向后兼容 JDK5 之前的字节码；泛型信息仅保留在 Signature 属性供反射读取。

**Qjava-basics-1382（场景单选·语法语义）** 在工程实践中关于「类型擦除」，下列做法符合推荐实践的是？
- A. 泛型检查发生在运行期。
- B. 反射 getGenericType() 可读取声明处的泛型参数。
- C. List<String> 运行时携带 String 类型信息。
- D. 擦除意味着泛型完全没有任何运行时痕迹。
**答案：B**
**解析：** 推荐实践：反射 getGenericType() 可读取声明处的泛型参数。。事实依据：Java 泛型是编译期检查、运行时擦除：List<String> 与 List<Integer> 运行时是同一个类。。

**Qjava-basics-1383（场景判断·语法语义）** 推荐实践：反射 getGenericType() 可读取声明处的泛型参数。
**答案：对。** 解析：Java 泛型是编译期检查、运行时擦除：List<String> 与 List<Integer> 运行时是同一个类。。原因：向后兼容 JDK5 之前的字节码；泛型信息仅保留在 Signature 属性供反射读取。

**Qjava-basics-1384（简答·语法语义）** 请说明「泛型」中类型擦除的机制与使用要点。
**要点（标准答案）**：① Java 泛型是编译期检查、运行时擦除：List<String> 与 List<Integer> 运行时是同一个类。；② 原理：向后兼容 JDK5 之前的字节码；泛型信息仅保留在 Signature 属性供反射读取。；③ 使用要点：反射 getGenericType() 可读取声明处的泛型参数。。版本锚点：JLS 4.6（擦除）。

**Qjava-basics-1385（单选·正向·语法语义）** 关于「泛型」的说法，正确的是？
- A. 类型擦除导致：不能 new T()、不能 new T[]、不能 instanceof T、静态成员不能用类的泛型参数。
- B. 泛型类中可以创建 T 的实例。
- C. 泛型类的静态方法可以访问类的泛型参数。
- D. T[] 数组可以正常 new 出来。
**答案：A**
**解析：** 类型擦除导致：不能 new T()、不能 new T[]、不能 instanceof T、静态成员不能用类的泛型参数。。原因：运行时没有 T 的类型信息，静态成员属于类不属于实例。。
**来源：** JB-047 · 泛型（JLS 4.x）

**Qjava-basics-1386（判断·语法语义）** 类型擦除导致：不能 new T()、不能 new T[]、不能 instanceof T、静态成员不能用类的泛型参数。
**答案：对。** 解析：运行时没有 T 的类型信息，静态成员属于类不属于实例。

**Qjava-basics-1387（判断·语法语义）** 泛型类中可以创建 T 的实例。
**答案：错。** 正确表述：类型擦除导致：不能 new T()、不能 new T[]、不能 instanceof T、静态成员不能用类的泛型参数。。原因：运行时没有 T 的类型信息，静态成员属于类不属于实例。

**Qjava-basics-1388（判断·语法语义）** 泛型类的静态方法可以访问类的泛型参数。
**答案：错。** 正确表述：类型擦除导致：不能 new T()、不能 new T[]、不能 instanceof T、静态成员不能用类的泛型参数。。原因：运行时没有 T 的类型信息，静态成员属于类不属于实例。

**Qjava-basics-1389（判断·语法语义）** T[] 数组可以正常 new 出来。
**答案：错。** 正确表述：类型擦除导致：不能 new T()、不能 new T[]、不能 instanceof T、静态成员不能用类的泛型参数。。原因：运行时没有 T 的类型信息，静态成员属于类不属于实例。

**Qjava-basics-1390（场景单选·语法语义）** 在工程实践中关于「限制」，下列做法符合推荐实践的是？
- A. T[] 数组可以正常 new 出来。
- B. 泛型类中可以创建 T 的实例。
- C. 泛型类的静态方法可以访问类的泛型参数。
- D. 绕行方案：传 Class<T> 用反射构造、或用数组列表。
**答案：D**
**解析：** 推荐实践：绕行方案：传 Class<T> 用反射构造、或用数组列表。。事实依据：类型擦除导致：不能 new T()、不能 new T[]、不能 instanceof T、静态成员不能用类的泛型参数。。

**Qjava-basics-1391（场景判断·语法语义）** 推荐实践：绕行方案：传 Class<T> 用反射构造、或用数组列表。
**答案：对。** 解析：类型擦除导致：不能 new T()、不能 new T[]、不能 instanceof T、静态成员不能用类的泛型参数。。原因：运行时没有 T 的类型信息，静态成员属于类不属于实例。

**Qjava-basics-1392（简答·语法语义）** 请说明「泛型」中限制的机制与使用要点。
**要点（标准答案）**：① 类型擦除导致：不能 new T()、不能 new T[]、不能 instanceof T、静态成员不能用类的泛型参数。；② 原理：运行时没有 T 的类型信息，静态成员属于类不属于实例。；③ 使用要点：绕行方案：传 Class<T> 用反射构造、或用数组列表。。版本锚点：JLS 4.x。

**Qjava-basics-1393（单选·正向·语法语义）** 关于「泛型」的说法，正确的是？
- A. 通配符列表可以任意 add 任意类型。
- B. 通配符原则 PECS：Producer Extends（只读用 ? extends）、Consumer Super（只写用 ? super）。
- C. PECS 只适用于数组。
- D. extends 与 super 在泛型里可以随意互换。
**答案：B**
**解析：** 通配符原则 PECS：Producer Extends（只读用 ? extends）、Consumer Super（只写用 ? super）。。原因：extends 通配的列表不能 add（除 null），super 通配的列表读取需强转——编译器按读写角色约束。。
**来源：** JB-048 · 泛型（Effective Java Item 31）

**Qjava-basics-1394（判断·语法语义）** 通配符原则 PECS：Producer Extends（只读用 ? extends）、Consumer Super（只写用 ? super）。
**答案：对。** 解析：extends 通配的列表不能 add（除 null），super 通配的列表读取需强转——编译器按读写角色约束。

**Qjava-basics-1395（判断·语法语义）** extends 与 super 在泛型里可以随意互换。
**答案：错。** 正确表述：通配符原则 PECS：Producer Extends（只读用 ? extends）、Consumer Super（只写用 ? super）。。原因：extends 通配的列表不能 add（除 null），super 通配的列表读取需强转——编译器按读写角色约束。

**Qjava-basics-1396（判断·语法语义）** PECS 只适用于数组。
**答案：错。** 正确表述：通配符原则 PECS：Producer Extends（只读用 ? extends）、Consumer Super（只写用 ? super）。。原因：extends 通配的列表不能 add（除 null），super 通配的列表读取需强转——编译器按读写角色约束。

**Qjava-basics-1397（判断·语法语义）** 通配符列表可以任意 add 任意类型。
**答案：错。** 正确表述：通配符原则 PECS：Producer Extends（只读用 ? extends）、Consumer Super（只写用 ? super）。。原因：extends 通配的列表不能 add（除 null），super 通配的列表读取需强转——编译器按读写角色约束。

**Qjava-basics-1398（场景单选·语法语义）** 在工程实践中关于「PECS」，下列做法符合推荐实践的是？
- A. PECS 只适用于数组。
- B. JDK 源码 Collections.copy 就是 PECS 的标准示范（src extends, dest super）。
- C. extends 与 super 在泛型里可以随意互换。
- D. 通配符列表可以任意 add 任意类型。
**答案：B**
**解析：** 推荐实践：JDK 源码 Collections.copy 就是 PECS 的标准示范（src extends, dest super）。。事实依据：通配符原则 PECS：Producer Extends（只读用 ? extends）、Consumer Super（只写用 ? super）。。

**Qjava-basics-1399（场景判断·语法语义）** 推荐实践：JDK 源码 Collections.copy 就是 PECS 的标准示范（src extends, dest super）。
**答案：对。** 解析：通配符原则 PECS：Producer Extends（只读用 ? extends）、Consumer Super（只写用 ? super）。。原因：extends 通配的列表不能 add（除 null），super 通配的列表读取需强转——编译器按读写角色约束。

**Qjava-basics-1400（填空·语法语义）** 通配符原则 ______：Producer Extends（只读用 ? extends）、Consumer Super（只写用 ? super）。
**答案：PECS**。解析：extends 通配的列表不能 add（除 null），super 通配的列表读取需强转——编译器按读写角色约束。

**Qjava-basics-1401（简答·语法语义）** 请说明「泛型」中PECS的机制与使用要点。
**要点（标准答案）**：① 通配符原则 PECS：Producer Extends（只读用 ? extends）、Consumer Super（只写用 ? super）。；② 原理：extends 通配的列表不能 add（除 null），super 通配的列表读取需强转——编译器按读写角色约束。；③ 使用要点：JDK 源码 Collections.copy 就是 PECS 的标准示范（src extends, dest super）。。版本锚点：Effective Java Item 31。

**Qjava-basics-1402（单选·正向·误用）** 关于「泛型」的说法，正确的是？
- A. 泛型重载可以按类型参数区分。
- B. List<String> 与 List<Integer> 运行时是不同类。
- C. 擦除后签名相同的两个泛型重载方法无法编译，如 f(List<String>) 与 f(List<Integer>)。
- D. 擦除不影响方法重载。
**答案：C**
**解析：** 擦除后签名相同的两个泛型重载方法无法编译，如 f(List<String>) 与 f(List<Integer>)。。原因：擦除后两者参数类型都是 List，字节码签名相同。。
**来源：** JB-049 · 泛型（JLS 15.12）

**Qjava-basics-1403（判断·误用）** 擦除后签名相同的两个泛型重载方法无法编译，如 f(List<String>) 与 f(List<Integer>)。
**答案：对。** 解析：擦除后两者参数类型都是 List，字节码签名相同。

**Qjava-basics-1404（判断·误用）** 泛型重载可以按类型参数区分。
**答案：错。** 正确表述：擦除后签名相同的两个泛型重载方法无法编译，如 f(List<String>) 与 f(List<Integer>)。。原因：擦除后两者参数类型都是 List，字节码签名相同。

**Qjava-basics-1405（判断·误用）** 擦除不影响方法重载。
**答案：错。** 正确表述：擦除后签名相同的两个泛型重载方法无法编译，如 f(List<String>) 与 f(List<Integer>)。。原因：擦除后两者参数类型都是 List，字节码签名相同。

**Qjava-basics-1406（判断·误用）** List<String> 与 List<Integer> 运行时是不同类。
**答案：错。** 正确表述：擦除后签名相同的两个泛型重载方法无法编译，如 f(List<String>) 与 f(List<Integer>)。。原因：擦除后两者参数类型都是 List，字节码签名相同。

**Qjava-basics-1407（场景单选·误用）** 在工程实践中关于「重载冲突」，下列做法符合推荐实践的是？
- A. 擦除不影响方法重载。
- B. List<String> 与 List<Integer> 运行时是不同类。
- C. 泛型重载可以按类型参数区分。
- D. javac 报"具有相同擦除签名"错误。
**答案：D**
**解析：** 推荐实践：javac 报"具有相同擦除签名"错误。。事实依据：擦除后签名相同的两个泛型重载方法无法编译，如 f(List<String>) 与 f(List<Integer>)。。

**Qjava-basics-1408（场景判断·误用）** 推荐实践：javac 报"具有相同擦除签名"错误。
**答案：对。** 解析：擦除后签名相同的两个泛型重载方法无法编译，如 f(List<String>) 与 f(List<Integer>)。。原因：擦除后两者参数类型都是 List，字节码签名相同。

**Qjava-basics-1409（简答·误用）** 请说明「泛型」中重载冲突的机制与使用要点。
**要点（标准答案）**：① 擦除后签名相同的两个泛型重载方法无法编译，如 f(List<String>) 与 f(List<Integer>)。；② 原理：擦除后两者参数类型都是 List，字节码签名相同。；③ 使用要点：javac 报"具有相同擦除签名"错误。。版本锚点：JLS 15.12。

**Qjava-basics-1410（单选·正向·语法语义）** 关于「异常」的说法，正确的是？
- A. RuntimeException 不需要处理所以不算异常。
- B. 所有异常都必须被捕获。
- C. Checked 异常编译期强制处理，RuntimeException 及其子类不强制。
- D. IOException 是 RuntimeException 的子类。
**答案：C**
**解析：** Checked 异常编译期强制处理，RuntimeException 及其子类不强制。。原因：Checked 的初衷是强制调用方处理可恢复错误，但工程实践暴露了大量吞异常问题。。
**来源：** JB-050 · 异常（JLS 11.2）

**Qjava-basics-1411（判断·语法语义）** Checked 异常编译期强制处理，RuntimeException 及其子类不强制。
**答案：对。** 解析：Checked 的初衷是强制调用方处理可恢复错误，但工程实践暴露了大量吞异常问题。

**Qjava-basics-1412（判断·语法语义）** IOException 是 RuntimeException 的子类。
**答案：错。** 正确表述：Checked 异常编译期强制处理，RuntimeException 及其子类不强制。。原因：Checked 的初衷是强制调用方处理可恢复错误，但工程实践暴露了大量吞异常问题。

**Qjava-basics-1413（判断·语法语义）** RuntimeException 不需要处理所以不算异常。
**答案：错。** 正确表述：Checked 异常编译期强制处理，RuntimeException 及其子类不强制。。原因：Checked 的初衷是强制调用方处理可恢复错误，但工程实践暴露了大量吞异常问题。

**Qjava-basics-1414（判断·语法语义）** 所有异常都必须被捕获。
**答案：错。** 正确表述：Checked 异常编译期强制处理，RuntimeException 及其子类不强制。。原因：Checked 的初衷是强制调用方处理可恢复错误，但工程实践暴露了大量吞异常问题。

**Qjava-basics-1415（场景单选·语法语义）** 在工程实践中关于「Checked与Runtime」，下列做法符合推荐实践的是？
- A. 自定义业务异常统一继承 RuntimeException 是主流实践。
- B. IOException 是 RuntimeException 的子类。
- C. RuntimeException 不需要处理所以不算异常。
- D. 所有异常都必须被捕获。
**答案：A**
**解析：** 推荐实践：自定义业务异常统一继承 RuntimeException 是主流实践。。事实依据：Checked 异常编译期强制处理，RuntimeException 及其子类不强制。。

**Qjava-basics-1416（场景判断·语法语义）** 推荐实践：自定义业务异常统一继承 RuntimeException 是主流实践。
**答案：对。** 解析：Checked 异常编译期强制处理，RuntimeException 及其子类不强制。。原因：Checked 的初衷是强制调用方处理可恢复错误，但工程实践暴露了大量吞异常问题。

**Qjava-basics-1417（简答·语法语义）** 请说明「异常」中Checked与Runtime的机制与使用要点。
**要点（标准答案）**：① Checked 异常编译期强制处理，RuntimeException 及其子类不强制。；② 原理：Checked 的初衷是强制调用方处理可恢复错误，但工程实践暴露了大量吞异常问题。；③ 使用要点：自定义业务异常统一继承 RuntimeException 是主流实践。。版本锚点：JLS 11.2。

**Qjava-basics-1418（单选·正向·误用）** 关于「异常」的说法，正确的是？
- A. 捕获异常后打个日志就算完整处理了。
- B. 异常被捕获后对系统没有任何影响。
- C. 捕获异常后既不处理也不抛出（空 catch 或仅 printStackTrace）是高危反模式：故障被静默掩盖。
- D. finally 里抛异常会覆盖原异常——所以 finally 只做资源清理。
**答案：C**
**解析：** 捕获异常后既不处理也不抛出（空 catch 或仅 printStackTrace）是高危反模式：故障被静默掩盖。。原因：异常包含故障现场，吞掉等于销毁证据链。。
**来源：** JB-051 · 异常（代码规范通用条款）

**Qjava-basics-1419（判断·误用）** 捕获异常后既不处理也不抛出（空 catch 或仅 printStackTrace）是高危反模式：故障被静默掩盖。
**答案：对。** 解析：异常包含故障现场，吞掉等于销毁证据链。

**Qjava-basics-1420（判断·误用）** 捕获异常后打个日志就算完整处理了。
**答案：错。** 正确表述：捕获异常后既不处理也不抛出（空 catch 或仅 printStackTrace）是高危反模式：故障被静默掩盖。。原因：异常包含故障现场，吞掉等于销毁证据链。

**Qjava-basics-1421（判断·误用）** 异常被捕获后对系统没有任何影响。
**答案：错。** 正确表述：捕获异常后既不处理也不抛出（空 catch 或仅 printStackTrace）是高危反模式：故障被静默掩盖。。原因：异常包含故障现场，吞掉等于销毁证据链。

**Qjava-basics-1422（判断·误用）** finally 里抛异常会覆盖原异常——所以 finally 只做资源清理。
**答案：错。** 正确表述：捕获异常后既不处理也不抛出（空 catch 或仅 printStackTrace）是高危反模式：故障被静默掩盖。。原因：异常包含故障现场，吞掉等于销毁证据链。

**Qjava-basics-1423（场景单选·误用）** 在工程实践中关于「吞异常」，下列做法符合推荐实践的是？
- A. 捕获异常后打个日志就算完整处理了。
- B. 异常被捕获后对系统没有任何影响。
- C. finally 里抛异常会覆盖原异常——所以 finally 只做资源清理。
- D. 空 catch 在静态检查中应标记为阻断级问题。
**答案：D**
**解析：** 推荐实践：空 catch 在静态检查中应标记为阻断级问题。。事实依据：捕获异常后既不处理也不抛出（空 catch 或仅 printStackTrace）是高危反模式：故障被静默掩盖。。

**Qjava-basics-1424（场景判断·误用）** 推荐实践：空 catch 在静态检查中应标记为阻断级问题。
**答案：对。** 解析：捕获异常后既不处理也不抛出（空 catch 或仅 printStackTrace）是高危反模式：故障被静默掩盖。。原因：异常包含故障现场，吞掉等于销毁证据链。

**Qjava-basics-1425（简答·误用）** 请说明「异常」中吞异常的机制与使用要点。
**要点（标准答案）**：① 捕获异常后既不处理也不抛出（空 catch 或仅 printStackTrace）是高危反模式：故障被静默掩盖。；② 原理：异常包含故障现场，吞掉等于销毁证据链。；③ 使用要点：空 catch 在静态检查中应标记为阻断级问题。。版本锚点：代码规范通用条款。

**Qjava-basics-1426（单选·正向·语法语义）** 关于「异常」的说法，正确的是？
- A. finally 执行顺序不确定。
- B. finally 只在 try 正常结束时执行。
- C. finally 块在 try/catch 之后必然执行（除非 JVM 退出或线程死亡），且其中的 return 会覆盖 try/catch 的返回值与异常。
- D. finally 中 return 后原异常仍会抛出。
**答案：C**
**解析：** finally 块在 try/catch 之后必然执行（除非 JVM 退出或线程死亡），且其中的 return 会覆盖 try/catch 的返回值与异常。。原因：编译器把 finally 代码内联到所有出口路径。。
**来源：** JB-052 · 异常（JLS 14.20）

**Qjava-basics-1427（判断·语法语义）** finally 块在 try/catch 之后必然执行（除非 JVM 退出或线程死亡），且其中的 return 会覆盖 try/catch 的返回值与异常。
**答案：对。** 解析：编译器把 finally 代码内联到所有出口路径。

**Qjava-basics-1428（判断·语法语义）** finally 只在 try 正常结束时执行。
**答案：错。** 正确表述：finally 块在 try/catch 之后必然执行（除非 JVM 退出或线程死亡），且其中的 return 会覆盖 try/catch 的返回值与异常。。原因：编译器把 finally 代码内联到所有出口路径。

**Qjava-basics-1429（判断·语法语义）** finally 中 return 后原异常仍会抛出。
**答案：错。** 正确表述：finally 块在 try/catch 之后必然执行（除非 JVM 退出或线程死亡），且其中的 return 会覆盖 try/catch 的返回值与异常。。原因：编译器把 finally 代码内联到所有出口路径。

**Qjava-basics-1430（判断·语法语义）** finally 执行顺序不确定。
**答案：错。** 正确表述：finally 块在 try/catch 之后必然执行（除非 JVM 退出或线程死亡），且其中的 return 会覆盖 try/catch 的返回值与异常。。原因：编译器把 finally 代码内联到所有出口路径。

**Qjava-basics-1431（场景单选·语法语义）** 在工程实践中关于「finally执行」，下列做法符合推荐实践的是？
- A. finally 只在 try 正常结束时执行。
- B. 阿里手册：禁止在 finally 中使用 return。
- C. finally 中 return 后原异常仍会抛出。
- D. finally 执行顺序不确定。
**答案：B**
**解析：** 推荐实践：阿里手册：禁止在 finally 中使用 return。。事实依据：finally 块在 try/catch 之后必然执行（除非 JVM 退出或线程死亡），且其中的 return 会覆盖 try/catch 的返回值与异常。。

**Qjava-basics-1432（场景判断·语法语义）** 推荐实践：阿里手册：禁止在 finally 中使用 return。
**答案：对。** 解析：finally 块在 try/catch 之后必然执行（除非 JVM 退出或线程死亡），且其中的 return 会覆盖 try/catch 的返回值与异常。。原因：编译器把 finally 代码内联到所有出口路径。

**Qjava-basics-1433（简答·语法语义）** 请说明「异常」中finally执行的机制与使用要点。
**要点（标准答案）**：① finally 块在 try/catch 之后必然执行（除非 JVM 退出或线程死亡），且其中的 return 会覆盖 try/catch 的返回值与异常。；② 原理：编译器把 finally 代码内联到所有出口路径。；③ 使用要点：阿里手册：禁止在 finally 中使用 return。。版本锚点：JLS 14.20。

**Qjava-basics-1434（单选·正向·语法语义）** 关于「异常」的说法，正确的是？
- A. 资源 close 的顺序与声明顺序相同。
- B. try-with-resources 只支持 IO 流。
- C. try-with-resources 会吞掉 try 块中的异常。
- D. 实现 AutoCloseable 的资源必须用 try-with-resources：编译器按声明逆序自动 close 并保留抑制异常。
**答案：D**
**解析：** 实现 AutoCloseable 的资源必须用 try-with-resources：编译器按声明逆序自动 close 并保留抑制异常。。原因：手动 close 可能因提前 return/异常被跳过；抑制异常（addSuppressed）保留关闭失败的次要异常。。
**来源：** JB-053 · 异常（JDK 7+（JLS 14.20.3））

**Qjava-basics-1435（判断·语法语义）** 实现 AutoCloseable 的资源必须用 try-with-resources：编译器按声明逆序自动 close 并保留抑制异常。
**答案：对。** 解析：手动 close 可能因提前 return/异常被跳过；抑制异常（addSuppressed）保留关闭失败的次要异常。

**Qjava-basics-1436（判断·语法语义）** try-with-resources 只支持 IO 流。
**答案：错。** 正确表述：实现 AutoCloseable 的资源必须用 try-with-resources：编译器按声明逆序自动 close 并保留抑制异常。。原因：手动 close 可能因提前 return/异常被跳过；抑制异常（addSuppressed）保留关闭失败的次要异常。

**Qjava-basics-1437（判断·语法语义）** try-with-resources 会吞掉 try 块中的异常。
**答案：错。** 正确表述：实现 AutoCloseable 的资源必须用 try-with-resources：编译器按声明逆序自动 close 并保留抑制异常。。原因：手动 close 可能因提前 return/异常被跳过；抑制异常（addSuppressed）保留关闭失败的次要异常。

**Qjava-basics-1438（判断·语法语义）** 资源 close 的顺序与声明顺序相同。
**答案：错。** 正确表述：实现 AutoCloseable 的资源必须用 try-with-resources：编译器按声明逆序自动 close 并保留抑制异常。。原因：手动 close 可能因提前 return/异常被跳过；抑制异常（addSuppressed）保留关闭失败的次要异常。

**Qjava-basics-1439（场景单选·语法语义）** 在工程实践中关于「try-with-resources」，下列做法符合推荐实践的是？
- A. try-with-resources 只支持 IO 流。
- B. 自定义资源类实现 AutoCloseable 即可享受语法糖。
- C. 资源 close 的顺序与声明顺序相同。
- D. try-with-resources 会吞掉 try 块中的异常。
**答案：B**
**解析：** 推荐实践：自定义资源类实现 AutoCloseable 即可享受语法糖。。事实依据：实现 AutoCloseable 的资源必须用 try-with-resources：编译器按声明逆序自动 close 并保留抑制异常。。

**Qjava-basics-1440（场景判断·语法语义）** 推荐实践：自定义资源类实现 AutoCloseable 即可享受语法糖。
**答案：对。** 解析：实现 AutoCloseable 的资源必须用 try-with-resources：编译器按声明逆序自动 close 并保留抑制异常。。原因：手动 close 可能因提前 return/异常被跳过；抑制异常（addSuppressed）保留关闭失败的次要异常。

**Qjava-basics-1441（填空·语法语义）** 实现 AutoCloseable 的资源必须用 ______：编译器按声明逆序自动 close 并保留抑制异常。
**答案：try-with-resources**。解析：手动 close 可能因提前 return/异常被跳过；抑制异常（addSuppressed）保留关闭失败的次要异常。

**Qjava-basics-1442（简答·语法语义）** 请说明「异常」中try-with-resources的机制与使用要点。
**要点（标准答案）**：① 实现 AutoCloseable 的资源必须用 try-with-resources：编译器按声明逆序自动 close 并保留抑制异常。；② 原理：手动 close 可能因提前 return/异常被跳过；抑制异常（addSuppressed）保留关闭失败的次要异常。；③ 使用要点：自定义资源类实现 AutoCloseable 即可享受语法糖。。版本锚点：JDK 7+（JLS 14.20.3）。

**Qjava-basics-1443（单选·正向·语法语义）** 关于「异常」的说法，正确的是？
- A. JDK7+ 支持多类型 catch（catch (A
- B. 多类型 catch 中 e 是隐式 final。
- C. 多类型 catch 的异常类型顺序随意。
- D. 多类型 catch 中 e 可以重新赋值。
**答案：A**
**解析：** JDK7+ 支持多类型 catch（catch (A。原因：B e)），但同族类型必须子类在前否则编译错误。。
**来源：** JB-054 · 异常（JDK 7+（JLS 14.20））

**Qjava-basics-1444（判断·语法语义）** JDK7+ 支持多类型 catch（catch (A
**答案：对。** 解析：B e)），但同族类型必须子类在前否则编译错误。

**Qjava-basics-1445（判断·语法语义）** 多类型 catch 中 e 是隐式 final。
**答案：错。** 正确表述：JDK7+ 支持多类型 catch（catch (A。原因：B e)），但同族类型必须子类在前否则编译错误。

**Qjava-basics-1446（判断·语法语义）** 多类型 catch 中 e 可以重新赋值。
**答案：错。** 正确表述：JDK7+ 支持多类型 catch（catch (A。原因：B e)），但同族类型必须子类在前否则编译错误。

**Qjava-basics-1447（判断·语法语义）** 多类型 catch 的异常类型顺序随意。
**答案：错。** 正确表述：JDK7+ 支持多类型 catch（catch (A。原因：B e)），但同族类型必须子类在前否则编译错误。

**Qjava-basics-1448（场景单选·语法语义）** 在工程实践中关于「多重catch」，下列做法符合推荐实践的是？
- A. 多类型 catch 中 e 是隐式 final。
- B. 多类型 catch 中 e 可以重新赋值。
- C. 多类型 catch 的异常类型顺序随意。
- D. 多类型 catch 是语法糖，反编译后是多个 catch 块。
**答案：D**
**解析：** 推荐实践：多类型 catch 是语法糖，反编译后是多个 catch 块。。事实依据：JDK7+ 支持多类型 catch（catch (A。

**Qjava-basics-1449（场景判断·语法语义）** 推荐实践：多类型 catch 是语法糖，反编译后是多个 catch 块。
**答案：对。** 解析：JDK7+ 支持多类型 catch（catch (A。原因：B e)），但同族类型必须子类在前否则编译错误。

**Qjava-basics-1450（简答·语法语义）** 请说明「异常」中多重catch的机制与使用要点。
**要点（标准答案）**：① JDK7+ 支持多类型 catch（catch (A；② 原理：B e)），但同族类型必须子类在前否则编译错误。；③ 使用要点：多类型 catch 是语法糖，反编译后是多个 catch 块。。版本锚点：JDK 7+（JLS 14.20）。

**Qjava-basics-1451（单选·正向·语法语义）** 关于「final」的说法，正确的是？
- A. final 类的所有方法自动 final 但不必标注。
- B. final 方法可以在子类中重写。
- C. final 修饰类不可继承、修饰方法不可重写、修饰变量不可重新赋值（引用类型指引用不可变，对象内容可变）。
- D. final List 中的元素也不能修改。
**答案：C**
**解析：** final 修饰类不可继承、修饰方法不可重写、修饰变量不可重新赋值（引用类型指引用不可变，对象内容可变）。。原因：final 是约束不是深拷贝：final List 的元素仍可 add。。
**来源：** JB-055 · final（JLS 4.12.4）

**Qjava-basics-1452（判断·语法语义）** final 修饰类不可继承、修饰方法不可重写、修饰变量不可重新赋值（引用类型指引用不可变，对象内容可变）。
**答案：对。** 解析：final 是约束不是深拷贝：final List 的元素仍可 add。

**Qjava-basics-1453（判断·语法语义）** final List 中的元素也不能修改。
**答案：错。** 正确表述：final 修饰类不可继承、修饰方法不可重写、修饰变量不可重新赋值（引用类型指引用不可变，对象内容可变）。。原因：final 是约束不是深拷贝：final List 的元素仍可 add。

**Qjava-basics-1454（判断·语法语义）** final 方法可以在子类中重写。
**答案：错。** 正确表述：final 修饰类不可继承、修饰方法不可重写、修饰变量不可重新赋值（引用类型指引用不可变，对象内容可变）。。原因：final 是约束不是深拷贝：final List 的元素仍可 add。

**Qjava-basics-1455（判断·语法语义）** final 类的所有方法自动 final 但不必标注。
**答案：错。** 正确表述：final 修饰类不可继承、修饰方法不可重写、修饰变量不可重新赋值（引用类型指引用不可变，对象内容可变）。。原因：final 是约束不是深拷贝：final List 的元素仍可 add。

**Qjava-basics-1456（场景单选·语法语义）** 在工程实践中关于「三用途」，下列做法符合推荐实践的是？
- A. final List 中的元素也不能修改。
- B. final 类的所有方法自动 final 但不必标注。
- C. final 方法可以在子类中重写。
- D. final 字段有更强的内存语义（构造器安全发布）。
**答案：D**
**解析：** 推荐实践：final 字段有更强的内存语义（构造器安全发布）。。事实依据：final 修饰类不可继承、修饰方法不可重写、修饰变量不可重新赋值（引用类型指引用不可变，对象内容可变）。。

**Qjava-basics-1457（场景判断·语法语义）** 推荐实践：final 字段有更强的内存语义（构造器安全发布）。
**答案：对。** 解析：final 修饰类不可继承、修饰方法不可重写、修饰变量不可重新赋值（引用类型指引用不可变，对象内容可变）。。原因：final 是约束不是深拷贝：final List 的元素仍可 add。

**Qjava-basics-1458（简答·语法语义）** 请说明「final」中三用途的机制与使用要点。
**要点（标准答案）**：① final 修饰类不可继承、修饰方法不可重写、修饰变量不可重新赋值（引用类型指引用不可变，对象内容可变）。；② 原理：final 是约束不是深拷贝：final List 的元素仍可 add。；③ 使用要点：final 字段有更强的内存语义（构造器安全发布）。。版本锚点：JLS 4.12.4。

**Qjava-basics-1459（单选·正向·内存）** 关于「final」的说法，正确的是？
- A. final 语义只影响编译器不影响运行时。
- B. final 字段写具有"构造器完成即对其他线程可见"的内存语义（无需 synchronized）。
- C. final 字段在构造器中可以二次赋值而不报错。
- D. final 字段的可见性和其他普通字段完全相同。
**答案：B**
**解析：** final 字段写具有"构造器完成即对其他线程可见"的内存语义（无需 synchronized）。。原因：JMM 为 final 专门定义了读写内存屏障规则（JSR-133）。。
**来源：** JB-056 · final（JLS 17.5）

**Qjava-basics-1460（判断·内存）** final 字段写具有"构造器完成即对其他线程可见"的内存语义（无需 synchronized）。
**答案：对。** 解析：JMM 为 final 专门定义了读写内存屏障规则（JSR-133）。

**Qjava-basics-1461（判断·内存）** final 字段的可见性和其他普通字段完全相同。
**答案：错。** 正确表述：final 字段写具有"构造器完成即对其他线程可见"的内存语义（无需 synchronized）。。原因：JMM 为 final 专门定义了读写内存屏障规则（JSR-133）。

**Qjava-basics-1462（判断·内存）** final 字段在构造器中可以二次赋值而不报错。
**答案：错。** 正确表述：final 字段写具有"构造器完成即对其他线程可见"的内存语义（无需 synchronized）。。原因：JMM 为 final 专门定义了读写内存屏障规则（JSR-133）。

**Qjava-basics-1463（判断·内存）** final 语义只影响编译器不影响运行时。
**答案：错。** 正确表述：final 字段写具有"构造器完成即对其他线程可见"的内存语义（无需 synchronized）。。原因：JMM 为 final 专门定义了读写内存屏障规则（JSR-133）。

**Qjava-basics-1464（场景单选·内存）** 在工程实践中关于「安全发布」，下列做法符合推荐实践的是？
- A. final 字段的可见性和其他普通字段完全相同。
- B. final 字段在构造器中可以二次赋值而不报错。
- C. 不可变对象+final 是线程安全设计的基石。
- D. final 语义只影响编译器不影响运行时。
**答案：C**
**解析：** 推荐实践：不可变对象+final 是线程安全设计的基石。。事实依据：final 字段写具有"构造器完成即对其他线程可见"的内存语义（无需 synchronized）。。

**Qjava-basics-1465（场景判断·内存）** 推荐实践：不可变对象+final 是线程安全设计的基石。
**答案：对。** 解析：final 字段写具有"构造器完成即对其他线程可见"的内存语义（无需 synchronized）。。原因：JMM 为 final 专门定义了读写内存屏障规则（JSR-133）。

**Qjava-basics-1466（简答·内存）** 请说明「final」中安全发布的机制与使用要点。
**要点（标准答案）**：① final 字段写具有"构造器完成即对其他线程可见"的内存语义（无需 synchronized）。；② 原理：JMM 为 final 专门定义了读写内存屏障规则（JSR-133）。；③ 使用要点：不可变对象+final 是线程安全设计的基石。。版本锚点：JLS 17.5。

**Qjava-basics-1467（单选·正向·语法语义）** 关于「static」的说法，正确的是？
- A. static 字段的初始化是非线程安全的。
- B. static 字段每次访问类时重新初始化。
- C. static 块在构造器之后执行。
- D. static 字段在类初始化（<clinit>）时按代码顺序赋值，仅执行一次且线程安全（JVM 保证）。
**答案：D**
**解析：** static 字段在类初始化（<clinit>）时按代码顺序赋值，仅执行一次且线程安全（JVM 保证）。。原因：<clinit> 由 JVM 加锁保证单线程执行。。
**来源：** JB-057 · static（JLS 12.4）

**Qjava-basics-1468（判断·语法语义）** static 字段在类初始化（<clinit>）时按代码顺序赋值，仅执行一次且线程安全（JVM 保证）。
**答案：对。** 解析：<clinit> 由 JVM 加锁保证单线程执行。

**Qjava-basics-1469（判断·语法语义）** static 字段每次访问类时重新初始化。
**答案：错。** 正确表述：static 字段在类初始化（<clinit>）时按代码顺序赋值，仅执行一次且线程安全（JVM 保证）。。原因：<clinit> 由 JVM 加锁保证单线程执行。

**Qjava-basics-1470（判断·语法语义）** static 字段的初始化是非线程安全的。
**答案：错。** 正确表述：static 字段在类初始化（<clinit>）时按代码顺序赋值，仅执行一次且线程安全（JVM 保证）。。原因：<clinit> 由 JVM 加锁保证单线程执行。

**Qjava-basics-1471（判断·语法语义）** static 块在构造器之后执行。
**答案：错。** 正确表述：static 字段在类初始化（<clinit>）时按代码顺序赋值，仅执行一次且线程安全（JVM 保证）。。原因：<clinit> 由 JVM 加锁保证单线程执行。

**Qjava-basics-1472（场景单选·语法语义）** 在工程实践中关于「类加载初始化」，下列做法符合推荐实践的是？
- A. 单例的 Holder 模式正是利用 <clinit> 的 JVM 线程安全。
- B. static 字段的初始化是非线程安全的。
- C. static 块在构造器之后执行。
- D. static 字段每次访问类时重新初始化。
**答案：A**
**解析：** 推荐实践：单例的 Holder 模式正是利用 <clinit> 的 JVM 线程安全。。事实依据：static 字段在类初始化（<clinit>）时按代码顺序赋值，仅执行一次且线程安全（JVM 保证）。。

**Qjava-basics-1473（场景判断·语法语义）** 推荐实践：单例的 Holder 模式正是利用 <clinit> 的 JVM 线程安全。
**答案：对。** 解析：static 字段在类初始化（<clinit>）时按代码顺序赋值，仅执行一次且线程安全（JVM 保证）。。原因：<clinit> 由 JVM 加锁保证单线程执行。

**Qjava-basics-1474（简答·语法语义）** 请说明「static」中类加载初始化的机制与使用要点。
**要点（标准答案）**：① static 字段在类初始化（<clinit>）时按代码顺序赋值，仅执行一次且线程安全（JVM 保证）。；② 原理：<clinit> 由 JVM 加锁保证单线程执行。；③ 使用要点：单例的 Holder 模式正是利用 <clinit> 的 JVM 线程安全。。版本锚点：JLS 12.4。

**Qjava-basics-1475（单选·正向·误用）** 关于「static」的说法，正确的是？
- A. static 字段在 GC 中永远不会被回收是正常且无害的。
- B. static 可变字段是线程安全的。
- C. static 字段随对象创建而初始化。
- D. static 可变字段是全局共享状态，多线程并发访问必须自行同步，且影响测试隔离。
**答案：D**
**解析：** static 可变字段是全局共享状态，多线程并发访问必须自行同步，且影响测试隔离。。原因：静态生命周期 = 类加载器生命周期，泄漏风险大。。
**来源：** JB-058 · static（并发设计通用）

**Qjava-basics-1476（判断·误用）** static 可变字段是全局共享状态，多线程并发访问必须自行同步，且影响测试隔离。
**答案：对。** 解析：静态生命周期 = 类加载器生命周期，泄漏风险大。

**Qjava-basics-1477（判断·误用）** static 可变字段是线程安全的。
**答案：错。** 正确表述：static 可变字段是全局共享状态，多线程并发访问必须自行同步，且影响测试隔离。。原因：静态生命周期 = 类加载器生命周期，泄漏风险大。

**Qjava-basics-1478（判断·误用）** static 字段随对象创建而初始化。
**答案：错。** 正确表述：static 可变字段是全局共享状态，多线程并发访问必须自行同步，且影响测试隔离。。原因：静态生命周期 = 类加载器生命周期，泄漏风险大。

**Qjava-basics-1479（判断·误用）** static 字段在 GC 中永远不会被回收是正常且无害的。
**答案：错。** 正确表述：static 可变字段是全局共享状态，多线程并发访问必须自行同步，且影响测试隔离。。原因：静态生命周期 = 类加载器生命周期，泄漏风险大。

**Qjava-basics-1480（场景单选·误用）** 在工程实践中关于「静态可变状态」，下列做法符合推荐实践的是？
- A. static 字段在 GC 中永远不会被回收是正常且无害的。
- B. static 字段随对象创建而初始化。
- C. 阿里手册限制滥用 static 可变变量；静态常量（final）不受限。
- D. static 可变字段是线程安全的。
**答案：C**
**解析：** 推荐实践：阿里手册限制滥用 static 可变变量；静态常量（final）不受限。。事实依据：static 可变字段是全局共享状态，多线程并发访问必须自行同步，且影响测试隔离。。

**Qjava-basics-1481（场景判断·误用）** 推荐实践：阿里手册限制滥用 static 可变变量；静态常量（final）不受限。
**答案：对。** 解析：static 可变字段是全局共享状态，多线程并发访问必须自行同步，且影响测试隔离。。原因：静态生命周期 = 类加载器生命周期，泄漏风险大。

**Qjava-basics-1482（简答·误用）** 请说明「static」中静态可变状态的机制与使用要点。
**要点（标准答案）**：① static 可变字段是全局共享状态，多线程并发访问必须自行同步，且影响测试隔离。；② 原理：静态生命周期 = 类加载器生命周期，泄漏风险大。；③ 使用要点：阿里手册限制滥用 static 可变变量；静态常量（final）不受限。。版本锚点：并发设计通用。

**Qjava-basics-1483（单选·正向·语法语义）** 关于「接口」的说法，正确的是？
- A. 接口实现类初始化永远不会触发任何接口的初始化。
- B. default 方法只能在实现类中调用。
- C. JDK8 起接口可以有 default 方法（有实现体）；实现类初始化时会连带初始化"含 default 方法的"接口。
- D. 接口的 default 方法破坏了接口不能有实现的规则因此被移除过。
**答案：C**
**解析：** JDK8 起接口可以有 default 方法（有实现体）；实现类初始化时会连带初始化"含 default 方法的"接口。。原因：JLS 12.4.1 规定：类初始化时，声明了 default 方法的父接口会被初始化。。
**来源：** JB-059 · 接口（JDK8+）

**Qjava-basics-1484（判断·语法语义）** JDK8 起接口可以有 default 方法（有实现体）；实现类初始化时会连带初始化"含 default 方法的"接口。
**答案：对。** 解析：JLS 12.4.1 规定：类初始化时，声明了 default 方法的父接口会被初始化。

**Qjava-basics-1485（判断·语法语义）** 接口实现类初始化永远不会触发任何接口的初始化。
**答案：错。** 正确表述：JDK8 起接口可以有 default 方法（有实现体）；实现类初始化时会连带初始化"含 default 方法的"接口。。原因：JLS 12.4.1 规定：类初始化时，声明了 default 方法的父接口会被初始化。

**Qjava-basics-1486（判断·语法语义）** default 方法只能在实现类中调用。
**答案：错。** 正确表述：JDK8 起接口可以有 default 方法（有实现体）；实现类初始化时会连带初始化"含 default 方法的"接口。。原因：JLS 12.4.1 规定：类初始化时，声明了 default 方法的父接口会被初始化。

**Qjava-basics-1487（判断·语法语义）** 接口的 default 方法破坏了接口不能有实现的规则因此被移除过。
**答案：错。** 正确表述：JDK8 起接口可以有 default 方法（有实现体）；实现类初始化时会连带初始化"含 default 方法的"接口。。原因：JLS 12.4.1 规定：类初始化时，声明了 default 方法的父接口会被初始化。

**Qjava-basics-1488（场景单选·语法语义）** 在工程实践中关于「default方法」，下列做法符合推荐实践的是？
- A. 接口实现类初始化永远不会触发任何接口的初始化。
- B. 本机实测：new Impl() 打印了含 default 的接口 I 的初始化，不含 default 的 I2 未初始化。
- C. default 方法只能在实现类中调用。
- D. 接口的 default 方法破坏了接口不能有实现的规则因此被移除过。
**答案：B**
**解析：** 推荐实践：本机实测：new Impl() 打印了含 default 的接口 I 的初始化，不含 default 的 I2 未初始化。。事实依据：JDK8 起接口可以有 default 方法（有实现体）；实现类初始化时会连带初始化"含 default 方法的"接口。。

**Qjava-basics-1489（场景判断·语法语义）** 推荐实践：本机实测：new Impl() 打印了含 default 的接口 I 的初始化，不含 default 的 I2 未初始化。
**答案：对。** 解析：JDK8 起接口可以有 default 方法（有实现体）；实现类初始化时会连带初始化"含 default 方法的"接口。。原因：JLS 12.4.1 规定：类初始化时，声明了 default 方法的父接口会被初始化。

**Qjava-basics-1490（填空·语法语义）** JDK8 起接口可以有 ______（有实现体）；实现类初始化时会连带初始化"含 default 方法的"接口。
**答案：default方法**。解析：JLS 12.4.1 规定：类初始化时，声明了 default 方法的父接口会被初始化。

**Qjava-basics-1491（简答·语法语义）** 请说明「接口」中default方法的机制与使用要点。
**要点（标准答案）**：① JDK8 起接口可以有 default 方法（有实现体）；实现类初始化时会连带初始化"含 default 方法的"接口。；② 原理：JLS 12.4.1 规定：类初始化时，声明了 default 方法的父接口会被初始化。；③ 使用要点：本机实测：new Impl() 打印了含 default 的接口 I 的初始化，不含 default 的 I2 未初始化。。版本锚点：JDK8+。

**Qjava-basics-1492（单选·正向·语法语义）** 关于「接口」的说法，正确的是？
- A. 接口字段可以不是 public。
- B. 接口的字段隐式为 public static final，且接口不允许静态初始化块。
- C. 接口可以有静态初始化块。
- D. 接口字段可以在实现类中被重新赋值。
**答案：B**
**解析：** 接口的字段隐式为 public static final，且接口不允许静态初始化块。。原因：接口无法用 <clinit> 控制，字段初始化靠常量表达式或引用其他类的初始化逻辑。。
**来源：** JB-060 · 接口（JLS 12.4.1）

**Qjava-basics-1493（判断·语法语义）** 接口的字段隐式为 public static final，且接口不允许静态初始化块。
**答案：对。** 解析：接口无法用 <clinit> 控制，字段初始化靠常量表达式或引用其他类的初始化逻辑。

**Qjava-basics-1494（判断·语法语义）** 接口可以有静态初始化块。
**答案：错。** 正确表述：接口的字段隐式为 public static final，且接口不允许静态初始化块。。原因：接口无法用 <clinit> 控制，字段初始化靠常量表达式或引用其他类的初始化逻辑。

**Qjava-basics-1495（判断·语法语义）** 接口字段可以不是 public。
**答案：错。** 正确表述：接口的字段隐式为 public static final，且接口不允许静态初始化块。。原因：接口无法用 <clinit> 控制，字段初始化靠常量表达式或引用其他类的初始化逻辑。

**Qjava-basics-1496（判断·语法语义）** 接口字段可以在实现类中被重新赋值。
**答案：错。** 正确表述：接口的字段隐式为 public static final，且接口不允许静态初始化块。。原因：接口无法用 <clinit> 控制，字段初始化靠常量表达式或引用其他类的初始化逻辑。

**Qjava-basics-1497（场景单选·语法语义）** 在工程实践中关于「字段与初始化」，下列做法符合推荐实践的是？
- A. 接口字段可以在实现类中被重新赋值。
- B. 需要复杂初始化逻辑的常量应放到辅助类。
- C. 接口字段可以不是 public。
- D. 接口可以有静态初始化块。
**答案：B**
**解析：** 推荐实践：需要复杂初始化逻辑的常量应放到辅助类。。事实依据：接口的字段隐式为 public static final，且接口不允许静态初始化块。。

**Qjava-basics-1498（场景判断·语法语义）** 推荐实践：需要复杂初始化逻辑的常量应放到辅助类。
**答案：对。** 解析：接口的字段隐式为 public static final，且接口不允许静态初始化块。。原因：接口无法用 <clinit> 控制，字段初始化靠常量表达式或引用其他类的初始化逻辑。

**Qjava-basics-1499（简答·语法语义）** 请说明「接口」中字段与初始化的机制与使用要点。
**要点（标准答案）**：① 接口的字段隐式为 public static final，且接口不允许静态初始化块。；② 原理：接口无法用 <clinit> 控制，字段初始化靠常量表达式或引用其他类的初始化逻辑。；③ 使用要点：需要复杂初始化逻辑的常量应放到辅助类。。版本锚点：JLS 12.4.1。

**Qjava-basics-1500（单选·正向·语法语义）** 关于「内部类」的说法，正确的是？
- A. 静态嵌套类持有外部类实例。
- B. 非静态内部类对象隐式持有外部类实例引用（Outer.this），可能导致外部类无法被 GC。
- C. 内部类导致外部类泄漏是不存在的说法。
- D. 非静态内部类不会引用外部类实例。
**答案：B**
**解析：** 非静态内部类对象隐式持有外部类实例引用（Outer.this），可能导致外部类无法被 GC。。原因：静态嵌套类（static nested class）不持有外部引用。。
**来源：** JB-061 · 内部类（JLS 8.1.3）

**Qjava-basics-1501（判断·语法语义）** 非静态内部类对象隐式持有外部类实例引用（Outer.this），可能导致外部类无法被 GC。
**答案：对。** 解析：静态嵌套类（static nested class）不持有外部引用。

**Qjava-basics-1502（判断·语法语义）** 非静态内部类不会引用外部类实例。
**答案：错。** 正确表述：非静态内部类对象隐式持有外部类实例引用（Outer.this），可能导致外部类无法被 GC。。原因：静态嵌套类（static nested class）不持有外部引用。

**Qjava-basics-1503（判断·语法语义）** 静态嵌套类持有外部类实例。
**答案：错。** 正确表述：非静态内部类对象隐式持有外部类实例引用（Outer.this），可能导致外部类无法被 GC。。原因：静态嵌套类（static nested class）不持有外部引用。

**Qjava-basics-1504（判断·语法语义）** 内部类导致外部类泄漏是不存在的说法。
**答案：错。** 正确表述：非静态内部类对象隐式持有外部类实例引用（Outer.this），可能导致外部类无法被 GC。。原因：静态嵌套类（static nested class）不持有外部引用。

**Qjava-basics-1505（场景单选·语法语义）** 在工程实践中关于「内部类引用」，下列做法符合推荐实践的是？
- A. 非静态内部类不会引用外部类实例。
- B. 静态嵌套类持有外部类实例。
- C. Handler 泄漏（Android）与回调泄漏（Java）都是此机制的产物。
- D. 内部类导致外部类泄漏是不存在的说法。
**答案：C**
**解析：** 推荐实践：Handler 泄漏（Android）与回调泄漏（Java）都是此机制的产物。。事实依据：非静态内部类对象隐式持有外部类实例引用（Outer.this），可能导致外部类无法被 GC。。

**Qjava-basics-1506（场景判断·语法语义）** 推荐实践：Handler 泄漏（Android）与回调泄漏（Java）都是此机制的产物。
**答案：对。** 解析：非静态内部类对象隐式持有外部类实例引用（Outer.this），可能导致外部类无法被 GC。。原因：静态嵌套类（static nested class）不持有外部引用。

**Qjava-basics-1507（简答·语法语义）** 请说明「内部类」中内部类引用的机制与使用要点。
**要点（标准答案）**：① 非静态内部类对象隐式持有外部类实例引用（Outer.this），可能导致外部类无法被 GC。；② 原理：静态嵌套类（static nested class）不持有外部引用。；③ 使用要点：Handler 泄漏（Android）与回调泄漏（Java）都是此机制的产物。。版本锚点：JLS 8.1.3。

**Qjava-basics-1508（单选·正向·语法语义）** 关于「内部类」的说法，正确的是？
- A. static 嵌套类不持有外部实例引用，可独立实例化；语义上更接近"把类组织进外部类的命名空间"。
- B. 所有嵌套类都持有外部类引用。
- C. static 嵌套类不能访问外部类的 static 字段。
- D. static 嵌套类必须依附外部实例才能创建。
**答案：A**
**解析：** static 嵌套类不持有外部实例引用，可独立实例化；语义上更接近"把类组织进外部类的命名空间"。。原因：不需要访问外部实例就应声明为 static——Effective Java 相关条目。。
**来源：** JB-062 · 内部类（JLS 8.1）

**Qjava-basics-1509（判断·语法语义）** static 嵌套类不持有外部实例引用，可独立实例化；语义上更接近"把类组织进外部类的命名空间"。
**答案：对。** 解析：不需要访问外部实例就应声明为 static——Effective Java 相关条目。

**Qjava-basics-1510（判断·语法语义）** 所有嵌套类都持有外部类引用。
**答案：错。** 正确表述：static 嵌套类不持有外部实例引用，可独立实例化；语义上更接近"把类组织进外部类的命名空间"。。原因：不需要访问外部实例就应声明为 static——Effective Java 相关条目。

**Qjava-basics-1511（判断·语法语义）** static 嵌套类必须依附外部实例才能创建。
**答案：错。** 正确表述：static 嵌套类不持有外部实例引用，可独立实例化；语义上更接近"把类组织进外部类的命名空间"。。原因：不需要访问外部实例就应声明为 static——Effective Java 相关条目。

**Qjava-basics-1512（判断·语法语义）** static 嵌套类不能访问外部类的 static 字段。
**答案：错。** 正确表述：static 嵌套类不持有外部实例引用，可独立实例化；语义上更接近"把类组织进外部类的命名空间"。。原因：不需要访问外部实例就应声明为 static——Effective Java 相关条目。

**Qjava-basics-1513（场景单选·语法语义）** 在工程实践中关于「静态嵌套类」，下列做法符合推荐实践的是？
- A. 集合内的 Builder/Node 类几乎都是 static 嵌套类（如 HashMap.Node）。
- B. static 嵌套类必须依附外部实例才能创建。
- C. 所有嵌套类都持有外部类引用。
- D. static 嵌套类不能访问外部类的 static 字段。
**答案：A**
**解析：** 推荐实践：集合内的 Builder/Node 类几乎都是 static 嵌套类（如 HashMap.Node）。。事实依据：static 嵌套类不持有外部实例引用，可独立实例化；语义上更接近"把类组织进外部类的命名空间"。。

**Qjava-basics-1514（场景判断·语法语义）** 推荐实践：集合内的 Builder/Node 类几乎都是 static 嵌套类（如 HashMap.Node）。
**答案：对。** 解析：static 嵌套类不持有外部实例引用，可独立实例化；语义上更接近"把类组织进外部类的命名空间"。。原因：不需要访问外部实例就应声明为 static——Effective Java 相关条目。

**Qjava-basics-1515（简答·语法语义）** 请说明「内部类」中静态嵌套类的机制与使用要点。
**要点（标准答案）**：① static 嵌套类不持有外部实例引用，可独立实例化；语义上更接近"把类组织进外部类的命名空间"。；② 原理：不需要访问外部实例就应声明为 static——Effective Java 相关条目。；③ 使用要点：集合内的 Builder/Node 类几乎都是 static 嵌套类（如 HashMap.Node）。。版本锚点：JLS 8.1。

**Qjava-basics-1516（单选·正向·语法语义）** 关于「语言杂项」的说法，正确的是？
- A. 浮点数（float/double）不能直接用 == 比较相等，应使用误差范围或 BigDecimal。
- B. double 运算是精确的十进制运算。
- C. float 精度比 double 高。
- D. 0.1 + 0.2 在 Java 中精确等于 0.3。
**答案：A**
**解析：** 浮点数（float/double）不能直接用 == 比较相等，应使用误差范围或 BigDecimal。。原因：IEEE754 二进制无法精确表示 0.1 等十进制小数。。
**来源：** JB-063 · 语言杂项（JLS 4.2.3）

**Qjava-basics-1517（判断·语法语义）** 浮点数（float/double）不能直接用 == 比较相等，应使用误差范围或 BigDecimal。
**答案：对。** 解析：IEEE754 二进制无法精确表示 0.1 等十进制小数。

**Qjava-basics-1518（判断·语法语义）** 0.1 + 0.2 在 Java 中精确等于 0.3。
**答案：错。** 正确表述：浮点数（float/double）不能直接用 == 比较相等，应使用误差范围或 BigDecimal。。原因：IEEE754 二进制无法精确表示 0.1 等十进制小数。

**Qjava-basics-1519（判断·语法语义）** double 运算是精确的十进制运算。
**答案：错。** 正确表述：浮点数（float/double）不能直接用 == 比较相等，应使用误差范围或 BigDecimal。。原因：IEEE754 二进制无法精确表示 0.1 等十进制小数。

**Qjava-basics-1520（判断·语法语义）** float 精度比 double 高。
**答案：错。** 正确表述：浮点数（float/double）不能直接用 == 比较相等，应使用误差范围或 BigDecimal。。原因：IEEE754 二进制无法精确表示 0.1 等十进制小数。

**Qjava-basics-1521（场景单选·语法语义）** 在工程实践中关于「浮点比较」，下列做法符合推荐实践的是？
- A. double 运算是精确的十进制运算。
- B. float 精度比 double 高。
- C. 资金计算用 BigDecimal 或长整型分单位；String 构造 BigDecimal 必用（double 构造有精度坑）。
- D. 0.1 + 0.2 在 Java 中精确等于 0.3。
**答案：C**
**解析：** 推荐实践：资金计算用 BigDecimal 或长整型分单位；String 构造 BigDecimal 必用（double 构造有精度坑）。。事实依据：浮点数（float/double）不能直接用 == 比较相等，应使用误差范围或 BigDecimal。。

**Qjava-basics-1522（场景判断·语法语义）** 推荐实践：资金计算用 BigDecimal 或长整型分单位；String 构造 BigDecimal 必用（double 构造有精度坑）。
**答案：对。** 解析：浮点数（float/double）不能直接用 == 比较相等，应使用误差范围或 BigDecimal。。原因：IEEE754 二进制无法精确表示 0.1 等十进制小数。

**Qjava-basics-1523（简答·语法语义）** 请说明「语言杂项」中浮点比较的机制与使用要点。
**要点（标准答案）**：① 浮点数（float/double）不能直接用 == 比较相等，应使用误差范围或 BigDecimal。；② 原理：IEEE754 二进制无法精确表示 0.1 等十进制小数。；③ 使用要点：资金计算用 BigDecimal 或长整型分单位；String 构造 BigDecimal 必用（double 构造有精度坑）。。版本锚点：JLS 4.2.3。

**Qjava-basics-1524（单选·正向·误用）** 关于「语言杂项」的说法，正确的是？
- A. switch 原生支持 byte/short/char/int 及其包装类、枚举（JDK7+）与 String（JDK7+），不支持 long/float/double/boolean。
- B. switch 支持 double 类型。
- C. switch 支持 long 类型。
- D. switch 从 Java 5 就支持 String。
**答案：A**
**解析：** switch 原生支持 byte/short/char/int 及其包装类、枚举（JDK7+）与 String（JDK7+），不支持 long/float/double/boolean。。原因：switch 底层基于 tableswitch/lookupswitch 整数跳转指令。。
**来源：** JB-064 · 语言杂项（JDK 7（String 支持））

**Qjava-basics-1525（判断·误用）** switch 原生支持 byte/short/char/int 及其包装类、枚举（JDK7+）与 String（JDK7+），不支持 long/float/double/boolean。
**答案：对。** 解析：switch 底层基于 tableswitch/lookupswitch 整数跳转指令。

**Qjava-basics-1526（判断·误用）** switch 支持 long 类型。
**答案：错。** 正确表述：switch 原生支持 byte/short/char/int 及其包装类、枚举（JDK7+）与 String（JDK7+），不支持 long/float/double/boolean。。原因：switch 底层基于 tableswitch/lookupswitch 整数跳转指令。

**Qjava-basics-1527（判断·误用）** switch 支持 double 类型。
**答案：错。** 正确表述：switch 原生支持 byte/short/char/int 及其包装类、枚举（JDK7+）与 String（JDK7+），不支持 long/float/double/boolean。。原因：switch 底层基于 tableswitch/lookupswitch 整数跳转指令。

**Qjava-basics-1528（判断·误用）** switch 从 Java 5 就支持 String。
**答案：错。** 正确表述：switch 原生支持 byte/short/char/int 及其包装类、枚举（JDK7+）与 String（JDK7+），不支持 long/float/double/boolean。。原因：switch 底层基于 tableswitch/lookupswitch 整数跳转指令。

**Qjava-basics-1529（场景单选·误用）** 在工程实践中关于「switch类型」，下列做法符合推荐实践的是？
- A. switch 支持 long 类型。
- B. switch 从 Java 5 就支持 String。
- C. JDK14+ 的 switch 表达式（箭头语法）是新的考察点。
- D. switch 支持 double 类型。
**答案：C**
**解析：** 推荐实践：JDK14+ 的 switch 表达式（箭头语法）是新的考察点。。事实依据：switch 原生支持 byte/short/char/int 及其包装类、枚举（JDK7+）与 String（JDK7+），不支持 long/float/double/boolean。。

**Qjava-basics-1530（场景判断·误用）** 推荐实践：JDK14+ 的 switch 表达式（箭头语法）是新的考察点。
**答案：对。** 解析：switch 原生支持 byte/short/char/int 及其包装类、枚举（JDK7+）与 String（JDK7+），不支持 long/float/double/boolean。。原因：switch 底层基于 tableswitch/lookupswitch 整数跳转指令。

**Qjava-basics-1531（简答·误用）** 请说明「语言杂项」中switch类型的机制与使用要点。
**要点（标准答案）**：① switch 原生支持 byte/short/char/int 及其包装类、枚举（JDK7+）与 String（JDK7+），不支持 long/float/double/boolean。；② 原理：switch 底层基于 tableswitch/lookupswitch 整数跳转指令。；③ 使用要点：JDK14+ 的 switch 表达式（箭头语法）是新的考察点。。版本锚点：JDK 7（String 支持）。

**Qjava-basics-1532（单选·正向·语法语义）** 关于「语言杂项」的说法，正确的是？
- A. 一个 char 一定能表示一个汉字之外的所有 Unicode 字符。
- B. char 只能存储英文字母。
- C. char 本质是 16 位无符号 UTF-16 代码单元，可参与整数运算（如 'a'+1 得 'b'）。
- D. char 参与运算的结果还是 char 类型。
**答案：C**
**解析：** char 本质是 16 位无符号 UTF-16 代码单元，可参与整数运算（如 'a'+1 得 'b'）。。原因：char 的算术结果自动提升为 int，赋回 char 需强转。。
**来源：** JB-065 · 语言杂项（JLS 4.2.1）

**Qjava-basics-1533（判断·语法语义）** char 本质是 16 位无符号 UTF-16 代码单元，可参与整数运算（如 'a'+1 得 'b'）。
**答案：对。** 解析：char 的算术结果自动提升为 int，赋回 char 需强转。

**Qjava-basics-1534（判断·语法语义）** char 参与运算的结果还是 char 类型。
**答案：错。** 正确表述：char 本质是 16 位无符号 UTF-16 代码单元，可参与整数运算（如 'a'+1 得 'b'）。。原因：char 的算术结果自动提升为 int，赋回 char 需强转。

**Qjava-basics-1535（判断·语法语义）** char 只能存储英文字母。
**答案：错。** 正确表述：char 本质是 16 位无符号 UTF-16 代码单元，可参与整数运算（如 'a'+1 得 'b'）。。原因：char 的算术结果自动提升为 int，赋回 char 需强转。

**Qjava-basics-1536（判断·语法语义）** 一个 char 一定能表示一个汉字之外的所有 Unicode 字符。
**答案：错。** 正确表述：char 本质是 16 位无符号 UTF-16 代码单元，可参与整数运算（如 'a'+1 得 'b'）。。原因：char 的算术结果自动提升为 int，赋回 char 需强转。

**Qjava-basics-1537（场景单选·语法语义）** 在工程实践中关于「char运算」，下列做法符合推荐实践的是？
- A. char 参与运算的结果还是 char 类型。
- B. char 只能存储英文字母。
- C. 一个 char 一定能表示一个汉字之外的所有 Unicode 字符。
- D. 增补平面字符（如 emoji）需要代理对（两个 char），length() 会返回 2。
**答案：D**
**解析：** 推荐实践：增补平面字符（如 emoji）需要代理对（两个 char），length() 会返回 2。。事实依据：char 本质是 16 位无符号 UTF-16 代码单元，可参与整数运算（如 'a'+1 得 'b'）。。

**Qjava-basics-1538（场景判断·语法语义）** 推荐实践：增补平面字符（如 emoji）需要代理对（两个 char），length() 会返回 2。
**答案：对。** 解析：char 本质是 16 位无符号 UTF-16 代码单元，可参与整数运算（如 'a'+1 得 'b'）。。原因：char 的算术结果自动提升为 int，赋回 char 需强转。

**Qjava-basics-1539（简答·语法语义）** 请说明「语言杂项」中char运算的机制与使用要点。
**要点（标准答案）**：① char 本质是 16 位无符号 UTF-16 代码单元，可参与整数运算（如 'a'+1 得 'b'）。；② 原理：char 的算术结果自动提升为 int，赋回 char 需强转。；③ 使用要点：增补平面字符（如 emoji）需要代理对（两个 char），length() 会返回 2。。版本锚点：JLS 4.2.1。

**Qjava-basics-1540（单选·正向·语法语义）** 关于「语言杂项」的说法，正确的是？
- A. int 溢出会抛 ArithmeticException。
- B. int 溢出会自动提升为 long。
- C. int 溢出不抛异常而是静默回绕（wrap around），必须用 Math.addExact 或 Math.multiplyExact 显式检测。
- D. 溢出后的结果仍然符合数学直觉。
**答案：C**
**解析：** int 溢出不抛异常而是静默回绕（wrap around），必须用 Math.addExact 或 Math.multiplyExact 显式检测。。原因：二进制补码运算天然回绕，硬件层面不报错。。
**来源：** JB-066 · 语言杂项（JLS 4.2.2）

**Qjava-basics-1541（判断·语法语义）** int 溢出不抛异常而是静默回绕（wrap around），必须用 Math.addExact 或 Math.multiplyExact 显式检测。
**答案：对。** 解析：二进制补码运算天然回绕，硬件层面不报错。

**Qjava-basics-1542（判断·语法语义）** int 溢出会抛 ArithmeticException。
**答案：错。** 正确表述：int 溢出不抛异常而是静默回绕（wrap around），必须用 Math.addExact 或 Math.multiplyExact 显式检测。。原因：二进制补码运算天然回绕，硬件层面不报错。

**Qjava-basics-1543（判断·语法语义）** int 溢出会自动提升为 long。
**答案：错。** 正确表述：int 溢出不抛异常而是静默回绕（wrap around），必须用 Math.addExact 或 Math.multiplyExact 显式检测。。原因：二进制补码运算天然回绕，硬件层面不报错。

**Qjava-basics-1544（判断·语法语义）** 溢出后的结果仍然符合数学直觉。
**答案：错。** 正确表述：int 溢出不抛异常而是静默回绕（wrap around），必须用 Math.addExact 或 Math.multiplyExact 显式检测。。原因：二进制补码运算天然回绕，硬件层面不报错。

**Qjava-basics-1545（场景单选·语法语义）** 在工程实践中关于「整数溢出」，下列做法符合推荐实践的是？
- A. int 溢出会自动提升为 long。
- B. 溢出后的结果仍然符合数学直觉。
- C. Math.addExact 溢出抛 ArithmeticException——金融计算必用。
- D. int 溢出会抛 ArithmeticException。
**答案：C**
**解析：** 推荐实践：Math.addExact 溢出抛 ArithmeticException——金融计算必用。。事实依据：int 溢出不抛异常而是静默回绕（wrap around），必须用 Math.addExact 或 Math.multiplyExact 显式检测。。

**Qjava-basics-1546（场景判断·语法语义）** 推荐实践：Math.addExact 溢出抛 ArithmeticException——金融计算必用。
**答案：对。** 解析：int 溢出不抛异常而是静默回绕（wrap around），必须用 Math.addExact 或 Math.multiplyExact 显式检测。。原因：二进制补码运算天然回绕，硬件层面不报错。

**Qjava-basics-1547（简答·语法语义）** 请说明「语言杂项」中整数溢出的机制与使用要点。
**要点（标准答案）**：① int 溢出不抛异常而是静默回绕（wrap around），必须用 Math.addExact 或 Math.multiplyExact 显式检测。；② 原理：二进制补码运算天然回绕，硬件层面不报错。；③ 使用要点：Math.addExact 溢出抛 ArithmeticException——金融计算必用。。版本锚点：JLS 4.2.2。

**Qjava-basics-1548（单选·正向·版本）** 关于「语言杂项」的说法，正确的是？
- A. JDK9 引入模块系统（JPMS）：module-info.java 声明依赖与导出，JDK 内部 API（如 sun.misc.Unsafe 部分）被强封装。
- B. module-info.java 是可选的注解文件。
- C. JDK9 对内部 API 没有任何封装变化。
- D. JPMS 强制所有类库都必须模块化。
**答案：A**
**解析：** JDK9 引入模块系统（JPMS）：module-info.java 声明依赖与导出，JDK 内部 API（如 sun.misc.Unsafe 部分）被强封装。。原因：强封装破坏了直接依赖 JDK 内部 API 的老代码——升级 JDK 的最大阻力源。。
**来源：** JB-067 · 语言杂项（JDK9+）

**Qjava-basics-1549（判断·版本）** JDK9 引入模块系统（JPMS）：module-info.java 声明依赖与导出，JDK 内部 API（如 sun.misc.Unsafe 部分）被强封装。
**答案：对。** 解析：强封装破坏了直接依赖 JDK 内部 API 的老代码——升级 JDK 的最大阻力源。

**Qjava-basics-1550（判断·版本）** JDK9 对内部 API 没有任何封装变化。
**答案：错。** 正确表述：JDK9 引入模块系统（JPMS）：module-info.java 声明依赖与导出，JDK 内部 API（如 sun.misc.Unsafe 部分）被强封装。。原因：强封装破坏了直接依赖 JDK 内部 API 的老代码——升级 JDK 的最大阻力源。

**Qjava-basics-1551（判断·版本）** JPMS 强制所有类库都必须模块化。
**答案：错。** 正确表述：JDK9 引入模块系统（JPMS）：module-info.java 声明依赖与导出，JDK 内部 API（如 sun.misc.Unsafe 部分）被强封装。。原因：强封装破坏了直接依赖 JDK 内部 API 的老代码——升级 JDK 的最大阻力源。

**Qjava-basics-1552（判断·版本）** module-info.java 是可选的注解文件。
**答案：错。** 正确表述：JDK9 引入模块系统（JPMS）：module-info.java 声明依赖与导出，JDK 内部 API（如 sun.misc.Unsafe 部分）被强封装。。原因：强封装破坏了直接依赖 JDK 内部 API 的老代码——升级 JDK 的最大阻力源。

**Qjava-basics-1553（场景单选·版本）** 在工程实践中关于「自动模块化」，下列做法符合推荐实践的是？
- A. module-info.java 是可选的注解文件。
- B. JPMS 强制所有类库都必须模块化。
- C. JDK9 对内部 API 没有任何封装变化。
- D. 升级 JDK 的两大障碍：内部 API 封装与废弃 API 清理。
**答案：D**
**解析：** 推荐实践：升级 JDK 的两大障碍：内部 API 封装与废弃 API 清理。。事实依据：JDK9 引入模块系统（JPMS）：module-info.java 声明依赖与导出，JDK 内部 API（如 sun.misc.Unsafe 部分）被强封装。。

**Qjava-basics-1554（场景判断·版本）** 推荐实践：升级 JDK 的两大障碍：内部 API 封装与废弃 API 清理。
**答案：对。** 解析：JDK9 引入模块系统（JPMS）：module-info.java 声明依赖与导出，JDK 内部 API（如 sun.misc.Unsafe 部分）被强封装。。原因：强封装破坏了直接依赖 JDK 内部 API 的老代码——升级 JDK 的最大阻力源。

**Qjava-basics-1555（简答·版本）** 请说明「语言杂项」中自动模块化的机制与使用要点。
**要点（标准答案）**：① JDK9 引入模块系统（JPMS）：module-info.java 声明依赖与导出，JDK 内部 API（如 sun.misc.Unsafe 部分）被强封装。；② 原理：强封装破坏了直接依赖 JDK 内部 API 的老代码——升级 JDK 的最大阻力源。；③ 使用要点：升级 JDK 的两大障碍：内部 API 封装与废弃 API 清理。。版本锚点：JDK9+。

**Qjava-basics-1556（单选·正向·版本）** 关于「语言杂项」的说法，正确的是？
- A. JDK16 转正 record 类：不可变数据载体，自动生成构造器/访问器/equals/hashCode/toString。
- B. record 可以继承其他类。
- C. record 可以有可变字段。
- D. record 需要手写 equals 和 hashCode。
**答案：A**
**解析：** JDK16 转正 record 类：不可变数据载体，自动生成构造器/访问器/equals/hashCode/toString。。原因：record 明确表达"这是纯数据"，字段 final、不能继承其他类（可实现接口）。。
**来源：** JB-068 · 语言杂项（JDK16+）

**Qjava-basics-1557（判断·版本）** JDK16 转正 record 类：不可变数据载体，自动生成构造器/访问器/equals/hashCode/toString。
**答案：对。** 解析：record 明确表达"这是纯数据"，字段 final、不能继承其他类（可实现接口）。

**Qjava-basics-1558（判断·版本）** record 可以有可变字段。
**答案：错。** 正确表述：JDK16 转正 record 类：不可变数据载体，自动生成构造器/访问器/equals/hashCode/toString。。原因：record 明确表达"这是纯数据"，字段 final、不能继承其他类（可实现接口）。

**Qjava-basics-1559（判断·版本）** record 可以继承其他类。
**答案：错。** 正确表述：JDK16 转正 record 类：不可变数据载体，自动生成构造器/访问器/equals/hashCode/toString。。原因：record 明确表达"这是纯数据"，字段 final、不能继承其他类（可实现接口）。

**Qjava-basics-1560（判断·版本）** record 需要手写 equals 和 hashCode。
**答案：错。** 正确表述：JDK16 转正 record 类：不可变数据载体，自动生成构造器/访问器/equals/hashCode/toString。。原因：record 明确表达"这是纯数据"，字段 final、不能继承其他类（可实现接口）。

**Qjava-basics-1561（场景单选·版本）** 在工程实践中关于「record类」，下列做法符合推荐实践的是？
- A. record 需要手写 equals 和 hashCode。
- B. record 可以有可变字段。
- C. DTO/值对象/配置项是 record 的标准使用场景。
- D. record 可以继承其他类。
**答案：C**
**解析：** 推荐实践：DTO/值对象/配置项是 record 的标准使用场景。。事实依据：JDK16 转正 record 类：不可变数据载体，自动生成构造器/访问器/equals/hashCode/toString。。

**Qjava-basics-1562（场景判断·版本）** 推荐实践：DTO/值对象/配置项是 record 的标准使用场景。
**答案：对。** 解析：JDK16 转正 record 类：不可变数据载体，自动生成构造器/访问器/equals/hashCode/toString。。原因：record 明确表达"这是纯数据"，字段 final、不能继承其他类（可实现接口）。

**Qjava-basics-1563（填空·版本）** JDK16 转正 ______：不可变数据载体，自动生成构造器/访问器/equals/hashCode/toString。
**答案：record类**。解析：record 明确表达"这是纯数据"，字段 final、不能继承其他类（可实现接口）。

**Qjava-basics-1564（简答·版本）** 请说明「语言杂项」中record类的机制与使用要点。
**要点（标准答案）**：① JDK16 转正 record 类：不可变数据载体，自动生成构造器/访问器/equals/hashCode/toString。；② 原理：record 明确表达"这是纯数据"，字段 final、不能继承其他类（可实现接口）。；③ 使用要点：DTO/值对象/配置项是 record 的标准使用场景。。版本锚点：JDK16+。

**Qjava-basics-1565（单选·正向·版本）** 关于「语言杂项」的说法，正确的是？
- A. sealed 的子类也不能再被继承是强制规则。
- B. JDK17 转正 sealed 类：用 permits 显式限定继承层级，配合 switch 模式匹配做穷尽检查。
- C. sealed 与模式匹配无关。
- D. sealed 类允许任何类继承它。
**答案：B**
**解析：** JDK17 转正 sealed 类：用 permits 显式限定继承层级，配合 switch 模式匹配做穷尽检查。。原因：编译器检查 switch 是否覆盖所有允许的子类型，漏分支直接编译错。。
**来源：** JB-069 · 语言杂项（JDK17+）

**Qjava-basics-1566（判断·版本）** JDK17 转正 sealed 类：用 permits 显式限定继承层级，配合 switch 模式匹配做穷尽检查。
**答案：对。** 解析：编译器检查 switch 是否覆盖所有允许的子类型，漏分支直接编译错。

**Qjava-basics-1567（判断·版本）** sealed 类允许任何类继承它。
**答案：错。** 正确表述：JDK17 转正 sealed 类：用 permits 显式限定继承层级，配合 switch 模式匹配做穷尽检查。。原因：编译器检查 switch 是否覆盖所有允许的子类型，漏分支直接编译错。

**Qjava-basics-1568（判断·版本）** sealed 与模式匹配无关。
**答案：错。** 正确表述：JDK17 转正 sealed 类：用 permits 显式限定继承层级，配合 switch 模式匹配做穷尽检查。。原因：编译器检查 switch 是否覆盖所有允许的子类型，漏分支直接编译错。

**Qjava-basics-1569（判断·版本）** sealed 的子类也不能再被继承是强制规则。
**答案：错。** 正确表述：JDK17 转正 sealed 类：用 permits 显式限定继承层级，配合 switch 模式匹配做穷尽检查。。原因：编译器检查 switch 是否覆盖所有允许的子类型，漏分支直接编译错。

**Qjava-basics-1570（场景单选·版本）** 在工程实践中关于「sealed类」，下列做法符合推荐实践的是？
- A. sealed 类允许任何类继承它。
- B. sealed 的子类也不能再被继承是强制规则。
- C. sealed 与模式匹配无关。
- D. 状态机/权限模型/AST 节点设计是典型场景。
**答案：D**
**解析：** 推荐实践：状态机/权限模型/AST 节点设计是典型场景。。事实依据：JDK17 转正 sealed 类：用 permits 显式限定继承层级，配合 switch 模式匹配做穷尽检查。。

**Qjava-basics-1571（场景判断·版本）** 推荐实践：状态机/权限模型/AST 节点设计是典型场景。
**答案：对。** 解析：JDK17 转正 sealed 类：用 permits 显式限定继承层级，配合 switch 模式匹配做穷尽检查。。原因：编译器检查 switch 是否覆盖所有允许的子类型，漏分支直接编译错。

**Qjava-basics-1572（填空·版本）** JDK17 转正 ______：用 permits 显式限定继承层级，配合 switch 模式匹配做穷尽检查。
**答案：sealed类**。解析：编译器检查 switch 是否覆盖所有允许的子类型，漏分支直接编译错。

**Qjava-basics-1573（简答·版本）** 请说明「语言杂项」中sealed类的机制与使用要点。
**要点（标准答案）**：① JDK17 转正 sealed 类：用 permits 显式限定继承层级，配合 switch 模式匹配做穷尽检查。；② 原理：编译器检查 switch 是否覆盖所有允许的子类型，漏分支直接编译错。；③ 使用要点：状态机/权限模型/AST 节点设计是典型场景。。版本锚点：JDK17+。

**Qjava-basics-1574（单选·正向·语法语义）** 关于「Object」的说法，正确的是？
- A. Object.clone 默认就是深拷贝。
- B. 实现 Cloneable 接口后 clone 会自动变深拷贝。
- C. 拷贝构造器比 clone 更脆弱。
- D. Object.clone 是浅拷贝（引用字段复制引用），深拷贝需重写 clone 递归复制或改用拷贝构造器/序列化。
**答案：D**
**解析：** Object.clone 是浅拷贝（引用字段复制引用），深拷贝需重写 clone 递归复制或改用拷贝构造器/序列化。。原因：Cloneable 是空标记接口且 clone 语义脆弱，Effective Java 建议用拷贝构造器替代。。
**来源：** JB-070 · Object（Object.clone javadoc / Effective Java）

**Qjava-basics-1575（判断·语法语义）** Object.clone 是浅拷贝（引用字段复制引用），深拷贝需重写 clone 递归复制或改用拷贝构造器/序列化。
**答案：对。** 解析：Cloneable 是空标记接口且 clone 语义脆弱，Effective Java 建议用拷贝构造器替代。

**Qjava-basics-1576（判断·语法语义）** Object.clone 默认就是深拷贝。
**答案：错。** 正确表述：Object.clone 是浅拷贝（引用字段复制引用），深拷贝需重写 clone 递归复制或改用拷贝构造器/序列化。。原因：Cloneable 是空标记接口且 clone 语义脆弱，Effective Java 建议用拷贝构造器替代。

**Qjava-basics-1577（判断·语法语义）** 实现 Cloneable 接口后 clone 会自动变深拷贝。
**答案：错。** 正确表述：Object.clone 是浅拷贝（引用字段复制引用），深拷贝需重写 clone 递归复制或改用拷贝构造器/序列化。。原因：Cloneable 是空标记接口且 clone 语义脆弱，Effective Java 建议用拷贝构造器替代。

**Qjava-basics-1578（判断·语法语义）** 拷贝构造器比 clone 更脆弱。
**答案：错。** 正确表述：Object.clone 是浅拷贝（引用字段复制引用），深拷贝需重写 clone 递归复制或改用拷贝构造器/序列化。。原因：Cloneable 是空标记接口且 clone 语义脆弱，Effective Java 建议用拷贝构造器替代。

**Qjava-basics-1579（场景单选·语法语义）** 在工程实践中关于「clone陷阱」，下列做法符合推荐实践的是？
- A. 拷贝构造器比 clone 更脆弱。
- B. Object.clone 默认就是深拷贝。
- C. 实现 Cloneable 接口后 clone 会自动变深拷贝。
- D. 防御性拷贝优先用拷贝构造器，避免暴露可变内部状态。
**答案：D**
**解析：** 推荐实践：防御性拷贝优先用拷贝构造器，避免暴露可变内部状态。。事实依据：Object.clone 是浅拷贝（引用字段复制引用），深拷贝需重写 clone 递归复制或改用拷贝构造器/序列化。。

**Qjava-basics-1580（场景判断·语法语义）** 推荐实践：防御性拷贝优先用拷贝构造器，避免暴露可变内部状态。
**答案：对。** 解析：Object.clone 是浅拷贝（引用字段复制引用），深拷贝需重写 clone 递归复制或改用拷贝构造器/序列化。。原因：Cloneable 是空标记接口且 clone 语义脆弱，Effective Java 建议用拷贝构造器替代。

**Qjava-basics-1581（简答·语法语义）** 请说明「Object」中clone陷阱的机制与使用要点。
**要点（标准答案）**：① Object.clone 是浅拷贝（引用字段复制引用），深拷贝需重写 clone 递归复制或改用拷贝构造器/序列化。；② 原理：Cloneable 是空标记接口且 clone 语义脆弱，Effective Java 建议用拷贝构造器替代。；③ 使用要点：防御性拷贝优先用拷贝构造器，避免暴露可变内部状态。。版本锚点：Object.clone javadoc / Effective Java。

**Qjava-basics-1582（单选·正向·语法语义）** 关于「Object」的说法，正确的是？
- A. finalize 会在对象不可达后立即执行。
- B. finalize 是可靠的资源清理手段。
- C. finalize 被 GC 最多调用两次。
- D. finalize 在 JDK9 标记废弃、JDK18 进一步降级，资源清理应使用 try-with-resources 或 Cleaner。
**答案：D**
**解析：** finalize 在 JDK9 标记废弃、JDK18 进一步降级，资源清理应使用 try-with-resources 或 Cleaner。。原因：finalize 执行时机不定、可能永不执行、且影响 GC 性能。。
**来源：** JB-071 · Object（JDK9+/JDK18+）

**Qjava-basics-1583（判断·语法语义）** finalize 在 JDK9 标记废弃、JDK18 进一步降级，资源清理应使用 try-with-resources 或 Cleaner。
**答案：对。** 解析：finalize 执行时机不定、可能永不执行、且影响 GC 性能。

**Qjava-basics-1584（判断·语法语义）** finalize 是可靠的资源清理手段。
**答案：错。** 正确表述：finalize 在 JDK9 标记废弃、JDK18 进一步降级，资源清理应使用 try-with-resources 或 Cleaner。。原因：finalize 执行时机不定、可能永不执行、且影响 GC 性能。

**Qjava-basics-1585（判断·语法语义）** finalize 会在对象不可达后立即执行。
**答案：错。** 正确表述：finalize 在 JDK9 标记废弃、JDK18 进一步降级，资源清理应使用 try-with-resources 或 Cleaner。。原因：finalize 执行时机不定、可能永不执行、且影响 GC 性能。

**Qjava-basics-1586（判断·语法语义）** finalize 被 GC 最多调用两次。
**答案：错。** 正确表述：finalize 在 JDK9 标记废弃、JDK18 进一步降级，资源清理应使用 try-with-resources 或 Cleaner。。原因：finalize 执行时机不定、可能永不执行、且影响 GC 性能。

**Qjava-basics-1587（场景单选·语法语义）** 在工程实践中关于「finalize废弃」，下列做法符合推荐实践的是？
- A. finalize 会在对象不可达后立即执行。
- B. finalize 被 GC 最多调用两次。
- C. finalize 是可靠的资源清理手段。
- D. Cleaner 也是"尽力而为"，显式关闭（AutoCloseable）才是正解。
**答案：D**
**解析：** 推荐实践：Cleaner 也是"尽力而为"，显式关闭（AutoCloseable）才是正解。。事实依据：finalize 在 JDK9 标记废弃、JDK18 进一步降级，资源清理应使用 try-with-resources 或 Cleaner。。

**Qjava-basics-1588（场景判断·语法语义）** 推荐实践：Cleaner 也是"尽力而为"，显式关闭（AutoCloseable）才是正解。
**答案：对。** 解析：finalize 在 JDK9 标记废弃、JDK18 进一步降级，资源清理应使用 try-with-resources 或 Cleaner。。原因：finalize 执行时机不定、可能永不执行、且影响 GC 性能。

**Qjava-basics-1589（简答·语法语义）** 请说明「Object」中finalize废弃的机制与使用要点。
**要点（标准答案）**：① finalize 在 JDK9 标记废弃、JDK18 进一步降级，资源清理应使用 try-with-resources 或 Cleaner。；② 原理：finalize 执行时机不定、可能永不执行、且影响 GC 性能。；③ 使用要点：Cleaner 也是"尽力而为"，显式关闭（AutoCloseable）才是正解。。版本锚点：JDK9+/JDK18+。

**Qjava-basics-1590（单选·正向·语法语义）** 关于「Object」的说法，正确的是？
- A. wait 可以在任意位置调用。
- B. wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。
- C. notify 会立即释放锁。
- D. wait/notify 定义在 Thread 类中。
**答案：B**
**解析：** wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。。原因：wait 释放锁进入等待集，notify/notifyAll 唤醒等待线程重新竞争锁。。
**来源：** JB-072 · Object（JLS 17.2）

**Qjava-basics-1591（判断·语法语义）** wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。
**答案：对。** 解析：wait 释放锁进入等待集，notify/notifyAll 唤醒等待线程重新竞争锁。

**Qjava-basics-1592（判断·语法语义）** wait 可以在任意位置调用。
**答案：错。** 正确表述：wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。。原因：wait 释放锁进入等待集，notify/notifyAll 唤醒等待线程重新竞争锁。

**Qjava-basics-1593（判断·语法语义）** notify 会立即释放锁。
**答案：错。** 正确表述：wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。。原因：wait 释放锁进入等待集，notify/notifyAll 唤醒等待线程重新竞争锁。

**Qjava-basics-1594（判断·语法语义）** wait/notify 定义在 Thread 类中。
**答案：错。** 正确表述：wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。。原因：wait 释放锁进入等待集，notify/notifyAll 唤醒等待线程重新竞争锁。

**Qjava-basics-1595（场景单选·语法语义）** 在工程实践中关于「wait与notify」，下列做法符合推荐实践的是？
- A. notify 会立即释放锁。
- B. notify 在锁释放前不生效（锁释放后等待线程才真正被唤醒）。
- C. wait/notify 定义在 Thread 类中。
- D. wait 可以在任意位置调用。
**答案：B**
**解析：** 推荐实践：notify 在锁释放前不生效（锁释放后等待线程才真正被唤醒）。。事实依据：wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。。

**Qjava-basics-1596（场景判断·语法语义）** 推荐实践：notify 在锁释放前不生效（锁释放后等待线程才真正被唤醒）。
**答案：对。** 解析：wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。。原因：wait 释放锁进入等待集，notify/notifyAll 唤醒等待线程重新竞争锁。

**Qjava-basics-1597（简答·语法语义）** 请说明「Object」中wait与notify的机制与使用要点。
**要点（标准答案）**：① wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。；② 原理：wait 释放锁进入等待集，notify/notifyAll 唤醒等待线程重新竞争锁。；③ 使用要点：notify 在锁释放前不生效（锁释放后等待线程才真正被唤醒）。。版本锚点：JLS 17.2。

**Qjava-basics-1598（单选·正向·误用）** 关于「Object」的说法，正确的是？
- A. 等待条件必须用 while 循环判断而非 if：被唤醒后条件可能已被其他线程改变。
- B. 虚假唤醒在 Java 中不存在所以 if 是安全的。
- C. notifyAll 只唤醒一个线程。
- D. if 判条件与 while 完全等价。
**答案：A**
**解析：** 等待条件必须用 while 循环判断而非 if：被唤醒后条件可能已被其他线程改变。。原因：notifyAll 会唤醒所有等待线程，先到者可能改变条件。。
**来源：** JB-073 · Object（JLS 17.2.3）

**Qjava-basics-1599（判断·误用）** 等待条件必须用 while 循环判断而非 if：被唤醒后条件可能已被其他线程改变。
**答案：对。** 解析：notifyAll 会唤醒所有等待线程，先到者可能改变条件。

**Qjava-basics-1600（判断·误用）** if 判条件与 while 完全等价。
**答案：错。** 正确表述：等待条件必须用 while 循环判断而非 if：被唤醒后条件可能已被其他线程改变。。原因：notifyAll 会唤醒所有等待线程，先到者可能改变条件。

**Qjava-basics-1601（判断·误用）** 虚假唤醒在 Java 中不存在所以 if 是安全的。
**答案：错。** 正确表述：等待条件必须用 while 循环判断而非 if：被唤醒后条件可能已被其他线程改变。。原因：notifyAll 会唤醒所有等待线程，先到者可能改变条件。

**Qjava-basics-1602（判断·误用）** notifyAll 只唤醒一个线程。
**答案：错。** 正确表述：等待条件必须用 while 循环判断而非 if：被唤醒后条件可能已被其他线程改变。。原因：notifyAll 会唤醒所有等待线程，先到者可能改变条件。

**Qjava-basics-1603（场景单选·误用）** 在工程实践中关于「虚假唤醒」，下列做法符合推荐实践的是？
- A. if 判条件与 while 完全等价。
- B. 虚假唤醒在 Java 中不存在所以 if 是安全的。
- C. "手写生产者消费者"笔试题的核心考点就是 while+notifyAll。
- D. notifyAll 只唤醒一个线程。
**答案：C**
**解析：** 推荐实践："手写生产者消费者"笔试题的核心考点就是 while+notifyAll。。事实依据：等待条件必须用 while 循环判断而非 if：被唤醒后条件可能已被其他线程改变。。

**Qjava-basics-1604（场景判断·误用）** 推荐实践："手写生产者消费者"笔试题的核心考点就是 while+notifyAll。
**答案：对。** 解析：等待条件必须用 while 循环判断而非 if：被唤醒后条件可能已被其他线程改变。。原因：notifyAll 会唤醒所有等待线程，先到者可能改变条件。

**Qjava-basics-1605（简答·误用）** 请说明「Object」中虚假唤醒的机制与使用要点。
**要点（标准答案）**：① 等待条件必须用 while 循环判断而非 if：被唤醒后条件可能已被其他线程改变。；② 原理：notifyAll 会唤醒所有等待线程，先到者可能改变条件。；③ 使用要点："手写生产者消费者"笔试题的核心考点就是 while+notifyAll。。版本锚点：JLS 17.2.3。

**Qjava-basics-1606（单选·正向·语法语义）** 关于「语言杂项」的说法，正确的是？
- A. String 的 switch 从 Java 5 就支持。
- B. String switch 的性能与 if-else 链完全相同。
- C. switch 对 String 从 JDK7 起支持，底层编译为 hashCode 分两次跳转（先 hash 后 equals 防冲突）。
- D. String 的 switch 只依赖 equals 不依赖 hashCode。
**答案：C**
**解析：** switch 对 String 从 JDK7 起支持，底层编译为 hashCode 分两次跳转（先 hash 后 equals 防冲突）。。原因：String 的 switch 不是语法糖直接变 if-else，而是 hash 跳转+equals 校验。。
**来源：** JB-074 · 语言杂项（JDK7+）

**Qjava-basics-1607（判断·语法语义）** switch 对 String 从 JDK7 起支持，底层编译为 hashCode 分两次跳转（先 hash 后 equals 防冲突）。
**答案：对。** 解析：String 的 switch 不是语法糖直接变 if-else，而是 hash 跳转+equals 校验。

**Qjava-basics-1608（判断·语法语义）** String 的 switch 从 Java 5 就支持。
**答案：错。** 正确表述：switch 对 String 从 JDK7 起支持，底层编译为 hashCode 分两次跳转（先 hash 后 equals 防冲突）。。原因：String 的 switch 不是语法糖直接变 if-else，而是 hash 跳转+equals 校验。

**Qjava-basics-1609（判断·语法语义）** String 的 switch 只依赖 equals 不依赖 hashCode。
**答案：错。** 正确表述：switch 对 String 从 JDK7 起支持，底层编译为 hashCode 分两次跳转（先 hash 后 equals 防冲突）。。原因：String 的 switch 不是语法糖直接变 if-else，而是 hash 跳转+equals 校验。

**Qjava-basics-1610（判断·语法语义）** String switch 的性能与 if-else 链完全相同。
**答案：错。** 正确表述：switch 对 String 从 JDK7 起支持，底层编译为 hashCode 分两次跳转（先 hash 后 equals 防冲突）。。原因：String 的 switch 不是语法糖直接变 if-else，而是 hash 跳转+equals 校验。

**Qjava-basics-1611（场景单选·语法语义）** 在工程实践中关于「字符串switch」，下列做法符合推荐实践的是？
- A. String switch 的性能与 if-else 链完全相同。
- B. String 的 switch 只依赖 equals 不依赖 hashCode。
- C. hashCode 相同的字符串会走 equals 校验分支。
- D. String 的 switch 从 Java 5 就支持。
**答案：C**
**解析：** 推荐实践：hashCode 相同的字符串会走 equals 校验分支。。事实依据：switch 对 String 从 JDK7 起支持，底层编译为 hashCode 分两次跳转（先 hash 后 equals 防冲突）。。

**Qjava-basics-1612（场景判断·语法语义）** 推荐实践：hashCode 相同的字符串会走 equals 校验分支。
**答案：对。** 解析：switch 对 String 从 JDK7 起支持，底层编译为 hashCode 分两次跳转（先 hash 后 equals 防冲突）。。原因：String 的 switch 不是语法糖直接变 if-else，而是 hash 跳转+equals 校验。

**Qjava-basics-1613（简答·语法语义）** 请说明「语言杂项」中字符串switch的机制与使用要点。
**要点（标准答案）**：① switch 对 String 从 JDK7 起支持，底层编译为 hashCode 分两次跳转（先 hash 后 equals 防冲突）。；② 原理：String 的 switch 不是语法糖直接变 if-else，而是 hash 跳转+equals 校验。；③ 使用要点：hashCode 相同的字符串会走 equals 校验分支。。版本锚点：JDK7+。

**Qjava-basics-1614（单选·正向·误用）** 关于「语言杂项」的说法，正确的是？
- A. SimpleDateFormat 的错误只影响解析不影响格式化。
- B. SimpleDateFormat 是线程安全的。
- C. SimpleDateFormat 非线程安全（内部 Calendar 共享），多线程共享实例会产生数据错乱。
- D. SimpleDateFormat 线程不安全的问题在 JDK 新版已被修复。
**答案：C**
**解析：** SimpleDateFormat 非线程安全（内部 Calendar 共享），多线程共享实例会产生数据错乱。。原因：官方建议每次创建新实例或用 ThreadLocal 包装。。
**来源：** JB-075 · 语言杂项（JDK8+）

**Qjava-basics-1615（判断·误用）** SimpleDateFormat 非线程安全（内部 Calendar 共享），多线程共享实例会产生数据错乱。
**答案：对。** 解析：官方建议每次创建新实例或用 ThreadLocal 包装。

**Qjava-basics-1616（判断·误用）** SimpleDateFormat 是线程安全的。
**答案：错。** 正确表述：SimpleDateFormat 非线程安全（内部 Calendar 共享），多线程共享实例会产生数据错乱。。原因：官方建议每次创建新实例或用 ThreadLocal 包装。

**Qjava-basics-1617（判断·误用）** SimpleDateFormat 线程不安全的问题在 JDK 新版已被修复。
**答案：错。** 正确表述：SimpleDateFormat 非线程安全（内部 Calendar 共享），多线程共享实例会产生数据错乱。。原因：官方建议每次创建新实例或用 ThreadLocal 包装。

**Qjava-basics-1618（判断·误用）** SimpleDateFormat 的错误只影响解析不影响格式化。
**答案：错。** 正确表述：SimpleDateFormat 非线程安全（内部 Calendar 共享），多线程共享实例会产生数据错乱。。原因：官方建议每次创建新实例或用 ThreadLocal 包装。

**Qjava-basics-1619（场景单选·误用）** 在工程实践中关于「可变静态日期」，下列做法符合推荐实践的是？
- A. SimpleDateFormat 线程不安全的问题在 JDK 新版已被修复。
- B. SimpleDateFormat 是线程安全的。
- C. SimpleDateFormat 的错误只影响解析不影响格式化。
- D. DateTimeFormatter（JDK8+）不可变且线程安全，直接替代。
**答案：D**
**解析：** 推荐实践：DateTimeFormatter（JDK8+）不可变且线程安全，直接替代。。事实依据：SimpleDateFormat 非线程安全（内部 Calendar 共享），多线程共享实例会产生数据错乱。。

**Qjava-basics-1620（场景判断·误用）** 推荐实践：DateTimeFormatter（JDK8+）不可变且线程安全，直接替代。
**答案：对。** 解析：SimpleDateFormat 非线程安全（内部 Calendar 共享），多线程共享实例会产生数据错乱。。原因：官方建议每次创建新实例或用 ThreadLocal 包装。

**Qjava-basics-1621（简答·误用）** 请说明「语言杂项」中可变静态日期的机制与使用要点。
**要点（标准答案）**：① SimpleDateFormat 非线程安全（内部 Calendar 共享），多线程共享实例会产生数据错乱。；② 原理：官方建议每次创建新实例或用 ThreadLocal 包装。；③ 使用要点：DateTimeFormatter（JDK8+）不可变且线程安全，直接替代。。版本锚点：JDK8+。

**Qjava-basics-1622（单选·正向·误用）** 关于「语言杂项」的说法，正确的是？
- A. Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。
- B. Random 是线程安全的且并发无性能损失。
- C. ThreadLocalRandom 需要手动创建和传递实例。
- D. new Random(固定种子) 每次结果不同。
**答案：A**
**解析：** Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。。原因：ThreadLocalRandom 为每个线程维护独立种子。。
**来源：** JB-076 · 语言杂项（JDK 7+（ThreadLocalRandom 推荐））

**Qjava-basics-1623（判断·误用）** Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。
**答案：对。** 解析：ThreadLocalRandom 为每个线程维护独立种子。

**Qjava-basics-1624（判断·误用）** Random 是线程安全的且并发无性能损失。
**答案：错。** 正确表述：Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。。原因：ThreadLocalRandom 为每个线程维护独立种子。

**Qjava-basics-1625（判断·误用）** ThreadLocalRandom 需要手动创建和传递实例。
**答案：错。** 正确表述：Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。。原因：ThreadLocalRandom 为每个线程维护独立种子。

**Qjava-basics-1626（判断·误用）** new Random(固定种子) 每次结果不同。
**答案：错。** 正确表述：Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。。原因：ThreadLocalRandom 为每个线程维护独立种子。

**Qjava-basics-1627（场景单选·误用）** 在工程实践中关于「随机数」，下列做法符合推荐实践的是？
- A. Random 是线程安全的且并发无性能损失。
- B. Random 用相同种子则序列可复现——测试可复现性的技巧。
- C. new Random(固定种子) 每次结果不同。
- D. ThreadLocalRandom 需要手动创建和传递实例。
**答案：B**
**解析：** 推荐实践：Random 用相同种子则序列可复现——测试可复现性的技巧。。事实依据：Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。。

**Qjava-basics-1628（场景判断·误用）** 推荐实践：Random 用相同种子则序列可复现——测试可复现性的技巧。
**答案：对。** 解析：Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。。原因：ThreadLocalRandom 为每个线程维护独立种子。

**Qjava-basics-1629（简答·误用）** 请说明「语言杂项」中随机数的机制与使用要点。
**要点（标准答案）**：① Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。；② 原理：ThreadLocalRandom 为每个线程维护独立种子。；③ 使用要点：Random 用相同种子则序列可复现——测试可复现性的技巧。。版本锚点：JDK 7+（ThreadLocalRandom 推荐）。

**Qjava-basics-1630（单选·正向·性能）** 关于「语言杂项」的说法，正确的是？
- A. 一个 emoji 的 length() 是 1。
- B. String.length() 返回的是 UTF-16 代码单元数而非字符数：增补字符（如 emoji）占 2 个代码单元。
- C. codePointCount 与 length 结果总是相同。
- D. String.length() 返回的是"字符个数"对任何字符都成立。
**答案：B**
**解析：** String.length() 返回的是 UTF-16 代码单元数而非字符数：增补字符（如 emoji）占 2 个代码单元。。原因：JDK9 前 String 底层是 char[]（UTF-16），JDK9+ byte[]+coder 逻辑上仍是 UTF-16 语义。。
**来源：** JB-077 · 语言杂项（JDK 9+（Compact Strings JEP 254））

**Qjava-basics-1631（判断·性能）** String.length() 返回的是 UTF-16 代码单元数而非字符数：增补字符（如 emoji）占 2 个代码单元。
**答案：对。** 解析：JDK9 前 String 底层是 char[]（UTF-16），JDK9+ byte[]+coder 逻辑上仍是 UTF-16 语义。

**Qjava-basics-1632（判断·性能）** String.length() 返回的是"字符个数"对任何字符都成立。
**答案：错。** 正确表述：String.length() 返回的是 UTF-16 代码单元数而非字符数：增补字符（如 emoji）占 2 个代码单元。。原因：JDK9 前 String 底层是 char[]（UTF-16），JDK9+ byte[]+coder 逻辑上仍是 UTF-16 语义。

**Qjava-basics-1633（判断·性能）** 一个 emoji 的 length() 是 1。
**答案：错。** 正确表述：String.length() 返回的是 UTF-16 代码单元数而非字符数：增补字符（如 emoji）占 2 个代码单元。。原因：JDK9 前 String 底层是 char[]（UTF-16），JDK9+ byte[]+coder 逻辑上仍是 UTF-16 语义。

**Qjava-basics-1634（判断·性能）** codePointCount 与 length 结果总是相同。
**答案：错。** 正确表述：String.length() 返回的是 UTF-16 代码单元数而非字符数：增补字符（如 emoji）占 2 个代码单元。。原因：JDK9 前 String 底层是 char[]（UTF-16），JDK9+ byte[]+coder 逻辑上仍是 UTF-16 语义。

**Qjava-basics-1635（场景单选·性能）** 在工程实践中关于「字符串长度」，下列做法符合推荐实践的是？
- A. codePointCount 与 length 结果总是相同。
- B. 涉及 emoji/生僻字的文本处理必须用码点 API（codePointAt 等）。
- C. String.length() 返回的是"字符个数"对任何字符都成立。
- D. 一个 emoji 的 length() 是 1。
**答案：B**
**解析：** 推荐实践：涉及 emoji/生僻字的文本处理必须用码点 API（codePointAt 等）。。事实依据：String.length() 返回的是 UTF-16 代码单元数而非字符数：增补字符（如 emoji）占 2 个代码单元。。

**Qjava-basics-1636（场景判断·性能）** 推荐实践：涉及 emoji/生僻字的文本处理必须用码点 API（codePointAt 等）。
**答案：对。** 解析：String.length() 返回的是 UTF-16 代码单元数而非字符数：增补字符（如 emoji）占 2 个代码单元。。原因：JDK9 前 String 底层是 char[]（UTF-16），JDK9+ byte[]+coder 逻辑上仍是 UTF-16 语义。

**Qjava-basics-1637（简答·性能）** 请说明「语言杂项」中字符串长度的机制与使用要点。
**要点（标准答案）**：① String.length() 返回的是 UTF-16 代码单元数而非字符数：增补字符（如 emoji）占 2 个代码单元。；② 原理：JDK9 前 String 底层是 char[]（UTF-16），JDK9+ byte[]+coder 逻辑上仍是 UTF-16 语义。；③ 使用要点：涉及 emoji/生僻字的文本处理必须用码点 API（codePointAt 等）。。版本锚点：JDK 9+（Compact Strings JEP 254）。

**Qjava-basics-1638（单选·正向·语法语义）** 关于「语言杂项」的说法，正确的是？
- A. 缓存对象与 new 对象 equals 不相等。
- B. valueOf 对任何值都返回缓存对象。
- C. new Integer(127) 与 valueOf(127) 是同一对象。
- D. Integer/Long/Short/Byte 缓存 -128~127 由 valueOf 触发，new Integer(127) 永远是新对象。
**答案：D**
**解析：** Integer/Long/Short/Byte 缓存 -128~127 由 valueOf 触发，new Integer(127) 永远是新对象。。原因：缓存实现于 IntegerCache 静态初始化块。。
**来源：** JB-078 · 语言杂项（JDK9+）

**Qjava-basics-1639（判断·语法语义）** Integer/Long/Short/Byte 缓存 -128~127 由 valueOf 触发，new Integer(127) 永远是新对象。
**答案：对。** 解析：缓存实现于 IntegerCache 静态初始化块。

**Qjava-basics-1640（判断·语法语义）** new Integer(127) 与 valueOf(127) 是同一对象。
**答案：错。** 正确表述：Integer/Long/Short/Byte 缓存 -128~127 由 valueOf 触发，new Integer(127) 永远是新对象。。原因：缓存实现于 IntegerCache 静态初始化块。

**Qjava-basics-1641（判断·语法语义）** valueOf 对任何值都返回缓存对象。
**答案：错。** 正确表述：Integer/Long/Short/Byte 缓存 -128~127 由 valueOf 触发，new Integer(127) 永远是新对象。。原因：缓存实现于 IntegerCache 静态初始化块。

**Qjava-basics-1642（判断·语法语义）** 缓存对象与 new 对象 equals 不相等。
**答案：错。** 正确表述：Integer/Long/Short/Byte 缓存 -128~127 由 valueOf 触发，new Integer(127) 永远是新对象。。原因：缓存实现于 IntegerCache 静态初始化块。

**Qjava-basics-1643（场景单选·语法语义）** 在工程实践中关于「整数缓存」，下列做法符合推荐实践的是？
- A. JDK9 起 new Integer 构造器已废弃，统一用 valueOf。
- B. new Integer(127) 与 valueOf(127) 是同一对象。
- C. 缓存对象与 new 对象 equals 不相等。
- D. valueOf 对任何值都返回缓存对象。
**答案：A**
**解析：** 推荐实践：JDK9 起 new Integer 构造器已废弃，统一用 valueOf。。事实依据：Integer/Long/Short/Byte 缓存 -128~127 由 valueOf 触发，new Integer(127) 永远是新对象。。

**Qjava-basics-1644（场景判断·语法语义）** 推荐实践：JDK9 起 new Integer 构造器已废弃，统一用 valueOf。
**答案：对。** 解析：Integer/Long/Short/Byte 缓存 -128~127 由 valueOf 触发，new Integer(127) 永远是新对象。。原因：缓存实现于 IntegerCache 静态初始化块。

**Qjava-basics-1645（简答·语法语义）** 请说明「语言杂项」中整数缓存的机制与使用要点。
**要点（标准答案）**：① Integer/Long/Short/Byte 缓存 -128~127 由 valueOf 触发，new Integer(127) 永远是新对象。；② 原理：缓存实现于 IntegerCache 静态初始化块。；③ 使用要点：JDK9 起 new Integer 构造器已废弃，统一用 valueOf。。版本锚点：JDK9+。

**Qjava-basics-1646（单选·正向·误用）** 关于「语言杂项」的说法，正确的是？
- A. 自动装箱没有性能开销。
- B. 装箱拆箱只发生在集合操作中。
- C. 循环中的包装类累加（Long sum = 0L; sum += i）每轮触发拆箱+装箱，性能差数倍。
- D. Long 累加和 long 累加性能相同。
**答案：C**
**解析：** 循环中的包装类累加（Long sum = 0L; sum += i）每轮触发拆箱+装箱，性能差数倍。。原因：装箱创建新对象（超缓存范围），产生大量临时对象。。
**来源：** JB-079 · 语言杂项（Effective Java 经典测量：装箱拖慢约数倍）

**Qjava-basics-1647（判断·误用）** 循环中的包装类累加（Long sum = 0L; sum += i）每轮触发拆箱+装箱，性能差数倍。
**答案：对。** 解析：装箱创建新对象（超缓存范围），产生大量临时对象。

**Qjava-basics-1648（判断·误用）** 自动装箱没有性能开销。
**答案：错。** 正确表述：循环中的包装类累加（Long sum = 0L; sum += i）每轮触发拆箱+装箱，性能差数倍。。原因：装箱创建新对象（超缓存范围），产生大量临时对象。

**Qjava-basics-1649（判断·误用）** 装箱拆箱只发生在集合操作中。
**答案：错。** 正确表述：循环中的包装类累加（Long sum = 0L; sum += i）每轮触发拆箱+装箱，性能差数倍。。原因：装箱创建新对象（超缓存范围），产生大量临时对象。

**Qjava-basics-1650（判断·误用）** Long 累加和 long 累加性能相同。
**答案：错。** 正确表述：循环中的包装类累加（Long sum = 0L; sum += i）每轮触发拆箱+装箱，性能差数倍。。原因：装箱创建新对象（超缓存范围），产生大量临时对象。

**Qjava-basics-1651（场景单选·误用）** 在工程实践中关于「自动装箱性能」，下列做法符合推荐实践的是？
- A. 自动装箱没有性能开销。
- B. 算法题累加统一用基本类型。
- C. 装箱拆箱只发生在集合操作中。
- D. Long 累加和 long 累加性能相同。
**答案：B**
**解析：** 推荐实践：算法题累加统一用基本类型。。事实依据：循环中的包装类累加（Long sum = 0L; sum += i）每轮触发拆箱+装箱，性能差数倍。。

**Qjava-basics-1652（场景判断·误用）** 推荐实践：算法题累加统一用基本类型。
**答案：对。** 解析：循环中的包装类累加（Long sum = 0L; sum += i）每轮触发拆箱+装箱，性能差数倍。。原因：装箱创建新对象（超缓存范围），产生大量临时对象。

**Qjava-basics-1653（简答·误用）** 请说明「语言杂项」中自动装箱性能的机制与使用要点。
**要点（标准答案）**：① 循环中的包装类累加（Long sum = 0L; sum += i）每轮触发拆箱+装箱，性能差数倍。；② 原理：装箱创建新对象（超缓存范围），产生大量临时对象。；③ 使用要点：算法题累加统一用基本类型。。版本锚点：Effective Java 经典测量：装箱拖慢约数倍。

**Qjava-basics-1654（单选·正向·语法语义）** 关于「集合通用」的说法，正确的是？
- A. Map 继承自 Collection 接口。
- B. Queue 不属于 Collection 体系。
- C. Collection 根接口下 List/Set/Queue 三大分支；Map 不是 Collection 的子接口。
- D. List 和 Set 都不是 Collection 的子接口。
**答案：C**
**解析：** Collection 根接口下 List/Set/Queue 三大分支；Map 不是 Collection 的子接口。。原因：Map 是独立的键值对抽象，与 Collection 并列。。
**来源：** JB-080 · 集合通用（JDK 集合框架文档）

**Qjava-basics-1655（判断·语法语义）** Collection 根接口下 List/Set/Queue 三大分支；Map 不是 Collection 的子接口。
**答案：对。** 解析：Map 是独立的键值对抽象，与 Collection 并列。

**Qjava-basics-1656（判断·语法语义）** Map 继承自 Collection 接口。
**答案：错。** 正确表述：Collection 根接口下 List/Set/Queue 三大分支；Map 不是 Collection 的子接口。。原因：Map 是独立的键值对抽象，与 Collection 并列。

**Qjava-basics-1657（判断·语法语义）** List 和 Set 都不是 Collection 的子接口。
**答案：错。** 正确表述：Collection 根接口下 List/Set/Queue 三大分支；Map 不是 Collection 的子接口。。原因：Map 是独立的键值对抽象，与 Collection 并列。

**Qjava-basics-1658（判断·语法语义）** Queue 不属于 Collection 体系。
**答案：错。** 正确表述：Collection 根接口下 List/Set/Queue 三大分支；Map 不是 Collection 的子接口。。原因：Map 是独立的键值对抽象，与 Collection 并列。

**Qjava-basics-1659（场景单选·语法语义）** 在工程实践中关于「Collection根接口」，下列做法符合推荐实践的是？
- A. Map 继承自 Collection 接口。
- B. Collections 是工具类，Collection 是接口——两者常被混淆。
- C. List 和 Set 都不是 Collection 的子接口。
- D. Queue 不属于 Collection 体系。
**答案：B**
**解析：** 推荐实践：Collections 是工具类，Collection 是接口——两者常被混淆。。事实依据：Collection 根接口下 List/Set/Queue 三大分支；Map 不是 Collection 的子接口。。

**Qjava-basics-1660（场景判断·语法语义）** 推荐实践：Collections 是工具类，Collection 是接口——两者常被混淆。
**答案：对。** 解析：Collection 根接口下 List/Set/Queue 三大分支；Map 不是 Collection 的子接口。。原因：Map 是独立的键值对抽象，与 Collection 并列。

**Qjava-basics-1661（填空·语法语义）** ______下 List/Set/Queue 三大分支；Map 不是 Collection 的子接口。
**答案：Collection根接口**。解析：Map 是独立的键值对抽象，与 Collection 并列。

**Qjava-basics-1662（简答·语法语义）** 请说明「集合通用」中Collection根接口的机制与使用要点。
**要点（标准答案）**：① Collection 根接口下 List/Set/Queue 三大分支；Map 不是 Collection 的子接口。；② 原理：Map 是独立的键值对抽象，与 Collection 并列。；③ 使用要点：Collections 是工具类，Collection 是接口——两者常被混淆。。版本锚点：JDK 集合框架文档。

**Qjava-basics-1663（单选·正向·误用）** 关于「集合通用」的说法，正确的是？
- A. 遍历集合删除元素的安全方式：Iterator.remove()、removeIf、或 CopyOnWriteArrayList（快照迭代）。
- B. Iterator.remove 之后 continue 会跳过元素。
- C. 增强 for 循环中直接 remove 是安全的。
- D. removeIf 内部不会处理并发修改。
**答案：A**
**解析：** 遍历集合删除元素的安全方式：Iterator.remove()、removeIf、或 CopyOnWriteArrayList（快照迭代）。。原因：裸 for+remove 因索引移动漏删；增强 for 中 remove 抛 CME。。
**来源：** JB-081 · 集合通用（Iterator.remove javadoc）

**Qjava-basics-1664（判断·误用）** 遍历集合删除元素的安全方式：Iterator.remove()、removeIf、或 CopyOnWriteArrayList（快照迭代）。
**答案：对。** 解析：裸 for+remove 因索引移动漏删；增强 for 中 remove 抛 CME。

**Qjava-basics-1665（判断·误用）** 增强 for 循环中直接 remove 是安全的。
**答案：错。** 正确表述：遍历集合删除元素的安全方式：Iterator.remove()、removeIf、或 CopyOnWriteArrayList（快照迭代）。。原因：裸 for+remove 因索引移动漏删；增强 for 中 remove 抛 CME。

**Qjava-basics-1666（判断·误用）** removeIf 内部不会处理并发修改。
**答案：错。** 正确表述：遍历集合删除元素的安全方式：Iterator.remove()、removeIf、或 CopyOnWriteArrayList（快照迭代）。。原因：裸 for+remove 因索引移动漏删；增强 for 中 remove 抛 CME。

**Qjava-basics-1667（判断·误用）** Iterator.remove 之后 continue 会跳过元素。
**答案：错。** 正确表述：遍历集合删除元素的安全方式：Iterator.remove()、removeIf、或 CopyOnWriteArrayList（快照迭代）。。原因：裸 for+remove 因索引移动漏删；增强 for 中 remove 抛 CME。

**Qjava-basics-1668（场景单选·误用）** 在工程实践中关于「迭代中删除」，下列做法符合推荐实践的是？
- A. Iterator.remove 之后 continue 会跳过元素。
- B. 增强 for 循环中直接 remove 是安全的。
- C. removeIf 内部不会处理并发修改。
- D. "漏删"是本机可复现的经典 bug：索引前移跳过下一元素。
**答案：D**
**解析：** 推荐实践："漏删"是本机可复现的经典 bug：索引前移跳过下一元素。。事实依据：遍历集合删除元素的安全方式：Iterator.remove()、removeIf、或 CopyOnWriteArrayList（快照迭代）。。

**Qjava-basics-1669（场景判断·误用）** 推荐实践："漏删"是本机可复现的经典 bug：索引前移跳过下一元素。
**答案：对。** 解析：遍历集合删除元素的安全方式：Iterator.remove()、removeIf、或 CopyOnWriteArrayList（快照迭代）。。原因：裸 for+remove 因索引移动漏删；增强 for 中 remove 抛 CME。

**Qjava-basics-1670（简答·误用）** 请说明「集合通用」中迭代中删除的机制与使用要点。
**要点（标准答案）**：① 遍历集合删除元素的安全方式：Iterator.remove()、removeIf、或 CopyOnWriteArrayList（快照迭代）。；② 原理：裸 for+remove 因索引移动漏删；增强 for 中 remove 抛 CME。；③ 使用要点："漏删"是本机可复现的经典 bug：索引前移跳过下一元素。。版本锚点：Iterator.remove javadoc。

**Qjava-basics-1671（单选·正向·性能）** 关于「集合通用」的说法，正确的是？
- A. LinkedList 随机访问是 O(1)。
- B. TreeMap 的 get 与 HashMap 相同都是 O(1)。
- C. 核心复杂度速记：ArrayList get O(1)/中间插 O(n)；HashMap get/put 均摊 O(1)；TreeMap O(log n)；LinkedList 头尾操作 O(1)/定位 O(n)。
- D. HashMap 最坏情况也是 O(1)。
**答案：C**
**解析：** 核心复杂度速记：ArrayList get O(1)/中间插 O(n)；HashMap get/put 均摊 O(1)；TreeMap O(log n)；LinkedList 头尾操作 O(1)/定位 O(n)。。原因：复杂度是集合选型的第一判据。。
**来源：** JB-082 · 集合通用（各容器 javadoc）

**Qjava-basics-1672（判断·性能）** 核心复杂度速记：ArrayList get O(1)/中间插 O(n)；HashMap get/put 均摊 O(1)；TreeMap O(log n)；LinkedList 头尾操作 O(1)/定位 O(n)。
**答案：对。** 解析：复杂度是集合选型的第一判据。

**Qjava-basics-1673（判断·性能）** HashMap 最坏情况也是 O(1)。
**答案：错。** 正确表述：核心复杂度速记：ArrayList get O(1)/中间插 O(n)；HashMap get/put 均摊 O(1)；TreeMap O(log n)；LinkedList 头尾操作 O(1)/定位 O(n)。。原因：复杂度是集合选型的第一判据。

**Qjava-basics-1674（判断·性能）** TreeMap 的 get 与 HashMap 相同都是 O(1)。
**答案：错。** 正确表述：核心复杂度速记：ArrayList get O(1)/中间插 O(n)；HashMap get/put 均摊 O(1)；TreeMap O(log n)；LinkedList 头尾操作 O(1)/定位 O(n)。。原因：复杂度是集合选型的第一判据。

**Qjava-basics-1675（判断·性能）** LinkedList 随机访问是 O(1)。
**答案：错。** 正确表述：核心复杂度速记：ArrayList get O(1)/中间插 O(n)；HashMap get/put 均摊 O(1)；TreeMap O(log n)；LinkedList 头尾操作 O(1)/定位 O(n)。。原因：复杂度是集合选型的第一判据。

**Qjava-basics-1676（场景单选·性能）** 在工程实践中关于「时间复杂度表」，下列做法符合推荐实践的是？
- A. LinkedList 随机访问是 O(1)。
- B. HashMap 树化后最坏 O(log n)（JDK8+）。
- C. TreeMap 的 get 与 HashMap 相同都是 O(1)。
- D. HashMap 最坏情况也是 O(1)。
**答案：B**
**解析：** 推荐实践：HashMap 树化后最坏 O(log n)（JDK8+）。。事实依据：核心复杂度速记：ArrayList get O(1)/中间插 O(n)；HashMap get/put 均摊 O(1)；TreeMap O(log n)；LinkedList 头尾操作 O(1)/定位 O(n)。。

**Qjava-basics-1677（场景判断·性能）** 推荐实践：HashMap 树化后最坏 O(log n)（JDK8+）。
**答案：对。** 解析：核心复杂度速记：ArrayList get O(1)/中间插 O(n)；HashMap get/put 均摊 O(1)；TreeMap O(log n)；LinkedList 头尾操作 O(1)/定位 O(n)。。原因：复杂度是集合选型的第一判据。

**Qjava-basics-1678（简答·性能）** 请说明「集合通用」中时间复杂度表的机制与使用要点。
**要点（标准答案）**：① 核心复杂度速记：ArrayList get O(1)/中间插 O(n)；HashMap get/put 均摊 O(1)；TreeMap O(log n)；LinkedList 头尾操作 O(1)/定位 O(n)。；② 原理：复杂度是集合选型的第一判据。；③ 使用要点：HashMap 树化后最坏 O(log n)（JDK8+）。。版本锚点：各容器 javadoc。

**Qjava-basics-1679（单选·正向·语法语义）** 关于「集合通用」的说法，正确的是？
- A. List.of 返回的就是 ArrayList。
- B. JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。
- C. List.of 允许 null 元素。
- D. List.of 返回的集合可以排序。
**答案：B**
**解析：** JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。。原因：不可变集合是防御性编程与安全发布的标准做法。。
**来源：** JB-083 · 集合通用（JDK9+）

**Qjava-basics-1680（判断·语法语义）** JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。
**答案：对。** 解析：不可变集合是防御性编程与安全发布的标准做法。

**Qjava-basics-1681（判断·语法语义）** List.of 返回的集合可以排序。
**答案：错。** 正确表述：JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。。原因：不可变集合是防御性编程与安全发布的标准做法。

**Qjava-basics-1682（判断·语法语义）** List.of 允许 null 元素。
**答案：错。** 正确表述：JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。。原因：不可变集合是防御性编程与安全发布的标准做法。

**Qjava-basics-1683（判断·语法语义）** List.of 返回的就是 ArrayList。
**答案：错。** 正确表述：JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。。原因：不可变集合是防御性编程与安全发布的标准做法。

**Qjava-basics-1684（场景单选·语法语义）** 在工程实践中关于「不可变集合」，下列做法符合推荐实践的是？
- A. List.of 返回的就是 ArrayList。
- B. List.of 返回的集合可以排序。
- C. 跨方法边界返回不可变集合可防调用方误改。
- D. List.of 允许 null 元素。
**答案：C**
**解析：** 推荐实践：跨方法边界返回不可变集合可防调用方误改。。事实依据：JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。。

**Qjava-basics-1685（场景判断·语法语义）** 推荐实践：跨方法边界返回不可变集合可防调用方误改。
**答案：对。** 解析：JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。。原因：不可变集合是防御性编程与安全发布的标准做法。

**Qjava-basics-1686（填空·语法语义）** JDK9+ 的 List.of/Set.of/Map.of 创建______：add/remove 抛 UnsupportedOperationException，不允许 null 元素。
**答案：不可变集合**。解析：不可变集合是防御性编程与安全发布的标准做法。

**Qjava-basics-1687（简答·语法语义）** 请说明「集合通用」中不可变集合的机制与使用要点。
**要点（标准答案）**：① JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。；② 原理：不可变集合是防御性编程与安全发布的标准做法。；③ 使用要点：跨方法边界返回不可变集合可防调用方误改。。版本锚点：JDK9+。

**Qjava-basics-1688（单选·正向·误用）** 关于「集合通用」的说法，正确的是？
- A. 堆污染是编译错误不是运行时风险。
- B. 泛型数组与普通数组行为完全一致。
- C. new T[10] 在 Java 中是合法的。
- D. 不能直接创建泛型数组（new T[] 编译错误），因为数组是协变且运行时携带精确类型，与擦除冲突。
**答案：D**
**解析：** 不能直接创建泛型数组（new T[] 编译错误），因为数组是协变且运行时携带精确类型，与擦除冲突。。原因：堆污染（heap pollution）风险：数组协变+泛型不变的设计冲突。。
**来源：** JB-084 · 集合通用（JLS 15.10）

**Qjava-basics-1689（判断·误用）** 不能直接创建泛型数组（new T[] 编译错误），因为数组是协变且运行时携带精确类型，与擦除冲突。
**答案：对。** 解析：堆污染（heap pollution）风险：数组协变+泛型不变的设计冲突。

**Qjava-basics-1690（判断·误用）** new T[10] 在 Java 中是合法的。
**答案：错。** 正确表述：不能直接创建泛型数组（new T[] 编译错误），因为数组是协变且运行时携带精确类型，与擦除冲突。。原因：堆污染（heap pollution）风险：数组协变+泛型不变的设计冲突。

**Qjava-basics-1691（判断·误用）** 泛型数组与普通数组行为完全一致。
**答案：错。** 正确表述：不能直接创建泛型数组（new T[] 编译错误），因为数组是协变且运行时携带精确类型，与擦除冲突。。原因：堆污染（heap pollution）风险：数组协变+泛型不变的设计冲突。

**Qjava-basics-1692（判断·误用）** 堆污染是编译错误不是运行时风险。
**答案：错。** 正确表述：不能直接创建泛型数组（new T[] 编译错误），因为数组是协变且运行时携带精确类型，与擦除冲突。。原因：堆污染（heap pollution）风险：数组协变+泛型不变的设计冲突。

**Qjava-basics-1693（场景单选·误用）** 在工程实践中关于「泛型数组」，下列做法符合推荐实践的是？
- A. new T[10] 在 Java 中是合法的。
- B. @SafeVarargs 标注是可变参数+泛型的官方豁免方式。
- C. 堆污染是编译错误不是运行时风险。
- D. 泛型数组与普通数组行为完全一致。
**答案：B**
**解析：** 推荐实践：@SafeVarargs 标注是可变参数+泛型的官方豁免方式。。事实依据：不能直接创建泛型数组（new T[] 编译错误），因为数组是协变且运行时携带精确类型，与擦除冲突。。

**Qjava-basics-1694（场景判断·误用）** 推荐实践：@SafeVarargs 标注是可变参数+泛型的官方豁免方式。
**答案：对。** 解析：不能直接创建泛型数组（new T[] 编译错误），因为数组是协变且运行时携带精确类型，与擦除冲突。。原因：堆污染（heap pollution）风险：数组协变+泛型不变的设计冲突。

**Qjava-basics-1695（填空·误用）** 不能直接创建______（new T[] 编译错误），因为数组是协变且运行时携带精确类型，与擦除冲突。
**答案：泛型数组**。解析：堆污染（heap pollution）风险：数组协变+泛型不变的设计冲突。

**Qjava-basics-1696（简答·误用）** 请说明「集合通用」中泛型数组的机制与使用要点。
**要点（标准答案）**：① 不能直接创建泛型数组（new T[] 编译错误），因为数组是协变且运行时携带精确类型，与擦除冲突。；② 原理：堆污染（heap pollution）风险：数组协变+泛型不变的设计冲突。；③ 使用要点：@SafeVarargs 标注是可变参数+泛型的官方豁免方式。。版本锚点：JLS 15.10。

**Qjava-basics-1697（单选·正向·语法语义）** 关于「包装类」的说法，正确的是？
- A. Character 没有缓存机制。
- B. Character 缓存与 Integer 完全相同是 -128~127。
- C. Character 缓存范围是 0~127（与 Integer 的 -128~127 不同），valueOf 在此范围返回缓存实例。
- D. Character 缓存覆盖所有 ASCII 字符。
**答案：C**
**解析：** Character 缓存范围是 0~127（与 Integer 的 -128~127 不同），valueOf 在此范围返回缓存实例。。原因：Character 无负值语义，缓存从 0 开始。。
**来源：** JB-085 · 包装类（JLS 5.1.7（0~127））

**Qjava-basics-1698（判断·语法语义）** Character 缓存范围是 0~127（与 Integer 的 -128~127 不同），valueOf 在此范围返回缓存实例。
**答案：对。** 解析：Character 无负值语义，缓存从 0 开始。

**Qjava-basics-1699（判断·语法语义）** Character 缓存与 Integer 完全相同是 -128~127。
**答案：错。** 正确表述：Character 缓存范围是 0~127（与 Integer 的 -128~127 不同），valueOf 在此范围返回缓存实例。。原因：Character 无负值语义，缓存从 0 开始。

**Qjava-basics-1700（判断·语法语义）** Character 没有缓存机制。
**答案：错。** 正确表述：Character 缓存范围是 0~127（与 Integer 的 -128~127 不同），valueOf 在此范围返回缓存实例。。原因：Character 无负值语义，缓存从 0 开始。

**Qjava-basics-1701（判断·语法语义）** Character 缓存覆盖所有 ASCII 字符。
**答案：错。** 正确表述：Character 缓存范围是 0~127（与 Integer 的 -128~127 不同），valueOf 在此范围返回缓存实例。。原因：Character 无负值语义，缓存从 0 开始。

**Qjava-basics-1702（场景单选·语法语义）** 在工程实践中关于「Character缓存」，下列做法符合推荐实践的是？
- A. Character 缓存覆盖所有 ASCII 字符。
- B. Character 缓存与 Integer 完全相同是 -128~127。
- C. Character 没有缓存机制。
- D. ASCII 128~255 的 Character 不在缓存内。
**答案：D**
**解析：** 推荐实践：ASCII 128~255 的 Character 不在缓存内。。事实依据：Character 缓存范围是 0~127（与 Integer 的 -128~127 不同），valueOf 在此范围返回缓存实例。。

**Qjava-basics-1703（场景判断·语法语义）** 推荐实践：ASCII 128~255 的 Character 不在缓存内。
**答案：对。** 解析：Character 缓存范围是 0~127（与 Integer 的 -128~127 不同），valueOf 在此范围返回缓存实例。。原因：Character 无负值语义，缓存从 0 开始。

**Qjava-basics-1704（填空·语法语义）** ______范围是 0~127（与 Integer 的 -128~127 不同），valueOf 在此范围返回缓存实例。
**答案：Character缓存**。解析：Character 无负值语义，缓存从 0 开始。

**Qjava-basics-1705（简答·语法语义）** 请说明「包装类」中Character缓存的机制与使用要点。
**要点（标准答案）**：① Character 缓存范围是 0~127（与 Integer 的 -128~127 不同），valueOf 在此范围返回缓存实例。；② 原理：Character 无负值语义，缓存从 0 开始。；③ 使用要点：ASCII 128~255 的 Character 不在缓存内。。版本锚点：JLS 5.1.7（0~127）。

**Qjava-basics-1706（单选·正向·语法语义）** 关于「包装类」的说法，正确的是？
- A. Boolean.valueOf 与 Boolean.parseBoolean 返回相同类型但用途不同（包装类 vs 基本类型）。
- B. Boolean 有四个缓存实例。
- C. Byte 只有部分值被缓存。
- D. Boolean 缓存仅 true/false 两个实例；Byte 因范围小（-128~127）全部缓存。
**答案：D**
**解析：** Boolean 缓存仅 true/false 两个实例；Byte 因范围小（-128~127）全部缓存。。原因：小范围类型的所有值都值得缓存。。
**来源：** JB-086 · 包装类（JLS 5.1.7）

**Qjava-basics-1707（判断·语法语义）** Boolean 缓存仅 true/false 两个实例；Byte 因范围小（-128~127）全部缓存。
**答案：对。** 解析：小范围类型的所有值都值得缓存。

**Qjava-basics-1708（判断·语法语义）** Byte 只有部分值被缓存。
**答案：错。** 正确表述：Boolean 缓存仅 true/false 两个实例；Byte 因范围小（-128~127）全部缓存。。原因：小范围类型的所有值都值得缓存。

**Qjava-basics-1709（判断·语法语义）** Boolean 有四个缓存实例。
**答案：错。** 正确表述：Boolean 缓存仅 true/false 两个实例；Byte 因范围小（-128~127）全部缓存。。原因：小范围类型的所有值都值得缓存。

**Qjava-basics-1710（判断·语法语义）** Boolean.valueOf 与 Boolean.parseBoolean 返回相同类型但用途不同（包装类 vs 基本类型）。
**答案：错。** 正确表述：Boolean 缓存仅 true/false 两个实例；Byte 因范围小（-128~127）全部缓存。。原因：小范围类型的所有值都值得缓存。

**Qjava-basics-1711（场景单选·语法语义）** 在工程实践中关于「Boolean与Byte」，下列做法符合推荐实践的是？
- A. Boolean.valueOf 与 Boolean.parseBoolean 返回相同类型但用途不同（包装类 vs 基本类型）。
- B. Boolean.valueOf 返回包装类，parseBoolean 返回基本类型。
- C. Boolean 有四个缓存实例。
- D. Byte 只有部分值被缓存。
**答案：B**
**解析：** 推荐实践：Boolean.valueOf 返回包装类，parseBoolean 返回基本类型。。事实依据：Boolean 缓存仅 true/false 两个实例；Byte 因范围小（-128~127）全部缓存。。

**Qjava-basics-1712（场景判断·语法语义）** 推荐实践：Boolean.valueOf 返回包装类，parseBoolean 返回基本类型。
**答案：对。** 解析：Boolean 缓存仅 true/false 两个实例；Byte 因范围小（-128~127）全部缓存。。原因：小范围类型的所有值都值得缓存。

**Qjava-basics-1713（简答·语法语义）** 请说明「包装类」中Boolean与Byte的机制与使用要点。
**要点（标准答案）**：① Boolean 缓存仅 true/false 两个实例；Byte 因范围小（-128~127）全部缓存。；② 原理：小范围类型的所有值都值得缓存。；③ 使用要点：Boolean.valueOf 返回包装类，parseBoolean 返回基本类型。。版本锚点：JLS 5.1.7。

**Qjava-basics-1714（单选·正向·误用）** 关于「String」的说法，正确的是？
- A. variable.equals("CONST") 与常量在前等价且同样安全。
- B. null.equals("x") 返回 false。
- C. 常量在前调用 equals（"CONST".equals(variable)）可避免 variable 为 null 时抛 NPE。
- D. Objects.equals(a,b) 不存在。
**答案：C**
**解析：** 常量在前调用 equals（"CONST".equals(variable)）可避免 variable 为 null 时抛 NPE。。原因：null.equals 抛 NPE，常量.equals(null) 返回 false。。
**来源：** JB-087 · String（JDK7+）

**Qjava-basics-1715（判断·误用）** 常量在前调用 equals（"CONST".equals(variable)）可避免 variable 为 null 时抛 NPE。
**答案：对。** 解析：null.equals 抛 NPE，常量.equals(null) 返回 false。

**Qjava-basics-1716（判断·误用）** variable.equals("CONST") 与常量在前等价且同样安全。
**答案：错。** 正确表述：常量在前调用 equals（"CONST".equals(variable)）可避免 variable 为 null 时抛 NPE。。原因：null.equals 抛 NPE，常量.equals(null) 返回 false。

**Qjava-basics-1717（判断·误用）** null.equals("x") 返回 false。
**答案：错。** 正确表述：常量在前调用 equals（"CONST".equals(variable)）可避免 variable 为 null 时抛 NPE。。原因：null.equals 抛 NPE，常量.equals(null) 返回 false。

**Qjava-basics-1718（判断·误用）** Objects.equals(a,b) 不存在。
**答案：错。** 正确表述：常量在前调用 equals（"CONST".equals(variable)）可避免 variable 为 null 时抛 NPE。。原因：null.equals 抛 NPE，常量.equals(null) 返回 false。

**Qjava-basics-1719（场景单选·误用）** 在工程实践中关于「equals方向」，下列做法符合推荐实践的是？
- A. variable.equals("CONST") 与常量在前等价且同样安全。
- B. null.equals("x") 返回 false。
- C. JDK7+ 的 java.util.Objects.equals(a,b) 是 null 安全的标准替代。
- D. Objects.equals(a,b) 不存在。
**答案：C**
**解析：** 推荐实践：JDK7+ 的 java.util.Objects.equals(a,b) 是 null 安全的标准替代。。事实依据：常量在前调用 equals（"CONST".equals(variable)）可避免 variable 为 null 时抛 NPE。。

**Qjava-basics-1720（场景判断·误用）** 推荐实践：JDK7+ 的 java.util.Objects.equals(a,b) 是 null 安全的标准替代。
**答案：对。** 解析：常量在前调用 equals（"CONST".equals(variable)）可避免 variable 为 null 时抛 NPE。。原因：null.equals 抛 NPE，常量.equals(null) 返回 false。

**Qjava-basics-1721（简答·误用）** 请说明「String」中equals方向的机制与使用要点。
**要点（标准答案）**：① 常量在前调用 equals（"CONST".equals(variable)）可避免 variable 为 null 时抛 NPE。；② 原理：null.equals 抛 NPE，常量.equals(null) 返回 false。；③ 使用要点：JDK7+ 的 java.util.Objects.equals(a,b) 是 null 安全的标准替代。。版本锚点：JDK7+。

**Qjava-basics-1722（单选·正向·误用）** 关于「String」的说法，正确的是？
- A. String.split 的参数是正则表达式，且默认省略尾部空串——特殊字符（点号与星号）必须转义。
- B. split 的参数就是普通字符串。
- C. split 永远保留尾部空字符串。
- D. split(".") 会按字面量点分割。
**答案：A**
**解析：** String.split 的参数是正则表达式，且默认省略尾部空串——特殊字符（点号与星号）必须转义。。原因：正则语义导致 "." 会匹配任意字符；limit 参数传负数保留尾部空串。。
**来源：** JB-088 · String（Java 正则语义）

**Qjava-basics-1723（判断·误用）** String.split 的参数是正则表达式，且默认省略尾部空串——特殊字符（点号与星号）必须转义。
**答案：对。** 解析：正则语义导致 "." 会匹配任意字符；limit 参数传负数保留尾部空串。

**Qjava-basics-1724（判断·误用）** split(".") 会按字面量点分割。
**答案：错。** 正确表述：String.split 的参数是正则表达式，且默认省略尾部空串——特殊字符（点号与星号）必须转义。。原因：正则语义导致 "." 会匹配任意字符；limit 参数传负数保留尾部空串。

**Qjava-basics-1725（判断·误用）** split 永远保留尾部空字符串。
**答案：错。** 正确表述：String.split 的参数是正则表达式，且默认省略尾部空串——特殊字符（点号与星号）必须转义。。原因：正则语义导致 "." 会匹配任意字符；limit 参数传负数保留尾部空串。

**Qjava-basics-1726（判断·误用）** split 的参数就是普通字符串。
**答案：错。** 正确表述：String.split 的参数是正则表达式，且默认省略尾部空串——特殊字符（点号与星号）必须转义。。原因：正则语义导致 "." 会匹配任意字符；limit 参数传负数保留尾部空串。

**Qjava-basics-1727（场景单选·误用）** 在工程实践中关于「split陷阱」，下列做法符合推荐实践的是？
- A. split 的参数就是普通字符串。
- B. split(".") 会按字面量点分割。
- C. 常见事故：按 "." 分割 IP 地址得到空数组。
- D. split 永远保留尾部空字符串。
**答案：C**
**解析：** 推荐实践：常见事故：按 "." 分割 IP 地址得到空数组。。事实依据：String.split 的参数是正则表达式，且默认省略尾部空串——特殊字符（点号与星号）必须转义。。

**Qjava-basics-1728（场景判断·误用）** 推荐实践：常见事故：按 "." 分割 IP 地址得到空数组。
**答案：对。** 解析：String.split 的参数是正则表达式，且默认省略尾部空串——特殊字符（点号与星号）必须转义。。原因：正则语义导致 "." 会匹配任意字符；limit 参数传负数保留尾部空串。

**Qjava-basics-1729（简答·误用）** 请说明「String」中split陷阱的机制与使用要点。
**要点（标准答案）**：① String.split 的参数是正则表达式，且默认省略尾部空串——特殊字符（点号与星号）必须转义。；② 原理：正则语义导致 "." 会匹配任意字符；limit 参数传负数保留尾部空串。；③ 使用要点：常见事故：按 "." 分割 IP 地址得到空数组。。版本锚点：Java 正则语义。

**Qjava-basics-1730（单选·正向·性能）** 关于「String」的说法，正确的是？
- A. substring 的实现与 JDK 版本无关。
- B. JDK7u6 前 substring 共享原字符数组导致内存泄漏风险，之后改为拷贝实现。
- C. substring 从未有过内存泄漏风险。
- D. substring 在所有 JDK 版本中都拷贝新数组。
**答案：B**
**解析：** JDK7u6 前 substring 共享原字符数组导致内存泄漏风险，之后改为拷贝实现。。原因：旧实现 offset+count 指向原数组，大字符串截取小片段会"钉住"整个大数组。。
**来源：** JB-089 · String（JDK7u6）

**Qjava-basics-1731（判断·性能）** JDK7u6 前 substring 共享原字符数组导致内存泄漏风险，之后改为拷贝实现。
**答案：对。** 解析：旧实现 offset+count 指向原数组，大字符串截取小片段会"钉住"整个大数组。

**Qjava-basics-1732（判断·性能）** substring 从未有过内存泄漏风险。
**答案：错。** 正确表述：JDK7u6 前 substring 共享原字符数组导致内存泄漏风险，之后改为拷贝实现。。原因：旧实现 offset+count 指向原数组，大字符串截取小片段会"钉住"整个大数组。

**Qjava-basics-1733（判断·性能）** substring 在所有 JDK 版本中都拷贝新数组。
**答案：错。** 正确表述：JDK7u6 前 substring 共享原字符数组导致内存泄漏风险，之后改为拷贝实现。。原因：旧实现 offset+count 指向原数组，大字符串截取小片段会"钉住"整个大数组。

**Qjava-basics-1734（判断·性能）** substring 的实现与 JDK 版本无关。
**答案：错。** 正确表述：JDK7u6 前 substring 共享原字符数组导致内存泄漏风险，之后改为拷贝实现。。原因：旧实现 offset+count 指向原数组，大字符串截取小片段会"钉住"整个大数组。

**Qjava-basics-1735（场景单选·性能）** 在工程实践中关于「substring」，下列做法符合推荐实践的是？
- A. substring 在所有 JDK 版本中都拷贝新数组。
- B. P10 面试常以"substring 与内存泄漏"考察对实现的版本敏感度。
- C. substring 从未有过内存泄漏风险。
- D. substring 的实现与 JDK 版本无关。
**答案：B**
**解析：** 推荐实践：P10 面试常以"substring 与内存泄漏"考察对实现的版本敏感度。。事实依据：JDK7u6 前 substring 共享原字符数组导致内存泄漏风险，之后改为拷贝实现。。

**Qjava-basics-1736（场景判断·性能）** 推荐实践：P10 面试常以"substring 与内存泄漏"考察对实现的版本敏感度。
**答案：对。** 解析：JDK7u6 前 substring 共享原字符数组导致内存泄漏风险，之后改为拷贝实现。。原因：旧实现 offset+count 指向原数组，大字符串截取小片段会"钉住"整个大数组。

**Qjava-basics-1737（填空·性能）** JDK7u6 前 ______ 共享原字符数组导致内存泄漏风险，之后改为拷贝实现。
**答案：substring**。解析：旧实现 offset+count 指向原数组，大字符串截取小片段会"钉住"整个大数组。

**Qjava-basics-1738（简答·性能）** 请说明「String」中substring的机制与使用要点。
**要点（标准答案）**：① JDK7u6 前 substring 共享原字符数组导致内存泄漏风险，之后改为拷贝实现。；② 原理：旧实现 offset+count 指向原数组，大字符串截取小片段会"钉住"整个大数组。；③ 使用要点：P10 面试常以"substring 与内存泄漏"考察对实现的版本敏感度。。版本锚点：JDK7u6。

**Qjava-basics-1739（单选·正向·误用）** 关于「String」的说法，正确的是？
- A. replace 不支持替换所有出现次数。
- B. replaceAll 的性能一定比 replace 好。
- C. replace 接收字面量（char/CharSequence），replaceAll 接收正则表达式——replaceAll(".") 会替换所有字符。
- D. replace 与 replaceAll 完全等价只是名字不同。
**答案：C**
**解析：** replace 接收字面量（char/CharSequence），replaceAll 接收正则表达式——replaceAll(".") 会替换所有字符。。原因：replaceAll 是正则语义，点号匹配任意字符。。
**来源：** JB-090 · String（String javadoc）

**Qjava-basics-1740（判断·误用）** replace 接收字面量（char/CharSequence），replaceAll 接收正则表达式——replaceAll(".") 会替换所有字符。
**答案：对。** 解析：replaceAll 是正则语义，点号匹配任意字符。

**Qjava-basics-1741（判断·误用）** replace 与 replaceAll 完全等价只是名字不同。
**答案：错。** 正确表述：replace 接收字面量（char/CharSequence），replaceAll 接收正则表达式——replaceAll(".") 会替换所有字符。。原因：replaceAll 是正则语义，点号匹配任意字符。

**Qjava-basics-1742（判断·误用）** replace 不支持替换所有出现次数。
**答案：错。** 正确表述：replace 接收字面量（char/CharSequence），replaceAll 接收正则表达式——replaceAll(".") 会替换所有字符。。原因：replaceAll 是正则语义，点号匹配任意字符。

**Qjava-basics-1743（判断·误用）** replaceAll 的性能一定比 replace 好。
**答案：错。** 正确表述：replace 接收字面量（char/CharSequence），replaceAll 接收正则表达式——replaceAll(".") 会替换所有字符。。原因：replaceAll 是正则语义，点号匹配任意字符。

**Qjava-basics-1744（场景单选·误用）** 在工程实践中关于「replace与replaceAll」，下列做法符合推荐实践的是？
- A. replace 与 replaceAll 完全等价只是名字不同。
- B. replaceAll 的性能一定比 replace 好。
- C. 分割 IP 前缀等场景 replaceAll("\\.","-") 需双反斜杠转义。
- D. replace 不支持替换所有出现次数。
**答案：C**
**解析：** 推荐实践：分割 IP 前缀等场景 replaceAll("\\.","-") 需双反斜杠转义。。事实依据：replace 接收字面量（char/CharSequence），replaceAll 接收正则表达式——replaceAll(".") 会替换所有字符。。

**Qjava-basics-1745（场景判断·误用）** 推荐实践：分割 IP 前缀等场景 replaceAll("\\.","-") 需双反斜杠转义。
**答案：对。** 解析：replace 接收字面量（char/CharSequence），replaceAll 接收正则表达式——replaceAll(".") 会替换所有字符。。原因：replaceAll 是正则语义，点号匹配任意字符。

**Qjava-basics-1746（简答·误用）** 请说明「String」中replace与replaceAll的机制与使用要点。
**要点（标准答案）**：① replace 接收字面量（char/CharSequence），replaceAll 接收正则表达式——replaceAll(".") 会替换所有字符。；② 原理：replaceAll 是正则语义，点号匹配任意字符。；③ 使用要点：分割 IP 前缀等场景 replaceAll("\\.","-") 需双反斜杠转义。。版本锚点：String javadoc。

**Qjava-basics-1747（单选·正向·语法语义）** 关于「泛型」的说法，正确的是？
- A. 泛型方法的类型参数由运行时决定。
- B. 泛型方法与泛型类的类型参数必须同名。
- C. 泛型方法必须显式指定类型参数。
- D. 泛型方法的类型参数声明在返回类型之前（<T> T f(...)），由编译器按实参推断。
**答案：D**
**解析：** 泛型方法的类型参数声明在返回类型之前（<T> T f(...)），由编译器按实参推断。。原因：推断规则在 JDK8 改进（目标类型推断）。。
**来源：** JB-091 · 泛型（JLS 8.4.4）

**Qjava-basics-1748（判断·语法语义）** 泛型方法的类型参数声明在返回类型之前（<T> T f(...)），由编译器按实参推断。
**答案：对。** 解析：推断规则在 JDK8 改进（目标类型推断）。

**Qjava-basics-1749（判断·语法语义）** 泛型方法的类型参数由运行时决定。
**答案：错。** 正确表述：泛型方法的类型参数声明在返回类型之前（<T> T f(...)），由编译器按实参推断。。原因：推断规则在 JDK8 改进（目标类型推断）。

**Qjava-basics-1750（判断·语法语义）** 泛型方法必须显式指定类型参数。
**答案：错。** 正确表述：泛型方法的类型参数声明在返回类型之前（<T> T f(...)），由编译器按实参推断。。原因：推断规则在 JDK8 改进（目标类型推断）。

**Qjava-basics-1751（判断·语法语义）** 泛型方法与泛型类的类型参数必须同名。
**答案：错。** 正确表述：泛型方法的类型参数声明在返回类型之前（<T> T f(...)），由编译器按实参推断。。原因：推断规则在 JDK8 改进（目标类型推断）。

**Qjava-basics-1752（场景单选·语法语义）** 在工程实践中关于「泛型方法」，下列做法符合推荐实践的是？
- A. 泛型方法与泛型类的类型参数必须同名。
- B. 泛型方法必须显式指定类型参数。
- C. 泛型方法的类型参数由运行时决定。
- D. 静态泛型方法不能使用类的泛型参数——作用域不同。
**答案：D**
**解析：** 推荐实践：静态泛型方法不能使用类的泛型参数——作用域不同。。事实依据：泛型方法的类型参数声明在返回类型之前（<T> T f(...)），由编译器按实参推断。。

**Qjava-basics-1753（场景判断·语法语义）** 推荐实践：静态泛型方法不能使用类的泛型参数——作用域不同。
**答案：对。** 解析：泛型方法的类型参数声明在返回类型之前（<T> T f(...)），由编译器按实参推断。。原因：推断规则在 JDK8 改进（目标类型推断）。

**Qjava-basics-1754（填空·语法语义）** ______的类型参数声明在返回类型之前（<T> T f(...)），由编译器按实参推断。
**答案：泛型方法**。解析：推断规则在 JDK8 改进（目标类型推断）。

**Qjava-basics-1755（简答·语法语义）** 请说明「泛型」中泛型方法的机制与使用要点。
**要点（标准答案）**：① 泛型方法的类型参数声明在返回类型之前（<T> T f(...)），由编译器按实参推断。；② 原理：推断规则在 JDK8 改进（目标类型推断）。；③ 使用要点：静态泛型方法不能使用类的泛型参数——作用域不同。。版本锚点：JLS 8.4.4。

**Qjava-basics-1756（单选·正向·语法语义）** 关于「泛型」的说法，正确的是？
- A. 限定不影响可调用的方法集。
- B. 泛型可以同时继承多个类。
- C. <T extends Comparable<T>> 限定类型参数必须实现 Comparable——多重限定用 & 连接（T extends A & B）。
- D. 限定语法是 <T super Comparable>。
**答案：C**
**解析：** <T extends Comparable<T>> 限定类型参数必须实现 Comparable——多重限定用 & 连接（T extends A & B）。。原因：限定后可调用边界类型的方法；多重限定中最多一个类，其余为接口。。
**来源：** JB-092 · 泛型（JLS 4.5.1）

**Qjava-basics-1757（判断·语法语义）** <T extends Comparable<T>> 限定类型参数必须实现 Comparable——多重限定用 & 连接（T extends A & B）。
**答案：对。** 解析：限定后可调用边界类型的方法；多重限定中最多一个类，其余为接口。

**Qjava-basics-1758（判断·语法语义）** 泛型可以同时继承多个类。
**答案：错。** 正确表述：<T extends Comparable<T>> 限定类型参数必须实现 Comparable——多重限定用 & 连接（T extends A & B）。。原因：限定后可调用边界类型的方法；多重限定中最多一个类，其余为接口。

**Qjava-basics-1759（判断·语法语义）** 限定语法是 <T super Comparable>。
**答案：错。** 正确表述：<T extends Comparable<T>> 限定类型参数必须实现 Comparable——多重限定用 & 连接（T extends A & B）。。原因：限定后可调用边界类型的方法；多重限定中最多一个类，其余为接口。

**Qjava-basics-1760（判断·语法语义）** 限定不影响可调用的方法集。
**答案：错。** 正确表述：<T extends Comparable<T>> 限定类型参数必须实现 Comparable——多重限定用 & 连接（T extends A & B）。。原因：限定后可调用边界类型的方法；多重限定中最多一个类，其余为接口。

**Qjava-basics-1761（场景单选·语法语义）** 在工程实践中关于「上限限定」，下列做法符合推荐实践的是？
- A. 限定不影响可调用的方法集。
- B. 排序工具 sort(List<T extends Comparable>) 是标准例子。
- C. 限定语法是 <T super Comparable>。
- D. 泛型可以同时继承多个类。
**答案：B**
**解析：** 推荐实践：排序工具 sort(List<T extends Comparable>) 是标准例子。。事实依据：<T extends Comparable<T>> 限定类型参数必须实现 Comparable——多重限定用 & 连接（T extends A & B）。。

**Qjava-basics-1762（场景判断·语法语义）** 推荐实践：排序工具 sort(List<T extends Comparable>) 是标准例子。
**答案：对。** 解析：<T extends Comparable<T>> 限定类型参数必须实现 Comparable——多重限定用 & 连接（T extends A & B）。。原因：限定后可调用边界类型的方法；多重限定中最多一个类，其余为接口。

**Qjava-basics-1763（简答·语法语义）** 请说明「泛型」中上限限定的机制与使用要点。
**要点（标准答案）**：① <T extends Comparable<T>> 限定类型参数必须实现 Comparable——多重限定用 & 连接（T extends A & B）。；② 原理：限定后可调用边界类型的方法；多重限定中最多一个类，其余为接口。；③ 使用要点：排序工具 sort(List<T extends Comparable>) 是标准例子。。版本锚点：JLS 4.5.1。

**Qjava-basics-1764（单选·正向·误用）** 关于「异常」的说法，正确的是？
- A. getCause() 默认返回原始异常即使未传入。
- B. 新异常不需要携带原始异常。
- C. 构造新异常必须传入 cause（new Exception(msg, e)）保留根因链，否则堆栈断链无法溯源。
- D. cause 信息会自动继承无需传递。
**答案：C**
**解析：** 构造新异常必须传入 cause（new Exception(msg, e)）保留根因链，否则堆栈断链无法溯源。。原因：initCause 可事后补充；printStackTrace 会输出 Caused by 链。。
**来源：** JB-093 · 异常（JDK 1.4+（initCause））

**Qjava-basics-1765（判断·误用）** 构造新异常必须传入 cause（new Exception(msg, e)）保留根因链，否则堆栈断链无法溯源。
**答案：对。** 解析：initCause 可事后补充；printStackTrace 会输出 Caused by 链。

**Qjava-basics-1766（判断·误用）** 新异常不需要携带原始异常。
**答案：错。** 正确表述：构造新异常必须传入 cause（new Exception(msg, e)）保留根因链，否则堆栈断链无法溯源。。原因：initCause 可事后补充；printStackTrace 会输出 Caused by 链。

**Qjava-basics-1767（判断·误用）** cause 信息会自动继承无需传递。
**答案：错。** 正确表述：构造新异常必须传入 cause（new Exception(msg, e)）保留根因链，否则堆栈断链无法溯源。。原因：initCause 可事后补充；printStackTrace 会输出 Caused by 链。

**Qjava-basics-1768（判断·误用）** getCause() 默认返回原始异常即使未传入。
**答案：错。** 正确表述：构造新异常必须传入 cause（new Exception(msg, e)）保留根因链，否则堆栈断链无法溯源。。原因：initCause 可事后补充；printStackTrace 会输出 Caused by 链。

**Qjava-basics-1769（场景单选·误用）** 在工程实践中关于「异常链」，下列做法符合推荐实践的是？
- A. cause 信息会自动继承无需传递。
- B. getCause() 默认返回原始异常即使未传入。
- C. 日志规范：每个 catch 至少保留 cause 或堆栈。
- D. 新异常不需要携带原始异常。
**答案：C**
**解析：** 推荐实践：日志规范：每个 catch 至少保留 cause 或堆栈。。事实依据：构造新异常必须传入 cause（new Exception(msg, e)）保留根因链，否则堆栈断链无法溯源。。

**Qjava-basics-1770（场景判断·误用）** 推荐实践：日志规范：每个 catch 至少保留 cause 或堆栈。
**答案：对。** 解析：构造新异常必须传入 cause（new Exception(msg, e)）保留根因链，否则堆栈断链无法溯源。。原因：initCause 可事后补充；printStackTrace 会输出 Caused by 链。

**Qjava-basics-1771（简答·误用）** 请说明「异常」中异常链的机制与使用要点。
**要点（标准答案）**：① 构造新异常必须传入 cause（new Exception(msg, e)）保留根因链，否则堆栈断链无法溯源。；② 原理：initCause 可事后补充；printStackTrace 会输出 Caused by 链。；③ 使用要点：日志规范：每个 catch 至少保留 cause 或堆栈。。版本锚点：JDK 1.4+（initCause）。

**Qjava-basics-1772（单选·正向·误用）** 关于「异常」的说法，正确的是？
- A. 异常构造会填充堆栈（fillInStackTrace），高频路径用异常做流程控制有显著性能代价。
- B. fillInStackTrace 是可选项且默认关闭。
- C. 异常对象创建后堆栈不会变化。
- D. 异常抛出的性能开销可以忽略。
**答案：A**
**解析：** 异常构造会填充堆栈（fillInStackTrace），高频路径用异常做流程控制有显著性能代价。。原因：JVM 需要捕获当前线程栈快照。。
**来源：** JB-094 · 异常（JIT 通用）

**Qjava-basics-1773（判断·误用）** 异常构造会填充堆栈（fillInStackTrace），高频路径用异常做流程控制有显著性能代价。
**答案：对。** 解析：JVM 需要捕获当前线程栈快照。

**Qjava-basics-1774（判断·误用）** 异常抛出的性能开销可以忽略。
**答案：错。** 正确表述：异常构造会填充堆栈（fillInStackTrace），高频路径用异常做流程控制有显著性能代价。。原因：JVM 需要捕获当前线程栈快照。

**Qjava-basics-1775（判断·误用）** fillInStackTrace 是可选项且默认关闭。
**答案：错。** 正确表述：异常构造会填充堆栈（fillInStackTrace），高频路径用异常做流程控制有显著性能代价。。原因：JVM 需要捕获当前线程栈快照。

**Qjava-basics-1776（判断·误用）** 异常对象创建后堆栈不会变化。
**答案：错。** 正确表述：异常构造会填充堆栈（fillInStackTrace），高频路径用异常做流程控制有显著性能代价。。原因：JVM 需要捕获当前线程栈快照。

**Qjava-basics-1777（场景单选·误用）** 在工程实践中关于「异常性能」，下列做法符合推荐实践的是？
- A. 性能敏感路径用返回值/Optional 表达"未找到"，异常留给真正的异常。
- B. 异常对象创建后堆栈不会变化。
- C. fillInStackTrace 是可选项且默认关闭。
- D. 异常抛出的性能开销可以忽略。
**答案：A**
**解析：** 推荐实践：性能敏感路径用返回值/Optional 表达"未找到"，异常留给真正的异常。。事实依据：异常构造会填充堆栈（fillInStackTrace），高频路径用异常做流程控制有显著性能代价。。

**Qjava-basics-1778（场景判断·误用）** 推荐实践：性能敏感路径用返回值/Optional 表达"未找到"，异常留给真正的异常。
**答案：对。** 解析：异常构造会填充堆栈（fillInStackTrace），高频路径用异常做流程控制有显著性能代价。。原因：JVM 需要捕获当前线程栈快照。

**Qjava-basics-1779（简答·误用）** 请说明「异常」中异常性能的机制与使用要点。
**要点（标准答案）**：① 异常构造会填充堆栈（fillInStackTrace），高频路径用异常做流程控制有显著性能代价。；② 原理：JVM 需要捕获当前线程栈快照。；③ 使用要点：性能敏感路径用返回值/Optional 表达"未找到"，异常留给真正的异常。。版本锚点：JIT 通用。

**Qjava-basics-1780（单选·正向·语法语义）** 关于「集合通用」的说法，正确的是？
- A. Iterator.remove 之后必须立即 next。
- B. Iterator 的 remove() 是唯一安全的迭代中删除方式，且每次 next 后最多调用一次 remove。
- C. 可以在不调用 next 的情况下多次 remove。
- D. Iterator 的 remove 与集合的 remove 等价且安全。
**答案：B**
**解析：** Iterator 的 remove() 是唯一安全的迭代中删除方式，且每次 next 后最多调用一次 remove。。原因：连续 remove 两次抛 IllegalStateException。。
**来源：** JB-095 · 集合通用（Iterator javadoc）

**Qjava-basics-1781（判断·语法语义）** Iterator 的 remove() 是唯一安全的迭代中删除方式，且每次 next 后最多调用一次 remove。
**答案：对。** 解析：连续 remove 两次抛 IllegalStateException。

**Qjava-basics-1782（判断·语法语义）** 可以在不调用 next 的情况下多次 remove。
**答案：错。** 正确表述：Iterator 的 remove() 是唯一安全的迭代中删除方式，且每次 next 后最多调用一次 remove。。原因：连续 remove 两次抛 IllegalStateException。

**Qjava-basics-1783（判断·语法语义）** Iterator 的 remove 与集合的 remove 等价且安全。
**答案：错。** 正确表述：Iterator 的 remove() 是唯一安全的迭代中删除方式，且每次 next 后最多调用一次 remove。。原因：连续 remove 两次抛 IllegalStateException。

**Qjava-basics-1784（判断·语法语义）** Iterator.remove 之后必须立即 next。
**答案：错。** 正确表述：Iterator 的 remove() 是唯一安全的迭代中删除方式，且每次 next 后最多调用一次 remove。。原因：连续 remove 两次抛 IllegalStateException。

**Qjava-basics-1785（场景单选·语法语义）** 在工程实践中关于「Iterator契约」，下列做法符合推荐实践的是？
- A. "为什么设计 next 后才能 remove"是理解迭代器状态的切入点。
- B. 可以在不调用 next 的情况下多次 remove。
- C. Iterator 的 remove 与集合的 remove 等价且安全。
- D. Iterator.remove 之后必须立即 next。
**答案：A**
**解析：** 推荐实践："为什么设计 next 后才能 remove"是理解迭代器状态的切入点。。事实依据：Iterator 的 remove() 是唯一安全的迭代中删除方式，且每次 next 后最多调用一次 remove。。

**Qjava-basics-1786（场景判断·语法语义）** 推荐实践："为什么设计 next 后才能 remove"是理解迭代器状态的切入点。
**答案：对。** 解析：Iterator 的 remove() 是唯一安全的迭代中删除方式，且每次 next 后最多调用一次 remove。。原因：连续 remove 两次抛 IllegalStateException。

**Qjava-basics-1787（简答·语法语义）** 请说明「集合通用」中Iterator契约的机制与使用要点。
**要点（标准答案）**：① Iterator 的 remove() 是唯一安全的迭代中删除方式，且每次 next 后最多调用一次 remove。；② 原理：连续 remove 两次抛 IllegalStateException。；③ 使用要点："为什么设计 next 后才能 remove"是理解迭代器状态的切入点。。版本锚点：Iterator javadoc。

**Qjava-basics-1788（单选·正向·语法语义）** 关于「集合通用」的说法，正确的是？
- A. ArrayDeque 不支持栈操作。
- B. Deque 接口（ArrayDeque/LinkedList）同时支持栈（push/pop）与队列（offer/poll）两种语义，官方推荐替代 Stack 类。
- C. ArrayDeque 底层是链表。
- D. Stack 是 Java 中栈的推荐实现。
**答案：B**
**解析：** Deque 接口（ArrayDeque/LinkedList）同时支持栈（push/pop）与队列（offer/poll）两种语义，官方推荐替代 Stack 类。。原因：Stack 继承 Vector 是设计失误（全方法 synchronized + 允许随机访问违反栈语义）。。
**来源：** JB-096 · 集合通用（JDK 6+）

**Qjava-basics-1789（判断·语法语义）** Deque 接口（ArrayDeque/LinkedList）同时支持栈（push/pop）与队列（offer/poll）两种语义，官方推荐替代 Stack 类。
**答案：对。** 解析：Stack 继承 Vector 是设计失误（全方法 synchronized + 允许随机访问违反栈语义）。

**Qjava-basics-1790（判断·语法语义）** Stack 是 Java 中栈的推荐实现。
**答案：错。** 正确表述：Deque 接口（ArrayDeque/LinkedList）同时支持栈（push/pop）与队列（offer/poll）两种语义，官方推荐替代 Stack 类。。原因：Stack 继承 Vector 是设计失误（全方法 synchronized + 允许随机访问违反栈语义）。

**Qjava-basics-1791（判断·语法语义）** ArrayDeque 不支持栈操作。
**答案：错。** 正确表述：Deque 接口（ArrayDeque/LinkedList）同时支持栈（push/pop）与队列（offer/poll）两种语义，官方推荐替代 Stack 类。。原因：Stack 继承 Vector 是设计失误（全方法 synchronized + 允许随机访问违反栈语义）。

**Qjava-basics-1792（判断·语法语义）** ArrayDeque 底层是链表。
**答案：错。** 正确表述：Deque 接口（ArrayDeque/LinkedList）同时支持栈（push/pop）与队列（offer/poll）两种语义，官方推荐替代 Stack 类。。原因：Stack 继承 Vector 是设计失误（全方法 synchronized + 允许随机访问违反栈语义）。

**Qjava-basics-1793（场景单选·语法语义）** 在工程实践中关于「Deque双端」，下列做法符合推荐实践的是？
- A. Stack 是 Java 中栈的推荐实现。
- B. ArrayDeque 不支持栈操作。
- C. ArrayDeque 底层是链表。
- D. ArrayDeque 底层是循环数组，无容量限制自动扩容。
**答案：D**
**解析：** 推荐实践：ArrayDeque 底层是循环数组，无容量限制自动扩容。。事实依据：Deque 接口（ArrayDeque/LinkedList）同时支持栈（push/pop）与队列（offer/poll）两种语义，官方推荐替代 Stack 类。。

**Qjava-basics-1794（场景判断·语法语义）** 推荐实践：ArrayDeque 底层是循环数组，无容量限制自动扩容。
**答案：对。** 解析：Deque 接口（ArrayDeque/LinkedList）同时支持栈（push/pop）与队列（offer/poll）两种语义，官方推荐替代 Stack 类。。原因：Stack 继承 Vector 是设计失误（全方法 synchronized + 允许随机访问违反栈语义）。

**Qjava-basics-1795（简答·语法语义）** 请说明「集合通用」中Deque双端的机制与使用要点。
**要点（标准答案）**：① Deque 接口（ArrayDeque/LinkedList）同时支持栈（push/pop）与队列（offer/poll）两种语义，官方推荐替代 Stack 类。；② 原理：Stack 继承 Vector 是设计失误（全方法 synchronized + 允许随机访问违反栈语义）。；③ 使用要点：ArrayDeque 底层是循环数组，无容量限制自动扩容。。版本锚点：JDK 6+。

**Qjava-basics-1796（单选·正向·性能）** 关于「集合通用」的说法，正确的是？
- A. ArrayDeque 作为队列/栈的性能全面优于 LinkedList（无节点创建开销、内存连续）。
- B. ArrayDeque 有固定的容量上限。
- C. LinkedList 作为栈比 ArrayDeque 快。
- D. ArrayDeque 允许插入 null 元素。
**答案：A**
**解析：** ArrayDeque 作为队列/栈的性能全面优于 LinkedList（无节点创建开销、内存连续）。。原因：JDK 官方文档明确建议优先使用 ArrayDeque。。
**来源：** JB-097 · 集合通用（JDK 官方推荐（替代 Stack））

**Qjava-basics-1797（判断·性能）** ArrayDeque 作为队列/栈的性能全面优于 LinkedList（无节点创建开销、内存连续）。
**答案：对。** 解析：JDK 官方文档明确建议优先使用 ArrayDeque。

**Qjava-basics-1798（判断·性能）** LinkedList 作为栈比 ArrayDeque 快。
**答案：错。** 正确表述：ArrayDeque 作为队列/栈的性能全面优于 LinkedList（无节点创建开销、内存连续）。。原因：JDK 官方文档明确建议优先使用 ArrayDeque。

**Qjava-basics-1799（判断·性能）** ArrayDeque 有固定的容量上限。
**答案：错。** 正确表述：ArrayDeque 作为队列/栈的性能全面优于 LinkedList（无节点创建开销、内存连续）。。原因：JDK 官方文档明确建议优先使用 ArrayDeque。

**Qjava-basics-1800（判断·性能）** ArrayDeque 允许插入 null 元素。
**答案：错。** 正确表述：ArrayDeque 作为队列/栈的性能全面优于 LinkedList（无节点创建开销、内存连续）。。原因：JDK 官方文档明确建议优先使用 ArrayDeque。

**Qjava-basics-1801（场景单选·性能）** 在工程实践中关于「ArrayDeque」，下列做法符合推荐实践的是？
- A. ArrayDeque 允许插入 null 元素。
- B. ArrayDeque 有固定的容量上限。
- C. LinkedList 作为栈比 ArrayDeque 快。
- D. Deque 不允许 null（队列语义需要 null 哨兵判断 poll 失败）。
**答案：D**
**解析：** 推荐实践：Deque 不允许 null（队列语义需要 null 哨兵判断 poll 失败）。。事实依据：ArrayDeque 作为队列/栈的性能全面优于 LinkedList（无节点创建开销、内存连续）。。

**Qjava-basics-1802（场景判断·性能）** 推荐实践：Deque 不允许 null（队列语义需要 null 哨兵判断 poll 失败）。
**答案：对。** 解析：ArrayDeque 作为队列/栈的性能全面优于 LinkedList（无节点创建开销、内存连续）。。原因：JDK 官方文档明确建议优先使用 ArrayDeque。

**Qjava-basics-1803（填空·性能）** ______ 作为队列/栈的性能全面优于 LinkedList（无节点创建开销、内存连续）。
**答案：ArrayDeque**。解析：JDK 官方文档明确建议优先使用 ArrayDeque。

**Qjava-basics-1804（简答·性能）** 请说明「集合通用」中ArrayDeque的机制与使用要点。
**要点（标准答案）**：① ArrayDeque 作为队列/栈的性能全面优于 LinkedList（无节点创建开销、内存连续）。；② 原理：JDK 官方文档明确建议优先使用 ArrayDeque。；③ 使用要点：Deque 不允许 null（队列语义需要 null 哨兵判断 poll 失败）。。版本锚点：JDK 官方推荐（替代 Stack）。

**Qjava-basics-1805（单选·正向·版本）** 关于「语言杂项」的说法，正确的是？
- A. 文本块在 JDK8 就已可用。
- B. 文本块中的换行需要 \n 转义。
- C. 文本块内的双引号必须转义。
- D. JDK15 转正文本块（""" 三引号）：保留预期缩进、无需转义换行与引号。
**答案：D**
**解析：** JDK15 转正文本块（""" 三引号）：保留预期缩进、无需转义换行与引号。。原因：编译器处理附带缩进（incidental indentation）按最少缩进剥离。。
**来源：** JB-098 · 语言杂项（JDK15+）

**Qjava-basics-1806（判断·版本）** JDK15 转正文本块（""" 三引号）：保留预期缩进、无需转义换行与引号。
**答案：对。** 解析：编译器处理附带缩进（incidental indentation）按最少缩进剥离。

**Qjava-basics-1807（判断·版本）** 文本块中的换行需要 \n 转义。
**答案：错。** 正确表述：JDK15 转正文本块（""" 三引号）：保留预期缩进、无需转义换行与引号。。原因：编译器处理附带缩进（incidental indentation）按最少缩进剥离。

**Qjava-basics-1808（判断·版本）** 文本块内的双引号必须转义。
**答案：错。** 正确表述：JDK15 转正文本块（""" 三引号）：保留预期缩进、无需转义换行与引号。。原因：编译器处理附带缩进（incidental indentation）按最少缩进剥离。

**Qjava-basics-1809（判断·版本）** 文本块在 JDK8 就已可用。
**答案：错。** 正确表述：JDK15 转正文本块（""" 三引号）：保留预期缩进、无需转义换行与引号。。原因：编译器处理附带缩进（incidental indentation）按最少缩进剥离。

**Qjava-basics-1810（场景单选·版本）** 在工程实践中关于「文本块」，下列做法符合推荐实践的是？
- A. 文本块内的双引号必须转义。
- B. JSON/SQL/HTML 内嵌场景可读性大幅提升。
- C. 文本块在 JDK8 就已可用。
- D. 文本块中的换行需要 \n 转义。
**答案：B**
**解析：** 推荐实践：JSON/SQL/HTML 内嵌场景可读性大幅提升。。事实依据：JDK15 转正文本块（""" 三引号）：保留预期缩进、无需转义换行与引号。。

**Qjava-basics-1811（场景判断·版本）** 推荐实践：JSON/SQL/HTML 内嵌场景可读性大幅提升。
**答案：对。** 解析：JDK15 转正文本块（""" 三引号）：保留预期缩进、无需转义换行与引号。。原因：编译器处理附带缩进（incidental indentation）按最少缩进剥离。

**Qjava-basics-1812（填空·版本）** JDK15 转正______（""" 三引号）：保留预期缩进、无需转义换行与引号。
**答案：文本块**。解析：编译器处理附带缩进（incidental indentation）按最少缩进剥离。

**Qjava-basics-1813（简答·版本）** 请说明「语言杂项」中文本块的机制与使用要点。
**要点（标准答案）**：① JDK15 转正文本块（""" 三引号）：保留预期缩进、无需转义换行与引号。；② 原理：编译器处理附带缩进（incidental indentation）按最少缩进剥离。；③ 使用要点：JSON/SQL/HTML 内嵌场景可读性大幅提升。。版本锚点：JDK15+。

**Qjava-basics-1814（单选·正向·版本）** 关于「语言杂项」的说法，正确的是？
- A. var 使 Java 变成动态类型语言。
- B. var 可以用于方法参数与返回值。
- C. JDK10 var 局部变量类型推断（仅局部变量，不能用于字段/参数/返回值）；JDK21 switch 模式匹配转正。
- D. switch 模式匹配在 JDK8 已可用。
**答案：C**
**解析：** JDK10 var 局部变量类型推断（仅局部变量，不能用于字段/参数/返回值）；JDK21 switch 模式匹配转正。。原因：var 保留静态类型（编译期确定），不是动态类型。。
**来源：** JB-099 · 语言杂项（JDK10/JDK21）

**Qjava-basics-1815（判断·版本）** JDK10 var 局部变量类型推断（仅局部变量，不能用于字段/参数/返回值）；JDK21 switch 模式匹配转正。
**答案：对。** 解析：var 保留静态类型（编译期确定），不是动态类型。

**Qjava-basics-1816（判断·版本）** var 使 Java 变成动态类型语言。
**答案：错。** 正确表述：JDK10 var 局部变量类型推断（仅局部变量，不能用于字段/参数/返回值）；JDK21 switch 模式匹配转正。。原因：var 保留静态类型（编译期确定），不是动态类型。

**Qjava-basics-1817（判断·版本）** var 可以用于方法参数与返回值。
**答案：错。** 正确表述：JDK10 var 局部变量类型推断（仅局部变量，不能用于字段/参数/返回值）；JDK21 switch 模式匹配转正。。原因：var 保留静态类型（编译期确定），不是动态类型。

**Qjava-basics-1818（判断·版本）** switch 模式匹配在 JDK8 已可用。
**答案：错。** 正确表述：JDK10 var 局部变量类型推断（仅局部变量，不能用于字段/参数/返回值）；JDK21 switch 模式匹配转正。。原因：var 保留静态类型（编译期确定），不是动态类型。

**Qjava-basics-1819（场景单选·版本）** 在工程实践中关于「var与模式匹配」，下列做法符合推荐实践的是？
- A. var 适用于右侧类型明显的局部声明；字段/公共 API 不建议。
- B. var 使 Java 变成动态类型语言。
- C. switch 模式匹配在 JDK8 已可用。
- D. var 可以用于方法参数与返回值。
**答案：A**
**解析：** 推荐实践：var 适用于右侧类型明显的局部声明；字段/公共 API 不建议。。事实依据：JDK10 var 局部变量类型推断（仅局部变量，不能用于字段/参数/返回值）；JDK21 switch 模式匹配转正。。

**Qjava-basics-1820（场景判断·版本）** 推荐实践：var 适用于右侧类型明显的局部声明；字段/公共 API 不建议。
**答案：对。** 解析：JDK10 var 局部变量类型推断（仅局部变量，不能用于字段/参数/返回值）；JDK21 switch 模式匹配转正。。原因：var 保留静态类型（编译期确定），不是动态类型。

**Qjava-basics-1821（简答·版本）** 请说明「语言杂项」中var与模式匹配的机制与使用要点。
**要点（标准答案）**：① JDK10 var 局部变量类型推断（仅局部变量，不能用于字段/参数/返回值）；JDK21 switch 模式匹配转正。；② 原理：var 保留静态类型（编译期确定），不是动态类型。；③ 使用要点：var 适用于右侧类型明显的局部声明；字段/公共 API 不建议。。版本锚点：JDK10/JDK21。

**Qjava-basics-1822（单选·正向·语法语义）** 关于「String」的说法，正确的是？
- A. Java 用 UTF-8 编码字符串内部存储。
- B. emoji 的 length() 是 1。
- C. length() 对任何字符串都等于"可见字符数"。
- D. Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。
**答案：D**
**解析：** Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。。原因：length()/charAt 以代码单元为单位；码点操作用 codePointAt/codePointCount。。
**来源：** JB-100 · String（JDK 9+（Compact Strings））

**Qjava-basics-1823（判断·语法语义）** Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。
**答案：对。** 解析：length()/charAt 以代码单元为单位；码点操作用 codePointAt/codePointCount。

**Qjava-basics-1824（判断·语法语义）** length() 对任何字符串都等于"可见字符数"。
**答案：错。** 正确表述：Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。。原因：length()/charAt 以代码单元为单位；码点操作用 codePointAt/codePointCount。

**Qjava-basics-1825（判断·语法语义）** emoji 的 length() 是 1。
**答案：错。** 正确表述：Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。。原因：length()/charAt 以代码单元为单位；码点操作用 codePointAt/codePointCount。

**Qjava-basics-1826（判断·语法语义）** Java 用 UTF-8 编码字符串内部存储。
**答案：错。** 正确表述：Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。。原因：length()/charAt 以代码单元为单位；码点操作用 codePointAt/codePointCount。

**Qjava-basics-1827（场景单选·语法语义）** 在工程实践中关于「UTF16与码点」，下列做法符合推荐实践的是？
- A. length() 对任何字符串都等于"可见字符数"。
- B. 涉及 emoji 的截断必须按码点边界，否则产生非法字符。
- C. Java 用 UTF-8 编码字符串内部存储。
- D. emoji 的 length() 是 1。
**答案：B**
**解析：** 推荐实践：涉及 emoji 的截断必须按码点边界，否则产生非法字符。。事实依据：Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。。

**Qjava-basics-1828（场景判断·语法语义）** 推荐实践：涉及 emoji 的截断必须按码点边界，否则产生非法字符。
**答案：对。** 解析：Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。。原因：length()/charAt 以代码单元为单位；码点操作用 codePointAt/codePointCount。

**Qjava-basics-1829（简答·语法语义）** 请说明「String」中UTF16与码点的机制与使用要点。
**要点（标准答案）**：① Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。；② 原理：length()/charAt 以代码单元为单位；码点操作用 codePointAt/codePointCount。；③ 使用要点：涉及 emoji 的截断必须按码点边界，否则产生非法字符。。版本锚点：JDK 9+（Compact Strings）。

**Qjava-basics-1830（单选·正向·性能）** 关于「HashMap」的说法，正确的是？
- A. 树化对安全性没有意义。
- B. 树化的目的仅仅是提升正常场景的查询速度。
- C. 正常业务一定会触发树化。
- D. 树化把最坏查询从 O(n) 降到 O(log n)，防御 hash 碰撞攻击（恶意构造同 hash key）。
**答案：D**
**解析：** 树化把最坏查询从 O(n) 降到 O(log n)，防御 hash 碰撞攻击（恶意构造同 hash key）。。原因：Tomcat 曾因 hash 碰撞 DoS 加固——树化是安全加固不只是性能优化。。
**来源：** JB-101 · HashMap（JDK 8+ 源码）

**Qjava-basics-1831（判断·性能）** 树化把最坏查询从 O(n) 降到 O(log n)，防御 hash 碰撞攻击（恶意构造同 hash key）。
**答案：对。** 解析：Tomcat 曾因 hash 碰撞 DoS 加固——树化是安全加固不只是性能优化。

**Qjava-basics-1832（判断·性能）** 树化的目的仅仅是提升正常场景的查询速度。
**答案：错。** 正确表述：树化把最坏查询从 O(n) 降到 O(log n)，防御 hash 碰撞攻击（恶意构造同 hash key）。。原因：Tomcat 曾因 hash 碰撞 DoS 加固——树化是安全加固不只是性能优化。

**Qjava-basics-1833（判断·性能）** 树化对安全性没有意义。
**答案：错。** 正确表述：树化把最坏查询从 O(n) 降到 O(log n)，防御 hash 碰撞攻击（恶意构造同 hash key）。。原因：Tomcat 曾因 hash 碰撞 DoS 加固——树化是安全加固不只是性能优化。

**Qjava-basics-1834（判断·性能）** 正常业务一定会触发树化。
**答案：错。** 正确表述：树化把最坏查询从 O(n) 降到 O(log n)，防御 hash 碰撞攻击（恶意构造同 hash key）。。原因：Tomcat 曾因 hash 碰撞 DoS 加固——树化是安全加固不只是性能优化。

**Qjava-basics-1835（场景单选·性能）** 在工程实践中关于「树化收益」，下列做法符合推荐实践的是？
- A. 树化的目的仅仅是提升正常场景的查询速度。
- B. 树化对安全性没有意义。
- C. 正常负载下树化几乎不触发（泊松分布保证）。
- D. 正常业务一定会触发树化。
**答案：C**
**解析：** 推荐实践：正常负载下树化几乎不触发（泊松分布保证）。。事实依据：树化把最坏查询从 O(n) 降到 O(log n)，防御 hash 碰撞攻击（恶意构造同 hash key）。。

**Qjava-basics-1836（场景判断·性能）** 推荐实践：正常负载下树化几乎不触发（泊松分布保证）。
**答案：对。** 解析：树化把最坏查询从 O(n) 降到 O(log n)，防御 hash 碰撞攻击（恶意构造同 hash key）。。原因：Tomcat 曾因 hash 碰撞 DoS 加固——树化是安全加固不只是性能优化。

**Qjava-basics-1837（简答·性能）** 请说明「HashMap」中树化收益的机制与使用要点。
**要点（标准答案）**：① 树化把最坏查询从 O(n) 降到 O(log n)，防御 hash 碰撞攻击（恶意构造同 hash key）。；② 原理：Tomcat 曾因 hash 碰撞 DoS 加固——树化是安全加固不只是性能优化。；③ 使用要点：正常负载下树化几乎不触发（泊松分布保证）。。版本锚点：JDK 8+ 源码。

**Qjava-basics-1838（单选·正向·误用）** 关于「HashMap」的说法，正确的是？
- A. entrySet 遍历在 JDK8 后被废弃。
- B. entrySet 遍历（含 key/value）性能优于先 keySet 再 get（后者每 key 额外一次 hash 定位）。
- C. 只取 key 时也应使用 entrySet。
- D. keySet 再 get 与 entrySet 遍历性能完全相同。
**答案：B**
**解析：** entrySet 遍历（含 key/value）性能优于先 keySet 再 get（后者每 key 额外一次 hash 定位）。。原因：keySet().get(k) 重复走一遍 hash 定位。。
**来源：** JB-102 · HashMap（JDK 8+（entrySet 推荐））

**Qjava-basics-1839（判断·误用）** entrySet 遍历（含 key/value）性能优于先 keySet 再 get（后者每 key 额外一次 hash 定位）。
**答案：对。** 解析：keySet().get(k) 重复走一遍 hash 定位。

**Qjava-basics-1840（判断·误用）** keySet 再 get 与 entrySet 遍历性能完全相同。
**答案：错。** 正确表述：entrySet 遍历（含 key/value）性能优于先 keySet 再 get（后者每 key 额外一次 hash 定位）。。原因：keySet().get(k) 重复走一遍 hash 定位。

**Qjava-basics-1841（判断·误用）** entrySet 遍历在 JDK8 后被废弃。
**答案：错。** 正确表述：entrySet 遍历（含 key/value）性能优于先 keySet 再 get（后者每 key 额外一次 hash 定位）。。原因：keySet().get(k) 重复走一遍 hash 定位。

**Qjava-basics-1842（判断·误用）** 只取 key 时也应使用 entrySet。
**答案：错。** 正确表述：entrySet 遍历（含 key/value）性能优于先 keySet 再 get（后者每 key 额外一次 hash 定位）。。原因：keySet().get(k) 重复走一遍 hash 定位。

**Qjava-basics-1843（场景单选·误用）** 在工程实践中关于「遍历方式」，下列做法符合推荐实践的是？
- A. keySet 再 get 与 entrySet 遍历性能完全相同。
- B. JDK8 的 forEach 与 Stream 同样基于 entrySet 视图。
- C. 只取 key 时也应使用 entrySet。
- D. entrySet 遍历在 JDK8 后被废弃。
**答案：B**
**解析：** 推荐实践：JDK8 的 forEach 与 Stream 同样基于 entrySet 视图。。事实依据：entrySet 遍历（含 key/value）性能优于先 keySet 再 get（后者每 key 额外一次 hash 定位）。。

**Qjava-basics-1844（场景判断·误用）** 推荐实践：JDK8 的 forEach 与 Stream 同样基于 entrySet 视图。
**答案：对。** 解析：entrySet 遍历（含 key/value）性能优于先 keySet 再 get（后者每 key 额外一次 hash 定位）。。原因：keySet().get(k) 重复走一遍 hash 定位。

**Qjava-basics-1845（简答·误用）** 请说明「HashMap」中遍历方式的机制与使用要点。
**要点（标准答案）**：① entrySet 遍历（含 key/value）性能优于先 keySet 再 get（后者每 key 额外一次 hash 定位）。；② 原理：keySet().get(k) 重复走一遍 hash 定位。；③ 使用要点：JDK8 的 forEach 与 Stream 同样基于 entrySet 视图。。版本锚点：JDK 8+（entrySet 推荐）。

**Qjava-basics-1846（单选·正向·语法语义）** 关于「包装类」的说法，正确的是？
- A. valueOf 对大数值也返回缓存。
- B. new Integer 与 valueOf 语义完全等价且性能相同。
- C. Integer.valueOf(int) 对缓存范围返回缓存实例，new Integer(int) 总是新建对象（JDK9 起构造器废弃）。
- D. new Integer 在 JDK21 仍是推荐写法。
**答案：C**
**解析：** Integer.valueOf(int) 对缓存范围返回缓存实例，new Integer(int) 总是新建对象（JDK9 起构造器废弃）。。原因：官方文档明确推荐 valueOf 优先。。
**来源：** JB-103 · 包装类（JDK9+）

**Qjava-basics-1847（判断·语法语义）** Integer.valueOf(int) 对缓存范围返回缓存实例，new Integer(int) 总是新建对象（JDK9 起构造器废弃）。
**答案：对。** 解析：官方文档明确推荐 valueOf 优先。

**Qjava-basics-1848（判断·语法语义）** new Integer 与 valueOf 语义完全等价且性能相同。
**答案：错。** 正确表述：Integer.valueOf(int) 对缓存范围返回缓存实例，new Integer(int) 总是新建对象（JDK9 起构造器废弃）。。原因：官方文档明确推荐 valueOf 优先。

**Qjava-basics-1849（判断·语法语义）** valueOf 对大数值也返回缓存。
**答案：错。** 正确表述：Integer.valueOf(int) 对缓存范围返回缓存实例，new Integer(int) 总是新建对象（JDK9 起构造器废弃）。。原因：官方文档明确推荐 valueOf 优先。

**Qjava-basics-1850（判断·语法语义）** new Integer 在 JDK21 仍是推荐写法。
**答案：错。** 正确表述：Integer.valueOf(int) 对缓存范围返回缓存实例，new Integer(int) 总是新建对象（JDK9 起构造器废弃）。。原因：官方文档明确推荐 valueOf 优先。

**Qjava-basics-1851（场景单选·语法语义）** 在工程实践中关于「valueOf契约」，下列做法符合推荐实践的是？
- A. new Integer 在 JDK21 仍是推荐写法。
- B. new Integer 与 valueOf 语义完全等价且性能相同。
- C. valueOf 对大数值也返回缓存。
- D. JDK9+ @Deprecated(since=9, forRemoval=true)。
**答案：D**
**解析：** 推荐实践：JDK9+ @Deprecated(since=9, forRemoval=true)。。事实依据：Integer.valueOf(int) 对缓存范围返回缓存实例，new Integer(int) 总是新建对象（JDK9 起构造器废弃）。。

**Qjava-basics-1852（场景判断·语法语义）** 推荐实践：JDK9+ @Deprecated(since=9, forRemoval=true)。
**答案：对。** 解析：Integer.valueOf(int) 对缓存范围返回缓存实例，new Integer(int) 总是新建对象（JDK9 起构造器废弃）。。原因：官方文档明确推荐 valueOf 优先。

**Qjava-basics-1853（简答·语法语义）** 请说明「包装类」中valueOf契约的机制与使用要点。
**要点（标准答案）**：① Integer.valueOf(int) 对缓存范围返回缓存实例，new Integer(int) 总是新建对象（JDK9 起构造器废弃）。；② 原理：官方文档明确推荐 valueOf 优先。；③ 使用要点：JDK9+ @Deprecated(since=9, forRemoval=true)。。版本锚点：JDK9+。

**Qjava-basics-1854（单选·正向·误用）** 关于「String」的说法，正确的是？
- A. 任何字符串拼接都会在编译期折叠。
- B. 常量折叠只发生在运行期。
- C. final 变量拼接也不能折叠。
- D. 两个编译期常量拼接（final String a="x"; String s=a+"y";）在编译期直接折叠为常量；含变量的拼接只能运行期计算。
**答案：D**
**解析：** 两个编译期常量拼接（final String a="x"; String s=a+"y";）在编译期直接折叠为常量；含变量的拼接只能运行期计算。。原因：常量折叠是编译器优化，变量拼接无法折叠。。
**来源：** JB-104 · String（JLS 15.28）

**Qjava-basics-1855（判断·误用）** 两个编译期常量拼接（final String a="x"; String s=a+"y";）在编译期直接折叠为常量；含变量的拼接只能运行期计算。
**答案：对。** 解析：常量折叠是编译器优化，变量拼接无法折叠。

**Qjava-basics-1856（判断·误用）** 任何字符串拼接都会在编译期折叠。
**答案：错。** 正确表述：两个编译期常量拼接（final String a="x"; String s=a+"y";）在编译期直接折叠为常量；含变量的拼接只能运行期计算。。原因：常量折叠是编译器优化，变量拼接无法折叠。

**Qjava-basics-1857（判断·误用）** final 变量拼接也不能折叠。
**答案：错。** 正确表述：两个编译期常量拼接（final String a="x"; String s=a+"y";）在编译期直接折叠为常量；含变量的拼接只能运行期计算。。原因：常量折叠是编译器优化，变量拼接无法折叠。

**Qjava-basics-1858（判断·误用）** 常量折叠只发生在运行期。
**答案：错。** 正确表述：两个编译期常量拼接（final String a="x"; String s=a+"y";）在编译期直接折叠为常量；含变量的拼接只能运行期计算。。原因：常量折叠是编译器优化，变量拼接无法折叠。

**Qjava-basics-1859（场景单选·误用）** 在工程实践中关于「常量折叠」，下列做法符合推荐实践的是？
- A. 可验证：折叠后的 s == "xy" 为 true（同池引用）。
- B. 任何字符串拼接都会在编译期折叠。
- C. final 变量拼接也不能折叠。
- D. 常量折叠只发生在运行期。
**答案：A**
**解析：** 推荐实践：可验证：折叠后的 s == "xy" 为 true（同池引用）。。事实依据：两个编译期常量拼接（final String a="x"; String s=a+"y";）在编译期直接折叠为常量；含变量的拼接只能运行期计算。。

**Qjava-basics-1860（场景判断·误用）** 推荐实践：可验证：折叠后的 s == "xy" 为 true（同池引用）。
**答案：对。** 解析：两个编译期常量拼接（final String a="x"; String s=a+"y";）在编译期直接折叠为常量；含变量的拼接只能运行期计算。。原因：常量折叠是编译器优化，变量拼接无法折叠。

**Qjava-basics-1861（简答·误用）** 请说明「String」中常量折叠的机制与使用要点。
**要点（标准答案）**：① 两个编译期常量拼接（final String a="x"; String s=a+"y";）在编译期直接折叠为常量；含变量的拼接只能运行期计算。；② 原理：常量折叠是编译器优化，变量拼接无法折叠。；③ 使用要点：可验证：折叠后的 s == "xy" 为 true（同池引用）。。版本锚点：JLS 15.28。

**Qjava-basics-1862（单选·正向·线程）** 关于「String」的说法，正确的是？
- A. String 拼接在多线程下会损坏数据。
- B. String 赋值存在竞态条件。
- C. String 共享需要 volatile 修饰才可见。
- D. String 作为字段在多线程间共享无需同步：不可变对象天然线程安全且可安全发布。
**答案：D**
**解析：** String 作为字段在多线程间共享无需同步：不可变对象天然线程安全且可安全发布。。原因：final 字段 + 不可变语义获得 JMM 安全发布保证。。
**来源：** JB-105 · String（JLS 17.5（不可变））

**Qjava-basics-1863（判断·线程）** String 作为字段在多线程间共享无需同步：不可变对象天然线程安全且可安全发布。
**答案：对。** 解析：final 字段 + 不可变语义获得 JMM 安全发布保证。

**Qjava-basics-1864（判断·线程）** String 共享需要 volatile 修饰才可见。
**答案：错。** 正确表述：String 作为字段在多线程间共享无需同步：不可变对象天然线程安全且可安全发布。。原因：final 字段 + 不可变语义获得 JMM 安全发布保证。

**Qjava-basics-1865（判断·线程）** String 赋值存在竞态条件。
**答案：错。** 正确表述：String 作为字段在多线程间共享无需同步：不可变对象天然线程安全且可安全发布。。原因：final 字段 + 不可变语义获得 JMM 安全发布保证。

**Qjava-basics-1866（判断·线程）** String 拼接在多线程下会损坏数据。
**答案：错。** 正确表述：String 作为字段在多线程间共享无需同步：不可变对象天然线程安全且可安全发布。。原因：final 字段 + 不可变语义获得 JMM 安全发布保证。

**Qjava-basics-1867（场景单选·线程）** 在工程实践中关于「安全共享」，下列做法符合推荐实践的是？
- A. String 共享需要 volatile 修饰才可见。
- B. 不可变对象是并发设计的默认选择（JCiP 原则）。
- C. String 赋值存在竞态条件。
- D. String 拼接在多线程下会损坏数据。
**答案：B**
**解析：** 推荐实践：不可变对象是并发设计的默认选择（JCiP 原则）。。事实依据：String 作为字段在多线程间共享无需同步：不可变对象天然线程安全且可安全发布。。

**Qjava-basics-1868（场景判断·线程）** 推荐实践：不可变对象是并发设计的默认选择（JCiP 原则）。
**答案：对。** 解析：String 作为字段在多线程间共享无需同步：不可变对象天然线程安全且可安全发布。。原因：final 字段 + 不可变语义获得 JMM 安全发布保证。

**Qjava-basics-1869（简答·线程）** 请说明「String」中安全共享的机制与使用要点。
**要点（标准答案）**：① String 作为字段在多线程间共享无需同步：不可变对象天然线程安全且可安全发布。；② 原理：final 字段 + 不可变语义获得 JMM 安全发布保证。；③ 使用要点：不可变对象是并发设计的默认选择（JCiP 原则）。。版本锚点：JLS 17.5（不可变）。

**Qjava-basics-1870（单选·正向·语法语义）** 关于「CHM」的说法，正确的是？
- A. computeIfAbsent(key, k->新值) 原子地"不存在则计算并放入"，是并发缓存的标准实现。
- B. computeIfAbsent 在 JDK7 就存在。
- C. computeIfAbsent 的映射函数可以返回 null 且会存入 null。
- D. computeIfAbsent 与 get 后 put 等价。
**答案：A**
**解析：** computeIfAbsent(key, k->新值) 原子地"不存在则计算并放入"，是并发缓存的标准实现。。原因：check-then-act 两步在并发下有竞态窗口。。
**来源：** JB-106 · CHM（JDK 8+）

**Qjava-basics-1871（判断·语法语义）** computeIfAbsent(key, k->新值) 原子地"不存在则计算并放入"，是并发缓存的标准实现。
**答案：对。** 解析：check-then-act 两步在并发下有竞态窗口。

**Qjava-basics-1872（判断·语法语义）** computeIfAbsent 与 get 后 put 等价。
**答案：错。** 正确表述：computeIfAbsent(key, k->新值) 原子地"不存在则计算并放入"，是并发缓存的标准实现。。原因：check-then-act 两步在并发下有竞态窗口。

**Qjava-basics-1873（判断·语法语义）** computeIfAbsent 的映射函数可以返回 null 且会存入 null。
**答案：错。** 正确表述：computeIfAbsent(key, k->新值) 原子地"不存在则计算并放入"，是并发缓存的标准实现。。原因：check-then-act 两步在并发下有竞态窗口。

**Qjava-basics-1874（判断·语法语义）** computeIfAbsent 在 JDK7 就存在。
**答案：错。** 正确表述：computeIfAbsent(key, k->新值) 原子地"不存在则计算并放入"，是并发缓存的标准实现。。原因：check-then-act 两步在并发下有竞态窗口。

**Qjava-basics-1875（场景单选·语法语义）** 在工程实践中关于「computeIfAbsent」，下列做法符合推荐实践的是？
- A. 映射函数返回 null 则不建立映射；函数内再操作同 map 有递归更新风险（JDK9 文档明确）。
- B. computeIfAbsent 与 get 后 put 等价。
- C. computeIfAbsent 在 JDK7 就存在。
- D. computeIfAbsent 的映射函数可以返回 null 且会存入 null。
**答案：A**
**解析：** 推荐实践：映射函数返回 null 则不建立映射；函数内再操作同 map 有递归更新风险（JDK9 文档明确）。。事实依据：computeIfAbsent(key, k->新值) 原子地"不存在则计算并放入"，是并发缓存的标准实现。。

**Qjava-basics-1876（场景判断·语法语义）** 推荐实践：映射函数返回 null 则不建立映射；函数内再操作同 map 有递归更新风险（JDK9 文档明确）。
**答案：对。** 解析：computeIfAbsent(key, k->新值) 原子地"不存在则计算并放入"，是并发缓存的标准实现。。原因：check-then-act 两步在并发下有竞态窗口。

**Qjava-basics-1877（填空·语法语义）** ______(key, k->新值) 原子地"不存在则计算并放入"，是并发缓存的标准实现。
**答案：computeIfAbsent**。解析：check-then-act 两步在并发下有竞态窗口。

**Qjava-basics-1878（简答·语法语义）** 请说明「CHM」中computeIfAbsent的机制与使用要点。
**要点（标准答案）**：① computeIfAbsent(key, k->新值) 原子地"不存在则计算并放入"，是并发缓存的标准实现。；② 原理：check-then-act 两步在并发下有竞态窗口。；③ 使用要点：映射函数返回 null 则不建立映射；函数内再操作同 map 有递归更新风险（JDK9 文档明确）。。版本锚点：JDK 8+。

**Qjava-basics-1879（单选·正向·语法语义）** 关于「HashMap」的说法，正确的是？
- A. new HashMap<>(initialCapacity) 的实际容量是 tableSizeFor(initialCapacity)（向上取 2 的幂），且首次 put 才分配。
- B. new HashMap<>(100) 的表长就是 100。
- C. 传入的 initialCapacity 会被原样用作表长。
- D. 传入 100 实际表长是 128 是因为内存对齐。
**答案：A**
**解析：** new HashMap<>(initialCapacity) 的实际容量是 tableSizeFor(initialCapacity)（向上取 2 的幂），且首次 put 才分配。。原因：预期存 n 个元素应设 initialCapacity = n/0.75 + 1 避免扩容。。
**来源：** JB-107 · HashMap（JDK 文档）

**Qjava-basics-1880（判断·语法语义）** new HashMap<>(initialCapacity) 的实际容量是 tableSizeFor(initialCapacity)（向上取 2 的幂），且首次 put 才分配。
**答案：对。** 解析：预期存 n 个元素应设 initialCapacity = n/0.75 + 1 避免扩容。

**Qjava-basics-1881（判断·语法语义）** new HashMap<>(100) 的表长就是 100。
**答案：错。** 正确表述：new HashMap<>(initialCapacity) 的实际容量是 tableSizeFor(initialCapacity)（向上取 2 的幂），且首次 put 才分配。。原因：预期存 n 个元素应设 initialCapacity = n/0.75 + 1 避免扩容。

**Qjava-basics-1882（判断·语法语义）** 传入的 initialCapacity 会被原样用作表长。
**答案：错。** 正确表述：new HashMap<>(initialCapacity) 的实际容量是 tableSizeFor(initialCapacity)（向上取 2 的幂），且首次 put 才分配。。原因：预期存 n 个元素应设 initialCapacity = n/0.75 + 1 避免扩容。

**Qjava-basics-1883（判断·语法语义）** 传入 100 实际表长是 128 是因为内存对齐。
**答案：错。** 正确表述：new HashMap<>(initialCapacity) 的实际容量是 tableSizeFor(initialCapacity)（向上取 2 的幂），且首次 put 才分配。。原因：预期存 n 个元素应设 initialCapacity = n/0.75 + 1 避免扩容。

**Qjava-basics-1884（场景单选·语法语义）** 在工程实践中关于「initialCapacity」，下列做法符合推荐实践的是？
- A. 传入的 initialCapacity 会被原样用作表长。
- B. new HashMap<>(100) 的表长就是 100。
- C. 传入 100 实际表长是 128 是因为内存对齐。
- D. 本机实测：new HashMap<>(100) 首插后 table.length=128。
**答案：D**
**解析：** 推荐实践：本机实测：new HashMap<>(100) 首插后 table.length=128。。事实依据：new HashMap<>(initialCapacity) 的实际容量是 tableSizeFor(initialCapacity)（向上取 2 的幂），且首次 put 才分配。。

**Qjava-basics-1885（场景判断·语法语义）** 推荐实践：本机实测：new HashMap<>(100) 首插后 table.length=128。
**答案：对。** 解析：new HashMap<>(initialCapacity) 的实际容量是 tableSizeFor(initialCapacity)（向上取 2 的幂），且首次 put 才分配。。原因：预期存 n 个元素应设 initialCapacity = n/0.75 + 1 避免扩容。

**Qjava-basics-1886（填空·语法语义）** new HashMap<>(______) 的实际容量是 tableSizeFor(initialCapacity)（向上取 2 的幂），且首次 put 才分配。
**答案：initialCapacity**。解析：预期存 n 个元素应设 initialCapacity = n/0.75 + 1 避免扩容。

**Qjava-basics-1887（简答·语法语义）** 请说明「HashMap」中initialCapacity的机制与使用要点。
**要点（标准答案）**：① new HashMap<>(initialCapacity) 的实际容量是 tableSizeFor(initialCapacity)（向上取 2 的幂），且首次 put 才分配。；② 原理：预期存 n 个元素应设 initialCapacity = n/0.75 + 1 避免扩容。；③ 使用要点：本机实测：new HashMap<>(100) 首插后 table.length=128。。版本锚点：JDK 文档。

**Qjava-basics-1888（单选·正向·误用）** 关于「包装类」的说法，正确的是？
- A. 两者返回类型相同可混用无影响。
- B. valueOf 不接受字符串参数。
- C. Integer.parseInt 返回基本类型 int，Integer.valueOf 返回包装类 Integer——按需求选择。
- D. parseInt 返回 Integer。
**答案：C**
**解析：** Integer.parseInt 返回基本类型 int，Integer.valueOf 返回包装类 Integer——按需求选择。。原因：parse 无装箱开销；valueOf 有缓存。。
**来源：** JB-108 · 包装类（各包装类 javadoc）

**Qjava-basics-1889（判断·误用）** Integer.parseInt 返回基本类型 int，Integer.valueOf 返回包装类 Integer——按需求选择。
**答案：对。** 解析：parse 无装箱开销；valueOf 有缓存。

**Qjava-basics-1890（判断·误用）** 两者返回类型相同可混用无影响。
**答案：错。** 正确表述：Integer.parseInt 返回基本类型 int，Integer.valueOf 返回包装类 Integer——按需求选择。。原因：parse 无装箱开销；valueOf 有缓存。

**Qjava-basics-1891（判断·误用）** parseInt 返回 Integer。
**答案：错。** 正确表述：Integer.parseInt 返回基本类型 int，Integer.valueOf 返回包装类 Integer——按需求选择。。原因：parse 无装箱开销；valueOf 有缓存。

**Qjava-basics-1892（判断·误用）** valueOf 不接受字符串参数。
**答案：错。** 正确表述：Integer.parseInt 返回基本类型 int，Integer.valueOf 返回包装类 Integer——按需求选择。。原因：parse 无装箱开销；valueOf 有缓存。

**Qjava-basics-1893（场景单选·误用）** 在工程实践中关于「parse与valueOf」，下列做法符合推荐实践的是？
- A. 两者返回类型相同可混用无影响。
- B. valueOf 不接受字符串参数。
- C. parseInt 返回 Integer。
- D. 高频解析场景 parseInt 更优（无装箱）。
**答案：D**
**解析：** 推荐实践：高频解析场景 parseInt 更优（无装箱）。。事实依据：Integer.parseInt 返回基本类型 int，Integer.valueOf 返回包装类 Integer——按需求选择。。

**Qjava-basics-1894（场景判断·误用）** 推荐实践：高频解析场景 parseInt 更优（无装箱）。
**答案：对。** 解析：Integer.parseInt 返回基本类型 int，Integer.valueOf 返回包装类 Integer——按需求选择。。原因：parse 无装箱开销；valueOf 有缓存。

**Qjava-basics-1895（简答·误用）** 请说明「包装类」中parse与valueOf的机制与使用要点。
**要点（标准答案）**：① Integer.parseInt 返回基本类型 int，Integer.valueOf 返回包装类 Integer——按需求选择。；② 原理：parse 无装箱开销；valueOf 有缓存。；③ 使用要点：高频解析场景 parseInt 更优（无装箱）。。版本锚点：各包装类 javadoc。

**Qjava-basics-1896（单选·正向·语法语义）** 关于「异常」的说法，正确的是？
- A. 浮点数除以零会抛 ArithmeticException。
- B. 所有运行时异常都必须捕获。
- C. 高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。
- D. NumberFormatException 属于 Checked 异常。
**答案：C**
**解析：** 高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。。原因：整数除零抛异常而浮点除零得 Infinity/NaN——IEEE754 规范行为。。
**来源：** JB-109 · 异常（JDK 文档）

**Qjava-basics-1897（判断·语法语义）** 高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。
**答案：对。** 解析：整数除零抛异常而浮点除零得 Infinity/NaN——IEEE754 规范行为。

**Qjava-basics-1898（判断·语法语义）** 浮点数除以零会抛 ArithmeticException。
**答案：错。** 正确表述：高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。。原因：整数除零抛异常而浮点除零得 Infinity/NaN——IEEE754 规范行为。

**Qjava-basics-1899（判断·语法语义）** NumberFormatException 属于 Checked 异常。
**答案：错。** 正确表述：高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。。原因：整数除零抛异常而浮点除零得 Infinity/NaN——IEEE754 规范行为。

**Qjava-basics-1900（判断·语法语义）** 所有运行时异常都必须捕获。
**答案：错。** 正确表述：高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。。原因：整数除零抛异常而浮点除零得 Infinity/NaN——IEEE754 规范行为。

**Qjava-basics-1901（场景单选·语法语义）** 在工程实践中关于「异常分类速查」，下列做法符合推荐实践的是？
- A. 所有运行时异常都必须捕获。
- B. NumberFormat 的 message 通常包含导致失败的字符串——排查入口。
- C. 浮点数除以零会抛 ArithmeticException。
- D. NumberFormatException 属于 Checked 异常。
**答案：B**
**解析：** 推荐实践：NumberFormat 的 message 通常包含导致失败的字符串——排查入口。。事实依据：高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。。

**Qjava-basics-1902（场景判断·语法语义）** 推荐实践：NumberFormat 的 message 通常包含导致失败的字符串——排查入口。
**答案：对。** 解析：高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。。原因：整数除零抛异常而浮点除零得 Infinity/NaN——IEEE754 规范行为。

**Qjava-basics-1903（简答·语法语义）** 请说明「异常」中异常分类速查的机制与使用要点。
**要点（标准答案）**：① 高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。；② 原理：整数除零抛异常而浮点除零得 Infinity/NaN——IEEE754 规范行为。；③ 使用要点：NumberFormat 的 message 通常包含导致失败的字符串——排查入口。。版本锚点：JDK 文档。

**Qjava-basics-1904（单选·正向·内存）** 关于「String」的说法，正确的是？
- A. 去重只对 intern 池的字符串生效。
- B. JDK8u20+ 提供 -XX:+UseStringDeduplication（G1 专属）：后台去重相同内容的 String 底层数组。
- C. 字符串去重会修改 String 的内容。
- D. 字符串去重默认开启。
**答案：B**
**解析：** JDK8u20+ 提供 -XX:+UseStringDeduplication（G1 专属）：后台去重相同内容的 String 底层数组。。原因：适用于大量重复长字符串（如缓存 JSON）场景。。
**来源：** JB-110 · String（JDK8u20+ / G1）

**Qjava-basics-1905（判断·内存）** JDK8u20+ 提供 -XX:+UseStringDeduplication（G1 专属）：后台去重相同内容的 String 底层数组。
**答案：对。** 解析：适用于大量重复长字符串（如缓存 JSON）场景。

**Qjava-basics-1906（判断·内存）** 字符串去重默认开启。
**答案：错。** 正确表述：JDK8u20+ 提供 -XX:+UseStringDeduplication（G1 专属）：后台去重相同内容的 String 底层数组。。原因：适用于大量重复长字符串（如缓存 JSON）场景。

**Qjava-basics-1907（判断·内存）** 字符串去重会修改 String 的内容。
**答案：错。** 正确表述：JDK8u20+ 提供 -XX:+UseStringDeduplication（G1 专属）：后台去重相同内容的 String 底层数组。。原因：适用于大量重复长字符串（如缓存 JSON）场景。

**Qjava-basics-1908（判断·内存）** 去重只对 intern 池的字符串生效。
**答案：错。** 正确表述：JDK8u20+ 提供 -XX:+UseStringDeduplication（G1 专属）：后台去重相同内容的 String 底层数组。。原因：适用于大量重复长字符串（如缓存 JSON）场景。

**Qjava-basics-1909（场景单选·内存）** 在工程实践中关于「字符串去重」，下列做法符合推荐实践的是？
- A. 去重只对 intern 池的字符串生效。
- B. 字符串去重默认开启。
- C. 字符串去重会修改 String 的内容。
- D. 开启前需评估 CPU 开销与实际重复率。
**答案：D**
**解析：** 推荐实践：开启前需评估 CPU 开销与实际重复率。。事实依据：JDK8u20+ 提供 -XX:+UseStringDeduplication（G1 专属）：后台去重相同内容的 String 底层数组。。

**Qjava-basics-1910（场景判断·内存）** 推荐实践：开启前需评估 CPU 开销与实际重复率。
**答案：对。** 解析：JDK8u20+ 提供 -XX:+UseStringDeduplication（G1 专属）：后台去重相同内容的 String 底层数组。。原因：适用于大量重复长字符串（如缓存 JSON）场景。

**Qjava-basics-1911（简答·内存）** 请说明「String」中字符串去重的机制与使用要点。
**要点（标准答案）**：① JDK8u20+ 提供 -XX:+UseStringDeduplication（G1 专属）：后台去重相同内容的 String 底层数组。；② 原理：适用于大量重复长字符串（如缓存 JSON）场景。；③ 使用要点：开启前需评估 CPU 开销与实际重复率。。版本锚点：JDK8u20+ / G1。

**Qjava-basics-1912（单选·反向·String）** 以下关于「String」的说法，**错误**的是？
- A. String 的 hashCode 在首次计算后缓存到内部 hash 字段，后续调用直接返回缓存值。
- B. String 提供 setCharAt 方法可以原地修改字符。
- C. String 是不可变类：内部 value 数组为 final 且不提供修改方法。
- D. 字符串常量池从 JDK7 起位于堆中，JDK6 及之前位于永久代。
**答案：B**
**解析：** 正确表述应为——String 是不可变类：内部 value 数组为 final 且不提供修改方法。。原因：不可变保证常量池安全共享、hashCode 可缓存、天然线程安全。。

**Qjava-basics-1913（单选·反向·包装类）** 以下关于「包装类」的说法，**错误**的是？
- A. Integer/Long/Short/Byte 的缓存范围是 -128~127，Character 是 0~127，Boolean 缓存 true/false。
- B. Long 类型用 == 比较，超出缓存范围（-128~127）时即使值相等也返回 false。
- C. 所有整数值的包装类都有缓存。
- D. 对值为 null 的包装类做自动拆箱会抛 NullPointerException。
**答案：C**
**解析：** 正确表述应为——Integer/Long/Short/Byte 的缓存范围是 -128~127，Character 是 0~127，Boolean 缓存 true/false。。原因：缓存由 valueOf 触发，超出范围的值每次都新建对象。。

**Qjava-basics-1914（单选·反向·equals体系）** 以下关于「equals体系」的说法，**错误**的是？
- A. 重写 equals 不重写 hashCode 会导致该对象在 HashMap/HashSet 中"找不到"。
- B. equals 只需要满足对称性。
- C. 重写 equals 必须满足自反、对称、传递、一致、非空（对 null 返回 false）五条。
- D. hashCode 计算选用 31 作乘数：奇素数散列分布好，且 31*i 可被 JVM 优化为 (i<<5)-i。
**答案：B**
**解析：** 正确表述应为——重写 equals 必须满足自反、对称、传递、一致、非空（对 null 返回 false）五条。。原因：违反任何一条都会导致该对象在集合中的行为异常。。

**Qjava-basics-1915（单选·反向·ArrayList）** 以下关于「ArrayList」的说法，**错误**的是？
- A. new ArrayList() 立即分配容量为 10 的数组。
- B. ArrayList get(i) 是 O(1)（数组直接寻址），LinkedList get(i) 是 O(n)。
- C. new ArrayList() 不分配数组，首次 add 时才分配容量 10 的数组。
- D. ArrayList 扩容为新容量的 1.5 倍（oldCapacity + oldCapacity >> 1）：10→15→22。
**答案：A**
**解析：** 正确表述应为——new ArrayList() 不分配数组，首次 add 时才分配容量 10 的数组。。原因：节省空集合的内存占用。。

**Qjava-basics-1916（单选·反向·HashMap）** 以下关于「HashMap」的说法，**错误**的是？
- A. new HashMap() 首次 put 分配容量 12 的表。
- B. HashMap 用 (h = key.hashCode()) ^ (h >>> 16) 做扰动，让高位参与低位运算。
- C. HashMap 元素数超过 threshold（容量×0.75）时扩容为原来的 2 倍并重排元素。
- D. new HashMap<>() 首次 put 时分配容量 16 的表（threshold=12）。
**答案：A**
**解析：** 正确表述应为——new HashMap<>() 首次 put 时分配容量 16 的表（threshold=12）。。原因：16 是 2 的幂，支撑 (n-1)&hash 定位；0.75 负载下 12 个即扩容。。

**Qjava-basics-1917（单选·反向·CHM）** 以下关于「CHM」的说法，**错误**的是？
- A. JDK8 的 ConcurrentHashMap 用 CAS + synchronized 锁单个桶头节点实现线程安全。
- B. ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。
- C. CHM 的 size 通过 baseCount + CounterCell[] 分段计数，返回的是近似值。
- D. JDK8 的 CHM 全表只有一把全局锁。
**答案：D**
**解析：** 正确表述应为——JDK8 的 ConcurrentHashMap 用 CAS + synchronized 锁单个桶头节点实现线程安全。。原因：锁粒度细到桶级，冲突概率低时 synchronized（锁升级后）开销小且免额外内存。。

**Qjava-basics-1918（单选·反向·泛型）** 以下关于「泛型」的说法，**错误**的是？
- A. Java 泛型是编译期检查、运行时擦除：List<String> 与 List<Integer> 运行时是同一个类。
- B. 通配符原则 PECS：Producer Extends（只读用 ? extends）、Consumer Super（只写用 ? super）。
- C. 类型擦除导致：不能 new T()、不能 new T[]、不能 instanceof T、静态成员不能用类的泛型参数。
- D. List<String> 运行时携带 String 类型信息。
**答案：D**
**解析：** 正确表述应为——Java 泛型是编译期检查、运行时擦除：List<String> 与 List<Integer> 运行时是同一个类。。原因：向后兼容 JDK5 之前的字节码；泛型信息仅保留在 Signature 属性供反射读取。。

**Qjava-basics-1919（单选·反向·异常）** 以下关于「异常」的说法，**错误**的是？
- A. finally 块在 try/catch 之后必然执行（除非 JVM 退出或线程死亡），且其中的 return 会覆盖 try/catch 的返回值与异常。
- B. IOException 是 RuntimeException 的子类。
- C. Checked 异常编译期强制处理，RuntimeException 及其子类不强制。
- D. 捕获异常后既不处理也不抛出（空 catch 或仅 printStackTrace）是高危反模式：故障被静默掩盖。
**答案：B**
**解析：** 正确表述应为——Checked 异常编译期强制处理，RuntimeException 及其子类不强制。。原因：Checked 的初衷是强制调用方处理可恢复错误，但工程实践暴露了大量吞异常问题。。

**Qjava-basics-1920（单选·反向·语言杂项）** 以下关于「语言杂项」的说法，**错误**的是？
- A. 0.1 + 0.2 在 Java 中精确等于 0.3。
- B. 浮点数（float/double）不能直接用 == 比较相等，应使用误差范围或 BigDecimal。
- C. switch 原生支持 byte/short/char/int 及其包装类、枚举（JDK7+）与 String（JDK7+），不支持 long/float/double/boolean。
- D. char 本质是 16 位无符号 UTF-16 代码单元，可参与整数运算（如 'a'+1 得 'b'）。
**答案：A**
**解析：** 正确表述应为——浮点数（float/double）不能直接用 == 比较相等，应使用误差范围或 BigDecimal。。原因：IEEE754 二进制无法精确表示 0.1 等十进制小数。。

**Qjava-basics-1921（单选·反向·Object）** 以下关于「Object」的说法，**错误**的是？
- A. wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。
- B. Object.clone 默认就是深拷贝。
- C. Object.clone 是浅拷贝（引用字段复制引用），深拷贝需重写 clone 递归复制或改用拷贝构造器/序列化。
- D. finalize 在 JDK9 标记废弃、JDK18 进一步降级，资源清理应使用 try-with-resources 或 Cleaner。
**答案：B**
**解析：** 正确表述应为——Object.clone 是浅拷贝（引用字段复制引用），深拷贝需重写 clone 递归复制或改用拷贝构造器/序列化。。原因：Cloneable 是空标记接口且 clone 语义脆弱，Effective Java 建议用拷贝构造器替代。。

**Qjava-basics-1922（单选·反向·集合通用）** 以下关于「集合通用」的说法，**错误**的是？
- A. 核心复杂度速记：ArrayList get O(1)/中间插 O(n)；HashMap get/put 均摊 O(1)；TreeMap O(log n)；LinkedList 头尾操作 O(1)/定位 O(n)。
- B. Map 继承自 Collection 接口。
- C. Collection 根接口下 List/Set/Queue 三大分支；Map 不是 Collection 的子接口。
- D. 遍历集合删除元素的安全方式：Iterator.remove()、removeIf、或 CopyOnWriteArrayList（快照迭代）。
**答案：B**
**解析：** 正确表述应为——Collection 根接口下 List/Set/Queue 三大分支；Map 不是 Collection 的子接口。。原因：Map 是独立的键值对抽象，与 Collection 并列。。

