"""多模态消息构造:图片压缩限制、base64 与 URL 两种引用方式(全 stub)。"""
import base64


def make_image_part(source: str, max_pixels: int = 1024 * 1024) -> dict:
    """source 为路径,演示压缩决策与两种引用方式。"""
    pixels = len(source) * 10000  # 假装这是图片像素数
    if pixels > max_pixels:
        print(f"  [预处理] 图片过大({pixels}px),压缩到 {max_pixels}px")
        pixels = max_pixels
    if source.startswith("http"):
        return {"type": "image_url", "url": source}
    fake_bytes = base64.b64encode(source.encode()).decode()
    return {"type": "image_base64", "data": fake_bytes[:16] + "...", "pixels": pixels}


def build_multimodal_message(text: str, images: list[str]) -> dict:
    content = [{"type": "text", "text": text}]
    content += [make_image_part(src) for src in images]
    return {"role": "user", "content": content}


class FakeVisionLLM:
    def chat(self, messages):
        types = [c["type"] for c in messages["content"]]
        return f"已接收 {types},识别结果:图片中是一张报销单"


if __name__ == "__main__":
    msg = build_multimodal_message("这张报销单的总金额是多少?",
                                   ["https://cdn.example.com/receipt.jpg",
                                    "/local/very_large_photo.png"])
    print(FakeVisionLLM().chat(msg))
