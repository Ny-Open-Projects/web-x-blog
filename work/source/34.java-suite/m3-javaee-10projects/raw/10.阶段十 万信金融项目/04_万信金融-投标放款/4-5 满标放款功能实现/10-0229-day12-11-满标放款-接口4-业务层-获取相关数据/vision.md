# 画面线理解：day12-11-满标放款-接口4-业务层-获取相关数据

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-11-满标放款-接口4-业务层-获取相关数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:00, 01:33, 02:30, 03:12, 04:26, 06:02, 09:43, 10:23, 11:01, 11:49, 13:23, 14:04, 14:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:52:56

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中，为“还款服务”模块创建并实现一个服务接口，包括定义接口、创建实现类、编写业务逻辑代码，并涉及 MyBatis Mapper 文件的配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了课程 PPT 页面，内容为“在 mapper 包中新建一个映射配置文件 ReceivablePlanMapper.xml”。
- 同时显示了 MyBatis 的 XML 映射文件模板，内容为：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN"
      "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
  <mapper namespace="cn.itcast.wanxing2p.repayment.mapper.ReceivablePlanMapper">
  </mapper>
  ```

画面 2：
- 展示了项目结构，其中 `mapper` 包下已存在 `ReceivablePlanMapper.xml` 文件，但尚未创建 `ReceivablePlanMapper` 接口。

画面 3：
- 展示了多个窗口，包括 IDEA、WPS、ECLog Professional 等，暗示可能在调试或查看日志。
- 同时显示了 `RepaymentService` 接口中的方法定义：
  ```java
  @Transactional(rollbackFor = Exception.class)
  public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
      final ProjectDTO project = projectWithTendersDTO.getProject();
      //return null;
  }
  ```

画面 4：
- 展示了 `ProjectWithTendersDTO` 类的源码，其中包含字段：
  ```java
  private ProjectDTO project;
  private List<TenderDTO> tenders;
  private BigDecimal commissionInvestorAnnualRate;
  private BigDecimal commissionBorrowerAnnualRate;
  ```

画面 5：
- 展示了 `RepaymentService` 接口的定义，其中包含方法：
  ```java
  public interface RepaymentService {
      /**
       * 滚动还款
       * @param projectWithTendersDTO
       * @return
       */
      String startRepayment(ProjectWithTendersDTO projectWithTendersDTO);
  }
  ```

画面 6：
- 展示了 `RepaymentServiceImpl` 类的创建过程，该类继承自 `ServiceImpl`。

画面 7：
- 展示了 `RepaymentServiceImpl` 类的代码，其中包含方法：
  ```java
  @Service
  @Slf4j
  public class RepaymentServiceImpl implements RepaymentService {
      @Override
      public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
          return null;
      }
  }
  ```

画面 8：
- 展示了 `RepaymentServiceImpl` 类的代码，其中包含方法：
  ```java
  @Override
  public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
      //1.生成借款人还款计划
      //1.1 获取标的
      ProjectDTO projectDTO = projectWithTendersDTO.getProject();
      //1.2 获取标的的投标信息
      List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
      //1.3 计算还款的月数
      //1.4 还款方式，只针对等额本息
      //1.5 生成还款计划
  }
  ```

画面 9：
- 展示了 `RepaymentServiceImpl` 类的代码，其中包含方法：
  ```java
  @Override
  public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
      //1.生成借款人还款计划
      //1.1 获取标的
      ProjectDTO projectDTO = projectWithTendersDTO.getProject();
      //1.2 获取标的的投标信息
      List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
      //1.3 计算还款的月数
      Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
      Integer months = cell.intValue();
      //1.4 还款方式，只针对等额本息
      //1.5 生成还款计划
  }
  ```

画面 10：
- 展示了 `RepaymentServiceImpl` 类的代码，其中包含方法：
  ```java
  @Override
  public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
      //1.生成借款人还款计划
      //1.1 获取标的
      ProjectDTO projectDTO = projectWithTendersDTO.getProject();
      //1.2 获取标的的投标信息
      List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
      //1.3 计算还款的月数
      Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
      Integer months = cell.intValue();
      //1.4 还款方式，只针对等额本息
      //1.5 生成还款计划
  }
  ```

画面 11：
- 展示了 `RepaymentServiceImpl` 类的代码，其中包含方法：
  ```java
  @Override
  public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
      //1.生成借款人还款计划
      //1.1 获取标的
      ProjectDTO projectDTO = projectWithTendersDTO.getProject();
      //1.2 获取标的的投标信息
      List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
      //1.3 计算还款的月数
      Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
      Integer months = cell.intValue();
      //1.4 还款方式，只针对等额本息
      //1.5 生成还款计划
  }
  ```

画面 12：
- 展示了 `RepaymentServiceImpl` 类的代码，其中包含方法：
  ```java
  @Override
  public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
      //1.生成借款人还款计划
      //1.1 获取标的
      ProjectDTO projectDTO = projectWithTendersDTO.getProject();
      //1.2 获取标的的投标信息
      List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
      //1.3 计算还款的月数
      Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
      Integer months = cell.intValue();
      //1.4 还款方式，只针对等额本息
      //1.5 生成还款计划
  }
  ```

画面 13：
- 展示了 `RepaymentServiceImpl` 类的代码，其中包含方法：
  ```java
  @Override
  public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
      //1.生成借款人还款计划
      //1.1 获取标的
      ProjectDTO projectDTO = projectWithTendersDTO.getProject();
      //1.2 获取标的的投标信息
      List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
      //1.3 计算还款的月数
      Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
      Integer months = cell.intValue();
      //1.4 还款方式，只针对等额本息
      //1.5 生成还款计划
  }
  ```

画面 14：
- 展示了 `RepaymentServiceImpl` 类的代码，其中包含方法：
  ```java
  @Override
  public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
      //1.生成借款人还款计划
      //1.1 获取标的
      ProjectDTO projectDTO = projectWithTendersDTO.getProject();
      //1.2 获取标的的投标信息
      List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
      //1.3 计算还款的月数
      Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
      Integer months = cell.intValue();
      //1.4 还款方式，只针对等额本息
      //1.5 生成还款计划
  }
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文第 2 点中各画面的代码内容。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- 画面 1 中的 PPT 标题为“在 mapper 包中新建一个映射配置文件 ReceivablePlanMapper.xml”。
- 画面 3 中的 PPT 标题为“万能项目 第4章 滚动还款服务”，并展示了多个窗口，但未提供架构图或流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
