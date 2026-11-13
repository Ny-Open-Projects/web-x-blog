-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
-- LeetCode 621. 任务调度器 — Lua 版

-- 方案4（26 位频率桶公式法）
local function least_interval(tasks, n) -- local function least_interval(tasks, 元素个数)
	local freq = {} -- 把 {} 写入 local freq
	for i = 1, 26 do
		freq[i] = 0
	end -- 让 下标 i 从 1 走到 26（Lua 1 基）
	local A = string.byte("A") -- 把 string.byte(「A」) 写入 local A
	for _, t in ipairs(tasks) do -- 遍历取 另一字符串
		local idx = string.byte(t) - A + 1 -- 把 string.byte(另一字符串) 减 A 加 1 写入 local idx
		freq[idx] = freq[idx] + 1 -- 把 频次表[idx] 加 1 写入 freq[idx]
	end -- 终点
	local max_freq = 0 -- 把 0 写入 local max_freq
	for _, f in ipairs(freq) do -- 遍历取 f
		if f > max_freq then
			max_freq = f
		end -- 若 f 超过 max_freq then max_freq 赋值为 f 终点
	end -- 终点
	local same = 0 -- 把 0 写入 local same
	for _, f in ipairs(freq) do -- 遍历取 f
		if f == max_freq then
			same = same + 1
		end -- 若 f 等于 max_freq then same 赋值为 same 加 1 终点
	end -- 终点
	return math.max((max_freq - 1) * (n + 1) + same, #tasks) -- 返回 math.取较大值 (max_freq 减 1) 乘 (元素个数 加 1) 加 same, #tasks)
end -- 终点

-- 自测：与 TS 事实源内嵌用例一致
local cases = { -- 把 { 写入 local cases
	{ { "A", "A", "A", "B", "B", "B" }, 2, 8 },
	{ { "A", "A", "A", "A" }, 2, 10 },
	{ { "A", "B", "C", "D" }, 0, 4 },
}
for i, c in ipairs(cases) do -- 遍历取 字符
	local got = least_interval(c[1], c[2]) -- 把 least_interval(字符[1], 字符[2]) 写入 local got
	assert(got == c[3], string.format("FAIL case %d got %d want %d", i, got, c[3])) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
