// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
// LeetCode 107524703. 人鬼渡河问题 — Rust 版（方案4：方向入状态的 DFS 变体，断言无可行路径）
use std::collections::HashSet; // 引入依赖

const D: [[i32; 2]; 5] = [[2, 0], [1, 0], [1, 1], [0, 1], [0, 2]];

fn safe(r: i32, g: i32) -> bool {
    // 定义函数/方法 safe
    0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g)
}

fn solve() -> Vec<[i32; 2]> {
    // 定义函数/方法 solve
    let mut path: Vec<[i32; 2]> = vec![]; // 把 vec取反 []; 写入 let mut path: Vec<[i32; 2]>
    let mut visited: HashSet<String> = HashSet::new(); // 把 HashSet::new(); 写入 let mut visited: HashSet<String>

    fn jump(
        dir: i32,
        r: i32,
        g: i32,
        step: i32,
        visited: &mut HashSet<String>,
        path: &mut Vec<[i32; 2]>,
    ) -> bool {
        // 定义函数/方法 jump
        if r == 0 && g == 0 && step % 2 == 0 {
            // 若 右指针 等于 0 且 g 等于 0 且 步数 对…取模 2 等于 0
            return true; // 返回 true
        }
        let key = format!("{},{},{}", r, g, step % 2); // 把 format取反 (「{},{},{}」, 右指针, g, 步数 对…取模 2) 存入 key
        if visited.contains(&key) {
            // 若 已访问集合 是否包含 按位与 key
            return false; // 返回 false
        }
        visited.insert(key); // 已访问集合 插入 key);
        for d in D.iter() {
            // 逐个取出 D 的元素（d）
            let (dr, dg) = (d[0], d[1]); // 把 (d[0], d[1]); 写入 let (dr, dg)
            let nr = r + dir * dr; // 把 右指针 加 dir 乘 dr 存入 nr
            let ng = g + dir * dg; // 把 g 加 dir 乘 dg 存入 ng
            if !safe(nr, ng) {
                // 若 取反 safe(nr, ng
                continue; // 跳过本轮，进入下一次
            }
            if jump(-dir, nr, ng, step + 1, visited, path) {
                // 定义函数/方法 jump
                path.push([dr, dg]); // 把 [dr, dg] 压入栈/数组尾部
                return true; // 返回 true
            }
        }
        false // false
    }

    jump(-1, 3, 3, 0, &mut visited, &mut path); // jump( 减 1, 3, 3, 0, 按位与 mut 已访问集合, 按位与 mut 当前路径);
    path.reverse(); // 反转
    path // 当前路径
}

fn main() {
    // 程序入口：跑内嵌自测用例
    // 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解）
    let got = solve(); // 把 solve() 存入 got
    assert!(got.is_empty(), "solve 应返回空路径"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
