from enum import Enum
from typing import List
from agents import Agent

class Process(Enum):
    SEQUENTIAL = "sequential"
    HIERARCHICAL = "hierarchical"

class Task:
    def __init__(self, name: str, description: str, agent: Agent):
        self.name = name
        self.description = description
        self.agent = agent
        self.result = None

class Crew:
    def __init__(self, agents: List[Agent], tasks: List[Task], process: Process):
        self.agents = agents
        self.tasks = tasks
        self.process = process

    def kickoff(self, startup_idea: str) -> List[str]:
        results = []
        
        if self.process == Process.SEQUENTIAL:
            # Execute tasks in sequence
            for task in self.tasks:
                task.result = task.agent.run({
                    'task_description': task.description,
                    'primary_input': startup_idea,
                    'previous_results': {t.name: t.result for t in self.tasks if t.result}
                })
                results.append(f"Task '{task.name}' result: {task.result}")
        
        elif self.process == Process.HIERARCHICAL:
            # Execute tasks in a hierarchical manner where each task can use results 
            # from previous tasks and delegate subtasks to other agents
            
            # Start with market research as the root task
            market_research_task = next(t for t in self.tasks if t.name == "Market Research")
            market_research_task.result = market_research_task.agent.run({
                'task_description': market_research_task.description,
                'primary_input': startup_idea,
                'previous_results': {}
            })
            results.append(f"Task '{market_research_task.name}' result: {market_research_task.result}")
            
            # Second level: Feasibility Analysis and Customer Analysis
            second_level = [t for t in self.tasks if t.name in ["Feasibility Analysis", "Customer Analysis"]]
            for task in second_level:
                task.result = task.agent.run({
                    'task_description': task.description,
                    'primary_input': startup_idea,
                    'previous_results': {'Market Research': market_research_task.result}
                })
                results.append(f"Task '{task.name}' result: {task.result}")
            
            # Third level: Business Model and Tech Stack
            third_level = [t for t in self.tasks if t.name in ["Business Model Development", "Technology Stack"]]
            for task in third_level:
                prev_results = {
                    'Market Research': market_research_task.result,
                    'Feasibility Analysis': next(t for t in second_level if t.name == "Feasibility Analysis").result,
                    'Customer Analysis': next(t for t in second_level if t.name == "Customer Analysis").result
                }
                task.result = task.agent.run({
                    'task_description': task.description,
                    'primary_input': startup_idea,
                    'previous_results': prev_results
                })
                results.append(f"Task '{task.name}' result: {task.result}")
            
            # Fourth level: Competitive Analysis and Monetization
            fourth_level = [t for t in self.tasks if t.name in ["Competitive Analysis", "Monetization Strategy"]]
            for task in fourth_level:
                prev_results = {t.name: t.result for t in self.tasks if t.result}
                task.result = task.agent.run({
                    'task_description': task.description,
                    'primary_input': startup_idea,
                    'previous_results': prev_results
                })
                results.append(f"Task '{task.name}' result: {task.result}")
            
            # Fifth level: GTM Strategy
            gtm_task = next(t for t in self.tasks if t.name == "Go-to-Market Strategy")
            prev_results = {t.name: t.result for t in self.tasks if t.result}
            gtm_task.result = gtm_task.agent.run({
                'task_description': gtm_task.description,
                'primary_input': startup_idea,
                'previous_results': prev_results
            })
            results.append(f"Task '{gtm_task.name}' result: {gtm_task.result}")
            
            # Final level: Investor Pitch
            pitch_task = next(t for t in self.tasks if t.name == "Investor Pitch")
            prev_results = {t.name: t.result for t in self.tasks if t.result}
            pitch_task.result = pitch_task.agent.run({
                'task_description': pitch_task.description,
                'primary_input': startup_idea,
                'previous_results': prev_results
            })
            results.append(f"Task '{pitch_task.name}' result: {pitch_task.result}")

        return results