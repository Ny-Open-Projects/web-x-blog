# 15.ES6新特性之修饰器

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\15.ES6新特性之修饰器【海量资源尽在 666java.com】.mp4
- 时长 5分3秒（音频 303s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下这个修饰器啊叫Dictator那么它呢本身呢是一个函数用来呢去修改类似的行为这个呢是非常相似于我们Java中的什么呢注解它呢是在ES2017这个版本中呢去加入了这项功能那么目前呢这个Babel这个转码器呢已经对它做了一个支持好,那我们下面来看一下怎么用啊怎么用
[00:29] 然后呢我们把这个删掉来看一下那么我现在有一个类啊叫Ura这个类然后呢我们给他去设置一个他的构造函数这个我们并不陌生刚刚我们讲过Name再来一个叫什么Age等于什么呢20这是他的一个默认值Race.NameRace.什么呢Name等于Name然后呢Race.Age等于什么呢Age
[00:59] 好那么我们这样的话就已经写完一个类了对不对那么这个我们是比较熟悉的那么大家回想一下在我们的加号中如何给类去添加一个注解呢通过什么符号呢没错通过什么按的符号那么按的符号什么呢我们来看一下按的符号
[01:17] 通过一个t,按着符号t,当然这个t是什么呢当然你这个不一定是t也可以是其他的一些符号或者是一些单词都是可以的那么我们给它按着t那么我们就需要在下面什么呢我们定义一个function, function什么呢t function
[01:38] 这个大家能够理解了吗刚才说过其实这个修饰器本身就是一个函数就是一个函数你看就这样的一个函数那么这个function那么它在什么时候去执行呢它是在执行我们这个代码的时候执行我们这个类代码的时候先去执行我们这个t这个方法那我们来看一下在这个t中它会接收一个参数叫什么target
[02:04] 那么这个target的什么意思呢是指我们被修饰的这个对象被修对象反而呢在这就是我们那个user所以我们加一个作者这个target是指什么呢被修饰的一个对象好那么我们来看一下我能不能够把它打印出来呢当然是可以的log打印一下好打印一下好那么我们
[02:33] 前面我们说过我们可以通过什么的这个修制器来修改类的这个行为对吧来修改这个类的行为那么我们来看一下那么怎么样去修改呢我们可以通过这个target点那么我们这个类似优惠我可以给他加一个什么的加一个国家对吧加个国家这个属性啊country而外啊等于什么呢等于叫中国啊中国那么注意
[03:02] 通过我们这个修饰器通过修饰器修饰器添加的属性是什么呢是静态属性静态属性那么也就是说我们通过这个类是不是直接就可以去打印出来那么来看一下点log能不能拿到呢来一个优热点什么的country那么能不能打印出这个中国呢来看效果来刷新
[03:33] 走非常遗憾非常遗憾那么并没有打印出这个中国那么这个是什么意思呢是指什么呢我们这样的写法他当前浏览器并不识别并不识别那么这个怎么办那么难道这种用法就不能使用呢并不是他的需要通过一些转码器进行转码之后才能够去做一个运行那么来看一下原因是
[04:02] 在我们当前的ES6中并没有这个方法并没有得到支持在2017中才有所以我不能直接运行我们就需要进行转码之后再运行转码的意思就是什么意思就是将ES2017要转成ES5再做执行类似于是这样的比如说我们转码前是这样的一种写法对吧转码之后是这样的一种写法它把箭头函数
[04:31] 转成了我们普通的一种函数那么OK关于这个转码器怎么用我们到下一节我们再讲那么我们这一节呢我们先要掌握的是这个修饰器的一种这种用法虽然最终的这个结果我们没有测试出来但是这种用法先希望大家能够去掌握那么下面我们去学习这个转码器之后我们再来验证它的一个结果
[04:59] 好,那么关于这个修饰器我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 ES6 的类（class）语法和装饰器（Decorator）的使用，以及在浏览器中运行时的兼容性问题。

2) 按时间顺序列出每张画面的要点：
画面1：在 IntelliJ IDEA 中编辑 index.html 文件，展示 ES6 类的构造函数语法，包含参数默认值和属性赋值。
画面2：在 IDE 中，光标位于 class User { 后，显示了代码补全建议，包括 ngd1、ngd2 等 Angular 指令。
画面3：在 IDE 中，光标位于 class User { 后，显示了 constructor 的方法属性补全列表，如 hasOwnProperty、isPrototypeOf 等。
画面4：在 IDE 中，光标位于 function 后，准备编写函数。
画面5：在 IDE 中，选中了 class User 的构造函数部分，高亮显示。
画面6：在 IDE 中，光标位于 function 后，准备编写函数体。
画面7：在 Typora 中打开 day01-React15A\J.md 文档，显示“1.1.1. 修饰器(Decorator)”章节，介绍装饰器是 ES2017 引入的功能，Babel 已支持。
画面8：在 IDE 中，光标位于 function T(target) { 后，准备编写装饰器逻辑。
画面9：在 IDE 中，光标位于 function T(target) { 后，显示了 console 对象的补全列表。
画面10：在浏览器中打开 index.html，显示了 console.log 输出的 "hello"、"world"、"abc"。
画面11：在 IDE 中，光标位于 function T(target) { 后，编写了 target.country = "中国" 并调用 console.log(User.country)。
画面12：在 Typora 中，显示“1.1.2. 转换器”章节，解释 Babel 是常用的 ES6 转换器，可以将 ES6 代码转为 ES5 代码。
画面13：在 Typora 中，显示“1.1.1. 修饰器(Decorator)”章节，展示代码示例和浏览器控制台报错信息。
画面14：在 Typora 中，显示“1.1.1. 修饰器(Decorator)”章节，展示代码示例和浏览器控制台报错信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ES6新特性的学习</title>
</head>
<body>
<script>
class User {
constructor(name, age = 20) {
this.name = name;
this.age = age;
}
}
function T(target) {
}
</script>
</body>
</html>
```

画面7：
```javascript
// 通过装饰器进行引用方法，类似java中的注解
class User {
constructor(name, age = 20) {
this.name = name;
this.age = age;
}
}
function T(target) { // 定义一个管理的方法
console.log(target); // target对象为被修饰的目标对象，这里是User对象
target.country = "中国"; // 为User类添加一个静态属性country
}
console.log(User.country); // 打印出country属性值
```

画面11：
```javascript
function T(target) { // target: 被修饰的对象
console.log(target);
target.country = "中国"; // 通过装饰器添加的属性是静态属性
console.log(User.country);
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面7：
标题：1.1.1. 修饰器(Decorator)
正文：修饰器(Decorator)是一个函数，用来修改类的行为。ES2017引入了这项功能。目前 Babel 转换器已经支持。
使用：
```javascript
// 通过装饰器进行引用方法，类似java中的注解
class User {
constructor(name, age = 20) {
this.name = name;
this.age = age;
}
}
function T(target) { // 定义一个管理的方法
console.log(target); // target对象为被修饰的目标对象，这里是User对象
target.country = "中国"; // 为User类添加一个静态属性country
}
console.log(User.country); // 打印出country属性值
```

画面12：
标题：1.1.2. 转换器
正文：Babel (babels.js) 是一个广为使用的 ES6 转换器，可以将 ES6 代码转为 ES5 代码，从而在浏览器或其他环境中执行。

5) 无。

