import { Controller, Get, Query, Post, Body } from '@nestjs/common';
import { Public } from '../utils/decorators/public.decorator';
import { WechatLoginService } from './wechat-login.service';
import { CallbackInsertRequest } from '@lowcode/share';

@Public() // 接入验证/二维码/回调/轮询均为公开接口
@Controller('wechat_login')
export class WechatLoginController {
  constructor(private readonly wechatLoginService: WechatLoginService) {}

  // 微信介入验证控制器
  @Get('callback')
  insert(@Query() params: CallbackInsertRequest) {
    return this.wechatLoginService.insert(params);
  }

  // 获取微信二维码控制器
  @Get('login')
  login() {
    return this.wechatLoginService.login();
  }

  /**
   * 接收微信回调的用户信息控制器
   */
  @Post('callback')
  wechatMessage(@Body() body) {
    return this.wechatLoginService.wechatMessage(body);
  }

  /**
   * 轮询用户是否扫码
   */
  @Get('check_scan')
  checkScan(@Query() param: { ticket: string }) {
    return this.wechatLoginService.checkScan(param);
  }
}
