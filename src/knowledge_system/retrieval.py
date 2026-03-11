from dataclasses import dataclass


@dataclass(slots=True)
class RetrievalResult:
    document_id: str
    score: float


def top_result() -> RetrievalResult:
    return RetrievalResult(document_id="doc_001", score=0.93)


if __name__ == "__main__":
    print(top_result())
