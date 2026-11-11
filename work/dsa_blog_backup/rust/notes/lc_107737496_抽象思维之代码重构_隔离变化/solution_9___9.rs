// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案9：规则串状态机，8 方向字母）
struct Location {
    // 定义类型
    row: i32,
    col: i32,
}

struct Filler {
    // 定义类型
    row_num: i32,
    col_num: i32,
    pos: Location,
    idx: usize,
    r_min: i32,
    c_min: i32,
    r_max: i32,
    c_max: i32,
    rule: String,
}

impl Filler {
    // 实现块
    fn new(rn: i32, cn: i32) -> Self {
        // 定义函数/方法 new
        Filler {
            // Filler {
            row_num: rn,
            col_num: cn,
            pos: Location { row: 0, col: 0 },
            idx: 0,
            r_min: 0,
            c_min: 0,
            r_max: rn - 1,
            c_max: cn - 1,
            rule: "ESVM".to_string(),
        }
    }
    fn set_rule(&mut self, rule: &str) {
        // 定义函数/方法 set_rule
        self.rule = rule.to_string(); // 把 rule.to_string(); 写入 self.rule
    }
    fn next(&mut self) -> (i32, i32) {
        // 定义函数/方法 next
        let res = (self.pos.row, self.pos.col); // 把 (self.pos.row, self.pos.col) 存入 结果
        let ch = self.rule.as_bytes()[self.idx % self.rule.len()] as char;
        if ch == 'E' {
            // 若 字符 等于 'E'
            self.pos.row += 1; // self.pos.row累加 1
            if self.pos.row == self.r_max {
                self.idx += 1;
                self.c_min += 1;
            }
        } else if ch == 'S' {
            // 否则，若 字符 等于 'S'
            self.pos.col += 1; // self.pos.col累加 1
            if self.pos.col == self.c_max {
                self.idx += 1;
                self.r_max -= 1;
            }
        } else if ch == 'V' {
            // 否则，若 字符 等于 'V'
            self.pos.row -= 1; // self.pos.row累减 1
            if self.pos.row == self.r_min {
                self.idx += 1;
                self.c_max -= 1;
            }
        } else if ch == 'M' {
            // 否则，若 字符 等于 'M'
            self.pos.col -= 1; // self.pos.col累减 1
            if self.pos.col == self.c_min {
                self.idx += 1;
                self.r_min += 1;
            }
        } else if ch == 'e' {
            // 否则，若 字符 等于 'e'
            self.pos.row += 1; // self.pos.row累加 1
            if self.pos.row == self.r_max {
                self.idx += 1;
                self.c_max -= 1;
            }
        } else if ch == 's' {
            // 否则，若 字符 等于 '字符串'
            self.pos.col += 1; // self.pos.col累加 1
            if self.pos.col == self.c_max {
                self.idx += 1;
                self.r_min += 1;
            }
        } else if ch == 'v' {
            // 否则，若 字符 等于 '值'
            self.pos.row -= 1; // self.pos.row累减 1
            if self.pos.row == self.r_min {
                self.idx += 1;
                self.c_min += 1;
            }
        } else if ch == 'm' {
            // 否则，若 字符 等于 '映射表'
            self.pos.col -= 1; // self.pos.col累减 1
            if self.pos.col == self.c_min {
                self.idx += 1;
                self.r_max -= 1;
            }
        }
        res // 结果
    }
}

fn test_filler(rule: &str, rn: i32, cn: i32) -> Vec<Vec<i32>> {
    // 定义函数/方法 test_filler
    let mut obj = Filler::new(rn, cn); // 把 Filler::new(rn, cn); 写入 let mut obj
    obj.set_rule(rule); // obj.set_rule(rule);
    let mut seq: Vec<Vec<i32>> = vec![]; // 把 vec取反 []; 写入 let mut seq: Vec<Vec<i32>>
    for _ in 0..(rn * cn) {
        // 逐个取出 0 的元素（_）
        let (r, c) = obj.next(); // 把 obj.下一个(); 写入 let (r, c)
        seq.push(vec![r, c]); // 把 vec取反 [右指针, 字符] 压入栈/数组尾部
    }
    seq // seq
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let want_esvm = vec![
        vec![0, 0],
        vec![1, 0],
        vec![2, 0],
        vec![3, 0],
        vec![3, 1],
        vec![3, 2],
        vec![3, 3],
        vec![2, 3],
        vec![1, 3],
        vec![0, 3],
        vec![0, 2],
        vec![0, 1],
        vec![1, 1],
        vec![2, 1],
        vec![2, 2],
        vec![1, 2],
    ];
    assert_eq!(test_filler("ESVM", 4, 4), want_esvm, "ESVM"); // 断言校验
    let want_semv = vec![
        vec![0, 0],
        vec![0, 1],
        vec![0, 2],
        vec![0, 3],
        vec![1, 3],
        vec![2, 3],
        vec![3, 3],
        vec![3, 2],
        vec![3, 1],
        vec![3, 0],
        vec![2, 0],
        vec![1, 0],
        vec![1, 1],
        vec![1, 2],
        vec![2, 2],
        vec![2, 1],
    ];
    assert_eq!(test_filler("semv", 4, 4), want_semv, "semv"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
