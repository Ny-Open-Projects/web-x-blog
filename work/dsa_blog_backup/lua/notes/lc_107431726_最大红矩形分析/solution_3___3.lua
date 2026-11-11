-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
-- LeetCode 107431726. 最大红矩形分析 — Lua 版（方案C：逐行高度 + 单调栈）
local function max_red_rectangle(matrix) -- local function max_red_rectangle(矩阵)
	local n, m = #matrix, #matrix[1] -- 把 #矩阵, #矩阵[1] 写入 local n, m
	local ans = 0 -- 把 0 写入 local ans
	local height = {} -- 把 {} 写入 local height
	height[0] = 0 -- 哨兵
	for i = 1, m + 2 do
		height[i] = 0
	end -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
	for k = 1, n do -- 让 下标 k 从 1 走到 元素个数（Lua 1 基）
		for i = 1, m do -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
			if matrix[k]:sub(i, i) == "." then
				height[i] = height[i] + 1
			else
				height[i] = 0
			end
		end -- 终点
		local stack = { 0 } -- 把 {0} 写入 local stack
		for i = 1, m + 1 do -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
			while height[stack[#stack]] > height[i] do -- while height[栈[#栈]] 超过 height[下标 i] do
				local top = table.remove(stack) -- 把 table 弹出 栈) 写入 local top
				local now_h = height[top] -- 把 height[top] 写入 local now_h
				local width = i - stack[#stack] - 1 -- 把 下标 i 减 栈[#栈] 减 1 写入 local width
				local area = now_h * width -- 把 now_h 乘 width 写入 local area
				if area > ans then
					ans = area
				end -- 若 area 超过 答案 then 答案 赋值为 area 终点
			end -- 终点
			stack[#stack + 1] = i -- 把 下标 i 写入 stack[#stack + 1]
		end -- 终点
	end -- 终点
	return ans -- 返回 答案
end -- 终点

local matrix = { ".....", "XXXXX", ".X...", "....." } -- 把 {「.....」, 「.....」, 「.....」, 「.....」} 写入 local matrix
assert(max_red_rectangle(matrix) == 6, "mono") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
