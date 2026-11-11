// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145078849
// LeetCode 341. 扁平化嵌套列表迭代器 — Rust 版（方案4）
// NestedInteger 用枚举模拟
#[derive(Clone, Debug)]
enum NI {
    Int(i32),
    List(Vec<NI>),
} // 定义类型
fn flatten(nested: Vec<NI>) -> Vec<i32> {
    // 定义函数/方法 flatten
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    fn go(items: &[NI], out: &mut Vec<i32>) {
        // 定义函数/方法 go
        for it in items {
            // 逐个取出 items 的元素（it）
            match it {
                // 按情况匹配处理
                NI::Int(v) => out.push(*v),
                NI::List(l) => go(l, out),
            }
        }
    }
    go(&nested, &mut out); // go( 按位与 nested, 按位与 mut out);
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let nested = vec![
        NI::Int(1),
        NI::List(vec![NI::Int(2), NI::List(vec![NI::Int(3), NI::Int(4)])]),
    ];
    assert_eq!(flatten(nested), vec![1, 2, 3, 4]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
