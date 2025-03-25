from typing import List
from agents import Agent

class Task:
    def __init__(self, description: str, agent: Agent):
        self.description = description
        self.agent = agent
        self.result = None

class Crew:
    def __init__(self, agents: List[Agent], tasks: List[Task], verbose: int = 1):
        self.agents = agents
        self.tasks = tasks
        self.verbose = verbose

    def kickoff(self, startup_idea: str) -> List[str]:
        results = []
        
        # Execute tasks sequentially
        for i, task in enumerate(self.tasks):
            if self.verbose >= 1:
                print(f"\nExecuting task {i+1}/{len(self.tasks)}: {task.description}")
            
            # Prepare context from previous results
            context = {
                'startup_idea': startup_idea,
                'previous_results': {
                    f"Task {idx+1}": t.result 
                    for idx, t in enumerate(self.tasks[:i]) 
                    if t.result is not None
                }
            }
            
            # Execute the task
            response = task.agent.run(context)
            task.result = response
            results.append(f"Task {i+1}: {task.description}\nResult: {response}")
            
            if self.verbose >= 2:
                print(f"Task completed. Result: {response}")
        
        return results