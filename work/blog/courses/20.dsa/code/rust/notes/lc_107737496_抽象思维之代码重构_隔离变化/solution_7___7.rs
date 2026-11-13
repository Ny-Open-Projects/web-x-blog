// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案7：螺旋矩阵分派表 place）
enum Move {
    // 定义类型
    Keep(usize, usize),
    Turn(usize, usize, char),
}

fn place(row: usize, col: usize, direction: char, n: usize, m: &[Vec<i32>]) -> Move {
    // 定义函数/方法 place
    match direction {
        // 按情况匹配处理
        'D' => {
            if row + 1 < n && m[row + 1][col] == 0 {
                // 若 row 加 1 小于 元素个数 且 映射表[row 加 1][col] 等于 0
                Move::Keep(row + 1, col) // Move::Keep(row 加 1, col)
            } else {
                // 否则
                Move::Turn(row, col + 1, 'R') // Move::Turn(row, col 加 1, 'R')
            }
        }
        'R' => {
            if col + 1 < n && m[row][col + 1] == 0 {
                // 若 col 加 1 小于 元素个数 且 映射表[row][col 加 1] 等于 0
                Move::Keep(row, col + 1) // Move::Keep(row, col 加 1)
            } else {
                // 否则
                Move::Turn(row - 1, col, 'U') // Move::Turn(row 减 1, col, 'U')
            }
        }
        'U' => {
            if row >= 1 && m[row - 1][col] == 0 {
                // 若 row 不低于 1 且 映射表[row 减 1][col] 等于 0
                Move::Keep(row - 1, col) // Move::Keep(row 减 1, col)
            } else {
                // 否则
                Move::Turn(row, col - 1, 'L') // Move::Turn(row, col 减 1, 'L')
            }
        }
        _ => {
            if col >= 1 && m[row][col - 1] == 0 {
                // 若 col 不低于 1 且 映射表[row][col 减 1] 等于 0
                Move::Keep(row, col - 1) // Move::Keep(row, col 减 1)
            } else {
                // 否则
                Move::Turn(row + 1, col, 'D') // Move::Turn(row 加 1, col, 'D')
            }
        }
    }
}

fn fill_spiral(n: usize) -> Vec<Vec<i32>> {
    // 定义函数/方法 fill_spiral
    let mut m = vec![vec![0i32; n]; n]; // 把 vec取反 [vec取反 [0i32; 元素个数]; 元素个数]; 写入 let mut m
    let (mut row, mut col) = (0usize, 0usize); // 把 (0usize, 0usize); 写入 let (mut row, mut col)
    let mut direction = 'D'; // 把 'D'; 写入 let mut direction
    let mut num = 1i32; // 把 1i32; 写入 let mut num
    while num <= (n * n) as i32 {
        // 把 (元素个数 乘 元素个数) as i32 { 写入 while num <
        m[row][col] = num; // 把 num; 写入 m[row][col]
        num += 1; // num累加 1
        match place(row, col, direction, n, &m) {
            // 定义函数/方法 place
            Move::Keep(r, c) => {
                row = r; // 把 右指针; 写入 row
                col = c; // 把 字符; 写入 col
            }
            Move::Turn(r, c, d) => {
                row = r; // 把 右指针; 写入 row
                col = c; // 把 字符; 写入 col
                direction = d; // 把 d; 写入 direction
            }
        }
    }
    m // 映射表
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let got3 = fill_spiral(3); // 把 fill_spiral(3) 存入 got3
    assert_eq!(
        got3,
        vec![vec![1, 8, 7], vec![2, 9, 6], vec![3, 4, 5]],
        "spiral3"
    ); // 断言校验
    let got4 = fill_spiral(4); // 把 fill_spiral(4) 存入 got4
    assert_eq!(
        got4,
        vec![
            vec![1, 12, 11, 10],
            vec![2, 13, 16, 9],
            vec![3, 14, 15, 8],
            vec![4, 5, 6, 7]
        ],
        "spiral4"
    ); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
