import type { NodeContract } from '@lowcode/shared';

export function Palette({
  contracts,
  onAdd,
}: {
  contracts: NodeContract[];
  onAdd: (c: NodeContract) => void;
}) {
  return (
    <aside
      style={{
        width: 210,
        borderRight: '1px solid #eee',
        padding: 12,
        overflowY: 'auto',
        background: '#fafafa',
      }}
    >
      <h3 style={{ margin: '0 0 8px', fontSize: 13 }}>节点库</h3>
      {contracts.length === 0 && <div style={{ color: '#999', fontSize: 12 }}>加载中…</div>}
      {contracts.map((c) => (
        <button
          key={c.type}
          onClick={() => onAdd(c)}
          title={c.type}
          style={{
            display: 'block',
            width: '100%',
            marginBottom: 6,
            padding: '6px 8px',
            textAlign: 'left',
            cursor: 'pointer',
            border: '1px solid #d9d9d9',
            borderRadius: 6,
            background: '#fff',
          }}
        >
          <div>{c.label}</div>
          <code style={{ fontSize: 10, color: '#888' }}>{c.type}</code>
        </button>
      ))}
    </aside>
  );
}
