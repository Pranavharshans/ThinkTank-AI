import warnings
warnings.filterwarnings('ignore')



class Agent:
    def __init__(self, role, goal, backstory, allow_delegation=False, verbose=True):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.allow_delegation = allow_delegation
        self.verbose = verbose

    def run(self, input_data):
        print(f"Agent {self.role} processing input: {input_data}")

# Define agents with detailed roles, goals, and backstories

market_research_agent = Agent(
    role="Market Research Agent",
    goal="Gather market data, trends, and competitor insights for startup idea validation",
    backstory=(
        "You are tasked with collecting industry trends, competitor analysis, and identifying market gaps. "
        "Your role is essential in validating the startup idea by providing real-time market insights."
    ),
    allow_delegation=False,
    verbose=True
)

feasibility_analysis_agent = Agent(
    role="Feasibility Analysis Agent",
    goal="Evaluate technical feasibility, financial viability, and legal viability of startup ideas",
    backstory=(
        "You assess whether a startup idea is technically and financially viable, while considering legal constraints. "
        "Your analysis forms the basis of the idea's feasibility assessment."
    ),
    allow_delegation=False,
    verbose=True
)

customer_persona_agent = Agent(
    role="Customer Persona Agent",
    goal="Define target customer segments and identify their pain points for the startup idea",
    backstory=(
        "You create detailed customer personas by analyzing demographic and behavioral data. "
        "Your insights help validate the startup idea by pinpointing customer needs."
    ),
    allow_delegation=False,
    verbose=True
)

business_model_agent = Agent(
    role="Business Model Agent",
    goal="Design robust business models and revenue frameworks for the startup",
    backstory=(
        "You develop monetization strategies and pricing models to ensure the business viability of the startup idea. "
        "Your work maps out the economic potential of the startup."
    ),
    allow_delegation=False,
    verbose=True
)

competitive_advantage_agent = Agent(
    role="Competitive Advantage Agent",
    goal="Identify unique selling propositions and strategic differentiators for the startup idea",
    backstory=(
        "You analyze competitors and market conditions to determine what sets the startup apart. "
        "Your insights help craft a competitive strategy."
    ),
    allow_delegation=False,
    verbose=True
)

gtm_strategy_agent = Agent(
    role="GTM Strategy Agent",
    goal="Develop effective go-to-market strategies for launching the startup",
    backstory=(
        "You design actionable marketing and distribution plans that drive the startup's success. "
        "Your strategies ensure the idea reaches its target audience effectively."
    ),
    allow_delegation=False,
    verbose=True
)

monetization_optimization_agent = Agent(
    role="Monetization Optimization Agent",
    goal="Identify and refine revenue-generation strategies for the startup idea",
    backstory=(
        "You focus on optimizing revenue channels by analyzing pricing and sales strategies. "
        "Your role is to ensure sustainable profitability for the startup."
    ),
    allow_delegation=False,
    verbose=True
)

tech_stack_recommender = Agent(
    role="Tech Stack Recommender",
    goal="Recommend an optimal technology stack for building the startup",
    backstory=(
        "You evaluate current technology trends and propose suitable tech stacks to support the startup idea. "
        "Your recommendations align with strategic and technical needs."
    ),
    allow_delegation=False,
    verbose=True
)

investor_pitch_agent = Agent(
    role="Investor Pitch Agent",
    goal="Create compelling pitch decks and executive summaries for the startup idea",
    backstory=(
        "You compile insights from all agents and transform them into persuasive materials for potential investors. "
        "Your role is pivotal in communicating the startup's value proposition."
    ),
    allow_delegation=False,
    verbose=True
)

if __name__ == '__main__':
    test_idea = "Revolutionary startup idea"
    market_research_agent.run(test_idea)
    feasibility_analysis_agent.run(test_idea)
    customer_persona_agent.run(test_idea)
    business_model_agent.run(test_idea)
    competitive_advantage_agent.run(test_idea)
    gtm_strategy_agent.run(test_idea)
    monetization_optimization_agent.run(test_idea)
    tech_stack_recommender.run(test_idea)
    investor_pitch_agent.run(test_idea)