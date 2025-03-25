from typing import List, Optional
from agents import Agent

class Task:
    def __init__(self, 
                 name: str,
                 description: str,
                 required_agent_role: str,
                 input_data: str,
                 dependencies: Optional[List['Task']] = None):
        self.name = name
        self.description = description
        self.required_agent_role = required_agent_role
        self.input_data = input_data
        self.dependencies = dependencies or []
        self.completed = False
        self.result = None

class TaskOrchestrator:
    def __init__(self):
        self.tasks = []
        self.agents = {}

    def register_agent(self, agent: Agent):
        """Register an agent with the orchestrator"""
        self.agents[agent.role] = agent

    def create_task(self, 
                   name: str, 
                   description: str, 
                   required_agent_role: str,
                   input_data: str,
                   dependencies: Optional[List[Task]] = None) -> Task:
        """Create and register a new task"""
        task = Task(name, description, required_agent_role, input_data, dependencies)
        self.tasks.append(task)
        return task

    def execute_task(self, task: Task) -> str:
        """Execute a single task if its dependencies are met"""
        # Check if all dependencies are completed
        if not all(dep.completed for dep in task.dependencies):
            return f"Cannot execute task '{task.name}' - dependencies not met"

        # Find the appropriate agent
        agent = self.agents.get(task.required_agent_role)
        if not agent:
            return f"No agent found for role: {task.required_agent_role}"

        # Prepare input data including results from dependencies
        enhanced_input = {
            'task_description': task.description,
            'primary_input': task.input_data,
            'dependency_results': {
                dep.name: dep.result for dep in task.dependencies
            }
        }

        # Execute the task
        result = agent.run(str(enhanced_input))
        task.completed = True
        task.result = result
        return result

    def execute_all_tasks(self) -> List[str]:
        """Execute all tasks in the correct order based on dependencies"""
        results = []
        remaining_tasks = self.tasks.copy()

        while remaining_tasks:
            # Find tasks with completed dependencies
            executable_tasks = [
                task for task in remaining_tasks
                if all(dep.completed for dep in task.dependencies)
            ]

            if not executable_tasks:
                break  # No tasks can be executed, might indicate circular dependencies

            # Execute all ready tasks
            for task in executable_tasks:
                result = self.execute_task(task)
                results.append(f"Task '{task.name}' result: {result}")
                remaining_tasks.remove(task)

        return results