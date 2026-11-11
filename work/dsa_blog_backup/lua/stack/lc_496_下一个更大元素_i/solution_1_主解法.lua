-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145012016
-- LeetCode 496. 下一个更大元素 I — Lua 版（方案1）
local function next_greater_element(nums1, nums2) -- local function next_greater_element(数组1, 数组2)
	local next_ = {} -- 把 {} 写入 local next_
	local st = {} -- 把 {} 写入 local st
	for _, v in ipairs(nums2) do -- 遍历取 值
		while #st > 0 and st[#st] < v do -- while #st 超过 0 and st[#st] 小于 值 do
			next_[st[#st]] = v -- 把 值 写入 next_[st[#st]]
			st[#st] = nil -- 把 nil 写入 st[#st]
		end -- 终点
		st[#st + 1] = v -- 把 值 写入 st[#st + 1]
	end -- 终点
	local out = {} -- 把 {} 写入 local out
	for i, v in ipairs(nums1) do -- 遍历取 值
		out[i] = next_[v] or -1 -- 把 next_[值] or 减 1 写入 out[i]
	end -- 终点
	return out -- 返回 out
end -- 终点
assert(table.concat(next_greater_element({ 4, 1, 2 }, { 1, 3, 4, 2 }), ",") == "-1,3,-1") -- 打印输出
assert(table.concat(next_greater_element({ 2, 4 }, { 1, 2, 3, 4 }), ",") == "3,-1") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
