-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134032039
-- LeetCode 48. 旋转矩阵 — Lua 版

-- 方案2：先上下翻转行（交换行引用），再沿主对角线转置
local function rotate(matrix) -- local function rotate(矩阵)
	local n = #matrix -- 把 #矩阵 写入 local n
	for i = 1, math.floor(n / 2) do -- 让 下标 i 从 1 走到 math（Lua 1 基）
		matrix[i], matrix[n + 1 - i] = matrix[n + 1 - i], matrix[i]
	end -- 终点
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		for j = 1, i - 1 do -- 让 下标 j 从 1 走到 下标 i（Lua 1 基）
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		end -- 终点
	end -- 终点
end -- 终点

local function eq_matrix(a, b) -- local function eq_matrix(数组, b)
	if #a ~= #b then
		return false
	end -- 若 #数组 ~ 赋值为 #b then return false 终点
	for i = 1, #a do -- 把 1, #数组 do 写入 for i
		if #a[i] ~= #b[i] then
			return false
		end -- 若 #数组[下标 i] ~ 赋值为 #b[下标 i] then return false 终点
		for j = 1, #a[i] do -- 把 1, #数组[下标 i] do 写入 for j
			if a[i][j] ~= b[i][j] then
				return false
			end -- 若 数组[下标 i][下标 j] ~ 赋值为 b[下标 i][下标 j] then return false 终点
		end -- 终点
	end -- 终点
	return true -- 返回 true
end -- 终点

-- 自测：与 TS 事实源内嵌用例一致（LeetCode 官方示例）
local cases = { -- 把 { 写入 local cases
	{ { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } }, { { 7, 4, 1 }, { 8, 5, 2 }, { 9, 6, 3 } } },
	{
		{ { 5, 1, 9, 11 }, { 2, 4, 8, 10 }, { 13, 3, 6, 7 }, { 15, 14, 12, 16 } },
		{
			{ 15, 13, 2, 5 },
			{ 14, 3, 4, 1 },
			{ 12, 6, 8, 9 },
			{ 16, 7, 10, 11 },
		},
	},
}
for idx, t in ipairs(cases) do -- 遍历取 另一字符串
	rotate(t[1]) -- rotate(另一字符串[1])
	assert(eq_matrix(t[1], t[2]), string.format("case %d failed", idx)) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
