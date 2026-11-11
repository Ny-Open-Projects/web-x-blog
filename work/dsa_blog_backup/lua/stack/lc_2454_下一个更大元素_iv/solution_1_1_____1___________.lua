-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397916
-- LeetCode 2454. 下一个更大元素 IV — Lua 版（方案1）
local function second_greater(nums) -- local function second_greater(数组)
	local n = #nums -- 把 #数组 写入 local n
	local res = {} -- 把 {} 写入 local res
	for i = 1, n do
		res[i] = -1
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	local s1, s2 = {}, {} -- 把 {}, {} 写入 local s1, s2
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		while #s2 > 0 and nums[s2[#s2]] < nums[i] do -- while #s2 超过 0 and 数组[s2[#s2]] 小于 数组[下标 i] do
			res[s2[#s2]] = nums[i] -- 把 数组[下标 i] 写入 res[s2[#s2]]
			s2[#s2] = nil -- 把 nil 写入 s2[#s2]
		end -- 终点
		while #s1 > 0 and nums[s1[#s1]] < nums[i] do -- while #s1 超过 0 and 数组[s1[#s1]] 小于 数组[下标 i] do
			s2[#s2 + 1] = s1[#s1] -- 把 s1[#s1] 写入 s2[#s2 + 1]
			s1[#s1] = nil -- 把 nil 写入 s1[#s1]
		end -- 终点
		s1[#s1 + 1] = i -- 把 下标 i 写入 s1[#s1 + 1]
	end -- 终点
	return res -- 返回 结果
end -- 终点
assert(table.concat(second_greater({ 2, 4, 0, 9, 6 }), ",") == "9,6,6,-1,-1") -- 打印输出
assert(table.concat(second_greater({ 5, 4, 3, 2, 1 }), ",") == "-1,-1,-1,-1,-1") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
