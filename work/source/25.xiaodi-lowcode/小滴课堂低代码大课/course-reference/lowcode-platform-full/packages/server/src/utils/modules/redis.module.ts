import type { DynamicModule, Provider } from '@nestjs/common';
import { Module } from '@nestjs/common';
import Redis, { RedisOptions } from 'ioredis';

@Module({})
export class RedisModule {
  // 定义一个私有的 Redis 实例
  private redis: Redis;

  // 接受 Redis 连接配置类型，并创建一个 Redis 实例
  constructor(options: RedisOptions) {
    this.redis = new Redis(options);
  }
  // 定义一个静态方法，用于创建包含 Redis 模块提供者的动态模块
  static forRoot(options: RedisOptions): DynamicModule {
    // 创建一个提供者数组，其中包含一个 RedisModule 实例
    const providers: Provider[] = [
      {
        provide: RedisModule,
        useValue: new RedisModule(options),
      },
    ];

    return {
      providers,
      global: true, // 将模块设置为全局可用
      exports: providers, // 导出提供者，使其可在其他模块中使用
      module: RedisModule, // 指定模块类
    };
  }

  // 设置 Redis 中的键值对，可选参数用于设置过期时间
  set(key: string, value: string, time?: number) {
    time ? this.redis.set(key, value, 'EX', time) : this.redis.set(key, value);
  }

  // 删除 Redis 中的指定键
  del(key: string) {
    this.redis.del(key);
  }

  // 异步方法从 Redis 中获取指定键的值
  async get(key: string) {
    const value = await this.redis.get(key);
    return value ? value.toString() : null;
  }

  // 异步方法检查 Redis 中是否存在指定键
  async exists(key: string) {
    const result = await this.redis.exists(key);
    return result;
  }

  async getCachedData<T = any>(
    key: string,
    fetchFunction: () => Promise<T>,
    options?: {
      ttl?: number;
      force?: boolean;
    },
  ): Promise<T> {
    let data = await this.redis.get(key);

    if (options?.force) {
      // 设置强制刷新
      data = null;
    }

    if (!data) {
      // @ts-expect-error ignore this type
      data = await fetchFunction();
      await this.redis.set(
        key,
        JSON.stringify(data),
        'EX',
        options?.ttl ?? 3600,
      );
    } else {
      data = JSON.parse(data);
    }

    return data as T;
  }
}
