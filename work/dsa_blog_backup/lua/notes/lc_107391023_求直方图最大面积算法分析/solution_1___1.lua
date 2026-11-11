-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
-- 求直方图最大面积算法分析 — Lua 版（方案1）
local function get_result(n, heights) -- local function get_result(元素个数, heights)
	local st = {} -- 把 {} 写入 local st
	local best = 0 -- 把 0 写入 local best
	local function at(i)
		return i <= #heights and heights[i] or 0
	end
	for i = 1, #heights + 1 do -- 把 1, #heights 加 1 do 写入 for i
		local cur = at(i) -- 把 at(下标 i) 写入 local cur
		while #st > 0 and heights[st[#st]] >= cur do -- 把 当前值 do 写入 while #st > 0 and heights[st[#st]] >
			local top = table.remove(st) -- 把 table 弹出 st) 写入 local top
			local left = st[#st] or 0 -- 把 st[#st] or 0 写入 local left
			local width = i - left - 1 -- 把 下标 i 减 左边界 减 1 写入 local width
			local area = heights[top] * width -- 把 heights[top] 乘 width 写入 local area
			if area > best then
				best = area
			end -- 若 area 超过 当前最优 then 当前最优 赋值为 area 终点
		end -- 终点
		st[#st + 1] = i -- 把 下标 i 写入 st[#st + 1]
	end -- 终点
	return best -- 返回 当前最优
end -- 终点
assert(get_result(5, { 0, 2, 3, 3, 3, 2, 0 }) == 10) -- 断言校验
assert(get_result(6, { 0, 2, 1, 5, 6, 2, 3, 0 }) == 10) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
