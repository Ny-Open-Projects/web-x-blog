# mksz892 运维落地附录（国内环境专用）

本附录是 90 篇博客的**运维补充件**，解决「照着做却跑不起来」的三类环境问题：境外资源不可达、示例地址照抄无效、命令跨平台差异。**建议通读一遍再动手实操**。

---

## 一、境外镜像/资源 → 国内替代总表

课程演示环境能直连外网，国内照抄大概率卡在拉取阶段。按资源类型给出替代方案：

| 官方源 | 用途 | 国内症状 | 替代方案 |
| --- | --- | --- | --- |
| `gcr.io` / `k8s.gcr.io` | kaniko 执行器、K8s 官方镜像 | 连接超时 | ① 配镜像加速器；② 用国内镜像站同步版本；③ 离线 `docker save/load` 导入构建节点 |
| `quay.io` | Drone 插件（如 `drone-kubernetes`） | 时快时慢，CI 偶发 pull 失败 | 一次性同步到内网 Harbor，改 `image:` 为内网地址 |
| `ghcr.io` | 新版 Tekton / Argo 组件 | 拉取慢 | 同上；或 `docker pull` 后 tag 推内网 |
| `registry.k8s.io` | K8s 组件镜像 | 不可达 | 国内云厂商镜像仓库有同步（如 `registry.aliyuncs.com/google_containers`） |
| `raw.githubusercontent.com` | Argo CD install.yaml 等 | 常被阻断 | ① `gh-proxy.com` / `raw.gitmirror.com` 前缀；② 跳板机下载后本地 apply |
| `storage.googleapis.com` | Tekton release YAML | 不可达 | 同上，下载到本地再 `kubectl apply -f` |
| `github.com/.../releases/download` | tkn / istioctl 等二进制 | 极慢或中断 | `gh-proxy.com` 前缀，或走发行版包管理器 |
| `helm.elastic.co`、`prometheus-community.github.io` | Helm chart 仓库 | repo add 超时 | ① 换国内 chart 镜像源；② **推荐**：把 chart 渲染成 YAML 直接进 git（少一层外部依赖，也更 GitOps） |

### 镜像加速器配置（一次配置，全局生效）

```bash
# Docker / containerd 通用思路：配 registry-mirrors（各云厂商在控制台给专属地址）
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<'EOF'
{
  "registry-mirrors": ["https://<你的专属加速地址>"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker

# 验证：看 Registry Mirrors 是否生效
docker info | grep -A2 "Registry Mirrors"
```

containerd（K8s 1.24+ 常见）改 `/etc/containerd/config.toml` 的 `[plugins."io.containerd.grpc.v1.cri".registry.mirrors]` 段，改完 `systemctl restart containerd`。

### 离线环境标准打法（内网/无出口集群）

```bash
# ① 出网机拉取并打包
docker pull <image>:<tag>
docker save <image>:<tag> -o pkg.tar

# ② 内网各节点导入（containerd 用 ctr/nerdctl）
docker load -i pkg.tar                                   # docker
nerdctl load -i pkg.tar                                  # containerd + nerdctl
ctr -n=k8s.io images import pkg.tar                      # 纯 containerd

# ③ 批量替换 YAML 里的镜像地址为内网仓库
sed -i 's#gcr.io/kaniko-project#registry.internal.example.com/kaniko#g' *.yaml
```

---

## 二、示例地址替换清单（别照抄课程 IP）

课程实拍环境用的是 `10.0.7.x` 内网段，共 **70 处**分布在 19 篇里。它们是**演示环境地址，不是通用值**，实操前逐项替换：

| 示例值 | 出现在 | 替换为 |
| --- | --- | --- |
| `10.0.7.101:31650` / `:32471` / `:30295` | Argo CD 登录地址（#76/#80/#81） | 你的 `kubectl get svc -n argocd argocd-server` 出来的 NodePort |
| `10.0.7.63` | git 仓库地址（#77 等） | 你的 GitLab/Gitea 地址 |
| `10.0.7.100:6443` | K8s apiserver（#52） | `kubectl config view --minify` 里的 server 地址 |
| `10.0.7.30` | Jenkins/Slave 节点（#21/#52） | 你的构建节点地址 |
| `10.0.7.11` | NFS server（#41/#67） | 你的 NFS/存储服务器地址 |
| `registry.cn-hangzhou.aliyuncs.com/...` | 课件作者的镜像仓库（17 篇） | 你自己的镜像仓库（别人的仓库你推不进去） |
| `git.example.com` / `gitlab.example.com` / `*.example.com` | 域名占位 | 你的实际域名 |

**替换后自检**：`grep -rn "10\.0\.7\." <你要执行的 YAML>`——应为空。

---

## 三、GNU/Linux 与 macOS 命令差异

博客里的命令默认跑在 **Linux 服务器**（构建节点、集群节点）。若你在 **macOS 本地**调试，以下四处会报错：

| 命令 | Linux（GNU） | macOS（BSD） | 报错症状 |
| --- | --- | --- | --- |
| `sed -i "s/a/b/" f` | ✅ 直接可用 | `sed -i '' "s/a/b/" f`（`-i` 后必须给空后缀参数） | `sed: s/a/b/: No such file or directory`（脚本被当成文件名） |
| `base64 -w 0` | ✅ `-w 0` 不折行 | 无 `-w` 参数，直接 `base64` | `invalid option -- w` |
| `date -d "+1 day"` | ✅ | `date -v+1d` | `illegal option -- d` |
| `timeout 60 cmd` | ✅ coreutils 自带 | 需 `brew install coreutils`，用 `gtimeout` | `command not found: timeout` |

**建议**：所有实验在 Linux 虚拟机/服务器里做，避免 BSD/GNU 语义差带来的假故障。本地 Mac 只做 YAML 编写与 git 推送。

---

## 四、双系命令对照（博客主要给 Debian 系，RHEL 系对照）

课程环境为 Ubuntu/CentOS 混合，博客里安装类命令多为 Debian 系。RHEL 系（Rocky/AlmaLinux/CentOS）对照：

| 场景 | Debian 系（Ubuntu/Debian） | RHEL 系（Rocky/AlmaLinux） |
| --- | --- | --- |
| 装包 | `apt-get update && apt-get install -y <pkg>` | `dnf install -y <pkg>`（CentOS 7 用 `yum`） |
| 装 NFS 客户端 | `apt-get install -y nfs-common` | `dnf install -y nfs-utils` |
| 防火墙放端口 | `ufw allow 31650/tcp` | `firewall-cmd --permanent --add-port=31650/tcp && firewall-cmd --reload` |
| 查看防火墙 | `ufw status` | `firewall-cmd --list-all` |
| 服务管理 | `systemctl restart docker`（两系通用） | 同左 |
| SELinux（RHEL 独有坑） | — | 挂载/NFS/容器目录被拒时先看 `getenforce`；排障期可 `setenforce 0` 验证，**生产不要长期关**，应写 `semanage fcontext` 策略 |

> **RHEL 系专属坑**：同样一份 NFS PV 配置，在 Rocky 上可能因 SELinux 报 `permission denied`，而 Ubuntu 正常。排查顺序：`getenforce` → `ausearch -m avc -ts recent` 看拒绝日志 → 加 SELinux 策略或给目录打 `container_file_t` 上下文。

---

## 五、高危操作清单（执行前必须确认）

90 篇里出现过的高危动作，统一给出**确认点 + 回滚方案**：

| 操作 | 风险 | 执行前确认 | 回滚方案 |
| --- | --- | --- | --- |
| Argo CD **页面删除**应用 | 连 K8s 应用一起删 = 停服 | ① 确实要下线；② 已通知业务方；③ git 里有 Application YAML | `kubectl apply -f application.yaml` + sync |
| `kubectl delete -f applicationset.yaml` | **级联删**该生成器渲染的所有应用 | 先 `kubectl get application -l app.kubernetes.io/instance=<appset名>` 看清数量 | 重新 apply applicationset |
| `kubectl delete -f xxx.yaml` | 删错对象 | 先 `--dry-run=client` 看影响面 | 从 git 重新 apply |
| `chmod 777`（共享卷） | 任何用户可写，等保必挂 | 改用 `chown` 对齐容器 UID，或 `chmod 775` + 同组 | `chown -R <uid>:<gid> /path && chmod 775 /path` |
| 开启 `selfHeal` | 会「修复」掉人工回滚 | **回滚前必须关** | 改回 `selfHeal: false` |
| 开启 `prune` | git 里误删 YAML → 集群资源跟着消失 | 开分支保护 + PR review 再开 | git revert 后 sync |
| 容器终端（`exec.enabled`） | 页面直达容器 shell | RBAC 只给必要运维角色 | 关 `exec.enabled` |
| `docker system prune` | 清掉未使用镜像/卷（含构建缓存） | 确认无在用悬空卷 | 无回滚，**先备份再清** |

---

## 六、验收自检命令（改完环境跑一遍）

```bash
# 1. 集群侧：CRD 与控制平面在位
kubectl get crd | grep -E "rollouts.argoproj.io|applications.argoproj.io|tekton.dev"

# 2. 镜像：关键组件都已拉取成功（无 ImagePullBackOff）
kubectl get pods -A | grep -vE "Running|Completed"

# 3. 存储：PVC 已绑定（Tekton/Zadig 的共享卷）
kubectl get pvc -A | grep -v Bound

# 4. 网络：NodePort/Ingress 可访问
kubectl get svc -A | grep -E "NodePort|LoadBalancer"

# 5. 无残留示例地址（你的执行目录里应为空）
grep -rn "10\.0\.7\." ./ || echo "OK: 无示例 IP 残留"
```

---

**维护说明**：本附录随 90 篇博客一同维护。新增环境类问题请追加到对应章节，并同步更新主进度表。

---

## 附二 · 代码执行红线（v2 审计新增，2026-10-15）

### 1. 教学代码占位符铁律：`<xxx>` 是 shell 重定向操作符

`kubectl describe taskrun <name>` 照抄必报 `bash: syntax error near unexpected token 'newline'`——`<` `>` 被 bash 解析为输入重定向。**全库 16 个文件 43 处已统一变量化为 `$VAR`**（如 `$APP_NAME`/`$ROLLOUT`/`$GIT_USER`），既修了语法又把示例升级成生产脚本形态。后续新增内容一律遵守：

```bash
# ❌ 照抄报错
vela adopt <deployment-name> <service-name> --apply --name <app-name>
# ✅ 生产真身
vela adopt $DEPLOY_NAME $SVC_NAME --apply --name $APP_NAME
```

自检命令（应输出 `OK: bash 块无裸尖括号占位符`，2026-10-15 实测通过）：

```bash
cd work/target/mksz892 && /Users/Wang/.workbuddy/binaries/python/envs/default/bin/python3 -c "
import os, re
bad = []
for fn in sorted(os.listdir('.')):
    if not fn.endswith('.md') or fn in ('_PROGRESS.md','_INDEX.md'): continue
    lines = open(fn, encoding='utf-8').read().split('\n')
    in_bash = False
    for i, l in enumerate(lines):
        if l.startswith('\`\`\`bash') or l.startswith('\`\`\`sh'): in_bash = True; continue
        if in_bash and l.startswith('\`\`\`'): in_bash = False; continue
        if in_bash and not l.strip().startswith('#'):
            for ph in re.findall(r'<[A-Za-z一-龥][^<>\`\n]*>', l):
                bad.append(f'{fn}:{i+1}: {ph}')
print('\n'.join(bad) if bad else 'OK: bash 块无裸尖括号占位符')
"
```

> 注意别用 grep 自查——mermaid 箭头 `-->` 会大量误报；必须用状态机只查 bash 块命令行。
> Jenkins DSL / YAML 字段值里的 `<占位符>`（如 `msAccessKey: '<你的AccessKey>'`）在引号内合法，不在清洗范围。

### 2. 代码块入库前四线校验（新内容必跑）

```bash
# bash 语法（最便宜，3 秒抓照抄必错）
# yaml / json / groovy / bash 四线 + 17 类安全模式：跑 /tmp/audit_mksz892_code.py
/Users/Wang/.workbuddy/binaries/python/envs/default/bin/python3 /tmp/audit_mksz892_code.py
```

判据：`bash_fail / yaml_fail / json_fail / groovy_fail` 全为 0；`sec_hits` 逐条过人工（P0 必须带生产提示，P1 确认是占位符或 from_secret 引用）。

### 3. 生产边界提示的加注位置（不删演示命令）

| 命令 | 提示加在哪 |
| --- | --- |
| `argocd login --insecure` | 命令块首行注释：仅限内网自签证书，生产配受信证书 |
| kaniko `runAsUser: 0` | securityContext 内注释：镜像要求 root；PSS restricted 用 BuildKit rootless 或 SA 豁免 |
| `curl ... \| bash/sh` | 前置注释：先下载审阅 + 锁版本 |
| `image: xxx:latest` | 行尾注释：生产锁版本 tag |
| 凭据类参数 | 用 flag 传参 + 提醒 shell history / ps 泄漏 |
