-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
-- LeetCode 133278676. 使用链表（指针链）获取 JSON 节点值 — Lua 版（方案B：逐键求值 / reduce 链式访问）
local function get_value_eval(data, path) -- local function get_value_eval(data, 当前路径)
	local cur = data -- 把 data 写入 local cur
	for _, k in ipairs(path) do -- 遍历取 下标 k
		cur = cur[k] -- 把 当前值[下标 k] 存入 当前值
	end -- 终点
	return cur -- 返回 当前值
end -- 终点

local function get_value_chain(data, path) -- local function get_value_chain(data, 当前路径)
	local acc = data -- 把 data 写入 local acc
	for _, k in ipairs(path) do -- 遍历取 下标 k
		acc = acc[k] -- 把 累加器[下标 k] 存入 累加器
	end -- 终点
	return acc -- 返回 累加器
end -- 终点

local data = { a = { b = { c = 1 } }, d = { e = 2 } }
assert(get_value_eval(data, { "a", "b", "c" }) == 1, "p1") -- 断言校验
assert(get_value_chain(data, { "d", "e" }) == 2, "p2") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
