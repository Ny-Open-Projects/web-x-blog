# 画面线理解：16.用户资料之保存更新

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\16.用户资料之保存更新_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:17, 00:31, 00:51, 01:20, 02:15, 02:40, 02:57, 03:31, 03:43, 04:02, 04:43, 04:58, 05:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:33:55

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
