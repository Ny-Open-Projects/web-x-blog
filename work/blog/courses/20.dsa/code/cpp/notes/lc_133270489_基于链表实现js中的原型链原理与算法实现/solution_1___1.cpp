// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — C++ 版（方案1：instanceOf 沿原型链判定）
#include <iostream>      // 引入头文件
#include <string>        // 引入头文件
#include <unordered_map> // 引入头文件

struct Proto {        // 定义类型
    std::string name; // std::string name;
    std::unordered_map<std::string, std::string>
        props;     // std::unordered_map 小于 std::string, std::string 超过 props;
    Proto *parent; // Proto 乘 parent;
    Proto(const std::string &n, Proto *p = nullptr) : name(n), parent(p) {}
};

static bool instance_of(const Proto *obj, const Proto *prototype) { // 定义函数/方法 instance_of
    const Proto *p = obj;                                           // 把 obj; 写入 const Proto *p
    while (p != nullptr) { // 循环，直到不满足「节点 不等于 nullptr」
        if (p == prototype)
            return true; // 若 节点 等于 prototype，直接返回 true
        p = p->parent;   // 把 节点 减 超过 parent; 写入 节点
    }
    return false; // 返回 false
}

int main() {                                // 程序入口：跑内嵌自测用例
    Proto object_proto("Object.prototype"); // Proto object_proto(「Object.prototype」);
    Proto function_proto("Function.prototype", &object_proto);
    Proto array_proto("Array.prototype",
                      &object_proto);    // Proto array_proto(「Array.prototype」, 按位与 object_proto);
    Proto obj("obj", &object_proto);     // Proto obj(「obj」, 按位与 object_proto);
    Proto func("func", &function_proto); // Proto func(「func」, 按位与 function_proto);
    Proto arr("arr", &array_proto);      // Proto 数组(「数组」, 按位与 array_proto);

    bool g0 = instance_of(&obj, &object_proto); // 把 instance_of( 按位与 obj, 按位与 object_proto) 存入 g0
    bool g1 =
        instance_of(&func, &function_proto); // 把 instance_of( 按位与 func, 按位与 function_proto) 存入 g1
    bool g2 = instance_of(&func, &object_proto); // 把 instance_of( 按位与 func, 按位与 object_proto) 存入 g2
    bool g3 = instance_of(&arr, &array_proto); // 把 instance_of( 按位与 数组, 按位与 array_proto) 存入 g3
    bool g4 = instance_of(&arr, &object_proto); // 把 instance_of( 按位与 数组, 按位与 object_proto) 存入 g4
    if (!g0 || !g1 || !g2 || !g3 || !g4) {
        std::cout << "FAIL" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
