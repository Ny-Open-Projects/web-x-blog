// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/98685358
// LeetCode 98685358. 农夫过河问题 — Rust 版（农夫过河问题：BFS 求最短过河序列，状态 (农夫,狼,羊,菜)，0=左岸 1=右岸）
use std::collections::HashMap; // 引入依赖

// 安全判定：狼与羊单独相处或羊与菜单独相处则不安全
fn is_safe(s: &[i32; 4]) -> bool {
    // 定义判定函数 is_safe
    let (farmer, wolf, goat, cabbage) = (s[0], s[1], s[2], s[3]);
    if wolf == goat && farmer != wolf {
        // 若 wolf 等于 goat 且 farmer 不等于 wolf
        return false; // 返回 false
    }
    if goat == cabbage && farmer != goat {
        // 若 goat 等于 cabbage 且 farmer 不等于 goat
        return false; // 返回 false
    }
    true // true
}

fn key(s: &[i32; 4]) -> String {
    // 定义函数/方法 key
    format!("{},{},{},{}", s[0], s[1], s[2], s[3]) // format取反 (「{},{},{},{}」, 字符串[0], 字符串[1], 字符串[2], 字符串[3])
}

fn solve() -> Option<Vec<[i32; 4]>> {
    // 定义函数/方法 solve
    let start = [0, 0, 0, 0]; // 把 [0, 0, 0, 0] 存入 起点
    let goal = [1, 1, 1, 1]; // 把 [1, 1, 1, 1] 存入 goal
    let mut prev: HashMap<String, Option<[i32; 4]>> = HashMap::new();
    prev.insert(key(&start), None); // 前一个 插入 key( 按位与 起点), None);
    let mut q: Vec<[i32; 4]> = vec![start]; // 把 vec取反 [起点]; 写入 let mut q: Vec<[i32; 4]>
    let mut head = 0usize; // 把 0usize; 写入 let mut head
    while head < q.len() {
        // while 头节点 小于 节点.长度() {
        let cur = q[head]; // 把 节点[头节点] 存入 当前值
        head += 1; // 头节点累加 1
        let cur_key = key(&cur); // 把 key( 按位与 当前值) 存入 cur_key
        if cur == goal {
            // 若 当前值 等于 goal
            let mut path: Vec<[i32; 4]> = vec![]; // 把 vec取反 []; 写入 let mut path: Vec<[i32; 4]>
            let mut k: Option<[i32; 4]> = Some(cur); // 把 Some(当前值); 写入 let mut k: Option<[i32; 4]>
            while let Some(s) = k {
                // 边取边处理，取空即停
                path.push(s); // 把 字符串 压入栈/数组尾部
                k = *prev.get(&key(&s)).unwrap(); // 把 乘 前一个 查找 按位与 key( 按位与 字符串)).unwrap(); 写入 下标 k
            }
            path.reverse(); // 反转
            return Some(path); // 返回 Some(当前路径)
        }
        let farmer = cur[0]; // 把 当前值[0] 存入 farmer
        for i in 0..4usize {
            // 逐个取出 0 的元素（下标 i）
            if i != 0 && cur[i] != farmer {
                // 若 下标 i 不等于 0 且 当前值[下标 i] 不等于 farmer
                continue; // 跳过本轮，进入下一次
            }
            let mut nxt = cur; // 把 当前值; 写入 let mut nxt
            nxt[0] = 1 - farmer; // 把 1 减 farmer; 写入 nxt[0]
            if i != 0 {
                // 若 下标 i 不等于 0
                nxt[i] = 1 - farmer; // 把 1 减 farmer; 写入 nxt[i]
            }
            let nk = key(&nxt); // 把 key( 按位与 nxt) 存入 nk
            if prev.contains_key(&nk) {
                // 若 前一个.contains_key( 按位与 nk
                continue; // 跳过本轮，进入下一次
            }
            if !is_safe(&nxt) {
                // 若 取反 is_safe( 按位与 nxt
                continue; // 跳过本轮，进入下一次
            }
            prev.insert(nk, Some(cur)); // 前一个 插入 nk, Some(当前值));
            q.push(nxt); // 把 nxt 压入栈/数组尾部
        }
    }
    None // None
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let want: Vec<[i32; 4]> = vec![
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 0, 1, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 1],
        [1, 1, 1, 1],
    ];
    let path = solve().expect("FAILED: 无解"); // 把 solve().expect(「FAILED: 无解」) 存入 当前路径
    assert_eq!(path, want, "path mismatch"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
