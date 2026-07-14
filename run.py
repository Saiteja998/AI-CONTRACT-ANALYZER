from src.pipeline.query import ContractQueryPipeline
from src.utils.json_writer import save_json


def main():

    pipeline = ContractQueryPipeline()

    question = "What are the termination clauses?"

    answer = pipeline.ask(question)

    result = pipeline.ask(question)

    print("\n========== AI RESPONSE ==========\n")
    print(result["response"])

    print("\n========== CONFIDENCE ==========\n")
    print(f"Confidence Score: {result['confidence']:.2f}")

    print("\n========== SOURCES ==========\n")

    for source in result["sources"]:
      print(source)
    save_json(result, "termination_result.json")


if __name__ == "__main__":
    main()