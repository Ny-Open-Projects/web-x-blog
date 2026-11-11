-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133907522
-- LeetCode 238. 除自身以外数组的乘积 — Lua 版（方案1）
local function product_except_self(nums) -- local function product_except_self(数组)
	local n = #nums -- 把 #数组 写入 local n
	local out = {} -- 把 {} 写入 local out
	local left = 1 -- 把 1 写入 local left
	for i = 1, n do
		out[i] = left
		left = left * nums[i]
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	local right = 1 -- 把 1 写入 local right
	for i = n, 1, -1 do
		out[i] = out[i] * right
		right = right * nums[i]
	end
	return out -- 返回 out
end -- 终点
assert(table.concat(product_except_self({ 1, 2, 3, 4 }), ",") == "24,12,8,6") -- 打印输出
assert(table.concat(product_except_self({ -1, 1, 0, -3, 3 }), ",") == "0,0,9,0,0") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
