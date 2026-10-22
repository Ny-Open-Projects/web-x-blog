# 80. Argo CD 应用删除、回滚、Webhook 与横幅终端配置

## 纲要

- **删除分两种语义**：页面删 = Argo CD 应用 + K8s 应用**一起没**；终端删 = 只删 Argo CD 应用，**K8s 应用继续跑**——误操作前先想清楚要哪种
- **回滚认 commit message**：历史版本靠提交信息辨认（「历史版本改为三，默认为六」）——团队必须约定提交信息规范，否则回滚靠猜
- **Webhook 把 3 分钟压成秒级**：仓库设置填 Argo CD 的 `/api/webhook` + 推送事件，可选 secret 验证——提交即同步，不用等轮询
- **日志看多看少有讲究**：Pod 里看单容器日志；**RS 上点 log 看全部 Pod 聚合日志**——多副本排障的效率差在这
- **横幅四行 configmap**：`argocd-cm` 加内容 + 跳转链接 + 永久粘性 + 上下位置——公告、跳转 Rollout 面板都靠它
- **容器终端两行开启**：默认不能在 Argo CD 进容器——改 `argocd-cm` 开 `exec` + 终端环境（sh/bash），Pod 详情多出终端入口

## 一、场景引入：日常运维的六个动作

Argo CD 的「配」讲完了（#77~#79），本篇讲「用」——课程挑的六个最高频运维动作：**回滚、看日志、同步、Webhook、删除、页面增强（横幅/终端）**。它们共同构成一个 SRE 使用 Argo CD 的日常动线，每个动作背后都有容易踩的语义细节。

## 二、回滚：历史版本与「不明显」的官方方案

### 2.1 操作路径

**应用 → 历史版本与回滚 → 选中版本 → 回滚**。

### 2.2 版本辨认靠 commit message

怎么确认回滚的是哪个版本？课程给的方法：「第一个方法是看我们的一个 commit id，或者说来查看我们的一个提交的一个信息。比如说我们提交的一个消息是什么内容，那我们可以通过这个内容来判断这个是不是我们要回滚的一个版本。」——实拍里提交信息「历史版本改为三，默认为六」就是版本的身份标识。

**这直接推出团队纪律：git 提交信息必须写清改了什么**（镜像版本、配置项），否则回滚时面对一串 SHA 无从下手。课程也坦白这个方案「并不明显」——回滚界面只显示时间和消息，不显示 diff，容易回错。**结论：回滚首选 Argo Rollout（#83，版本语义清晰 + 一键 abort），Argo CD 自带回滚是兜底**。

## 三、Pod 日志：单容器与多副本的正确打开方式

课程的日志方法论，一个高频效率点：

| 看法 | 路径 | 效果 |
| --- | --- | --- |
| **单 Pod 单容器** | Pod → 三个点 → log | 只看当前 Pod 当前容器 |
| **单 Pod 多容器** | Pod → log → 容器选择器 | 切换看不同容器 |
| **多 Pod 聚合** | **RS → 三个点 → log** | **同时查看所有 Pod 的日志** |

「如果我们在单个 Pod 里面点击三个点，然后点 log 来查看的话，那只能查看当前的日志，而在 RS 里面点 log 查看的话，可以查看多个 Pod 的日志。」——多副本服务排障，从 RS 进日志是标准动作，逐个 Pod 翻是原始社会。

## 四、同步：全局与局部

两种粒度的 sync（与 #79 状态机联动）：

- **全局同步**：页面顶部 sync——同步所有更改的资源；
- **局部同步**：某资源（如 Ingress）三个点 → sync——只同步该资源里更改过的字段。

典型用法：全量变更走全局；只动了 ingress 规则就局部同步，减少无关资源的 apply 抖动。

## 五、Webhook：从 3 分钟到秒级

### 5.1 原理与配置

Argo CD 默认 3 分钟轮询 git，**配 webhook 后提交即触发**。路径：**代码仓库 → 设置 → Webhook**：

| 配置项 | 填法 |
| --- | --- |
| URL | Argo CD 登录地址 + `/api/webhook` |
| 触发事件 | **推送事件**（打勾） |
| SSL 验证 | 演示环境**关掉** |
| Secret（可选） | 不配则不需要密码 |

### 5.2 Secret 验证（可选加固）

要验证就编辑 `argocd-secret` 加一段：

```yaml
stringData:
  webhook.gitlab.secret: 输入你的secret字符串不需要双引号括起来
```

课程特别提醒「不需要使用双引号括起来」——YAML 字符串引号的细节坑。

### 5.3 验证效果

课程实拍：把配置从 6 改成 3 → 提交 → 「可以看到这边已经更改……这个触发已经成功了，所以我们添加了 webhook，这样就可以实时的来更新我们的一个服务配置。那如果我们不加 webhook 的话，它就会有一个三分钟的延时。」

## 六、应用删除：页面删 vs 终端删的语义鸿沟

这是本篇**最容易造成事故**的知识点，课程专门对比：

| 方式 | 删掉什么 | K8s 应用 |
| --- | --- | --- |
| **页面删除** | Argo CD Application **+** K8s 应用 | **一起删除** |
| **终端删除**（`kubectl delete -f application.yaml`） | 只删 Argo CD Application | **继续运行** |

> ⚠️ **风险提醒（危险操作，执行前必读）**
> - **页面删除是「连锅端」**：Argo CD 应用 + 集群里的 Deployment/Service/Pod 一起没，**生产环境等同于停服**。执行前确认：① 该应用确实要下线；② 已通知业务方；③ 集群里有可用备份/清单可恢复（Application YAML 与业务清单都在 git 里，恢复只需重新 apply）。
> - **终端删除前先 `--dry-run` 看影响面**：`kubectl delete -f application.yaml --dry-run=client` 确认删的是预期对象，再去掉参数真删。
> - **回滚方案**：两种删除都能恢复——`kubectl apply -f application.yaml`（重建管理关系）+ Argo CD sync（重建集群资源）。**前提是 YAML 在 git 里有版本**（#77 第 8 条「Application YAML 也要版本化」就是这个用途）。

「终端删除的话，只会删除 Argo CD 应用，它不会删除 K8s 应用。也就是说我们只会删除 Application，但是我们 K8s 的应用仍然存在。」——**终端删 = 解除管理关系但服务不停**，这个特性可用于「Argo CD 下线但业务续跑」的迁移场景；反之页面删是连锅端。

**ApplicationSet 的应用**（#78）：页面删不掉，只能 `kubectl delete -f applicationset.yaml` 级联删全部——**这是级联删除，一次干掉该生成器渲染出的所有 Application 及其集群资源**，务必先 `kubectl get application -l app.kubernetes.io/instance=<appset名>` 看清要删多少，再执行。

## 七、页面增强：横幅与容器终端

### 7.1 横幅（argocd-cm 四行）

用途：系统公告、常用链接跳转（课程示例跳转「百度」占位，生产可放 Argo Rollout Dashboard 地址）。改 `argocd-cm` configmap 加四行：

```yaml
data:
  # 内容 + 跳转链接 + 永久粘性(true=一直在) + 位置(bottom/top)
  ui.bannercontent: "系统维护通知：今晚 22:00 升级"
  ui.bannerurl: "https://example.com/notice"
  ui.bannerpermanent: "true"
  ui.bannerposition: "bottom"
```

课程实拍：保存后刷新页面横幅出现，点击跳转；改 `bottom`→`top` 横幅从头/底切换。**永久粘性 = true 时横幅永驻**，适合放长期公告或 Rollout 面板入口。

### 7.2 容器终端（argocd-cm 两行）

默认 Argo CD 页面**进不了容器终端**，改 `argocd-cm` 加两行开启：

```yaml
data:
  exec.enabled: "true"      # 开启容器终端
  exec.shell: "sh"          # 终端环境：sh / bash / cmd
```

保存后 Pod 详情多出**终端入口**——点击直接进容器的 sh 环境。多容器 Pod 会列出各容器名，选哪个进哪个。**排障价值**：不用 `kubectl exec` 切上下文，Argo CD 页面里从应用 → Pod → 终端一条路直达；配合 RBAC 的 `exec` 权限（#81）可控谁能进。

## 八、生产实践要点

1. **删除前默念语义**：页面删连 K8s 应用一起没；终端删只解除管理。要「停服并清理」才用页面删。
2. **提交信息规范是回滚的前置**：约定「镜像版本 + 变更内容」格式，否则历史版本列表对回滚毫无帮助。
3. **Webhook 生产必配**：3 分钟轮询对 CI/CD 反馈环太慢；配 secret 验证防恶意触发。
4. **exec 权限从严**：容器终端 = 页面直达容器 shell，RBAC 里 `exec` 授权只给必要的运维角色（#81）。
5. **横幅做公告位**：维护窗口、发布冻结期用永久粘性横幅公示，比群发邮件可靠。
6. **多副本排障从 RS 进日志**：聚合日志一次看全，别逐个 Pod 翻。
7. **ApplicationSet 删除走 YAML**：培训团队别在页面跟生成的应用较劲。

## 九、报错排查表

| 现象 | 根因 | 解法 |
| --- | --- | --- |
| Webhook 触发没反应 | URL 错/事件没勾/secret 不匹配 | 核对 `/api/webhook` 路径与事件；secret 两侧一致 |
| Webhook 报 SSL 错 | 自签证书 + 开着 SSL 验证 | 演示关 SSL 验证；生产换有效证书 |
| 回滚后不确定回对没 | 提交信息没写清 | 规范提交信息；优先用 Argo Rollout 回滚 |
| 页面删了应用 Pod 还在跑 | 用了终端删（只删 Application） | 预期行为；要连 Pod 删用页面删 |
| 页面找不到删除按钮（生成的应用） | ApplicationSet 生成物 | `kubectl delete -f applicationset.yaml` 级联删 |
| Pod 详情没有终端入口 | `exec.enabled` 没配 | argocd-cm 加两行；确认 RBAC 有 exec 权限 |
| 横幅不显示 | argocd-cm 四行拼错/位置值错 | 核对四个 key 与 position 取值 |

## 十、面试考点与追问

**Q1：Argo CD 页面删除与终端删除的区别？**
页面删除 = Application + K8s 应用一起删（连锅端）；终端删除 = 只删 Application，K8s 应用继续运行（解除管理不停服务）。ApplicationSet 生成的应用只能终端级联删。

**Q2：如何辨认回滚到哪个版本？**
看历史版本的 commit id 与提交信息——前提是团队提交信息规范（写清镜像版本与变更）。Argo CD 回滚不显示 diff 易回错，生产优先用 Argo Rollout 的回滚。

**Q3：看多副本 Pod 日志的正确方式？**
从 RS 资源进 log——同时查看所有 Pod 的聚合日志；单个 Pod 的 log 只看当前 Pod。

**Q4：Webhook 怎么配？不配会怎样？**
仓库设置 → Webhook → URL 填 Argo CD 地址 + `/api/webhook` → 勾选推送事件 →（可选 secret）。不配则依赖默认 3 分钟轮询，提交后有最长 3 分钟延时。

**Q5：argocd-cm 里横幅和容器终端各配什么？**
横幅四行：`ui.bannercontent`/`ui.bannerurl`/`ui.bannerpermanent`/`ui.bannerposition`。容器终端两行：`exec.enabled: "true"` + `exec.shell: "sh"`（sh/bash/cmd）。

**Q6：容器终端开了就有入口吗？**
还要 RBAC 授权——`exec` 资源的动作权限（#81 权限配置里那条 `exec` 策略就是为它准备的）。

## 📎 文本↔代码关联

| 代码文件 | 正文提及 | 内容 |
| --- | --- | --- |
| `code/10-Argocd/webhook-secret/argocd-secret.txt` | 5.2 Secret 验证 | Webhook secret 配置样例：`kubectl edit secret argocd-secret -n argocd` + `stringData: webhook.gitlab.secret:` 字段（字符串不需双引号），对应正文「可选加固」段 |
| `code/10-Argocd/app-cli/app-cli.txt` | 第二节回滚 CLI、第六节终端删除 | argocd CLI 操作清单：`argocd app list/get/delete/sync`、`--sync-policy automated`、`--auto-prune`、`--self-heal`——终端删除与同步开关的命令行入口 |

**技术点总结**：本篇是 Argo CD 的日常运维手册，核心是六个动作的语义细节：**回滚**认 commit message（不显示 diff，生产优先 Rollout）、**日志**多副本从 RS 进聚合视图、**同步**分全局与局部、**Webhook** 把 3 分钟轮询压成秒级（secret 可选加固）、**删除**页面连 K8s 应用一起没而终端只解除管理（语义鸿沟防事故）、**页面增强**横幅四行 + 容器终端两行（exec 需 RBAC 授权）。把这些动作的正确姿势固化下来，Argo CD 才算真正进入日常。

