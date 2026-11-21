/**
 * WorkflowContract —— 工作流模块契约。
 * 节点注册表、Graph DSL、端口类型。前端画布与后端引擎共用同一份定义。
 */

export type PortType = 'trigger' | 'data' | 'record' | 'schema' | 'condition' | 'page' | 'any';

export interface PortDef {
  name: string;
  type: PortType;
}

export type NodeCategory = 'trigger' | 'source' | 'transform' | 'logic' | 'ui' | 'action' | 'script' | 'ai';

/** 节点声明：仅描述契约（端口/类别），执行逻辑不在此处，仅后端运行时有。 */
export interface NodeContract {
  type: string;
  category: NodeCategory;
  label: string;
  version: number;
  deprecated?: boolean;
  inputs: PortDef[];
  outputs: PortDef[];
}

export interface GraphNode {
  id: string;
  type: string;
  params: Record<string, unknown>;
  /** 画布坐标，保存后用于还原布局（可选，旧数据无此字段时回退 0,0） */
  position?: { x: number; y: number };
}

export interface GraphEdge {
  id: string;
  from: string;
  fromPort: string;
  to: string;
  toPort: string;
}

export interface WorkflowGraph {
  id?: string;
  name: string;
  version: number;
  nodes: GraphNode[];
  edges: GraphEdge[];
}
