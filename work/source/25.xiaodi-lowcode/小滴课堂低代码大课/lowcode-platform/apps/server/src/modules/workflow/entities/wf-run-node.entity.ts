import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

/** 节点级执行追踪，支持失败重跑与逐步调试。 */
@Entity('wf_run_node')
export class WfRunNode {
  @PrimaryGeneratedColumn('uuid')
  id!: string;

  @Column()
  runId!: string;

  @Column()
  nodeId!: string;

  @Column({ type: 'varchar', length: 32 })
  status!: 'running' | 'success' | 'failed' | 'skipped';

  @Column({ type: 'json', nullable: true })
  inputMd?: unknown;

  @Column({ type: 'json', nullable: true })
  outputMd?: unknown;

  @Column({ type: 'int', nullable: true })
  durationMs?: number;
}
