# 画面线理解：02.实现前端的mock服务

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\02.实现前端的mock服务【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:28, 02:18, 04:19, 05:37, 07:04, 08:15, 09:38, 10:41, 12:02, 13:17, 14:55, 16:37, 17:38, 18:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:18:49

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Spring Boot 构建一个 Mock 服务，为前端 React 应用提供模拟数据支持，包括配置、控制器编写和前端调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示前端 React 应用在 http://localhost:9000/home 的页面，显示“一线江景度假洋房”广告和多个功能图标。
画面 2: 展示 PDF 文档，标题为“1. 仿mock服务”，内容说明为前端系统提供 mock 服务，包括 GraphQL 查询列表、更新房源功能、Redis 缓存和 WebSocket 门。
画面 3: 展示 IntelliJ IDEA 中的 MockConfig.java 文件，代码内容为：
```java
package cn.itcast.haoke.dubbo.api.config;
import org.springframework.context.annotation.Configuration;
@Configuration
@PropertySource("classpath:mock-data.properties")
@Component
@ControllerAdvice (org.springframework.web.bind.annotation)
@ConfigurationProperties (org.springframework.context.boot.context.properties)
@Conditional (sun.misc)
@ConditionalOnBean (org.springframework.boot.autoconfigure.condition)
@ConditionalOnClass (org.springframework.boot.autoconfigure.condition)
@ConditionalOnEnabledResourceChain (org.springframework.boot.autoconfigure.condition)
@ConditionalOnExpression (org.springframework.boot.autoconfigure.condition)
```
画面 4: 展示 IntelliJ IDEA 中的 MockConfig.java 文件，代码内容为：
```java
class MockConfig {
    String indexMenu;
    String indexInfo;
    String indexFaq;
    String indexHouse;
    String indexList;
    String infosList1;
    String infosList2;
    String infosList3;
    String my;
```
画面 5: 展示 IntelliJ IDEA 中的 MockController.java 文件，代码内容为：
```java
import cn.itcast.haoke.dubbo.api.config.MockConfig;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
@RequestMapping("mock")
@RestController
public class MockController {
    @Autowired
    private MockConfig mockConfig;
    @GetMapping("indexMenu")
    public String indexMenu() {
        return this.mockConfig.getIndexMenu();
    }
```
画面 6: 展示 Advanced REST Client 中的请求页面，URL 为 http://127.0.0.1:18080/mock/indexMenu，状态为 200。
画面 7: 展示 IntelliJ IDEA 中的 MockController.java 文件，代码内容为：
```java
import org.springframework.web.bind.annotation.RestController;
public class MockController {
    @RequestMapping("mock")
    @RestController
    public class MockController {
        @Autowired
        private MockConfig mockConfig;
        @GetMapping("indexMenu")
        public String indexMenu() {
            return this.mockConfig.getIndexMenu();
        }
```
画面 8: 展示 PDF 文档，内容为 MockController.java 文件中的 infosList 方法，代码内容为：
```java
@GetMapping("infos/list")
public String infosList(@RequestParam("type") Integer type) {
    switch (type) {
        case 1:
            return this.mockConfig.getInfosList1();
        case 2:
            return this.mockConfig.getInfosList2();
        case 3:
            return this.mockConfig.getInfosList3();
    }
    return this.mockConfig.getInfosList1();
```
画面 9: 展示浏览器开发者工具 Network 面板，显示多个请求状态为 403，包括 /infos/list 和 /faq。
画面 10: 展示浏览器开发者工具 Network 面板，显示请求 /infos/list 的响应内容，包含“历史半年销售业绩突破中”等文本。
画面 11: 展示 IntelliJ IDEA 中的 find.js 文件，代码内容为：
```javascript
url: 'http://127.0.0.1:18080/mock/infos/list?type=2'
```
画面 12: 展示浏览器开发者工具 Network 面板，显示请求 /infos/list 的响应内容，包含“历史半年销售业绩突破中”等文本。
画面 13: 展示 IntelliJ IDEA 中的 my.js 文件，代码内容为：
```javascript
this.state = {
    uname: '',
    avatarPath: false,
    openAvatar: false,
    openImage: false,
    avatar: ''
};
componentWillMount = () => {
    axios.get('http://127.0.0.1:18080/mock/my/info', {
        user_id: localStorage.getItem('uid')
    }).then(ret => {
        this.setState({
            uname: ret.data.username,
            avatarPath: ret.data.avatar
        });
```
画面 14: 展示 PDF 文档，内容与画面 2 相同，标题为“1. 仿mock服务”，内容说明为前端系统提供 mock 服务，包括 GraphQL 查询列表、更新房源功能、Redis 缓存和 WebSocket 门。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 3:
```java
package cn.itcast.haoke.dubbo.api.config;
import org.springframework.context.annotation.Configuration;
@Configuration
@PropertySource("classpath:mock-data.properties")
@Component
@ControllerAdvice (org.springframework.web.bind.annotation)
@ConfigurationProperties (org.springframework.context.boot.context.properties)
@Conditional (sun.misc)
@ConditionalOnBean (org.springframework.boot.autoconfigure.condition)
@ConditionalOnClass (org.springframework.boot.autoconfigure.condition)
@ConditionalOnEnabledResourceChain (org.springframework.boot.autoconfigure.condition)
@ConditionalOnExpression (org.springframework.boot.autoconfigure.condition)
```
画面 4:
```java
class MockConfig {
    String indexMenu;
    String indexInfo;
    String indexFaq;
    String indexHouse;
    String indexList;
    String infosList1;
    String infosList2;
    String infosList3;
    String my;
```
画面 5:
```java
import cn.itcast.haoke.dubbo.api.config.MockConfig;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
@RequestMapping("mock")
@RestController
public class MockController {
    @Autowired
    private MockConfig mockConfig;
    @GetMapping("indexMenu")
    public String indexMenu() {
        return this.mockConfig.getIndexMenu();
    }
```
画面 8:
```java
@GetMapping("infos/list")
public String infosList(@RequestParam("type") Integer type) {
    switch (type) {
        case 1:
            return this.mockConfig.getInfosList1();
        case 2:
            return this.mockConfig.getInfosList2();
        case 3:
            return this.mockConfig.getInfosList3();
    }
    return this.mockConfig.getInfosList1();
```
画面 11:
```javascript
url: 'http://127.0.0.1:18080/mock/infos/list?type=2'
```
画面 13:
```javascript
this.state = {
    uname: '',
    avatarPath: false,
    openAvatar: false,
    openImage: false,
    avatar: ''
};
componentWillMount = () => {
    axios.get('http://127.0.0.1:18080/mock/my/info', {
        user_id: localStorage.getItem('uid')
    }).then(ret => {
        this.setState({
            uname: ret.data.username,
            avatarPath: ret.data.avatar
        });
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“1. 仿mock服务”，内容为：
- 为前端系统提供mock服务
- 前端系统中通过graphql查询房源列表
- 实现后台系统的更新房源功能
- 为接口服务添加Redis缓存
- WebSocket入门
画面 8: PPT 标题为“1. 仿mock服务”，内容为：
- 为前端系统提供mock服务
- 前端系统中通过graphql查询房源列表
- 实现后台系统的更新房源功能
- 为接口服务添加Redis缓存
- WebSocket入门
画面 14: PPT 标题为“1. 仿mock服务”，内容为：
- 为前端系统提供mock服务
- 前端系统中通过graphql查询房源列表
- 实现后台系统的更新房源功能
- 为接口服务添加Redis缓存
- WebSocket入门

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
