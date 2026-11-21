# 画面线理解：15.Elasticsearch快速入门之RESTful api（高亮显示）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\15.Elasticsearch快速入门之RESTful api（高亮显示）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:09, 00:11, 00:13, 00:15, 00:16, 00:18, 00:20, 00:48, 00:50, 01:22, 01:32, 01:39, 01:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:33:11

1) 这一组画面整体在讲什么（一句话）：
演示如何使用浏览器和开发者工具分析百度搜索结果页面的 HTML 结构和 CSS 样式，以理解前端渲染机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Adobe Reader 中查看 PDF 文档，内容为 Elasticsearch 的高亮显示（highlight）配置示例，页面显示“2.4.7、高亮显示”章节。
画面 2: 浏览器打开新标签页，地址栏为空。
画面 3: 浏览器访问百度首页（https://www.baidu.com），显示百度的节日主题页面。
画面 4: 在百度搜索框中输入“java”，并显示搜索建议。
画面 5: 百度搜索结果页面加载完成，显示多个关于“java”的搜索结果链接。
画面 6: 鼠标悬停在“Java 百度百科”链接上，页面未发生明显变化。
画面 7: 鼠标悬停在“download java - 下载免费的 Java 软件”链接上。
画面 8: 鼠标悬停在“Java SE Development Kit 8 - Downloads”链接上。
画面 9: 点击“Java SE Development Kit 8 - Downloads”链接，页面跳转至 Oracle 官网的 JDK 下载页面。
画面 10: 浏览器开发者工具（F12）打开，切换到“Elements”标签页，显示百度搜索结果页面的 HTML 结构。
画面 11: 在开发者工具中，鼠标悬停在“Java SE Development Kit 8 - Downloads”链接对应的 HTML 元素上，显示其 CSS 类名和样式。
画面 12: 在开发者工具中，鼠标悬停在“Java 教程 | 鸟哥教程”链接对应的 HTML 元素上，显示其 CSS 类名和样式。
画面 13: 返回 Adobe Reader，查看 PDF 文档的“2.4.7、高亮显示”章节，页面显示“2.4.7、高亮显示”章节。
画面 14: 在 Postman 中构造一个 POST 请求，发送到 http://172.16.55.185:9200/haoke/user_search，请求体为 JSON 格式，包含查询条件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```json
{
  "query": {
    "match": {
      "name": "张三 李四"
    }
  },
  "highlight": {
    "fields": {
      "name": {}
    }
  }
}
```

画面 13:
```json
{
  "query": {
    "match": {
      "name": "张三 李四"
    }
  },
  "highlight": {
    "fields": {
      "name": {}
    }
  }
}
```

画面 14:
```json
{
  "query": {
    "match": {
      "name": "张三 李四"
    }
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
