// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
/**
 ** 笔记：抽象思维之代码重构_隔离变化
 ** 方案：方案8（Filler 迭代器式旋转填充）
 ** 来源：python 参考忠实移植
 */

class Filler {
  // 定义类型
  rowNum: number; // rowNum: number;
  colNum: number; // colNum: number;
  rule: string; // rule: string;
  pos: { row: number; col: number }; // pos: { row: number; col: number };
  idx: number; // idx: number;
  rMin: number; // rMin: number;
  cMin: number; // cMin: number;
  rMax: number; // rMax: number;
  cMax: number; // cMax: number;
  constructor(rn: number, cn: number) {
    // constructor(rn: number, cn: number) {
    this.rowNum = rn; // 把 rn; 写入 this.rowNum
    this.colNum = cn; // 把 cn; 写入 this.colNum
    this.rule = 'ESVM'; // 把 「ESVM」; 写入 this.rule
    this.reset(); // this.reset();
  }
  reset(): void {
    // reset(): void {
    this.pos = { row: 0, col: 0 }; // 把 { row: 0, col: 0 }; 写入 this.pos
    this.idx = 0; // 把 0; 写入 this.idx
    this.rMin = 0; // 把 0; 写入 this.rMin
    this.cMin = 0; // 把 0; 写入 this.cMin
    this.rMax = this.rowNum - 1; // 把 this.rowNum 减 1; 写入 this.rMax
    this.cMax = this.colNum - 1; // 把 this.colNum 减 1; 写入 this.cMax
  }
  setRule(r: string): void {
    this.rule = r;
  } // 把 右指针; } 写入 setRule(r: string): void { this.rule
  hasNext(): boolean {
    // hasNext(): boolean {
    return (
      this.rMin <= this.pos.row &&
      this.pos.row <= this.rMax &&
      this.cMin <= this.pos.col &&
      this.pos.col <= this.cMax
    ); // 把 this.pos.col 且 this.pos.col 不超过 this.cMax; 写入 this.cMin <
  }
  next(): [number, number] {
    // 下一个(): [number, number] {
    const r = this.pos.row; // 把 this.pos.row 存入 右指针
    const c = this.pos.col; // 把 this.pos.col 存入 字符
    this._advance(); // this._advance();
    return [r, c]; // 返回 [右指针, 字符]
  }
  _advance(): void {
    // _advance(): void {
    const cmd = this.rule[this.idx % 4]; // 把 this.rule[this.idx 对…取模 4] 存入 cmd
    if (cmd === 'E') {
      // 若 cmd 全等于 「E」
      this.pos.row += 1; // this.pos.row累加 1
      if (this.pos.row === this.rMax) {
        this.idx += 1;
        this.cMin += 1;
      }
    } else if (cmd === 'S') {
      // 否则，若 cmd 全等于 「S」
      this.pos.col += 1; // this.pos.col累加 1
      if (this.pos.col === this.cMax) {
        this.idx += 1;
        this.rMax -= 1;
      }
    } else if (cmd === 'V') {
      // 否则，若 cmd 全等于 「V」
      this.pos.row -= 1; // this.pos.row累减 1
      if (this.pos.row === this.rMin) {
        this.idx += 1;
        this.cMax -= 1;
      }
    } else if (cmd === 'M') {
      // 否则，若 cmd 全等于 「M」
      this.pos.col -= 1; // this.pos.col累减 1
      if (this.pos.col === this.cMin) {
        this.idx += 1;
        this.rMin += 1;
      }
    }
  }
}

function fillMatrix(rn: number, cn: number, rule: string = 'ESVM'): number[][] {
  // 定义函数/方法 fillMatrix
  const mat: number[][] = Array.from({ length: rn }, () =>
    new Array(cn).fill(0),
  );
  const f = new Filler(rn, cn); // 把 new Filler(rn, cn) 存入 f
  f.setRule(rule); // f.setRule(rule);
  let i = 1; // 把 1 存入 下标 i
  while (f.hasNext()) {
    // 循环，直到不满足「f.hasNext(」
    const [r, c] = f.next(); // 把 f.下一个(); 写入 const [r, c]
    mat[r][c] = i; // 把 下标 i; 写入 mat[r][c]
    i++; // 下标 i 加一
  }
  return mat; // 返回 mat
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function eqMat(a: number[][], b: number[][]): boolean {
    // 定义函数/方法 eqMat
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (a[i].length !== b[i].length) return false; // 若 数组[下标 i].长度 不等于 b[下标 i].长度，直接返回 false
      for (let j = 0; j < a[i].length; j++)
        if (a[i][j] !== b[i][j]) return false; // 让 下标 j 从 0 开始计数，下标 j 小于 数组[下标 i].长度 就继续
    }
    return true; // 返回 true
  }
  const cases: { in: [number, number, string]; want: number[][] }[] = [
    {
      in: [6, 6, 'ESVM'],
      want: [
        [1, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
      ],
    },
    {
      in: [3, 3, 'ESVM'],
      want: [
        [1, 0, 0],
        [2, 0, 0],
        [0, 0, 0],
      ],
    },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = fillMatrix(c.in[0], c.in[1], c.in[2]); // 把 fillMatrix(字符.in[0], 字符.in[1], 字符.in[2]) 存入 got
    if (!eqMat(got, c.want)) {
      // 若 取反 eqMat(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL',
        JSON.stringify(c.in),
        'want',
        JSON.stringify(c.want),
        'got',
        JSON.stringify(got),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
