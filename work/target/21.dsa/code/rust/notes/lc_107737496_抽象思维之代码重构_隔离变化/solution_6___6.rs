// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案6：Matrix 公开 buf 直接访问）
struct Matrix {
    // 定义类型
    row: usize,
    col: usize,
    buf: Vec<Vec<i32>>,
}

impl Matrix {
    // 实现块
    fn new(r: usize, c: usize) -> Self {
        // 定义函数/方法 new
        Matrix {
            row: r,
            col: c,
            buf: vec![vec![0i32; c]; r],
        }
    }
    fn call(&self, r: usize, c: usize) -> i32 {
        // 定义函数/方法 call
        self.buf[r][c] // self.buf[右指针][字符]
    }
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let mut m = Matrix::new(4, 5); // 把 Matrix::new(4, 5); 写入 let mut m
    for i in 0..4 {
        // 逐个取出 0 的元素（下标 i）
        for j in 0..5 {
            // 逐个取出 0 的元素（下标 j）
            m.buf[i][j] = (i * j) as i32; // 直接访问 buf
        }
    }
    assert_eq!(m.call(2, 3), 6, "matrix call"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
