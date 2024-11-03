from openai import OpenAI
from dotenv import load_dotenv
import os
from agents.clarity_agent import ClarityAgent
from agents.niche_agent import NicheAgent
from agents.action_agent import ActionAgent
from agents.business_strategist import BusinessStrategist

# Load environment variables
load_dotenv()

def run_business_builder():
    # Get user input
    user_input = input("Describe your business goals and current situation: ")

    try:
        # Initialize agents
        clarity_agent = ClarityAgent()
        niche_agent = NicheAgent()
        action_agent = ActionAgent()
        strategist = BusinessStrategist()

        # Run each agent in sequence
        print("\nAnalyzing your business situation...")
        clarity_insights = clarity_agent.analyze(user_input)

        print("\nIdentifying your ideal niche...")
        niche_analysis = niche_agent.analyze(clarity_insights)

        print("\nCreating your action plan...")
        action_plan = action_agent.create_plan(niche_analysis)

        print("\nGenerating your business strategy...")
        final_strategy = strategist.create_strategy(
            clarity_insights, 
            niche_analysis, 
            action_plan, 
            user_input
        )

        # Print final strategy
        print("\n=== Your Business Strategy ===")
        print(final_strategy)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_business_builder() 