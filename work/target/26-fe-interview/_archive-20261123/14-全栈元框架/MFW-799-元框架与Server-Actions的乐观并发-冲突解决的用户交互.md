---
title: [MFW-799] 乐观锁冲突的用户交互
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-799：乐观锁冲突的用户交互

**答**:
- 冲突解决的 UX 设计（RBL-782 冲突处理的 UI 层）：1) **通知 + 重新加载**（「数据已被他人修改」→ 提供刷新按钮——用户选择：保留我的编辑 or 使用最新数据；2) **diff 展示**（我的编辑 vs 他人编辑的并排 diff——用户看到冲突点（哪些字段不同）；3) **自动合并**（非冲突字段自动合并 + 冲突字段标红——git merge 的 UX 版（同字段不同值 = 冲突；不同字段 = 自动合并）；4) **覆盖选项**（「使用我的版本」——覆盖他人编辑（危险——需二次确认）。
- 冲突的交互层次：轻冲突（不同字段——自动合并无感）→ 中冲突（同字段不同值——diff 展示让用户选）→ 重冲突（结构变化——全量刷新）；「冲突的分级 UX」与「冲突的严重性」匹配。
- 追问钩子：为什么「自动合并不同字段」是乐观锁冲突 UX 的优化方向？——两个用户编辑同一条目的不同字段（A 改 name、B 改 age）→ 乐观锁报冲突 → 但实际无冲突（不同字段可安全合并）；「字段级合并」优于「整条拒绝」：减少不必要的冲突提示（用户只在意自己编辑的字段）；字段级冲突检测（zod schema 逐字段——RBL-791 双端验证的冲突维度）需要 diff 算法（旧值 × 我的值 × 他人值的三方比较——git merge 的三方合并）。

```tsx
'use client';
function ProfileEditor({ user }) {
  const [conflict, setConflict] = useState(null);
  return (
    <div>
      <form action={async (fd) => {
        const result = await updateProfile(user.id, data, user.version);
        if (result.conflict) {
          setConflict(result.currentData);               // 显示冲突 UI
        }
      }}>
        {/* 表单字段 */}
      </form>
      {conflict && (
        <ConflictDialog
          myChanges={user}                                // 我的编辑
          theirChanges={conflict}                         // 他人的修改
          onMerge={(merged) => {
            // 自动合并：非冲突字段合并 + 冲突字段用户选择
            updateProfile(user.id, merged, conflict.version);
            setConflict(null);
          }}
          onOverride={() => {
            // 覆盖：使用我的版本（二次确认后）
            updateProfile(user.id, data, conflict.version);   // 用最新 version 覆盖
            setConflict(null);
          }}
        />
      )}
    </div>
  );
}
// 三方合并：base(user.version 时的值) + mine + theirs
function mergeFields(base, mine, theirs) {
  const merged = {};
  for (const key of Object.keys(base)) {
    if (mine[key] !== base[key] && theirs[key] !== base[key] && mine[key] !== theirs[key])
      merged[key] = 'CONFLICT';                           // 同字段不同值 → 冲突
    else if (mine[key] !== base[key]) merged[key] = mine[key];     // 我改的
    else if (theirs[key] !== base[key]) merged[key] = theirs[key]; // 他人改的
    else merged[key] = base[key];                        // 未改
  }
  return merged;
}
```
