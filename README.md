# Chat-with-Multi-PDF-App-using-Gemini-and-FAISS 📄🤖

This project provides an interactive Streamlit interface that allows users to upload multiple PDF documents and ask questions about their content. It uses Google's Gemini model for generating responses and stores PDF embeddings in a FAISS vector database for efficient retrieval.

## Prerequisites
- Python 3.7 or later
- `streamlit` package
- `PyPDF2` package
- `langchain`, `langchain-google-genai`, and `langchain-community`
- `python-dotenv` package
- Google AI account and API key for Gemini
- FAISS (via `langchain_community.vectorstores`)

## Installation
1. Clone this repository.
2. Create a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # For Windows: env\Scripts\activate.bat
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Create a `.env` file in the project root and add your Google AI API key:

    ```
    GOOGLE_API_KEY=your_actual_key_here
    ```

2. Run the Streamlit app:

    ```bash
    streamlit run your_app_file_name.py
    ```

3. In the sidebar:
   - Upload one or more PDF files.
   - Click "Submit & Process" to convert and vectorize the contents.
   - Use the main interface to ask questions based on the uploaded content.

## Explanation
- The app works as follows:
  - PDF files are uploaded and read using `PyPDF2`.
  - The full text is split into manageable chunks with `RecursiveCharacterTextSplitter`.
  - These chunks are embedded using `GoogleGenerativeAIEmbeddings` and stored locally using FAISS.
  - When a question is entered, the app performs a similarity search in the FAISS vector store to retrieve the most relevant chunks.
  - A Gemini-powered QA chain is used to generate an answer from the retrieved chunks.
  - The response is then displayed on the Streamlit UI.

## Additional Notes
- Ensure that the `.env` file is present and correctly configured before running the app.
- You may need to allow dangerous deserialization when loading FAISS for local use (already handled in the code).
- You can customize the prompt or modify the temperature/model settings for Gemini according to your use case.
