# 10.ES6新特性之扩展运算符

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\10.ES6新特性之扩展运算符【海量资源尽在 666java.com】.mp4
- 时长 5分5秒（音频 305s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看扩展运算符在ES6中呢为我们提供了有扩展运算符的一个操作它呢是通过三个点做一个表示它的目的是将一个数组转为用逗号分割的这样的一个参数列表那我们先来看一下这个效果那么这个是什么意思呢可以这么来玩那么比如说我们现在直接来Cosm打印log来一个什么呢我们写一个数组
[00:29] 二三那么我们先来看一下这个数组打印的情况怎么样是不是就是一个数组一二三对吧那么我们其实可以直接在数组前面加三个点那么就代表着什么呢我们把这个数组要给它干嘛呢展开或者做一个扩展那么你可以看到最后打印的结果是不是就是一二三我们拿到这个里面的每一个这个值每一个这个值
[00:53] 那么这个呢是一种用法对不对那么我们还可以怎么用呢这样来用啊就是说你可以在前面啊再去加一些东西啊咱们把这个再拷一下吧然后呢这个我可以来个1然后呢然后来个0吧0然后后面来一个什么呢4来个5这个最后打印的效果是不是就是0到5啊
[01:16] 来看一下012345那么0是我们自己写的这个0那么123呢是不是就是从通过这个数组中把它展开的啊然后45就是我们写的这个值45好那么这是它的基本的一个用法下面我们来看一下它还有一些其他的用法那我们把这个例子我们靠过来来看一下它的是什么意思啊好那么我们把它靠到哪里呢靠到这个位置来看一下效果那么我们定义了一个function
[01:45] 然后呢他的return就是x加y然后呢现在我们假设有一个我们的一个数组numbers有1 2然后呢我们调用这个and方法由于and这个方法要求是有两个参数那我们可以直接通过一个三个点扩展预算符把我们的一个数组给它展开然后呢直接传递到这个and中我们来看效果那么他打印的结果是多少呢是不是就是3呢
[02:12] 就是3ok好这是这样的一个效果是不是就可以直接把素组展开然后作为一个参数传递到我们这个function中对吧这样的一个操作好那我们继续往下面看还有一种操作叫做素组的合并那这个是什么意思呢我们来看一下那么我们是不是有一个定义了一个素组定义了一个素组然后呢它呢是有什么呢有两个素组展开之后做一个合并之后的一个素组
[02:42] 那么是不是有一个123数组有个456这个数组我们把123和456分别展开然后呢形成一个新的一个数组得到一个ARR然后呢我们把它打印出来那么最终的结果那一定是什么呢是123456而且呢它本身呢又是一个什么数组哎OK好那么这是这样的一种用法那么下面我们来看一下它可以和结构表达式去做一个结合那么这个又是什么意思呢来看一下那么
[03:11] 假设我们现在我们定义了这样的一个定义了一个素组这样的一个结构表达式然后它所对应的就是后面的一个素组那么要注意的是那么这个fast那么它所对应的是我们的什么是不是就第一这个数字或者这个元素然后后面是点点点那么它所对应的注意它所对应的这些这个所对应的就是什么呢
[03:39] 对应的就是从2开始一直到5后面的这样的一个数据这个能够理解了吗好 那么咱们把它打印出来来看一下那么可以看到前面的fast那么显然就是什么呢1然后后面的是不是就是变成一个素组OK和结构表达是做一个结合那么还可以什么呢把这个正串转成一个素组那它用法还是比较多的我们来分别的去给大家演示一下
[04:09] 那么我们来看在这个位置我们是不是写了一个这个我们一个字符串hello然后呢我们可以把这个hello的字符串呢三个点操作然后我们就可以转成一个制服的这样的一个素组那么来看一下效果走那么是不是你可以看到是不是hello被转成这样的素组把一个字符串转成一个素组那么这个就是我们所讲的这个什么呢
[04:33] 扩展运算幅那么当大家以后看到有三个点这个操作的时候要想到这个是它的扩展运算幅它可以去对素组做扩展也可以做素组的合并也可以和结构表达师做结合也可以把这幅创转成一个素组它的操作是比较多的那么如果你现在记不住没关系等到你在使用的过程中发现有三个点就想到这是扩展运算幅回过头来再来看它的用法那么你就理解了
[05:01] 好那么关于这扩展运算服呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 ES6 的扩展运算符（...）的用法，包括数组合并、与解构赋值结合、将字符串转成数组等。

2) 按时间顺序列出每张画面的要点：
画面1：在 IntelliJ IDEA 中展示 index.html 文件，其中包含 ES6 的 reduce 方法示例代码。
画面2：在 IntelliJ IDEA 中，光标在 "const" 关键字上，下方弹出代码补全建议，包含 Console、confirm 等方法。
画面3：在浏览器开发者工具的 Console 面板中，显示了空的控制台。
画面4：在浏览器开发者工具的 Console 面板中，显示了数组 [1, 2, 3, 4, 5] 的输出。
画面5：在 IntelliJ IDEA 中，代码编辑器显示了 console.log([...1,2,3]) 的代码。
画面6：在 IntelliJ IDEA 中，代码编辑器显示了 console.log([...1,2,3]) 的代码，同时弹出一个 PPT 页面，标题为“ES6特性学习 - Google Chrome”，下方有多个软件图标。
画面7：在 Typora 中打开的 day01-ReactJS\J.md 文件，显示了“1.6. 扩展运算符”章节，其中包含扩展运算符的用法和示例代码。
画面8：在 IntelliJ IDEA 中，代码编辑器显示了 function add(x, y) { return x + y; } 的代码。
画面9：在 Typora 中打开的 day01-ReactJS\J.md 文件，显示了“1.6. 扩展运算符”章节，其中包含扩展运算符的用法和示例代码。
画面10：在 IntelliJ IDEA 中，代码编辑器显示了 let arr = [...[1,2,3],...[4,5,6]] 的代码。
画面11：在 IntelliJ IDEA 中，代码编辑器显示了 const [first, ...rest] = [1, 2, 3, 4, 5]; 的代码。
画面12：在浏览器开发者工具的 Console 面板中，显示了数组 [1, 2, 3, 4, 5] 的输出。
画面13：在 IntelliJ IDEA 中，代码编辑器显示了 console.log([...‘hello’]) 的代码。
画面14：在 Typora 中打开的 day01-ReactJS\J.md 文件，显示了“1.6. 扩展运算符”章节，其中包含扩展运算符的用法和示例代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ES6新特性学习</title>
</head>
<body>
<script>
const arr = [1,20,-5,3];
let result = arr.reduce((a, b) => {
return a + b;
}, 1);
console.log(result);
</script>
</body>
</html>
```

画面5：
```javascript
console.log([...1,2,3]);
```

画面8：
```javascript
function add(x, y) {
return x + y;
}
var numbers = [1, 2];
console.log(add(...numbers)); // 3
```

画面10：
```javascript
// 数组合并
let arr = [...[1,2,3],...[4,5,6]];
console.log(arr); // [1, 2, 3, 4, 5, 6]
```

画面11：
```javascript
// 与解构赋值结合
const [first, ...rest] = [1, 2, 3, 4, 5];
console.log(first, rest) // [2, 3, 4, 5]
```

画面13：
```javascript
// 将字符串转成数组
console.log([...‘hello’]) // ["h", "e", "l", "l", "o"]
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面6：PPT 标题为“ES6特性学习 - Google Chrome”，下方有多个软件图标，包括 IntelliJ IDEA、Chrome、Node.js、Git、VS Code、Docker、MySQL、Redis、MongoDB、Nginx、Kubernetes、Docker Compose、Yarn、Webpack、Babel、ESLint、Prettier、Jest、Mocha、Chai、Cypress、Selenium、Playwright、Puppeteer、Curl、Postman、Swagger、GraphQL、REST、gRPC、Kafka、RabbitMQ、Redis、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、CockroachDB、PostgreSQL、MySQL、SQLite、Oracle、SQL Server、MongoDB、Cassandra、Cockroach

