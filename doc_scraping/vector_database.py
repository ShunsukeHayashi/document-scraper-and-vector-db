import openai
import pandas as pd
import numpy as np
import faiss
from dotenv import load_dotenv
import os

# 環境変数をロード
load_dotenv()

# OpenAI APIキーの設定
openai.api_key = os.getenv('OPENAI_API_KEY')

# テキストデータの読み込み
def load_documents(filename='doc_scraping/documents.txt'):
    print(f"Loading documents from {filename}")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            documents = file.readlines()
        print(f"Loaded {len(documents)} documents.")
    except Exception as e:
        print(f"Error loading documents: {e}")
        return []
    return documents

# ドキュメントのチャンキング
def chunk_documents(documents, max_length=8191):
    chunks = []
    for doc in documents:
        tokens = doc.split()
        for i in range(0, len(tokens), max_length):
            chunk = ' '.join(tokens[i:i + max_length])
            chunks.append(chunk)
    return chunks

# テキストデータのベクトル化
def vectorize_documents(chunks):
    print("Vectorizing document chunks...")
    vectors = []
    for i, chunk in enumerate(chunks):
        print(f"Vectorizing chunk {i+1}/{len(chunks)}")
        # 新しいAPIを使用してベクトルを取得
        response = openai.Embedding.create(input=chunk, model="text-embedding-ada-002")
        vector = response['data'][0]['embedding']
        vectors.append(vector)
    print("Vectorization complete.")
    return np.array(vectors)

# ベクトルデータベースの構築
def build_vector_database(vectors):
    print("Building vector database...")
    try:
        dimension = vectors.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(vectors)
        print("Vector database built successfully.")
    except Exception as e:
        print(f"Error building vector database: {e}")
        return None
    return index

# ベクトルデータベースの内容を表示
def display_vector_database(vectors):
    print("Displaying vector database...")
    df = pd.DataFrame(vectors)
    print(df)

# ベクトルデータベースの保存
def save_vector_database(index, filename='vector_database.index'):
    print(f"Saving vector database to {filename}...")
    faiss.write_index(index, filename)
    print("Vector database saved successfully.")

# ベクトルデータベースの読み込み
def load_vector_database(filename='vector_database.index'):
    print(f"Loading vector database from {filename}...")
    try:
        index = faiss.read_index(filename)
        print("Vector database loaded successfully.")
        return index
    except Exception as e:
        print(f"Error loading vector database: {e}")
        return None

# 使用例
if __name__ == "__main__":
    documents = load_documents()
    if documents:
        chunks = chunk_documents(documents)
        vectors = vectorize_documents(chunks)
        if vectors.size > 0:
            vector_database = build_vector_database(vectors)
            if vector_database is not None:
                print("ベクトルデータベースが構築されました。")
                display_vector_database(vectors)
                save_vector_database(vector_database)  # ベクトルデータベースを保存