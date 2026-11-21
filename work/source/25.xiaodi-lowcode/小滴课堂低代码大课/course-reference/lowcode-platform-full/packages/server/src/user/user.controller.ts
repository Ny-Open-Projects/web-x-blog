import { Controller, Post, Body } from '@nestjs/common';
import { Public } from '../utils/decorators/public.decorator';
import { UserService } from './user.service';
import { CaptchaDto } from './dto/captcha.dto';
import { SendCodeDto } from './dto/sendCode.dto';
import { GetUserIp, GetUserAgent } from '../utils/GetUserMessTool';
import { SecretTool } from '../utils/SecretTool';
import { RandomTool } from '../utils/RandomTool';
import { RegisterDto } from './dto/register.dto';
import { PasswordLoginDto, PhoneLoginDto } from './dto/login.dto';
@Public() // 注册/登录/验证码均为公开接口
@Controller('user')
export class UserController {
  constructor(
    private readonly userService: UserService,
    private readonly secretTool: SecretTool,
    private readonly randomTool: RandomTool,
  ) {}

  /**
   * 图形验证码控制器
   */
  @Post('captcha')
  getCaptcha(
    @Body() body: CaptchaDto,
    @GetUserIp() ip: string,
    @GetUserAgent() agent: string,
  ) {
    const { type } = body;
    // 用户的 ip+设备加密
    const _key = this.secretTool.getSecret(ip + agent);
    return this.userService.getCaptcha(_key, type);
  }

  /**
   * 短信验证码控制器
   */
  @Post('send_code')
  async sendCode(
    @Body() body: SendCodeDto,
    @GetUserIp() ip: string,
    @GetUserAgent() agent: string,
  ) {
    const { phone, type, captcha } = body;
    // 用户的 ip+设备加密
    const _key = this.secretTool.getSecret(ip + agent);
    return this.userService.sendCode(
      phone,
      captcha,
      type,
      _key,
      this.randomTool.randomCode(),
    );
  }

  /**
   * 注册控制器
   */
  @Post('register')
  register(@Body() body: RegisterDto) {
    const { phone, sendCode, password, confirm } = body;
    return this.userService.register(phone, sendCode, password, confirm);
  }

  /**
   * 账号密码登录控制器
   */
  @Post('password_login')
  passwordLogin(@Body() body: PasswordLoginDto) {
    return this.userService.passwordLogin(body);
  }

  /**
   * 手机验证码登录控制器
   */
  @Post('phone_login')
  phoneLogin(@Body() body: PhoneLoginDto) {
    return this.userService.phoneLogin(body);
  }
}
