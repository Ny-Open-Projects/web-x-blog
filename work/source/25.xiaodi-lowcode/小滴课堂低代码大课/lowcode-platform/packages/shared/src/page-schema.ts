/**
 * PageSchema —— 平台核心契约。
 * 页面即一份 JSON：渲染端照此渲染，工作流 UI 发射节点也产出此结构。
 * 全平台（编辑器 / 工作流 / 渲染端）共用，禁止在任一端私自加字段（破坏性变更走版本化）。
 */

export type ComponentType =
  | 'input' | 'textarea' | 'select' | 'radio' | 'checkbox'
  | 'button' | 'form' | 'grid' | 'text' | 'image' | 'container'
  | (string & {}); // 允许平台扩展自定义组件

export interface ComponentOption {
  label?: string;
  placeholder?: string;
  required?: boolean;
  defaultValue?: unknown;
  dataSource?: { type: 'static' | 'api' | 'workflow'; ref?: string };
  [key: string]: unknown;
}

export interface ComponentNode {
  id: string;
  type: ComponentType;
  options: ComponentOption;
  children?: ComponentNode[];
}

export interface PageSchema {
  version: number;
  title: string;
  nodes: ComponentNode[];
  meta?: Record<string, unknown>;
}
