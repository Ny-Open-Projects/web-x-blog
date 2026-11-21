import { Module } from '@nestjs/common';
import { ResourcesService } from './resources.service';
import { ResourcesController } from './resources.controller';
import { MulterModule } from '@nestjs/platform-express';
import { AliOssModule } from 'src/utils/modules/ali-oss.module';
import { aliOssConfig } from 'config';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Resources } from './entities/resources.entity';

@Module({
  imports: [
    MulterModule.register({ dest: '__temps__' }),
    AliOssModule.forRoot(aliOssConfig),
    TypeOrmModule.forFeature([Resources]),
  ],
  controllers: [ResourcesController],
  providers: [ResourcesService],
})
export class ResourcesModule {}
