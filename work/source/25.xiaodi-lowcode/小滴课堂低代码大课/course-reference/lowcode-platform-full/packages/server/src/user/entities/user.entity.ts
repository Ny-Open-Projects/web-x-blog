import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number = 0;

  @Column()
  username: string = '';

  @Column()
  head_img: string = '';

  @Column()
  phone: string = '';

  @Column()
  password: string = '';

  @Column()
  open_id: string = '';
}
