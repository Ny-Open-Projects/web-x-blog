# 16.用户资料之保存更新

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\16.用户资料之保存更新_【海量资源尽在 666java.com】.mp4
- 时长 5分16秒（音频 316s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下这个保存修改这个其实就比较简单了那我们可以通过我们的这个user info vo对象直接接收我们的一些参数啊就可以了好那么接下来呢我们把这个Controller呢Controller我们就这个方法好那我们还是去找到我们这个us的Controller然后呢下面呢把这个方法呢写过来然后呢我们去创建我们的这个方法当然了我们
[00:28] 也可以直接来拷贝啊那么我们来拷过来吧那么来看一下这个方法的一个编写那么首先呢我们先来看一下我们的Controller在我们的Controller中啊那么我们呃就可以通过我们这个Udeinfo的一个VO去做一个接收我们的一个数据呃因为我们的这个接口啊来看一下那么这个接口呢是保存啊在这他所提交的呢呃首先他是一个put这样的一个请求
[00:56] 然后呢所提交的一些数据呢是这样的数据那么显然这个数据结构跟我们响应的数据结构呢是一样的并且它是一个这个阶层类型的所以说呢我们在这个位置就可以通过request body直接去通过对象去做一个接收然后呢我们就调用我们这个方法啊就OK了并且这个位置要设置成是一个put mapping然后呢我们在这个里面呢就需要去设置我们的一些
[01:22] 需要去修改的一些字段那我们去做一些这个设置啊一些细节呢大家需要注意一下比如说像我们这个性别呢我们需要设置是我们的一个美角然后呢下面的这个呢还有是我们的这个婚姻的一个状态然后如果等于一呢就设置为已婚如果不是的话就设置为未婚啊然后呢我们这个收入的话需要把这个key给它替换掉所以说这些保存的都一些细节内容呢大家需要注意一下
[01:51] 然后呢在我们原有的这个user info Service中啊我们去扩展一个更新的这个方法那么之前呢我们是没有这个方法的那我们就来扩展一下那我们就扩展一下这个方法那么把这个方法呢就创建出来
[02:09] 那我们来看一下这个是怎么样去做一个扩展那么我们是不是就可以通过直接这个优惠麦有运风map做一个update就可以了对吧然后呢有人啊音符啊去把它保存进去那么我们需要注意的是呢对啊那么需要我们需要注意的是呢我们要传递什么呢是不是传递我们的一个这个条件呢因为我们这个更新啊并不是根据组件更新啊所以我们需要写一个
[02:37] 这个叫做什么呢queryquerywrap对象然后呢这个叫eo.info然后呢querywrap等于new一个querywrap对象然后呢我们把这个呢传递给他第二个参数好然后呢我们需要设置一个条件那么这个条件呢我们就需要设置他的eq相等谁呢就是我们eo.下滑线id条件就是我们的用户id了
[03:06] 那么有的info点get U的ID这个就是我们的一个条件根据这个条件去做一个更新那么它的返回值就是一个update那么这样我们就直接就把它拿到下面来到这它是不是大于0它是不是大于0那么如果要是大于0的话那么就代表着什么我们更新的就成功了是不是好那么这个就OK了那么这个是不是也就OK了
[03:35] 好那么接下来呢把这个server重启一下那我们再来做一个测试好那么接下来呢我们就来测试一下那么我们先来去点击它去做一个查询然后呢你比如说呢我们设置我们的一个性别把它设置为女性用户然后点击这个确认它应该就保存了然后呢我们再退出一下当然我们为了去测试呢我们就直接把这个应用退出然后呢我们再去打开我们的应用重新
[04:05] 来登录一下我们做一个测试然后我们去点击一下他然后026868然后我们获取验证码123456好然后我们就进入到我的页面中然后点击他那么其实可以看到查询的性别是不是就是女性了对吧然后还有我们的一些学历
[04:33] 这种修改啊这个这个好像我们这个前端啊没有去做这一块啊然后比如说这个婚姻状态啊这个这几个好像都没做然后呢这个也没做在性别做了然后呢日期我这个生日生日呢也做了比如说我们设置成9月30号我们去改一下啊然后呢我们再点击再进入来看一下啊9月30号这个呢是不是就改了对吧好那么这个呢就是我们的一个
[05:00] 这个用户资料的一个保存那么其实对于我们服务端而言我们就非常的简单了对吧那我们就直接去做修改就可以了OK好那么关于我们的这个保存修改呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中实现用户资料的保存与修改功能，包括 Controller、Service 层代码编写、MyBatis 查询与更新操作，以及通过 Mock 服务模拟前端数据交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 Typora 文档中“5.2. 保存修改”章节，聚焦于 UsersController 的代码。
- 代码内容：
  ```java
  @PutMapping
  public ResponseEntity<Void> updateUserInfo(@RequestBody UserInfoVo userInfoVo){
      Boolean bool = this.userService.updateUserInfo(userInfoVo);
      if(bool){
          return ResponseEntity.ok(null);
      } catch (Exception e) {
          e.printStackTrace();
      }
      return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }
  ```

画面 2：
- 展示 IntelliJ IDEA 中 UserService.java 文件的代码，重点在 userInfoVo 对象的属性赋值。
- 代码内容：
  ```java
  UserInfoVo userInfoVo = new UserInfoVo();
  userInfoVo.setAge(userInfo.getAge() != null ? userInfo.getAge().toString() : null);
  userInfoVo.setAvatar(userInfo.getLogo());
  userInfoVo.setBirthday(userInfo.getBirthday());
  userInfoVo.setCity(userInfo.getCity());
  userInfoVo.setEducation(userInfo.getEdu());
  userInfoVo.setGender(userInfo.getSex().name().toLowerCase());
  userInfoVo.setIncome(userInfo.getIncome() + "K");
  userInfoVo.setMarriage(StringUtils.equals(userInfo.getMarriage(), "已婚") ? 1 : 0);
  userInfoVo.setNickname(userInfo.getNickName());
  userInfoVo.setProfession(userInfo.getIndustry());
  return userInfoVo;
  ```

画面 3：
- 展示 Typora 文档中 UserService 的代码部分，与画面 1 类似，但聚焦于 Service 层。
- 代码内容：
  ```java
  public Boolean updateUserInfo(UserInfoVo userInfoVo) {
      User user = UserThreadLocal.get();
      UserInfo userInfo = new UserInfo();
      userInfo.setUserId(user.getId());
      userInfo.setAge(Integer.valueOf(userInfoVo.getAge()));
      userInfo.setSex(StringUtils.equalsIgnoreCase(userInfoVo.getGender(), "man") ? SexEnum.MAN : SexEnum.WOMAN);
      userInfo.setBirthday(userInfoVo.getBirthday());
      userInfo.setCity(userInfoVo.getCity());
      userInfo.setEducation(userInfoVo.getEducation());
      userInfo.setIncome(StringUtils.replaceAll(userInfoVo.getIncome(), "K", ""));
      userInfo.setMarriage(userInfoVo.getMarriage());
      userInfo.setProfession(userInfoVo.getProfession());
      userInfo.setNickname(userInfoVo.getNickname());
      userInfo.setNickName(userInfoVo.getNickName());
      userInfo.setProfession(userInfoVo.getProfession());
      return this.userInfoService.updateUserInfoByUserId(userInfo);
  }
  ```

画面 4：
- 展示 MockBox 的 Mock 接口配置页面，用于模拟用户资料保存接口。
- 页面信息：
  - 接口名称：用户资料-保存
  - 接口路径：/users
  - Mock 地址：https://mock.boxuegu.com/mock/164/users
  - Headers：Content-Type: application/json

画面 5：
- 展示 UserService.java 代码，重点在 updateUserInfo 方法的实现。
- 代码内容：
  ```java
  public Boolean updateUserInfo(UserInfoVo userInfoVo) {
      User user = UserThreadLocal.get();
      UserInfo userInfo = new UserInfo();
      userInfo.setUserId(user.getId());
      userInfo.setAge(Integer.valueOf(userInfoVo.getAge()));
      userInfo.setSex(StringUtils.equalsIgnoreCase(userInfoVo.getGender(), "man") ? SexEnum.MAN : SexEnum.WOMAN);
      userInfo.setBirthday(userInfoVo.getBirthday());
      userInfo.setCity(userInfoVo.getCity());
      userInfo.setEducation(userInfoVo.getEducation());
      userInfo.setIncome(StringUtils.replaceAll(userInfoVo.getIncome(), "K", ""));
      userInfo.setMarriage(userInfoVo.getMarriage());
      userInfo.setProfession(userInfoVo.getProfession());
      userInfo.setNickname(userInfoVo.getNickname());
      userInfo.setNickName(userInfoVo.getNickName());
      userInfo.setProfession(userInfoVo.getProfession());
      return this.userInfoService.updateUserInfoByUserId(userInfo);
  }
  ```

画面 6：
- 展示 UserService.java 代码，光标位于 queryUserInfoById 方法，显示了 MyBatis 的 Mapper 接口。
- 代码内容：
  ```java
  public UserInfo queryUserInfoById(Long id) {
      return this.userInfoMapper.selectById(id);
  }
  ```

画面 7：
- 展示 UserService.java 代码，光标位于 queryUserInfoList 方法，显示了 MyBatis 的 Mapper 接口。
- 代码内容：
  ```java
  public List<UserInfo> queryUserInfoList(QueryWrapper queryWrapper) {
      return this.userInfoMapper.selectList(queryWrapper);
  }
  ```

画面 8：
- 展示 UserService.java 代码，光标位于 update 方法，显示了 MyBatis 的 Mapper 接口。
- 代码内容：
  ```java
  public Boolean updateUserInfo(UserInfo userInfo, QueryWrapper queryWrapper) {
      this.userInfoMapper.update(userInfo, queryWrapper);
      return null;
  }
  ```

画面 9：
- 展示 UserService.java 代码，光标位于 queryUserInfoById 方法，显示了 MyBatis 的 Mapper 接口。
- 代码内容：
  ```java
  @Autowired
  private UserInfoMapper userInfoMapper;

  public UserInfo queryUserInfoById(Long id) {
      return this.userInfoMapper.selectById(id);
  }

  public List<UserInfo> queryUserInfoList(QueryWrapper queryWrapper) {
      return this.userInfoMapper.selectList(queryWrapper);
  }
  ```

画面 10：
- 展示 Genymotion 模拟器界面，显示“编辑资料”页面，用户正在编辑个人资料。
- 页面信息：
  - 标题：编辑资料
  - 内容：昵称 heima，生日 2019-08-01，性别 女，现居城市 北京市北京市城区-朝阳区，学历 本科，月收入 30K

画面 11：
- 展示 Genymotion 模拟器界面，显示“编辑资料”页面，用户正在编辑个人资料。
- 页面信息：
  - 标题：编辑资料
  - 内容：昵称 heima，生日 2019-08-01，性别 女，现居城市 北京市北京市城区-朝阳区，学历 本科，月收入 30K

画面 12：
- 展示 MockBox 的 Mock 接口配置页面，用于模拟用户资料保存接口。
- 页面信息：
  - 接口名称：用户资料-保存
  - 接口路径：/users
  - Mock 地址：https://mock.boxuegu.com/mock/164/users
  - Headers：Content-Type: application/json

画面 13：
- 展示 MockBox 的 Mock 接口配置页面，用于模拟用户资料保存接口。
- 页面信息：
  - 接口名称：用户资料-保存
  - 接口路径：/users
  - Mock 地址：https://mock.boxuegu.com/mock/164/users
  - Headers：Content-Type: application/json

画面 14：
- 展示 Typora 文档中“5.2. 保存修改”章节，聚焦于 UsersController 的代码。
- 代码内容：
  ```java
  @PutMapping
  public ResponseEntity<Void> updateUserInfo(@RequestBody UserInfoVo userInfoVo){
      Boolean bool = this.userService.updateUserInfo(userInfoVo);
      if(bool){
          return ResponseEntity.ok(null);
      } catch (Exception e) {
          e.printStackTrace();
      }
      return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }
  ```

