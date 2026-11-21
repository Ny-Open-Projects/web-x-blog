// low-code.entity.ts
import type { IComponent, IComponentData, ILowCode } from '@lowcode/share';
import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';
import { TComponentTypes } from '@lowcode/share';

@Entity({ name: 'page' })
export class Page implements ILowCode {
  @PrimaryGeneratedColumn()
  id: number = 0;

  @Column()
  account_id: number = 0;

  @Column()
  page_name: string = '';

  @Column({ type: 'simple-array' })
  components: string[] = [];

  @Column()
  tdk: string = '';

  @Column()
  desc: string = '';
}

@Entity({ name: 'component' })
export class Component implements IComponent {
  @PrimaryGeneratedColumn()
  id: number = 0;

  @Column()
  type: TComponentTypes = 'titleText';

  @Column()
  page_id: number = 0;

  @Column()
  account_id: number = 0;

  @Column({ type: 'simple-json' })
  options: Record<string, any> = {};
}

@Entity({ name: 'component_data' })
export class ComponentData implements IComponentData {
  @PrimaryGeneratedColumn()
  id: number = 0;

  @Column()
  page_id: number = 0;

  @Column()
  user: string = '';

  @Column({ type: 'simple-json' })
  props: {
    id: number;
    value: string | string[];
  }[] = [];
}
