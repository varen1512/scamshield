from typing import Literal
from pydantic import BaseModel, Field


class ScamAssessment(BaseModel):
    verdict: Literal[
        "suspicious", "legitimate", "uncertain"
    ]

    scam_type: Literal[
        "kyc_phishing",
        "fake_job",
        "upi_fraud",
        "impersonation",
        "lottery",
        "parcel",
        "utility",
        "other",
        "none"
    ]

    red_flags: list[str] = Field(
        description="Warning signs supported by the message"
    )

    explanation: str

    recommended_action: str