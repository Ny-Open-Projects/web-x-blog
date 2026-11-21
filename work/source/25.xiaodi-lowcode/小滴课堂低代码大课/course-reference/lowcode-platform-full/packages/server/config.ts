import 'dotenv/config';
import { JwtModuleOptions } from '@nestjs/jwt';
import type { TypeOrmModuleOptions } from '@nestjs/typeorm';
import { RedisOptions } from 'ioredis';

/**
 * 全部配置从环境变量读取(开发期读 packages/server/.env,
 * 生产期由 Docker/CI 注入)。模板见 packages/server/.env.example。
 * 启动时强校验关键变量,缺配置直接失败,避免带病上线。
 */
function required(name: string): string {
  const value = process.env[name];
  if (!value) {
    throw new Error(
      `[config] 缺少环境变量 ${name} —— 请复制 .env.example 为 .env 并填写`,
    );
  }
  return value;
}

function optional(name: string, fallback: string): string {
  return process.env[name] || fallback;
}

const isProd = process.env.NODE_ENV === 'production';

// ---------- 数据库(MySQL)----------
export const typeOrmConfig: TypeOrmModuleOptions = {
  type: 'mysql',
  host: required('DB_HOST'),
  port: Number(optional('DB_PORT', '3306')),
  username: required('DB_USERNAME'),
  password: required('DB_PASSWORD'),
  database: required('DB_DATABASE'),
  entities: ['dist/**/*.entity{.ts,.js}'],
  autoLoadEntities: true,
  // 结构同步仅限开发环境;生产请用迁移(migration)管理表结构
  synchronize: !isProd && process.env.DB_SYNCHRONIZE !== 'false',
};

// ---------- 缓存(Redis)----------
export const redisConfig: RedisOptions = {
  host: required('REDIS_HOST'),
  port: Number(optional('REDIS_PORT', '6379')),
  password: required('REDIS_PASSWORD'),
};

// ---------- 短信服务(第三方运营商)----------
export const xdclassConfig = {
  appid: optional('SMS_APPID', ''),
  appSecret: optional('SMS_APP_SECRET', ''),
  smsApi: optional('SMS_API', 'https://api-v2.xdclass.net/send_sms'),
};

// ---------- JWT ----------
export const jwtConfig: JwtModuleOptions = {
  secret: required('JWT_SECRET'), // 生产必须使用强随机串,绝不入库入仓
  signOptions: { expiresIn: optional('JWT_EXPIRES_IN', '7d') },
  global: true,
};

// ---------- 微信扫码登录 ----------
export const wechatLoginConfig = {
  appId: optional('WECHAT_APPID', ''),
  appSecret: optional('WECHAT_APP_SECRET', ''),
  qrUrl: 'https://mp.weixin.qq.com/cgi-bin/showqrcode',
  token: optional('WECHAT_TOKEN', ''),
};

// ---------- 阿里云 OSS ----------
export const aliOssConfig = {
  region: optional('OSS_REGION', 'oss-cn-hangzhou'),
  accessKeyId: optional('OSS_ACCESS_KEY_ID', ''),
  accessKeySecret: optional('OSS_ACCESS_KEY_SECRET', ''),
  bucket: optional('OSS_BUCKET', ''),
};

export const aliOssDomain = optional('OSS_DOMAIN', '');
