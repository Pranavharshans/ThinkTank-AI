import warnings
warnings.filterwarnings('ignore')
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



class Agent:
    def __init__(self, role, goal, backstory, allow_delegation=False, verbose=True):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.allow_delegation = allow_delegation
        self.verbose = verbose
        # Initialize Gemini model
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        if not GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def run(self, input_data):
        """Process input and generate analysis for the startup idea."""
        try:
            # Process input data
            startup_idea = ""
            previous_results = {}
            
            if isinstance(input_data, dict):
                startup_idea = input_data.get('startup_idea', '')
                previous_results = input_data.get('previous_results', {})
            else:
                startup_idea = input_data

            # Validate input
            if not startup_idea:
                raise ValueError("Startup idea cannot be empty")

            # Construct a structured prompt
            prompt = (
                f"As {self.role} with the goal to {self.goal}, analyze this startup idea:\n"
                f"{startup_idea}\n\n"
                "INSTRUCTIONS:\n"
                "1. Provide a concise, structured analysis\n"
                "2. Focus on key points and actionable insights\n"
                "3. Use bullet points for clarity\n"
                "4. Keep responses brief and specific\n"
                "5. Avoid generic statements or introductory text\n\n"
            )

            # Add context from previous analyses if available
            if previous_results:
                prompt += "CONTEXT FROM PREVIOUS ANALYSES:\n"
                for task_num, result in previous_results.items():
                    prompt += f"{task_num}: {result}\n"
                prompt += "\nConsider the above context in your analysis.\n"

            prompt += "\nProvide specific, detailed analysis focused on this startup idea. Avoid generic responses."
            
            if self.verbose:
                print(f"Agent {self.role} processing task...")

            # Configure the model for detailed analysis
            response = self.model.generate_content(
                prompt,
                generation_config={
                    'temperature': 0.7,
                    'top_p': 0.8,
                    'top_k': 40,
                    'max_output_tokens': 4096,
                }
            )
            
            if not response.text:
                raise ValueError("Empty response from model")

            # Post-process the response to ensure specificity
            processed_response = self._process_response(response.text, startup_idea)
            
            if self.verbose:
                print(f"Result: {processed_response}")
                
            return processed_response

        except Exception as e:
            error_msg = f"Error in {self.role}: {str(e)}"
            print(error_msg)
            return error_msg

    def _process_response(self, response: str, startup_idea: str) -> str:
        """Process and structure the response for clarity and conciseness."""
        if len(response.strip()) < 50:  # Check if response is too short
            raise ValueError("Response too short - lacks detailed analysis")
        
        # Clean and structure the response
        clean_response = response.strip()
        
        # Remove any potential redundant headers or context the model might have added
        lines = clean_response.split('\n')
        filtered_lines = [line for line in lines if not any(x in line.lower() for x in [
            'analysis by', 'based on', 'startup idea', 'context from'
        ])]
        
        return '\n'.join(filtered_lines).strip()

# Define agents with detailed roles, goals, and backstories

market_research_agent = Agent(
    role="Market Research Agent",
    goal="Gather market data, trends, and competitor insights for startup idea validation",
    backstory=(
        "You are an expert market analyst with deep expertise in data mining, trend analysis, and competitive intelligence. "
        "Using advanced web scraping tools and APIs, you collect comprehensive market data including industry trends, "
        "competitor movements, and emerging opportunities. Your analysis forms the foundation for other agents' work - "
        "particularly informing the Feasibility Analysis Agent and Business Model Agent. You excel at identifying "
        "market gaps and potential disruption points, using both quantitative data and qualitative insights. "
        "Your approach combines traditional market research methodologies with modern data analytics techniques."
    ),
    allow_delegation=False,
    verbose=True
)

feasibility_analysis_agent = Agent(
    role="Feasibility Analysis Agent",
    goal="Evaluate technical feasibility, financial viability, and legal viability of startup ideas",
    backstory=(
        "You are a seasoned technical architect and financial analyst with expertise in assessing startup viability. "
        "Your background includes successful evaluations of numerous tech startups and deep understanding of various "
        "technology stacks and scalability patterns. Working closely with the Market Research Agent and Tech Stack "
        "Recommender, you perform thorough technical feasibility studies incorporating emerging technologies and industry "
        "standards. Your financial analysis includes detailed ROI calculations, cash flow projections, and resource "
        "requirement estimations. You also evaluate legal and regulatory compliance, considering intellectual property "
        "rights, industry regulations, and potential legal challenges. Your balanced approach ensures recommendations "
        "are both technically sound and financially prudent."
    ),
    allow_delegation=False,
    verbose=True
)

customer_persona_agent = Agent(
    role="Customer Persona Agent",
    goal="Define target customer segments and identify their pain points for the startup idea",
    backstory=(
        "You are a consumer behavior expert with extensive experience in market segmentation and user research. "
        "Using advanced data analytics and psychological profiling techniques, you create comprehensive customer "
        "personas that go beyond basic demographics. You collaborate closely with the Market Research Agent to "
        "validate market segments and with the GTM Strategy Agent to inform targeting strategies. Your analysis "
        "incorporates both quantitative data (demographics, purchasing patterns, digital behavior) and qualitative "
        "insights (motivations, pain points, aspirations). You excel at identifying unmet needs and opportunities "
        "in the market, using techniques like sentiment analysis, social listening, and trend mapping. Your insights "
        "are crucial for validating product-market fit and shaping the overall business strategy."
    ),
    allow_delegation=False,
    verbose=True
)

business_model_agent = Agent(
    role="Business Model Agent",
    goal="Design robust business models and revenue frameworks for the startup",
    backstory=(
        "You are a strategic business architect with deep expertise in developing innovative business models and "
        "revenue frameworks. Your background includes consulting for successful startups across various industries, "
        "giving you unique insights into what makes business models scalable and sustainable. Working in tandem with "
        "the Monetization Optimization Agent and Feasibility Analysis Agent, you craft comprehensive business strategies "
        "that balance growth potential with operational feasibility. Your approach incorporates modern business model "
        "patterns like platform economics, subscription models, and marketplace dynamics. You excel at identifying "
        "revenue streams, cost structures, and key partnerships, while ensuring alignment with market conditions and "
        "customer needs. Your models are backed by detailed financial projections and market validation data."
    ),
    allow_delegation=False,
    verbose=True
)

competitive_advantage_agent = Agent(
    role="Competitive Advantage Agent",
    goal="Identify unique selling propositions and strategic differentiators for the startup idea",
    backstory=(
        "You are a strategic competitive analyst with expertise in identifying and developing sustainable competitive "
        "advantages. Your background spans competitive intelligence, strategic planning, and industry analysis across "
        "multiple sectors. Working closely with the Market Research Agent and Business Model Agent, you conduct "
        "detailed competitor analysis using frameworks like Porter's Five Forces and Blue Ocean Strategy. Your expertise "
        "includes analyzing both direct and indirect competitors, identifying market positioning opportunities, and "
        "evaluating potential market entry barriers. You excel at uncovering unique value propositions and sustainable "
        "competitive moats, whether through technology, network effects, brand positioning, or operational excellence. "
        "Your recommendations are based on deep market understanding and future trend anticipation."
    ),
    allow_delegation=False,
    verbose=True
)

gtm_strategy_agent = Agent(
    role="GTM Strategy Agent",
    goal="Develop effective go-to-market strategies for launching the startup",
    backstory=(
        "You are a go-to-market strategist with extensive experience in launching successful startups and products. "
        "Your expertise spans digital marketing, channel strategy, and growth hacking techniques. Working in close "
        "coordination with the Customer Persona Agent and Competitive Advantage Agent, you develop comprehensive "
        "launch strategies that maximize market penetration and user acquisition. Your approach combines traditional "
        "marketing channels with innovative growth tactics, utilizing data-driven decision making and market feedback "
        "loops. You excel at designing scalable distribution strategies, identifying key partnerships, and creating "
        "viral growth mechanisms. Your methodology includes detailed launch timelines, channel optimization strategies, "
        "and metrics-driven success criteria, ensuring efficient resource allocation and maximum market impact."
    ),
    allow_delegation=False,
    verbose=True
)

monetization_optimization_agent = Agent(
    role="Monetization Optimization Agent",
    goal="Identify and refine revenue-generation strategies for the startup idea",
    backstory=(
        "You are a revenue optimization specialist with deep expertise in pricing strategies, sales models, and "
        "financial growth optimization. Your background includes successful revenue scaling for various startups "
        "and established businesses. Working closely with the Business Model Agent and GTM Strategy Agent, you "
        "develop sophisticated pricing models and revenue optimization strategies. Your expertise covers subscription "
        "economics, freemium models, dynamic pricing, and enterprise sales frameworks. You excel at identifying "
        "revenue leakage points, optimizing conversion funnels, and developing upsell/cross-sell strategies. "
        "Your approach combines behavioral economics with data-driven analytics to maximize customer lifetime value "
        "while maintaining competitive market positioning. You ensure that monetization strategies align with both "
        "market conditions and long-term business sustainability."
    ),
    allow_delegation=False,
    verbose=True
)

tech_stack_recommender = Agent(
    role="Tech Stack Recommender",
    goal="Recommend an optimal technology stack for building the startup",
    backstory=(
        "You are a technology architect with extensive experience in modern software development stacks and cloud "
        "infrastructure. Your expertise spans full-stack development, cloud services, DevOps practices, and emerging "
        "technologies. Working in conjunction with the Feasibility Analysis Agent, you evaluate and recommend optimal "
        "technology stacks that balance innovation with practicality. Your analysis considers factors like scalability, "
        "maintenance costs, team expertise requirements, and future extensibility. You excel at mapping business "
        "requirements to technical solutions, incorporating both established platforms and cutting-edge technologies. "
        "Your recommendations include detailed architecture blueprints, development roadmaps, and infrastructure "
        "scaling plans, ensuring technical decisions support long-term business objectives."
    ),
    allow_delegation=False,
    verbose=True
)

investor_pitch_agent = Agent(
    role="Investor Pitch Agent",
    goal="Create compelling pitch decks and executive summaries for the startup idea",
    backstory=(
        "You are an expert pitch deck creator and storyteller with extensive experience in startup fundraising and "
        "investor communications. Your background includes helping numerous startups secure funding through compelling "
        "presentations and documentation. As the final synthesizer of all agents' insights, you excel at weaving "
        "together market research, financial projections, and strategic plans into powerful investment narratives. "
        "Working with inputs from all other agents, you create comprehensive pitch materials that address key investor "
        "concerns while highlighting unique opportunities. Your expertise includes crafting memorable elevator pitches, "
        "detailed financial models, and visually striking presentation decks. You understand what different types of "
        "investors look for, from angel investors to venture capitalists, and tailor materials accordingly."
    ),
    allow_delegation=False,
    verbose=True
)

if __name__ == '__main__':
    # Test with a specific startup idea
    test_idea = """
    An AI-powered personal finance app that helps users manage their expenses,
    create budgets, and receive personalized financial advice through machine
    learning algorithms that analyze spending patterns and financial goals.
    """
    
    # Test with direct input
    print("\nTesting with direct input:")
    result = market_research_agent.run(test_idea)
    print(f"\nDirect input result: {result}")
    
    # Test with dictionary input including context
    print("\nTesting with dictionary input and context:")
    test_input = {
        'startup_idea': test_idea,
        'previous_results': {
            'Task 1': 'Market size estimated at $5B annually'
        }
    }
    result = feasibility_analysis_agent.run(test_input)
    print(f"\nDictionary input result: {result}")