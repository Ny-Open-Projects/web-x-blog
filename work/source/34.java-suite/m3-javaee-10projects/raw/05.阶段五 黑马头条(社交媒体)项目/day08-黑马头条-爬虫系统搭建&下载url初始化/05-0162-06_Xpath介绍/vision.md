# 画面线理解：06_Xpath介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\06_Xpath介绍【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:00, 02:21, 03:13, 03:23, 03:37, 04:09, 04:25, 04:32, 04:40, 05:23, 06:08, 06:12, 06:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:32:17

1) 这一组画面整体在讲什么（一句话）：
讲解 XPath 语法，包括标签定位、路径定位、轴定位和筛选条件等核心概念。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：介绍 XPath 是一种在 XML 中查找信息的语言，常用于 HTML，是 Selenium 自动化的核心基础。
画面2：介绍 XPath 定位主要由标签定位、属性定位、轴定位组合构成，外加筛选功能辅助。
画面3：展示标签定位示例，包括 div、input、* 和 @属性名 的 XPath 表达式。
画面4：展示路径定位示例，包括 /html、/div、//div[@id='id1']/span 等 XPath 表达式。
画面5：展示轴定位概念，包括 ancestor、ancestor-or-self、attribute、child、descendant、descendant-or-self、following、namespace、parent、preceding、preceding-sibling、following-sibling、Self 等轴名称及其作用。
画面6：展示轴定位示例，包括 ancestor、ancestor-or-self、attribute、child、descendant、descendant-or-self、following、namespace、parent、preceding、preceding-sibling、following-sibling、Self 等轴名称及其作用。
画面7：展示轴定位示例，包括 ancestor、ancestor-or-self、attribute、child、descendant、descendant-or-self、following、namespace、parent、preceding、preceding-sibling、following-sibling、Self 等轴名称及其作用。
画面8：展示轴定位示例，包括 ancestor、ancestor-or-self、attribute、child、descendant、descendant-or-self、following、namespace、parent、preceding、preceding-sibling、following-sibling、Self 等轴名称及其作用。
画面9：介绍筛选条件，包括属性筛选和文本筛选。
画面10：展示属性筛选示例，包括 //div[@class='class1']、//div[@height>10]、//div[contains(text(),'text')]、//div[contains(text(),'text1') and @class='class1']、//div[text()='text1'] and not(@class)。
画面11：展示序号筛选示例，包括 //div[@id='id1']/span[1]、//div[@id='id1']/span[last()]、//div[@id='id1']/span[position()>2 and position()<7]、//div[@id='id1']/text()[2]。
画面12：展示序号筛选示例，包括 //div[@id='id1']/span[1]、//div[@id='id1']/span[last()]、//div[@id='id1']/span[position()>2 and position()<7]、//div[@id='id1']/text()[2]。
画面13：展示筛选条件示例，包括 //div[@class='class1']、//div[@height>10]、//div[contains(text(),'text')]、//div[contains(text(),'text1') and @class='class1']、//div[text()='text1'] and not(@class)。
画面14：展示轴定位示例，包括 ancestor、ancestor-or-self、attribute、child、descendant、descendant-or-self、following、namespace、parent、preceding、preceding-sibling、following-sibling、Self 等轴名称及其作用。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
xpath是一种在xml中查找信息的语言，普遍应用于xml中，在装xml的html中也可以使用，在selenium自动化中起核心作用，是写selenium自动化脚本的基础。
```
画面2：
```
xpath的定位主要由标签定位、标签定位、轴定位组合构成，外加筛选功能进行辅助，几乎可以定位到任意元素
```
画面3：
```
xpath 说明
div 找到所有的div标签元素
input 找到所有的Input标签元素
*  定位任意元素或属性
@属性名  找到指定名称的属性
```
画面4：
```
xpath 说明
/html 找到根元素html
/div 找到所有的div元素
//div[@id='id1']/span 找到id="id1"的div元素的子元素span
//div[@id='id1']/span 找到id="id1"的div元素下的所有后代元素span
//div[@id='id1']/@class 找到id="id1"的div元素的class属性
//div[@id='id1']/span//div[@id='id2']/span 找到id="id1"和id="id2"的div元素的子元素span
```
画面5：
```
轴名称 结果
ancestor 选取当前节点的所有先辈（父、祖父等）
ancestor-or-self 选取当前节点的所有先辈（父、祖父等）以及当前节点本身
attribute 选取当前节点的所有属性
child 选取当前节点的所有子元素
descendant 选取当前节点的所有后代元素（子、孙等）。
descendant-or-self 选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
following 选取文档中当前节点的结束标签之后的所有节点。
namespace 选取当前节点的所有命名空间节点
parent 选取当前节点的父节点。
preceding 选取文档中当前节点的开始标签之前的所有节点。
preceding-sibling 选取当前节点之前的所有同级节点。
following-sibling 选取当前节点之后的所有同级节点。
Self 选取当前节点
```
画面6：
```
轴名称 结果
ancestor 选取当前节点的所有先辈（父、祖父等）
ancestor-or-self 选取当前节点的所有先辈（父、祖父等）以及当前节点本身
attribute 选取当前节点的所有属性
child 选取当前节点的所有子元素
descendant 选取当前节点的所有后代元素（子、孙等）。
descendant-or-self 选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
following 选取文档中当前节点的结束标签之后的所有节点。
namespace 选取当前节点的所有命名空间节点
parent 选取当前节点的父节点。
preceding 选取文档中当前节点的开始标签之前的所有节点。
preceding-sibling 选取当前节点之前的所有同级节点。
following-sibling 选取当前节点之后的所有同级节点。
Self 选取当前节点
```
画面7：
```
轴名称 结果
ancestor 选取当前节点的所有先辈（父、祖父等）
ancestor-or-self 选取当前节点的所有先辈（父、祖父等）以及当前节点本身
attribute 选取当前节点的所有属性
child 选取当前节点的所有子元素
descendant 选取当前节点的所有后代元素（子、孙等）。
descendant-or-self 选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
following 选取文档中当前节点的结束标签之后的所有节点。
namespace 选取当前节点的所有命名空间节点
parent 选取当前节点的父节点。
preceding 选取文档中当前节点的开始标签之前的所有节点。
preceding-sibling 选取当前节点之前的所有同级节点。
following-sibling 选取当前节点之后的所有同级节点。
Self 选取当前节点
```
画面8：
```
轴名称 结果
ancestor 选取当前节点的所有先辈（父、祖父等）
ancestor-or-self 选取当前节点的所有先辈（父、祖父等）以及当前节点本身
attribute 选取当前节点的所有属性
child 选取当前节点的所有子元素
descendant 选取当前节点的所有后代元素（子、孙等）。
descendant-or-self 选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
following 选取文档中当前节点的结束标签之后的所有节点。
namespace 选取当前节点的所有命名空间节点
parent 选取当前节点的父节点。
preceding 选取文档中当前节点的开始标签之前的所有节点。
preceding-sibling 选取当前节点之前的所有同级节点。
following-sibling 选取当前节点之后的所有同级节点。
Self 选取当前节点
```
画面9：
```
一般情况下，我们使用简写的语法。虽然完整的轴描述是一种更加贴近人类语言，利用自然语言的单词和语法来书写的描述方式，但是相比之下也更加啰嗦。
```
画面10：
```
xpath 说明
//div[@class='class1']  筛选class属性等于class1的div
//div[@height>10]  筛选height属性值大于10的div(仅限数字)
//div[contains(text(),'text')]  筛选文本中包含text的div
//div[contains(text(),'text1') and @class='class1']  同时满足两个条件的筛选，类似的“或者”的“or”运算符先离散的用“()”括起来
//div[text()='text1'] and not(@class)  筛选文本包含text1，且无class属性的 div
```
画面11：
```
xpath 说明
//div[@id='id1']/span[1]  找到id="id1"的div元素后代的第一个span元素，如[1]则是第4个
//div[@id='id1']/span[last()]  找到id="id1"的div元素子的
