from pydantic import BaseModel, Field


class Customer(BaseModel):
    age: int = Field(
        title="Age",
        ge=0,
    )
    arpu: float = Field(
        title="ARPU",
        ge=-1e5,
        le=1e5
    )


class ChurnResponse(BaseModel):
    score: float = Field(
        title="ChurnScore",
        ge=0,
        le=1
    )
