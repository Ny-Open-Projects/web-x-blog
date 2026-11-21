import { createHash } from 'node:crypto';
import { Injectable } from '@nestjs/common';

@Injectable()
export class SecretTool {
  getSecret(data: string) {
    // 创建一个 MD5 哈希对象,更新哈希对象的内容为指定的数据,以十六进制返回
    return createHash('md5').update(data).digest('hex');
  }
}
