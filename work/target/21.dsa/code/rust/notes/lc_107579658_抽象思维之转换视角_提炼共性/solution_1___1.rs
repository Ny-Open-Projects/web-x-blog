// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107579658
// LeetCode 107579658. 转换视角，提炼共性 — Rust 版（抽象思维之转换视角：统一分书问题与八皇后的回溯框架）
// queen=false: 分书问题（5人，like 偏好矩阵）; queen=true: 八皇后

const LIKE: [[i32; 5]; 5] = [
    [0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
];

struct Ctx {
    // 定义类型
    queen: bool,
    size: usize,
    q: Vec<i32>,
    rows: Vec<bool>,
    diag1: Vec<bool>,
    diag2: Vec<bool>,
    results: Vec<Vec<i32>>,
}

impl Ctx {
    // 实现块
    fn is_valid(&self, row: usize, col: usize) -> bool {
        // 定义判定函数 is_valid
        if self.queen {
            // 若 self.queen
            true // true
        } else {
            // 否则
            LIKE[row][col] == 1 // 把 赋值为 1 写入 LIKE[row][col]
        }
    }

    fn is_safe(&self, row: usize, col: usize) -> bool {
        // 定义判定函数 is_safe
        if self.queen {
            // 若 self.queen
            self.rows[row] && self.diag1[col + self.size - 1 - row] && self.diag2[col + row]
        } else {
            // 否则
            self.rows[row] // self.行数[row]
        }
    }

    fn place(&mut self, col: usize) {
        // 定义函数/方法 place
        if col == self.size {
            // 若 col 等于 self.大小
            self.results.push(self.q.clone()); // 把 self.节点.clone( 压入栈/数组尾部
            return; // return;
        }
        for row in 0..self.size {
            // 逐个取出 0 的元素（row）
            if !self.is_valid(row, col) {
                // 若 取反 self.is_valid(row, col
                continue; // 跳过本轮，进入下一次
            }
            if !self.is_safe(row, col) {
                // 若 取反 self.is_safe(row, col
                continue; // 跳过本轮，进入下一次
            }
            self.q[col] = row as i32; // 把 row as i32; 写入 self.q[col]
            self.rows[row] = false; // 把 false; 写入 self.rows[row]
            if self.queen {
                // 若 self.queen
                let d1 = col + self.size - 1 - row; // 把 col 加 self.大小 减 1 减 row 存入 d1
                let d2 = col + row; // 把 col 加 row 存入 d2
                self.diag1[d1] = false; // 把 false; 写入 self.diag1[d1]
                self.diag2[d2] = false; // 把 false; 写入 self.diag2[d2]
            }
            self.place(col + 1); // self.place(col 加 1);
            self.rows[row] = true; // 把 true; 写入 self.rows[row]
            if self.queen {
                // 若 self.queen
                let d1 = col + self.size - 1 - row; // 把 col 加 self.大小 减 1 减 row 存入 d1
                let d2 = col + row; // 把 col 加 row 存入 d2
                self.diag1[d1] = true; // 把 true; 写入 self.diag1[d1]
                self.diag2[d2] = true; // 把 true; 写入 self.diag2[d2]
            }
        }
    }
}

fn solve_unified(queen: bool) -> Vec<Vec<i32>> {
    // 定义函数/方法 solve_unified
    let size = if queen { 8usize } else { 5usize }; // 把 if queen { 8usize } else { 5usize } 存入 大小
    let mut ctx = Ctx {
        // 把 Ctx { 写入 let mut ctx
        queen,
        size,
        q: vec![-1i32; size],
        rows: vec![true; size],
        diag1: vec![true; 2 * size - 1],
        diag2: vec![true; 2 * size - 1],
        results: vec![],
    };
    ctx.place(0); // ctx.place(0);
    ctx.results // ctx.results
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let want: Vec<Vec<i32>> = vec![vec![1, 2, 0, 3, 4], vec![1, 4, 0, 3, 2]];
    let got = solve_unified(false); // 把 solve_unified(false) 存入 got
    assert_eq!(got, want, "solve_unified(false) mismatch"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
