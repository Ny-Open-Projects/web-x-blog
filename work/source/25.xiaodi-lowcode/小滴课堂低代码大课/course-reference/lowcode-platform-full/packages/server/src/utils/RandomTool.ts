import { Injectable } from '@nestjs/common';

@Injectable()
export class RandomTool {
  // 随机生成数字
  randomCode() {
    return Math.floor(Math.random() * (9999 - 1000)) + 1000;
  }
  // 随机生成头像
  randomAvatar() {
    const baseImgUrl = (num: number) => {
      const _num = num === 0 ? 1 : num > 19 ? 19 : num;
      return `https://xd-video-pc-img.oss-cn-beijing.aliyuncs.com/xdclass_pro/default/head_img/${_num}.jpeg`;
    };
    return baseImgUrl(Math.floor(Math.random() * 20));
  }
  // 随机生成昵称
  randomName() {
    return `编程小白${Math.floor(Math.random() * 10000)}`;
  }
}
