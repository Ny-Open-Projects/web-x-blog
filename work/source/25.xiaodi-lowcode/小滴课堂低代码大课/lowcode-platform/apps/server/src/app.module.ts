import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { TypeOrmModule } from '@nestjs/typeorm';
import { WorkflowModule } from './modules/workflow/workflow.module';
import { PageBuilderModule } from './modules/page-builder/page-builder.module';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    TypeOrmModule.forRoot({
      type: 'mysql',
      host: process.env.DB_HOST ?? 'localhost',
      port: Number(process.env.DB_PORT ?? 3306),
      username: process.env.DB_USER ?? 'lowcode',
      password: process.env.DB_PASSWORD ?? 'change_me',
      database: process.env.DB_DATABASE ?? 'lowcode',
      autoLoadEntities: true,
      synchronize: true, // 仅开发期；生产用迁移脚本（见 README）
    }),
    WorkflowModule,
    PageBuilderModule,
  ],
})
export class AppModule {}
