-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145634738
-- LeetCode 1797. 设计一个验证系统 — Lua 版（方案1）
local AuthenticationManager = {} -- 把 {} 写入 local AuthenticationManager
AuthenticationManager.__index = AuthenticationManager -- 把 AuthenticationManager 写入 AuthenticationManager.__index
function AuthenticationManager.new(ttl) -- function AuthenticationManager.new(ttl)
	return setmetatable({ ttl = ttl, expires_at = {} }, AuthenticationManager)
end -- 终点
function AuthenticationManager:generate(token_id, current_time)
	self.expires_at[token_id] = current_time + self.ttl -- 把 current_time 加 self.ttl 写入 self.expires_at[token_id]
end -- 终点
function AuthenticationManager:renew(token_id, current_time) -- function AuthenticationManager:renew(token_id, current_time)
	local exp = self.expires_at[token_id] -- 把 self.expires_at[token_id] 写入 local exp
	if exp and exp > current_time then -- 若 exp and exp 超过 current_time then
		self.expires_at[token_id] = current_time + self.ttl -- 把 current_time 加 self.ttl 写入 self.expires_at[token_id]
	end -- 终点
	return self:count_valid_tokens(current_time) -- 返回 self:count_valid_tokens(current_time)
end -- 终点
function AuthenticationManager:count_valid_tokens(current_time)
	local cnt = 0 -- 把 0 写入 local cnt
	for _, e in pairs(self.expires_at) do -- 遍历取 e
		if e > current_time then
			cnt = cnt + 1
		end -- 若 e 超过 current_time then 计数 赋值为 计数 加 1 终点
	end -- 终点
	return cnt -- 返回 计数
end -- 终点
local auth = AuthenticationManager.new(5) -- 把 AuthenticationManager.new(5) 写入 local auth
auth:generate("aaa", 1) -- auth:generate(「aaa」, 1)
assert(auth:count_valid_tokens(3) == 1) -- 断言校验
assert(auth:renew("aaa", 4) == 1) -- 断言校验
assert(auth:count_valid_tokens(6) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
