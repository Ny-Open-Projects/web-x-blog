# 扫描7：物料内容深挖（25 小滴课堂低代码大课）

> 数据源：`graph.json` / `file_manifest.json`（17146 条物料）、物理工程 `lowcode-platform`（A）与 `course-reference/lowcode-platform-full`（B）、`audio/`（229 转写）。
> 与 scan1~5 的分工：只列**博客正文没讲、且 scan3 也没覆盖到配置细节**的知识点。

## 0. 关键前提：物料实体不在本工作区

- 物料根目录是外部盘 `X:\小滴课堂-解压`（见 SRC/资料关联索引.md），本工作区**只有清单（file_manifest.json）无实体**。抽样核验 200 条 manifest 路径，物理存在 0/200；「笔记+资料-已8期」「安装包（已8期）」「代码（已8期）」目录均不在 SRC 下。
- 本工作区实际可深读的实体只有：`blog/`（229 篇）、`audio/`（229 md + 229 srt）、两个代码工程（A/B，scan3 已析）。
- 因此 doc/image 类的"内容深读"只能做到：**名称 + 体积 + 挂链课号 + 博客/音频对内容的转写覆盖度核对**；原始 PDF/drawio/mwb 内容需回到原始盘才能读。这本身是成稿配图、引用资料的硬约束，见 §5。

## 1. doc 类（299 条，唯一去重后约 36+263）

### 1.1 课程级公共资料（笔记+资料-已8期/，全部无实体，仅清单）

| 物料 | 体积 | 挂链情况 | 博客覆盖结论 |
|---|---|---|---|
| 全栈低代码平台需求文档.pdf | 818KB | 挂 1-2、5-1~5-3 等 | **已讲透**：5-1（前言/版本信息/变更日志/术语表 6 词条）、5-2~5-3（流程图+原型图）就是逐节讲这份 PDF，无遗留知识点 |
| 全栈多端低代码平台项目大课.pdf | 29.5MB | 几乎每课都挂 | 即全套课程笔记成书；229 篇博客=其音频化转写，正文知识点以博客为准，无独立增量 |
| 图.drawio（+15 个 .bkp/.dtmp 备份） | 42.6KB | 1-2、2-x、5-x、需求/流程相关课 | 内容=5-2/5-3 讲的流程图，已讲；**.bkp/.dtmp 是 drawio 自动备份，可证明流程图经≥15 次迭代**，可作"需求文档是打磨出来的"话术素材（新，博客未提） |
| 低代码平台数据库设计.mwb | 10.7KB | 数据库相关课 | MySQL Workbench ER 模型；博客只讲过建表，**没讲"先画 ER 图再建表"这一设计流程**（mwb 文件是证据，可补一句） |
| xdclass-lowcode.sql | 7.3KB | 数据库课 | 原始建库 dump；无实体，但其"后代"即物理工程 B 的 `docs/schema.sql`（可读，见 §2.2） |
| 高级前端开发工程师简历【前端大课+低代码】.docx/pdf | 147KB/431KB | 31-1~31-4 | 简历写法已讲透（scan2 320-324 行），docx 本体无新知 |

### 1.2 安装包随附文档（红线与无效项）

- `安装包（已8期）/Navicat/windows/navicate安装和爆破包/步骤.docx / 步骤.pdf`：**Navicat 破解教程**。红线：博客成稿绝不可引用、复述或链接该物料；替代口径用官方试用版/DBeaver。
- JMeter `printable_docs/` 下 7 个 PDF（usermanual/tutorial）＝Apache 官方手册样板，无知识增量；`bin/templates/*.jmx` 17 个＝官方示例模板，同无增量。
- doc 里 360 个 `.md`＝每课代码包的 Nest CLI 默认 README 模板（packages/client、packages/server 各一份×每课快照），内容零差异，无知识。

### 1.3 nginx conf 快照链（doc 类 14 个 .conf，新发现）

- conf 出现的课号演进：`23-4`（首个 server.nginx.conf）→ `23-5` → `23-6`（新增 release.nginx.conf，双网关成型）→ `24-2` → `27-1/27-2/27-3` → `30-6`（最终版）。物理工程只有最终版（scan3 已析其内容）。
- **可讲的新点**：nginx 双 conf（server/release）不是一开始就有的，是 23-6 才拆出 release 网关——"先单网关、后按 C 端独立扩成双网关"的演进顺序，博客正文没讲；成稿可作为部署章节的叙事线。〔出处：manifest 中各课号 nginx/*.nginx.conf 路径〕
- 最终版 conf 里的 `X-Client-Verify SUCCESS`、`proxy_buffering off` 两个非默认项，scan3 未提：前者是自定义透传头（示例值，非真实校验），后者对 SSR 页面代理有意义（避免缓冲大 HTML）。〔`course-reference/lowcode-platform-full/nginx/server.nginx.conf`、`release.nginx.conf`〕

## 2. data 类（1323 条）

### 2.1 组成判定：绝大多数是脚手架快照，无独立知识

- 433 package.json / 332 tsconfig / 105 nest-cli / 100 pnpm-workspace……＝116 个课号代码目录的**演进快照**，实体不在盘上，无法逐课 diff 依赖引入时点（scan3 已用最终工程版本表替代）。
- 官方包样板：`jmeter.properties`、`saveservice.properties`、`CSVSample_*.csv`、`GrafanaJMeterTemplate.json` 等＝JMeter 5.6.3 自带，无增量。`28-7` 博客讲的 `sampleresult.default.encoding=UTF-8` 改法是这份 properties 的唯一可讲点，已讲。
- **jest-e2e.json ×9**（预先课代码包内）：Nest 脚手架自带 supertest e2e 配置。博客第 2 章只一句"test/ 是 Nest 比 Express 多出的 e2e 目录"带过，**未展开 jest-e2e.json 的存在与作用**。可在预先课成稿补一句：Nest 生成的 e2e 走独立 `jest-e2e.json` 配置 + supertest 发真实 HTTP 请求。〔出处：manifest `代码（已8期）/代码（已8期）/{8-2..}/lowcode/**/jest-e2e.json`〕

### 2.2 物理可读的 data/doc 配置（A/B 工程，仅列 scan3 未覆盖项）

- **B 工程三包 .env.example**（scan3 未逐项列）：
  - `packages/server/.env.example`：`JWT_SECRET` 附生成命令 `node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"`；`DB_SYNCHRONIZE` 注释明确"生产务必 false，用 migration"；短信端点写死 `https://api-v2.xdclass.net/send_sms`；微信/OSS/SMS 全部"选填不填则功能不可用"的**优雅降级约定**。博客正文（11-2/11-4 等）讲了 Redis 模块与短信接入，但没讲 env 降级约定与 JWT secret 生成命令。〔`course-reference/lowcode-platform-full/packages/server/.env.example`〕
  - `packages/client/.env.example`：Vite 约定 `.env.local` + `VITE_API_BASE_URL` 指向 Nginx 网关 5000（不是直连 Nest 3000）；`packages/release/.env.example`：Next `NEXT_PUBLIC_` 前缀双端注入。三端"都指向网关而非源服务"是配置级架构事实，博客未明说。〔同目录 client/release〕
  - 库名证据：`DB_DATABASE=xdclass-lowcode`——与外部盘 xdclass-lowcode.sql 同名，印证工程 B 与课程资料是同一套库。
- **A 工程 .env.example**（scan3 讲了沙箱 env 化，漏了两项）：
  - `RATE_LIMIT_PER_TENANT=1000`：按租户限流的商业化钩子预留，注释直说"限流/计量（商业化钩子预留）"——多租户商业化的第一个配置位，scan3 未提。〔`lowcode-platform/.env.example`〕
  - LLM 节点示例配置给出 `base=https://dashscope.aliyuncs.com/compatible-mode/v1 model=qwen-plus`（OpenAI 兼容网关；scan3 只讲了机制，没讲这份可抄的通义示例配置）。
  - Docker socket 双平台注释：Linux/macOS `/var/run/docker.sock`，Windows `//./pipe/docker_engine`（scan3 只说 Windows 命名管道，未给字面值）。
- **B 工程 docs/schema.sql 种子数据**（scan3 只析了表结构，种子可讲）：
  - `component` AUTO_INCREMENT=17：出厂即带 1 页 15 组件的成品页种子——swiper（3 图轮播，每图含 `handleClicked:"open-url"`+link 的点击行为配置）、list×4、video、问卷四件套 input/textArea/radio/checkbox（radio/checkbox 的 options JSON 内选项 id 用 ULID 风格 `01HFBG…`）。**组件 options 的字段命名（fit/height/handleClicked/titleLink/avatar）是 Blog 没逐一列过的数据字典**。〔`docs/schema.sql` 45~57 行〕
  - `user` 种子只有 1 条微信登录用户：`open_id` 非空而 `phone/password` 为空串——印证"微信注册用户不落手机号密码、双登录体系并存"的数据形态（scan3 表结构列了 open_id 列，但没讲这个空值语义）。〔schema.sql 143 行〕
  - 种子里的演示域名 `lowcode.16web.net`（OSS 自定义域名回源 upload_files/）——课程线上演示环境地址，成稿可注明数据来源，也可作为"OSS 必配自定义域名"的实例。
  - `docs/API.md` 错误约定表（scan3 未提）：`code=-1` 业务/DTO 校验失败（含字段级提示数组）、`401` token 缺失/过期走过滤器统一包装、`500` 发布事务失败——**平台统一错误码契约**，成稿可直接引。〔`docs/API.md` §七〕
  - `docs/API.md` 端点细节 3 处博客未讲：图形验证码 key=MD5(ip+ua) 由服务端自动生成（博客只说"Redis 自定义 key"，没给 key 公式）；微信扫码 Redis 记 `{isScan:"no"}` 120s → 回调置 yes → 前端 ticket 轮询 check_scan 的完整状态机（scan3 一句带过）；问卷重复提交防重是"服务端 MD5(ip+ua) 匿名标识 + 提交时二次查重"双层。〔`docs/API.md` 11/22-24/52-53 行〕

## 3. audio/ 对应关系核查（任务项 3，结论：零缺口）

- `audio/` 下 **229 个 .md + 229 个 .srt**，与 graph 229 篇博客**文件名逐一相同**（blog-not-audio=0，audio-not-blog=0），即"229 转写 ↔ 229 博客稿"完整闭环；但 blog 与 audio 同名文件内容**不同**（blog 是清洗稿，audio 是原始转写，抽 diff 确认 DIFFER）。
- ep_ref 只给 189 篇主课；**40 篇无 ep_ref 全部集中在 00 预先课**（graph 按章容器 pre_chapter 挂链，不走 ep_ref），40 篇的转写文件在 `audio/00.预先课 - 低代码大课必备技术/` 下物理齐全（缺 0）。**不存在"有音频没博客稿"的集**。
- 音频原始音/视频文件 0 个（只有 md/srt 文本对），无需处理版权音频。
- 附带发现：**13-4 课无视频也无博客**（第三期 nums 缺 1304），其代码快照目录 13-4 以 orphan_code 锚点挂到 13-3——成稿时若引用 13-4 代码需注明"该集未录制，内容并入 13-3"。〔`资料关联索引.md` 9161 行；graph stage03 nums〕

## 4. image 类（任务项 4）

- 1102 张图（唯一文件名 220 个）：几乎全部是 `image-20231102….png` 型**笔记 PDF 截图**，按课挂链（160 篇有图）；具名图仅框架样板（react.svg/next.svg/vite.svg/vercel.svg/docker.svg/logo*/favicon）——均为脚手架自带，**无知识**。
- 独立的架构图/流程图实体**不存在**（图.drawio、mwb ER 图、29.5MB 笔记 PDF 内的图都在外部盘）；且 229 篇 blog md 中 `![` 图片引用为 **0**——博客成稿目前是纯文字。
- **成稿建议**：若需要配图，两条路——① 回原始盘取 `笔记+资料-已8期/图.drawio`（42.6KB，可编辑源文件）重导出；② 依据 scan3 的架构事实自绘（三端/双网关/端口链 5000→5001→3000、4000→4001→3000 已足够画图）。截图型物料（1102 张）不建议直接用：含网盘水印与第三方品牌信息。

## 5. 新发现知识点清单（可直接进博客的增量，汇总）

1. 需求文档之外的过程资产：流程图 drawio 有 ≥15 个自动备份版本、数据库设计有独立 Workbench ER 模型——"大厂产研流程"章节可用作"文档是迭代产物"的实证。（§1.1）
2. nginx 双网关是 23-6 才从单网关拆出的演进结果；最终 conf 有 `X-Client-Verify`（示例头）与 `proxy_buffering off`（SSR 代理）两个非默认项。（§1.3）
3. Nest 脚手架自带 jest-e2e.json + supertest 的 e2e 形态，预先课博客仅提目录未提配置。（§2.1）
4. B 工程 env 约定：JWT_SECRET 现成生成命令、DB_SYNCHRONIZE 生产关闭走 migration、第三方服务"选填即降级"、三端一律指向网关而非源服务、库名 xdclass-lowcode。（§2.2）
5. A 工程 env：RATE_LIMIT_PER_TENANT 商业化限流钩子、通义 compatible-mode 的 LLM 网关示例配置、Docker socket 双平台字面值。（§2.2）
6. schema.sql 种子数据的三个可讲点：15 组件成品页出厂种子及 options 字段字典（含 handleClicked 点击行为、ULID 选项 id）、微信用户 open_id 有值而 phone/password 空串的双登录数据形态、lowcode.16web.net 演示域名即 OSS 自定义域名实例。（§2.2）
7. 平台统一错误码契约（-1/401/500）与三个 API 细节：验证码 key=MD5(ip+ua)、微信扫码 isScan 120s 状态机、问卷防重双层（匿名标识+二次查重）。（§2.2）
8. 物料红线一条：Navicat 破解步骤 PDF/docx 不得在任何成稿中引用。（§1.2）
9. 13-4 集缺失（无视频/无博客），代码快照挂在 13-3 名下；40 篇无 ep_ref 文章为预先课章容器挂链，音频转写齐全，无内容缺口。（§3）

## 6. 遗留事项（需人工/原始盘）

- 笔记+资料 5 个核心原件（需求文档 PDF、项目大课 PDF 29.5MB、图.drawio、mwb、xdclass-lowcode.sql）与 61 个课程自建 .jmx 实体在外部盘 `X:\小滴课堂-解压`；如需在博客成稿中引用原文/原图，需从原始盘补取（本工作区不可读）。
- .jmx 课程自建件仅 4 个在课号目录（28-5/28-9/30-1/30-2），其余 57 个是 JMeter 安装包 backups/自动备份，非独立资产——scan1 的 61 个 .jmx 计数含样板，引用时注意区分。
