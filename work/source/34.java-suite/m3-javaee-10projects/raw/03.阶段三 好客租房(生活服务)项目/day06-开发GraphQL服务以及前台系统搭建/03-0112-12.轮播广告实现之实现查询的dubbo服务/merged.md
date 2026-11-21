# 12.轮播广告实现之实现查询的dubbo服务

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\12.轮播广告实现之实现查询的dubbo服务【海量资源尽在 ubkz.com】.mp4
- 时长 19分17秒（音频 1158s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们接着继续啊下面呢,我们来创建我们的广告这个工程就是AD的一个工程啊那我们先把这个工程呢,先创建出来我先拷贝这个工程的名字啊,别搞错了然后呢,进入这个里面呢,要注意的是是不是在这个下面创建一个子工程,OK好,然后呢,选择它,点击这个Next然后呢,下一步,然后呢,拷贝一下Next,点击Finish完成
[00:27] 好那么这个模块是不是就已经搞定了那么我们接下来呢还是需要跟我们这个房源是不是一样下面继续创建两个是不是子工程啊哎呀ok呃所以呢我在这个下面啊继续再创建两个子的一个model然后呢我依然呢选择是这个我的JDK然后点击这个下一步然后呢我在这个下面呢创建一个叫interfaceinterface啊interface然后呢拷贝一下下一步拷贝然后呢非净子完成
[00:57] 而这个工程是不是就创建好了紧接着的我们继续来创建一个叫做Service的一个工程点击下一步然后呢把这个interface改成serviceservice然后呢拷贝next然后呢fittings完成那么这两个工程是不是就已经创建好了那么创建好之后呢我们来梳理一下他的一些依赖的关系那么这个工程对吧这个工程一定要依赖于他对不对
[01:27] OK这是第一个第二个是这个工程是不是要去被他依赖反过来就是说他们要依赖于他对吧OKservice要依赖于我们的 interface那么下面我们来看一下我们把这common导入进来怎么导是不是在我们这个下面是不是导入过对吧我们把这个依赖的坐标拷贝一下Ctrl C拷贝到这个AD这个里面来这个大家能够理解吧
[01:57] 好那么我们先把它是不是call过来好这个我们是不是就搞定了哎OK然后呢紧接着呢我们需要在我们这个Service这个下面我们去导入它的一个依赖那么dependence导入一个dependence然后呢ad然后呢gon然后呢interface是不是就是这个依赖把它导入进来是不是就是它要依赖于它哎OK
[02:22] 好 那么我们的依赖呢我们基本上就ok了当然了还缺一个依赖就是在我们这个Service这个依赖下面我们还是需要把这个sprintboot的这个tdbc的支持我们导入进来因为这个里面它一定会涉及到的是放到下面一定会涉及到的是我们数据库的操作对吧ok好 那么这样的话我们就基本上依赖就搞定了一会我们来看缺什么依赖我们再导就可以了好 那么下面我们来编写这个posal
[02:52] 在我们 interface下面我们创建一个包就叫 podo 包把包名我们扣过来找到 interface那么下面我们来创建一个 package 包然后在 package 下面我们就创建一个类把这个类我们创建出来那么咱们就这么创建拷贝它然后到这Ctrl C那么我就不去一点一点去写了对吧就直接拷贝了因为这个内容
[03:22] 这个内容就是跟我们的数据库结构是一样的内容啊好那么我们来看一下这个里面呢他还缺少一些东西是吧来看一下缺少哪些东西呢缺一些这个我们的一些依赖啊我们去把这个依赖导入一下那么首先我们可以看到这个里面我们是缺少一个这个table table name而这个注解呢他其实是什么呢我们的mybid is plus是不是我提供的一个注解所以呢我们需要
[03:51] 在我们的interface这个包下面的这个里面我们给他去引入一个谁呢是不是引入我们的一个mybattis plus的一个spinbook这样的一个支持对吧mybattis plus没有提示没有提示的话那我就拷贝吧去拷贝一下我就进入到这个里面应该有拷贝一下是不是就是这个依赖对吧这个依赖那么我把它放到我的这个
[04:22] interface这个下面好导入进来来看一下这回有没有还没有把这个包导入进来让我导导入一下OK这样的话导入进来是不是就搞定了对吧好那么OK这样的话呢我们就已经完成了他的一个引用完成了一个引用好嘞那么这个puzzle呢我们是不是就搞定了对吧puzzle就搞定了
[04:52] 那么下面呢我们来定义我们那个double的一个这个接口依然呢还是在我们这个interface这个包下面那我们还是给他创建一个这个API的这个包然后呢在这个java这个下面的创建一个API的这个包然后呢我们把这个内容呢我们来拷贝一下内容拷贝一下到这拷贝那么显然呢我们是定义了一个查询我们AD这样的一个服务对吧把这个包看一下
[05:22] 它是不是还是缺包来看一下缺一个VO的一个PageInfo我们来看一下那么这个PageInfo我们来找一下PageInfo其实是在我们前面的是不是这个里面有一个VO的一个定义对吧PageInfo这个PageInfo是不是也可以作为我们公用的一个PageInfo所以我们也可以把它丢到哪里是不是丢到这个common一个工程里面来你把它丢一下
[05:52] 然后呢我们进入这个下面创建一个包啊叫做VO然后呢把它呢也丢过来就是配置info然后呢我们是不是就可以把我们这个这个房源这个接口中的这个配置info是不是就可以给它删掉了把这个删掉然后呢把它呢也删掉OK好那么这样的话呢我们回到我们刚才interface中那么这个API这个接口是不是就搞定了来看一下
[06:21] 那么在这个接口中呢我们定义了一个方法叫做query AD list就是去查询我们的广告啊那么有三个参数一个呢就是我们的广告的一个类型然后呢还有一个呢就是我们的一个这个页数以及我们的每页显示的一个数据条数那么到这里呢我们这个interface中的它的一个定义是不是就搞定了那么接下来我们就要去做一个具体的实现
[06:48] 那么就要回到我们的这个服务Service这个工程里面对吧ok那么我们把这个都合起来啊别搞混了啊然后呢是在这个下面我们是不是继续做开发对吧好那么我们首先呢来去实现我们的double的这个接口啊是这个Service然后呢我们把这个包呢先创建好然后我们在下面呢把这个具体的一个实现类啊
[07:16] 这个我就不写了因为比较简单这个实现那么我们来拷贝一下就拷贝它它是不是就实现了我们刚刚所定义的这样的一个接口对吧OK那么我们来看一下这个里面是我们去需要引入的一个是不是这个double下面的对吧然后AD这个Service当然这个AD这个Service我们现在是不是还没有
[07:44] 所以我们需要去创建一个AD这个Service那么这个Service我们需要有一个包那么我们先把这个包也给它创建出来这个AD Service其实就是我们的业务的Service对不对那么同样的我们是先给它定义一个什么的接口还是定义这个AD Service这个接口来看一下那么这个就是我们所定义的AD Service接口它在这个接口中有一个方法叫做query ID
[08:13] ad list然后去做这样的一个查询OK传递的参数注意是一个ad对象ok好那么下面我们是不是就需要在这个位置要去给他去编写他的一个实现类对吧创建一个impl实现类我们就来写一个实现类叫做ad serviceimpl那么实现类首先他要继承谁
[08:42] 继承我们的base serviceimpl这个t,t呢是不是就是我们ad这个对象然后呢我们还要去实现我们的一个ad Service这个接口对吧这个接口然后呢我们去实现这个接口中的这个方法ok好那么实现这个方法这个是不是就是我们需要写的具体的一个业务逻辑啊业务逻辑好那么在这个里面我们来看一下我们该如何去
[09:11] 做一个实现呢那么显然在这个位置我们需要调用我们shopper中的一个叫做querylistquerypagerlist要做分页对吧要做分页因为返回的是一个pager info那么我们是不是需要调用这个方法对吧好那么我们来看一下它需要有几个参数是不是需要有123个参数第一个参数就是我们查询条件
[09:39] 第二个参数配置第三个参数就是nos好那么我们就把这个常规条件的给他那么他需要什么是不是我们就给他定义什么叫做query什么呢repo对吧queryrepo这个把它先拿掉不是他然后query好来我们进入里面来看一下是不是我们现在没有这个包是不是引入不进来呢来看一下先把这个拿掉
[10:12] 我们把它来引入一下到这个里面我们去引入一下啊有没有呢你发现没有那么也就是说这个里面我们并没有这个包啊并没有这个包这个包呢是不是也是买杯的意思啊买杯的意思这个plus为我们所提供的一个这个包那么没有我们也需要去引入一下啊我们把这个拷贝一下然后进入到我们这个Service下面啊我们去把它引入进来哎ok好那么引入进来之后呢
[10:46] 他肯定就有了这个包了你看现在是有这个包了那么有这个包之后呢我们就定义一个query的一个wrap然后等于去new一个query的一个wrap然后呢我们把它是不是传递给传递给他然后呢第二个呢就是这个pager这个参数第三个呢就是pagerSize这个参数ok这样的话呢我们是不是就
[11:12] 基本上把这个架构是打好了但是代码还没写完那么下面我们给他设置一些参数第一个我们需要设置的是他的一个排序注意排序那么我们是不是需要他根据一个什么的叫order根据一个orderorder by什么的DESC根据什么根据我们的一个字段叫做update是不是做一个倒序的一个排序
[11:41] 那第二个呢就是设置一个查询查询的这个条件那么这个条件呢是什么呢是不是就是我们那个type呀对不对所以呢我们要给他设置一个query这个rop.eq是不是一个相等哪个字段呢是不是就我们那个type那个字段它呢等于谁呢等于我们传入的这个type对象这个ad中那个type的一个值ok那么它的返回值要注意
[12:10] 它的返回值是一个叫做ipage这个对象而我们最终返回的是需要一个page info所以我们在这个位置需要给它new一个page info这个对象那么page info这个对象它需要有四个参数total, page number, page size和recode我们分别来给它去做一个设置那么我们从这个里面去拿到一个什么呢total
[12:40] 那么要注意的total这个类型它是一个run类型那么我们在我们配置info中需要它是个int类型我们需要给它做一个处理那就这么来处理run value of然后点int做一个int第一个参数是它第二个参数是否配置第三个参数配置set第四个参数那就是我们的这个recode就是我们的数据点get什么呢recode这样的话我们是不是就拿到一个
[13:11] 是不是我们就去可以返回一个配置info这样的一个对象啊OK这个呢是不是就是我们具体的一个这个实现啊哎OK来看一下那么下面是我们具体一个这个实现类啊具体的这个实现类好那么下面呢我们需要去把这个AD的这个map我们是不是给他去创建出来哎要说明的一点是啊在我们这个讲义中的这个实现啊他并没有啊并没有去
[13:40] 做一个我们的一个倒序的一个排序这个是稍微有点问题的稍微有点问题的就是说这样你查询到的数据它不是最新的数据OK好那么下面我们来看一下这个AD的这个Mapper这个接口那么我们也需要去给它定义一个接口对不对如果没有这个接口的话那么mybattie是没有办法去运行的所以我们需要把这个接口给它去定义出来那么就在这个下面我们创建一个这个包
[14:10] 这样我来创这样创建包创建Mapper包然后我把接口拷过来拷过来拷过来之后我们把简单的去格式做一个整理这样的话就可以了继承我们的baseMapper好然后我们继续往下面看那么下面我们要写一个mybattles的config为什么写它大家还记得吗原因是为我们要配置我们的一个分页的插件ok以及我们的一个Mapper的扫描包好那么我们把这个包也
[14:41] 拷过来把这个包名拷过来然后呢我们进入到我们这个工程里面创建啊这样的一个包创建包啊然后呢我们把这个mybattiesconfig这个类的内容我们也贴过来在config这个下面ok好那么我们来看一下那么现在呢我们是不是就已经做了这样的一个配置对吧好那我接着继续往下面看下面呢我们要编写一个我们的一个
[15:12] Spring Boot的一个配置文件就是obligation这个publish文件那么把这个文件的内容我们也都贴过来都贴过来那么这个里面的内容我相信大家并不陌生并不陌生来看一下那么首先我们可以看到它已经有一个地方已经报错了对吧有个这个位置报错了那就说明我们现在是不是缺少一个mycircle的一个驱动的一个包
[15:41] 这个我可以看到我们可以看到ADI的工具还是比较智能的他发现你缺少这个类那么我们来看一下在我们 AD这个server中我们是不是需要这样的一个依赖对吧那我们把它拷贝过来我们来找一下找一下我们 mycircle的依赖那么 mycircle的依赖我们往上面找在上面肯定有我们找一下那么 mycircle的依赖是在这个位置是不是有那么把它拷贝过来
[16:10] 那么我们拷贝一下到这好这样的话我们就已经有了 MySQL 的一个驱动包然后我们再次打开它里面发现它肯定就不报错了ok 这样就ok 了然后这个是我们的数据库的一个连接然后下面是我们服务的一个扫描包没有问题还是我们 API 包扫描的还是这个包名都是一样的然后我们应用的名称我们把它设置为是
[16:39] double的一个provide的一个ad为了跟我们的房源的一个应用名称做一个区分然后呢下面的一个协议以及端口协议呢是double这个协议没有任何问题但是要注意的是这个端口那么我们之前在我们的房源的这个里面呢我们所设置它的一个
[16:59] 端口是20880要注意是20880那么我们现在在我们这广告的端口中我们设置为是21880这个要设置不一样一定要切记要不然的话就重复了重复了但这样的话就你这工程在本地是跑不起来的因为端口冲突了ok好那么到这里我们这个是不是已经就引入了
[17:24] 我spin boot的一个配置文件对吧那么下面呢我们就要去编写spin boot的一个启动类启动类那么我们把这个拷过来那么这个启动类呢我们就在这个server这个包下面我们去做一个创建那么是在这个包下面创建一个这个ad double的一个provider那么我们把这个代码呢做一个格式化OK那么这样的话呢我们是不是就可以做一个启动了那么我们点击这个运行启动走
[17:54] 我们看一下它是否能够正常的启动起来那么ok那么等待它启动那么我把视频先暂停一下好我们来看一下在启动的时候报错了报了这样的一个错误就是说我找不到一个ad server实现类那么我们来看一下是不是我们刚刚写的一个代码有点问题我们打开来看一下在这个里面我们是不是缺少了一个Service的一个注解注意是谁是我们sprint的注解对吧
[18:24] 因为我们最终的是要把它去加载到Spring的容器中的OK那么我们再次做一个启动走那么我们依然的把视频的暂停一下好那么我们现在看到了它已经正常的就启动起来了那么下面我们去我们的注册中心我们看一下是否有服务去注册到我们的注册中心我们去找一下那么搜索走那么会发现是不是已经有一个服务是不是注册到我们的注册中心去了
[18:53] 那么它的端口是不是就是21880是不是就刚刚我们所配置这个21880OK那么到这里我们这个服务是不是就搞定了对吧OK我们这个double的服务就实现完成了OK好那么关于我们这个实现这个查询广告的这个接口也就是我们这个double这个服务我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 和 Dubbo 的广告管理服务的开发过程，包括项目结构、实体类、接口、服务实现、MyBatis 配置及 Dubbo 服务注册。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 IntelliJ IDEA 中的项目结构，当前选中模块为 `itcast-haoke-manage-dubbo-server`。
- 显示 `pom.xml` 文件内容，包含父模块信息和依赖配置：
  ```xml
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <parent>
      <artifactId>itcast-haoke-manage</artifactId>
      <groupId>cn.itcast.haoke.manage</groupId>
      <version>1.0-SNAPSHOT</version>
  </parent>
  <modelVersion>4.0.0</modelVersion>
  <artifactId>itcast-haoke-manage-dubbo-server</artifactId>
  <packaging>pom</packaging>
  <modules>
      <module>itcast-haoke-manage-dubbo-server-house-resources</module>
      <module>itcast-haoke-manage-dubbo-server-generator</module>
      <module>itcast-haoke-manage-dubbo-server-common</module>
  </modules>
  <dependencies>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter</artifactId>
      </dependency>
  </dependencies>
  ```

画面 2：
- 选中 `itcast-haoke-manage-dubbo-server-ad-interface` 模块。
- 显示该模块的 `pom.xml` 文件内容：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <project xmlns="http://maven.apache.org/POM/4.0.0"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <parent>
          <artifactId>itcast-haoke-manage-dubbo-server-ad</artifactId>
          <groupId>cn.itcast.haoke.manage</groupId>
          <version>1.0-SNAPSHOT</version>
      </parent>
      <modelVersion>4.0.0</modelVersion>
      <artifactId>itcast-haoke-manage-dubbo-server-ad-interface</artifactId>
  </project>
  ```

画面 3：
- 显示 PDF 文档《讲义.pdf》的第 24 页，内容为 `Ad` 实体类的 Java 代码。
- 代码内容：
  ```java
  package cn.itcast.haoke.dubbo.server.pojo;
  import com.baomidou.mybatisplus.annotation.IdType;
  import com.baomidou.mybatisplus.annotation.TableId;
  import com.baomidou.mybatisplus.annotation.TableName;
  import lombok.Data;
  import lombok.experimental.Accessors;
  @Data
  @Accessors(chain = true)
  @TableName("tb_ad")
  public class Ad extends BasePojo {
      @TableId(value = "id", type = IdType.AUTO)
      private long id;
      //广告类型
      private Integer type;
      //描述
      private String title;
      //图片URL地址
      private String url;
  }
  ```

画面 4：
- 显示 `Ad.java` 文件内容，与画面 3 代码一致，但注释更完整。

画面 5：
- 显示 `PageInfo` 类的 Java 代码，位于 `itcast-haoke-manage-dubbo-server-house-resources` 模块。
- 代码内容：
  ```java
  import java.util.Collections;
  import java.util.List;
  @Data
  @AllArgsConstructor
  public class PageInfo<T> implements java.io.Serializable {
      private static final long serialVersionUID = -2105385778778117877L;
      //总条数
      private Integer total;
      //当前页
      private Integer pageNum;
      //一页显示的大小
      private Integer pageSize;
  }
  ```

画面 6：
- 显示 `ApiAdService.java` 文件内容，定义了分页查询广告数据的接口。
- 代码内容：
  ```java
  package cn.itcast.haoke.dubbo.server.api;
  import cn.itcast.haoke.dubbo.server.pojo.Ad;
  import cn.itcast.haoke.dubbo.server.vo.PageInfo;
  public interface ApiAdService {
      /**
       * 分页查询广告数据
       */
      PageInfo<Ad> queryAdList(Integer type, Integer page, Integer pageSize);
  }
  ```

画面 7：
- 显示 `AdServiceImpl.java` 文件，正在编写实现类。
- 代码内容：
  ```java
  package cn.itcast.haoke.dubbo.server.Service.impl;
  public class AdServiceImpl extends BaseServiceImpl<Ad> {
  ```

画面 8：
- 显示 `AdServiceImpl.java` 文件，正在编写 `queryAdList` 方法。
- 代码内容：
  ```java
  import cn.itcast.haoke.dubbo.server.Service.BaseServiceImpl;
  import cn.itcast.haoke.dubbo.server.vo.PageInfo;
  import javax.management.Query;
  public class AdServiceImpl extends BaseServiceImpl<Ad> implements AdService {
      @Override
      public PageInfo<Ad> queryAdList(Ad ad, Integer page, Integer pageSize) {
          Query query = new Query();
          return super.queryPageList(query, page, pageSize);
      }
  }
  ```

画面 9：
- 显示 `AdServiceImpl.java` 文件，正在使用 `QueryWrapper`。
- 代码内容：
  ```java
  import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
  QueryWrapper<Ad> queryWrapper = new QueryWrapper<>();
  return super.queryPageList(queryWrapper, page, pageSize);
  ```

画面 10：
- 显示 PDF 文档《讲义.pdf》的第 25 页，内容为“3.3.8、创建AdMapper接口”。
- 代码内容：
  ```java
  package cn.itcast.haoke.dubbo.server.Mapper;
  import cn.itcast.haoke.dubbo.server.pojo.Ad;
  import com.baomidou.mybatisplus.core.Mapper.BaseMapper;
  public interface AdMapper extends BaseMapper<Ad> {
  }
  ```

画面 11：
- 显示 `MybatisConfig.java` 文件，正在创建 `PaginationInterceptor`。
- 代码内容：
  ```java
  package cn.itcast.haoke.dubbo.server.config;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.context.annotation.Bean;
  @Configuration
  public class MybatisConfig {
      @Bean
      public PaginationInterceptor paginationInterceptor() {
          return new PaginationInterceptor();
      }
  }
  ```

画面 12：
- 显示 `application.properties` 文件内容，配置 Dubbo 服务。
- 代码内容：
  ```properties
  # Spring boot application
  spring.application.name = itcast-haoke-manage-dubbo-server-ad
  # 数据库
  spring.datasource.driver-class-name=com.mysql.jdbc.Driver
  spring.datasource.url=jdbc:mysql://172.16.55.185:3306/haoke?useUnicode=true&characterEncoding=utf8&autoReconnect=true&failOverReadOnly=false&maxReconnects=10
  spring.datasource.username=root
  spring.datasource.password=root
  # 服务的扫描包
  dubbo.scan.basePackages = cn.itcast.haoke.dubbo.server.api
  # 应用名称
  dubbo.application.name = dubbo-provider-ad
  # 协议及端口
  dubbo.protocol.name = dubbo
  dubbo.protocol.port = 21880
  # zk注册中心
  dubbo.registry.address = ZooKeeper://172.16.55.185:2181
  dubbo.registry.client = zkclient
  ```

画面 13：
- 显示 `AdDubboProvider.java` 文件内容，启动 Dubbo 服务。
- 代码内容：
  ```java
  package cn.itcast.haoke.dubbo.server;
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  @SpringBootApplication
  public class AdDubboProvider {
      public static void main(String[] args) {
          new SpringApplicationBuilder(AdDubboProvider.class)
                  .web(WebApplicationType.NONE) // Web 服务类型
                  .run(args);
      }
  }
  ```

画面 14：
- 显示 PDF 文档《讲义.pdf》的第 4 页，内容为“3.3. 实现查询接口（dubbo服务）”。
- 代码内容：
  ```markdown
  3.3.1、分析
  - 首页的轮播广告，属于网站广告，不能只是开发一个功能而是要开发全站广告功能
  - 实现独立的dubbo服务，便于后期的扩展和维护
  3.3.2、创建common工程
  创建itcast-haoke-manage-dubbo-server-common工程，将BasePojo、BaseServiceImpl移动至

