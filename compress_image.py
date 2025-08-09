# compress_image.py

import os
import sys
from PIL import Image

# --- 可配置参数 ---
# 输出文件夹名称
OUTPUT_FOLDER = "_compressed"
# 图片最长边的最大尺寸（像素）
MAX_SIZE = 1920
# JPEG 图片的输出质量（1-100，建议 80-90）
JPG_QUALITY = 85
# --------------------

def compress_image(input_path):
    """处理单张图片"""
    try:
        # 确保输出目录存在
        output_dir = os.path.join(os.path.dirname(input_path), OUTPUT_FOLDER)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 打开图片
        img = Image.open(input_path)
        original_size = os.path.getsize(input_path) / 1024  # KB
        filename = os.path.basename(input_path)

        # 1. 调整尺寸
        if img.width > MAX_SIZE or img.height > MAX_SIZE:
            img.thumbnail((MAX_SIZE, MAX_SIZE), Image.LANCZOS)

        # 构建输出路径
        output_filename = os.path.splitext(filename)[0]
        output_path = os.path.join(output_dir, output_filename)

        # 2. 保存并压缩
        if img.format == 'JPEG' or img.mode == 'RGB':
            output_path += '.jpg'
            img.save(output_path, 'jpeg', quality=JPG_QUALITY, optimize=True)
        else:
            # 对于 PNG 和其他格式，保留透明度
            output_path += '.png'
            img.save(output_path, 'png', optimize=True)

        compressed_size = os.path.getsize(output_path) / 1024  # KB
        reduction_percent = (original_size - compressed_size) / original_size * 100

        print(f"处理成功: {filename} ({original_size:.1f} KB)")
        print(f"  -> 保存至: {os.path.basename(output_path)} ({compressed_size:.1f} KB)")
        print(f"  -> 体积减小: {reduction_percent:.1f}%")

    except FileNotFoundError:
        print(f"错误: 文件未找到 - {input_path}")
    except Exception as e:
        print(f"处理失败: {os.path.basename(input_path)} - {e}")

if __name__ == "__main__":
    # 从命令行接收文件路径参数
    if len(sys.argv) > 1:
        for image_path in sys.argv[1:]:
            compress_image(image_path)
            print("-" * 20)
    else:
        print("请拖动一个或多个图片文件到批处理脚本上。")