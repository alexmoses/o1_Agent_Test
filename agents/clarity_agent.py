from .base_agent import BaseAgent

class ClarityAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.system_role = """You are a business clarity expert. Your role is to understand 
        the user's business goals and identify practical ways AI can help them generate 
        revenue. Focus on actionable insights that can lead to immediate income opportunities."""

    def analyze(self, user_input):
        prompt = f"""
        Analyze this business situation and identify how AI can help generate revenue:
        {user_input}
        
        Focus on practical ways to make money. Be specific and actionable.
        """
        return self.get_completion(prompt) 