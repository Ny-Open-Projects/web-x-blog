// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案12：Location/Rule/Filler 组合）
#[derive(Clone)]
struct Rule {
    // 定义类型
    data: Vec<char>,
    idx: usize,
}

impl Rule {
    // 实现块
    fn new(r: &str) -> Self {
        // 定义函数/方法 new
        Rule {
            data: r.chars().collect(),
            idx: 0,
        } // Rule { data: 右指针.chars().collect(), idx: 0 }
    }
    fn current(&self) -> char {
        // 定义函数/方法 current
        self.data[self.idx] // self.data[self.idx]
    }
    fn advance(&mut self) {
        // 定义函数/方法 advance
        self.idx = (self.idx + 1) % self.data.len(); // 把 (self.idx 加 1) 对…取模 self.data.长度(); 写入 self.idx
    }
}

struct Filler {
    // 定义类型
    pos: (i32, i32),
    r_min: i32,
    c_min: i32,
    r_max: i32,
    c_max: i32,
    cmd: Rule,
}

impl Filler {
    // 实现块
    fn new(rn: i32, cn: i32, rule: &str) -> Self {
        // 定义函数/方法 new
        Filler {
            // Filler {
            pos: (0, 0),
            r_min: 0,
            c_min: 0,
            r_max: rn - 1,
            c_max: cn - 1,
            cmd: Rule::new(rule),
        }
    }
    fn next(&mut self) -> (i32, i32) {
        // 定义函数/方法 next
        let res = self.pos; // 把 self.pos 存入 结果
        let ch = self.cmd.current(); // 把 self.cmd.current() 存入 字符
        if ch == 'E' {
            // 若 字符 等于 'E'
            self.pos.0 += 1; // self.pos.0累加 1
            if self.pos.0 == self.r_max {
                self.cmd.advance();
                self.c_min += 1;
            }
        } else if ch == 'S' {
            // 否则，若 字符 等于 'S'
            self.pos.1 += 1; // self.pos.1累加 1
            if self.pos.1 == self.c_max {
                self.cmd.advance();
                self.r_max -= 1;
            }
        } else if ch == 'V' {
            // 否则，若 字符 等于 'V'
            self.pos.0 -= 1; // self.pos.0累减 1
            if self.pos.0 == self.r_min {
                self.cmd.advance();
                self.c_max -= 1;
            }
        } else if ch == 'M' {
            // 否则，若 字符 等于 'M'
            self.pos.1 -= 1; // self.pos.1累减 1
            if self.pos.1 == self.c_min {
                self.cmd.advance();
                self.r_min += 1;
            }
        }
        res // 结果
    }
}

fn test_filler(rule: &str, rn: i32, cn: i32) -> Vec<Vec<i32>> {
    // 定义函数/方法 test_filler
    let mut obj = Filler::new(rn, cn, rule); // 把 Filler::new(rn, cn, rule); 写入 let mut obj
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
    let want = vec![
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
    assert_eq!(test_filler("ESVM", 4, 4), want, "filler4"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
