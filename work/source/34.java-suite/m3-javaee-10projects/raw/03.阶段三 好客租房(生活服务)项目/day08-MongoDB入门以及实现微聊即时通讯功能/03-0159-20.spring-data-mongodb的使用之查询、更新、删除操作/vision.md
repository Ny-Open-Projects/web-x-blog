# 画面线理解：20.spring-data-mongodb的使用之查询、更新、删除操作

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\20.spring-data-mongodb的使用之查询、更新、删除操作【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:57, 01:45, 02:11, 02:50, 04:11, 04:37, 05:31, 06:35, 07:03, 07:41, 08:21, 08:59, 09:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:46:24

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
