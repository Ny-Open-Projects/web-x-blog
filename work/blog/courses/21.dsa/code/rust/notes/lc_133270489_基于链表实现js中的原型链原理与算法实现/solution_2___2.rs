// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — Rust 版（方案2：get 沿原型链查找属性）
use std::cell::RefCell; // 引入依赖
use std::collections::HashMap; // 引入依赖
use std::rc::Rc; // 引入依赖

struct Proto {
    // 定义类型
    name: String,
    props: RefCell<HashMap<String, String>>,
    parent: Option<Rc<Proto>>,
}

impl Proto {
    // 实现块
    fn new(name: &str, parent: Option<Rc<Proto>>) -> Rc<Proto> {
        // 定义函数/方法 new
        Rc::new(Proto {
            // Rc::new(Proto {
            name: name.to_string(),
            props: RefCell::new(HashMap::new()),
            parent,
        }) // })
    }
    fn set(&self, key: &str, value: &str) {
        // 定义函数/方法 set
        self.props
            .borrow_mut()
            .insert(key.to_string(), value.to_string());
    }
    fn get(&self, key: &str) -> Option<String> {
        // 定义函数/方法 get
        // 从自身开始沿链查找
        if let Some(v) = self.props.borrow().get(key) {
            // 若 let Some(值) 赋值为 self.props.borrow() 查找 key
            return Some(v.clone()); // 返回 Some(值.clone())
        }
        let mut cur = self.parent.as_ref(); // 把 self.parent.as_ref(); 写入 let mut cur
        while let Some(node) = cur {
            // 边取边处理，取空即停
            if let Some(v) = node.props.borrow().get(key) {
                // 若 let Some(值) 赋值为 节点.props.borrow() 查找 key
                return Some(v.clone()); // 返回 Some(值.clone())
            }
            cur = node.parent.as_ref(); // 把 节点.parent.as_ref(); 写入 当前值
        }
        None // None
    }
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let object_proto = Proto::new("Object.prototype", None); // 把 Proto::new(「Object.prototype」, None) 存入 object_proto
    object_proto.set("x", "x"); // object_proto.set(「x」, 「x」);
    let function_proto = Proto::new("Function.prototype", Some(object_proto.clone()));
    function_proto.set("y", "y"); // function_proto.set(「y」, 「y」);
    let array_proto = Proto::new("Array.prototype", Some(object_proto.clone()));
    array_proto.set("z", "z"); // array_proto.set(「z」, 「z」);
    let obj = Proto::new("obj", Some(object_proto.clone())); // 把 Proto::new(「obj」, Some(object_proto.clone())) 存入 obj
    let func = Proto::new("func", Some(function_proto.clone())); // 把 Proto::new(「func」, Some(function_proto.clone())) 存入 func
    let arr = Proto::new("arr", Some(array_proto.clone())); // 把 Proto::new(「数组」, Some(array_proto.clone())) 存入 数组

    assert_eq!(obj.get("x").as_deref(), Some("x"), "case 0 failed"); // 断言校验
    assert_eq!(func.get("y").as_deref(), Some("y"), "case 1 failed"); // 断言校验
    assert_eq!(arr.get("z").as_deref(), Some("z"), "case 2 failed"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
