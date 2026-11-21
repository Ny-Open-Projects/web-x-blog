# 画面线理解：10.Freemarker基础-基础指令-其它指令

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\10.Freemarker基础-基础指令-其它指令【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 01:17, 02:06, 03:22, 04:14, 05:14, 06:09, 07:05, 08:46, 09:50, 11:12, 13:07, 14:42, 16:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:52:44

1) 这一组画面整体在讲什么（一句话）：
演示 FreeMarker 模板引擎中 if 指令的用法，以及如何通过数据模型和模板渲染生成 HTML 页面，并展示因数据模型中 key 不存在导致的模板错误及解决方案。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了 FreeMarker 基础指令章节中的“2.4 if指令”。
- 画面中显示了 if 指令的说明文字和一个包含 if 判断的模板代码片段。
- 代码片段：
  ```html
  <table>
  <tr>
  <td>姓名</td>
  <td>年龄</td>
  <td>钱包</td>
  </tr>
  <#list stus as stu>
  <tr>
  <td <if stu.name == "小明">style="background:red"</if> >${stu.name}</td>
  <td>${stu.age}</td>
  <td >${stu.mony}</td>
  </tr>
  </#list>
  ```

画面 2:
- 继续展示模板代码，光标位于 if 判断条件处。
- 画面下方文字说明：“通过阅读上面的代码，实现的功能是：如果姓名为“小明”则背景色显示为红色。”

画面 3:
- 展示了 IntelliJ IDEA 中的项目结构，选中了 `test.ftl` 模板文件。
- 代码编辑器中显示了模板代码，其中 `#list stus as stu` 部分被高亮。
- 项目结构中可见 `application.yml`、`Student.java`、`FreemarkerController.java` 等文件。

画面 4:
- 显示了 IntelliJ IDEA 中的“Run”菜单，用户点击了“Run ‘FreemarkerTestApplication’ with Coverage”。
- 画面右侧显示了“Watch Case”和“Page save Case”等选项。

画面 5:
- 展示了 `FreemarkerController.java` 文件中的代码，光标位于 `stul.setMoney(1000.86f);` 行。
- 画面下方的终端显示了 Java 运行时路径。

画面 6:
- 显示了 `test.ftl` 模板文件中的代码，光标位于 `#list stus as stu` 部分。
- 画面下方的终端显示了错误信息：“FIL stack trace (*** means nesting-related): - Failed at: ${stu.name} [in template 'test.ftl' at line 28, column 83]”。

画面 7:
- 展示了浏览器中显示的 HTML 页面，内容为“Hello world!”和学生信息。
- 画面下方的浏览器地址栏显示了“localhost:8088”。
- 画面下方的终端显示了错误信息：“FreeMarker template error (DEBUG mode use RETROW in production)”。

画面 8:
- 展示了 `FreemarkerController.java` 文件中的代码，光标位于 `model.put("stuMap", stuMap);` 行。
- 画面下方的终端显示了错误信息：“FIL stack trace (*** means nesting-related): - Failed at: ${stuMap["stu1"].name} [in template 'test.ftl' at line 28, column 4]”。

画面 9:
- 展示了 `FreemarkerController.java` 文件中的代码，光标位于 `return "test1";` 行。
- 画面下方的终端显示了错误信息：“FIL stack trace (*** means nesting-related): - Failed at: ${stuMap["stu1"].name} [in template 'test.ftl' at line 29, column 4]”。

画面 10:
- 展示了 `application.yml` 文件中的配置内容。
- 配置内容：
  ```yaml
  server:
    port: 8088 #服务端口
  spring:
    application:
      name: test-freemarker #设定服务名
    freemarker:
      charset: UTF-8
      content-type: text/html
      suffix: .ftl
      enabled: true
      template-loader-path: classpath:/templates/
      resources:
        add-mappings: false #关闭工程中默认请求处理
      allow-exception-if-no-handler-found: true #出现错误时能继续输出
  ```

画面 11:
- 展示了 `test.ftl` 模板文件中的代码，光标位于 `#list stuMap.keys as key` 部分。
- 画面下方的终端显示了错误信息：“FIL stack trace (*** means nesting-related): - Failed at: ${stuMap["stu1"].name} [in template 'test.ftl' at line 29, column 4]”。

画面 12:
- 展示了 `test.ftl` 模板文件中的代码，光标位于 `</table>` 部分。
- 画面下方的终端显示了日志信息：“2020-01-15 17:50:07.318 [http-nio-8088-exec-2] INFO o.s.web.servlet.DispatcherServlet - Completed initialization in 5 ms”。

画面 13:
- 展示了 `test.ftl` 模板文件中的代码，光标位于 `url请求地址：${requestUri}` 部分。
- 画面下方的终端显示了日志信息：“2020-01-15 17:50:07.318 [http-nio-8088-exec-2] INFO o.s.web.servlet.DispatcherServlet - Completed initialization in 5 ms”。

画面 14:
- 展示了 FreeMarker 基础指令章节中的“2.1 数据模型”。
- 画面中显示了数据模型的定义方法和代码示例。
- 代码示例：
  ```java
  @RequestMapping("/test1")
  public String freemarker(Map<String, Object> map){
      //内数据模型放数据
      map.put("name","world");
      Student stu1 = new Student();
      stu1.setName("小明");
      stu1.setAge(18);
      stu1.setMoney(1000.86f);
      Student stu2 = new Student();
      stu2.setName("小红");
      stu2.setMoney(200.1f);
      stu2.setAge(19);
  }
  ```
