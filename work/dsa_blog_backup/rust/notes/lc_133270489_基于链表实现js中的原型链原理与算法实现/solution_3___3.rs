// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — Rust 版（方案3：get 查找 + instanceOf 判定）
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

fn instance_of(obj: &Rc<Proto>, prototype: &Rc<Proto>) -> bool {
    // 定义函数/方法 instance_of
    let mut p: Option<&Rc<Proto>> = Some(obj); // 把 Some(obj); 写入 let mut p: Option<&Rc<Proto>>
    while let Some(cur) = p {
        // 边取边处理，取空即停
        if std::ptr::eq(cur.as_ref(), prototype.as_ref()) {
            // 若 std::ptr::eq(当前值.as_ref(), prototype.as_ref(
            return true; // 返回 true
        }
        p = cur.parent.as_ref(); // 把 当前值.parent.as_ref(); 写入 节点
    }
    false // false
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let object_proto = Proto::new("Object.prototype", None); // 把 Proto::new(「Object.prototype」, None) 存入 object_proto
    object_proto.set("a", "aaa"); // object_proto.set(「数组」, 「数组」);
    let function_proto = Proto::new("Function.prototype", Some(object_proto.clone()));
    function_proto.set("b", "bbb"); // function_proto.set(「b」, 「b」);
    let obj = Proto::new("obj", Some(object_proto.clone())); // 把 Proto::new(「obj」, Some(object_proto.clone())) 存入 obj
    let func = Proto::new("func", Some(function_proto.clone())); // 把 Proto::new(「func」, Some(function_proto.clone())) 存入 func

    assert_eq!(obj.get("a").as_deref(), Some("aaa"), "case 0 failed"); // 断言校验
    assert_eq!(obj.get("b"), None, "case 1 failed"); // 断言校验
    assert_eq!(func.get("a").as_deref(), Some("aaa"), "case 2 failed"); // 断言校验
    assert_eq!(func.get("b").as_deref(), Some("bbb"), "case 3 failed"); // 断言校验
    assert!(instance_of(&func, &object_proto), "case 4 failed"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
