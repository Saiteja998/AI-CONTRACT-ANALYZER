import pytest
from src.pipeline import ContractAnalysisPipeline

def test_pipeline_initialization():
    """Test that the pipeline can be instantiated with default variables."""
    pipeline = ContractAnalysisPipeline()
    assert pipeline.db_path == "./chroma_db"
    assert pipeline.embedding_model == "text-embedding-004"
    assert pipeline.llm_model == "gemini-2.5-flash"

def test_pipeline_query_structure():
    """Test that query_contract returns a dict containing standard output keys."""
    pipeline = ContractAnalysisPipeline()
    result = pipeline.query_contract("What is the termination clause?")
    
    assert isinstance(result, dict)
    assert "query" in result
    assert "answer" in result
    assert "sources" in result
    assert result["query"] == "What is the termination clause?"
