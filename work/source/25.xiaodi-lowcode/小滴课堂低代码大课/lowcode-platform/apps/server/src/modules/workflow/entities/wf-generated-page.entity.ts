import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, Index } from 'typeorm';

/**
 * 工作流运行产出的页面（composePage 节点生成）。
 * 与 wf_* 命名空间一致；tenantId 预留多租户。
 */
@Entity('wf_generated_page')
export class WfGeneratedPage {
  @PrimaryGeneratedColumn('uuid') id!: string;

  @Index()
  @Column({ type: 'varchar', length: 64, nullable: true })
  graphId?: string;

  @Index()
  @Column({ type: 'varchar', length: 64, nullable: true })
  tenantId?: string;

  @Column('text')
  schemaJson!: string;

  @CreateDateColumn()
  createdAt!: Date;
}
