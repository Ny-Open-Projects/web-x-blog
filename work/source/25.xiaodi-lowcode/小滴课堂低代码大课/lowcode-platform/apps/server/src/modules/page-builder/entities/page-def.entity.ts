import {
  Entity,
  PrimaryGeneratedColumn,
  Column,
  CreateDateColumn,
  UpdateDateColumn,
} from 'typeorm';

/**
 * 可视化页面定义表（page-builder 模块）。
 * 一页即一份 PageSchema JSON；渲染端复用 workflow 引擎的 renderPageToHtml 产出 HTML。
 * 与 wf_* 表同库，共享租户隔离（tenantId 字段由 TenantGuard 注入）。
 */
@Entity('page_def')
export class PageDef {
  @PrimaryGeneratedColumn('uuid')
  id!: string;

  @Column({ type: 'varchar', length: 64, nullable: true })
  tenantId?: string | null;

  @Column({ type: 'varchar', length: 128 })
  name!: string;

  @Column({ type: 'text' })
  schemaJson!: string;

  @CreateDateColumn()
  createdAt!: Date;

  @UpdateDateColumn()
  updatedAt!: Date;
}
