from dataclasses import dataclass


@dataclass
class Contract:
    contract_id: str
    filename: str
    text: str