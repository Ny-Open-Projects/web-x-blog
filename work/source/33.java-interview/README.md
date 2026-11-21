# java-interview —— 阿里 P10 面试准备项目

> 从零基础 → 亿级微服务 → AI/Agent 的 Java 后端面试全卷，对标阿里专家（P10）考察要求。
> 内容 + 生成器一体：`docs/` 是内容库，`src/` 是一个零依赖的 Java 生成器。

## ✅ 运行环境（2026-11-14 已配置并全链路验证）

- **JDK 21.0.2**：`C:\Users\Administrator\.zcode\tools\jdk-21.0.2`（JAVA_HOME 与用户 PATH 已设置，新终端直接可用）
- **Arthas 4.3.5**：`notes/arthas-practice/arthas-boot.jar`（core 在 `C:\Users\Administrator\.arthas\`）
- **已验证**：生成器编译运行 ✅（INDEX.md 现为生成器产物，149 题统计与手工审计一致）；ArthasPractice 四种故障模式 ✅；Arthas 附加 + `thread`/`trace` 实际诊断输出 ✅

### 常用命令

```bash
# 刷新 INDEX.md 统计（无需 Maven，javac 即可）
javac -encoding UTF-8 -d target/classes src/main/java/com/p10/interview/model/Chapter.java src/main/java/com/p10/interview/generator/InterviewGuideGenerator.java
java -cp target/classes com.p10.interview.generator.InterviewGuideGenerator

# Arthas 实战演练（详见 notes/arthas-practice/README.md）
cd notes/arthas-practice && javac -encoding UTF-8 ArthasPractice.java && java ArthasPractice cpu
```

> Maven 用户也可 `mvn compile exec:java` 运行同一生成器（pom 已配置 exec 插件）。

## 目录结构

```
java-interview/
├── docs/                          # 面试内容库（核心资产）
│   ├── 00-outline.md              # 大纲：十章结构 + 每章统一模板
│   ├── 01-java-fundamentals/      # 第1章 Java 基础与集合
│   ├── 02-jvm-concurrency/        # 第2章 并发编程与 JUC
│   ├── 03-jvm/                    # 第3章 JVM 与性能调优
│   ├── 04-spring-ecosystem/       # 第4章 Spring 与框架生态
│   ├── 05-mysql-storage/          # 第5章 MySQL 与存储
│   ├── 06-redis-cache/            # 第6章 Redis 与缓存体系
│   ├── 07-messaging/              # 第7章 消息队列与异步化
│   ├── 08-distributed-microservices/ # 第8章 分布式理论与微服务
│   ├── 09-system-design/          # 第9章 亿级高并发与场景设计题
│   ├── 10-ai-agent/               # 第10章 AI 时代：LLM / Agent
│   ├── 11-appendix/               # 附录 A-E：软实力/简历/反问/备考计划/总速记
│   ├── 12-arthas-lab/             # 第12册 Arthas 线上诊断实操手册
│   ├── 13-coding-lab/             # 第13册 手写代码题全解（10 道）
│   ├── 14-mock-interview/         # 第14册 模拟面试实战剧本（五轮追问剧本）
│   ├── 15-rapid-fire/             # 第15册 快问快答冲刺卡（70 道闪卡）
│   ├── 16-daily-plan/             # 第16册 90 天每日打卡任务清单
│   ├── 17-process/                # 第17册 阿里职级体系与面试流程解析
│   ├── 18-annotated-transcript/   # 第18册 示例面试实录（一面带批注回放）
│   ├── 19-transcript-r2r3/        # 第19册 二面/三面实录精简版（带批注）
│   ├── 20-source-code/            # 第20册 源码逐行精读（HashMap/CHM/AQS/refresh）
│   └── 21-transcript-final/       # 第21册 四面（总监面）与HR面实录
├── src/main/java/com/p10/interview/
│   ├── model/Chapter.java         # 章节统计模型
│   └── generator/InterviewGuideGenerator.java  # 生成器：扫描内容 → INDEX.md
├── pom.xml                        # Maven（零第三方依赖，JDK 8+ 可编译）
├── notes/
│   └── arthas-practice/           # Arthas 实战沙盘：4 个可复现故障 + 练习指南
├── INDEX.md                       # 自动生成的总索引
├── SPEED-CARDS.md                 # 全卷速记卡合订本（考前一小时专用）
└── STUDY-TRACKER.md               # 自动生成的学习打卡表
```

## 使用方式

1. **直接读**：从 [INDEX.md](INDEX.md) 进入，按 30/60/90 天计划推进（见附录 D）。
2. **重新生成索引**（需要 JDK 8+ 和 Maven）：
   ```bash
   mvn compile exec:java
   ```
   生成器会扫描 docs/ 下所有章节，统计每章题数、字数、预计学习时长，刷新 INDEX.md 与 STUDY-TRACKER.md。
3. **背题节奏**：每章按"零基础卡片 → 入门题 → 进阶题 → 压轴题 → 追问链 → 速记卡"顺序学习，
   速记卡用于考前 30 分钟滚动复习。

## 内容规范（给后续增补者）

- 每道题固定四要素：【面试官意图】【参考回答（可背）】【追问链】【P10 加分项】；
- 压轴题必须带"事故复盘/选型权衡"叙事模板；
- 章末必须有：追问链图谱（ASCII）、一页速记卡（10 条以内）、参考资料。
