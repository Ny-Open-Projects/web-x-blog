import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { PageDef } from './entities/page-def.entity';
import { PageBuilderService } from './page-builder.service';
import { PageBuilderController } from './page-builder.controller';

@Module({
  imports: [TypeOrmModule.forFeature([PageDef])],
  controllers: [PageBuilderController],
  providers: [PageBuilderService],
})
export class PageBuilderModule {}
