/**
 ** LeetCode 1797. 设计一个验证系统
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145354494
 */

export class AuthenticationManager {
  // export class AuthenticationManager {
  private expiresAt: Map<string, number>; // private expiresAt: Map 小于 string, number 超过 ;
  private ttl: number; // private ttl: number;
  constructor(timeToLive: number) {
    // constructor(timeToLive: number) {
    this.expiresAt = new Map(); // 把 new Map(); 写入 this.expiresAt
    this.ttl = timeToLive; // 把 timeToLive; 写入 this.ttl
  }
  generate(token: string, currentTime: number): void {
    // generate(token: string, currentTime: number): void {
    this.expiresAt.set(token, currentTime + this.ttl); // this.expiresAt.set(token, currentTime 加 this.ttl);
  }
  renew(token: string, currentTime: number): number {
    // renew(token: string, currentTime: number): number {
    if (this.expiresAt.has(token) && this.expiresAt.get(token)! > currentTime) {
      this.expiresAt.set(token, currentTime + this.ttl); // this.expiresAt.set(token, currentTime 加 this.ttl);
      return 1; // 返回 1
    }
    return 0; // 返回 0
  }
  countValidTokens(currentTime: number): number {
    // countValidTokens(currentTime: number): number {
    let count = 0; // 把 0 存入 计数
    for (const expire of this.expiresAt.values()) {
      // for (const expire of this.expiresAt.values()) {
      if (expire > currentTime) count++; // 若 expire 超过 currentTime) 计数 加一 ;
    }
    return count; // 返回 计数
  }
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const auth = new AuthenticationManager(5); // 把 new AuthenticationManager(5) 存入 auth
  auth.generate('aaa', 1); // auth.generate(「aaa」, 1);
  if (auth.countValidTokens(3) !== 1) throw new Error('FAILED count1');
  if (auth.renew('aaa', 4) !== 1) throw new Error('FAILED renew'); // 若 auth.renew(「aaa」, 4) 不等于 1) throw new Error(「aaa」);
  if (auth.countValidTokens(6) !== 1)
    throw new Error('FAILED count2 got ' + auth.countValidTokens(6));
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
