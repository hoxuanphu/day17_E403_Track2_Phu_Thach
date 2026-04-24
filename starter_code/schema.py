from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    This schema defines the standard fields required for both Group A (PDF) and Group B (Video) data, ensuring a unified structure for the AI agent's Knowledge Base.
    """
    document_id: str
    source_type: str
    author: str
    category: str
    content: str
    timestamp: str
    
