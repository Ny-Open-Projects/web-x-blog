# 画面线理解：13.ES6新特性之class类的基本语法

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\13.ES6新特性之class类的基本语法【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:33, 01:38, 02:34, 03:04, 03:32, 04:11, 04:37, 05:01, 05:35, 06:25, 06:49, 07:15, 07:58, 08:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:06:26

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
