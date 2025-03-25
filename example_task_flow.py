from agents import (
    market_research_agent, feasibility_analysis_agent, customer_persona_agent,
    business_model_agent, competitive_advantage_agent, gtm_strategy_agent,
    monetization_optimization_agent, tech_stack_recommender, investor_pitch_agent
)
from tasks import Crew, Task, Process

def create_startup_analysis_flow(startup_idea: str):
    # Create tasks with assigned agents
    tasks = [
        Task(
            name="Market Research",
            description="Analyze market size, trends, and competitor landscape",
            agent=market_research_agent
        ),
        Task(
            name="Feasibility Analysis",
            description="Evaluate technical and financial feasibility",
            agent=feasibility_analysis_agent
        ),
        Task(
            name="Customer Analysis",
            description="Define target customers and their needs",
            agent=customer_persona_agent
        ),
        Task(
            name="Business Model Development",
            description="Design comprehensive business model",
            agent=business_model_agent
        ),
        Task(
            name="Competitive Analysis",
            description="Identify key differentiators and advantages",
            agent=competitive_advantage_agent
        ),
        Task(
            name="Technology Stack",
            description="Recommend optimal technology stack",
            agent=tech_stack_recommender
        ),
        Task(
            name="Monetization Strategy",
            description="Develop revenue generation strategies",
            agent=monetization_optimization_agent
        ),
        Task(
            name="Go-to-Market Strategy",
            description="Create launch and market entry strategy",
            agent=gtm_strategy_agent
        ),
        Task(
            name="Investor Pitch",
            description="Create compelling pitch materials",
            agent=investor_pitch_agent
        )
    ]

    # Create crew with all agents and tasks
    crew = Crew(
        agents=[
            market_research_agent,
            feasibility_analysis_agent,
            customer_persona_agent,
            business_model_agent,
            competitive_advantage_agent,
            tech_stack_recommender,
            monetization_optimization_agent,
            gtm_strategy_agent,
            investor_pitch_agent
        ],
        tasks=tasks,
        process=Process.HIERARCHICAL
    )

    # Execute all tasks in hierarchical order
    results = crew.kickoff(startup_idea)
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