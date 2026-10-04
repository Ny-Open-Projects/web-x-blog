---
disableNunjucks: true
title: "Kubernetes 集群部署: 镜像仓库配置与动态获取镜像 Tag"
date: 2026-10-04 06:00:00
categories: [Kubernetes, CI/CD]
tags: [镜像仓库, 阿里云, Harbor, CLI, jq, 级联变量]
---

发布到 UAT 或生产时以"唯一镜像 tag"为准，但人工记忆或手填 tag 易错且无法核对。结论是：把镜像仓库（阿里云 ACR 或自建 Harbor）配置好访问凭证，并在流水线中调用其接口/CLI 动态拉取 tag 列表，配合上一节的级联变量回填到下拉框，做到"选环境即列对应镜像"。

## 纲要

- 阿里云 ACR 与自建 Harbor 的命名空间/仓库概念对齐
- 在 Jenkins 所在节点安装并配置阿里云 CLI（AK/SK）
- 用 `aliyun cr get-repo-tags` 获取 tag，并用 `jq` 解析
- Harbor 直接用 REST API 取 tag（无需额外客户端）
- 命名空间/仓库/镜像的层级对照
- 阿里云与 Harbor 取 tag 的差异点

## 一、仓库概念对齐

两类仓库的层级概念一致，只是名词不同：

| 阿里云 ACR | 自建 Harbor | 含义 |
| --- | --- | --- |
| 命名空间 (namespace) | 项目 (project) | 镜像分组 |
| 镜像仓库 (repo) | 仓库 (repository) | 同一应用的不同 tag |
| tag | tag | 同一镜像的不同版本 |

演示用阿里云命名空间 `citools` 存放 docker、kubectl 等课程工具镜像；自建 Harbor 中项目 `yt` 下存放 `springcloud-demo` 等应用镜像，目录层级几乎一致。

## 二、配置阿里云访问（AK/SK）

在 linux 上安装阿里云 CLI 并配置 AK/SK 与地域：

```bash
# 下载并安装阿里云 CLI（放到 /usr/local/bin）
wget -O aliyun-cli.tgz https://aliyuncli.alicdn.com/aliyun-cli-linux.tgz
tar -xzf aliyun-cli.tgz -C /usr/local/bin

# 配置 AK/SK/Region（交互式）
aliyun configure
# Access Key Id:     $ALI_AK
# Access Key Secret: $ALI_SK
# Region:            cn-beijing
```

登录验证：

```bash
docker login --username=$ALI_AK registry.cn-beijing.aliyuncs.com
# 输入在 ACR 控制台设置的密码
```

## 三、动态获取 tag

阿里云使用其 CLI 取 tag，Harbor 直接请求 API：

```bash
# 阿里云：获取某仓库的全部 tag
aliyun cr get-repo-tags --namespace citools --repo-name docker \
  | jq -r '.data[].tag'

# Harbor：直接调用 REST API 取 tag 列表
curl -s -u '$REG_USER:$REG_PASS' \
  "https://$REGISTRY_ADDR/api/v2.0/projects/$NS/repositories/$IMG/artifacts?page_size=20" \
  | jq -r '.[].tags[].name'
```

`jq` 解析要点：`.data[].tag` 取阿里云返回集合下的 tag；Harbor 返回数组中每个元素 `.tags[].name` 才是 tag 名。去掉引号用 `-r`。

## 四、命名空间/仓库层级

```text
registry.cn-beijing.aliyuncs.com/
└── citools/                # 命名空间
    ├── docker/             # 镜像仓库
    │   ├── tag: 24
    │   └── tag: 25
    └── kubectl/            # 镜像仓库
        └── tag: latest

$REGISTRY_ADDR/              # Harbor
└── yt/                     # 项目
    └── springcloud-demo/   # 仓库
        ├── tag: v1.0.1
        └── tag: v1.0.2
```

## 取 tag 流程

```mermaid
flowchart LR
    A[选择环境 test1] --> B[调用仓库接口]
    B --> C{仓库类型}
    C -->|阿里云| D[aliyun cr get-repo-tags]
    C -->|Harbor| E[REST API /artifacts]
    D --> F[jq 解析 .data[].tag]
    E --> G[jq 解析 .tags[].name]
    F --> H[回填下拉框]
    G --> H
```

## API 速览

| 能力 | 做法 |
| --- | --- |
| 阿里云登录 | `docker login registry.cn-beijing.aliyuncs.com` |
| 配置 CLI | `aliyun configure` 填 AK/SK/Region |
| 阿里云取 tag | `aliyun cr get-repo-tags --namespace X --repo-name Y` |
| Harbor 取 tag | `curl .../api/v2.0/.../artifacts` + `jq` |
| 解析阿里云结果 | `jq -r '.data[].tag'` |
| 解析 Harbor 结果 | `jq -r '.[].tags[].name'` |
| 去引号 | `jq -r`（raw 输出） |
| 概念映射 | 命名空间↔项目，镜像仓库↔repository |

## Demo 示例

```bash
# 阿里云：列出 citools/docker 的 tag
aliyun cr get-repo-tags --namespace citools --repo-name docker | jq -r '.data[].tag'

# Harbor：列出 yt/springcloud-demo 的 tag
curl -s -u '$REG_USER:$REG_PASS' \
  "https://$REGISTRY_ADDR/api/v2.0/projects/yt/repositories/springcloud-demo/artifacts" \
  | jq -r '.[].tags[].name'

# 选中的 tag 拼成完整镜像地址推送/拉取
echo "registry.cn-beijing.aliyuncs.com/citools/docker:$TAG"
```

### 总结

- 阿里云 ACR 与 Harbor 概念一致：命名空间≈项目，镜像仓库≈repository，下面才是 tag。
- 阿里云需安装其 CLI 并 `aliyun configure` 配置 AK/SK；Harbor 直接 REST API 即可，无需额外客户端。
- 取 tag 后务必用 `jq` 正确解析（阿里云 `.data[].tag`，Harbor `.tags[].name`），`-r` 去引号。
- 动态获取 tag 配合级联变量，可让发布者在下拉框中直接选"该环境已有镜像"，避免手填出错。
- 课程用阿里云演示，但原理与自建 Harbor 完全相同，仅"取 tag 的入口"不同（CLI vs API）。

