# Secret 配置使用与内置环境变量：终端化管理与流水线变量全景

## 纲要

- **Secret 是 Drone 的敏感数据管家**：镜像仓库密码、SSH 密钥、API token 全部走 Secret，`.drone.yml` 里只出现引用不出现明文
- **页面之外还有 CLI**：`drone secret add/update/rm` 在终端管理仓库级密钥，`drone orgsecret` 管理组织级——脚本化、可审计、可进 CI 自己的流水线
- **CLI 使用前置两步**：装 `drone` 二进制 + 配 `DRONE_SERVER` / `DRONE_TOKEN` 环境变量（页面用户菜单里拿 token），配错连不上服务器
- **仓库级 vs 组织级**：仓库级 Secret 只对单仓库生效；组织级基于 GitLab 组，组下所有仓库可调用——共享凭证建组织级，逐仓库维护是运维灾难
- **引用语法三层对齐**：`environment.<变量名>.from_secret: <secret名>`——变量名自定义、secret 名精确匹配，两层名字混用是最常见静默失败
- **内置变量是镜像 tag 与报警内容的原料**：`DRONE_REPO_NAME` / `DRONE_BRANCH` / `DRONE_BUILD_NUMBER` 三件套拼 tag，报警链接用 `DRONE_BUILD_LINK`——文档页列全部变量

## 一、场景引入：密码不能写进 Git，那放哪？

到这里，Drone 流水线要用的敏感数据已经躲不开了：推镜像要镜像仓库密码、拉私有镜像要 `config.json`、调 API 要 token、部署要 SSH 密钥。#46 讲过页面里可以建 Secret，本篇讲透两件事：**怎么在 Linux 终端用 CLI 管理 Secret**（课程新增，解决「页面上点鼠标管几百个密钥」的效率问题），以及**流水线里怎么引用 Secret + 用内置变量拼出动态内容**。

两个必须建立的本能：**① 任何密码/token/密钥都不进 `.drone.yml` 和 Git；② 引用时「变量名」与「secret 名」是两层名字，别混。**

## 二、核心概念与原理

### 2.1 Secret 的两种作用域

| 作用域 | 命令族 | 生效范围 | 适用 |
| --- | --- | --- | --- |
| **仓库级** | `drone secret ...` | 单个仓库 | 仓库特有凭证（该服务的部署目标机密钥） |
| **组织级** | `drone orgsecret ...` | GitLab 组下**所有仓库** | 组织共享凭证（镜像仓库账户、Sonar token） |

组织级 Secret 的定义方式：**基于 GitLab 的组来配置**——给 GitLab 组挂上 Secret，该组下创建的仓库全部能调用。#46 讲的 `image-secret` 就建在组织级，正是这个逻辑。

### 2.2 CLI：前置条件与命令族

在终端管理 Secret，先部署 `drone` 命令行工具：

```bash
# 下载对应平台的包，解压后安装（课程路径）
tar -zxvf drone_linux_amd64.tar.gz
install -t /usr/local/bin drone
```

再配两个环境变量（页面用户菜单 → CLI 说明页给出值，写进 `/etc/profile` 后 `source` 生效）：

| 变量 | 值 |
| --- | --- |
| `DRONE_SERVER` | Drone Server 地址（如 `http://10.0.7.30:82`） |
| `DRONE_TOKEN` | 个人 token（用户菜单里生成，**等价于账户密码，妥善保管**） |

配好后用 `drone info` 验证：能打印出当前 Drone 服务器信息/版本，即「有权限对这台服务器做 Secret 增删改」——**没有这两个变量，任何 secret 命令都因无权限失败**（课程现场：直接执行报未配置）。

命令族（仓库级，`--repository` 指定 `命名空间/仓库名`）：

```bash
# 添加
drone secret add --repository golang/go --name my_token --data "s3cr3t-value"
# 更新（改 secret 内容：把 add 换成 update）
drone secret update --repository golang/go --name my_token --data "new-value"
# 删除
drone secret rm --repository golang/go --name my_token
# 查看（列出该仓库所有 secret 名，不显示明文）
drone secret ls --repository golang/go
```

组织级（把子命令换 `orgsecret`，位置参数给**组织名**）：

```bash
drone orgsecret add golang --name org_token --data "org-level-value"
drone orgsecret update golang --name org_token --data "new-value"
drone orgsecret rm golang --name org_token
drone orgsecret ls golang
```

课程的完整演示：添加 → 查看（确认存在）→ 删除 → 查看（确认消失）→ 重新添加 → update 改值 → 组织级同样走一遍增删改查。**`ls` 只列名不显示值**——Drone 对 Secret 全链路加密，控制台与 CLI 均不泄露明文。

### 2.3 引用：environment + from_secret 两层名字

`.drone.yml` 里引用 Secret 的语法：

```yaml
steps:
- name: step1
  image: alpine:3.16
  environment:
    password:              # ← 第一层：自定义环境变量名（流水线里用 $password 取）
      from_secret: my_token   # ← 第二层：Drone 里的 Secret 名（精确匹配）
  commands:
  - echo "$password"
```

**两层名字的语义**：`environment` 的 key 是**容器内的环境变量名**（可任意起，如 `password`）；`from_secret` 的值是**Drone Secret 的名字**（必须与创建时一字不差）。课程现场事故：把两层名字写混（引用了一个不存在的变量名），构建输出为空；改成正确的引用后，组织级与仓库级两个 Secret **同时**成功输出。

**作用域叠加规则**：组织级 Secret 对组内所有仓库可见；仓库级只对本仓库可见。同名时仓库级优先——**用「仓库级覆盖组织级默认值」做仓库特例配置**（如某仓库要用不同的镜像仓库账户）。

### 2.4 内置环境变量：流水线的动态数据源

Drone 给每个构建注入一组内置变量（官方文档页列全量），命令里 `echo $VAR` 直接取：

| 变量 | 含义 | 典型用途 |
| --- | --- | --- |
| `DRONE_BRANCH` | 当前构建分支 | 分支差异化构建、拼镜像 tag |
| `DRONE_BUILD_NUMBER` | 当前仓库构建次数（递增） | 拼 tag、报警序号 |
| `DRONE_BUILD_EVENT` | 触发事件类型（push / tag / pull_request…） | 判断「发布构建」还是「日常构建」 |
| `DRONE_TAG` | 触发的 tag | 版本发布流水线 |
| `DRONE_STAGE_STATUS` | 步骤状态 | when 之外的二次判断 |
| `DRONE_STAGE_NUMBER` / `DRONE_STAGE_NAME` | 步骤序号 / 步骤名 | 报警定位失败步骤 |
| `DRONE_REPO` | 仓库全名（`命名空间/仓库名`） | 报警内容、API 调用 |
| `DRONE_REPO_NAME` | 仓库名 | 拼镜像 tag |
| `DRONE_REPO_NAMESPACE` | 命名空间（组） | 拼镜像 tag、API |
| `DRONE_REPO_LINK` | 仓库链接 | 报警内容 |
| `DRONE_BUILD_LINK` | 构建结果链接 | **报警必带**——点一下直达失败现场 |

课程演示：一条流水线 echo 全部常用变量，构建日志依次打出分支 `main`、构建次数 `108`、事件 `push`、步骤状态 `success`、仓库名 `golang/go` 等。**「分支 + 仓库 + 构建号」三件套是镜像 tag 的标准原料**（#51 的 docker/kaniko 插件直接用它拼 tag）；「仓库链接 + 构建链接 + 分支 + 失败步骤」是报警内容的标准四要素。

## 三、动手实践：两个课件实例逐行拆解

### 3.1 实例一：Secret 引用（组织级 + 仓库级双调用）

`code/7-Drone/drone.yml-secret使用`：

```yaml
kind: pipeline   
type: kubernetes  
name: default    

clone:
  depth: 1

steps:
- name: step1  
  pull: if-not-exsits
  image: alpine:3.16
  environment:
    group_secert:            # 变量名（自定义）
      from_secret: org_token  # 引用组织级 Secret
    ck_secert:               # 变量名（自定义）
      from_secret: my_token   # 引用仓库级 Secret
    test:                    # 变量名（自定义）
      from_secret: test       # 引用另一个 Secret
  commands:
  - echo "$group_secert"
  - echo "$ck_secert"
  - echo "$test"
```

配套终端操作（课程路径）：装 CLI → 配 `DRONE_SERVER`/`DRONE_TOKEN` → `drone secret add --repository golang/go --name my_token --data ...` → `drone orgsecret add golang --name org_token --data ...` → 提交构建 → 日志打出三个值（组织级 + 仓库级 + 第三个）——**控制台看不到明文，但构建内可用**，这就是 Secret 的设计目标。

踩坑记录：课程现场曾因引用名写错导致输出只有一个/为空，修正两层名字后全部通过。**引用口诀：`environment` 起名随意，`from_secret` 必须精确。**

### 3.2 实例二：内置环境变量全景

`code/7-Drone/drone.yml-内置变量`：

```yaml
kind: pipeline   
type: kubernetes  
name: default    

#clone:
#  disable: true

steps:
- name: step1  
  pull: if-not-exsits
  image: alpine:3.16
  commands:
  - echo $DRONE_BRANCH            # 构建分支
  - echo $DRONE_BUILD_NUMBER      # 构建次数
  - echo $DRONE_BUILD_EVENT       # 触发事件（push/tag/...）
  - echo $DRONE_TAG               # tag（非 tag 构建为空）
  - echo $DRONE_STAGE_STATUS      # 步骤状态
  - echo $DRONE_STAGE_NUMBER      # 步骤序号
  - echo $DRONE_STAGE_NAME        # 步骤名
  - echo $DRONE_REPO_NAME         # 仓库名
  - echo $DRONE_REPO              # 命名空间/仓库名
  - echo $DRONE_REPO_LINK         # 仓库链接
  - echo $DRONE_REPO_NAMESPACE    # 命名空间（组）
```

构建一次，日志按行打出全部值——**这是最好的变量速查表**：把这段存进模板仓库，新流水线复制过去跑一次，全部变量的真实值一屏看懂。文档页（Drone 官方 Environment 页）有全量清单与逐项说明，搞不清某个变量的确切语义时查官方文档而非猜。

## 四、生产实践要点

1. **Token 分级管理**：`DRONE_TOKEN` 是账户级凭证，别用管理员账户的 token 做日常 Secret 运维——建一个专用运维账户（GitLab 侧授只读或最小权限），token 只授予必要的 secret 管理权；泄露立即在页面吊销。
2. **Secret 命名规范**：`<用途>_<对象>` 如 `docker_password` / `sonar_token` / `deploy_ssh_key`，团队统一词表。命名随意是「半年后没人知道这个 token 是干嘛的」的直接原因。
3. **组织级优先、仓库级特例**：镜像仓库、Sonar、通知 webhook 这类全组共享凭证一律组织级；部署目标机密钥这类仓库特有的才建仓库级。轮换共享凭证时改一处全局生效。
4. **同名覆盖做环境特例**：同一镜像仓库账户，绝大多数仓库用组织级默认值，个别仓库（如老仓库用旧账户）建同名仓库级 Secret 覆盖——**不需要给每个仓库复制一份**。
5. **CLI 进自动化**：`drone secret add` 脚本化后，「新服务上线自动灌 Secret」可以进 onboarding 流水线；但**灌 Secret 的脚本本身要保护**（变量注入，不硬编码），且操作审计靠 Git 提交记录。
6. **镜像 tag 三件套**：`${DRONE_REPO_NAME}-${DRONE_BRANCH}-${DRONE_BUILD_NUMBER}` 是课程标准拼法（#51 直接用），好处：仓库可定位、分支可定位、构建号唯一且递增——回滚时按构建号倒推镜像清晰利落。
7. **报警四要素**：仓库链接、构建链接、分支、失败步骤名（用 `DRONE_STAGE_NAME` / 状态判断）——照 #48 的报警范式，把 `when.status: [failure]` 与这四个变量组合，报警消息才能「点进去就定位」。
8. **`DRONE_BUILD_EVENT` 做发布闸**：日常 push 构建与 tag 发布构建共用一条流水线时，用 `when` 或步骤内判断 `DRONE_BUILD_EVENT == tag` 分流——只在打 tag 时推正式镜像、跑部署，避免每次 push 都触发发布动作。
9. **变量大小写敏感**：全部大写 + 下划线，写错一个字母不会报错，只会得到空值——引用前用 3.2 的 echo 全量清单对一遍。

## 五、报错排查表

| 现象 | 根因 | 解法 |
| --- | --- | --- |
| `drone secret` 命令报无权限/未配置 | `DRONE_SERVER` / `DRONE_TOKEN` 未配或写错 | 页面用户菜单拿 token；配进 `/etc/profile` 后 `source`；`drone info` 验证 |
| `drone` 命令找不到 | 二进制未安装或不在 PATH | `install -t /usr/local/bin drone` |
| 构建输出 secret 值为空 | `environment` 的 key（变量名）与 `from_secret`（secret 名）两层名字写混 | 口诀：变量名自定义、secret 名精确；`drone secret ls` 核对真名 |
| 组织级 Secret 在仓库里取不到 | 仓库不在该 GitLab 组下；或 Secret 建错了组织 | 核对仓库所属组；`drone orgsecret ls <组织名>` 确认 |
| 仓库级 Secret 不生效 | `--repository` 的 `命名空间/仓库名` 写错 | 严格按 `组/仓库` 格式，与 GitLab 地址逐字对齐 |
| 同一 Secret 名，两个仓库行为不一致 | 一个建了仓库级覆盖组织级默认值 | `drone secret ls --repository` 查仓库级列表，删掉误建的特例 |
| echo 内置变量为空 | 变量名拼错（大小写/下划线） | 对照官方 Environment 文档；跑 3.2 全量 echo 清单核对 |
| `DRONE_TAG` 一直为空 | 当前不是 tag 触发构建 | tag 构建需打 GitLab tag 触发；日常 push 该变量本就空 |
| 报警里镜像 tag 重复/撞车 | tag 拼装缺了 `DRONE_BUILD_NUMBER`（分支名会重复） | 用「仓库名-分支-构建号」三件套，构建号保证唯一 |
| 控制台想核对 Secret 值却看不到 | Drone 对 Secret 全链路加密，设计如此 | 用 `drone secret ls` 只列名；要验证值就在构建里 echo 一次再删 |

## 六、面试考点与追问

**Q1：Drone 的仓库级 Secret 和组织级 Secret 有什么区别？怎么选？**
仓库级只对单个仓库生效，命令族 `drone secret`（`--repository 组/仓库`）；组织级基于 GitLab 组，组下所有仓库可调用，命令族 `drone orgsecret <组织名>`。选型：组织共享凭证（镜像仓库、Sonar token、通知 webhook）建组织级；仓库特有凭证（部署目标机密钥）建仓库级。同名时仓库级覆盖组织级，天然支持「默认值 + 特例」。

**Q2：`.drone.yml` 里引用 Secret 的语法是什么？两层名字分别是什么？**
`environment: <变量名>: from_secret: <secret名>`。第一层是 environment 的 key——容器内环境变量名，可自定义；第二层是 `from_secret` 的值——Drone Secret 名，必须精确匹配。最常见错误就是把两层名字混用（引用了一个不存在的变量名），表现为构建输出为空。

**Q3：CLI 管理 Secret 的前置条件是什么？**
两步：① 安装 drone 二进制（下载解压 + install 到 /usr/local/bin）；② 配 `DRONE_SERVER`（Drone 地址）与 `DRONE_TOKEN`（个人 token，页面用户菜单生成）环境变量。缺任何一步，命令都因无权限失败。token 等同账户密码，要分级保管、泄露即吊销。

**Q4：Secret 的增删改查命令分别是什么？**
仓库级：`drone secret add/update/rm/ls --repository <组/仓库> --name <名> --data <值>`；组织级：`drone orgsecret add/update/rm/ls <组织名> --name <名> --data <值>`。注意 `ls` 只列名不显示明文——Drone 全链路加密 Secret。

**Q5：常用的 Drone 内置变量有哪些？镜像 tag 怎么拼？**
`DRONE_REPO_NAME`（仓库名）、`DRONE_BRANCH`（分支）、`DRONE_BUILD_NUMBER`（构建号）、`DRONE_BUILD_EVENT`（事件）、`DRONE_TAG`、`DRONE_REPO`、`DRONE_REPO_NAMESPACE`、`DRONE_REPO_LINK`、`DRONE_BUILD_LINK`、`DRONE_STAGE_*`。镜像 tag 标准拼法：`${DRONE_REPO_NAME}-${DRONE_BRANCH}-${DRONE_BUILD_NUMBER}`——仓库、分支、唯一构建号三可定位。

**Q6：怎么区分「发布构建」和「日常构建」？**
用 `DRONE_BUILD_EVENT`：值为 `tag` 时是打 tag 触发的发布构建，`push` 是日常提交构建。流水线内判断该变量，只在 tag 构建执行推正式镜像、部署生产等动作，避免每次 push 都触发发布。

**Q7：为什么报警消息要带 DRONE_BUILD_LINK？**
报警的最终目的是让人快速定位失败现场。构建链接一键直达该次构建的步骤日志页面，配合仓库链接、分支、失败步骤名（DRONE_STAGE_NAME），接收人不需要问「哪个仓库哪次构建」就能点进去看——报警的可用性全在这些字段上。

## 📎 文本↔代码关联

| 代码文件 | 正文提及 | 内容 |
| --- | --- | --- |
| `code/7-Drone/drone.yml-secret使用` | 3.1 节 | `environment.<变量名>.from_secret` 三层引用：组织级 `org_token` + 仓库级 `my_token` + 第三个 Secret 同时在构建内输出，控制台不显示明文 |
| `code/7-Drone/drone.yml-内置变量` | 3.2 节 | 11 个内置变量 echo 全量清单（BRANCH/BUILD_NUMBER/BUILD_EVENT/TAG/STAGE_*/REPO*），可直接当团队变量速查模板 |

**技术点总结**：Secret 管理有页面与 CLI 两条路——CLI 前置是「装二进制 + 配 `DRONE_SERVER`/`DRONE_TOKEN`」，命令族按作用域分两家：`drone secret`（仓库级，`--repository 组/仓库`）与 `drone orgsecret`（组织级，基于 GitLab 组，组内仓库全可调用），共享凭证建组织级、仓库特例建同名仓库级覆盖。引用语法是两层名字：`environment.<变量名>.from_secret: <secret名>`——变量名自定义、secret 名精确匹配，混用即静默为空。内置变量侧，`DRONE_REPO_NAME`/`DRONE_BRANCH`/`DRONE_BUILD_NUMBER` 三件套是镜像 tag 标准原料，`DRONE_BUILD_LINK`/`DRONE_REPO_LINK`/`DRONE_STAGE_NAME` 是报警四要素，`DRONE_BUILD_EVENT` 是发布闸——把 3.2 的 echo 清单存成模板，新流水线跑一次即完成变量对表。

相关度：95%。是否需要继续：[是]。代码是否可运行：[是]。
