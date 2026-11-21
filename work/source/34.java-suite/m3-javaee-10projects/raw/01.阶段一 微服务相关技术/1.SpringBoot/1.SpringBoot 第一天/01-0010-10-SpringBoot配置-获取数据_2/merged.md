# 10-SpringBoot配置-获取数据_2

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\10-SpringBoot配置-获取数据_2_【海量资源尽在 ubkz.com】.mp4
- 时长 10分29秒（音频 629s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 介绍完前边两种获取配置文件内容的方式接下来我们来说最后一种At Configuration Properties的这种方式那么这种方式呢其实是让配置内容和我们的对象进行相互绑定的一种方式它也是一种比较实用的一种方式那么我们打开IDR看一下我们这个配置我们这个配置里边有一个PersonPerson下面有两个属性一个是Name一个是Age
[00:30] 那么在之前的时候我们是单个的把它每一个属性都注入到我们需要用这些属性的位置上比如说我们单个注入了Name单个注入了Age但是现在我们期望我们有一个Person的对象将来我们在这配置的内容的属性值就能自动的注入到Person对象的Name成员位置Age的成员位置那么这个时候我们就可以采用Add Configuration Properties的方式
[00:59] 那么这个时候我们可以先定义一个person类person类在person类上呢我们有一些属性比如说private string的name然后呢private int的age好这个时候你想注入成功的话你这个name和age它的get和setter方法啊它的一个名字必须跟这个名字是保持一致的那么定义完了person的对象之后呢我们再提供一个
[01:30] insert里边我们给它添加get和set的方法为了待会打印方便我们给它加一个toString的方法好弄完了之后这个类还需要加这么两个注解第一个注解呢我们加个complement表示了这个person类它被sprint所识别它是一个bin那么第二个注解就比较关键了就是我们用的这个叫做configuration properties
[01:57] 那么加上这个诸解之后呢你看这个类就有反应了它上面有个红条很难看这个红条的事呢我们先不说待会最后我们再来解决这个红条其实这个东西呢并不影响运行它只是一个提示的问题那么加上了这个configuration properties之后那么接下来我们再说一个比较关键的东西就是说这个里边啊现在我要在配置文件里边去找有没有一个name和一个age那么我们看
[02:25] 配置文件里边有name age吗有啊这个地方有name这个地方是不是也有name如果我加了这个注解之后我什么都不干现在呢它会把这个name就是这个属性的nameabc给它注入到我们对应的person类里边的这个name属性里边去它并不会注入这个name就是person下边的name
[02:49] 因为我们在这个里边要指定一个前缀如果指定了前缀之后才可以去使用person前缀下面的name和age属性当然我们可以来测试一下我们打开这个Controller然后呢我们在这里边注入一个private person好person注入完了之后呢我们直接用all to where注解注入相当于创建了一个person对象那么弄完了之后呢我们在这最后呢我们再来分隔一下
[03:19] 分割完了之后我们直接把我们注入的这个person对象给它打出来打出来完事之后我们来启动运行一下看一下如果说这个地方它注入的是这个第一层级的就是这个name应该是abcage呢是注入不进来的那么age会有默认值应该是0对吧好如果是name是abcage是0那么证明它是没有采用这两个属性值的好我们同样的来访问一下
[03:48] 访问一下呢我们刷一下来看这个name是不是abcage就是0了所以呢在这个configuration properties注入的时候一定要格外小心你应该去注入相对应你需要的那个前缀下边的这些属性所以呢在这个数注解上我们可以有一个属性来控制叫做profix前缀前缀是谁呢就是person这个名
[04:16] 就是这个person这个名是跟这个值是一模一样的那么这样弄完了之后我们再来重启当然为了看到区别我们把这个就改成张三了好把这个给它注释掉注释掉之后呢我们在这个地方写成张三那么写成张三之后呢这时候我们再获取这个person对象的值应该是张三20重启一下重启完成了之后呢我们再来刷新一下这个程序刷新完事之后我们可以看
[04:48] 它的name值是20age值name值是张三age值就是20了OK那么这个configuration properties这种注入方式呢我们就介绍完了当然了除了注入这种基本的属性啊比如说这个地方我们把address也给它复制一份address呢其实这种数组或者集合的值也是同样可以注入的那么这样论完了之后我们在person类里边呢也可以加上一个比如说加上一个数组吧provide weight
[05:18] 数组呢四不串的数组OK然后叫做address当然集合也是可以的哈为了看它效果我们给它加这么一个getter和setter的方法然后呢把toString方法toString方法我们就不用重写了哈因为这个数组打印出来的这个值呢是一个地址值所以呢为了获取到这个address的属性我们可以在这个地方我们把
[05:46] 给它单独打印一下Person第二GetAdress获取这么一个数组然后呢我们便利循环一下我们打印一下这个S如果不出任何意外的话这个S应该是北京第二个应该是上海好我们再来重启一下我们这个程序重启完事之后呢我们再来刷新一下刷新完事之后我们来看这个值有没有注入进来呢北京上海是不是都没有问题的OK
[06:20] 那么这样呢我们就介绍完了这么一个第三种获取配置文件内容的方式就是用这个configuration properties这个地方一定要注意啊我们一般会加上这么一个前缀表示了person这个配置下边的内容和这些属性一一的对应注入那么最后我们来解决一下这个红条这个问题啊这个红条呢我们可以简单读一下说Spring Boot Configuration Annotation就是Spring Boot的配置注解处理器Processor
[06:50] Not found in ClassPass在我们ClassPass的路径下没有发现这么一个注解的处理器这个东西是啥呢不用担心我们在后边看它说打开一个Documention就是打开一个文档我们打开打开之后呢它就会弹出这么一个配置文件的网页其实就是Spring Boot的这个参考手册里边那个一个配置项的网页打开之后呢它说你可以加上这么一段注解加上这么一段叫做依赖
[07:18] 我们有这么一段依赖这个依赖呢就是一个叫做Spring Boot的Configuration的Processor就是配置的处理器这个处理器加上之后有什么用啊其实就是一个提示的功能那么我们把它加上加到我们POM文件里边去好我们在在这个地方加一下好加完之后呢你注意看加完之后再来回过头来看这个Person你看是不是就没有了
[07:43] 没有了之后接下来我们再写这个person的配置的时候在配置文件里边就会有这么一些提示信息了好打开这个页面然后呢我们比如说我们把这个age删掉删掉之后呢我们再写age哎你看现在是不是没有这个提示没有提示这样哈我们把其他的配置呢都给它删掉都删掉因为将来也不可能说我们再加很多的这样的一个
[08:08] 在一个目录下配三个不同的一个配置文件一般配置文件的风格就需要统一一下对吧我们比如说剩这么一个删掉其他两个好我们全部都删掉删掉之后呢这个压面你看还是这个样子它图标没有变过来我们这样我们把这个值呢都给它去掉去掉之后呢我们再来写Course你看是不是有提示了对吧其实呢之前呢只有我们
[08:35] Spring Boot里边自带的那些配置才有提示现在我们自己写的这个PersonLeader一个属性它也有提示了比如张三比如说age好20然后呢add is saddress这样就非常方便啊对吧北京然后呢上海这个处理器呢其实就是干这个事的让你写配置文件有提示啊当然了你在配一些自带的属性比如说server.port它是也有提示的OK
[09:06] 那么这个处理器我们就介绍完了那么至此呢我们Spring Boot来读取自定义的配置内容的三种方式我们都介绍完了第一种方式呢就是我们使用value注解的方式来获取这个配置那么这样的方式呢它是一个一个属性单个的去注入如果属性值比较少的话用value是比较方便的但是一旦多了可能就比较麻烦看起来要注入很多的属性内容
[09:34] 那么第二种呢是注入一个对象environment环境对象那么通过这个ENV对象它对应的get property的方法就可以把对应的你想要获取的属性值给它获取出来还有第三种是我们的对象和我们配置属性的一个绑定是用configuration properties这么一个注解然后一般我们会去指定这么一个前作那么指定完前作之后呢就可以去将我们这个对象
[10:03] 对应的这些属性和我们配置前缀下边的这些属性挨个的依次的注入最后不要忘记在这个自定义的Java Bean上要加这么一个complement注解让它被Spring Boot或者说被Spring所识别OK那么这个Spring Boot来获取配置文件内容的三种方式我们都介绍完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 中使用 @ConfigurationProperties 注解将 YAML 配置文件中的属性绑定到 Java Bean，并演示了配置处理器的使用和相关报错解决。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 application.yml 文件内容，其中定义了 server.port、name、person、address、msg 等配置项，用于演示属性绑定。
画面 2: 切换到 Person.java 文件，准备编写实体类。
画面 3: 编写 Person.java 类，包含 name、age 字段和 getter/setter 方法。
画面 4: 编写 HelloController.java，使用 @Value 注解注入配置属性。
画面 5: 浏览器访问 http://localhost:8082/hello，显示 "hello Spring Boot 222!"。
画面 6: 在控制台输出了从配置文件中读取的属性值，包括 name、age、address、msg。
画面 7: 编写 Person.java 类，添加 address 字段和 setter 方法。
画面 8: 编写 HelloController.java，使用 @Value 注解注入配置属性。
画面 9: 在控制台输出了从配置文件中读取的属性值，包括 name、age、address、msg。
画面 10: 打开 Spring Boot 官方文档，查看 @ConfigurationProperties 注解的说明，了解配置处理器的使用。
画面 11: 在 Person.java 中添加 @ConfigurationProperties(prefix = "person") 注解。
画面 12: 在 application.yml 文件中，将 person 配置项的值修改为 "zhangsan"。
画面 13: 在 application.yml 文件中，将 person 配置项的值修改为 "zhangsan"。
画面 14: 在 Person.java 中添加 @ConfigurationProperties(prefix = "person") 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```yaml
server:
  port: 8082

name: abc
# 1. 基础属性
name: ${name} # zhangsan
age: 20

# 2. 对象属性
person: {name: zhangsan,age: 20}

# 3. 数组
address:
  - beijing
  - shanghai

# 4. 数组属性
address2: [beijing,shanghai]

# 5. 变量
msg1: 'hello \n world' # 不会识别转义字符，会原样输出
msg2: "hello \n world" # 会识别转义字符
```

画面 2:
```yaml
server:
  port: 8082

name: abc
# 1. 基础属性
name: ${name} # zhangsan
age: 20

# 2. 对象属性
person: {name: zhangsan,age: 20}

# 3. 数组
address:
  - beijing
  - shanghai

# 4. 数组属性
address2: [beijing,shanghai]

# 5. 变量
msg1: 'hello \n world' # 不会识别转义字符，会原样输出
msg2: "hello \n world" # 会识别转义字符
```

画面 3:
```java
import org.springframework.stereotype.Component;

@Component
public class Person {
    private String name;
    private int age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
```

画面 4:
```java
import org.springframework.stereotype.Component;

@Component
public class Person {
    private String name;
    private int age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
```

画面 5:
```java
@Value("${person.name}")
private String name;
@Value("${person.age}")
private int age;
@Value("${person.address}")
private String address;
@Value("${person.msg1}")
private String msg1;
@Value("${person.msg2}")
private String msg2;

@Autowired
private Environment env;
@Autowired
private Person person;

@GetMapping("/hello")
public String hello() {
    System.out.println(name);
    System.out.println(age);
    System.out.println(address);
    System.out.println(msg1);
    System.out.println(msg2);
    System.out.println(person);
    String[] address = person.getAddress();
    for (String s : address) {
        System.out.println(s);
    }
    return "hello Spring Boot!";
}
```

画面 6:
```
hello Spring Boot 222!
```

画面 7:
```yaml
server:
  port: 8082

name: abc
# 1. 基础属性
name: ${name} # zhangsan
age: 20

# 2. 对象属性
person: {name: zhangsan,age: 20}

# 3. 数组
address:
  - beijing
  - shanghai

# 4. 数组属性
address2: [beijing,shanghai]

# 5. 变量
msg1: 'hello \n world' # 不会识别转义字符，会原样输出
msg2: "hello \n world" # 会识别转义字符
```

画面 8:
```java
public void setName(String name) {
    this.name = name;
}

public int getAge() {
    return age;
}

public void setAge(int age) {
    this.age = age;
}

public String getAddress() {
    return address;
}

public void setAddress(String[] address) {
    this.address = address;
}

@Override
public String toString() {
    return "Person{" +
            "name='" + name + '\'' +
            ", age=" + age +
            ", address=" + address +
            '}';
}
```

画面 9:
```java
@Value("${person.name}")
private String name;
@Value("${person.age}")
private int age;
@Value("${person.address}")
private String address;
@Value("${person.msg1}")
private String msg1;
@Value("${person.msg2}")
private String msg2;

@Autowired
private Environment env;
@Autowired
private Person person;

@GetMapping("/hello")
public String hello() {
    System.out.println(name);
    System.out.println(age);
    System.out.println(address);
    System.out.println(msg1);
    System.out.println(msg2);
    System.out.println(person);
    String[] address = person.getAddress();
    for (String s : address) {
        System.out.println(s);
    }
    return "hello Spring Boot!";
}
```

画面 10:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-configuration-processor</artifactId>
    <optional>true</optional>
</dependency>
```

画面 11:
```java
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Component
@ConfigurationProperties(prefix = "person")
public class Person {
    private String name;
    private int age;
    private String[] address;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String[] getAddress() {
        return address;
    }

    public void setAddress(String[] address) {
        this.address = address;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", address=" + address +
                '}';
    }
}
```

画面 12:
```yaml
person:
  name: zhangsan
  age: 20
  address:
    - beijing
    - shanghai
```

画面 13:
```yaml
person:
  name: zhangsan
  age: 20
  address:
    - beijing
    - shanghai
```

画面 14:
```java
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Component
@ConfigurationProperties(prefix = "person")
public class Person {
    private String name;
    private int age;
    private String[] address;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String[] getAddress() {
        return address;
    }

    public

