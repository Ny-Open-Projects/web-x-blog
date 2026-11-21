import 'reflect-metadata';
import { NestFactory } from '@nestjs/core';
import { ValidationPipe } from '@nestjs/common';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.setGlobalPrefix('api');
  // CORS：生产经 CORS_ORIGINS（逗号分隔）锁定域名；未配置时开发期放宽到全部。
  const origins = process.env.CORS_ORIGINS?.split(',').map((s) => s.trim()).filter(Boolean);
  if (origins && origins.length) {
    app.enableCors({ origin: origins });
  } else {
    app.enableCors();
  }
  app.useGlobalPipes(new ValidationPipe({ transform: true, whitelist: true }));
  const port = Number(process.env.SERVER_PORT ?? 3000);
  await app.listen(port);
  // eslint-disable-next-line no-console
  console.log(`[lowcode-server] listening on :${port} (prefix=/api)`);
}
bootstrap();
