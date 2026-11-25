---
title: [ARC-542] 离线优先（PWA）的调试与验收体系如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-542：离线优先调试与验收体系
**答**:
- 离线场景矩阵复杂（在线/断网/弱网/恢复 × 读/写/冲突），必须体系化验收而非手工点点。
- 自动化验收：Playwright 网络条件模拟（offline/slow 3G/恢复）跑场景矩阵断言（断网可读/写操作入队/恢复后重放成功/冲突提示），关键协议断言（幂等键/去重/补拉 seq ARC-374/389）。
- 调试工具：离线状态面板（队列内容可视化：pending 操作列表 + 重试次数 + 冲突状态）、SW 调试（Bypass SW 开关快速对比在线行为）、存储查看器（IndexedDB 数据与 dirty 标记检查，ARC-541 同思路）。
- 真机专项：真实弱网与飞行模式（模拟器不可信）、后台恢复时序（切后台/回前台的数据重放时机）、多 Tab 离线写冲突。
- 指标验收：离线可用率（断网下核心功能可完成率）、恢复同步成功率、冲突率——作为离线架构的质量指标持续监控。
```javascript
// Playwright 离线矩阵
for (const scene of [['online','read'], ['offline','write'], ['restore','sync']]) {
  test(`离线矩阵 ${scene}`, async ({ page, context }) => {
    await page.goto('/notes');
    if (scene[0] === 'offline') await context.setOffline(true);
    await page.click('#new-note'); await page.fill('#editor', 'draft');
    await page.click('#save');
    expect(await page.locator('.pending-badge')).toContainText('1');  // 入队
    if (scene[0] === 'restore') {
      await context.setOffline(false);
      await expect(page.locator('.synced-badge')).toBeVisible({ timeout: 10000 }); // 重放成功
    }
  });
}
```
