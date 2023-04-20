from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from dotenv import load_dotenv


def load_data() -> VectorstoreIndexCreator:
    """Load data from file and create index"""
    loader = TextLoader("data/20221224_mensaje_navidad_esp_rey_felipe.txt", encoding="utf8")
    index = VectorstoreIndexCreator().from_loaders([loader])
    return index


if __name__ == "__main__":
    # load environment variables
    load_dotenv()

    # load data and create index
    index = load_data()

    # loop until user exits with Ctrl+C
    while True:
        try:
            # ask user for a question
            query = input("> prompt: ")
            resp = index.query(query)

            # print response
            print(resp)

        except KeyboardInterrupt:
            break
