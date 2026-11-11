// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
// LeetCode 107524703. 人鬼渡河问题 — Rust 版（方案3：DFS+奇偶步求解）
use std::cell::RefCell;
use std::collections::HashSet; // 引入依赖 // 引入依赖

const D: [[i32; 2]; 5] = [[2, 0], [1, 0], [1, 1], [0, 1], [0, 2]];

fn safe(r: i32, g: i32) -> bool {
    // 定义函数/方法 safe
    0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g)
}

fn solve() -> Vec<[i32; 2]> {
    // 定义函数/方法 solve
    let path: RefCell<Vec<[i32; 2]>> = RefCell::new(vec![]);
    let visited: RefCell<HashSet<String>> = RefCell::new(HashSet::new());

    fn dfs(
        r: i32,
        g: i32,
        step: i32,
        visited: &RefCell<HashSet<String>>,
        path: &RefCell<Vec<[i32; 2]>>,
    ) -> bool {
        // 定义函数/方法 dfs
        if r == 0 && g == 0 {
            // 若 右指针 等于 0 且 g 等于 0
            return true; // 返回 true
        }
        let key = format!("{},{},{}", r, g, step % 2); // 把 format取反 (「{},{},{}」, 右指针, g, 步数 对…取模 2) 存入 key
        if visited.borrow().contains(&key) {
            // 若 已访问集合.borrow() 是否包含 按位与 key
            return false; // 返回 false
        }
        visited.borrow_mut().insert(key); // 已访问集合.borrow_mut() 插入 key);
        let odd = step % 2 == 1; // 把 步数 对…取模 2 等于 1 存入 odd
        for d in D.iter() {
            // 逐个取出 D 的元素（d）
            let (dr, dg) = (d[0], d[1]); // 把 (d[0], d[1]); 写入 let (dr, dg)
            let (nr, ng); // let (nr, ng);
            if odd {
                // 若 odd
                if r < dr || g < dg {
                    // 若 右指针 小于 dr 或 g 小于 dg
                    continue; // 跳过本轮，进入下一次
                }
                nr = r - dr; // 把 右指针 减 dr; 写入 nr
                ng = g - dg; // 把 g 减 dg; 写入 ng
            } else {
                // 否则
                if (3 - r) < dr || (3 - g) < dg {
                    // 若 3 减 右指针) 小于 dr 或 (3 减 g) 小于 dg
                    continue; // 跳过本轮，进入下一次
                }
                nr = r + dr; // 把 右指针 加 dr; 写入 nr
                ng = g + dg; // 把 g 加 dg; 写入 ng
            }
            if !safe(nr, ng) {
                // 若 取反 safe(nr, ng
                continue; // 跳过本轮，进入下一次
            }
            if dfs(nr, ng, step + 1, visited, path) {
                // 定义函数/方法 dfs
                path.borrow_mut().push([dr, dg]); // 把 [dr, dg] 压入栈/数组尾部
                return true; // 返回 true
            }
        }
        false // false
    }

    dfs(3, 3, 1, &visited, &path); // dfs(3, 3, 1, 按位与 已访问集合, 按位与 当前路径);
    let mut p = path.borrow().clone(); // 把 当前路径.borrow().clone(); 写入 let mut p
    p.reverse(); // 反转
    p // 节点
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let want: Vec<[i32; 2]> = vec![
        [1, 1],
        [1, 0],
        [0, 2],
        [0, 1],
        [2, 0],
        [1, 1],
        [2, 0],
        [0, 1],
        [0, 2],
        [1, 0],
        [1, 1],
    ];
    let got = solve(); // 把 solve() 存入 got
    assert_eq!(got.len(), want.len(), "solve length mismatch"); // 断言校验
    for i in 0..want.len() {
        // 逐个取出 0 的元素（下标 i）
        assert_eq!(got[i], want[i], "solve at {} mismatch", i); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
