# 33. RAG 微调实战：Embedding 与 LLM 两类模型的高效微调（LoRA + 领域检索适配）

## 纲要

- **RAG 要微调哪两个模型**：① **Embedding 模型**（检索侧，决定「召回得准不准」）；② **大模型 LLM**（生成侧，决定「答得好不好」）。
- **为什么必须微调**：检索侧——通用开源 Embedding 在垂直领域语义偏弱、召回差；生成侧——小模型在有限算力下生成质量不足。
- **高效微调主线 LoRA**：低秩分解，只训练 `A/B` 两个小矩阵，显存省 2/3、可插拔、易回滚；用 PEFT 三行接入任意 HF 模型。
- **微调框架全流程**（以 LLaMA-Factory / SWIFT 为代表）：数据准备 → 数据注册 → 训练超参配置 → 训练 → 模型跟踪与评估。
- **Embedding 微调**：用对比损失（MultipleNegativesRankingLoss / TripletLoss）拉进正样本、推开负样本；sentence-transformers 或 FlagEmbedding 均可落地。
- **先评估再微调（ops）**：检索差先换更强 Embedding + 加 Re-rank；生成差先换更强模型/prompt；微调是成本最高的最后一步。

> 本章代码基于课程标准工程（`huihuiz2026/RAG_erag-master` 口径）按开源标准实现重构。外部代码卷暂未挂载，下列代码为**可独立运行的标准实现**（PEFT / sentence-transformers / LLaMA-Factory），非逐文件提取；坐标、超参与目录结构以开源标准 + 课程口径为准，可重挂卷后对照替换。

## 一、为什么要微调 RAG 里的两个模型

RAG 效果由「检索」与「生成」两段决定，对应两类模型：

| 模型 | 在 RAG 中职责 | 何时需要微调 | 不微调的代价 |
| --- | --- | --- | --- |
| **Embedding 模型** | 向量检索（把问题/文档编码成向量做相似度） | 特定领域（医疗/法律/金融）检索匹配差、召回靠后 | 召回 Top-K 全是噪声，LLM 再强也答不对 |
| **大模型 LLM** | 基于检索上下文生成答案 | 小模型（7B 以下）在有限算力下生成质量不足、格式乱 | 答案幻觉、不遵循领域术语 |

> 微调是「领域适配」的关键手段：检索段让 Embedding 更懂领域语义，生成段让小模型在有限算力下达到可用效果。**但微调不是第一步**——先确认是不是数据切分、Re-rank、prompt 的问题，再决定是否微调（见文末 ops）。

## 二、大模型（LLM）微调概述

### 2.1 全量微调 vs 高效微调

| 方式 | 显存占用 | 训练参数 | 适用 | 缺点 |
| --- | --- | --- | --- | --- |
| 全量微调（Full Fine-Tuning） | 极高（需存优化器状态+梯度+副本） | 100% | 算力充足、追求极致 | 显存爆炸、易灾难性遗忘、难回滚 |
| **LoRA / QLoRA**（高效微调） | 低（只训低秩矩阵） | 0.1%~5% | 单卡/小团队领域适配 | 效果略逊全量（但常够用） |

课程主推 **LoRA**（及其量化版 **QLoRA**：4-bit 加载基座 + LoRA，进一步降显存）。

### 2.2 LoRA 原理（低秩适配）

LoRA 的核心思想：权重更新矩阵 `ΔW` 可用两个低秩矩阵乘积近似 `ΔW = B·A`，其中 `B∈R^{d×r}`,`A∈R^{r×k}`,秩 `r ≪ d`。

```
原始：  y = W₀·x                (W₀ 冻结，不更新)
LoRA：  y = W₀·x + (B·A)·x       (只训练 A、B，r 远小于 d)
```

- `r`（lora_rank）：秩，常见 8/16/32/64，越大容量越高、显存越涨。
- `lora_alpha`：缩放系数，常取 `2*r`。
- `target_modules`：作用在哪些层，通常 `q_proj,v_proj`（注意力），也可加 `k_proj,o_proj,gate_proj,up_proj,down_proj`。
- 训练完可用 `merge_and_unload()` 把 `B·A` 合并回 `W₀`，推理零额外开销。

## 三、LoRA 实战（PEFT，可独立运行）

### 3.1 依赖

```bash
pip install torch transformers peft datasets accelerate sentencepiece
# QLoRA 还需：
pip install bitsandbytes
```

### 3.2 用 PEFT 给任意 HF 模型加 LoRA

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, TaskType

MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"   # 课程示例基座；可换 DeepSeek/GLM 等

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,   # 省显存；QLoRA 用 load_in_4bit=True
    device_map="auto",
)

# ① LoRA 配置：只训练注意力 q/v 投影的低秩矩阵
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,                       # 秩
    lora_alpha=16,              # 缩放 = 2*r
    lora_dropout=0.05,
    target_modules=["q_proj", "v_proj"],
    bias="none",
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
# 典型输出：trainable params: 4,194,304 || all params: 7,724,557,312 || trainable%: 0.05
```

### 3.3 构造训练数据 + 训练

```python
from datasets import load_dataset

# 课程格式：instruction / input / output（alpaca 风格，领域问答对）
data = load_dataset("json", data_files="train.jsonl")["train"]

def tokenize(example):
    # 用对话模板把 instruction+input+output 拼成模型训练样本
    messages = [{"role": "user", "content": example["instruction"] + example.get("input", "")},
                {"role": "assistant", "content": example["output"]}]
    text = tokenizer.apply_chat_template(messages, tokenize=False)
    out = tokenizer(text, truncation=True, max_length=2048)
    out["labels"] = out["input_ids"].copy()
    return out

train_ds = data.map(tokenize, remove_columns=data.column_names)

training_args = TrainingArguments(
    output_dir="./outputs/qwen-lora",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=8,
    num_train_epochs=3,
    learning_rate=2e-4,          # LoRA 学习率通常比全量大 5~10 倍
    fp16=False, bf16=True,
    logging_steps=10,
    save_strategy="epoch",
    report_to="none",             # 接 wandb 可改 "wandb"（模型跟踪）
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    tokenizer=tokenizer,
)
trainer.train()

# ② 训练完合并权重，推理无额外开销
model = model.merge_and_unload()
model.save_pretrained("./outputs/qwen-lora-merged")
```

### 3.4 QLoRA（4-bit 量化 + LoRA，单卡可跑 7B/13B）

```python
from transformers import BitsAndBytesConfig
from peft import prepare_model_for_kbit_training

bnb = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, quantization_config=bnb, device_map="auto")
model = prepare_model_for_kbit_training(model)   # 关键：冻结 layernorm/embedding 并准备梯度
model = get_peft_model(model, lora_config)        # 同 3.2
```

## 四、微调框架全流程（以 LLaMA-Factory 为代表）

课程提到的「微调框架」（机翻音译失真，疑为 SWIFT / LLaMA-Factory）本质是把上面的步骤**可视化 + 配置化**。以最主流的 **LLaMA-Factory** 为例，全流程四步：

### 4.1 数据准备（领域问答对）

```jsonl
// data/domain_rag.jsonl
{"instruction": "根据已知信息回答问题", "input": "已知：公司年假为20天。问题：员工一年有多少天年假？", "output": "根据已知信息，员工一年有20天年假。"}
{"instruction": "把下列产品描述归类", "input": "产品：企业级SSD 3.84TB", "output": "存储设备"}
```

### 4.2 数据注册（dataset_info.json）

```json
{
  "domain_rag": {
    "file_name": "domain_rag.jsonl",
    "formatting": "alpaca",
    "columns": { "prompt": "instruction", "query": "input", "response": "output" }
  }
}
```

### 4.3 训练超参配置（lora_sft.yaml）

```yaml
model_name_or_path: Qwen/Qwen2.5-7B-Instruct
stage: sft
do_train: true
finetuning_type: lora            # 高效微调
lora_rank: 8
lora_alpha: 16
lora_target: q_proj,v_proj
dataset: domain_rag
cutoff_len: 2048
per_device_train_batch_size: 2
gradient_accumulation_steps: 8
learning_rate: 2.0e-4
num_train_epochs: 3
output_dir: outputs/llama-factory-lora
logging_steps: 10
save_steps: 100
```

### 4.4 训练 + 模型跟踪

```bash
# 命令行训练
llamafactory-cli train examples/train_lora/lora_sft.yaml
# 或启动可视化 Web UI（模型跟踪/评估更直观）
llamafactory-cli webui
```

> **模型跟踪**：LLaMA-Factory 内置 TensorBoard / wandb 接入，记录 loss 曲线、学习率、eval 指标；SWIFT（魔搭）同样支持 `swift sft` 命令 + 可视化。跟踪重点是看 **loss 是否稳定下降、eval 集指标是否提升**，避免过拟合（train loss 掉但 eval 涨=过拟合信号）。

## 五、Embedding 模型微调实战

### 5.1 为什么 Embedding 也要微调

通用 Embedding（如 `bge-base`、`text-embedding` 类）在通用语料上训练，遇到垂直领域术语（法律条文、医疗名词、企业内部黑话）时，语义空间不匹配 → 召回 Top-K 不准。微调让它把领域内「近义表达」在空间里拉得更近。

### 5.2 用 sentence-transformers 做领域检索微调（可运行）

```python
from sentence_transformers import SentenceTransformer, InputExample, losses, evaluation
from torch.utils.data import DataLoader

model = SentenceTransformer("BAAI/bge-small-zh-v1.5")   # 课程示例基座

# ① 构造 (query, positive) 对 —— 领域内「问」与「应召回文档」配对
train_examples = [
    InputExample(texts=["如何申请年假", "员工年假申请流程：登录OA提交申请单..."]),
    InputExample(texts=["SSD 与 HDD 区别", "SSD 基于闪存无机械结构，HDD 靠磁盘旋转..."]),
    # ... 数百~数千对领域样本
]

train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)

# ② 对比损失：batch 内互为负样本，拉近正例、推远负例
train_loss = losses.MultipleNegativesRankingLoss(model)

# ③ （可选）评估：用信息检索评估器看召回
evaluator = evaluation.InformationRetrievalEvaluator(
    queries={"q1": "如何申请年假"},
    corpus={"c1": "员工年假申请流程...", "c2": "SSD 介绍..."},
    relevant_docs={"q1": ["c1"]},
)

model.fit(
    train_objectives=[(train_dataloader, train_loss)],
    epochs=3,
    warmup_steps=100,
    evaluator=evaluator,
    evaluation_steps=500,
    output_path="./outputs/bge-domain",
)
```

### 5.3 三元组损失（更精细的正负对）

```python
from sentence_transformers import InputExample, losses

# (anchor, positive, negative)
triplet_examples = [
    InputExample(texts=["年假怎么申请", "OA提交年假申请单", "SSD 存储原理"]),
]
train_loss = losses.TripletLoss(model)   # 拉进 anchor-positive，推开 anchor-negative
```

### 5.4 FlagEmbedding（BGE 官方微调，支持大模型蒸馏）

BGE 官方 `FlagEmbedding` 支持更复杂训练（含 LLM 蒸馏、`bge-reranker` 联合训练）：

```bash
pip install FlagEmbedding
```
```python
from FlagEmbedding import FlagModel
# 官方提供 finetune 脚本：用一个 (query, pos, neg) 三元组数据集即可
# python -m FlagEmbedding.finetune.encode.bge_standard \
#   --model_name_or_path BAAI/bge-base-zh-v1.5 \
#   --train_data ./triplets.jsonl --output_dir ./outputs/bge-ft
```

## 六、端到端：RAG 两模型微调串联

```text
领域文档
  ├─ Embedding 微调 ──→ 领域检索器（召回更准）
  │        │
  │        └─ 检索 Top-K 上下文
  │                 │
  └─ LLM(LoRA) 微调 ──→ 领域生成器（答得更准、用术语）
                    │
                    ▼
              领域 RAG 问答系统
```

1. **先微调 Embedding**：用领域 (query,doc) 对训练，提升召回准确率（看 IR 评估器的 Recall@K）。
2. **再准备 SFT 数据**：用「检索到的上下文 + 标准答案」构造 instruction/input/output。
3. **LoRA 微调 LLM**：让生成贴合领域术语与格式。
4. **联合评估**：端到端测「问题→正确答案」命中率，对比微调前后的 RAG 评分。

## 七、排错 SOP

1. **LoRA 没生效/效果差**：`target_modules` 是否命中真实层名（不同模型层名不同，用 `model.print_trainable_parameters()` 确认 >0 且落在注意力层）；`r` 是否太小。
2. **显存 OOM**：开 QLoRA（4-bit）、降 `per_device_train_batch_size`、加 `gradient_accumulation_steps`、开 `gradient_checkpointing`。
3. **Embedding 微调 loss 不降**：正负样本质量/配比问题；batch 太小（对比损失依赖 in-batch 负例，batch≥16）。
4. **过拟合**：train loss 掉但 eval 涨 → 早停、降 epochs、加 dropout、扩数据。
5. **基座加载失败**：`trust_remote_code=True` 是否加；镜像源是否可达；4-bit 需 `bitsandbytes` 正常编译。

## 八、FAQ

**Q1：RAG 里要微调哪两个模型？**
Embedding 模型（检索侧）与大模型（生成侧）。

**Q2：什么情况下要微调 Embedding？**
开源通用 Embedding 在特定领域检索匹配差、召回靠后时，需领域微调提升召回精度。

**Q3：为什么强调 LoRA 而不是全量微调？**
大模型全量微调算力/显存门槛高、易遗忘、难回滚；LoRA 只训低秩矩阵，省显存、可插拔、易回滚，是小团队首选。

**Q4：LoRA 的 r 和 alpha 怎么选？**
`r` 常见 8/16/32，越大容量越高；`alpha` 常取 `2*r` 做缩放；先小后调。

**Q5：Embedding 微调用什么损失？**
领域检索用 `MultipleNegativesRankingLoss`（in-batch 负例）或 `TripletLoss`（显式正负对）。

**Q6：微调框架一般覆盖哪些环节？**
数据准备、数据注册、超参配置、训练、模型跟踪与评估（LLaMA-Factory / SWIFT 均支持）。

## 九、面试高频问答

**1. RAG 微调针对哪两类模型？各解决什么？**
Embedding（检索召回精度）+ LLM（生成质量/领域术语）。

**2. LoRA 原理？**
对权重更新 `ΔW` 做低秩分解 `B·A`（`r≪d`），冻结原权重只训 A/B，显存省、可合并、易回滚。

**3. LoRA 相比全量微调优势？**
训练参数 0.1%~5%、显存大幅降低、支持 QLoRA 4-bit、插件式可插拔、回滚简单。

**4. 微调 Embedding 的核心损失？**
对比损失：拉近正例、推开负例；`MultipleNegativesRankingLoss` 或 `TripletLoss`。

**5. 怎么判断要不要微调？**
先排查切分/Re-rank/prompt 问题；检索差先换更强 Embedding+Re-rank，生成差先换更强模型/prompt；微调是成本最高的最后一步。

**6. QLoRA 是什么？**
4-bit 量化加载基座 + LoRA 微调，进一步降显存，单卡可微调 7B/13B。

## 十、ops 提示（增效与风险）

> **先评估再微调**：检索差先试换更强通用 Embedding / 加 Re-rank；生成差先试更强模型或优化 prompt。**微调是最后一步，成本最高、数据要求最严**。
>
> **数据质量决定上限**：微调效果八成靠数据，脏数据不如不调；务必先清洗、去重、校验标注。
>
> **LoRA 优先于全量微调**：显存省、可插拔、回滚易，小团队领域适配首选。
>
> **显存与稳定性**：OOM 优先开 QLoRA + 梯度检查点；`target_modules` 必须命中真实层名（用 `print_trainable_parameters()` 校验）。
>
> **防过拟合**：跟踪 eval 指标，train loss 降而 eval 涨即过拟合，早停 + 扩数据。
>
> **合规与成本**：微调需算力与标注预算；企业内部数据微调注意脱敏与授权，避免泄露敏感语料。

