// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案10：Filler+Matrix 组合 9x9 全螺旋）
struct Filler {
    // 定义类型
    pos_row: usize,
    pos_col: usize,
    idx: usize,
    r_min: usize,
    c_min: usize,
    r_max: usize,
    c_max: usize,
}

impl Filler {
    // 实现块
    fn new(rn: usize, cn: usize) -> Self {
        // 定义函数/方法 new
        Filler {
            pos_row: 0,
            pos_col: 0,
            idx: 0,
            r_min: 0,
            c_min: 0,
            r_max: rn - 1,
            c_max: cn - 1,
        }
    }
    fn next(&mut self) -> (usize, usize) {
        // 定义函数/方法 next
        let res = (self.pos_row, self.pos_col); // 把 (self.pos_row, self.pos_col) 存入 结果
        let cmd = "ESVM".as_bytes()[self.idx % 4] as char; // 把 「ESVM」.as_bytes()[self.idx 对…取模 4] as char 存入 cmd
        if cmd == 'E' {
            // 若 cmd 等于 'E'
            self.pos_row += 1; // self.pos_row累加 1
            if self.pos_row == self.r_max {
                self.idx += 1;
                self.c_min += 1;
            }
        } else if cmd == 'S' {
            // 否则，若 cmd 等于 'S'
            self.pos_col += 1; // self.pos_col累加 1
            if self.pos_col == self.c_max {
                self.idx += 1;
                self.r_max -= 1;
            }
        } else if cmd == 'V' {
            // 否则，若 cmd 等于 'V'
            self.pos_row -= 1; // self.pos_row累减 1
            if self.pos_row == self.r_min {
                self.idx += 1;
                self.c_max -= 1;
            }
        } else if cmd == 'M' {
            // 否则，若 cmd 等于 'M'
            self.pos_col -= 1; // self.pos_col累减 1
            if self.pos_col == self.c_min {
                self.idx += 1;
                self.r_min += 1;
            }
        }
        res // 结果
    }
}

fn fmt_row(row: &[i32]) -> String {
    // 定义函数/方法 fmt_row
    row.iter()
        .map(|x| format!("{:2}", x))
        .collect::<Vec<_>>()
        .join(" ") // 拼接为字符串
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let (rn, cn) = (9usize, 9usize); // 把 (9usize, 9usize); 写入 let (rn, cn)
    let mut obj = Filler::new(rn, cn); // 把 Filler::new(rn, cn); 写入 let mut obj
    let mut m = vec![vec![0i32; cn]; rn]; // 把 vec取反 [vec取反 [0i32; cn]; rn]; 写入 let mut m
    for i in 0..rn * cn {
        // 逐个取出 0 的元素（下标 i）
        let (r, c) = obj.next(); // 把 obj.下一个(); 写入 let (r, c)
        m[r][c] = (i + 1) as i32; // 把 (下标 i 加 1) as i32; 写入 m[r][c]
    }
    let want = [
        " 1 32 31 30 29 28 27 26 25",
        " 2 33 56 55 54 53 52 51 24",
        " 3 34 57 72 71 70 69 50 23",
        " 4 35 58 73 80 79 68 49 22",
        " 5 36 59 74 81 78 67 48 21",
        " 6 37 60 75 76 77 66 47 20",
        " 7 38 61 62 63 64 65 46 19",
        " 8 39 40 41 42 43 44 45 18",
        " 9 10 11 12 13 14 15 16 17",
    ];
    for i in 0..rn {
        // 逐个取出 0 的元素（下标 i）
        let got = fmt_row(&m[i]); // 把 fmt_row( 按位与 映射表[下标 i]) 存入 got
        assert_eq!(got, want[i], "matrix9 row {}", i); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
