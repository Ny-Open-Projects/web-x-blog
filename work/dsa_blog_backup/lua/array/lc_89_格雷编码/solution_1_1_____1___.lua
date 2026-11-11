-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134866839
-- LeetCode 89. 格雷编码 — Lua 版（方案1）
local function gray_code(n) -- local function gray_code(元素个数)
	local m = 1 << n -- 把 1 小于 小于 元素个数 写入 local m
	local out = {} -- 把 {} 写入 local out
	for i = 0, m - 1 do
		out[#out + 1] = i ~ (i >> 1)
	end -- 让 下标 i 从 0 走到 映射表（Lua 1 基）
	return out -- 返回 out
end -- 终点
assert(table.concat(gray_code(2), ",") == "0,1,3,2") -- 打印输出
assert(table.concat(gray_code(1), ",") == "0,1") -- 打印输出
local g3 = gray_code(3) -- 把 gray_code(3) 写入 local g3
assert(#g3 == 8) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
