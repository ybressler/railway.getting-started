from typing import List, Union

from pydantic import BaseModel, Field


class NameLength(BaseModel):
    n_chars: int = Field(..., description="Character length")
    role_name: str = Field(..., description="Name of the role")

class TechRolesSummary(BaseModel):
    """
    A summary of all tech roles in the Mongo DB
    for the [Artists Who Code SuperBlocks app](https://app.superblocks.com/applications/9e80434c-64a6-480f-bac3-0093f0139dbf/pages/ecb00eea-214d-4877-8c62-f88f999b5f94)
    """
    nice_message: str = Field(..., description="Human readible summary of contents of this collection")
    n_roles: int = Field(..., description="Number of distinct roles in this database", ge=0)
    role_names: List[str] = Field(..., description="List of distinct roles in this collection")
    shortest_name: NameLength = Field(..., description="The shortest name present in the collection")
    longest_name: NameLength = Field(..., description="The longest name present in the collection")
