# 48. K8s 管道配置：克隆、步骤插件空间、触发器与 when

## 纲要

- **管道三件套定位一切**：`kind: pipeline` + `type: kubernetes` + `name: default`，type 可选 kubernetes / docker / ssh / exec，K8s 管道每步骤一个 Pod
- **克隆是默认动作但可定制**：`clone.depth: 1` 浅克隆解决大仓库龟速；`clone.disable: true` 关掉默认克隆，改用自定义 clone 步骤（name/image/commands 三要素缺一不可）
- **步骤 = 一串在 /drone/src 下执行的命令，插件 = 封装命令的镜像**：官方插件市场开箱即用，k8s 部署类插件能直接更新集群 Deployment
- **工作空间 /drone/src 是「构建内共享、构建间隔离」**：同一次构建的步骤间文件互通；每次构建都是全新目录，上一次的产物不会残留
- **trigger 决定「什么事件触发什么分支」**：`trigger.branch` + `trigger.event: push` 白名单制，没列进来的分支提交一千次也不触发
- **when 决定「步骤在什么状态下执行」**：`when.status: failure` 让失败报警步骤在流水线失败时仍然执行——这是 Drone 报警的标准姿势

## 一、场景引入：会跑 hello world 之后，真要写流水线了

前四篇把 Drone 的「是什么 → 怎么装 → 权限怎么管 → Runner 怎么部署」走完了。从本篇开始进入**管道配置**深水区——`.drone.yml` 怎么写。

这是整个 Drone 章节信息密度最高的部分，课程拆成三小节：**克隆（一）、步骤/插件/空间（二）、触发器与 when（三）**。本篇按原顺序合并讲透，所有结论都来自课件里十几次真实构建的页面观察，不是纸上参数。

先建立地图：一条 `.drone.yml` 的完整生命周期是——**trigger 判断要不要跑 → clone 拉代码 → steps 逐步执行（when 控制条件）→ 每一步的产物落在 /drone/src**。本篇把这四个环节一次讲完。

## 二、核心概念与原理

### 2.1 管道三件套与类型选型

任何 Drone 流水线的第一行永远是三件套：

```yaml
kind: pipeline    # 资源类型，固定 pipeline
type: kubernetes  # 管道类型
name: default     # 管道名称，自定义
```

`type` 决定执行引擎（详见 #47）：`kubernetes`（K8s Runner，每步骤一个 Pod，课程主线）、`docker`（Docker Runner，每步骤一个容器）、`ssh`（远程主机）、`exec`（Runner 本机）。**同一仓库可以配多条同名不同 type 的管道吗？不行——`name` 是流水线身份，靠不同 name 区分不同流水线**（如 `default` / `release`）。

### 2.2 克隆：默认行为与两个开关

Drone 默认在流水线最前面插入一个**自动 clone 步骤**（页面可见、不可删除但可禁用），把仓库代码拉到工作空间。它的两个配置开关：

| 配置 | 作用 | 场景 |
| --- | --- | --- |
| `clone: depth: 1` | **浅克隆**：只取最近一次提交历史 | 大仓库必备。默认全量克隆在提交历史庞大的仓库里耗时几分钟到几十分钟 |
| `clone: disable: true` | **关掉默认克隆** | 需要自己控制克隆逻辑时（如带凭据的定制克隆） |

浅克隆的代价：构建内拿不到完整 git 历史——需要 `git log` 全量、按 tag 差分、计算变更文件集的场景要权衡。

### 2.3 步骤与插件：一个硬币的两面

课程定义：**步骤（step）是被定义为一系列 docker 命令的执行单元，所有命令都在仓库根目录（实际是工作空间 /drone/src）中执行**；**插件（plugin）是封装命令的 docker 容器**。

```mermaid
flowchart LR
    A[".drone.yml<br/>steps 列表"] --> B["step = name + image + commands<br/>三要素缺一不可"]
    B --> C["commands 在<br/>/drone/src 下执行"]
    D["官方插件市场<br/>plugins/*"] --> E["插件 = 预封装镜像<br/>settings 传参"]
    E --> B
```

**步骤三要素**：`name`（步骤名）、`image`（执行镜像）、`commands`（命令列表）。少任何一个，流水线直接报错。

**插件生态**：Drone 官方插件市场（drone-plugins）提供大量预封装镜像——部署类（K8s deployment 插件可直接更新集群 Deployment 容器，不需要准备额外文件）、构建类（docker / kaniko）、通知类（钉钉、飞书、企业微信）、扫描类（sonar）等。**注意血统**：插件市场由 eBay 主导，AWS 向镜像占绝大多数，**阿里云/腾讯云/华为云等国内云厂商插件基本没有**——对接国内云服务要么用官方插件拼 CLI，要么自制插件镜像。

**多行命令写法**：commands 下用 `- |` 加缩进块写多行 shell，比堆多条 `-` 更可读：

```yaml
commands:
- |
  ls -la
  pwd
```

### 2.4 工作空间：/drone/src 的共享与隔离语义

**共享**：同一次构建内，所有步骤共享 /drone/src——step1 里 `touch a.txt`，step2 里 `ls` 能看到。这是步骤间传文件的默认通道（#49 会讲卷的进阶用法）。

**隔离**：**不同构建之间，工作空间完全独立、互不影响**。课程做了对照实验：第 4 次构建 step1 创建了 `a.txt`，step2 可见；删掉文件后第 5 次构建重新拉代码，`a.txt` **不存在**。所以「把构建产物放到工作空间留给下次用」是错误心智——**跨构建留存数据必须用卷（PVC）或外部存储**。

### 2.5 触发器：白名单制的事件过滤

`trigger` 决定「什么事件、什么分支才启动流水线」：

```yaml
trigger:
  branch:
  - test      # 只有这些分支的提交才触发
  - main
  event:
  - push      # 只有 push 事件触发（另有 tag、pull_request 等）
```

语义要点：

1. **白名单制**：分支没列进来（如课程演示的 `pre` 分支），提交多少次都不会自动触发。
2. **`event` 与 `branch` 是「与」关系**：分支命中且事件类型命中才触发。
3. **`.drone.yml` 文件名必须与仓库激活时配置的名字一致**——课程演示中文件名差一个字符（`onel.yml` vs `a.yml`）导致提交无反应，改名后才触发。这是最隐蔽的坑：**不报错、不触发，只是安静地不工作**。

### 2.6 when：步骤级条件执行

`when` 控制单个步骤的执行条件，核心是 `status`：

| 配置 | 语义 |
| --- | --- |
| `when: status: [failure]` | 前面有步骤失败时执行（**失败报警的标准姿势**） |
| `when: status: [success]` | 前面全部成功时执行（**成功通知**） |

默认行为对照：**不带 when 的步骤，只要前面有步骤失败，整条流水线终止、后续步骤一律不执行**；而 `when.status: failure` 的步骤会「逆流而上」——流水线失败它照样跑。由此得到 Drone 报警的标准范式：**把报警步骤放最后，配 `when.status: failure`**，构建失败即发通知到群里；配 `success` 则构建成功发通知。when 一般只配在最后一个步骤。

## 三、动手实践：三个课件实例逐行拆解

### 3.1 实例一：克隆操作（自定义克隆 + 验证）

`code/7-Drone/drone.yml-克隆操作` 完整演示「关掉默认克隆 → 自己克隆 → 验证」：

```yaml
kind: pipeline    # 资源类型
type: kubernetes  # 管道类型：kubernetes、docker、ssh、exec等
name: default     # 管道名称

clone:
  disable: true   # 关掉默认克隆步骤
  #depth: 1       # 浅克隆开关（本例关掉默认克隆，故注释）

steps:
- name: custom-clone          # 自定义克隆步骤
  image: alpine/git           # 带 git 的镜像
  commands:
  - git clone http://root:${GIT_PASSWORD}@gitlab.example.com/golang/go.git

- name: ls-file               # 验证克隆结果
  image: alpine
  commands:
  - |                         # 多行命令块
    ls -la
    pwd
```

逐字段拆解：

| 字段 | 值 | 作用 |
| --- | --- | --- |
| `clone.disable` | `true` | 关闭默认 clone 步骤——页面构建记录里不再出现自动 clone |
| `steps[0].name` | `custom-clone` | 自定义克隆步骤名，页面按它标识 |
| `steps[0].image` | `alpine/git` | 内置 git 客户端的镜像 |
| `steps[0].commands` | `git clone http://root:${GIT_PASSWORD}@...` | 带凭据克隆：密码用**环境变量/Secret 注入**（`${GIT_PASSWORD}`），不明文写死 |
| `steps[1].commands` | `- |` + `ls -la` / `pwd` | 多行命令块；顺带验证工作空间就是 /drone/src |

构建记录里能看到完整现场：默认 clone 消失、custom-clone 成功、ls-file 打出仓库文件与 `/drone/src` 路径。**自定义克隆的典型价值**：需要凭据注入、需要 clone 后做 checkout 指定分支/tag、需要 monorepo 部分拉取等默认克隆搞不定的场景。

### 3.2 实例二：工作空间与步骤（构建内共享实验）

`code/7-Drone/drone.yml-工作空间与步骤`：

```yaml
kind: pipeline      # 资源类型
type: kubernetes    # 管道类型
name: default       # 管道名称

clone:
  depth: 1          # 浅克隆

steps:
- name: step1
  image: alpine
  commands:
  - ls -la

- name: step2
  image: alpine
  commands:
  - pwd
  - ls -la
```

课程在此文件基础上做了经典实验：在 step1 加 `touch a.txt`、step2 加 `ls -la` → **step2 能看到 a.txt**（构建内共享）；删掉 touch、重新构建 → **新构建的工作空间里没有上一次的 a.txt**（构建间隔离）。这条经验直接决定工程习惯：**同一构建内用 /drone/src 传文件；跨构建必须上卷或外部存储**。

### 3.3 实例三：触发器与 when（分支过滤 + 失败报警）

`code/7-Drone/drone.yml-触发器与when`：

```yaml
kind: pipeline   
type: kubernetes  
name: default    

clone:
  depth: 1

steps:
- name: step1
  image: alpine
  commands:
  - laqw                 # 课程演示用的占位命令（替换为真实命令即正常）

- name: alert             # 报警步骤
  image: alpine
  commands:
  - echo "alert..." 
  when:
    status:
    - failure             # 前面有失败才执行
    #- success            # 全成功才执行（二者按需取一）

trigger:      
  branch:
  - test                  # 只在这些分支触发
  - main  
  event:
  - push                  # 只 push 事件触发
```

逐字段拆解：

| 字段 | 作用 |
| --- | --- |
| `trigger.branch` | `test` / `main` 白名单：只有这两个分支的提交触发构建；演示中 `pre` 分支提交**无任何反应** |
| `trigger.event` | `push` 事件类型（另有 `tag`、`pull_request`、`cron` 等） |
| `steps[1].when.status: [failure]` | alert 步骤的条件：前面有步骤失败才执行 |

课程的对照实验走完了全部三种状态：

1. **failure 不执行**：step1 命令成功 → alert 步骤一条中划线跳过（页面显示 skipped）；
2. **success 执行**：when 改 `success` → 前两步全成功 → 第三步正常执行；
3. **failure 触发**：把 step1 命令改成不存在的命令 → step1 失败 → **alert 步骤立即触发执行**。

这就是生产报警的最小闭环：`when.status: [failure]` + 通知插件（钉钉/飞书/企业微信，#52 详解），把「构建失败」变成「群里立刻知道」。

## 四、生产实践要点

1. **浅克隆按仓库规模默认开启**：`clone: depth: 1` 对大仓库是分钟级的节省；但需要完整历史的场景（changelog 生成、按 tag 差分、monorepo 变更检测）要显式调大或关闭——在流水线里加一个「需要历史吗」的判断，别一刀切。
2. **自定义克隆的凭据必须走 Secret**：`git clone http://root:${GIT_PASSWORD}@...` 里的密码用 Secret 注入（#50 详解 from_secret），明文写进 `.drone.yml` = 把仓库密码提交进 Git。
3. **插件镜像锁版本**：官方插件市场镜像同样会发新版，`image: plugins/xxx:latest` 的行为漂移风险与 #44 同理——生产锁 tag。
4. **插件市场国内云短板要预判**：AWS 向为主，对接阿里云/腾讯云时优先评估「官方 CLI 打底 + 通用插件」的方案，或自制内部插件镜像收敛调用方式。
5. **trigger 白名单 + 分支保护联动**：只给 `main`/`release` 配触发，功能分支的流水线改用手动触发或 MR 事件；配合 GitLab Protected Branch，实现「主干门禁、分支自由」。
6. **报警步骤标准化**：所有仓库的 `.drone.yml` 统一带最后一步 `notify`（`when.status: [failure]`），报警内容至少含：仓库、分支、commit、构建链接（内置变量，#50 讲）、失败步骤名——照 #17 篇 Jenkins 报警的字段标准执行。
7. **when 只放最后一步**：中间步骤挂 when 会让流水线控制流难以推理（失败后哪些跑了哪些没跑，读配置的人要画状态机）。报警/通知是 when 的 90% 场景，放最后足够。
8. **/drone/src 不要当缓存**：课程实验证明构建间隔离。把依赖缓存、构建产物寄托在工作空间「上次还在」的团队，会在某次偶发失败后浪费半天排查一个不存在的玄学。

## 五、报错排查表

| 现象 | 根因 | 解法 |
| --- | --- | --- |
| 提交代码后完全不触发构建 | 分支不在 `trigger.branch` 白名单；或 `.drone.yml` 文件名与仓库配置的名字不一致 | 补分支名；核对仓库激活时配置的流水线文件名（差一个字符都不行） |
| 默认 clone 步骤不见了 / 构建直接失败 | `clone.disable: true` 但没提供自定义克隆步骤 | 二选一：去掉 disable，或补带 git 镜像的自定义 clone 步骤 |
| 大仓库克隆耗时几分钟 | 未配浅克隆，默认全量拉历史 | `clone: depth: 1` |
| 克隆步骤报 403 / authentication failed | 克隆 URL 里的凭据失效或未注入 | 用 Secret 注入密码；确认账户对仓库有权限 |
| 自定义 clone 用 alpine 镜像报 `git: not found` | 镜像里没有 git | 换 `alpine/git` 或先 `apk add git` |
| step2 看不到 step1 创建的文件 | kubernetes 管道每步骤独立 Pod——除非默认共享 /drone/src，写文件写到了别的路径 | 确认文件写在 /drone/src（默认工作目录）下 |
| 上次构建的产物这次不见了 | 工作空间**构建间隔离**，本就如此 | 跨构建留存用 PVC/外部存储（#49 展开） |
| 报警步骤（alert）从不执行 | when 配的是 `success` 而前面失败了；或步骤没放对位置 | 失败报警用 `status: [failure]`；放最后一个步骤 |
| 失败时报警执行了，成功时也想通知却不动 | when 只有一种 status | 需要双通知就配两个步骤分别挂 failure / success |
| YAML 报错 `mapping values are not allowed` | commands 多行块缩进不齐，或 `- |` 后没换行 | `- |` 后必须换行，块内统一缩进 |

## 六、面试考点与追问

**Q1：Drone 流水线的 `type` 有哪几种？生产常用哪种？**
`kubernetes`、`docker`、`ssh`、`exec`。生产常用 `kubernetes`——每步骤一个 Pod，资源弹性、故障隔离、与集群生态打通；`docker` 绑定单机、`ssh`/`exec` 面向遗留环境。

**Q2：`clone: depth: 1` 解决什么问题？什么场景不能用它？**
解决大仓库全量克隆慢的问题，只取最近一次提交。需要完整 git 历史的场景不能用：changelog 生成、按 tag/commit 差分计算变更文件、monorepo 变更检测——这些要完整历史或调大 depth。

**Q3：禁用默认克隆后，自定义克隆步骤的最小要素是什么？**
三要素：`name`（步骤名）、`image`（带 git 的镜像如 alpine/git）、`commands`（git clone 命令）。凭据用 Secret 经环境变量注入，不明文进 Git。

**Q4：Drone 插件和 Jenkins 插件的区别是什么？**
Drone 插件是封装好命令的 docker 容器，通过镜像 + settings 使用，容器隔离、版本随 tag 固定；Jenkins 插件是安装在主进程的扩展。另外 Drone 插件市场由 eBay 主导，AWS 向为主，国内云厂商插件稀缺。

**Q5：/drone/src 的共享与隔离语义是什么？对工程习惯有什么要求？**
同一次构建内所有步骤共享 /drone/src（步骤间传文件的默认通道）；不同构建之间完全隔离（上次的产物不会残留）。要求：构建内传文件放工作空间，跨构建留存数据必须用卷（PVC）或外部存储，不能把工作空间当缓存。

**Q6：`trigger.branch` 没配的分支提交了代码，会发生什么？**
什么都不发生——不触发、不报错、构建列表安静如鸡。这是白名单制的设计，也是最隐蔽的坑：配合「`.drone.yml` 文件名与仓库配置不一致」这类静默失败，排查时先看这两个。

**Q7：`when.status: failure` 的执行时机是什么？为什么报警步骤都配它？**
当前面存在失败步骤时执行。默认语义是「前序失败则流水线终止、后续不执行」，而挂 `failure` 的步骤会逆流执行——所以失败报警（通知群、回收环境、归档日志）统一用它，放在最后一个步骤。成功通知则用 `status: [success]`。

**Q8：一条流水线里 trigger 和 when 的分工是什么？**
trigger 是**流水线级门卫**（什么事件+什么分支才启动整条流水线）；when 是**步骤级开关**（流水线已经跑起来了，这一步在什么状态下执行）。一个管入口，一个管内部控制流。

## 📎 文本↔代码关联

| 代码文件 | 正文提及 | 内容 |
| --- | --- | --- |
| `code/7-Drone/drone.yml-克隆操作` | 3.1 节 | `clone.disable: true` 关默认克隆 + `custom-clone` 自定义克隆（alpine/git + 凭据注入）+ `ls-file` 多行命令验证（`- \|` 块） |
| `code/7-Drone/drone.yml-工作空间与步骤` | 3.2 节 | 最小两步串行骨架（step1/step2 均 alpine），课程在其上做「构建内共享 / 构建间隔离」对照实验 |
| `code/7-Drone/drone.yml-触发器与when` | 3.3 节 | `trigger.branch`（test/main 白名单）+ `trigger.event: push` + alert 步骤 `when.status: [failure]` 失败报警范式 |

**技术点总结**：`.drone.yml` 的四个控制面在本篇全部就位——**克隆**（`depth: 1` 浅克隆提速、`disable: true` 后自定义 clone 三要素 name/image/commands，凭据走 Secret）、**步骤与插件**（步骤=name+image+commands、命令跑在 /drone/src、插件=预封装镜像但国内云生态稀缺）、**工作空间**（构建内步骤间共享 /drone/src、构建间完全隔离，缓存必须用卷）、**触发与条件**（trigger 白名单制过滤分支+事件，没配的分支安静不触发；when.status 让失败报警步骤逆流执行，是 Drone 报警标准范式）。两个最深的静默坑：`.drone.yml` 文件名与仓库配置不一致、分支不在 trigger 白名单——都不报错，只是不工作。

