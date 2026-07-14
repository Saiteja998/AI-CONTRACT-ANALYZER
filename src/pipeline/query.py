from src.pipeline.retrieve import Retriever
from src.llm.extractor import ClauseExtractor
from src.evaluation.confidence import ConfidenceCalculator
import pprint




class ContractQueryPipeline:
    """
    End-to-end query pipeline.
    """

    def __init__(self):
        self.retriever = Retriever()
        self.extractor = ClauseExtractor()
        self.confidence = ConfidenceCalculator()

    def ask(self, question: str):

        # Retrieve relevant chunks
        results = self.retriever.retrieve(question)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        pprint.pprint(metadatas[0])

        context = ""

        sources = []

        for doc, meta in zip(documents, metadatas):

            context += f"""
Contract: {meta['filename']}
Chunk: {meta['chunk']}

{doc}

----------------------------------
"""

            sources.append({
                "contract": meta["filename"],
                "chunk": meta["chunk"]
            })

        response = self.extractor.extract(
            query=question,
            context=context
        )
        

        
        

        print("HAS contract_summary?", "contract_summary" in response)
        print("FINAL RESPONSE:", response)

        print("\n========== FINAL RESPONSE ==========")
        print(response)
        print("====================================")

        confidence = self.confidence.calculate(len(sources))

        return {
            "response": response,
            "sources": sources,
            "confidence": confidence
        }