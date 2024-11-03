from .base_agent import BaseAgent

class BusinessStrategist(BaseAgent):
    def __init__(self):
        super().__init__()
        self.system_role = """You are a senior business strategist. Your expertise lies 
        in synthesizing various insights into coherent, practical business strategies. 
        You excel at creating clear, actionable plans that align with business goals 
        while maintaining focus on revenue generation."""

    def create_strategy(self, clarity_insights, niche_analysis, action_plan, user_input):
        prompt = f"""
        Synthesize this information into a clear business strategy:
        
        ORIGINAL GOALS:
        {user_input}
        
        CLARITY INSIGHTS:
        {clarity_insights}
            
        NICHE ANALYSIS:
        {niche_analysis}
            
        ACTION PLAN:
        {action_plan}
            
        Create a concise, step-by-step business strategy that aligns with the user's goals and can be started today.
        """
        return self.get_completion(prompt)