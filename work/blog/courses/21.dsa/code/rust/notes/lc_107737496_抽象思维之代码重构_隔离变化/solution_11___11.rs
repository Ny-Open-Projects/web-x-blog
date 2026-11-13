// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案11：Rule 循环游标）
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
    fn next(&mut self) -> char {
        // 定义函数/方法 next
        let ch = self.data[self.idx]; // 把 self.data[self.idx] 存入 字符
        self.idx = (self.idx + 1) % self.data.len(); // 把 (self.idx 加 1) 对…取模 self.data.长度(); 写入 self.idx
        ch // 字符
    }
    fn peek(&self) -> char {
        // 定义函数/方法 peek
        self.data[self.idx] // self.data[self.idx]
    }
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let mut r = Rule::new("ESVM"); // 把 Rule::new(「ESVM」); 写入 let mut r
    let s1: String = (0..10).map(|_| r.next()).collect();
    let mut r2 = Rule::new("semv"); // 把 Rule::new(「semv」); 写入 let mut r2
    let s2: String = (0..6).map(|_| r2.next()).collect();
    assert_eq!(s1, "ESVMESVMES", "rule1"); // 断言校验
    assert_eq!(s2, "semvse", "rule2"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
