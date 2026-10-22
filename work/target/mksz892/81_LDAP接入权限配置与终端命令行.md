# 81. Argo CD LDAP 接入、权限配置与终端命令行

## 纲要

- **LDAP 接入走 Dex**：Argo CD 自身不直连目录——`argocd-cm` 里配 `dex.config` 连接器，账号密码拆到 `argocd-secret`，**改完必须重启 dex-server 与 argocd-server 两个 Pod**
- **目录侧先建组**：OpenLDAP 里用 `groupOfUniqueNames` 类型建 argocd 组、把用户加进去——组过滤器 `(cn=argocd)` 与它对应
- **RBAC 两行式语法**：`p` 行定义角色（role: org-x + 资源 + 动作 + 对象），`g` 行把 LDAP 组绑到角色——组内用户即获权
- **资源与动作的粒度**：资源支持 application/cluster/project/applicationset/exec；动作支持 get/create/delete/sync/update——对象用 `*` 或 `项目/应用` 限定
- **exec 权限是容器终端的钥匙**：#80 开的容器终端，靠 RBAC 里一条 `exec` 策略放行——没它终端入口点了也进不去
- **CLI 先登录再操作**：`argocd login` 是所有 app 命令的前置；list/get/delete/sync/set 一套覆盖日常

## 一、场景引入：从「能用」到「团队敢用」

单用户 admin 的 Argo CD 是 demo，团队用的 Argo CD 必须回答三个问题：**谁能登录（认证）、登录后能干什么（授权）、不登页面能不能操作（CLI）**。课程用三节讲完：LDAP 接入（认证）、RBAC 配置（授权）、CLI（命令行）。

## 二、LDAP 接入：目录侧 + Dex 配置 + 重启三连

### 2.1 目录侧准备（OpenLDAP）

1. 创建测试用户（如 `test1`）；
2. **创建用户组**：课程实拍强调组类型选 **`groupOfUniqueNames`**（不能选错类型），组名如 `argocd`；
3. 把用户加入组（选 test 用户加进去）。

### 2.2 Dex 连接器配置（argocd-cm）

编辑 `argocd-cm` configmap，加 `dex.config`：

```yaml
data:
  dex.config: |
    connectors:
      - type: ldap
        name: ldap用户登陆          # 页面显示名，自定义
        id: ldap
        config:
          host: gitlab.example.com:389
          insecureNoSSL: true        # 演示环境；生产上 LDAPS
          insecureSkipVerify: true
          bindDN: "$dex.ldap.bindDN"     # 引用 secret 里的值
          bindPW: "$dex.ldap.bindPW"
          usernamePrompt: username
          userSearch:                  # 用户匹配
            baseDN: ou=user,dc=example,dc=com
            filter: ""
            username: cn
            idAttr: uid
            emailAttr: mail
          groupSearch:                 # 组匹配
            baseDN: ou=group,dc=example,dc=com
            filter: "(cn=argocd)"      # 过滤 argocd 组
            userMatchers:
            - userAttr: DN
              groupAttr: uniqueMember
            nameAttr: cn
  url: https://node1.example.com:30295       # Argo CD 访问地址
```

三个匹配块各司其职：**userSearch** 定「哪些人是用户」（baseDN 在 `ou=user`）、**groupSearch** 定「哪些组的人能登录」（filter 过滤 `cn=argocd`）、**userMatchers** 定「用户怎么绑到组」（DN 对 uniqueMember）。

### 2.3 账号密码进 secret（argocd-secret）

敏感信息不写 configmap，用 patch 注入：

```bash
# GNU/Linux（服务器侧，本文默认环境）
kubectl -n argocd patch secrets argocd-secret --patch \
  "{\"data\":{\"dex.ldap.bindPW\":\"$(echo your-password | base64 -w 0)\"}}"
kubectl -n argocd patch secrets argocd-secret --patch \
  "{\"data\":{\"dex.ldap.bindDN\":\"$(echo cn=admin,dc=example,dc=com | base64 -w 0)\"}}"
```

> **平台差异提醒**：`base64 -w 0` 是 GNU coreutils 参数（`-w 0` = 不折行）。在 **macOS/BSD** 上 `base64` 没有 `-w`，直接写 `base64` 即可（BSD 版默认不折行）。若运维同学在本地 Mac 上拼这段 JSON，去掉 `-w 0`：
> ```bash
> # macOS
> kubectl -n argocd patch secrets argocd-secret --patch \
> "{\"data\":{\"dex.ldap.bindPW\":\"$(echo your-password | base64)\"}}"
> ```
> 折行的 base64 值带换行符，Secret 解码后凭据会错——这是「配了却登不上」的常见暗坑。

`$dex.ldap.bindDN`/`$dex.ldap.bindPW` 的占位符由 Dex 从 secret 解析——**配置与凭据分离**，configmap 可以进 git，secret 不进。

### 2.4 重启：不改重启不生效

课程实拍连续踩了两个坑，都指向同一个动作：

1. 配完登录页出现「LDAP 用户登录」，输入密码报**「无效的内容类型」**——配置没生效，重新访问；
2. 页面能登录但 **UI 显示异常**——必须重启才正常。要重启的 Pod 是 **`argocd-dex-server`**（Dex 本体）和 **`argocd-server`**（核心服务）：删掉它们让 Deployment 重建。

> **铁律**：`argocd-cm`/`argocd-secret` 改完，**dex-server 与 argocd-server 必须重启**，否则新旧配置混用。

## 三、RBAC：两行式授权语法

登录成功只是起点——课程实拍：「现在已经登录成功了。但是为什么我们看不到任何的一个应用，是因为我们目前默认的权限是没有任何权限的。」**LDAP 认证 ≠ 授权**，授权走 RBAC。

### 3.1 语法：p 行 + g 行

编辑 `argocd-rbac-cm` configmap：

```csv
# p 行：定义角色（role: <角色名> + 资源 + 动作 + 对象）
p, role:org-admin, applications, sync, *, allow
p, role:org-admin, applications, update, *, allow
p, role:org-read, applications, get, *, allow
p, role:org-exec, exec, *, *, allow

# g 行：把 LDAP 组绑到角色
g, testglue, role:readonly          # 预定义角色：全部只读
g, testblue, role:org-2             # 自定义角色：sync+update+log+exec
```

- **`p` 行 = 策略条目（policy）**：`role:<名字>` + 资源类型 + 动作 + 对象 + `allow/deny`；
- **`g` 行 = 主条目（group binding）**：`<LDAP组名>,role:<角色名>`——组内用户继承角色权限。

### 3.2 资源、动作与对象

| 维度 | 可选值（课程列举） |
| --- | --- |
| **资源** | `applications`、`clusters`、`projects`、`applicationsets`、`exec`（容器终端） |
| **动作** | `get`、`create`、`delete`、`sync`、`update`、`override`… |
| **对象** | `*`（所有应用）或 `项目名/应用名`（限定范围） |

**预置角色**：`role:readonly`（所有资源只读）、`role:admin`（全部权限）——课程示例 testglue 组直接绑 readonly。

### 3.3 课程示例解读

四条 p 行 + 两个 g 行的组合：

- `org-2` 角色 = applications 的 **sync + update** + 查看日志 + **exec**（进容器终端）；
- `testblue` 组绑 `org-2`——组内用户可同步、可更新、可看日志、可进终端；
- 实拍验证：**删除按钮点了报权限不足**（没配 delete）、**sync/update/查看 log/容器终端全部正常**——权限精确到动作级的体感。

**最小权限实践**：按「查看 → 同步 → 更新 → 删除」递进授权；exec 这种高危动作单独给；deny 显式兜底。

## 四、CLI：登录即一切

所有 `argocd app` 命令的前置是**登录**：

```bash
# ⚠️ --insecure 跳过 TLS 校验，仅限内网自签证书的演示环境；生产应为 Argo CD 配置受信证书后去掉该参数
argocd login node1.example.com:32471 --insecure --username admin
```

之后覆盖日常全部操作（课件 `app-cli.txt` 清单）：

| 命令 | 作用 |
| --- | --- |
| `argocd app list` | 列出所有应用 |
| `argocd app get <app>` | 查看应用详细信息 |
| `argocd app delete <app>` | 删除应用 |
| `argocd app sync <app>` | 执行同步 |
| `argocd app set <app> --sync-policy automated` | 启用自动同步 |
| `argocd app set <app> --auto-prune` | 启动自动修剪 |
| `argocd app set <app> --self-heal` | 自动自我修复 |

课程实拍：未登录直接 `argocd app list` 报无权限——「必须要先登录，我们才可以在这边执行操作」。CLI 的价值在脚本化：#86 的部署状态监控脚本就是「login + app get -o json + jq」的组合。

## 五、生产实践要点

1. **认证授权分离**：LDAP 只回答「你是谁」，RBAC 回答「你能干嘛」——接入 LDAP 后第一件事配 RBAC，否则全员零权限或滥用 admin。
2. **组类型别选错**：OpenLDAP 建组用 `groupOfUniqueNames`，与 Dex 的 `uniqueMember` 匹配对应；选错类型用户加进组也不生效。
3. **改配置必重启**：argocd-cm/secret 变更后重启 dex-server + argocd-server——「配了没生效」九成是这个。
4. **bindDN/PW 进 secret**：configmap 里只放 `$dex.ldap.*` 占位符，凭据走 `argocd-secret` patch——配置可入 git、凭据不入。
5. **exec 授权从严**：容器终端 = 页面直达容器 shell，只给必要运维角色；普通开发给 get/sync 就够。
6. **预置角色起步**：readonly/admin 两个预置角色覆盖大部分场景；自定义角色按「资源 × 动作」矩阵精雕。
7. **CLI 登录态用于脚本**：监控/巡检脚本统一 `argocd login` + `app get -o json | jq` 模式（#86 实战）。
8. **生产上 LDAPS**：演示关 SSL 图省事，生产 389 明文传密码不可接受——636 端口 + 证书，`insecureNoSSL` 改 false。

## 六、报错排查表

| 现象 | 根因 | 解法 |
| --- | --- | --- |
| 登录报「无效的内容类型」 | 配置没重启生效 | 删 argocd-dex-server + argocd-server Pod 重启 |
| 能登录但 UI 显示异常 | 同上，服务未 reload | 重启两个 Pod |
| 登录成功但看不到应用 | RBAC 没配（默认零权限） | argocd-rbac-cm 配 g 行绑角色 |
| LDAP 用户加进组仍无权 | 组类型选错 / 过滤器不匹配 | 组用 groupOfUniqueNames；核对 `(cn=argocd)` 与 nameAttr |
| bindDN/PW 报错 | secret 没 patch / base64 错 | 用 patch 命令注入，核对 base64 编码 |
| 删除/更新按钮报权限不足 | RBAC 没配对应动作 | p 行加 delete/update + allow |
| 终端入口点了进不去 | 没配 exec 策略 | p 行加 `exec,*,*,allow` 并绑组 |
| CLI 命令报无权限 | 没登录 | `argocd login <ip:port> --insecure` |

## 七、面试考点与追问

**Q1：Argo CD 接入 LDAP 的组件与配置位置？**
通过 Dex（`argocd-cm` 里的 `dex.config` 连接器）接入；账号密码拆到 `argocd-secret`（`$dex.ldap.bindDN/bindPW` 占位符）；改完必须重启 dex-server 与 argocd-server。

**Q2：LDAP 接入后登录成功但看不到应用，为什么？**
认证（能登录）与授权（能看什么）分离——RBAC 默认零权限。要在 `argocd-rbac-cm` 里用 `g` 行把 LDAP 组绑到带权限的角色。

**Q3：RBAC 的 p 行与 g 行分别是什么？**
p 行定义角色权限：`p,role:xxx,<资源>,<动作>,<对象>,allow`；g 行做组绑定：`g,<LDAP组>,role:xxx`。组内用户继承角色权限。

**Q4：RBAC 支持哪些资源与动作？对象怎么限定范围？**
资源：applications/clusters/projects/applicationsets/exec 等；动作：get/create/delete/sync/update 等；对象 `*` 表示全部，或 `项目名/应用名` 限定到具体应用。

**Q5：容器终端功能受什么控制？**
两层：`argocd-cm` 的 `exec.enabled` 开功能；RBAC 的 `exec` 资源授权放人。缺一不可。

**Q6：argocd CLI 的常用命令？前置条件是什么？**
前置 `argocd login <ip:port> --insecure --username admin`；之后 `app list/get/delete/sync`、`app set --sync-policy automated/--auto-prune/--self-heal`。未登录直接操作报无权限。

**Q7：管理员密码怎么改？**
`argocd account update-password --current-password <旧> --new-password <新>`。

## 📎 文本↔代码关联

| 代码文件 | 正文提及 | 内容 |
| --- | --- | --- |
| `code/10-Argocd/ldap-config/ldap-config.txt` | 2.2 Dex 连接器配置、2.3 密码注入 | LDAP 接入完整样例：`argocd-cm` 的 `dex.config`（ldap 连接器 + userSearch `ou=user` + groupSearch `(cn=argocd)` + userMatchers）+ url + `argocd-secret` patch 命令（bindPW/bindDN base64 注入），对应正文三段配置 |
| `code/10-Argocd/app-cli/app-cli.txt` | 第四节 CLI | argocd CLI 命令清单：`app list/get/delete/sync`、`--sync-policy automated`、`--auto-prune`、`--self-heal`，对应正文命令表 |
| `code/10-Argocd/webhook-secret/argocd-secret.txt` | 2.3 凭据管理 | `argocd-secret` 的编辑样例（stringData 形态），印证「敏感信息进 secret 不进 configmap」的模式 |

**技术点总结**：Argo CD 的账号体系 = **Dex 管认证 + RBAC 管授权 + CLI 管脚本**三件套。LDAP 接入三部曲：目录建组（groupOfUniqueNames）→ `argocd-cm` 配 dex.config（userSearch/groupSearch/userMatchers 三匹配）→ 重启 dex-server 与 argocd-server；凭据走 `argocd-secret` patch，配置凭据分离。RBAC 两行式：p 行定「角色能对什么资源做什么动作」（application/cluster/project/exec × get/delete/sync/update，对象 `*` 或 `项目/应用`），g 行把 LDAP 组绑上去——认证成功零权限是常态，授权必须显式配。exec 授权是容器终端的钥匙，CLI 登录是脚本化的门票——三件事齐了，Argo CD 才从 demo 变成团队基础设施。

