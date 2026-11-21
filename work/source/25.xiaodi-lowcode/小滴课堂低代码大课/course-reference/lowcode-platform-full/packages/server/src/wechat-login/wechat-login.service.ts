import { Injectable } from '@nestjs/common';
import { CallbackInsertRequest } from '@lowcode/share';
import { WechatLoginToolModule } from 'src/utils/modules/wechat-login-tool.module';
import { createHash } from 'node:crypto';
import { RedisModule } from '../utils/modules/redis.module';
import { WechatDataTool } from '../utils/WechatDataTool';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from '../user/entities/user.entity';
import { RandomTool } from '../utils/RandomTool';
import { JwtService } from '@nestjs/jwt';

@Injectable()
export class WechatLoginService {
  constructor(
    private readonly randomTool: RandomTool,
    private readonly jwtService: JwtService,
    private readonly redis: RedisModule,
    private readonly wechatDataTool: WechatDataTool,
    private readonly wechatLoginToolModule: WechatLoginToolModule,
    @InjectRepository(User) private readonly userRepository: Repository<User>,
  ) {}

  // 微信服务接入验证服务
  insert(params: CallbackInsertRequest) {
    const { signature, timestamp, nonce, echostr } = params;
    const token = this.wechatLoginToolModule.token;
    const str = [token, timestamp, nonce].sort().join('');
    const hash = createHash('sha1');
    hash.update(str);
    const encrypteData = hash.digest('hex');
    console.log(encrypteData, signature);
    if (encrypteData === signature) {
      return { data: echostr, msg: '微信验证回调' };
    }
  }

  // 获取微信二维码服务
  async login() {
    // 获取二维码
    const { qrcodeUrl, ticket } = await this.wechatLoginToolModule.getOR();
    // 将 ticket 存入 reids
    const key = `wechat:ticket:${ticket}`;
    this.redis.set(key, JSON.stringify({ isScan: 'no' }), 120);
    return { qrcodeUrl, ticket };
  }

  // 接受微信调用的服务
  async wechatMessage(body) {
    interface IObjectData {
      xml: object;
    }
    console.log(body);
    // 处理微信的 XML 数据
    const xmlData = Object.keys(body)[0];
    // 正式版本
    // const xmlData = await this.wechatDataTool.getXMLStr(body)
    // 课程的版本
    const objectData = (await this.wechatDataTool.getObject(
      xmlData,
    )) as IObjectData;
    const lastData = this.wechatDataTool.getLastData(objectData.xml);
    console.log(lastData);
    // 根据 openid 判断是否注册过
    const openidRes = await this.userRepository.findOne({
      where: { open_id: lastData.FromUserName },
    });

    // 随机生成头像和昵称
    const username = this.randomTool.randomName();
    const head_img = this.randomTool.randomAvatar();

    let userId = null;

    if (openidRes) {
      //注册过
      userId = openidRes.id;
    } else {
      // 没注册;
      const resData = await this.userRepository.save({
        head_img,
        username,
        open_id: lastData.FromUserName,
        phone: '',
        password: '',
      });
      userId = resData.id;
    }

    // 生成 token
    const token = this.jwtService.sign({ id: userId });

    // 更新 redis 状态
    const key = `wechat:ticket:${lastData.Ticket}`;
    const existsKey = await this.redis.exists(key);
    if (existsKey)
      this.redis.set(key, JSON.stringify({ isScan: 'yes', token }), 120);

    // 返回微信服务器的内容
    let content = '';
    if (lastData.MsgType === 'event') {
      if (lastData.Event === 'SCAN') content = '欢迎回来,讲师微信:xdclass6';
      else if (lastData.Event === 'subscribe')
        content = '感谢关注,讲师微信:xdclass6';

      const msgStr = `<xml>
      <ToUserName><![CDATA[${lastData.FromUserName}]]></ToUserName>
      <FromUserName><![CDATA[${lastData.ToUserName}]]></FromUserName>
      <CreateTime>${Date.now()}</CreateTime>
      <MsgType><![CDATA[text]]></MsgType>
      <Content><![CDATA[${content}]]></Content>
     </xml>`;
      return {
        data: msgStr,
        msg: '微信验证回调',
      };
    }
  }

  //轮询的服务
  async checkScan(param: { ticket: string }) {
    const { ticket } = param;
    const key = `wechat:ticket:${ticket}`;
    const redisData = JSON.parse((await this.redis.get(key)) as string);
    if (redisData && redisData.isScan === 'yes') {
      const { token } = redisData;
      return {
        data: token,
        msg: '登录成功',
      };
    }
  }
}
