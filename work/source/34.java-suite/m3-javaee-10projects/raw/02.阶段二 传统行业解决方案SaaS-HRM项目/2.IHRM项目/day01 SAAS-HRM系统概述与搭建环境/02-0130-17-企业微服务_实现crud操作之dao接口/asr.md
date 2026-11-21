# 声音线转写：17-企业微服务：实现crud操作之dao接口

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\17-企业微服务：实现crud操作之dao接口_【海量资源尽在 ubkz.com】.mp4
- 时长：7分40秒（音频 461s）
- 转写：faster-whisper-large-v3 / 语言 zh / 13 段
- 生成时间：2026-10-27 12:49:06

## 逐段转写（教师原声）

[00:03] 实体类创建好了之后呢接下来我们回到企业为服务在这个代码当中首先去完成我们DO层代码的一个编写那打开Java目录下在company创建一个包好了这个包呢我就叫做DO了那咱们现在使用的是SpringData JPA的形式去完成数据库操作那SpringData JPA去写一个DO接口那很简单
[00:35] 很简单简单至极我们只需要去创建一个do接口即可注意这边创建一class这边我们把它创建叫做companydo注意它是一个接口interface那这个接口我们需要去实现两个规范接口实现错了继承一个tense继承两个接口这两个接口第一个呢叫做jpa repository好了它需要提供
[01:07] 这个范形第一个参数指的是你当前的实体类型company第二个指的是你当前主建属性的类型我们主建属性是死菌所以我写一个死菌OK那除了这一个接口之外呢还需要第二个接口第二个接口叫做GPAspecial Cation Excluter
[01:41] 那这个接口呢也需要提供一个范形范形就是说你当前实体类的类型拷过来即可那这样一来我的company do其实就已经都写好了那这个company do我们写好了之后它究竟能不能用呢我们可以写一个简单的测试一起来看一下效果找到泰斯特这个包在泰斯特包下创建一个我们自己的测试类把它放到
[02:12] cn.com.ihrm.cumpany下一个名字呢我们叫做company.do test好了在Spring Boot当中我们要想去完成测试其实比较简单首先ata test首先ata Spring Boot test好了接下来ata run with这些都是一些固定的写法Spring提供的单元测试环境.class好了那接下来
[02:44] at auto where我们注入进来一个company dook接着at testpublic willid test我们一起来试一下这个do里面究竟有没有方法有的朋友始终抱有怀疑态度你写了一个do切口实际上也没写他真的能查询吗那么一起来看一下company do打点他有方法比如说find by id那find by id我们查看一下数据库
[03:19] 我其中有一个ID叫1那我根据ID点get那这样一来就能完成查询并且得到我们company这个对象我们可以打印出来一起来看一下效果究竟能不能用咱们测试一下走这个执行起来稍微有点慢因为它有个编译的过程各位耐心等待一下这边报了一个错误咱们一起来解决它
[04:06] no default contractor for entity company这个company下是不是没有构造方法呀哦抱歉抱歉我这边写了一个all args contractor那还需要配合ata需要给他指定一个无参的吧no args contractor这是无参构造这个是满参嘛因为如果你用满参的话就必须要多写一个无参嘛这个常识啊好了再执行好了耐心等待哎各位来看没问题
[04:45] 已经从数据库里面把数据查印出来封装到我们的对象当中了当了咱们写好的 DO 里面还有很多的方法咱们就不是一个一个给各位去试了我这边简单的和各位来罗列一下DO 打点 C5里面可以传递一个 Company 对象进来传递一个 Company 对象这种我把它注视过来它完成的其实就是保存或更新
[05:24] 那保存和更新的依据就是ID如果对象当中有ID更新如果对象没ID保存OK好了接下来company.do打点delete by id需要传递一个ID参数这个呢见名思义很简单就叫做根据ID删除那接下来呢还有比如说呢我们刚才看过一个叫做find by id根据ID查询
[06:00] 好了那这样一来我们的基本增删改查这些方法就已经都有了当然了除了这玩意儿还有一个方法company do 打点我们叫做find all那find all得到的就是一个粒子集合查询全部OK所以对于这个do来说呢它有很多种方法第一个方法sale需要传递一个对象
[06:29] 第二个方法delete by id传递id根据id删除第三个方法根据id查询翻到代表查询全部但是有一个前提条件我们自己写DAU的时候需要去实现或者需要去继承接口DAU接口继承GPA repository以及GPA special kishin executorOK那第一个里面呢我们需要
[07:06] 范形范形的第一个就是实体类类型好了第二个就是主件类型同样的第二个我们也需要提供一个范形实体类类型OK那这样一来我们的do层代码其实就已经都写好了也比较简单相的位置编写于do接口g乘gpa repositoryg乘gpa special locationexecutor就可以了当然它提供了很多的方法c5 delete find by以及find all
