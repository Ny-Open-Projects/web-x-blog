// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
// LeetCode 107431726. 最大红矩形分析 — Rust 版（方案A：逐行高度 + 暴力区间 / 卡片扩展）
fn get_result(n: usize, m: usize, matrix: &[&str]) -> i64 {
    // 定义函数/方法 get_result
    let bytes: Vec<&[u8]> = matrix.iter().map(|s| s.as_bytes()).collect();
    let mut ans = 0i64; // 把 0i64; 写入 let mut ans
    let mut height = vec![0i64; m + 2]; // 把 vec取反 [0i64; 映射表 加 2]; 写入 let mut height
    for k in 0..n {
        // 逐个取出 0 的元素（下标 k）
        for i in 1..=m {
            // 逐个取出 1 的元素（下标 i）
            if bytes[k][i - 1] == b'.' {
                // 若 bytes[下标 k][下标 i 减 1] 等于 b'.'
                height[i] += 1; // height[i]累加 1
            } else {
                // 否则
                height[i] = 0; // 把 0; 写入 height[i]
            }
        }
        for a in 1..=m {
            // 逐个取出 1 的元素（数组）
            let mut min_h = 50000i64; // 把 50000i64; 写入 let mut min_h
            for c in a..=m {
                // 逐个取出 数组 的元素（字符）
                if height[c] < min_h {
                    // 若 height[字符] 小于 min_h
                    min_h = height[c]; // 把 height[字符]; 写入 min_h
                }
            }
            let area = (m - a + 1) as i64 * min_h; // 把 (映射表 减 数组 加 1) as i64 乘 min_h 存入 area
            if area > ans {
                // 若 area 超过 答案
                ans = area; // 把 area; 写入 答案
            }
        }
    }
    ans // 答案
}

fn get_result_card(n: usize, m: usize, matrix: &[&str]) -> i64 {
    // 定义函数/方法 get_result_card
    let bytes: Vec<&[u8]> = matrix.iter().map(|s| s.as_bytes()).collect();
    let mut ans = 0i64; // 把 0i64; 写入 let mut ans
    let mut height = vec![0i64; m + 2]; // 把 vec取反 [0i64; 映射表 加 2]; 写入 let mut height
    for k in 0..n {
        // 逐个取出 0 的元素（下标 k）
        for i in 1..=m {
            // 逐个取出 1 的元素（下标 i）
            if bytes[k][i - 1] == b'.' {
                // 若 bytes[下标 k][下标 i 减 1] 等于 b'.'
                height[i] += 1; // height[i]累加 1
            } else {
                // 否则
                height[i] = 0; // 把 0; 写入 height[i]
            }
        }
        for a in 1..=m {
            // 逐个取出 1 的元素（数组）
            let cur_h = height[a]; // 把 height[数组] 存入 cur_h
            let mut lo = a as i64 - 1; // 把 数组 as i64 减 1; 写入 let mut lo
            while lo >= 1 && height[lo as usize] >= cur_h {
                // 把 1 且 height[左边界 as usize] 不低于 cur_h { 写入 while lo >
                lo -= 1; // 左边界累减 1
            }
            let mut hi = a + 1; // 把 数组 加 1; 写入 let mut hi
            while hi <= m && height[hi] >= cur_h {
                // 把 映射表 且 height[右边界] 不低于 cur_h { 写入 while hi <
                hi += 1; // 右边界累加 1
            }
            let area = (hi - lo as usize - 1) as i64 * cur_h; // 把 (右边界 减 左边界 as usize 减 1) as i64 乘 cur_h 存入 area
            if area > ans {
                // 若 area 超过 答案
                ans = area; // 把 area; 写入 答案
            }
        }
    }
    ans // 答案
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let matrix = [".....", "XXXXX", ".X...", "....."]; // 把 [「.....」, 「.....」, 「.....」, 「.....」] 存入 矩阵
    assert_eq!(get_result(4, 5, &matrix), 6, "brute"); // 断言校验
    assert_eq!(get_result_card(4, 5, &matrix), 6, "card"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
