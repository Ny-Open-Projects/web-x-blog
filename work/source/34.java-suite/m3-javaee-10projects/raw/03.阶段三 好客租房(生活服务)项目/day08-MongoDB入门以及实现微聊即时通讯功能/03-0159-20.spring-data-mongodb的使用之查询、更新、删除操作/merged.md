# 20.spring-data-mongodb的使用之查询、更新、删除操作

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\20.spring-data-mongodb的使用之查询、更新、删除操作【海量资源尽在 ubkz.com】.mp4
- 时长 9分47秒（音频 587s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下这个PersonDL中的一些其他方法的实现啊那么我们来看一下我们的讲义在讲义中呢会有怎么几个实现那么在上面啊在上面这个位置那么可以看到呢它呢是通过名字去做一个查询我们的一个这个数据那我们把这个拷过来我们来测一下OK放到这个位置好
[00:28] 那么我们可以看到它是去通过名字那么我们通过我们template然后fund去查找它需要接收是两个参数一个参数是query就是我们查询的一个对象另外一个就是class那么class其实我们就是要去指定它返回的是一个什么类型的数据所以我们指定person.class然后在这个位置需要给它构造一个query对象
[00:55] 那么这个快速对象是SpringSpringDate中的这样的一个快速对象那么我们去通过这样的构造那么在这个位置它需要一个creator然后点Value然后你构造一个条件就是ValueValue等于什么点Ease一个name,传入一个nameok它就是这样的一个写法好的那么下面我们来基于这个方法我们去做一个测试测试大家看一下在这个位置我们去写一个
[01:25] word叫test这个方法好那么我们把这个q给它改成大写然后呢加一个test一个注解test注解然后呢我们去调用类似点person.do中的queryperson.list.by.name给它一个比如说叫张三去做一个查询然后呢我们来看一下它的返回值呢将是一个
[01:54] 哎他的返回值是一个list哎刚刚为什么没有提示出来呢我们来再来一下啊他的返回值呢是这个张三返回是一个list然后呢我们对这个list呢去做一个便利然后呢我们把它呢去打印出来那么就是person把这个person这个对象打印出来哎OK那么看一下他是否能够查到我们这个多条名为张三的这个数据呢我们来看一下好那么来看一下他会怎么样呢
[02:22] 等待他的一个执行执行结束了但是我们发现呢没有查到数据为什么呢原因是我们这里面没有张三对吧那么我们就再查一个吧李四吧或者说就李四吧就查李四那我们再去执行一下看他会怎么样然后呢我们来数据李四有李四王五赵六孙七等待他的一个执行OK那么现在我们可以看到这个数据啊是不是就已经显示出来了对吧就是
[02:55] 李四这个数据那我们接着继续看它下面的一些这个操作下面这个查询是做什么呢去做一个分页的一个查询那么传了一个配置传了一个ros做一个分页那么我们来看一下这个它怎么玩呢好那么在这个里面呢我们可以看到它去传了两个参数一个配置一个ros那么前面我们在讲mongodb操作的时候呢是不是讲过它的一个limit和speak这样的一个方法
[03:23] 那么limit就是我们需要拿几条数据而这个speak就是我们跳过几条数据那么可以看到在这个里有一个小的一个算法就是怎么呢你跳过的这个数量呢是你的配置减一乘以rosOK这个我相信大家也都会去计算啊然后呢limit ros是不是就是去拿几条数据啊OK那么下面呢我们去来测试一下get a person list by name
[03:50] 那么没有by name了这个名字这个方法名写的有点不合适那么应该叫做queryPagerPagerPersonList那么应该是这样写一个名字我们再来写它的一个测试的用例public返回值word然后 test一个他然后把它拷过来然后把这个q我们改成大写好那么我们加一个测试用例然后我们就要用类似点类似点 do
[04:17] 点什么呢是不是传这个交通这个方法传递两根参数一个是配着一个ros比如说我们第一页拿两条我们来看一下那么第一页拿两条返回的数据呢显然是不是就是李四和王五那么我们来看一下它的一个结果那么拿到一个list然后把它编例出来然后呢好那么我们来执行一下那么这个呢是第一个拿的数据对吧李四和王五那么我一会呢我们把这个配置改成二我们再来做一个测试
[04:50] 好那么可以看到这个结果是不是就李四和王五我们把这配置改成二我们再来测试一下走那么我们可以看到那么现在是不是已经查到赵六和孙七这两条数据其实这个就是给大家演示这个的目的就是告诉大家在芒果DB中我们怎么样去做分页OK好那么大阿咖的分页还有另外一种写法那么到后面的时候我们去做我们的微聊项目的时候我们再来做一个讲解OK
[05:19] 好那么这个是这个方法还有一个呢是做update和deleteupdate delete那么这样咱们把这两个方法全部都抠过来吧抠过来之后呢我们去做一个测试然后呢把它呢去放到放到我们的这个deo里面放到这那我们重点来关注一下它的一个代码的写法那么在这个位置呢去调用update first那显然是更新一条数据对不对然后呢有三个参数
[05:48] 第一个呢是第一个呢这个呢是我们的查询条件那第二个呢是我们的更新条件啊就是你更新什么数据第三个呢就是我们你返回的一个数据的类型是什么样的类型那么ok那么query呢我们现在是不是去通过这个id就是我们的组件是不是去做一个作为条件去做个更新然后呢我们把这个年龄改成啊这个你具体传入这个值那么ok啊这就是一个更新的一个逻辑啊相对还是比较简单的那么下面我们来做一个测试
[06:17] 那么我们把这个代码call一下然后 test怎么改一下改成updateupdateupdateupdate然后这个位置我们就调用什么类似点person.do.updateupdateupdate在这儿,传入一个person那么我们需要传什么内容是不是personperson然后来一个person等于new一个person
[06:52] 那么他是需要根据ID是不是去做一个查询那么OK那么我们来看一下这个怎么样去给他传递然后再这样去set一个ID那么这个ID是什么类型呢ID是一个project ID这种类型那么project ID怎么去给他传递呢我们需要去new一个object ID然后去把一个支付券给他传递进去这个支付券我们可以考一下比如说我们要更新李四的这个数据那么就把李四的这个ID的值给他拷贝过来
[07:20] 然后这个是不是就是我们的一个条件对吧然后我们再去给他设置一个AIDS年龄我看一下你原来是多少的原来是21岁那么改成23岁ok然后我们把这个person给他传递过去好这样的话是不是就完成了一个更新它的一个返回值就是update一个result那么把这个update result去打印出来好嘞那么我们去执行走好那么我们可以看到在这个位置它匹配的数量是不是1
[07:50] 然后更新的数量也是1ok好那么说明我们这个数据它肯定已经更新了对吧我们来看一下那么在这个位置是不是我们就把这个数据是不是就更新成这个名字这个年龄改成23岁ok好那么这个就是更新那么接下来我们来测试最后一个就是什么的删除来看一下那么test deleteok那么看一下怎么去操作这叫做this.person.do.deletebyid
[08:22] 那么注意这个ID呢传的是一个字符串那么我们就传一个字符串吧把这个刘德华删掉把这个给他传递过去哎OK然后呢他的一个返回值呢我们来看一下他的返回值是一个叫做delete result那么我们把这个delete result呢也打印出来叫delete result打印出来哎OK那么我们去我们去做一个执行等待他的一个执行的结束那么我们可以看到
[08:51] 这个是不是已经就删除成功了对吧因为它的一个delete count等于1那说明已经删除成功了那么我们来看一下我们的数据有没有被删掉呢数据是不是已经被成功了是不是删掉了刘德华这个用户已经被删除了OK那么这个呢就是所给大家去简单的去讲解了一下这个sprinted
[09:12] 对一个mongoDB的一个基本的使用那么后面在我们项目中也会有一些其他的使用那么到后面我们再做一些学习那么OK现在讲的都是一些基本的操作也希望大家能够动手的去把这些API的去操作一下去用一下相对如果前面我们有一些Splendid的一些学习或者说使用经验的话那么去写这样的代码应该是还是比较轻松很容易的
[09:39] 那么ok好那么关于我们的spam boot以及spam data去整合mango db的一个使用我们讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Data MongoDB 框架对 Person 实体进行增删改查操作，并通过测试类验证功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PersonDAO 类，使用 @Component 注解，通过 @Autowired 注入 MongoTemplate，实现 savePerson 方法。
画面2：在 PersonDAO 类中，导入 Query 和 Criteria 包，准备进行查询操作。
画面3：在 TestSpringPerson 类中，定义 testSave 方法，创建 Person 对象并调用 personDAO.savePerson()。
画面4：在 TestSpringPerson 类中，定义 testQueryPersonListByName 方法，调用 personDAO.queryPersonListByName("张三") 查询并打印结果。
画面5：终端显示 testQueryPersonListByName("李四") 测试通过，打印出匹配的 Person 对象信息。
画面6：在 TestSpringPerson 类中，定义 testQueryPersonListByName 方法，调用 personDAO.queryPersonListByName("李四") 查询并打印结果。
画面7：在 TestSpringPerson 类中，定义 testQueryPagePersonList 方法，调用 personDAO.queryPagePersonList(page, rows) 查询分页数据。
画面8：在 TestMongoDB.java 中，定义 testInsert 方法，创建 Document 并插入数据。
画面9：在 TestSpringPerson 类中，定义 testUpdates 方法，准备调用 personDAO.update 方法。
画面10：展示 Person 类，包含 id、name、age、address 字段，使用 @AllArgsConstructor 和 @NoArgsConstructor 注解。
画面11：在 testUpdates 方法中，创建 Person 对象并设置属性，调用 personDAO.update(person)。
画面12：在 TestSpringPerson 类中，定义 testDelete 方法，调用 personDAO.deleteById(id) 删除数据。
画面13：在 testDelete 方法中，调用 personDAO.deleteById("5c0c8a19235e19494a6533ad") 删除数据。
画面14：展示 PDF 文档，内容为 PersonDao 类的代码和 queryPersonListByName 方法的实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Component;

@Component
public class PersonDAO {
    @Autowired
    private MongoTemplate mongoTemplate;

    public Person savePerson(Person person) {
        return this.mongoTemplate.save(person);
    }
}
```

画面2：
```java
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class PersonDAO {
    @Autowired
    private MongoTemplate mongoTemplate;

    public Person savePerson(Person person) {
        return this.mongoTemplate.save(person);
    }
}
```

画面3：
```java
@Test
public void testSave() {
    Person person = new Person(ObjectId.get(), name: "刘德华", age: 50, new Address (street: "人民路", city: "北京", zip: "666666"));
    this.personDAO.savePerson(person);
}

@Test
public void testQueryPersonListByName() {
    this.personDAO.queryPersonListByName("张三");
}
```

画面4：
```java
@Test
public void testQueryPersonListByName() {
    List<Person> list = this.personDAO.queryPersonListByName("李四");
    for (Person person : list) {
        System.out.println(person);
    }
}
```

画面5：
```java
2019-12-09 14:17:46.321 INFO 2700 --- [main] cn.itcast.mongodb.TestSpringPerson: Person(id=5c0c8a19235e19494a6e6cc, name=李四, age=21, address=Address(street=北京西, city=北京, zip=666666))
2019-12-09 14:17:46.631 INFO 2700 --- [main] cn.itcast.mongodb.TestSpringPerson: Person(id=5c0c8a19235e19494a6e6cc, name=李四, age=21, address=Address(street=北京西, city=北京, zip=666666))
2019-12-09 14:17:46.631 INFO 2700 --- [main] cn.itcast.mongodb.TestSpringPerson: Person(id=5c0c8a19235e19494a6e6cc, name=李四, age=21, address=Address(street=北京西, city=北京, zip=666666))
```

画面6：
```java
@Test
public void testQueryPersonListByName() {
    List<Person> list = this.personDAO.queryPersonListByName("李四");
    for (Person person : list) {
        System.out.println(person);
    }
}
```

画面7：
```java
@Test
public void testQueryPagePersonList() {
    List<Person> list = this.personDAO.queryPagePersonList(page, rows);
    for (Person person : list) {
        System.out.println(person);
    }
}
```

画面8：
```java
@Test
public void testInsert() {
    Document document = new Document();
    document.append("id", "9999");
    document.append("username", "张三");
    document.append("age", 30);
}
```

画面9：
```java
@Test
public void testUpdates() {
    Person person = new Person();
    person.setId(new ObjectId(hexString: "5c0c8a19235e19494a6e6cc"));
    person.setAge(23);
    UpdateResult update = this.personDAO.update(person);
    System.out.println(update);
}
```

画面10：
```java
@AllArgsConstructor
@NoArgsConstructor
public class Person {
    private ObjectId id;
    private String name;
    private int age;
    private Address address;
}
```

画面11：
```java
@Test
public void testUpdates() {
    Person person = new Person();
    person.setId(new ObjectId(hexString: "5c0c8a19235e19494a6e6cc"));
    person.setAge(23);
    UpdateResult update = this.personDAO.update(person);
    System.out.println(update);
}
```

画面12：
```java
@Test
public void testDelete() {
    this.personDAO.deleteById("5c0c8a19235e19494a6e6cc");
}
```

画面13：
```java
@Test
public void testDelete() {
    this.personDAO.deleteById("5c0c8a19235e19494a6e6cc");
}
```

画面14：
```java
public class PersonDao {
    @Component
    public class PersonDao {
        @Autowired
        private MongoTemplate mongoTemplate;

        public void savePerson(Person person) {
            this.mongoTemplate.save(person);
        }
    }

    public List<Person> queryPersonListByName(String name) {
        Query query = Query.query(Criteria.where("name").is(name));
        return this.mongoTemplate.find(query, Person.class);
    }

    public List<Person> queryPersonListByName(Integer page, Integer rows) {
        Query query = Query.query(Criteria.where("name").is(name));
        return this.mongoTemplate.find(query, Person.class);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

