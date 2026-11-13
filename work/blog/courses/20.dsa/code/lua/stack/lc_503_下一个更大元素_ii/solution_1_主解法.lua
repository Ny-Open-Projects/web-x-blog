-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145045460
-- LeetCode 503. 下一个更大元素 II — Lua 版（方案1）
local function next_greater_elements(nums) -- local function next_greater_elements(数组)
	local n = #nums -- 把 #数组 写入 local n
	local res = {} -- 把 {} 写入 local res
	for i = 1, n do
		res[i] = -1
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	local st = {} -- 把 {} 写入 local st
	for i = 1, 2 * n do -- 让 下标 i 从 1 走到 2（Lua 1 基）
		local ii = (i - 1) % n + 1 -- 把 (下标 i 减 1) 对…取模 元素个数 加 1 写入 local ii
		while #st > 0 and nums[st[#st]] < nums[ii] do -- while #st 超过 0 and 数组[st[#st]] 小于 数组[ii] do
			res[st[#st]] = nums[ii] -- 把 数组[ii] 写入 res[st[#st]]
			st[#st] = nil -- 把 nil 写入 st[#st]
		end -- 终点
		if i <= n then
			st[#st + 1] = ii
		end -- 若 下标 i 不超过 元素个数 then st[#st 加 1] 赋值为 ii 终点
	end -- 终点
	return res -- 返回 结果
end -- 终点
assert(table.concat(next_greater_elements({ 1, 2, 1 }), ",") == "2,-1,2") -- 打印输出
assert(table.concat(next_greater_elements({ 3, 2, 1 }), ",") == "-1,3,3") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
