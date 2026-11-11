// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133530983
// 数据结构与算法之堆: 实现最大堆类及堆排序 — Rust 版（方案1）
fn max_heap_pop_all(input: &[i32]) -> Vec<i32> {
    // 定义函数/方法 max_heap_pop_all
    let mut h: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut h: Vec<i32>
    for &v in input {
        // for 按位与 值 in input {
        h.push(v); // 把 值 压入栈/数组尾部
        let mut i = h.len() - 1; // 把 h.长度() 减 1; 写入 let mut i
        while i > 0 {
            // while 下标 i 超过 0 {
            let p = (i - 1) / 2; // 把 (下标 i 减 1) 除以 2 存入 节点
            if h[p] >= h[i] {
                break;
            } // 若 h[节点] 不低于 h[下标 i] { break; }
            h.swap(p, i); // h.交换 节点, 下标 i);
            i = p; // 把 节点; 写入 下标 i
        }
    }
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    while !h.is_empty() {
        // while 取反 h 是否为空 {
        out.push(h[0]); // 把 h[0] 压入栈/数组尾部
        let last = h.pop().unwrap(); // 把 h 弹出 ).unwrap() 存入 last
        if !h.is_empty() {
            // 若 取反 h.is_empty(
            h[0] = last; // 把 last; 写入 h[0]
            let mut i = 0usize; // 把 0usize; 写入 let mut i
            loop {
                // loop {
                let (l, r) = (2 * i + 1, 2 * i + 2); // 把 (2 乘 下标 i 加 1, 2 乘 下标 i 加 2); 写入 let (l, r)
                let mut m = i; // 把 下标 i; 写入 let mut m
                if l < h.len() && h[l] > h[m] {
                    m = l;
                } // 若 左指针 小于 h.长度() 且 h[左指针] 超过 h[映射表] { 映射表 赋值为 左指针; }
                if r < h.len() && h[r] > h[m] {
                    m = r;
                } // 若 右指针 小于 h.长度() 且 h[右指针] 超过 h[映射表] { 映射表 赋值为 右指针; }
                if m == i {
                    break;
                } // 若 映射表 等于 下标 i { break; }
                h.swap(i, m); // h.交换 下标 i, 映射表);
                i = m; // 把 映射表; 写入 下标 i
            }
        }
    }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        max_heap_pop_all(&[3, 1, 6, 5, 2, 4]),
        vec![6, 5, 4, 3, 2, 1]
    ); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
