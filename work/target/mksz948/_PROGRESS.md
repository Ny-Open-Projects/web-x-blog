# SpringAI 博客生产进度表 (mksz948)

> 源机翻: `source/17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）`；代码/资料源: `done/17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/code/unzip-target/springai-mcp-rag-dev`
> 代码状态: 已解压2567文件(32 Java+86 TS+前端)；排除 model.onnx(90MB模型非代码)
> 状态: pending=待产 / done=已完成 / partial=部分完成。串行推进，防 429。

| 状态 | 单元 | 源目录 | 备注 |
|---|---|---|---|
| done | 第10章 基于MCP的大模型与数据库交互开发 | 17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/第10章 基于MCP的大模型与数据库交互开发 | 6 篇机翻 → 2 张卡片 `10-1/10-2`（合计 28.1KB / 0.36x；MyBatis-Plus 集成(坐标冲突排除/yml 5506/IDTYPE/BaseResultMap/@MapperScan)+创建商品 MCP(BeanUtils/RandomStringUtils/insert)+删除(事务+QueryWrapper 按 product_id 非 deleteById 主键坑)+枚举映射 PriceCompareEnum(9项)/ListSortEnum+条件查询组装(gt/lt/ge/le/like/orderBy)+修改 MCP(update+setUpdateTime)；覆盖优先，质量强扩展，最大坑已写入卡片） |
| done | 第11章 云服务器部署与项目上线全流程指南 | 17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/第11章 云服务器部署与项目上线全流程指南 | 11 篇机翻 → 5 张卡片 `11-1~11-5`（合计 37.3KB / 0.42x；腾讯云采购(香港/按量/2核4G/CentOS7.9/安全组/关机不收费)+SSH(Electerm/SecureCRT)+OpenJDK21(profile/source)+Docker-ce(enable/重启验证)+MySQL8(5506/Navicat迁表)+Redis Stack(9379)+SearXNG(6080)+prod配置(内网IP/密码/cors/删filesystem)+Maven打包nohup发布+Nginx-1.28.0编译安装+前端发布联调；覆盖优先，质量强扩展，安全加固(改默认端口/强密码/最小开放)贯穿全章） |
| done | 第12章 多平台集成MCP服务与智能体应用 | 17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/第12章 多平台集成MCP服务与智能体应用 | 5 篇机翻 → 3 张卡片 `12-1~12-3`（合计 22.5KB / 0.44x；Cursor集成(删示例+spring-ai-sse+安全组488/489+查/改/发邮件)+CherryStudio(装uv/bun+SSE类型+实测)+Dify私有部署(Mac/Win,Docker+git+.env+docker compose up -d+Ollama host.docker.internal:11434)+Dify工作流(chatflow+react策略Agent+SSE MCP+sys.query+记忆+查商品HTML发邮件)；覆盖优先，质量强扩展，全栈打通收官） |
| done | 第13章 LLM大模型智能引擎实战--课程总结 | 17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/第13章 LLM大模型智能引擎实战--课程总结 | 1 篇机翻 → `13-1_LLM大模型智能引擎实战课程总结.md`（12.1KB / 3.01x ✅ 已清 3x） |
| done | 第1章 LLM大模型智能引擎实战--课程导学 | 17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/第1章 LLM大模型智能引擎实战--课程导学 | 1 篇机翻 → `1-1_LLM大模型智能引擎实战课程导学.md`（19.4KB / 2.23x ✅ 超 2x） |
| done | 第2章 初识SpringAI 项目功能与架构全解析 | 17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/第2章 初识SpringAI 项目功能与架构全解析 | 2 篇机翻 → 1 篇博客卡片 `2-1_初识SpringAI项目功能与架构全解析.md`（44.8KB / 3.03x，关联 14 个真实代码文件） |
| done | 第3章 配置高效开发环境 | 17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/第3章 配置高效开发环境 | 7 篇机翻 → 2 张卡片 `3-1/3-2`（合计 70.3KB / 1.48x；环境配置类章节，内容已涵盖 JDK21/Maven/IDEA/MySQL8/Docker/Navicat/内网互通/排错全链路，env-bounded，超额扩展） |
| done | 第4章 SpringBoot3 快速入门与配置管理 | 17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/第4章 SpringBoot3 快速入门与配置管理 | 4 篇机翻 → 4 张卡片 `4-1/4-2/4-3/4-4`（合计 58.5KB / 2.00x ✅ 已清 2x；代码为主章节） |
| done | 第5章 大模型集成与高阶功能开发 | 17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/第5章 大模型集成与高阶功能开发 | 6 篇机翻 → 2 张卡片 `5-1/5-2`（合计 38.5KB / 0.61x；含 DeepSeek 同步+流式+提示词三类+AOP 计时+StopWatch+.env 外置+通义千问集成+进阶 API/结构化输出/多轮/Ollama/配置中心；质量为强扩展，章节覆盖率优先） |
| done | 第6章 SSE实时通信与前端联调实战 | 17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/第6章 SSE实时通信与前端联调实战 | 8 篇机翻 → 2 张卡片 `6-1/6-2`（合计 30.1KB / 0.37x；SSE 原理+SseEmitter 服务端+客户端+发送+CORS+群发+前后端流式联调+MD转HTML；覆盖优先，质量强扩展） |
| done | 第7章 构建高效的RAG知识库系统功能 | 17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/第7章 构建高效的RAG知识库系统功能 | 7 篇机翻 → 2 张卡片 `7-1/7-2`（合计 35.7KB / 0.56x；RAG 原理+Redis Stack 安装+项目集成+上传读取+CustomTextSplitter 切分+向量库存储+similaritySearch 检索+大模型 RAG Prompt 合成；覆盖优先，质量强扩展） |
| done | 第8章 SearXNG 联网搜索集成实战 | 17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/第8章 SearXNG 联网搜索集成实战 | 7 篇机翻 → 2 张卡片 `8-1/8-2`（合计 27.1KB / 0.42x；联网搜索原理+SearXNG Docker安装+项目集成+OkHttpConfig+URL构建+body.string解析坑+SearXNGResponse+dealResults排序截断+SearchGptPrompt大模型合成；覆盖优先，质量强扩展） |
| done | 第9章 深入理解与实践MCP服务 | 17.mksz948-LLM大模型智能引擎实战--SpringAI+RAG+MCP+实时搜索（13章完结）/第9章 深入理解与实践MCP服务 | 14 篇机翻 → 3 张卡片 `9-1/9-2/9-3`（合计 37.9KB / 0.31x；MCP概念/场景/通信机制/平台/Cursor本地远程集成+SpringAI接STDIO/SSE+首个DateTool+自动编排+邮件MCP实战配置/发送/MD转HTML/记忆/类型匹配；覆盖优先，质量强扩展，最大章拆 3 卡） |

## 关联 manifest
- 见同目录 `manifest.json`（章节→机翻→代码/资料 关联，随博客产出回填 code_artifacts / blog_cards）