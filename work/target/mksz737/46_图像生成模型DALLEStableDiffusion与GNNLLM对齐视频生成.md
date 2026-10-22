# 46. 图像生成模型：DALL·E / Stable Diffusion 与 GNN+LLM 对齐、视频生成

## 纲要

- **两类视觉模型**：通用视觉大模型（LLM 的「眼睛」，看图识别，如手势/人脸，已成熟）vs 图像生成大模型（文生图，如 Midjourney、Stable Diffusion）。
- **Stable Diffusion 生态**：LCM（加速出图）、SDXL Turbo（秒级出图，小狐狸流水线）、SD 2.0；WebUI 插件丰富。
- **DALL·E**：已迭代到第三代（DALL·E 3），可直接给指令、自动提炼关键词生成图，贴合使用习惯。
- **GNN + LLM 结合**：用 LLM 的文本理解 + GNN 捕获图结构关系，实现更强图学习。
- **LLM 助力图任务的四种对齐策略**：对比（Contrastive）、迭代对比（Iterative）、图嵌套（Graph Nested）、蒸馏（Distillation）。
- **文生视频**：Runway（图生视频老大哥）、Pika（斯坦福团队，文字生成视频片段，已融 5500 万美元）。

> 本章按课程口径重构；模型名词已规范化；剥离营销与课程群引流。

## 一、图像模型 vs 视觉模型

- **通用视觉大模型**：可理解为 LLM 的「眼睛」，负责看/识别图（人脸、手势、追踪），技术早已成熟。
- **图像生成大模型**：由模型自己生成图片（文生图），如 Midjourney、Stable Diffusion——本课程重点在提示词侧。
- **GPT-4 多模态**：集成了 GNN（视觉）与 DALL·E（生成），既看图又生图。

## 二、Stable Diffusion 与 DALL·E 进展

- **Stable Diffusion（SD）**：
 - **LCM（Latent Consistency Model）**：提升出图速度。
 - **SDXL Turbo**：秒级出图，课程演示「边输入文字边出图」，小狐狸是其流水线代表。
 - **SD 2.0**：横向对比 DALL·E 1/2 的版本，部分模型可下载本地用、部分提供可商用 license。
- **DALL·E 3**：第三代；前代靠提示词生图，三代后可直接下指令、自动提炼关键词再生成，更贴合习惯。
- **综述参考**：香港大学联合综述、清华综述、《Honest Evaluation of Text-to-Image Models》《A Survey of AI Text-to-Image and Text-to-Video Generators》——含 SD 各版本与 DALL·E 横向对比。

## 三、GNN + LLM 结合

- **原理**：LLM 理解文本，GNN（图神经网络）捕获结构关系，二者结合实现更全面强大的图学习。
- **LLM 助力图任务的分类**（综述表格）：
 - 列：使用的神经网络（GNN）、使用的大模型（多为 GPT-3.5，也有 Llama/BERT）、微调（Fine-tuning）/提示词（Prompting）、任务（Node 节点 / Link 关系 / Graph Reasoning 图推理 / Retrieval 检索 / Captioning 图像描述）。
 - 行：LLM as Enhancer（增强）、LLM as Predictor（预测/解析图）、GNN 与 LLM 并列架构。

## 四、四种对齐策略

- **LLM as Enhancer**：LLM 把输入文本翻译/向量化，交给 GNN 运算生成图；或直接输出图像模型能懂的提示词。
- **LLM as Predictor**：反向——解析图片关键信息交给 LLM 生成描述（图生文）。
- **四种对齐（Alignment）策略**：
 1. **Contrastive（对比）**：图像模型队列 vs 文本模型队列比较，使二者对齐（如「黄色」文本→黄色猫图像）。
 2. **Iterative（迭代对比）**：交叉比对两种大模型做监督学习与评价，反复调整预期。
 3. **Graph Nested（图嵌套）**：与 Transformer 深度学习深度交织，让 Transformer 处理图结构数据（其擅长点）。
 4. **Distillation（蒸馏）**：抽取大模型特定知识块并聚焦，类似给模型设角色限定知识范围，提升该范围性能。

## 五、文生视频与商业产品

- **Runway**：图生视频「老大哥」，让静止图片动起来。
- **Pika（Pika Labs）**：斯坦福两位女博士生创立，文字生成视频片段；可像导演一样控制图片中人物行为与动画，生成不同视频风格；demo 已融 5500 万美元。可能沿用 Discord 发提示词/图/视频的商业模式。
- **应用方向**：用图像模型做成人/儿童绘本 → 交 LLM 生成文本与配音 → 绘本成品。

## 六、FAQ

**Q1：图像生成模型和视觉模型区别？**
前者文生图（生成），后者看图识别（理解），是两类方向。

**Q2：LLM 怎么帮到图任务？**
作 Enhancer 把文本转向量/提示词给 GNN；作 Predictor 解析图生成描述；二者对齐策略让文本与图像表现一致。

**Q3：SDXL Turbo 有什么用？**
秒级出图，支持边输入文字边出图，极大降低等待、提升交互体验。

**Q4：文生视频现在到什么阶段？**
Runway 图生视频、Pika 文字生视频片段，已能让用户导演式控制人物动画，尚在早期商业化。

## 七、面试高频问答

**1. 简述 LLM 与 GNN 结合的四种对齐策略。**
Contrastive（双队列对比对齐）、Iterative（迭代交叉比对监督）、Graph Nested（与 Transformer 交织处理图结构）、Distillation（蒸馏聚焦特定知识）。

**2. Stable Diffusion 生态近期有哪些加速进展？**
LCM 提速、SDXL Turbo 秒级出图、WebUI 插件丰富；DALL·E 已到第三代可自动提炼关键词。

**3. LLM as Enhancer 与 as Predictor 区别？**
Enhancer 是文本→向量/提示词→GNN 生图（文生图方向）；Predictor 是图→关键信息→LLM 描述（图生文方向）。

**4. 文生视频代表产品与差异？**
Runway 主打图生视频；Pika 主打文字生视频片段且可导演式控制人物，均处早期高成长。

## 八、ops 提示（选型）

> **选型看任务与成本**：个人小团队用大厂 API 性价比高；有资金/团队再考虑可商用 license 模型本地扩展。
>
> **读综述不读搬运**：香港大学/清华综述、Honest Evaluation 等一手文献含版本横向对比，比二手准。
>
> **绘本工作流**：图像模型出图 + LLM 出文/配音，可快速产出绘本类内容。

