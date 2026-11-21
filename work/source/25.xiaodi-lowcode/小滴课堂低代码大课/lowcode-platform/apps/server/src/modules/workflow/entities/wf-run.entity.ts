import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn } from 'typeorm';

/** 一次工作流执行记录。 */
@Entity('wf_run')
export class WfRun {
  @PrimaryGeneratedColumn('uuid')
  id!: string;

  @Column()
  graphId!: string;

  @Column({ type: 'varchar', length: 32, default: 'running' })
  status!: 'running' | 'success' | 'failed';

  @Column({ nullable: true })
  trigger?: string;

  @Column({ nullable: true })
  tenantId?: string;

  @Column({ nullable: true })
  caller?: string;

  @CreateDateColumn()
  startedAt!: Date;

  @Column({ type: 'datetime', nullable: true })
  finishedAt?: Date;
}
