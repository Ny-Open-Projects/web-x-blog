# PASS3 — 独立第三遍扫描：素材技术点全集 vs knowledge_graph.json（47 节点 / 120 边）

- 扫描对象：`work/source/24.真实高质量低代码商业项目-前端后端运维管理系统/`（23 个章目录、547 篇 .md，约 1.75M 字符；第 19~22 章目录名带 week 前缀 1-1/2-1…）
- 对照对象：`/Volumes/SAMSUNG/ai-done/24.真实高质量低代码商业项目-前端后端运维管理系统/graph/knowledge_graph.json`、INDEX.md、verification_manifest.json
- 方法：脚本统计各章讲稿数/字数 → 关键词/文件名全量匹配 → 抽样读取原文验证。代码模块 7 个（opsflow-web/ui/server/admin、mongo-lab、ts-lab、vue-starter）已确认存在于 `课程源码+电子书/解压后/`，非幽灵节点。

## 各章规模（实测）

| 章 | 篇数 | 字符 | 章 | 篇数 | 字符 |
|---|---|---|---|---|---|
| 1 | 1 | 4,555 | 13 | 39 | 156,093 |
| 2 | 4 | 12,717 | 14 | 41 | 153,531 |
| 3 | 10 | 38,591 | 15 | 26 | 93,529 |
| 4 | 34 | 125,387 | 16 | 31 | 105,445 |
| 5 | 21 | 72,703 | 17 | 29 | 102,323 |
| 6 | 18 | 60,859 | 18 | 30 | 103,015 |
| 7 | 21 | 70,698 | 19 | 29 | 100,880 |
| 8 | 24 | 92,057 | 20 | 28 | 101,754 |
| 9 | 17 | 60,925 | 21 | 23 | 103,727 |
| 10 | 27 | 100,708 | 22 | 17 | 76,766 |
| 11 | 25 | 94,840 | 12 | 17 | 69,098 |

## 一、幽灵节点 / 幽灵边（图谱有、素材支撑不足）

1. **C_vue2「Vue 2」概念节点**：全素材仅 2 处顺带对比提及（`第1章/1-1 课程导学​.md` L229「要掌握 Vue 2 的基础知识」、`第8章/8-15 Vue3 中组件通信的四种方法.md` L11），无任何 Vue2 教学内容。但图谱有 ch04→C_vue2、ch05→C_vue2 两条 covers 边 → 建议：降级或删边（ch05 的 21 篇全为工具链/Vue Router/Vuex 搭建，无 Vue2）。
2. **边 ch18→C_nuxt（covers）**：第 18 章 30 篇全部是 B 端功能（html2canvas 截图发布、渠道二维码、Clipboard、FileSaver、useLoadMore），`grep -i nuxt 第18章 = 0 命中`。Nuxt 从第 20 章才开始。→ 建议删边或改为 ch18→业务功能概念。
3. **边 ch19→C_cicd（covers）**：第 19 章 `grep "github actions" = 0 命中`，内容是 Webpack 优化 + Nginx/HTTP 缓存。→ 建议删边。
4. **边 ch19→C_docker（covers）**：仅 `第19章/5-1部署的概念_.md` L41/L45 顺带回顾 Docker Compose，非教学内容。→ 建议删边或降为弱引用。
5. 代码模块 7 个均实测存在（`课程源码+电子书/解压后/`），**无幽灵模块节点**。

## 二、少漏技术点清单（素材有、图谱未收录）

| # | 技术点 | 证据（素材路径） | 建议动作 |
|---|---|---|---|
| 1 | Vue Router（SPA 路由原理、嵌套路由、路由守卫/权限验证） | 第5章/5-12~5-15；第17章/5-6~5-7「路由权限验证」 | 补概念卡 + 边 ch05/ch17 |
| 2 | Vuex 状态管理（module 拆分、action、mutations 测试） | 第5章/5-16~5-20；第6章/6-2；第16章/4-3；第17章/2-3 | 补概念卡（mod_opsflow-web.tech 里已有 Vuex，但无节点无边） |
| 3 | Vite（创建项目、与 Vue CLI 对比） | 第4章/4-17「使用 vite 创建项目」；第5章/5-4「Vue CLI 对战 Vite」 | 补概念卡 + 边 ch04/ch05 |
| 4 | Webpack 深入：手写 loader/plugin、bundle-analyzer、分包、路由懒加载、chainWebpack | 第19章/3-2~3-5、4-2~4-9 | 补概念卡「Webpack 工程化」 + 边 ch19 |
| 5 | Rollup 与组件库打包（UMD/ESM 双格式、Vue/TS 插件、npm link、插件原理、Snowpack 花絮） | 第9章/9-4~9-17 | 补概念卡 + 边 ch09、mod_opsflow-ui |
| 6 | 前端工程化规范：ESLint/Prettier/Git Flow/项目结构 | 第4章/4-19~4-20；第5章/5-5~5-9 | 补概念卡 + 边 ch04/ch05 |
| 7 | TDD 开发方式与 Jest mock 体系（mock timers/第三方模块/全局组件、异步测试） | 第7章/7-3~7-16、7-17~7-20（TDD）；第8章/8-5、8-10、8-13、8-19 | 建议细分 C_test 或补 TDD 边 ch07/ch08 |
| 8 | Web 性能优化：Nginx、HTTP 缓存（Expires/Cache-Control/Etag/Last-Modified）、gzip/Brotli、HTTP2、keep-alive | 第19章/5-2~5-9 | 补概念卡「HTTP 优化/Nginx」 + 边 ch19（这是 ch19 的真实主内容，可修正幽灵边） |
| 9 | 多环境与环境变量（dev/staging/prod、mode、.env） | 第14章/14-10；第19章/2-1~2-5；第20章/20-23 | 补概念卡（跨前后端） |
| 10 | Node 进程模型：Cluster、Egg 多进程、压力测试 | 第14章/14-3~14-6 | 补概念卡 + 边 ch14 |
| 11 | Docker 细分：Dockerfile、docker-compose、镜像体积/构建速度优化、MongoDB 权限、.env 敏感信息、YAML 语法 | 第14章/14-17~14-29 | 建议 C_docker 下补细分边或概念 |
| 12 | GitHub Actions 细分：Secrets、阿里云 ACR 推镜像、自动部署+回滚、release-it 版本发布 | 第14章/14-30~14-40 | 建议 C_cicd 细分；release-it（14-40）单独补点 |
| 13 | 云服务器运维：SSH key 免密登录、Linux 装机 | 第14章/14-7~14-9 | 补概念卡 + 边 ch14 |
| 14 | 图片处理与流：Sharp 缩略图、Stream/pipeline、busboy/co-busboy、egg-multipart 源码 | 第13章/13-4~13-16 | 补概念卡「流与图片处理」 + 边 ch13 |
| 15 | CropperJS 图片裁剪 | 第15章/2-2~2-6 | 补卡 + 边 ch15 |
| 16 | B 端功能生态库：html2canvas（含原理手写）、qrcode、Clipboard.js、FileSaver.js（含源码解析） | 第18章/2-3~2-7、4-2、5-1~5-4、7-1~7-4 | 补概念卡「发布链路工具库」 + 边 ch18 |
| 17 | 组合式函数库（usePublishWork/useLoadMore/useClickOutside/InlineEdit/actionWrapper） | 第15章/3-4~3-5、4-1~4-5；第17章/4-5；第18章/3-3、6-2~6-6 | 补概念卡「Vue3 组合式函数复用」 |
| 18 | Mock 与前后端分离联调：JSON Server + JWT mock | 第17章/3-1~3-4 | 补卡 + 边 ch17 |
| 19 | 表单验证体系：egg-validate、错误码规范化、AForm/useForm 源码解析 | 第12章/12-5~12-6；第17章/4-1、4-6~4-7 | 补卡 |
| 20 | Session 体系细节：Cookie、egg-session 外部存储、koa-session 源码分析、bcrypt、mongoose-sequence | 第12章/12-8~12-17 | C_auth 太粗，建议细分「JWT vs Session」两卡 |
| 21 | MongoDB 进阶：索引、聚合 $lookup、数据库设计原则、egg-mongoose 源码解读、egg 插件抽象 | 第11章/11-12~11-17、11-24、11-23 | 建议 C_mongo 下细分或补边 ch11 |
| 22 | Nuxt3 细分：渲染模式、Nitro server/服务器中间件/存储层、nuxt-mongoose、SEO | 第20章/20-3、20-17~20-27 | 建议 C_nuxt 细分 + 边 ch20 |
| 23 | Nuxt 生态：Zod（前后端验证）、VeeValidate、NuxtUI、Tailwind CSS | 第21章/21-1~21-9、21-16；第1章/1-1 提及 Tailwind | 补概念卡 4 张或合并「Nuxt 全栈验证/UI 生态」 |
| 24 | 管理系统部署：Nuxt 构建、部署脚本、PM2、Bun | 第22章/22-13~22-17 | 补卡 + 边 ch22 |
| 25 | 业务概念缺失：作品发布流程/展示渠道/H5 渲染链路（低代码项目的核心业务闭环） | 第13章/13-28~13-29；第17章/6-4~6-7 自动保存；第18章/3-1~3-2 | 补业务概念卡，串起 C_editor/C_ssr/C_oss |

## 三、明显缺失的关键边

1. `C_ssr → mod_opsflow-server`（H5 SSR 渲染产物由 server 生成并上传 OSS：第13章/13-23~13-27）；现有 `C_ssr → mod_opsflow-web` 不准确。
2. `mod_opsflow-admin → C_upload / C_oss`（admin 也有上传组件并传阿里云：第22章/22-4~22-7）。
3. `mod_opsflow-admin → C_docker` 或部署相关（22-13~22-16 部署章节；虽用 PM2 而非 Docker，图谱应体现「admin 部署方式与 web 不同」）。
4. `ch05 → Vue Router/Vuex/Vite`（若补上概念卡，需加 covers 边）。
5. `mod_opsflow-server → mod_opsflow-web` 的 API 依赖方向已有 depends_on（web→server），但缺 `mod_opsflow-admin → mod_opsflow-server`（admin 调同一套后端：第20-21 章注册/登录/表格均打后端接口）。
6. `ch14 → C_auth`？14-21/14-22 MongoDB 权限验证属 Docker 篇内容，可加弱边或忽略。

## 四、核对口径

- INDEX.md 写「22 章 / 512 篇」，实测 source 下 23 个目录（含「第23章」不存在——实为第 19~22 章目录名内含周次子编号，仍为 22 章）、547 篇 .md。第 7 章 Done/ 35 篇重复转写的说法与实测（第 7 章 21 篇 .md）不符——Done 副本不在本 source 树中，差异记录备查。
- verification_manifest.json 的 7 个 verified 模块路径全部实测存在。

## 五、结论

- 幽灵：0 个幽灵节点（7 个代码模块全实测存在）；4 条幽灵/弱边（ch18→Nuxt、ch19→CI/CD、ch19→Docker、以及 C_vue2 的两条覆盖边支撑不足）。
- 少漏：25 条技术点未入图（集中在打包体系 Rollup/Webpack、Web 性能优化、流/图片处理、B 端功能工具库、Nuxt 生态、组合式函数、Session/JWT 细分）。
- 缺边：6 类关键关联缺失（SSR→server、admin→upload/OSS、admin→server API、工程化概念边等）。
