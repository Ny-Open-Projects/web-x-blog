// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — C++ 版（方案4：null/undefined 边界：instanceOf 均返回 false）
#include <iostream> // 引入头文件

struct Obj {                   // 定义类型
    void *__proto__ = nullptr; // 把 nullptr; 写入 void *__proto__
};

struct Ctor {                  // 定义类型
    void *prototype = nullptr; // 把 nullptr; 写入 void *prototype
};

static bool instance_of(const void *a, const Ctor &b) { // 定义函数/方法 instance_of
    const void *p = a;                                  // 把 数组; 写入 const void *p
    while (p != nullptr) { // 循环，直到不满足「节点 不等于 nullptr」
        if (p == b.prototype)
            return true; // 若 节点 等于 b.prototype，直接返回 true
        p = static_cast<const Obj *>(p)
                ->__proto__; // 把 static_cast 小于 const Obj 乘 超过 (节点) 减 超过 __proto__; 写入 节点
    }
    return false; // 返回 false
}

int main() {   // 程序入口：跑内嵌自测用例
    Ctor ctor; // Ctor ctor;
    if (instance_of(nullptr, ctor)) {
        std::cout << "null case failed" << std::endl;
        return 1;
    }
    if (instance_of(nullptr, ctor)) {
        std::cout << "undefined case failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl; // 全部用例通过，输出 PASS
    return 0;                         // 返回 0
}
