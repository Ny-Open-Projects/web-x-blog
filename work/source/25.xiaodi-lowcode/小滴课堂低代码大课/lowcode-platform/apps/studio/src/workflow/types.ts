import type { NodeContract } from '@lowcode/shared';

export interface RFNodeData {
  contract: NodeContract;
  params: Record<string, unknown>;
}

export const WF_NODE_TYPE = 'wf';
