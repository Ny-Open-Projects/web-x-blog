import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

/** 节点定义持久化（与代码注册表镜像），供前端拉取元信息。 */
@Entity('wf_node_def')
export class WfNodeDef {
  @PrimaryGeneratedColumn('uuid')
  id!: string;

  @Column()
  type!: string;

  @Column()
  category!: string;

  @Column({ type: 'int' })
  version!: number;

  @Column({ type: 'json' })
  portsJson!: { inputs: unknown[]; outputs: unknown[] };

  @Column({ default: false })
  deprecated!: boolean;
}
