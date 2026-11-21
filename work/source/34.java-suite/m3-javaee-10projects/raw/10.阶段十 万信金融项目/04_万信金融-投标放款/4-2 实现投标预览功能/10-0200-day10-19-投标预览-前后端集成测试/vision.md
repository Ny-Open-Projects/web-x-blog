# 画面线理解：day10-19-投标预览-前后端集成测试

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-19-投标预览-前后端集成测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:38, 00:52, 01:22, 02:04, 02:09, 02:16, 02:40, 03:14, 03:29, 03:57, 04:09, 04:36, 04:55, 05:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:28:46

1) 这一组画面整体在讲一个金融项目前端页面与后端服务、数据库及搜索引擎的联动开发与调试过程。

2) 按时间顺序列出每张画面的要点：

画面1：
- 显示 Vue.js 项目结构，当前编辑的是 `main.vue` 文件。
- 代码片段：`getListData(){ const (pageNo, pageSize) - this this.request({ url: 'transaction/projects/indexes/q?pageNo=$pageNo&pageSize=$pageSize', method: 'POST', params: { pageNo, pageSize, // ... } }) }`

画面2：
- 显示 IntelliJ IDEA 中的 Java 代码，文件为 `ProjectIndexServiceImpl.java`。
- 代码片段：`projectDTO.setPeriod(period); projectDTO.setName(name); projectDTO.setDescription(description); projectDTO.setId(Long.parseLong(loanRecordMap.get("id").toString()); list.add(projectDTO); } catch (Exception e) { return null; }`

画面3：
- 显示一个 PPT 页面，标题为“万信金融-投标管理”。
- 内容：展示投标标的列表，包含“10、”、“2900元”、“360天”、“出借”等信息。

画面4：
- 显示 IntelliJ IDEA 的终端窗口，输出大量日志信息。
- 日志内容：`[main] [INFO] [NettyClientSelector_1] [NioEventLoopGroup] [1] - closeChannel: close the connection`。

画面5：
- 显示 IntelliJ IDEA 的终端窗口，输出 Spring Boot 启动日志。
- 日志内容：`[main] [INFO] [NettyClientSelector_1] [NioEventLoopGroup] [1] - closeChannel: close the connection`。

画面6：
- 显示 IntelliJ IDEA 中的 Java 代码，文件为 `ProjectIndexServiceImpl.java`。
- 代码片段：`projectDTO.setPeriod(period); projectDTO.setName(name); projectDTO.setDescription(description); projectDTO.setId(Long.parseLong(loanRecordMap.get("id").toString()); list.add(projectDTO); } catch (Exception e) { return null; }`

画面7：
- 显示 SQLyog 数据库管理工具，连接到 `localhost:3306`。
- 数据库表：`yq_consumer`，显示多条记录，包含 `USER_ID`、`USER_TYPE`、`HOLD`、`AUTH_LIST`、`BID_CARD`、`TOTAL_AMOUNT`、`STATUS`、`REQUEST_ID` 等字段。

画面8：
- 显示浏览器中访问的登录页面，地址为 `http://localhost:8081/user/login`。
- 页面内容：显示“万信金融”Logo，下方有“登录”按钮。

画面9：
- 显示浏览器中访问的前端页面，地址为 `http://localhost:8081/#/pages/end/main`。
- 页面内容：显示“正在加载...”，右侧为网络请求监控面板。

画面10：
- 显示浏览器中访问的 Elasticsearch 管理页面，地址为 `http://localhost:9200`。
- 页面内容：显示索引 `wansing2p_project_doc` 的数据，包含 `score`、`name`、`annualrate`、`amount`、`period`、`@version`、`consumerId` 等字段。

画面11：
- 显示浏览器中访问的前端页面，地址为 `http://localhost:8081/#/pages/end/main`。
- 页面内容：显示多个投资标的，包含“0%”、“360天”、“出借”等信息。

画面12：
- 显示浏览器中访问的前端页面，地址为 `http://localhost:8081/#/pages/details/213948364380390657`。
- 页面内容：显示“借款详情”，包含“NaN%”、“风险等级B”、“总额：12000”、“剩余金额：3000”等信息。

画面13：
- 显示 SQLyog 数据库管理工具，连接到 `localhost:3306`。
- 数据库表：`yq_transaction`，显示多条记录，包含 `ID`、`USER_ID`、`USER_TYPE`、`HOLD`、`AUTH_LIST`、`BID_CARD`、`TOTAL_AMOUNT`、`STATUS`、`REQUEST_ID` 等字段。

画面14：
- 显示浏览器中访问的前端页面，地址为 `http://localhost:8081/#/pages/details/213948364380390657`。
- 页面内容：显示“借款详情”，包含“10%”、“风险等级B”、“总额：12000”、“剩余金额：3000”等信息。

3) 无。

4) 无。

5) 无。
