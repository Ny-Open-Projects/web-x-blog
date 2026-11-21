# 画面线理解：day11-8-用户投标-功能实现7

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-8-用户投标-功能实现7_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:35, 01:46, 02:48, 03:32, 04:36, 05:35, 06:06, 07:09, 07:37, 09:36, 10:22, 11:04, 11:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:35:47

1) 这一组画面整体在讲什么（一句话）：
演示如何在交易服务中，根据投标状态更新项目信息，包括计算利息、转换DTO对象、校验金额并抛出业务异常。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 代码：在 ProjectServiceImpl.java 中，判断投标结果，若为成功则更新项目状态为“已满标”（FULLY），并调用 updateById(project)。
- 代码：BigDecimal remainder = getProjectRemainingAmount(project); if (remainder.compareTo(new BigDecimal(0)) == 0) { project.setProjectStatus(ProjectCode.FULLY.getCode()); updateById(project); }

画面2：
- 代码：else { throw new BusinessException(TransactionErrorCode.E_150113); }

画面3：
- 代码：在 project 变量后，IDE 提示 Project 类的 setter 方法，如 setProjectStatus(String projectStatus)。

画面4：
- 代码：在 project 变量后，IDE 提示 Project 类的 getter 方法，如 getProjectName()。

画面5：
- 代码：project.setRepaymentWay(RepaymentWayCode.FIXED_REPAYMENT.getDesc()); tenderDTO.setProject(convertProjectEntityToDTO(project)); // 封装项目信息

画面6：
- 代码：在 IncomeCalculate.java 中，计算利息的静态方法 getIncomeTotalInterest。
- 代码：public static BigDecimal getIncomeTotalInterest(BigDecimal invest, BigDecimal yearRate, int month) {
    double monthRate = yearRate.doubleValue() / 12;
    BigDecimal totalInterest = new BigDecimal(0);
    for (int i = 1; i <= month; i++) {
        BigDecimal multiply = invest.multiply(new BigDecimal(monthRate));
        BigDecimal sub = multiply.subtract(new BigDecimal(Math.pow(1 + monthRate, month)));
        totalInterest = totalInterest.add(sub);
    }
    return totalInterest;
}

画面7：
- 代码：在 ProjectServiceImpl.java 中，创建 TenderOverviewDTO 列表并遍历，将 Tender 实体转换为 TenderOverviewDTO。
- 代码：List<TenderOverviewDTO> tenderOverviewDTOs = new ArrayList<>(); tenderList.forEach(tender -> {
    TenderOverviewDTO tenderOverviewDTO = new TenderOverviewDTO();
    BeanUtils.copyProperties(tender, tenderOverviewDTO);
    tenderOverviewDTO.setConsumerUsername(CommUtil.hiddenMobile(tender.getConsumerUsername()));
    tenderOverviewDTO.setTenderAmount(tender.getAmount());
    tenderOverviewDTO.setTenderTime(tender.getCreateTime());
    tenderOverviewDTO.setTenderStatus(tender.getStatus());
    tenderOverviewDTO.setTenderId(tender.getId());
    tenderOverviewDTO.setTenderType(tender.getType());
    tenderOverviewDTO.setTenderUserId(tender.getUserId());
    tenderOverviewDTO.setTenderUserName(tender.getUserName());
    tenderOverviewDTO.setTenderUserPhone(tender.getUserPhone());
    tenderOverviewDTO.setTenderUserEmail(tender.getUserEmail());
    tenderOverviewDTO.setTenderUserAddress(tender.getUserAddress());
    tenderOverviewDTO.setTenderUserPostCode(tender.getUserPostCode());
    tenderOverviewDTO.setTenderUserProvince(tender.getUserProvince());
    tenderOverviewDTO.setTenderUserCity(tender.getUserCity());
    tenderOverviewDTO.setTenderUserDistrict(tender.getUserDistrict());
    tenderOverviewDTO.setTenderUserTown(tender.getUserTown());
    tenderOverviewDTO.setTenderUserVillage(tender.getUserVillage());
    tenderOverviewDTO.setTenderUserStreet(tender.getUserStreet());
    tenderOverviewDTO.setTenderUserBuilding(tender.getUserBuilding());
    tenderOverviewDTO.setTenderUserUnit(tender.getUserUnit());
    tenderOverviewDTO.setTenderUserRoom(tender.getUserRoom());
    tenderOverviewDTO.setTenderUserDoor(tender.getUserDoor());
    tenderOverviewDTO.setTenderUserDoorCode(tender.getUserDoorCode());
    tenderOverviewDTO.setTenderUserDoorName(tender.getUserDoorName());
    tenderOverviewDTO.setTenderUserDoorType(tender.getUserDoorType());
    tenderOverviewDTO.setTenderUserDoorStatus(tender.getUserDoorStatus());
    tenderOverviewDTO.setTenderUserDoorLock(tender.getUserDoorLock());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoorLockType());
    tenderOverviewDTO.setTenderUserDoorLockStatus(tender.getUserDoorLockStatus());
    tenderOverviewDTO.setTenderUserDoorLockCode(tender.getUserDoorLockCode());
    tenderOverviewDTO.setTenderUserDoorLockName(tender.getUserDoorLockName());
    tenderOverviewDTO.setTenderUserDoorLockType(tender.getUserDoor
