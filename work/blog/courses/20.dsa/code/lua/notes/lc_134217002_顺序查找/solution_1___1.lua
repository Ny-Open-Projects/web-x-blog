-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002
-- 数据结构与算法之查找: 顺序查找 — Lua 版（方案1）
local function seq_search(arr, key) -- local function seq_search(数组, key)
	for i, v in ipairs(arr) do -- 遍历取 值
		if v == key then
			return i - 1
		end -- 若 值 等于 key then return 下标 i 减 1 终点
	end -- 终点
	return -1 -- 返回 减 1
end -- 终点
assert(seq_search({ 1, 2, 3 }, 1) == 0) -- 断言校验
assert(seq_search({ 1, 2, 3 }, 2) == 1) -- 断言校验
assert(seq_search({ 1, 2, 3 }, 3) == 2) -- 断言校验
assert(seq_search({ 1, 2, 3 }, 4) == -1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
