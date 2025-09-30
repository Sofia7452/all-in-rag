from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# 1. 配置全局嵌入模型（需与保存时一致）
Settings.embed_model = HuggingFaceEmbedding("BAAI/bge-small-zh-v1.5")
Settings.llm = None  # 显式禁用 LLM，防止自动加载 OpenAI

# 2. 加载本地持久化的索引
persist_path = "./llamaindex_index_store"
storage_context = StorageContext.from_defaults(persist_dir=persist_path)
index = load_index_from_storage(storage_context)

print(f"LlamaIndex 索引已从 {persist_path} 加载")

# 3. 执行相似性搜索
query = "LlamaIndex是做什么的？"
query_engine = index.as_query_engine(similarity_top_k=1)
response = query_engine.query(query)

print(f"\n查询: '{query}'")
print("相似度最高的文档:")
print(f"- {response}")