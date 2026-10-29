from pydantic import BaseModel, Field

class CodeGenerationResult(BaseModel):
    code: str = Field(
    description="Complete Python source code without Markdown fences."
    )

    explanation: str = Field(
    description="Brief explanation of the changes made."
    )

