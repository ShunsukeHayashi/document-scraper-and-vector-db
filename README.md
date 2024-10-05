# Document Extraction and Vector Database Construction

This project scrapes web pages from a specified root URL, extracts relevant document information, consolidates it into a text file, vectorizes the text data, and constructs a vector database.

## Project Objectives

- Automatically extract documents from web pages and save them to a text file.
- Vectorize text data and build a vector database for efficient search and similarity calculations.

## Directory Structure

```
doc_scraping/
│
├── .env                   # Environment variables file
├── documents.txt          # Text file storing scraped documents
├── vector_database.py     # Script for building and managing the vector database
├── run_all.py             # Script to execute the entire process
├── document_scraper.py    # Script for scraping documents from web pages
├── url_tree.txt           # Text file storing the tree structure of scraped URLs
├── Dockerfile             # Docker environment setup file
├── docker-compose.yml     # Docker Compose configuration file
├── requirements.txt       # Project dependencies
└── readme.md              # Project description and usage instructions
```

## File Dependencies

- `document_scraper.py`:
  - Scrapes documents from the specified root URL and saves them to `documents.txt`.
  - Saves the tree structure of scraped URLs to `url_tree.txt`.

- `vector_database.py`:
  - Reads text data from `documents.txt` and chunks the documents.
  - Vectorizes the chunked data and builds a vector database.
  - Saves the vector database as `vector_database.index`.

- `run_all.py`:
  - Sequentially executes `document_scraper.py` and `vector_database.py` to manage the entire process.

## Usage

1. **Document Scraping:**
   - Run `document_scraper.py` to extract documents from the specified root URL.
   - Extracted documents are saved to `doc_scraping/documents.txt`.

2. **Vector Database Construction:**
   - Run `vector_database.py` to read text data from `documents.txt` and vectorize it.
   - The vector database is built using the vectorized data.
   - The vector database is saved as `vector_database.index`.

3. **Vector Database Saving and Loading:**
   - Use the `save_vector_database` function to save the vector database to a file.
   - Use the `load_vector_database` function to load a saved vector database.

## Required Libraries

- `openai`
- `pandas`
- `numpy`
- `faiss`
- `requests`
- `beautifulsoup4`
- `python-dotenv`

## Important Notes

- You need to set your OpenAI API key.  Set the API key in the `.env` file.
- Ensure that the `openai` library version is 1.0.0 or higher.  If necessary, update the library by running `pip install openai --upgrade`.

## License

This project is licensed under the MIT License.


## Docker (Optional)

This project includes a `Dockerfile` and `docker-compose.yml` for easy setup and execution within a Docker container.  This is the recommended way to run the project to avoid dependency conflicts.

To build and run the Docker container:

```bash
docker-compose build
docker-compose up
```

Make sure your `.env` file with the `OPENAI_API_KEY` is in the same directory as the `docker-compose.yml` file.


This improved README provides more detailed information about the project, including how to use Docker, and clarifies the usage of the vector database saving and loading functions. It also includes a more standard formatting for the required libraries section.
