# 审稿 B8-P7：07.第七期（22 篇）专家复核报告

- 审稿对象：`work/target/25-lowcode/posts/07.第七期/`（25-1~25-8、26-1~26-3、27-1~27-8、28-1~28-3，共 22 篇，主题：低代码平台深化 / 云效 CI/CD / Docker 部署 / Jmeter 压测）
- 真源对照（SRC）：`work/source/25.xiaodi-lowcode/小滴课堂低代码大课/course-reference/lowcode-platform-final`（按任务指定名；实际目录为 `course-reference/lowcode-platform-full`，下文统称 SRC）——本批重点核对根目录 `docker-compose.yml`、`server.Dockerfile`、`release.Dockerfile`、`server.nginx.Dockerfile`、`release.nginx.Dockerfile`、`nginx/server.nginx.conf`、`nginx/release.nginx.conf`、根 `package.json`、`packages/server|release|client` 的 `package.json` 与 `.env.example`、`docs/schema.sql`、`packages/release/src/app/[id]/page.tsx`、`src/components/ComponentRender.tsx`、`packages/client/src/pages/release.tsx`、`src/utils/request.ts`
- 基准：`reports/scan3-code.md`、`reports/scan6-applied.md`、`reports/review-eng-b.md`（表述风险清单）、`reports/review-b5-p4.md` / `reports/review-b6-p5.md`（判例：教学期命名 vs SRC、title/h1 与文件名一致、`/local/` 旧路由一律上报）
- 审查维度：技术硬伤（云效流水线 / Docker / Compose / Nginx 部署链路、命令与配置块可执行性）· 代码/配置块与真实仓库一致性 · 六段结构与互链真实 · 去 AI 味
- 结论口径：沿用 b5/b6——【合格】= 无 P0/P1（可附 P2 建议）；【需修】= 存在 P0/P1 或有必须改的 P2（标题断链、命名错认）。只出报告，未改任何文件。

---

## 〇、残留复查（对齐 scan6 / review-eng-b / b5 / b6 已修点）

| 检查项 | 结果 |
|---|---|
| scan6 清单外残留 27-5 `/api/local/release` ×3 | **仍在**（L30/L32/L62），本次正式上报并入 27-5 条目 1 |
| A5 同源（getQuestionComponentValueFeed / defaultCheckbox） | P7 全 22 篇 0 处（grep 证实） |
| b6 簇七 `textarea` → `textArea` | 27-5（L35）、27-8（L33/L47）为新残留，并入簇六 |
| b6 簇六 ip+ua 防重口径注 | 27-5（L54/L64）把「IP + 设备去重」写成既成事实、未加限定，并入簇五 |
| review-eng-b P0-7（release_with_user 恒空）现状注 | 27-7 L22「从后端接口读取之前发布过的缓存数据」未加注，并入簇七 |
| transcript / 拓展运算符 | 0 处 |
| 整句加粗 | 仅 28-3 L33 一处（27-3 L24 加粗的是引用的报错文案，属引语，可保留） |
| 六段结构（title/H1 + 导语 + 前置知识 + 正文 + 小结 + 下一步） | 22 篇全部齐整，无缺段 |

---

## 一、共性簇（跨篇问题，逐篇条目只留指针）

### 簇一（P1）：Dockerfile / Nginx 配置路径与 SRC 不一致——照文配置流水线会「文件不存在」构建失败

SRC 四个 Dockerfile 全部在**仓库根目录**：`server.Dockerfile`、`release.Dockerfile`、`server.nginx.Dockerfile`、`release.nginx.Dockerfile`；两份 Nginx 配置在根目录 **`nginx/`** 下：`nginx/server.nginx.conf`、`nginx/release.nginx.conf`（23-3/23-4 也是按「根目录 + nginx/ 目录」教的）。本批多处以不存在的路径/大小写指认：

| 篇·行 | 博客写法 | SRC 实名 |
|---|---|---|
| 25-5 L38、L67 | `server/nginx.dockerfile` | `server.nginx.Dockerfile`（根目录，无 `server/` 子目录） |
| 25-6 L30、L58 | `server.dockerfile` | `server.Dockerfile`（Linux 大小写敏感） |
| 25-7 L32、L51、L58 | `release/nginx.dockerfile` | `release.nginx.Dockerfile`（根目录） |
| 25-7 L52 | `release.dockerfile` | `release.Dockerfile` |
| 25-8 L28、L65 | `release.dockerfile` | `release.Dockerfile` |
| 27-2 L44 | `server/nginx.dockerfile` 与 `release/nginx.dockerfile` | `server.nginx.Dockerfile` / `release.nginx.Dockerfile` |
| 27-3 L24/L28/L30/L34/L39/L49/L50（贯穿） | `release.dockerfile`（Releases.dockerfile 故事的修复目标） | `release.Dockerfile` |
| 27-1 L38、L39、L67 | `server/nginx.config`、`release/nginx.config` | `nginx/server.nginx.conf`、`nginx/release.nginx.conf`（路径、扩展名双错） |

修法：首次出现处改为 SRC 实名；确要保留教学期别名时按 b5 簇二判例**首次出现括注**「（最终仓库为 `xxx.Dockerfile`，位于仓库根目录）」。27-1 的 `nginx.config` 扩展名必须改（`.conf`），否则与 SRC 及 23-4 的教学直接冲突。

### 簇二：title/H1 与文件名不一致（25-3 为 P1，其余 P2）

系列判例（b5 簇一 / 任务规则）：title/H1 必须与文件名（= 全批引用名）一致，改偏离方，引用方不动。P7 内部互链全部按文件名风格书写，以下各篇偏离：

| 篇 | 实际 title/H1 | 文件名/引用名 | 建议 | 严重度 |
|---|---|---|---|---|
| **25-3** | **React 部署配置：把打包产物 dist 上传到阿里云 OSS** | 《React项目部署配置—线上代码上传OSS配置》（25-2 L70、25-4 L16、27-6 L16 共 3 处引用） | title/h1 改为引用名 | **P1** |
| 25-1 | DevOps 自动化部署实现**：**流水线关联代码源 | 《DevOps自动化部署实现**—**流水线关联代码源》（25-2 L15、26-1 L16） | 冒号改破折号、去 DevOps 后空格 | P2 |
| 25-2 | React **␣**项目部署配置—打包构建 | 《React项目部署配置—打包构建》（25-1 L62、25-3 L15、25-4 L15） | 去 React 后空格 | P2 |
| 26-1 | …Docker-compose **␣**文件上传服务器配置 | 文件名 `Docker-compose_文件上传服务器配置`（引用 4 处：25-8 L72、26-2 L16、26-3 L16、27-4 L16） | 见簇二 A | P2 |
| 27-1 | 第1集 **␣**项目自动化部署上线—更改线上 **␣**ip+端口 | 文件名 `第1集_项目自动化部署上线—更改线上_ip+端口`（引用 3 处：26-3 L71、27-2 L15、27-5 L16） | 见簇二 A | P2 |
| 27-2 | …镜像名称 **␣**BUG **␣**修复 | 文件名 `镜像名称_BUG_修复`（引用 1 处：27-1 L74） | 见簇二 A | P2 |
| 27-3 | …Dockerfile名称 **␣**BUG **␣**修复 | 文件名 `Dockerfile名称_BUG_修复`（引用 2 处：27-2 L58、27-4 L15） | 见簇二 A | P2 |
| 27-4 | …Docker-compose上传 **␣**BUG **␣**修复 | 文件名 `Docker-compose上传_BUG_修复`（引用 2 处：27-3 L56、27-5 L15） | 见簇二 A | P2 |

**簇二 A（下划线→空格）**：05 期 20-5（`前端_Nextjs_项目初始化`）、17-1（`阿里云_OSS_资源上传配置`）的判例是 title **逐字保留文件名下划线**。P7 这 5 篇把 `_` 渲染成空格，title 自洽但违背「与文件名一致」规则。建议统一：5 个 title/h1 恢复下划线，并同步批内 12 处引用名（上文括注的引用行）；若系列级决定改用空格形，则应重命名文件并在后续审稿统一——二选一，不可两头不靠。

### 簇三（P2）：P7 引用 06/08 期篇目按名检索不命中（偏离方在对方 title，P7 侧无需改）

P7 引用名全部等于对方**文件名**（写法正确），但对方 title 偏离了自家文件名，站内按 title 检索会断：

| P7 引用（出处） | 对方 title 实际值 |
|---|---|
| 《项目部署上线—运行容器Docker-compose的介绍和使用》（25-4 L17） | 24-1 title「Docker Compose 入门：一条命令编排多个容器」 |
| 《项目部署上线—Docker-compose运行多容器的配置》（26-2 L16、27-1 L16） | 24-2 title「项目部署上线：Docker Compose 运行多容器的配置」 |
| 《项目部署上线—构建前端发布Nextjs镜像的Dockerfile配置》（25-8 L16） | 23-5 title「项目部署上线：构建前端发布 Next.js 镜像的 Dockerfile 配置」 |
| 《项目部署上线—构建前端nginx镜像的Dockerfile配置》（25-7 L16） | 23-6 title「项目部署上线—构建前端 Nginx 镜像的 Dockerfile 配置」 |
| 《多环境快速安装Jmeter5》（28-3 L16、L57） | 28-4 title「多环境快速安装 JMeter 5.x」 |

不在本批修改范围；应记入 06/08 期审稿清单（改对方 title 为文件名形，或跨期统一时处理）。

### 簇四（P2）：批内事实口径小冲突

1. **Bucket 名**：25-3 L23 立了「演示 Bucket 名为 `lowcode-client`」，25-8 L45 却写「（如 `local-client`）」。统一为一个（建议 `lowcode-client`），或在 25-8 改为「Bucket（25-3 的 `lowcode-client`）」。
2. **compose 制品名**：25-4 L38「起名叫 `docker-compose`」vs 26-1 L30「如 `doc-compose-<环境变量>`」。建议 26-1 括注「（25-4 示例名为 `docker-compose`，带环境变量后缀亦可）」或统一。
3. **阶段/任务编号**：25-4 L34 与 27-2 L24 把「compose 文件上传」归入**构建阶段**（与 26-1 L28「构建阶段'Docker-compose.yml文件上传'步骤」一致）；但 27-4 L22/L50 又把它称作「第二阶段」、26-2 L11 称「部署阶段的第三个任务」、L20 标题「第三个阶段」。建议以「构建阶段（打包 / OSS / compose 上传三步骤）→ 部署阶段（主机部署 + Docker 部署两任务）」统一口径：26-2 导语改「部署阶段的 Docker 部署任务」、L20 标题改「### 部署阶段：Docker 部署任务」；27-4 L22/L50 的「第一/第二/第三阶段」改为「构建阶段 / 部署阶段的主机部署任务 / 部署阶段的 Docker 部署任务」。

### 簇五（P2）：ip+ua 防重口径未加限定（沿用 b6 簇六 / review-eng-b 风险 #6/#19）

27-5（L54、L64）把「按 IP + 设备去重、换浏览器可再提交」写成既成事实。SRC 实现 `MD5(ip + ua)`（GetUserMessTool），`main.ts` 未设 trust proxy：经 nginx 反代后 request.ip 恒为网关 IP。建议在 L54 后加一句：「该判定在单机直连下有效；经 Nginx 反代需配 trust proxy 与 X-Forwarded-For，否则同 UA 用户互挤、换 UA 可绕过」。

### 簇六（P2）：`textarea` → `textArea`（沿用 b6 簇七）

SRC 组件 type 名为 `textArea`（camelCase）。残留：27-5 L35、27-8 L33、L47。

### 簇七（P2）：`release_with_user` 现状注（沿用 b6 簇八 / review-eng-b P0-7）

27-7 L22「系统会从后端接口读取之前发布过的缓存数据」——最终仓库 `low-code.controller.ts` 实现为 `getReleaseData(null, user)` 恒空，编辑器实际依赖 localStorage 草稿恢复。参照 b6 对 19-5 的处理加一句现状注即可。

### 簇八（P2）：「大厂几乎都基于 JMeter 二次封装」表述夸大

课程口播原话，但写成事实过强。28-1 L40「阿里、字节、腾讯，国外 Google、Facebook、Amazon、Apple 等，其测试平台底层**几乎都**基于 JMeter 做二次封装」→ 建议改「国内外不少公司的自研压测平台会基于 JMeter 二次封装」；28-2 L47「大厂普遍二次封装」、28-3 L26「互联网公司普遍使用并二次封装」同步降格为「不少公司」。

---

## 二、逐篇明细

### 25-1.DevOps自动化部署实现—流水线关联代码源 — 需修

1. 【P2】标题断链（簇二）：title/h1（L2、L9）「DevOps 自动化部署实现：流水线关联代码源」→ 改「DevOps自动化部署实现—流水线关联代码源」。引用方（25-2、26-1）已按文件名书写，改 title 一处即修复。
2. 【P2】L62 下一步引用《DevOps自动化部署实现—Docker-compose 文件上传服务器配置》为空格形，26-1 title 修复（簇二 A）后需同步为下划线形。

（两条路径对比表、Codeup 流程、分支 master、仅保存等操作描述与云效实际一致；无仓库级硬伤。）

### 25-2.React项目部署配置—打包构建 — 需修

1. 【P2】标题（L2、L9）「React 项目部署配置—打包构建」→ 去「React」后空格（簇二）。
2. 【P2】L37 `npm config set registry <国内镜像源地址>` → 建议括注 SRC Dockerfile 实际值 `https://registry.npmmirror.com`，读者可直接复制。

（构建顺序 registry → pnpm -g → install → build:share → build:client 与 SRC 根 package.json 脚本及 25-6 Dockerfile 叙事一致；`pnpm run build:share`/`build:client` 均为合法脚本名；「先 share 后其余子包」的依赖解释正确；dist 产物路径与 25-3 衔接正确。）

### 25-3.React项目部署配置—线上代码上传OSS配置 — 需修

1. 【P1】标题断链（簇二第 1 行）：title/h1（L2、L9）整体改写为「React 部署配置：把打包产物 dist 上传到阿里云 OSS」，与文件名及 3 处引用名《React项目部署配置—线上代码上传OSS配置》完全不一致（b5 对 14-9/15-6/16-4 同型判 P1）。改 title/h1，一处修复全部引用。

（Bucket 三项配置、源文件目录 `packages/client/dist`、「dist 不进 git、必须接在构建后」的说明均正确；与 24-4 的口径衔接一致。）

### 25-4.React项目部署配置—Docker-compose文件上传至公共存储空间 — 合格

（四个服务划分、归档制品流程、OSS 存静态资源 vs ACR 存镜像的区分、打包路径填根目录文件名，均与 SRC `docker-compose.yml`（四服务、`image: ${*_tag}` 变量）一致。制品名口径微差见簇四 2，可不改。）

### 25-5.Nestjs项目部署配置—后端Nginx镜像构建上传 — 需修

1. 【P1】L38 原句「**Dockerfile 路径**：填 `server/nginx.dockerfile`，这是生成后端 Nginx 镜像的构建文件」→ SRC 为仓库根目录 `server.nginx.Dockerfile`，不存在 `server/` 子目录；照文配置云效「Dockerfile 路径」会直接构建失败（可执行性硬伤）。小结 L67「后端 Nginx 镜像对应的 Dockerfile 是 `server/nginx.dockerfile`」同改。
2. 【P2】L26/L36/L60/L65 命名空间 `local-images` 为讲师环境值，建议首次出现处括注「（按自己创建的命名空间为准）」。
3. 【P2】L42-49 compose 片段本身与 SRC 一致（`backend_nginx` / `${backend_nginx_tag}` / `5000:80`），无需改——仅提示：该片段若按簇一改名，正文与片段的「对应关系」仍然成立。

### 25-6.Nestjs项目部署配置—后端项目镜像构建上传 — 需修

1. 【P2】L30 原句「**Dockerfile 路径**：填 `server.dockerfile`」→ SRC 实名 `server.Dockerfile`（大写 D）。云效执行机为 Linux、大小写敏感，照文填小写会「文件不存在」；小结 L58 同改。（簇一）
2. 【P2】L32-39 compose 片段（`backend` / `${backend_tag}` / `5001:3000`）与 SRC 逐字一致；L29「对应 docker-compose.yml 里的 `backend_tag`」正确。

### 25-7.Nextjs项目部署配置—服务端渲染Nginx镜像构建上传 — 需修

1. 【P1】L32 原句「**Dockerfile 路径**：填 `release/nginx.dockerfile`」→ SRC 为根目录 `release.nginx.Dockerfile`；L51、L58 同改（簇一）。
2. 【P2】L52「前端发布的项目镜像（`release.dockerfile`）」→ `release.Dockerfile`（簇一，大小写）。
3. 【P2】L34-41 compose 片段（`frontend_nginx` / `${frontend_nginx_tag}` / `4000:80`）与 SRC 一致；L31 变量对应关系正确。

### 25-8.Nextjs项目部署配置—服务端渲染项目镜像构建上传 — 需修

1. 【P2】L28/L65「`release.dockerfile`」→ `release.Dockerfile`（簇一，大小写）。
2. 【P2】L45 原句「上传阿里云 OSS Bucket（如 `local-client`）」→ 与 25-3 已立的 `lowcode-client` 冲突（簇四 1），统一为 `lowcode-client`。
3. 【P2】L30-37 compose 片段（`frontend` / `${frontend_tag}` / `4001:3000`）与 L49-56 四服务端口总览均与 SRC 一致。

### 26-1.DevOps自动化部署实现—Docker-compose_文件上传服务器配置 — 需修

1. 【P2】标题（L2、L9）空格形 → 与文件名下划线形对齐（簇二 A），并同步 4 处引用名（25-8 L72、26-2 L16、26-3 L16、27-4 L16）。
2. 【P2】L30 制品名「如 `doc-compose-<环境变量>`」与 25-4 L38 的 `docker-compose` 口径不一（簇四 2），统一或括注。

（主机部署 / 下载制品 / `/root/yx/backend.tgz` 下载路径 / `tar zxvf … -C /root/yx` 解压命令本身可执行；L48「上一级目录 /root/yx」指 `backend.tgz` 的父目录，语义成立。）

### 26-2.DevOps自动化部署实现—多个镜像运行在服务器配置《上》 — 需修

1. 【P2】阶段/任务口径自相矛盾（簇四 3）：L11 导语「部署阶段的**第三个任务**」vs L20 标题「### 第三个**阶段**：Docker 部署任务」，且与 25-4/27-2 把 compose 上传归入构建阶段的说法冲突。改法见簇四 3。
2. 【P2】L28-36 清理脚本技术点核对：`docker ps -a | grep local | awk '{print $1}'` 取容器 ID（第一列）✓；`docker images | grep local | awk '{print $3}'` 取 IMAGE ID（第三列）✓；`|| true` 防首次部署空集报错中断 ✓——与 27-4 L53 的日志叙事互洽，无需改。

### 26-3.DevOps自动化部署实现—多个镜像运行在服务器配置《下》 — 合格

（四变量表 `backend_tag`/`backend_nginx_tag`/`frontend_tag`/`frontend_nginx_tag` 与 SRC `docker-compose.yml` 的 `image:` 变量逐一对应；「变量值=上游制品标签」的机制描述正确；手动/定时/Webhook 触发的取舍合理。互链 3 处全部真实。）

### 27-1.第1集_项目自动化部署上线—更改线上_ip+端口 — 需修

1. 【P1】L38 原句「`server/nginx.config`：代理后端服务，端口填 **5001**」→ SRC 配置文件为 `nginx/server.nginx.conf`（路径、扩展名双错；端口 5001 与 SRC `upstream server host.docker.internal:5001` 一致）。
2. 【P1】L39 原句「`release/nginx.config`：前端发布 Nginx 代理，端口填 **4001**」→ SRC 为 `nginx/release.nginx.conf`（端口 4001 正确）。小结 L67 两个错误路径同步改（簇一）。
3. 【P2】L36「两处 Nginx 配置文件里的 `server` 地址（IP + 端口）要改成线上值」→ 补现状注：SRC 的两份 conf 已用 `host.docker.internal`（配合 compose `extra_hosts: host.docker.internal:host-gateway`），**无需写死公网 IP**；「改 IP」适用于课程阶段写死地址的代码。
4. 【P2】L49/L50/L56-58「把 IP 改成线上」→ 补括注：最终仓库这些地址走环境变量——client 为 `VITE_API_BASE_URL` / `VITE_RELEASE_BASE_URL`（client/.env.example），release 为 `NEXT_PUBLIC_API_BASE_URL`（release/.env.example，构建期注入），改 `.env` 不必改源码。
5. 【P2】L56/L70 `components/componentRender.tsx` → SRC 实名 `src/components/ComponentRender.tsx`（大写 C）。
6. 【P2】端口规划块（L24-30）与小结第 1 条与 SRC 四服务端口映射逐一一致；安全组四端口正确。

### 27-2.项目自动化部署上线—镜像名称_BUG_修复 — 需修

1. 【P1】L44 原句「打开对应 Dockerfile：`server/nginx.dockerfile` 与 `release/nginx.dockerfile`」→ SRC 实名 `server.nginx.Dockerfile` 与 `release.nginx.Dockerfile`（簇一；本篇是 BUG 修复叙事，文件名错了整个排障故事都对不上仓库）。
2. 【P2】L37「正确写法 `FROM nginx`」→ 括注 SRC 实际为 `FROM nginx:1.25.0-alpine`，顺带说明 pin tag（固定基础镜像版本）是生产惯例，免得读者把「裸 nginx」当最佳实践。
3. 【P2】标题（L2、L9）空格形 → 文件名下划线形（簇二 A），同步 27-1 L74 引用。

（`FROM nginx::` 多冒号的报错故事本身成立；「海外镜像源慢是提醒不是报错」的备注有用；运行/日志/并行三步骤描述与 25-x 衔接一致。）

### 27-3.项目自动化部署上线—Dockerfile名称_BUG_修复 — 需修

1. 【P2】贯穿篇的 `release.dockerfile`（L11 导语、L24、L28、L30、L34 `mv` 命令、L39、L49、L50）→ SRC 实名 `release.Dockerfile`（簇一，大小写；`mv Releases.dockerfile release.Dockerfile`）。故事线（多写 s、流水线配置与文件名不一致）保留。
2. 【P2】标题（L2、L9）空格形 → 下划线形（簇二 A），同步 27-2 L58、27-4 L15 引用。

（ACR 地域选广州否则「无数据」、清理历史镜像的提示合理。）

### 27-4.项目自动化部署上线—Docker-compose上传_BUG_修复 — 需修

1. 【P2】L22「第二阶段'Docker-compose 文件上传'却报错」、L50「第二阶段…」、L51「第三阶段 Docker 部署」→ 阶段口径与 25-4/26-1 冲突（簇四 3），按簇四 3 的统一口径改。
2. 【P2】标题（L2、L9）空格形 → 下划线形（簇二 A），同步 27-3 L56、27-5 L15 引用。

（tar `-c` vs `-C` 的根因分析正确：`-c` 创建归档与 `zxvf` 解压模式冲突必失败，改 `-C` 后可执行；L51 四变量关联与 26-3 呼应一致。）

### 27-5.项目自动化部署上线—访问后端接口+发布页面 — 需修

1. 【P1】路由残留（scan6 清单外正式上报）：L30 `GET http://<服务器IP>:5001/api/local/release`、L32 `GET http://<服务器IP>:5000/api/local/release`、L62 小结「发布页数据接口 `/api/local/release`」→ SRC `GET /api/low_code/release?id=<页面id>`（`@Controller('low_code')` + `@Get('release')` + 全局前缀 api）。与 scan6 A8-1 对 19-5、b6 簇一的处理一致。顺带：不带 `?id=` 时 TypeORM 空条件会返回表中第一行（review-eng-b P2#2），示例补上 `?id=` 更严谨。
2. 【P1】L56 原句「提交内容（如姓名、描述）以 `v6` 字段存储」→ SRC `component_data` 表只有 `id / page_id / user / props` 四列（docs/schema.sql），问卷答案是 `props` 里的 JSON 数组项 `{ id, value }`，匿名标识在 `user`（MD5(ip+ua)），不存在 `v6` 字段。改为「提交内容存入 `props` 字段（JSON 数组，每项 `{id, value}`），访客标识存 `user`」。b6 20-1 已立同口径。
3. 【P2】L54/L64「IP + 设备」防重口径 → 簇五（加 trust proxy 限定注）。
4. 【P2】L35「问卷类组件（input、textarea、radio、checkbox）」→ `textarea` → `textArea`（簇六）。

（4001/4000 直连与代理的区分、发布页必须带页面 ID 访问 `/<id>`（L44-50，与 release App Router 动态路由一致）、根路径「页面未找到」属正常，均正确。）

### 27-6.项目自动化部署上线—前端编辑页面Bucket绑定域名 — 合格

（公共读 + 默认首页 index.html + 域名管理三前置、跨账号 TXT 所有权验证 → CNAME 解析的两步流程与 OSS 控制台实际一致；`16web.net`/`cdlocal.16web.net` 为演示域名且已标「如」，无需括注。互链 2 处真实。）

### 27-7.项目自动化部署上线—线上前端项目编辑平台功能确认 — 合格（附 P2 建议）

1. 【P2】L22「系统会从后端接口读取之前发布过的缓存数据」→ 建议加现状注（簇七）：最终仓库 `release_with_user` 实现传 null 恒空（review-eng-b P0-7），线上实测「还能看到旧数据」的来源是浏览器 localStorage 草稿，参照 b6 对 19-5 的处理加一句即可。

（OSS accessKeySecret 占位符的安全提醒（L35）是本批少见的好实践提示；登录/组件增删/拖拽/草稿/预览/发布的功能确认叙事与前文功能期篇目一致。）

### 27-8.项目自动化部署上线—线上前端项目后台数据统计功能确认 — 合格（附 P2 建议）

1. 【P2】L33/L47 `textarea` → `textArea`（簇六）。

（统计页左表右图、Excel/压缩包导出、动态表格与饼图/柱状图联动的确认叙事与 21-x/22-x 建立的功能一致；收尾对三个项目的总结与前文呼应。）

### 28-1.Jmeter性能压测—为什么要学习Jmeter压测 — 合格（附 P2 建议）

1. 【P2】L40「其测试平台底层**几乎都**基于 JMeter 做二次封装」→ 表述夸大（簇八），降格为「不少公司的压测平台基于 JMeter 二次封装」。

（Postman 偏功能 / JMeter 偏性能的定位区分、开源免费跨平台、可测 FTP/JDBC 等协议范围均属实。）

### 28-2.Jmeter性能压测—性能测试分类和常见工具 — 合格（附 P2 建议）

1. 【P2】L47 表格「大厂普遍二次封装」→ 簇八同步降格。

（性能/压力/负载/稳定性四类定义与区分准确；LoadRunner、Apache ab、Web Bench 的优缺点评价公允；ab「对目标服务器负载大」的提醒实用。）

### 28-3.Jmeter性能压测—基本介绍和使场景 — 合格（附 P2 建议）

1. 【P2】L33 整句加粗「**JMeter 不在浏览器层面工作，它是在协议级别工作**」→ 只加粗关键词（簇三去 AI 味判例）。
2. 【P2】文件名/标题「基本介绍和**使**场景」缺「用」字（应为「使用场景」）。title 与文件名一致、28-2 L64 引用同名，暂不算断链；属系列级命名瑕疵，如修需三处同步（文件重命名 + 本篇 title/h1 + 28-2 引用），可与 16-7「多选框框」同类归入系列小洁癖。

（「JMeter 不是浏览器、协议层工作、不执行 JS」的技术表述准确；静态资源用浏览器 Network 看性能、异步接口才用 JMeter 的场景划分合理；对 08 期《多环境快速安装Jmeter5》的前向引用真实存在。）

---

## 三、统计

| 项 | 数量 |
|---|---|
| 总篇数 | 22 |
| 合格（含附 P2 建议 5 篇：27-7、27-8、28-1、28-2、28-3；纯合格 3 篇：25-4、26-3、27-6） | **8** |
| 需修 | **14** |
| P0 | 0 |
| P1 | 7（25-3 标题整体断链 1；簇一 Dockerfile/Nginx 路径错认 4（25-5、25-7、27-1、27-2）；27-5 `/local` 路由残留 1 + `v6` 字段 1） |
| P2 | 约 33（title/h1 变体与下划线簇 8 篇 13 处（含引用同步）；簇一大小写残留 5；批内口径冲突 4；现状注/括注 5；textarea 3；防重口径 1；JMeter 夸大 3；整句加粗 1；文件名 typo 1；跨期 title 断链 1 簇） |

需修优先级建议：

1. **先修簇一（P1，可执行性）**：25-5/25-7/27-2 的 Dockerfile 路径、27-1 的 Nginx conf 路径与扩展名、25-6/25-8/27-3 的大小写——统一改为 SRC 实名（根目录 `server.Dockerfile` / `release.Dockerfile` / `server.nginx.Dockerfile` / `release.nginx.Dockerfile`，`nginx/server.nginx.conf` / `nginx/release.nginx.conf`）。这是「照着做会构建失败」的一批。
2. **再修 27-5 两个 P1**：`/api/local/release` ×3 → `/api/low_code/release?id=`；`v6` 字段 → `props`（JSON 数组）+ `user`。与 scan6 A8、b6 簇一口径对齐。
3. **簇二标题**：25-3（P1）改 title/h1；25-1/25-2 标点变体与 26-1/27-1~27-4 下划线簇（P2）一次批量完成，并同步 12 处批内引用名。
4. **簇四口径、簇五~簇八注记**（P2）：26-2/27-4 阶段编号、25-8 Bucket 名、26-1 制品名、27-1 两处现状注（host.docker.internal / env 变量）、27-5 防重限定、27-7 现状注、28-x 夸大降格——可与 08 期审稿合并批量执行。
5. **簇三跨期 title 断链**（24-1、24-2、23-5、23-6、28-4）转交 06/08 期审稿处理，P7 侧引用名写法正确、无需改。
