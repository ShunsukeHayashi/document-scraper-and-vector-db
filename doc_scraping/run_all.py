import os
import subprocess

def run_document_scraper():
    print("Running document scraper...")
    try:
        subprocess.run(["python", "document_scraper.py"], check=True, cwd=os.path.dirname(__file__))
        print("Document scraping completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running document scraper: {e}")

def run_vector_database():
    print("Running vector database builder...")
    try:
        subprocess.run(["python", "vector_database.py"], check=True, cwd=os.path.dirname(__file__))
        print("Vector database built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running vector database builder: {e}")

if __name__ == "__main__":
    run_document_scraper()
    run_vector_database()