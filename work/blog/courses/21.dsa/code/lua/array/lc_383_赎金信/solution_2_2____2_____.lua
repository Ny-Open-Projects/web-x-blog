-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134312127
-- LeetCode 383. 赎金信 — Lua 版（方案2）
local function can_construct(ransom, magazine) -- local function can_construct(ransom, magazine)
	local cnt = {} -- 把 {} 写入 local cnt
	for c in magazine:gmatch("[%a]") do
		cnt[c] = (cnt[c] or 0) + 1
	end
	for c in ransom:gmatch("[%a]") do -- for 字符 in ransom:gmatch(「[ 对…取模 数组]」) do
		cnt[c] = (cnt[c] or 0) - 1 -- 把 (计数[字符] or 0) 减 1 写入 cnt[c]
		if cnt[c] < 0 then
			return false
		end -- 若 计数[字符] 小于 0 then return false 终点
	end -- 终点
	return true -- 返回 true
end -- 终点
assert(can_construct("a", "b") == false) -- 断言校验
assert(can_construct("aa", "ab") == false) -- 断言校验
assert(can_construct("aa", "aab") == true) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
