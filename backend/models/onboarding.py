from uuid import UUID

from pydantic import BaseModel


class Onboardings(BaseModel):
    user_id: UUID
    onboarding_b1: bool
    onboarding_b2: bool
    onboarding_b3: bool
