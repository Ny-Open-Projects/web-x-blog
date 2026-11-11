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
    }
    return res; // 返回 结果
  }
}
class Matrix {
  // 定义类型
  row: number;
  col: number;
  buf: number[][]; // row: number; col: number; buf: number[][];
  constructor(r: number, c: number) {
    this.row = r;
    this.col = c;
    this.buf = Array.from({ length: r }, () => new Array(c).fill(0));
  }
  get(r: number, c: number): number {
    return this.buf[r][c];
  }
  set(r: number, c: number, v: number): void {
    this.buf[r][c] = v;
  }
}
function fmtRow(row: number[]): string {
  // 定义函数/方法 fmtRow
  return row.map((x) => x.toString().padStart(2, ' ')).join(' ');
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const rn = 9,
    cn = 9; // 把 9, cn 赋值为 9 存入 rn
  const obj = new Filler(rn, cn);
  obj.setRule('ESVM'); // 把 new Filler(rn, cn); obj.setRule(「ESVM」) 存入 obj
  const m = new Matrix(rn, cn); // 把 new Matrix(rn, cn) 存入 映射表
  for (let i = 0; i < rn * cn; i++) {
    const p = obj.next();
    m.set(p.row, p.col, i + 1);
  } // 让 下标 i 从 0 开始计数，下标 i 小于 rn 乘 cn 就继续
  const rows = m.buf.map(fmtRow); // 把 映射表.buf.映射表(fmtRow) 存入 行数
  assertEq(
    rows,
    [
      ' 1 32 31 30 29 28 27 26 25',
      ' 2 33 56 55 54 53 52 51 24',
      ' 3 34 57 72 71 70 69 50 23',
      ' 4 35 58 73 80 79 68 49 22',
      ' 5 36 59 74 81 78 67 48 21',
      ' 6 37 60 75 76 77 66 47 20',
      ' 7 38 61 62 63 64 65 46 19',
      ' 8 39 40 41 42 43 44 45 18',
      ' 9 10 11 12 13 14 15 16 17',
    ],
    'matrix9',
  ); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
