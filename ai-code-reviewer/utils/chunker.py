from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_code(code_files):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    documents = []
    for file in code_files:
        chunks = splitter.split_text(file["content"])
        for chunk in chunks:
            documents.append({
                "text": chunk,
                "metadata": {"file": file["path"]}
            })
    return documents
