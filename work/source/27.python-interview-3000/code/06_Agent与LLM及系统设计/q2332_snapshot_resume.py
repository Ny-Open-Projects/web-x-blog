"""快照传输断点续传:切块加校验和,接收方记游标,中断后从下一个未确认块继续,末尾整体校验。"""
import hashlib


def chunk_snapshot(data, size=8):
    chunks = []
    for i in range(0, len(data), size):
        part = data[i:i + size]
        chunks.append({"idx": i // size, "sha": hashlib.sha256(part.encode("utf-8")).hexdigest()[:8],
                       "payload": part})
    return chunks


class Receiver:
    def __init__(self, total_chunks):
        self.got = {}
        self.total = total_chunks

    def accept(self, chunk):
        if chunk["idx"] in self.got:
            return "dup"
        self.got[chunk["idx"]] = chunk
        return "ok"

    def cursor(self):
        c = 0
        while c in self.got:
            c += 1
        return c

    def complete(self, full_data, manifest):
        if len(self.got) != self.total:
            return False
        for idx, ch in self.got.items():
            if hashlib.sha256(ch["payload"].encode("utf-8")).hexdigest()[:8] != ch["sha"] or ch["sha"] != manifest[idx]:
                return False
        return "".join(self.got[i]["payload"] for i in range(self.total)) == full_data


def send_all(chunks, receiver, drop_idx=None):
    log = []
    for c in chunks:
        if c["idx"] == drop_idx:
            log.append("lost:%d" % c["idx"])
            continue
        log.append(receiver.accept(c))
    return log


if __name__ == "__main__":
    data = "SNAPSHOT:" + "".join(chr(65 + i % 26) for i in range(30))
    chunks = chunk_snapshot(data, size=8)
    assert len(chunks) == 5 and sum(len(c["payload"]) for c in chunks) == len(data)
    manifest = [c["sha"] for c in chunks]
    recv = Receiver(len(chunks))
    log = send_all(chunks, recv, drop_idx=2)
    assert "lost:2" in log and recv.cursor() == 2, "连续前缀到缺口为止"
    assert recv.accept(chunks[2]) == "ok"
    assert recv.complete(data, manifest), "补齐后逐块校验并整体对账"
    recv2 = Receiver(len(chunks))
    send_all(chunks, recv2, drop_idx=1)
    assert recv2.accept(chunks[1]) == "ok", "缺口补上"
    assert recv2.accept(chunks[3]) == "dup", "重复块去重"
    assert recv2.complete(data, manifest), "乱序补齐也能完成"
    bad = Receiver(len(chunks))
    bad.got[0] = {"idx": 0, "sha": manifest[0], "payload": "TAMPERED"}
    for c in chunks[1:]:
        bad.accept(c)
    assert not bad.complete(data, manifest), "块内容被改 校验拦截"
    print("快照续传通过:分块校验 游标续传 去重 整体对账防篡改")
