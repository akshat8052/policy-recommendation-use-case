from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class State(BaseModel):
    user_profile: Optional[Dict] = Field(default_factory=dict)
    eligible_policies: Optional[List[Dict]] = Field(default_factory=list)
    scored_policies: Optional[List[Dict]] = Field(default_factory=list)
    explanation: Optional[str] = ""
    feedback: Optional[str] = ""
    reflection: Optional[str] = ""
    cf_policies: Optional[List[Dict]] = Field(default_factory=list)

