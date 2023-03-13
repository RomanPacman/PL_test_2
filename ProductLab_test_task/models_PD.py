from pydantic import BaseModel, Field


class ParsModel(BaseModel):
    article: int = Field(alias="nm_id")
    title: str = Field(alias="imt_name")
    brand: str = Field(alias="brand_name")