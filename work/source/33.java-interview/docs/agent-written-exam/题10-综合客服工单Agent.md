# 题 10（综合）：客服工单 Agent

## 题目（40 分钟）

设计并实现**客服工单 Agent**（综合题，覆盖前九题全部能力）：

**需求**：用户提交售后问题（文本+可选图片）→ Agent 分类（退款/换货/咨询）→ 知识库检索回答（政策类）→ 工具操作（查订单/创建工单，退款需人工确认）→ 复杂问题升级人工（带会话摘要）。

**要求**：
① 宪法（system）：角色/边界（不做赔付决策 JA-551）/升级条件/语气
② 工具：query_order / create_ticket / escalate（升级人工），图片走多模态消息（JA-292）
③ 预算：单会话 token 上限，耗尽优雅收尾转人工（AD-099）
④ 轨迹：全程轨迹（AD-040）+敏感脱敏（AD-054）
⑤ 升级：升级人工带会话摘要（AD-134）+已尝试方案（交接清单 AD-464）
⑥ 安全：政策回答必须引用知识库来源（JA-202 引用校验），无法回答明确说不知道（JA-367 拒答）

**交付**：架构类图 + 核心代码（宪法/循环/工具/升级路径）+ 评测方案（任务集设计 AD-090）+ 追问应对。

## 评分细则（四维，权重同 README）

| 维度 | 得分点 |
|------|--------|
| 功能正确 40% | 分类路由 ✓｜RAG 回答带引用 ✓｜工具操作（查单/建单）✓｜升级人工带摘要 ✓｜多模态图片接入 ✓ |
| 边界处理 20% | 拒答（知识库没有）✓｜退款强确认（人审）✓｜预算耗尽转人工 ✓｜知识库检索空兜底 ✓ |
| 工程质量 20% | 类图清晰（Executor/Registry/Memory/Trajectory）✓｜脱敏（对话含个人信息）✓｜评测任务集设计 ✓ |
| 并发与安全 20% | 会话隔离（多用户）✓｜工具幂等（建单幂等键）✓｜轨迹审计 ✓｜注入防线意识 ✓ |

## 参考架构（类图 + 核心骨架）

```java
/** 宪法（system）——JA-009 宪法资产 */
String SYSTEM = """
    你是电商售后助手。规则：
    1. 只回答售后相关问题；政策类回答必须引用知识库来源编号。
    2. 退款决策不由你做出——只能创建退款工单转人工（AD-551 边界）。
    3. 无法从知识库找到依据时，明确说"暂无相关政策信息"并创建人工工单。
    4. 语气专业友好；不泄露内部信息；用户情绪激动时主动升级人工。
    """;

/** 主流程（组合前九题能力） */
public String handle(String userId, String text, Optional<Image> image) {
    BudgetCounter budget = new BudgetCounter("cs-" + userId, 50_000); // AD-193
    List<Message> messages = new ArrayList<>();
    messages.add(Message.system(SYSTEM));
    messages.addAll(memory.search(userId, text, 3) // 题 4 记忆检索注入
        .stream().map(m -> Message.system("相关历史：" + m.summary())).toList());
    messages.add(Message.user(text, image));       // 多模态消息（AD-292）

    for (int step = 0; step < 10; step++) {
        budget.check(estimate(messages));          // 题 5 预算检查
        ModelResponse resp = model.chat(messages, tools.specs());
        messages.add(Message.assistant(resp));
        recorder.record(step, resp);               // 题 7 轨迹（脱敏钩子 AD-054）

        if (!resp.hasToolCalls()) {
            String answer = resp.content();
            validator.validateCitation(answer, retrievedSources); // 题 10 引用校验（JA-202）
            scanner.scan(answer);                  // 敏感扫描（AD-367）
            memory.write(userId, MemoryEntry.of(text, answer)); // 题 4 写回
            return answer;
        }
        for (ToolCall call : resp.toolCalls()) {
            if (call.name().equals("create_refund_ticket")) {
                String summary = summarizer.summarize(messages); // 升级摘要（AD-134）
                return escalateToHuman(userId, call.args(), summary); // 强确认升级（AD-080）
            }
            messages.addAll(parallelExecutor.execute(List.of(call))); // 题 2/3 容错执行
        }
    }
    return escalateToHuman(userId, Map.of("reason", "步数耗尽"),
                           summarizer.summarize(messages)); // 预算/步数收尾转人工（AD-005）
}
```

**评测方案**（任务集三层 AD-090）：真实客服对话采样 30 条（政策类/操作类/复杂类）+边界 10 条（辱骂/超范围/无知识）+对抗 10 条（诱导退款/诱导泄露）→门禁指标（政策引用率 100%、退款误执行 0、升级准确率）。

## 追问清单

1. 退款为什么不能让 Agent 直接执行？→ 资金不可逆+幻觉风险（AD-080 三防线/ JA-551 责任链）
2. 用户上传的图片里夹带"忽略以上指令"怎么办？→ 多模态注入（JA-580），图像文字过注入检测+边界标签
3. 客户并发两个会话会串号吗？→ 会话隔离（userId+sessionId 双键 AD-097），隔离测试（AD-208）
4. 知识库更新后缓存答案怎么办？→ 缓存键含知识版本（JA-669/456），失效传播
5. 情绪激动的用户怎么识别？→ 情绪信号（关键词+模型判断 JA-434 漏斗），升级阈值
6. 为什么政策回答必须引用？→ 无引用=幻觉无法溯源（JA-202），金融/电商合规要求
7. 如果一天 10 万会话，架构怎么扩？→ 无状态编排层水平扩展+记忆/向量库独立扩（JA-535/597）

## 常见错误

退款让 Agent 决策（越权）｜政策回答无引用（幻觉）｜升级人工不带摘要（人工从零开始）｜图片未处理（多模态缺失）｜无预算（会话烧钱）｜轨迹含明文手机号（脱敏缺失）。

---
*本套卷十题与 agent-dev 域矩阵同源（AD 系列），全部参考实现为本机风格验证（ExamSolutions 系列同标准）。返回 [README](README.md)。*
