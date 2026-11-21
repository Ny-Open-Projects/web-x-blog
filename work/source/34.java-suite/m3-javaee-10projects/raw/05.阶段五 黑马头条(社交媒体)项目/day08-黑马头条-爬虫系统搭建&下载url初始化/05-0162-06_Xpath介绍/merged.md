# 06_Xpath介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\06_Xpath介绍【海量资源尽在 666java.com】.mp4
- 时长 6分17秒（音频 377s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们要去讲一下爬虫里边涉及到的X-pass那X-pass是啥呢来看一下它是一种在X-Mile中查找信息的语言普遍应用于X-Mile但是当然了咱们也可以在HTML中也可以使用也可以使用咱们本项目用的就是X-Mile去查找一些元素特别是解析HTML内容的时候咱们主要用的是它去定位
[00:28] 会快速定位某一个信息来获取咱们的想要的内容好吧那这里边也说了说Clinium自动化中其核心作用是这个Clinium自动化脚本的这个基础啊咱们主要是用它去解析一些内容下面呢怎么去用呢咱们这里边也去简单去介绍了一下啊它主要是分着这么些东西第一个就是什么呢路径定位标签定位轴定位等组合结构
[00:53] 构成当然他也可以筛选可以去筛选进行辅助咱们一会回去再去介绍好吧咱们先来看第一个标签定位标签定位的话呢你看比较简单啊说你如果说是DIB这时候你找到所有的DIB标签元素如果input的话呢就是找到所有的input标签元素新呢就是找到任意你可以用at属性名找到指定名称的属性
[01:19] 指定名称的属性啊这就是标签定位然后下面这个呢用的会比较多一些就是叫路径定位路径定位里边你看一看一下首先是个杠咱们先要了解这东西啊杠就是从跟路径开始跟路径开始啊其他位置表示子元素或者分割符然后下面是表示后代元素后代元素然后点点呢表示负元素就是上一集点就是表示当前元素这个
[01:47] 这个或也就是数杠表示多条路径有可能是有两个路径去同时查找下面有些例子咱们可以再简单看一下首先是杠HML杠杠DIV这是啥意思这是首先杠HML就是根元素的HML杠杠DIV也是所有的DIV元素因为它这个第一个杠是啥呢第一个杠的话就是根第二个杠的话就是它要去找到你看这
[02:12] 表示后代元素后代元素啊但是你也可以在前面去加一些属性啊咱们也可以去这么找啊然后再往下看啊说你这个啊杠杠dab下面有一个呃属性id等于ide找到什么呢dab中有id等于1说错了啊有个dab标签啊它的属性是idid等于1并且呢找到它下面所有的死判所有的死判看到了吗找到
[02:38] ID等于ID1的dmi元素的子元素死盘就是找死盘好吧然后这个跟这个唯一一个区别就是加了一个杠是吧这是找到所有后代的死盘后代的死盘它两个级别是不一样的然后再往下是有一个classadd class的意思就是找到什么class属性是吧你看这有一个这个杠的意思刚才说了就是有两条路径第一条路径是它第二条路径是它是吧也就是分别去找到
[03:07] ID1和ID2下面的是什么同级别的死盘子元素死盘子元素死盘行下面还有一些轴定位轴定位的话就是能够更精确的去查找你的元素更精确怎么可以看一下首先你看这个这里边这里边是有两个东西说通过轴定位轴运算幅加上两个冒号或和标签和标签
[03:32] 找到需要的元素类似于路径领域其实跟上面差不多首先来看第一个DIV ID等于Children其实这是一个关键字说死判这意思其实跟上面是一样的也是找到所有的DIV下面的ID等于1的死判标签下面这个是找到属性class这个的意思就是说
[04:00] 而且在它之前的所有元素在它之前的所有元素下面其实都有一些定义比如说你看这块获取当前节点之前的所有同级节点是吧当然还有些其他的比如说咱们找一个 attribute这是什么属性是吧trodden是自由元素下面还有parent是副节点self这个就是当前节点
[04:23] 好吧咱们用到的时候呢咱们可以再去说大家呢也可以去详细去看一看首先呢先有一个印象最重要好吧然后下面啊下面的话其实咱们用到最多的呢其实还是下面这些组合的去筛选去筛选啊你看啊属性筛选呢其实这个咱们用的也会多因为一般的html啊特别是页面上的html它是会比较复杂的这时候呢你要通过当前的s pass去定位是比较重要的啊
[04:53] 首先是有一个属性名前加什么爱他来表示属性你看当前的什么爱他这就是属性是吧class等于一的DIB中class等于一class一这时候呢就能去找到当前的DIB好吧当前如果说你要是找到一些什么这种什么属性值是吧孩子属性值大于十的DIB也可以去找到是吧像这些都是类似标签大家可以看一看好吧
[05:19] 下面还有一些序号这个序号的话大家作为了解就可以比如说-1-1的话就是找到当前DIV中下面的是什么子元素有一个第一个这是第一个你说是4的话那就是第4个如果说当前这个序号如果说没有DIV的话那这个东西可能是无效的如果说你那边一共是5个但你要设置个6那这时候它就是无效的下面还有一个last这是最后一个是吧但是你也可以设置一个范围
[05:49] 是这个范围你看这里边去找到什么ID等于ID1的DAB元素后代的第3456个你看这是大于吗大于2小于7不就是3456吗是吧行下面还有一些例子大家可以看一看这个其实就是咱们的什么咱们的这个S pass这个比较重要大家也可以去看一看咱们用到的时候咱们还会再去说好吧再去说行那这个咱们就讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

