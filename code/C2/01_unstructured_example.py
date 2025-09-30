from unstructured.partition.pdf import partition_pdf

# PDF文件路径
pdf_path = "../../data/C2/pdf/rag.pdf"

# 使用partition_pdf的hi_res模式解析PDF文档
print("=== 使用 hi_res 模式解析 ===")
elements_hi_res = partition_pdf(
    filename=pdf_path,
    strategy="hi_res"
)
print(f"hi_res模式: 解析完成: {len(elements_hi_res)} 个元素, {sum(len(str(e)) for e in elements_hi_res)} 字符")
from collections import Counter
types_hi_res = Counter(e.category for e in elements_hi_res)
print(f"hi_res模式: 元素类型: {dict(types_hi_res)}")

# 使用partition_pdf的ocr_only模式解析PDF文档
print("\n=== 使用 ocr_only 模式解析 ===")
elements_ocr_only = partition_pdf(
    filename=pdf_path,
    strategy="ocr_only"
)
print(f"ocr_only模式: 解析完成: {len(elements_ocr_only)} 个元素, {sum(len(str(e)) for e in elements_ocr_only)} 字符")
types_ocr_only = Counter(e.category for e in elements_ocr_only)
print(f"ocr_only模式: 元素类型: {dict(types_ocr_only)}")

# 可选：显示部分元素内容对比
print("\n=== hi_res模式部分元素 ===")
for i, element in enumerate(elements_hi_res[:3], 1):
    print(f"Element {i} ({element.category}):")
    print(element)
    print("=" * 60)

print("\n=== ocr_only模式部分元素 ===")
for i, element in enumerate(elements_ocr_only[:3], 1):
    print(f"Element {i} ({element.category}):")
    print(element)
    print("=" * 60)