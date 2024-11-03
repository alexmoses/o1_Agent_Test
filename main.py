from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os
from agents.clarity_agent import ClarityAgent
from agents.niche_agent import NicheAgent
from agents.action_agent import ActionAgent
from agents.business_strategist import BusinessStrategist

# Load environment variables
load_dotenv()

app = Flask(__name__)

def run_business_builder(user_input):
    try:
        # Initialize agents
        clarity_agent = ClarityAgent()
        niche_agent = NicheAgent()
        action_agent = ActionAgent()
        strategist = BusinessStrategist()

        # Run each agent in sequence
        clarity_insights = clarity_agent.analyze(user_input)
        niche_analysis = niche_agent.analyze(clarity_insights)
        action_plan = action_agent.create_plan(niche_analysis)
        final_strategy = strategist.create_strategy(
            clarity_insights, 
            niche_analysis, 
            action_plan, 
            user_input
        )

        return {
            "clarity_insights": clarity_insights,
            "niche_analysis": niche_analysis,
            "action_plan": action_plan,
            "final_strategy": final_strategy
        }

    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.json.get('user_input', '')
    results = run_business_builder(user_input)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True) 