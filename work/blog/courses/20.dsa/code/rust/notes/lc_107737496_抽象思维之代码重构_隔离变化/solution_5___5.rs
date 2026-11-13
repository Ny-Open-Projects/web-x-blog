// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案5：Matrix 封装 set/call）
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
    fn set(&mut self, r: usize, c: usize, v: i32) {
        // 定义函数/方法 set
        self.buf[r][c] = v; // 把 值; 写入 self.buf[r][c]
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
            m.set(i, j, (i * j) as i32); // 映射表.set(下标 i, 下标 j, (下标 i 乘 下标 j) as i32);
        }
    }
    assert_eq!(m.call(2, 3), 6, "matrix call"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
