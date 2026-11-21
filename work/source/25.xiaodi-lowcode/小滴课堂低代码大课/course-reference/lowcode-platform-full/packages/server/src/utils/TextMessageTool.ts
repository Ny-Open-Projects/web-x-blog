import { Injectable } from '@nestjs/common';
import { xdclassConfig } from 'config';

/**
 * 短信发送装饰器
 */
@Injectable()
export class TextMessageTool {
  async sendMsgCode(phone: string, randomCode: number) {
    const headers = new Headers();
    headers.append('Content-Type', 'application/json');
    const result = await fetch(xdclassConfig.smsApi, {
      headers,
      method: 'post',
      body: JSON.stringify({
        ...xdclassConfig,
        code: randomCode,
        phoneNum: phone,
        templateCode: 'SMS_168781429',
      }),
    });
    return result.json();
  }
}
