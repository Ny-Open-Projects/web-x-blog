import { useReactFlow, Handle, Position, type NodeProps } from 'reactflow';
import type { RFNodeData } from './types';
import { ParamEditor, PARAM_SCHEMAS } from './ParamEditor';

export function WorkflowNode({ id, data, selected }: NodeProps<RFNodeData>) {
  const { setNodes } = useReactFlow();
  const { contract, params } = data;
  const schema = PARAM_SCHEMAS[contract.type];

  const updateParam = (key: string, value: unknown) => {
    setNodes((nds) =>
      nds.map((n) =>
        n.id === id ? { ...n, data: { ...n.data, params: { ...n.data.params, [key]: value } } } : n,
      ),
    );
  };

  const commitParams = (raw: string) => {
    try {
      const v = JSON.parse(raw);
      setNodes((nds) => nds.map((n) => (n.id === id ? { ...n, data: { ...n.data, params: v } } : n)));
    } catch {
      /* 忽略非法 JSON，保留原值 */
    }
  };

  return (
    <div
      style={{
        border: `1px solid ${selected ? '#1677ff' : '#d9d9d9'}`,
        borderRadius: 8,
        background: '#fff',
        minWidth: 196,
        fontSize: 12,
        boxShadow: selected ? '0 0 0 2px rgba(22,119,255,.2)' : '0 1px 4px rgba(0,0,0,.08)',
      }}
    >
      <div
        style={{
          padding: '5px 8px',
          background: '#fafafa',
          borderBottom: '1px solid #f0f0f0',
          borderTopLeftRadius: 8,
          borderTopRightRadius: 8,
          fontWeight: 600,
        }}
      >
        {contract.label}
      </div>
      <div style={{ padding: '6px 8px' }}>
        {contract.inputs.map((p) => (
          <div key={p.name} style={{ display: 'flex', alignItems: 'center', gap: 4, lineHeight: '18px' }}>
            <Handle type="target" position={Position.Left} id={p.name} style={{ background: '#1677ff' }} />
            <span>{p.name}</span>
            <em style={{ color: '#999', fontStyle: 'normal' }}>{p.type}</em>
          </div>
        ))}
        {contract.outputs.map((p) => (
          <div key={p.name} style={{ display: 'flex', alignItems: 'center', justifyContent: 'flex-end', gap: 4, lineHeight: '18px' }}>
            <span>{p.name}</span>
            <em style={{ color: '#999', fontStyle: 'normal' }}>{p.type}</em>
            <Handle type="source" position={Position.Right} id={p.name} style={{ background: '#52c41a' }} />
          </div>
        ))}
      </div>
      <div style={{ padding: '6px 8px', borderTop: '1px solid #f0f0f0' }}>
        {schema ? (
          <ParamEditor schema={schema} params={params} onChange={updateParam} />
        ) : (
          <textarea
            defaultValue={JSON.stringify(params)}
            onBlur={(e) => commitParams(e.target.value)}
            rows={2}
            spellCheck={false}
            style={{ width: '100%', fontSize: 10, fontFamily: 'monospace', boxSizing: 'border-box' }}
          />
        )}
      </div>
    </div>
  );
}
