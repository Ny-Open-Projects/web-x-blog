# 13.ES6新特性之class类的基本语法

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\13.ES6新特性之class类的基本语法【海量资源尽在 666java.com】.mp4
- 时长 8分23秒（音频 503s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下这class类的一些基本的一些语法那么JavaScript呢它早期的定位呢是基于对象的并不是面向对象的所以它并没有提供这class的这种语法但是在ES6之后呢它引入了class的概念那么这个引入之后呢就变得我们使用这种class类变得更加的方便了那么
[00:26] 它的这种用法基本上和我们java中的类的这种用法差不多好那么下面我们就来看一下那么如何定义一个类呢通过关键字class定义一个user然后我们去写它内容同样它也有什么呢也有构造函数构造函数那么构造函数那么在构造函数中我们就可以给它设置一些值
[00:52] 比如说在这个位置设置一个name然后呢设置一个age当然了你也可以给他设置什么呢出设置默认值如果我们没有传递的话就采用这个什么默认值然后呢在这个位置叫做this.name等于什么呢namethis.什么呢age等于什么呢age好那么我们构造函数就搞定那么在我们的对象中呢他还可以有自己的一些这个方法
[01:22] 比如说有个叫什么的say什么的hello那么我们就把它呢就来实现一下return什么的return叫什么的hello逗号加一个什么的race.什么的name好那么就说谁你好啊你好谁好那么在我在这个class中呢还有一种函数叫什么呢叫静态函数
[01:51] 通过关键字啊叫静态啊静态函数通过关键字什么呢static你看和Java钟是吧非常的相像啊static一个函数那么叫什么函数呢比如说我们有个叫什么判断啊判断这个呃判断年龄啊你传递一个年龄给他然后呢我们去做一个这个判断if如果你的年龄大于等于18岁的话
[02:20] 那我们就给你return什么呢你是成年人那如果elseelse的话当然不写else也可以对吧好那咱们就直接return吧return什么呢叫未成年人对吧小于18岁就是未成年人未成年人好那么接下来我们来看这个lay怎么去用那么我们定义let来一个url等于注意是new一个什么呢url
[02:52] Nu一个这个对象那么当我们去Nu的时候呢你要去传递构造函数构造函数两个参数那么我们第一个参数Name你是必须要传递的第二个参数呢是可以不用传递也可以传递如果不传递呢就是20如果传递呢就以你传递的为主那么好那么我们是不是首先我们可以把这个什么UserUser先给它打印出来User点什么Log打印出来
[03:21] 那我们先来刷新看一下页面看效果走那么我们可以看到是不是已经把这个U的对象是不是打印出来了年龄是20名字呢是张三好那么那么我们来调用它的方法那么我们怎么去调用呢是不是通过这个对象点这个方法去做一个调用那么我们把它的这个呢也打印出来console.log打印一下那么把这个sayhello来打印一下走
[03:50] 可以看到hello张三哎ok没有任何问题那么静态方法怎么使用注意静态方法啊方法的使用那么静态方法的使用呢我们就不用拿到这个对象去点而是通过什么呢拿到这个类啊直接去点就可以了来一个console点log那么输出什么呢来一个优的注意大写的优的啊是我们的类点什么呢我们判断一下他年龄比如说传入个20
[04:20] 那么20岁这个人他是成年人还是未成年人呢是成年人那么你传一个比如16对吧刷新一下那就是未成年人哎呀OK这个呢就是一个静态方法这个是他的什么的这个是一个非静态方法哎呀OK好那么这个是关于类的一个基本的使用那么在在这个类类的使用中呢还有一种方式叫什么呢叫继承
[04:46] 继承的同样也是通过一个Extender去做一个继承那我们来看一下那么假设的我现在的我有一个用户啊我有一个类叫别的叫张三或者李四啊都可以class李四吧李四我要继承谁呢继承我这个User注意使用的关键字是什么呢Extender当我们去继承这个User之后由于你这个User是不是有一个
[05:13] 有一个构造函数对吧那么我们必须理识它也有一个构造函数那么它的构造函数注意你看它会报错它呢必须要求我们去调用什么呢我们负类的一个负类的一个构造函数那么我们通过一个shopper这个关键字去调用那么那么shopper调用谁呢调用你负类的一个构造函数那么你需要两个参数我给你传递比如说
[05:43] 这叫李四啊李四年龄我李四呢是三岁是不是可以这样去做一个调用啊好那么你自己呢也可以写自己的一些这个方法啊比如说我们来一个叫做test吧啊随便写个方法那么return什么呢叫做呃什么呢test然后呢加一个这个箭头然后呢我们再更一个谁呢raise点什么的name
[06:12] 好,那么我们下面是不是就可以去直接去new一个这个李四这个改成搭写吧李四那么我们来一个叫做let来一个李四等于new一个李四那么我们先把这个李四呢给它打印出来点log打印出来来看一下log好,那么我们把它打印看一下效果啊走那么我们可以看到李四呢它也是个对象
[06:40] 那么他通过一个tend去扩展做了一个继承那么我们可以看到他的名字是李四年龄是30对不对年龄是30那么我们来看一下他的一个test方法能用吗我们这样来看一下那么console把上一行复制一下然后李四点什么点test来看效果走是不是打印出来是不是就是test
[07:08] 箭头李四哎OK那么同样的你的子类也可以去自定义这个方法啊也是可以的好哎OK好那么他的用法呢就这样去使用大了你能不能使用他的负内动的方法呢可不可以啊我们来看一下效果啊那把它也靠一个那么我能不能对用这个c hello呢可以吗当然是可以由于你继承了这个优势就可以去
[07:36] 使用这个负类中所定的这个方法那么能不能去调用他的什么呢调用他的这个静态方法呢我们来看一下例四啊我们去看一下18岁啊判断一下18岁是未成年人还是成年人呢啊是成年人同样是不是也可以去调用他的一个静态方法对吧哎OK好那么这个呢就是关于他的类的一个使用那么我们可以看一下
[08:04] 基本用法的就这样去使用那么继承的就可以通过一个X的关键字去做一个继承去使用OK这个用法跟加尔宗的类的使用法非常的相似这个理解起来并不难好那么关于这个类的一些基本的语法我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 JavaScript ES6 中 class（类）语法的使用，包括构造函数、实例方法、静态方法和继承。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 HTML 文件结构，包含 <script> 标签，准备编写 ES6 代码。
画面2：在 <script> 标签内开始编写 ES6 class User，定义构造函数和 sayHello 方法，光标在 return 语句后，IDE 提示“expression expected”。
画面3：在 sayHello 方法中添加了 let length = ... 的代码，但未完成，IDE 提示“expression expected”。
画面4：完成 sayHello 方法，添加静态方法 isAdult，判断年龄并返回“成年人”或“未成年人”。
画面5：在 class User 后添加实例化代码：let user = new User("张三"); console.log(user);。
画面6：在 console.log(user) 后添加 console.log(user.sayHello());，IDE 提示“expression expected”。
画面7：在 console.log(user.sayHello()); 后添加 console.log(User.isAdult(16));，IDE 提示“expression expected”。
画面8：在 console.log(User.isAdult(16)); 后添加 class Lisi extends User，IDE 提示“expression expected”。
画面9：完成 class Lisi extends User，定义构造函数和 test 方法。
画面10：在 class Lisi 后添加 let lisi = new Lisi();，IDE 提示“expression expected”。
画面11：在 let lisi = new Lisi(); 后添加 console.log(lisi);，IDE 提示“expression expected”。
画面12：在 console.log(lisi); 后添加 console.log(lisi.test());，IDE 提示“expression expected”。
画面13：在浏览器中查看页面，Console 面板显示了执行结果：user 对象、sayHello 方法返回值、isAdult 方法返回值、test 方法返回值。
画面14：展示课程 PPT，标题为“1.9. class（类）的基本语法”，内容包括 class 基本用法、静态方法、继承等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
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

</script>
</body>
</html>
```

画面2：
```javascript
class User {
    // 构造函数
    constructor(name, age = 20) {
        this.name = name;
        this.age = age;
    }
    sayHello() {
        return "hello, " + this.name;
    }
}
```

画面3：
```javascript
sayHello() {
    return "hello, " + this.name;
}
// 静态函数
static isAdult(age) {
    if (age >= 18) {
        return "成年人";
    }
    return "未成年人";
}
```

画面4：
```javascript
class User {
    // 构造函数
    constructor(name, age = 20) {
        this.name = name;
        this.age = age;
    }
    sayHello() {
        return "hello, " + this.name;
    }
    // 静态函数
    static isAdult(age) {
        if (age >= 18) {
            return "成年人";
        }
        return "未成年人";
    }
}
let user = new User("张三");
console.log(user);
```

画面5：
```javascript
let user = new User("张三");
console.log(user);
console.log(user.sayHello());
```

画面6：
```javascript
let user = new User("张三");
console.log(user);
console.log(user.sayHello());
console.log(User.isAdult(16));
```

画面7：
```javascript
let user = new User("张三");
console.log(user);
console.log(user.sayHello());
console.log(User.isAdult(16));
class Lisi extends User
```

画面8：
```javascript
let user = new User("张三");
console.log(user);
console.log(user.sayHello());
console.log(User.isAdult(16));
class Lisi extends User
```

画面9：
```javascript
let user = new User("张三");
console.log(user);
console.log(user.sayHello());
console.log(User.isAdult(16));
class Lisi extends User {
    constructor() {
        super("李四", 30);
    }
    test() {
        return "test -> " + this.name;
    }
}
```

画面10：
```javascript
let user = new User("张三");
console.log(user);
console.log(user.sayHello());
console.log(User.isAdult(16));
class Lisi extends User {
    constructor() {
        super("李四", 30);
    }
    test() {
        return "test -> " + this.name;
    }
}
let lisi = new Lisi();
```

画面11：
```javascript
let user = new User("张三");
console.log(user);
console.log(user.sayHello());
console.log(User.isAdult(16));
class Lisi extends User {
    constructor() {
        super("李四", 30);
    }
    test() {
        return "test -> " + this.name;
    }
}
let lisi = new Lisi();
console.log(lisi);
```

画面12：
```javascript
let user = new User("张三");
console.log(user);
console.log(user.sayHello());
console.log(User.isAdult(16));
class Lisi extends User {
    constructor() {
        super("李四", 30);
    }
    test() {
        return "test -> " + this.name;
    }
}
let lisi = new Lisi();
console.log(lisi);
console.log(lisi.test());
```

画面13：
```javascript
// Console 面板显示：
user: {name: "张三", age: 20}
hello, 张三
未成年人
test -> 李四
```

画面14：
```markdown
1.9. class（类）的基本语法

JavaScript 语言的传统方法是通过构造函数定义并生成新对象。ES6引入了class的关键字自定义类。

基本用法：
<script>
class User {
    constructor(name, age = 20) { // 构造方法
        this.name = name; // 添加属性并初始化
        this.age = age;
    }
    sayHello() { // 实例方法
        return "hello";
    }
}
static isAdult(age) { // 静态方法
    if (age >= 18) {
        return "成年人";
    }
    return "未成年人";
}
let user = new User("张三");
console.log(user); // User {name: "张三", age: 20}
console.log(user.sayHello()); // hello
console.log(User.isAdult(20)); // 成年人
</script>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
标题：1.9. class（类）的基本语法
内容：
- JavaScript 语言的传统方法是通过构造函数定义并生成新对象。ES6中引入了class的关键字自定义类。
- 基本用法：
  - class User {
    - constructor(name, age = 20) { // 构造方法
      - this.name = name; // 添加属性并初始化
      - this.age = age;
    }
    - sayHello() { // 实例方法
      - return "hello";
    }
  }
  - static isAdult(age) { // 静态方法
    - if (age >= 18) {
      - return "成年人";
    }
    - return "未成年人";
  }
  - let user = new User("张三");
  - console.log(user); // User {name: "张三", age: 20}
  - console.log(user.sayHello()); // hello
  - console.log(User.isAdult(20)); // 成年人

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

