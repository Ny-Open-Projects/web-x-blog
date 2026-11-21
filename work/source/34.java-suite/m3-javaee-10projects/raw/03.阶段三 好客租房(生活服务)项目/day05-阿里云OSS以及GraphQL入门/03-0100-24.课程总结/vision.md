# 画面线理解：24.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\24.课程总结【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:54, 01:10, 01:20, 01:38, 02:02, 02:12, 02:23, 02:59, 03:08, 03:23, 03:38, 03:53, 04:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:05:07

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
  package cn.itcast.haoke.dubbo.server.service.impl;
  import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
  import cn.itcast.haoke.dubbo.server.service.HouseResourcesService;
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
  github : https://github.com/graphql-java/graphql-java

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
  package cn.itcast.graphql.vo;
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
