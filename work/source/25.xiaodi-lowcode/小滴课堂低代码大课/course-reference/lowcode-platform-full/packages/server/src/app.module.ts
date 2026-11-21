import { Module } from '@nestjs/common';
import { APP_GUARD } from '@nestjs/core';
import { TypeOrmModule } from '@nestjs/typeorm';
import { typeOrmConfig, redisConfig, jwtConfig } from '../config';
import { UserModule } from './user/user.module';
import { RedisModule } from './utils/modules/redis.module';
import { JwtModule } from '@nestjs/jwt';
import { WechatLoginModule } from './wechat-login/wechat-login.module';
import { User } from './user/entities/user.entity';
import { LowCodeModule } from './low-code/low-code.module';
import { JWTstrategy } from './utils/JwtStrategyTool';
import { ResourcesModule } from './resources/resources.module';
import { JwtAuthGuard } from './utils/guards/jwt-auth.guard';

@Module({
  imports: [
    TypeOrmModule.forRoot(typeOrmConfig),
    UserModule,
    RedisModule.forRoot(redisConfig),
    JwtModule.register(jwtConfig),
    WechatLoginModule,
    { ...TypeOrmModule.forFeature([User]), global: true },
    LowCodeModule,
    ResourcesModule,
  ],
  controllers: [],
  providers: [
    JWTstrategy,
    // 全局鉴权:默认拦截一切,@Public() 显式豁免(见 utils/decorators)
    { provide: APP_GUARD, useClass: JwtAuthGuard },
  ],
})
export class AppModule {}
