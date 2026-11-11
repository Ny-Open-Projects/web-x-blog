/* 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
 * LeetCode 133270489. 原型链原理 — C 版（方案4：null/undefined 边界：instanceOf 均返回 false）
 */
#include <stdio.h> // 引入头文件

typedef struct Obj { // typedef struct Obj {
    void *__proto__; // void 乘 __proto__;
} Obj;               // } Obj;

typedef struct Ctor { // typedef struct Ctor {
    void *prototype;  // void 乘 prototype;
} Ctor;               // } Ctor;

static int instance_of(const void *a, const Ctor *b) { // 定义函数/方法 instance_of
    const void *p = a;                                 // 把 数组; 写入 const void *p
    while (p != NULL) {                                // 循环，直到不满足「节点 不等于 NULL」
        if (p == b->prototype)
            return 1;                    // 若 节点 等于 b 减 超过 prototype，直接返回 1
        p = ((const Obj *)p)->__proto__; // 把 ((const Obj 乘 )节点) 减 超过 __proto__; 写入 节点
    }
    return 0; // 返回 0
}

int main(void) {        // 程序入口：跑内嵌自测用例
    Ctor ctor = {NULL}; // 把 { NULL }; 写入 Ctor ctor
    if (instance_of(NULL, &ctor)) {
        printf("null case failed\n");
        return 1;
    }
    if (instance_of(NULL, &ctor)) {
        printf("undefined case failed\n");
        return 1;
    }
    printf("PASS\n"); // 全部用例通过，输出 PASS
    return 0;         // 返回 0
}
