-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134026430
-- LeetCode 54. 螺旋矩阵 — Lua 版

-- 方案1：四边界逐层收缩（1 基下标，与 TS 事实源逻辑一致）
local function spiral_order(matrix) -- local function spiral_order(矩阵)
	if not matrix or #matrix == 0 or #matrix[1] == 0 then
		return {}
	end -- 若 not 矩阵 or #矩阵 等于 0 or #矩阵[1] 等于 0 then return {} 终点
	local result = {} -- 把 {} 写入 local result
	local top, bottom, left, right = 1, #matrix, 1, #matrix[1] -- 把 1, #矩阵, 1, #矩阵[1] 写入 local top, bottom, left, right
	while top <= bottom and left <= right do -- 把 bottom and 左边界 不超过 右边界 do 写入 while top <
		for i = left, right do
			result[#result + 1] = matrix[top][i]
		end -- 把 左边界, 右边界 do 结果[#结果 加 1] 赋值为 矩阵[top][下标 i] 终点 写入 for i
		top = top + 1 -- 把 top 加 1 存入 top
		for i = top, bottom do
			result[#result + 1] = matrix[i][right]
		end -- 把 top, bottom do 结果[#结果 加 1] 赋值为 矩阵[下标 i][右边界] 终点 写入 for i
		right = right - 1 -- 把 右边界 减 1 存入 右边界
		if top <= bottom then -- 若 top 不超过 bottom then
			for i = right, left, -1 do
				result[#result + 1] = matrix[bottom][i]
			end
			bottom = bottom - 1 -- 把 bottom 减 1 存入 bottom
		end -- 终点
		if left <= right then -- 若 左边界 不超过 右边界 then
			for i = bottom, top, -1 do
				result[#result + 1] = matrix[i][left]
			end
			left = left + 1 -- 把 左边界 加 1 存入 左边界
		end -- 终点
	end -- 终点
	return result -- 返回 结果
end -- 终点

-- 自测：与 TS 事实源内嵌用例一致（空矩阵）
local got = spiral_order({}) -- 把 spiral_order({}) 写入 local got
assert(#got == 0, "FAILED empty") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
