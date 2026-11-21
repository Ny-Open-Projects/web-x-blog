import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { ResponseIntercept } from './common/ResponseIntercept';
import { AbnormalFilter } from './common/AbnormalFilter';
import { ValidationPipe } from '@nestjs/common';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  // 配置跨域
  app.enableCors();
  // 全局注册拦截器
  app.useGlobalInterceptors(new ResponseIntercept());
  // 全局注册异常拦截器
  app.useGlobalFilters(new AbnormalFilter());
  app.useGlobalPipes(new ValidationPipe());
  app.setGlobalPrefix('api');
  await app.listen(3000);
}
bootstrap();
