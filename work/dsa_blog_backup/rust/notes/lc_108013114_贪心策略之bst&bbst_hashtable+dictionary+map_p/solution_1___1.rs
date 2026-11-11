// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108013114
// LeetCode 108013114. 贪心策略之BST&BBST_hashtable+dictionary+map — Rust 版（贪心策略之 BST/BBST/哈希表：Kruskal 最小生成树（并查集 + 排序））
use std::collections::HashMap; // 引入依赖

fn kruskal_mst(edges: &[(i32, i32, i32)]) -> i32 {
    // 定义函数/方法 kruskal_mst
    let mut sorted = edges.to_vec(); // 把 边集.to_vec(); 写入 let mut sorted
    sorted.sort_by_key(|e| e.2); // sorted.sort_by_key( 按位或 e 按位或 e.2);
    let mut parent: HashMap<i32, i32> = HashMap::new(); // 把 HashMap::new(); 写入 let mut parent: HashMap<i32, i32>

    fn find(parent: &mut HashMap<i32, i32>, x: i32) -> i32 {
        // 定义函数/方法 find
        parent.entry(x).or_insert(x); // parent.entry(x).or_insert(x);
        let mut x = x; // 把 x; 写入 let mut x
        while parent[&x] != x {
            // 把 x { 写入 while parent[&x] !
            let px = parent[&x]; // 把 parent[ 按位与 x] 存入 px
            let ppx = parent[&px]; // 把 parent[ 按位与 px] 存入 ppx
            parent.insert(x, ppx); // parent 插入 x, ppx);
            x = ppx; // 把 ppx; 写入 x
        }
        x
    }

    let mut total = 0; // 把 0; 写入 let mut total
    for &(u, v, w) in &sorted {
        // for 按位与 (节点 u, 值, 权重) in 按位与 sorted {
        let ru = find(&mut parent, u); // 把 find( 按位与 mut parent, 节点 u) 存入 ru
        let rv = find(&mut parent, v); // 把 find( 按位与 mut parent, 值) 存入 rv
        if ru != rv {
            // 若 ru 不等于 rv
            parent.insert(ru, rv); // parent 插入 ru, rv);
            total += w; // 总和累加 权重
        }
    }
    total // 总和
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let cases: Vec<(Vec<(i32, i32, i32)>, i32)> = vec![
        (
            vec![(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)],
            19,
        ),
        (vec![(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4)], 10),
        (vec![(0, 1, 2), (1, 2, 3)], 5),
        (vec![], 0),
    ];
    for (idx, (edges, want)) in cases.iter().enumerate() {
        // for (idx, (边集, want)) in cases.iter().enumerate() {
        let got = kruskal_mst(edges); // 把 kruskal_mst(边集) 存入 got
        assert_eq!(got, *want, "case {} failed", idx); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
