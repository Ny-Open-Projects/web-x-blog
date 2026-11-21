import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, Index } from 'typeorm';

export type AuditStatus = 'success' | 'error' | 'timeout';

/**
 * 工作流审计表：记录每一次"高风险节点"（脚本 / 大模型）的执行轨迹。
 * 商业场景的合规与追责依据——谁、在什么租户、跑了什么（哈希）、是否逃逸、耗时多少。
 */
@Entity('wf_audit')
@Index(['tenantId', 'createdAt'])
@Index(['runId'])
export class WfAudit {
  @PrimaryGeneratedColumn('uuid')
  id!: string;

  @Column({ nullable: true })
  tenantId?: string;

  @Column()
  runId!: string;

  @Column()
  nodeId!: string;

  @Column()
  nodeType!: string;

  /** 脚本/提示词的 sha256，便于事后审计"具体跑了什么"而不存储明文。 */
  @Column({ nullable: true })
  codeHash?: string;

  @Column('int')
  durationMs!: number;

  @Column({ type: 'varchar', length: 16 })
  status!: AuditStatus;

  @Column({ type: 'text', nullable: true })
  errorMessage?: string;

  @Column('int', { nullable: true })
  outputBytes?: number;

  /** 实际隔离层：vm 软隔离 / container 容器硬隔离。 */
  @Column({ type: 'varchar', length: 16, nullable: true })
  isolation?: string;

  @CreateDateColumn()
  createdAt!: Date;
}
