// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案7：八皇后位置对列表）
fn n_queens_simple(n: usize) -> Vec<Vec<i32>> {
    // 定义函数/方法 n_queens_simple
    let mut solutions: Vec<Vec<i32>> = vec![]; // 把 vec取反 []; 写入 let mut solutions: Vec<Vec<i32>>

    fn safe(positions: &[(i32, i32)], r: i32, c: i32) -> bool {
        // 定义函数/方法 safe
        for &(rr, cc) in positions {
            // for 按位与 (rr, cc) in positions {
            if rr == r || (rr - r).abs() == (cc - c).abs() {
                // 若 rr 等于 右指针 或 (rr 减 右指针).取绝对值 ) 等于 (cc 减 字符).取绝对值
                return false; // 返回 false
            }
        }
        true // true
    }

    fn solve(col: usize, n: usize, positions: &mut Vec<(i32, i32)>, solutions: &mut Vec<Vec<i32>>) {
        // 定义函数/方法 solve
        if col == n {
            // 若 col 等于 元素个数
            solutions.push(positions.iter().map(|p| p.0).collect()); // 把 positions.iter( 压入栈/数组尾部
            return; // return;
        }
        for r in 0..n as i32 {
            // 逐个取出 0 的元素（右指针）
            if safe(positions, r, col as i32) {
                // 定义函数/方法 safe
                positions.push((r, col as i32)); // 把 (右指针, col as i32 压入栈/数组尾部
                solve(col + 1, n, positions, solutions); // solve(col 加 1, 元素个数, positions, solutions);
                positions.pop(); // 弹出栈顶元素
            }
        }
    }

    solve(0, n, &mut vec![], &mut solutions); // solve(0, 元素个数, 按位与 mut vec取反 [], 按位与 mut solutions);
    solutions // solutions
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let cases: Vec<(usize, usize, Option<Vec<i32>>)> = vec![
        (8, 92, Some(vec![0, 4, 7, 5, 2, 6, 1, 3])),
        (1, 1, Some(vec![0])),
        (2, 0, None),
        (4, 2, Some(vec![1, 3, 0, 2])),
    ];
    for (idx, (n, count, first)) in cases.iter().enumerate() {
        // for (idx, (元素个数, 计数, first)) in cases.iter().enumerate() {
        let sols = n_queens_simple(*n); // 把 n_queens_simple( 乘 元素个数) 存入 sols
        assert_eq!(sols.len(), *count, "case {} count mismatch", idx); // 断言校验
        if let Some(w) = first {
            // 若 let Some(权重) 赋值为 first
            assert_eq!(&sols[0], w, "case {} first mismatch", idx); // 断言校验
        }
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
