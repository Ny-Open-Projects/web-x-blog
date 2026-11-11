// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案1：螺旋矩阵递归填充）
struct Matrix {
    // 定义类型
    n: usize,
    m: Vec<Vec<i32>>,
}

impl Matrix {
    // 实现块
    fn new(size: usize) -> Self {
        // 定义函数/方法 new
        Matrix {
            n: size,
            m: vec![vec![0i32; size]; size],
        } // Matrix { 元素个数: 大小, 映射表: vec取反 [vec取反 [0i32; 大小]; 大小] }
    }

    fn fill(&mut self, mut num: i32, begin: usize, size: usize) {
        // 定义函数/方法 fill
        if size == 0 {
            // 若 大小 等于 0
            return; // return;
        }
        if size == 1 {
            // 若 大小 等于 1
            self.m[begin][begin] = num; // 把 num; 写入 self.m[begin][begin]
            return; // return;
        }
        for j in 0..size - 1 {
            // 逐个取出 0 的元素（下标 j）
            self.m[begin + j][begin] = num; // 把 num; 写入 self.m[begin + j][begin]
            num += 1; // num累加 1
        }
        for j in 0..size - 1 {
            // 逐个取出 0 的元素（下标 j）
            self.m[begin + size - 1][begin + j] = num; // 把 num; 写入 self.m[begin + size - 1][begin + j]
            num += 1; // num累加 1
        }
        let mut j = size - 1; // 把 大小 减 1; 写入 let mut j
        while j > 0 {
            // while 下标 j 超过 0 {
            self.m[begin + j][begin + size - 1] = num; // 把 num; 写入 self.m[begin + j][begin + size - 1]
            num += 1; // num累加 1
            j -= 1; // 下标 j累减 1
        }
        let mut j = size - 1; // 把 大小 减 1; 写入 let mut j
        while j > 0 {
            // while 下标 j 超过 0 {
            self.m[begin][begin + j] = num; // 把 num; 写入 self.m[begin][begin + j]
            num += 1; // num累加 1
            j -= 1; // 下标 j累减 1
        }
        self.fill(num, begin + 1, size - 2); // self.fill(num, begin 加 1, 大小 减 2);
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
    let mut m = Matrix::new(6); // 把 Matrix::new(6); 写入 let mut m
    m.fill(1, 0, 6); // 映射表.fill(1, 0, 6);
    let rows: Vec<String> = m.m.iter().map(|r| fmt_row(r)).collect();
    let want = [
        " 1 20 19 18 17 16",
        " 2 21 32 31 30 15",
        " 3 22 33 36 29 14",
        " 4 23 34 35 28 13",
        " 5 24 25 26 27 12",
        " 6  7  8  9 10 11",
    ];
    for i in 0..6 {
        // 逐个取出 0 的元素（下标 i）
        assert_eq!(rows[i], want[i], "spiral6 row {}", i); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
