import { Injectable } from '@nestjs/common';
import { parseString } from 'xml2js';

@Injectable()
export class WechatDataTool {
  getXMLStr(req: any) {
    // 函数返回一个新的 Promise 对象，用于异步处理数据
    return new Promise((resolve) => {
      let data = '';
      // req 触发 'data' 事件，数据流中接收到新数据
      req.on('data', (msg: any) => {
        // 将接收到的数据（msg）转换为字符串，并追加到 data 变量上
        data += msg.toString();
      });
      // req 触发 'end' 事件，数据流结束接收数据
      req.on('end', () => {
        resolve(data);
      });
    });
  }

  // 将 XML 转化为对象的方法
  getObject(data: any) {
    return new Promise((resolve, reject) => {
      parseString(data, (err, result) => {
        if (err) reject(err);
        else resolve(result);
      });
    });
  }

  // 转成普通对象
  getLastData(query: any) {
    const obj: any = {};
    // 检查 query 是否存在且其类型是否为对象。如果不是，函数将返回一个空对象
    if (query && typeof query === 'object') {
      // 遍历 query 对象的所有属性
      for (const key in query) {
        const value = query[key];
        // 如果该属性的值存在且其长度大于0，则将数组的第一个元素存储在 obj 对象中，使用相同的属性名
        if (value && value.length > 0) obj[key] = value[0];
      }
      return obj;
    } else {
      return obj;
    }
  }
}
