from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=250
    )

    return text_splitter.split_documents(documents)