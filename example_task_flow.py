from agents import (
    market_research_agent, feasibility_analysis_agent, customer_persona_agent,
    business_model_agent, competitive_advantage_agent, gtm_strategy_agent,
    monetization_optimization_agent, tech_stack_recommender, investor_pitch_agent
)
from tasks import TaskOrchestrator

def create_startup_analysis_flow(startup_idea: str):
    # Initialize the task orchestrator
    orchestrator = TaskOrchestrator()

    # Register all agents
    orchestrator.register_agent(market_research_agent)
    orchestrator.register_agent(feasibility_analysis_agent)
    orchestrator.register_agent(customer_persona_agent)
    orchestrator.register_agent(business_model_agent)
    orchestrator.register_agent(competitive_advantage_agent)
    orchestrator.register_agent(gtm_strategy_agent)
    orchestrator.register_agent(monetization_optimization_agent)
    orchestrator.register_agent(tech_stack_recommender)
    orchestrator.register_agent(investor_pitch_agent)

    # Create tasks with dependencies
    market_research = orchestrator.create_task(
        name="Market Research",
        description="Analyze market size, trends, and competitor landscape",
        required_agent_role="Market Research Agent",
        input_data=startup_idea
    )

    feasibility = orchestrator.create_task(
        name="Feasibility Analysis",
        description="Evaluate technical and financial feasibility",
        required_agent_role="Feasibility Analysis Agent",
        input_data=startup_idea,
        dependencies=[market_research]
    )

    customer_analysis = orchestrator.create_task(
        name="Customer Analysis",
        description="Define target customers and their needs",
        required_agent_role="Customer Persona Agent",
        input_data=startup_idea,
        dependencies=[market_research]
    )

    business_model = orchestrator.create_task(
        name="Business Model Development",
        description="Design comprehensive business model",
        required_agent_role="Business Model Agent",
        input_data=startup_idea,
        dependencies=[market_research, customer_analysis]
    )

    competitive_advantage = orchestrator.create_task(
        name="Competitive Analysis",
        description="Identify key differentiators and advantages",
        required_agent_role="Competitive Advantage Agent",
        input_data=startup_idea,
        dependencies=[market_research, business_model]
    )

    tech_stack = orchestrator.create_task(
        name="Technology Stack",
        description="Recommend optimal technology stack",
        required_agent_role="Tech Stack Recommender",
        input_data=startup_idea,
        dependencies=[feasibility]
    )

    monetization = orchestrator.create_task(
        name="Monetization Strategy",
        description="Develop revenue generation strategies",
        required_agent_role="Monetization Optimization Agent",
        input_data=startup_idea,
        dependencies=[business_model, customer_analysis]
    )

    gtm_strategy = orchestrator.create_task(
        name="Go-to-Market Strategy",
        description="Create launch and market entry strategy",
        required_agent_role="GTM Strategy Agent",
        input_data=startup_idea,
        dependencies=[competitive_advantage, customer_analysis]
    )

    investor_pitch = orchestrator.create_task(
        name="Investor Pitch",
        description="Create compelling pitch materials",
        required_agent_role="Investor Pitch Agent",
        input_data=startup_idea,
        dependencies=[
            market_research, feasibility, business_model,
            competitive_advantage, gtm_strategy, monetization
        ]
    )

    # Execute all tasks in the correct order
    results = orchestrator.execute_all_tasks()
    return results

if __name__ == "__main__":
    # Example usage
    startup_idea = """
    A mobile app that provides personalized fitness and nutrition tracking using AI
    to create custom workout plans and meal recommendations based on user goals,
    preferences, and progress. The app integrates with wearables for real-time
    health data monitoring and offers community features for motivation and support.
    """
    
    results = create_startup_analysis_flow(startup_idea)
    
    # Print results
    print("\nStartup Analysis Results:")
    print("------------------------")
    for result in results:
        print(f"\n{result}")