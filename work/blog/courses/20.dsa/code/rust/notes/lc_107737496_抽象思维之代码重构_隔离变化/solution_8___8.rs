// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案8：Filler 状态机 + hasNext 部分填充）
struct Filler {
    // 定义类型
    row_num: usize,
    col_num: usize,
    rule: String,
    pos: (usize, usize),
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
            // Filler {
            row_num: rn,
            col_num: cn,
            rule: "ESVM".to_string(),
            pos: (0, 0),
            idx: 0,
            r_min: 0,
            c_min: 0,
            r_max: rn - 1,
            c_max: cn - 1,
        }
    }
    fn set_rule(&mut self, r: &str) {
        // 定义函数/方法 set_rule
        self.rule = r.to_string(); // 把 右指针.to_string(); 写入 self.rule
    }
    fn has_next(&self) -> bool {
        // 定义函数/方法 has_next
        self.r_min <= self.pos.0  // 把 self.pos.0 写入 self.r_min <
            && self.pos.0 <= self.r_max  // 把 self.r_max 写入 && self.pos.0 <
            && self.c_min <= self.pos.1  // 把 self.pos.1 写入 && self.c_min <
            && self.pos.1 <= self.c_max // 把 self.c_max 写入 && self.pos.1 <
    }
    fn next(&mut self) -> (usize, usize) {
        // 定义函数/方法 next
        let r = self.pos.0; // 把 self.pos.0 存入 右指针
        let c = self.pos.1; // 把 self.pos.1 存入 字符
        self.advance(); // self.advance();
        (r, c) // (右指针, 字符)
    }
    fn advance(&mut self) {
        // 定义函数/方法 advance
        let cmd = self.rule.as_bytes()[self.idx % 4] as char; // 把 self.rule.as_bytes()[self.idx 对…取模 4] as char 存入 cmd
        if cmd == 'E' {
            // 若 cmd 等于 'E'
            self.pos.0 += 1; // self.pos.0累加 1
            if self.pos.0 == self.r_max {
                // 若 self.pos.0 等于 self.r_max
                self.idx += 1; // self.idx累加 1
                self.c_min += 1; // self.c_min累加 1
            }
        } else if cmd == 'S' {
            // 否则，若 cmd 等于 'S'
            self.pos.1 += 1; // self.pos.1累加 1
            if self.pos.1 == self.c_max {
                // 若 self.pos.1 等于 self.c_max
                self.idx += 1; // self.idx累加 1
                self.r_max -= 1; // self.r_max累减 1
            }
        } else if cmd == 'V' {
            // 否则，若 cmd 等于 'V'
            self.pos.0 -= 1; // self.pos.0累减 1
            if self.pos.0 == self.r_min {
                // 若 self.pos.0 等于 self.r_min
                self.idx += 1; // self.idx累加 1
                self.c_max -= 1; // self.c_max累减 1
            }
        } else if cmd == 'M' {
            // 否则，若 cmd 等于 'M'
            self.pos.1 -= 1; // self.pos.1累减 1
            if self.pos.1 == self.c_min {
                // 若 self.pos.1 等于 self.c_min
                self.idx += 1; // self.idx累加 1
                self.r_min += 1; // self.r_min累加 1
            }
        }
    }
}

fn fill_matrix(rn: usize, cn: usize, rule: &str) -> Vec<Vec<i32>> {
    // 定义函数/方法 fill_matrix
    let mut mat = vec![vec![0i32; cn]; rn]; // 把 vec取反 [vec取反 [0i32; cn]; rn]; 写入 let mut mat
    let mut f = Filler::new(rn, cn); // 把 Filler::new(rn, cn); 写入 let mut f
    f.set_rule(rule); // f.set_rule(rule);
    let mut i = 1i32; // 把 1i32; 写入 let mut i
    while f.has_next() {
        // while f.has_next() {
        let (r, c) = f.next(); // 把 f.下一个(); 写入 let (r, c)
        mat[r][c] = i; // 把 下标 i; 写入 mat[r][c]
        i += 1; // 下标 i累加 1
    }
    mat // mat
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let want1 = vec![
        vec![1, 0, 0, 0, 0, 0],
        vec![2, 0, 0, 0, 0, 0],
        vec![3, 0, 0, 0, 0, 0],
        vec![4, 0, 0, 0, 0, 0],
        vec![5, 0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0],
    ];
    assert_eq!(fill_matrix(6, 6, "ESVM"), want1, "case1"); // 断言校验
    let want2 = vec![vec![1, 0, 0], vec![2, 0, 0], vec![0, 0, 0]];
    assert_eq!(fill_matrix(3, 3, "ESVM"), want2, "case2"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
