import { Buffer } from 'node:buffer';
import { resolve } from 'node:path';
import { unlinkSync } from 'node:fs';
import * as AliOss from 'ali-oss';
import { Options as AliOssOptions } from 'ali-oss';
import type { DynamicModule, Provider } from '@nestjs/common';
import { BadRequestException, Module } from '@nestjs/common';
import { aliOssConfig, aliOssDomain } from 'config';

// 这个正则用于处理OSS取出的域名不是自定义域名的问题
const regex = new RegExp(
  `http[s]?:\/\/(?:${aliOssConfig.bucket})\.(?:${aliOssConfig.region})(?:\.aliyuncs\.com)`,
);

@Module({})
export class AliOssModule {
  // 定义一个私有的 alioss 实例
  private alioss: AliOss;

  // 接受 alioss 连接配置类型，并创建一个 alioss 实例
  constructor(options: AliOssOptions) {
    this.alioss = new AliOss(options);
  }

  // 创建包含 AliOss 模块提供者的动态模块
  static forRoot(options: AliOssOptions): DynamicModule {
    // 创建一个提供者数组，其中包含一个 AliOssModule 实例
    const providers: Provider[] = [
      {
        provide: AliOssModule,
        useValue: new AliOssModule(options),
      },
    ];

    return {
      providers,
      global: true,
      exports: providers,
      module: AliOssModule,
    };
  }

  // 上传资源，接受中间件Multer处理的上传文件对象参数
  async uploadToAliOss(file: Express.Multer.File) {
    // 使用Buffer将文件名从latin1编码转换为utf8编码，为了确保文件名是正确的Unicode格式
    const name = Buffer.from(file.originalname, 'latin1').toString('utf8');
    // 生成上传到阿里云 oss 的文件的路径，原始文件名+当前时间戳+原始文件扩展名
    const toUploadPath = `upload_files/${name
      .split('.')
      .shift()}-${Date.now()}.${name.split('.').pop()}`;
    // 生成本地临时文件路径
    const localPath = resolve(`./__temps__/${file.filename}`);

    // 调用阿里云oss的上传api将本地临时文件上传到阿里云OSS
    const { url, res } = await this.alioss
      .put(toUploadPath, localPath)
      .finally(() => {
        // 不管是否成功都删除掉本地临时文件
        unlinkSync(localPath);
      });

    // 响应状态为200并且URL存在，如果条件满足，则使用正则表达式替换URL中的某些部分，并返回最终的URL
    if (res.status === 200 && url) return url.replace(regex, aliOssDomain);

    throw new BadRequestException('上传失败, 请重试');
  }

  // 删除资源
  async deleteFromAliOss(url: string) {
    // 调用阿里云删除 api，拿到前端的 url 处理成名字+后缀
    const { res } = await this.alioss.delete(
      decodeURI(url.replace(aliOssDomain, '')),
    );
    // 删除成功
    if (res.status === 204) return;
    throw new BadRequestException('删除失败，请重试');
  }
}
