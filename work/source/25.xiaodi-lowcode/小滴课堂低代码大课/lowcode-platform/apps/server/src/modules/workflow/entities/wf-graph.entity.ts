import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, UpdateDateColumn } from 'typeorm';

/** 工作流图定义。tenantId 预留多租户，当前不强制隔离。 */
@Entity('wf_graph')
export class WfGraph {
  @PrimaryGeneratedColumn('uuid')
  id!: string;

  @Column()
  name!: string;

  @Column({ type: 'int', default: 1 })
  version!: number;

  /** 图的 JSON（nodes + edges），经 DTO 校验后入库 */
  @Column({ type: 'json' })
  graphJson!: { nodes: unknown[]; edges: unknown[] };

  @Column({ type: 'varchar', length: 32, default: 'draft' })
  status!: 'draft' | 'published';

  @Column({ nullable: true })
  tenantId?: string;

  @Column({ nullable: true })
  ownerId?: string;

  @CreateDateColumn()
  createdAt!: Date;

  @UpdateDateColumn()
  updatedAt!: Date;
}
