import { Module } from '@nestjs/common';
import { WechatLoginService } from './wechat-login.service';
import { WechatLoginController } from './wechat-login.controller';
import { WechatLoginToolModule } from '../utils/modules/wechat-login-tool.module';
import { wechatLoginConfig } from '../../config';
import { WechatDataTool } from '../utils/WechatDataTool';
import { RandomTool } from '../utils/RandomTool';

@Module({
  imports: [WechatLoginToolModule.forRootop(wechatLoginConfig)],
  controllers: [WechatLoginController],
  providers: [WechatLoginService, WechatDataTool, RandomTool],
})
export class WechatLoginModule {}
