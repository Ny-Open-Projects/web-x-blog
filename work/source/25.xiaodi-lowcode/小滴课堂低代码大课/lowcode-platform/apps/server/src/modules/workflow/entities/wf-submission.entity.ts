import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, Index } from 'typeorm';

/**
 * 表单提交记录（trigger.formSubmit 节点产出）。
 * M6：由内存 mock 改为真实落库，使工作流具备可追溯的业务数据。
 */
@Entity('wf_submission')
@Index(['tenantId', 'createdAt'])
export class WfSubmission {
  @PrimaryGeneratedColumn('uuid')
  id!: string;

  @Column()
  formId!: string;

  @Column('json')
  data!: Record<string, unknown>;

  @Column({ nullable: true })
  tenantId?: string;

  @CreateDateColumn()
  createdAt!: Date;
}
