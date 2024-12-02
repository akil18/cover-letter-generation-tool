import pandas as pd
import chromadb
import uuid

class Technology:
    def __init__(self, file_path="app/resource/technologies.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="technology")

    def load_technologies(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Technology"], metadatas={"links": row["Links"]}, ids=[str(uuid.uuid4())])

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])
