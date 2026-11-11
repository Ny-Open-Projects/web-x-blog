// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

class Location {
  // 定义类型
  row: number;
  col: number; // row: number; col: number;
  constructor(row: number = 0, col: number = 0) {
    this.row = row;
    this.col = col;
  }
}
class Filler {
  // 定义类型
  row_num: number;
  col_num: number; // row_num: number; col_num: number;
  pos: Location;
  idx: number;
  r_min: number;
  c_min: number;
  r_max: number;
  c_max: number;
  rule: string;
  constructor(rn: number, cn: number) {
    this.row_num = rn;
    this.col_num = cn;
    this.reset();
  }
  reset(): void {
    // reset(): void {
    this.pos = new Location(0, 0);
    this.idx = 0;
    this.r_min = this.c_min = 0;
    this.r_max = this.row_num - 1;
    this.c_max = this.col_num - 1;
    this.rule = 'ESVM';
  }
  setRule(rule: string): void {
    this.rule = rule;
  } // 把 rule; } 写入 setRule(rule: string): void { this.rule
  next(): Location {
    // 下一个(): Location {
    const res = new Location(this.pos.row, this.pos.col); // 把 new Location(this.pos.row, this.pos.col) 存入 结果
    const ch = this.rule[this.idx % this.rule.length]; // 把 this.rule[this.idx 对…取模 this.rule.长度] 存入 字符
    if (ch === 'E') {
      this.pos.row++;
      if (this.pos.row === this.r_max) {
        this.idx++;
        this.c_min++;
      }
    } else if (ch === 'S') {
      this.pos.col++;
      if (this.pos.col === this.c_max) {
        this.idx++;
        this.r_max--;
      }
    } else if (ch === 'V') {
      this.pos.row--;
      if (this.pos.row === this.r_min) {
        this.idx++;
        this.c_max--;
      }
    } else if (ch === 'M') {
      this.pos.col--;
      if (this.pos.col === this.c_min) {
        this.idx++;
        this.r_min++;
      }
    } else if (ch === 'e') {
      this.pos.row++;
      if (this.pos.row === this.r_max) {
        this.idx++;
        this.c_max--;
      }
    } else if (ch === 's') {
      this.pos.col++;
      if (this.pos.col === this.c_max) {
        this.idx++;
        this.r_min++;
      }
    } else if (ch === 'v') {
      this.pos.row--;
      if (this.pos.row === this.r_min) {
        this.idx++;
        this.c_min++;
      }
    } else if (ch === 'm') {
      this.pos.col--;
      if (this.pos.col === this.c_min) {
        this.idx++;
        this.r_max--;
      }
    }
    return res; // 返回 结果
  }
}
function testFiller(rule: string, rn: number, cn: number): number[][] {
  // 定义函数/方法 testFiller
  const obj = new Filler(rn, cn);
  obj.setRule(rule); // 把 new Filler(rn, cn); obj.setRule(rule) 存入 obj
  const seq: number[][] = []; // 把 []; 写入 const seq: number[][]
  for (let i = 0; i < rn * cn; i++) {
    const p = obj.next();
    seq.push([p.row, p.col]);
  } // 让 下标 i 从 0 开始计数，下标 i 小于 rn 乘 cn 就继续
  return seq; // 返回 seq
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(
    testFiller('ESVM', 4, 4),
    [
      [0, 0],
      [1, 0],
      [2, 0],
      [3, 0],
      [3, 1],
      [3, 2],
      [3, 3],
      [2, 3],
      [1, 3],
      [0, 3],
      [0, 2],
      [0, 1],
      [1, 1],
      [2, 1],
      [2, 2],
      [1, 2],
    ],
    'ESVM',
  ); // 断言校验
  assertEq(
    testFiller('semv', 4, 4),
    [
      [0, 0],
      [0, 1],
      [0, 2],
      [0, 3],
      [1, 3],
      [2, 3],
      [3, 3],
      [3, 2],
      [3, 1],
      [3, 0],
      [2, 0],
      [1, 0],
      [1, 1],
      [1, 2],
      [2, 2],
      [2, 1],
    ],
    'semv',
  ); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
