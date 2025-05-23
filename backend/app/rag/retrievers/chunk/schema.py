from abc import ABC
from typing import Any, Dict, Optional

from pydantic import BaseModel

from app.models import Document


class RerankerConfig(BaseModel):
    enabled: bool = True
    model_id: int = None
    top_n: int = 10


class MetadataFilterConfig(BaseModel):
    enabled: bool = True
    filters: Dict[str, Any] = None


class VectorSearchRetrieverConfig(BaseModel):
    top_k: int = 10
    similarity_top_k: Optional[int] = None
    oversampling_factor: Optional[int] = 5
    reranker: Optional[RerankerConfig] = None
    metadata_filter: Optional[MetadataFilterConfig] = None


class KBChunkRetrievalConfig(BaseModel):
    knowledge_base_ids: list[int] = None


class ChunkRetrievalConfig(BaseModel):
    knowledge_base_ids: list[int] = None


# Retrieved Chunks


class RetrievedChunkDocument(BaseModel):
    id: int
    name: str
    source_uri: str


class RetrievedChunk(BaseModel):
    id: str
    text: str
    metadata: dict
    document_id: Optional[int]
    score: float


class ChunksRetrievalResult(BaseModel):
    chunks: list[RetrievedChunk]
    documents: Optional[list[Document | RetrievedChunkDocument]] = None


class ChunkRetriever(ABC):
    def retrieve_chunks(
        self,
        query_str: str,
        full_document: bool = False,
    ) -> ChunksRetrievalResult:
        """Retrieve chunks"""
