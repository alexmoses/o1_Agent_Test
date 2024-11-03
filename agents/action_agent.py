from .base_agent import BaseAgent

class ActionAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.system_role = """You are an action-oriented business coach. Your expertise 
        is in creating specific, actionable plans that entrepreneurs can implement immediately. 
        You provide exact steps, platforms, and templates for finding and engaging potential clients."""

    def create_plan(self, niche_info):
        prompt = f"""
        Based on this niche analysis:
        {niche_info}
        
        Create a specific action plan including:
        1. Exact platforms to use
        2. Search terms to find leads
        3. Message templates for outreach
        4. Specific offers to make
        """
        return self.get_completion(prompt) 