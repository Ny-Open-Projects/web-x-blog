---
title: [SCN-112] 三个业务方对同一个组件（如上传器）的 API 设计各执一词，如何决策？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-112：三个业务方对同一个组件（如上传器）的 API 设计各执一词，如何决策？
**答**：
- 用轻量 RFC 流程替代口头扯皮：提案文档（API 草案 + 各方用例 + 破坏性变更说明）发到团队仓库，明确组件 owner 为决策人并给截止时间。
- 评审聚焦"用例反推 API"而不是口味之争：把三方场景列成表格，逐个验证 API 是否覆盖，覆盖不了的才是需要讨论的点。
- 技术上用"受控/非受控双模式 + 插槽"吸收多数差异，避免为了个性化无限加 props。

```typescript
// RFC 落地示例：上传器 API —— 受控与非受控双模式 + 插槽吸收差异
interface UploaderProps {
  /** 非受控：内部管理文件列表（简单业务方开箱即用） */
  defaultFileList?: FileItem[];
  /** 受控：列表完全由外部管理（需要深度定制的业务方） */
  fileList?: FileItem[];
  onChange?: (files: FileItem[]) => void;
  maxCount?: number;
  accept?: string;
  /** 个性化展示用插槽吸收，而不是无限加 props */
  renderItem?: (file: FileItem) => ReactNode;
}

export function Uploader({ defaultFileList, fileList, onChange, renderItem, ...rest }: UploaderProps) {
  const [inner, setInner] = useState<FileItem[]>(defaultFileList ?? []);
  const files = fileList ?? inner;                       // 受控优先，非受控兜底
  const update = (next: FileItem[]) => {
    if (fileList === undefined) setInner(next);          // 非受控才写内部状态
    onChange?.(next);
  };
  return <DropZone files={files} onFilesChange={update} renderItem={renderItem} {...rest} />;
}
```
