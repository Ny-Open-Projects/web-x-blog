# 课程25 知识卡片总目（扫描8 产出）

> 源报告：`../reports/scan2-knowledge.md`（229 篇知识点总账）、`../reports/scan4-lowcode-domain.md`（领域体系）、`../reports/scan3-code.md`（代码实况）。
> 卡片为 hexo front-matter 风格，可直接进站。front-matter：`categories: [课程, 低代码]`、`tags: [25-lowcode, 概念/原理/实战/面试]`。
> 共 35 张：概念 11 + 原理 6 + 实战 12 + 面试 6。

## 概念卡（是什么）

| 文件 | 主题 | 出处 |
|---|---|---|
| concept-01-meta-driven | 元信息驱动：低代码第一性原理 | 14-2、18-5 |
| concept-02-schema-dsl | Schema 与 DSL：数据契约层 | 8-5、14-2 |
| concept-03-material-registry | 物料体系与组件注册表 | 14-7、14-9 |
| concept-04-render-engine | 渲染引擎：读 Schema 画 UI | 19-3、20-6 |
| concept-05-data-model | 五张核心表与关系化 Schema 存储 | 6-4、14-2 |
| concept-06-protocol | 低代码协议与标准化 | scan4 §2/§5 |
| concept-07-permission-model | 权限模型与多端差异化鉴权 | 14-3、20-3 |
| concept-08-release-pipeline | 发布链路：草稿/预览/发布三态 | 19-2~19-5 |
| concept-09-sandbox | 沙箱：执行不可信代码的隔离方案 | scan3 §2-A |
| concept-10-workflow-dag | 工作流引擎：节点契约与 DAG | scan3 §2-A |
| concept-11-lowcode-vs-nocode | 低代码 vs 零代码 vs 自研选型 | scan4 §9 |

## 原理卡（为什么）

| 文件 | 主题 | 出处 |
|---|---|---|
| principle-01-schema-to-ui | Schema→UI 驱动机制（store→视图闭环） | 14-8、14-9 |
| principle-02-drag-index-swap | 拖拽排序的本质：数组索引交换 | 18-4、18-5 |
| principle-03-transaction-release | 事务化发布：QueryRunner 三段式 | 14-4、10-8 |
| principle-04-cache-qps | Redis 缓存优化与 QPS 压测验证 | 30-6、29-1 |
| principle-05-jwt-chain | JWT 鉴权链路：签发→全局守卫 | 8-4、11-7、14-3 |
| principle-06-undo-redo | 撤销/重做：状态快照模型 | 18-5 |

## 实战卡（怎么做/怎么排坑）

| 文件 | 主题 | 出处 |
|---|---|---|
| practice-01-nestjs-core | NestJS 全家桶要点 | 00-4~5、9-3 |
| practice-02-typeorm-pitfalls | TypeORM 要点与高频坑 | 10-1~10-8 |
| practice-03-captcha-antifraud | 手机验证码六步防刷 | 11-1~11-6 |
| practice-04-wechat-scan | 微信扫码登录全链路 | 12-1~12-6 |
| practice-05-oss-resource | OSS 资源体系：上传/删除/CDN | 17-1~17-5 |
| practice-06-excel-export | ExcelJS 导出 + JSZip 压缩包 | 21-9、22-1 |
| practice-07-docker-deploy | Docker/云效部署：四镜像双 Nginx | 23-1~27-4 |
| practice-08-jmeter | JMeter 压测实战 | 28-1~29-3 |
| practice-09-redis-cache-pattern | Redis 工程化封装与 getCachedData | 11-2、30-6 |
| practice-10-editor-interactions | 工具栏定位与滚动显隐 | 18-6~18-8 |
| practice-11-stat-frontend | 问卷统计：动态表头与 ECharts | 21-2~22-5 |
| practice-12-component-recipe | 组件开发五步范式 | 15-1~16-7 |

## 面试卡

| 文件 | 主题 | 出处 |
|---|---|---|
| interview-01-tech-choice | 技术选型话术 | 2-3~2-9、31-1 |
| interview-02-security | 安全类问题应答 | 8-3、11-6、14-3 |
| interview-03-performance | 性能问题应答（压测数据说话） | 29-1、30-6 |
| interview-04-lowcode-highlights | 低代码项目亮点话术 | 1-2、31-4 |
| interview-05-resume-rules | 简历写法铁律与项目经验应答 | 31-1~31-4 |
| interview-06-pitfall-talk | 踩坑谈资合集（BUG 叙事） | 10-8、18-3、27-2~4 |

## 表述红线（写博客引用时注意）

- 工作流/沙箱/AI 节点内容来自**自研参考实现**（lowcode-platform），不是课程原始代码，引用要说清。
- 两套代码工程均无真正 RBAC 角色模型，别写"RBAC 权限体系"。
- 课程原版（B 工程）无工作流模块；参考实现（A）的 Redis 未实际使用。
- 事务化发布卡中"保留问卷数据"是参考实现修正，原课程实现会重置问卷数据。
