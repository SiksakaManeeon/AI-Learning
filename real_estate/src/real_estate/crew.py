from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool
from dotenv import load_dotenv

load_dotenv()
@CrewBase
class RealEstate():
    """RealEstate crew"""

    agents = 'config/agents.yaml'
    tasks = 'config/tasks.yaml'

    @agent
    def seeder(self) -> Agent:
        return Agent(
            config=self.agents_config['seeder'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def responder(self) -> Agent:
        return Agent(
            config=self.agents_config['responder'],
            tools=[],
            verbose=True
        )

    @agent
    def critic(self) -> Agent:
        return Agent(
            config=self.agents_config['critic'],
            tools=[SerperDevTool()],
            verbose=True
        )
    
    @agent
    def summary(self) -> Agent:
        return Agent(
            config=self.agents_config['summary'],
            tools=[FileWriterTool()],
            verbose=True
        )

    @task
    def seeder_task(self) -> Task:
        return Task(
            config=self.tasks_config['seeder_task'],
        )

    @task
    def responder_task(self) -> Task:
        return Task(
            config=self.tasks_config['responder_task'],
        )
    
    @task
    def critic_task(self) -> Task:
        return Task(
            config=self.tasks_config['critic_task'],
        )
    
    @task
    def summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['summary_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the RealEstate crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
