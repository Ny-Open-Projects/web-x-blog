// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案4：螺旋矩阵方向模拟 placeFill）
fn place_fill(n: usize) -> Vec<Vec<i32>> {
    // 定义函数/方法 place_fill
    let mut m = vec![vec![0i32; n]; n]; // 把 vec取反 [vec取反 [0i32; 元素个数]; 元素个数]; 写入 let mut m
    let (mut row, mut col) = (0usize, 0usize); // 把 (0usize, 0usize); 写入 let (mut row, mut col)
    let mut direction = 'D'; // 把 'D'; 写入 let mut direction
    let mut num = 1i32; // 把 1i32; 写入 let mut num
    let total = n * n; // 把 元素个数 乘 元素个数 存入 总和
    while num <= total as i32 {
        // 把 总和 as i32 { 写入 while num <
        m[row][col] = num; // 把 num; 写入 m[row][col]
        num += 1; // num累加 1
        if direction == 'D' {
            // 若 direction 等于 'D'
            if row + 1 < n && m[row + 1][col] == 0 {
                // 若 row 加 1 小于 元素个数 且 映射表[row 加 1][col] 等于 0
                row += 1; // row累加 1
            } else {
                // 否则
                direction = 'R'; // 把 'R'; 写入 direction
                col += 1; // col累加 1
            }
        } else if direction == 'R' {
            // 否则，若 direction 等于 'R'
            if col + 1 < n && m[row][col + 1] == 0 {
                // 若 col 加 1 小于 元素个数 且 映射表[row][col 加 1] 等于 0
                col += 1; // col累加 1
            } else {
                // 否则
                direction = 'U'; // 把 'U'; 写入 direction
                row -= 1; // row累减 1
            }
        } else if direction == 'U' {
            // 否则，若 direction 等于 'U'
            if row >= 1 && m[row - 1][col] == 0 {
                // 若 row 不低于 1 且 映射表[row 减 1][col] 等于 0
                row -= 1; // row累减 1
            } else {
                // 否则
                direction = 'L'; // 把 'L'; 写入 direction
                col -= 1; // col累减 1
            }
        } else {
            // 否则
            if col >= 1 && m[row][col - 1] == 0 {
                // 若 col 不低于 1 且 映射表[row][col 减 1] 等于 0
                col -= 1; // col累减 1
            } else {
                // 否则
                direction = 'D'; // 把 'D'; 写入 direction
                row += 1; // row累加 1
            }
        }
    }
    m // 映射表
}

fn eq_mat(a: &[Vec<i32>], b: &[&[i32]]) -> bool {
    // 定义函数/方法 eq_mat
    a.len() == b.len()  // 把 赋值为 b.长度() 写入 a.len()
        && a.iter().zip(b.iter()).all(|(x, y)| x.as_slice() == *y)
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let got3 = place_fill(3); // 把 place_fill(3) 存入 got3
    assert!(
        eq_mat(&got3, &[&[1, 8, 7], &[2, 9, 6], &[3, 4, 5]]),
        "place3"
    ); // 断言校验
    let got4 = place_fill(4); // 把 place_fill(4) 存入 got4
    assert!(
        eq_mat(
            &got4,
            &[
                &[1, 12, 11, 10],
                &[2, 13, 16, 9],
                &[3, 14, 15, 8],
                &[4, 5, 6, 7]
            ]
        ),
        "place4"
    ); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
