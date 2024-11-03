from .base_agent import BaseAgent

class NicheAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.system_role = """You are a niche market expert. Your role is to analyze 
        business contexts and identify specific, profitable niches. You excel at defining 
        detailed customer avatars and finding untapped market opportunities."""

    def analyze(self, clarity_insights):
        prompt = f"""
        Based on this business context:
        {clarity_insights}
        
        Identify a specific profitable niche and define the ideal customer avatar.
        Include demographics, pain points, and where to find them online.
        """
        return self.get_completion(prompt) 