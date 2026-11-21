# 24.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\24.课程总结【海量资源尽在 ubkz.com】.mp4
- 时长 4分27秒（音频 267s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对今天的所学的内容呢我们做一个简单的一个总结那么今天的我们讲了有哪些内容呢我们回顾一下啊那么我们首先分析了我们这个图片存储的解决方案对吧然后呢我们又去实现了两种解决方案一种是阿里云的OSS的存储另外一种的是本地的文件的一个存储的方式做一个实现然后呢我们去整合了前端实现了我们图片上传这个功能
[00:28] 后面呢我们紧接着呢去实现了我们的房源列表查询这个功能后面呢我们给大家讲了一个新的一个技术叫GrabQL它的一个规范和它的一个实现啊OK那么我们大概是不是讲了这么多些内容呢我们简单的来看一下
[00:44] 在我们去讲图片存储解决方案的时候我们有讲了多种解决方案那么我们实现的是不是第一种这种和第四种对吧OK那么下面我们就基于阿里云的OSS存储的去做这样的一个服务OK那么这个是使用使用阿里的OSS服务是非常方便的能够去完成我们数据或者文件的一个存储大家的唯一的缺点就是需要付费需要付费
[01:11] OK好那么至于它怎么去用这个我们就不重复了前面我们都讲过了OK好那么下面呢我们在本地的这个文件系统中去实现的话那么实现逻辑跟我们前面的OS实现逻辑呢几乎是一样的只是在存储方面呢它会存到本地的文件系统中好嘞好那么下面呢我们就针对于我们的这个图片上传去做一个这样的一个整合OK好那么
[01:37] 在我们在前端整合的时候呢大家一定要去能够非常清晰的搞清楚我们在图片上传文件上传之后那个URL的在我们这个Android Source.js文件中的一个处理要把它搞清楚啊OK然后呢在我们去做表单提交的时候在这个位置有一个这样的一个小技巧也希望大家能够把这个小技巧呢学会啊好那么继续往下面看下面呢是否我们实现了一个房源的一个列表
[02:07] 通过一个分页的一个查询对吧OK好这个就不再重复了这个内容呢大家也希望大家能跟着去敲一遍好嘞好那么在我们后面呢是不是做了一个跟我们前端的一个整合然后在这个里面呢我们实现了一个是不是图片的一个展示这样的一个效果OK也希望大家能够动手去做一下好
[02:31] 那么最后呢是不是我们去学习了一个新的一个技术叫GrabQL这样的一个入门对吧做了这样的入门它呢是Facebook去用于我们去描述查询的这样的一个前后端
[02:46] 去做这样的一个接口调用的一个规范这样的规范然后它的一些地址大家都可以去官网地址都可以阅读一下去查看一下包括我们后面分析了rest4它所存在的一些问题OK那么我们可以看到rest4所存在的问题GraderQL的确是不是做了这样的一些相关的一些解决那么以及我们讲了它的一些规范
[03:10] 好那么在后面呢我们去讲了一些什么呢讲了那个GradQ2它的一个Java的一个实现是不是就是GradQ2-Java这样的一个项目是不是对这个规范做了一些这个具体的一个实现那我们基于这个项目呢就去实现了GradQ2这样的一个服务的一个提供啊OK好那么在我们去提供这个GradQ2服务的时候呢有两种实现啊一种呢是存
[03:38] 加把API的实现一种呢是通过这个SDL的实现对吧那么我们更推荐的是不是使用第二种这种方式做一个推荐啊OK然后呢在最后呢我们给大家讲了一个对象的一个这个嵌套哎呀OK那么要明白的一点是在我们做完这个嵌套之后啊他并不是说这个GradualQL就能够帮我们帮我们去实现这个关联的查询他并不能实现啊那么需要我们自己
[04:07] 来去实现我们的观点的查询那么最终才能够实现我们想要的一个效果OK好那么这个就是我们今天的大致的一些内容OK那么剩下的就交给大家了需要你们去自己动手去把它实现一下好那么课程的一个小节我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
本课程讲解了图片上传存储方案（含本地文件系统与阿里云OSS）、RESTful API设计、以及GraphQL入门与Java实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 内容：展示GraphQL Java实现中User对象的构建逻辑，包含查询测试用例。
- 代码：
  .dataFetcher("user", environment -> {
  Long id = environment.getArgument("id");
  return new User(id, "张三".id, 20 + id.intValue(),new
  Card("number_",id, id);
  }).build();
- 测试用例：
  查询字符串：{user(id:1){id,name}}
  错误：[]
  结果：{user={id=1, name=张三_1}}
  查询字符串：{user(id:1){id,name,card(cardNumber)}}
  错误：[]
  结果：{user={id=1, name=张三_1, card={cardNumber=number_1}}}
  查询字符串：{user(id:1){id,name,card(cardNumber,userId)}}
  错误：[]
  结果：{user={id=1, name=张三_1, card={cardNumber=number_1, userId=1}}}

画面2：
- 内容：介绍图片存储解决方案，重点讲解阿里云OSS服务。
- 文本：
  1. 直接将图片保存到服务的硬盘
    1. 优点：开发便捷，成本低
    2. 缺点：扩容困难
  2. 使用分布式文件系统进行存储
    1. 优点：容易实现扩容
    2. 缺点：开发复杂度稍大（尤其是开发复杂的功能）
  3. 使用nfs做存储
    1. 优点：开发较为便捷
    2. 缺点：需要有一定的运维知识进行部署和维护
  4. 使用第三方的存储服务
    1. 优点：开发简单，拥有强大功能，免维护
    2. 缺点：付费
  在本套课程中采用第一、第四解决方案，第三方服务选用阿里云的OSS服务。

画面3：
- 内容：展示阿里云OSS服务的购买页面，包含流量包购买选项。
- 文本：
  购买下行流量包：
  （表格数据：包含“流量包”、“单价”、“数量”、“总价”等列，具体数值如“100GB”、“0.01元/GB”、“1000”、“10元”等）

画面4：
- 内容：展示本地文件系统存储方案的Java代码实现。
- 代码：
  import cn.itcast.haoke.dubbo.api.vo.PicUploadResult;
  import org.apache.commons.lang3.RandomUtils;
  import org.apache.commons.lang3.StringUtils;
  import org.joda.time.DateTime;
  import org.springframework.stereotype.Service;
  import org.springframework.web.multipart.MultipartFile;
  import java.awt.ImageIO;
  import java.awt.image.BufferedImage;
  import java.io.ByteArrayInputStream;
  import java.io.File;
  import java.io.IOException;
  import java.util.Date;
  @Service
  public class PicUploadFileSystemService {
  // 允许上传的格式
  private static final String[] IMAGE_TYPE = new String[]{"bmp", ".jpg", ".jpeg", ".gif", ".png"};

画面5：
- 内容：展示前端上传组件的HTML代码和JavaScript处理逻辑。
- 代码：
  <div>
  <Upload
  action="/haoke/pic/upload"
  listType="picture-card"
  fileList={fileList}
  onPreview={this.handlePreview}
  onChange={this.handleChange}
  >
  {fileList.length ? null : uploadButton}
  </Upload>
  <Modal visible={previewVisible} footer={null} onCancel={this.handleCancel}>
  <img alt="example" style={{ width: '100%' }} src={previewImage} />
  </Modal>
  </div>
  handleFileList = (obj) => {
  let pics = new Set();
  obj.forEach((v, k) => {
  if(v.response_name) {
  pics.add(v.response_name);
  }
  });

画面6：
- 内容：展示前端图片上传测试界面。
- 代码：
  // 处理图片
  values.pic = [...this.state.pics].join(',');
  dispatch({
  type: 'house/submitHouseForm',
  payload: values,
  });

画面7：
- 内容：展示HouseResourcesService的Java实现代码。
- 代码：
  package cn.itcast.haoke.dubbo.server.Service.impl;
  import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
  import cn.itcast.haoke.dubbo.server.Service.HouseResourcesService;
  import cn.itcast.haoke.dubbo.server.vo.PageInfo;
  import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
  import com.baomidou.mybatisplus.core.metadata.Page;
  import org.apache.commons.lang3.StringUtils;
  import org.springframework.stereotype.Service;
  import org.springframework.transaction.annotation.Transactional;
  @Transactional
  public class HouseResourcesServiceImpl extends BaseServiceImpl implements HouseResourcesService {

画面8：
- 内容：展示商品列表页面的效果。
- 表格数据：
  （表格列：商品编号、商品名称、属性、规格、发货方式、单价、销量、操作）
  （示例数据：商品编号1，商品名称“商品1”，属性“1”，规格“1”，发货方式“一”，单价“17万”，销量“1”，操作“查看 编辑”）

画面9：
- 内容：展示RESTful API的HTTP请求方法。
- 代码：
  GET http://127.0.0.1/user/1 #查询
  POST http://127.0.0.1/user #新增
  PUT http://127.0.0.1/user #更新
  DELETE http://127.0.0.1/user #删除
  #请求
  GET http://127.0.0.1/user/1001
  #响应：
  {
  id: 1001,
  name: "张三",
  age: 20,
  address: "北京市"。

画面10：
- 内容：展示GraphQL如何避免RESTful的过度请求。
- 图形结构：
  上方：{hero {name}} → 下方：{“data”: {“hero”: “R2-D2”}}
  上方：{hero {name, appearsIn}} → 下方：{“data”: {“hero”: {“name”: “R2-D2”, “appearsIn”: [“NEWHOPE”, “EMPIRE”]}}}

画面11：
- 内容：展示GraphQL的GitHub仓库地址。
- 文本：
  github : https://github.com/GraphQL-java/GraphQL-java

画面12：
- 内容：展示User类的Java代码实现。
- 代码：
  public class User {
  private Long id;
  private String name;
  private Integer age;
  public User() {
  }
  public User(Long id, String name, Integer age) {
  this.id = id;
  this.name = name;
  this.age = age;
  }
  public Long getId() {
  return id;
  }

画面13：
- 内容：展示Card类的Java代码实现。
- 代码：
  package cn.itcast.GraphQL.vo;
  public class Card {
  private String cardNumber;
  private Long userId;
  public Card() {
  }
  public Card(String cardNumber, Long userId) {
  this.cardNumber = cardNumber;
  this.userId = userId;
  }
  public String getCardNumber() {
  return cardNumber;
  }
  public void setCardNumber(String cardNumber) {
  this.cardNumber = cardNumber;
  }

画面14：
- 内容：重复画面1的内容，展示GraphQL Java实现中User对象的构建逻辑和查询测试用例。
- 代码：
  .dataFetcher("user", environment -> {
  Long id = environment.getArgument("id");
  return new User(id, "张三".id, 20 + id.intValue(),new
  Card("number_",id, id);
  }).build();
- 测试用例：
  查询字符串：{user(id:1){id,name}}
  错误：[]
  结果：{user={id=1, name=张三_1}}
  查询字符串：{user(id:1){id,name,card(cardNumber)}}
  错误：[]
  结果：{user={id=1, name=张三_1, card={cardNumber=number_1}}}
  查询字符串：{user(id:1){id,name,card(cardNumber,userId)}}
  错误：[]
  结果：{user={id=1, name=张三_1, card={cardNumber=number_1, userId=1}}}

