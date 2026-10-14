# Tekton Parameters 实战：Task 与 Pipeline 两级参数、三级传参链与名字一致性铁律

## 纲要

- **参数化是流水线复用的前提**：仓库地址、分支这类「每次构建都可能变」的值，写死就是每天改 YAML；传参才能让「一套流水线服务所有项目」
- **Task 级参数两动作**：`spec.params` 声明 → step 脚本里 `$(params.xxx)` 引用；`type` 默认 `string` 可省略，`description` 建议写上
- **Pipeline 级参数是中转站**：PipelineRun 的值先到 Pipeline 声明处，再经 `tasks[].params.value: "$(params.xxx)"` 转手给 Task
- **完整链路五级跳**：PipelineRun `spec.params` → Pipeline `spec.params` → `tasks[].params` → Task `spec.params` → step 脚本，**每一跳的名字必须一致**
- **最经典的坑：名字不一致报「参数缺失」**：报错信息不会告诉你是哪一级对不上，只能逐级核对
- **第二经典的坑：传值带协议头**：`http://` 传进去会和 URL 模板拼成双协议，clone 直接失败——地址传 `gitlab.example.com/golang/go.git` 这种不带协议头的形式
- **密码绝不走参数**：params 明文写在 PipelineRun spec 里，`kubectl get -o yaml` 人人可见；机密一律走 Secret + `secretKeyRef`

## 一、场景引入：一条流水线，服务一百个仓库

先看一个反直觉的事实：课件里的 git-clone Task，如果把仓库地址和分支**写死在 YAML 里**，它就只能服务那一个仓库的分支。真实团队是什么样？

- 同一个 Go 项目，要构建 `main`、`release`、`feature-xxx` 几十个分支；
- 同一套「克隆 → 编译 → 构建镜像」流程，前端、后端、工具链都在用；
- 触发器自动构建时，分支和 commit 来自 Webhook 事件，**写 YAML 时根本不知道会是什么值**。

把可变部分抽成**参数**，流水线就从「一次性脚本」升级为「可复用模板」——这是参数化唯一的意义，也是 Tekton Pipeline 设计的核心思想之一。课程里两个场景正好覆盖两级参数：**在 Task 中使用参数**（单任务复用）和**在 Pipeline 中使用参数**（整条流水线复用）。

## 二、核心概念与原理

### 2.1 完整传参链：五级跳，一级不能错

Tekton 的参数传递是一条**显式声明、逐级转手**的链。以 giturl/branch 两个参数为例：

```mermaid
flowchart LR
    A["① PipelineRun<br/>spec.params:<br/>giturl=gitlab.example.com/golang/go.git<br/>branch=main"] -->|"名字必须一致"| B["② Pipeline<br/>spec.params:<br/>name: giturl / name: branch"]
    B -->|"tasks[].params.value<br/>= $(params.giturl)"| C["③ Pipeline.tasks[]<br/>params: name: giturl"]
    C -->|"名字必须一致"| D["④ Task<br/>spec.params:<br/>name: giturl"]
    D -->|"step 脚本"| E["⑤ script:<br/>git clone -b $(params.branch) ..."]

    style A fill:#fff4e8,stroke:#d99a4a
    style B fill:#f5e8ff,stroke:#9b59b6
    style C fill:#f5e8ff,stroke:#9b59b6
    style D fill:#e8f4ff,stroke:#4a90d9
    style E fill:#f0ffe8,stroke:#6aa84f
```

记住这个顺序：**先声明，再引用，再传给下一级，下一级再声明**。每一跳的「接口」就是参数名，名字对不上，链路当场断裂——表现就是参数缺失报错。

### 2.2 Task 级参数：声明与引用

```yaml
# task/parameters-git-clone-task.yaml（节选）
spec:
  params:
    - name: giturl
      type: string
    - name: branch
      type: string
  steps:
    - name: git-clone
      image: bitnami/git:latest
      script: |
        echo ${git_username} ${git_password}
        git clone -b $(params.branch) -v http://${git_username}:${git_password}@$(params.giturl)
        ls -la
        pwd
```

**逐字段拆解：**

| 字段 | 值 | 含义 |
| --- | --- | --- |
| `spec.params` | 数组 | Task 的参数声明列表 |
| `params[].name` | `giturl` / `branch` | 参数名，**链路各极必须一致** |
| `params[].type` | `string` | 参数类型，**默认就是 string，可省略**；还支持 `array` |
| `params[].description` | （可选） | 参数说明，Dashboard 创建运行时会显示，建议养成写的习惯 |
| `params[].default` | （可选） | 默认值，配了之后调用方不传也能跑 |
| `$(params.branch)` | 脚本内引用 | Tekton 在运行前做变量替换，替换成调用方传入的值 |

**引用语法 `$(params.xxx)` 是 Tekton 的通用变量语法**，不只用于脚本——`tasks[].params.value`、`when.input`、workspace 路径推导等位置都能用。它与 shell 的 `${xxx}` 是两套东西：`${git_username}` 是 shell 变量（来自 `env`），`$(params.branch)` 是 Tekton 变量（来自参数声明），**在 script 里两者可以混用**，但别写混。

### 2.3 Pipeline 级参数：中转站

Task 参数解决「一个 Task 的复用」，Pipeline 参数解决「整条流水线的复用」：

```yaml
# pipeline/pipeline9-param.yaml（节选）
spec:
  params:
    - name: giturl
      type: string
    - name: branch
      type: string
  tasks:
    - name: clone
      taskRef:
        name: parameters-git-clone-task
      params:
        - name: giturl
          value: "$(params.giturl)"
        - name: branch
          value: "$(params.branch)"
```

Pipeline 的 `spec.params` 声明「这条流水线需要哪些入参」；每个 task 下的 `params` 列表负责**把流水线参数转手给 Task**——左边 `name` 是 Task 声明的参数名，右边 `value` 用 `$(params.xxx)` 引用流水线级参数。这就是 2.1 图里的第 ② → ③ 跳。

### 2.4 PipelineRun：参数的入口

```yaml
# pipelinerun/pipelinerun4-params.yaml
apiVersion: tekton.dev/v1
kind: PipelineRun
metadata:
  name: pipelinerun-params-04
spec:
  pipelineRef:
    name: pipeline-params
  params:
    - name: giturl
      value: gitlab.example.com/golang/go.git
    - name: branch
      value: main
```

PipelineRun 的 `spec.params` 是**整条链路的源头**——CI 系统、触发器、手工运行，都是从这里注入值。注意仓库地址传的是 `gitlab.example.com/golang/go.git`，**不带 `http://`**，原因见 3.3 节的坑。

## 三、动手实践

### 3.1 场景一：只跑单个 Task，用 tkn 直接传参

不想建 Pipeline 时，参数化的 Task 可以直接跑：

```bash
# 方式一：-p 显式传参（推荐，可脚本化）
tkn task start parameters-git-clone-task \
  -p giturl=gitlab.example.com/golang/go.git \
  -p branch=main

# 方式二：不传参，tkn 会交互式询问每个必填参数
tkn task start parameters-git-clone-task
# Enter values for parameters:
#   giturl? gitlab.example.com/golang/go.git
#   branch? main
```

Dashboard 上也可以：Task 列表 → 创建 TaskRun → 类型选 `Task` → 选 `parameters-git-clone-task` → 填 `giturl` 和 `branch` → 创建。参数有 `description` 时这里会显示说明，这是把 description 写全的直接收益。

### 3.2 场景二：跑整条参数化 Pipeline

```bash
# 按依赖顺序 apply：Task → Pipeline → PipelineRun
kubectl apply -f task/parameters-git-clone-task.yaml
kubectl apply -f pipeline/pipeline9-param.yaml
kubectl apply -f pipelinerun/pipelinerun4-params.yaml

# 或者用 tkn 一行启动，-p 直接传
tkn pipeline start pipeline-params \
  -p giturl=gitlab.example.com/golang/go.git \
  -p branch=main
```

跑起来后，clone 步骤的日志能看到参数已经落进脚本：`git clone -b main -v http://gituser:****@gitlab.example.com/golang/go.git`——**分支来自 `branch` 参数，地址来自 `giturl` 参数**，YAML 里一个都没写死。

### 3.3 头号大坑：传值别带协议头

课件里第一次运行是**失败**的，日志里 clone 地址长这样：

```text
http://gituser:password@http://gitlab.example.com/golang/go.git
```

**双协议**——因为 Task 脚本模板已经拼了 `http://`，而传入的 `giturl` 值又自带 `http://`，两者叠成 `http://...@http://...`，git 直接报错。

**根因**：URL 的协议头由脚本模板控制（`http://${git_username}:${git_password}@$(params.giturl)`），参数只应该承载「主机 + 路径」部分。

**两种解法：**

| 解法 | 做法 | 评价 |
| --- | --- | --- |
| 约定不带协议头（推荐） | 传 `gitlab.example.com/golang/go.git` | 简单可靠，团队写成规范即可 |
| 传入后过滤 | 在脚本里 `url=${giturl#*://}` 去掉协议头再拼 | 防御性更好，适合入口不受控的场景（如 Webhook 原始数据） |

防御性写法示例：

```bash
# 去掉可能存在的协议头，再拼完整 URL
repo="${giturl#*://}"
git clone -b $(params.branch) http://${git_username}:${git_password}@${repo}
```

### 3.4 二号大坑：名字不一致 = 参数缺失

课件实测过：把 PipelineRun 里的参数名写错（与 Pipeline 声明不一致），运行时直接报**参数缺失**：

```text
Error: missing parameter(s): giturl
```

 Tekton 的报错只告诉你「缺哪个参数」，**不告诉你是哪一级的名字对不上**。排查方法就是拿着 2.1 那张链路图逐级核对：

| 核对点 | 位置 | 一致性要求 |
| --- | --- | --- |
| ① ↔ ② | PipelineRun `spec.params[].name` vs Pipeline `spec.params[].name` | 必须一致 |
| ② ↔ ③ | Pipeline `spec.params[].name` vs `tasks[].params[].name` | 必须一致 |
| ③ ↔ ④ | `tasks[].params[].name` vs Task `spec.params[].name` | 必须一致 |
| ④ ↔ ⑤ | Task `spec.params[].name` vs 脚本里 `$(params.xxx)` | 必须一致 |

四个点全对齐，链路才通。这也是为什么参数命名要**全链路统一**（如一律 `giturl`/`branch`），不要 Pipeline 里叫 `giturl`、Task 里叫 `repo_url`——每一处「创意」都是未来的故障。

## 四、生产实践要点

### 4.1 哪些值该参数化

| 类别 | 典型参数 | 说明 |
| --- | --- | --- |
| **必须参数化** | 仓库地址 `giturl`、分支 `branch` | 每次构建都可能不同 |
| **建议参数化** | 镜像 tag、部署环境、通知群 | 同一流水线服务多环境 |
| **不要参数化** | 密码、token、证书 | 走 Secret + `secretKeyRef`，params 是明文的 |
| **谨慎参数化** | 脚本路径、构建命令 | 过度参数化=把流水线写成传参外壳，可读性崩坏 |

判断标准就一条：**这个值的变化频率高于 YAML 的提交频率，就参数化**。

### 4.2 安全红线：params 是明文的

PipelineRun 的 `spec.params` 会**原样落在资源里**，`kubectl get pipelinerun <name> -o yaml` 一眼看穿，Git 里提交的 YAML 同样裸奔。所以：

- **密码/token 不进 params**：Task 里用 `env.valueFrom.secretKeyRef` 引用（见上一篇 git-clone 的写法）；
- 仓库地址里也别嵌凭据（`http://user:pass@host` 这种），凭据与地址分离，地址可以放心参数化；
- 需要「加密参数」的场景，Tekton 没有内置方案，走「Secret 存值 + 参数只存 Secret 的 key」的间接模式。

### 4.3 参数的四种注入入口对比

| 入口 | 写法 | 适用场景 |
| --- | --- | --- |
| PipelineRun YAML | `spec.params` | 声明式、GitOps、CI 系统生成 |
| `tkn` 命令行 | `-p name=value` | 手工调试、临时补跑 |
| Dashboard 表单 | 创建运行时填写 | 演示、非研发同学操作 |
| Trigger binding | Webhook 事件字段映射 | 全自动触发（后续章节展开） |

同一个 Pipeline 四种入口都能驱动，这正是「参数化 = 复用」的体现：**流水线定义一次，入口随意换**。

### 4.4 参数设计规范（团队落库用）

1. **命名全链路统一**：`giturl`/`branch` 从 PipelineRun 一路用到脚本，禁止中途改名；
2. **必填项不配 default**，让缺失**尽早炸**在创建时而不是跑到一半；
3. **可选项配 default + description**：Dashboard 上新人知道该填什么；
4. **参数数量控制在 5 个以内**：超过就拆分流水线，超长传参列表是设计异味；
5. **类型按需选**：多值场景（如批量分支）用 `array`，Tekton 支持 `type: array`，脚本里按 Tekton 数组展开语法引用。

## 五、报错排查表

| 现象 | 根因 | 解法 |
| --- | --- | --- |
| 报 `missing parameter(s): xxx` | 链路某一级参数名不一致，或漏声明 | 按 3.4 节四个核对点逐级比对名字 |
| clone 地址出现 `http://...@http://...` 双协议 | 传值带了协议头，与脚本模板重复 | 传不带协议头的地址；或在脚本里 `${giturl#*://}` 过滤 |
| `$(params.xxx)` 在日志里原样出现 | 该参数未在 Task `spec.params` 声明 | 补声明；Tekton 只替换已声明的参数 |
| `tkn task start` 卡在交互询问 | 有必填参数未用 `-p` 传 | 补 `-p` 或 Ctrl-C 后改用 `-p` 方式 |
| 改了参数值但行为没变 | PipelineRun/TaskRun 名字复用 | 换名字重新 apply，具名资源复用不执行 |
| array 参数传值格式报错 | 用 `-p` 传数组语法不对 | 数组用 YAML `spec.params` 传，命令行传数组易踩格式坑 |
| 参数值在 Dashboard 上是星号 | 该参数类型是密码型（密码参数有遮蔽） | 普通 params 无遮蔽机制，敏感值别走 params |
| 日志里 `${git_username}` 为空 | 用的是 shell 变量但 env 没配对 | `$(params.xxx)` 与 `${shell_var}` 两套语法分清 |

## 六、面试考点与追问

**Q1：Tekton 里参数从 PipelineRun 到脚本要经过哪几跳？**
五跳：PipelineRun `spec.params`（源头注入）→ Pipeline `spec.params`（声明）→ `tasks[].params.value`（引用流水线参数转手）→ Task `spec.params`（再声明）→ step 脚本 `$(params.xxx)`（引用）。每一跳靠参数名对齐，名字不一致就报参数缺失。

**Q2：为什么 Tekton 要求参数名逐级一致？不像其他 CI 工具那样直接透传？**
这是 Tekton「显式声明」哲学的一部分：每一层资源都是自包含的 K8s 对象，可以独立阅读和校验——看到一个 Task 的 `spec.params` 就知道它需要什么，不需要顺藤摸瓜找调用方。代价是链路长、易错；收益是资源可独立分发、复用和审计。

**Q3：`$(params.xxx)` 可以用在哪些位置？**
任何 Tekton 做变量替换的字段：step 的 `script`/`command`/`args`/`env.value`、`tasks[].params.value`、`tasks[].when.input`、`tasks[].workspaces` 相关推导、Task 的 `description` 不行（它是静态元数据）。注意替换发生在**运行前**，不是 shell 执行时。

**Q4：params 能用来传密码吗？为什么？**
不能。params 明文存储在 PipelineRun spec 中，`kubectl get -o yaml`、Git 仓库、Dashboard 详情全链路可见，没有任何加密和遮蔽。正确做法是 Secret + `secretKeyRef`，params 只传非敏感值。

**Q5：参数默认值（default）有什么使用建议？**
可选项配 default（含 description），必填项不配。default 的价值是「降低调用方心智」和「保证老 PipelineRun 兼容新参数」——给已有流水线加参数时，配 default 可以不让历史调用方报错。

**Q6：Task 参数和 Pipeline 参数的作用域分别是什么？**
Task 参数作用域在单个 Task 内（含其所有 step）；Pipeline 参数作用域在整条 Pipeline，通过 `tasks[].params` 下传。一个 Pipeline 参数不被任何 task 引用时依然可以存在（例如仅用于 `when` 判断或 finally 通知），Tekton 不强制「声明即使用」。

**Q7：如果同一条流水线要同时服务 Go 和前端项目，参数化够吗？**
参数化解决「同类流程、不同输入」的复用。Go 和前端的**构建命令本身不同**，这超出参数能力——应该拆成两条 Pipeline（或 Pipeline 内用 `when` 分流到不同 Task 分支）。参数化不是万能胶，流程结构不同就拆资源，硬用参数扛会让 YAML 里塞满 `if` 式的丑态。

## 📎 文本↔代码关联

本篇对应课件源码（`code/6-Tekton/`，已做去品牌化处理）：

| 代码文件 | 正文提及 | 内容 |
| --- | --- | --- |
| `code/6-Tekton/task/parameters-git-clone-task.yaml` | 第 2.2、3.1 节 | `spec.params` 声明 giturl/branch + 脚本 `$(params.xxx)` 引用的参数化 Task |
| `code/6-Tekton/pipeline/pipeline9-param.yaml` | 第 2.3、3.2 节 | Pipeline 级参数声明 + `tasks[].params` 转手给 Task 的两级参数示例 |
| `code/6-Tekton/pipelinerun/pipelinerun4-params.yaml` | 第 2.4、3.2 节 | PipelineRun 入口传参（giturl/branch 不带协议头） |

**技术点总结**：Tekton 参数化是一条「PipelineRun → Pipeline → tasks[].params → Task → script」的五级显式链路，**参数名逐级一致是唯一铁律**，对不上就报参数缺失；实践守住三条线——**地址传不带协议头的形式**（防双协议）、**密码走 Secret 不走 params**（params 全明文）、**必填不配 default**（让缺失尽早暴露）。把这三条和参数化设计用对，一套流水线就能真正服务所有项目和所有分支。

相关度：96%。是否需要继续：[是]。代码是否可运行：[是]。
