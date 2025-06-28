from crewai import Crew, Process
from agents import PlannerAgent, StorytellerAgent, BookerAgent, ContextAgent
from tasks import PlanTask, StoryTask, BookTask, ContextTask
from models.itinerary import Itinerary

class TravelOrchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.storyteller = StorytellerAgent()
        self.booker = BookerAgent()
        self.context = ContextAgent()
    
    def create_itinerary(self, destination, dates, preferences) -> Itinerary:
        # Create tasks
        plan_task = PlanTask(destination, dates, preferences, self.planner)
        context_task = ContextTask(destination, dates, self.context)
        
        # Execute planning crew
        planning_crew = Crew(
            agents=[self.planner, self.context],
            tasks=[plan_task, context_task],
            process=Process.sequential
        )
        itinerary = planning_crew.kickoff()
        
        # Add destination story
        if preferences.include_story:
            story_task = StoryTask(destination, self.storyteller)
            story_crew = Crew(
                agents=[self.storyteller],
                tasks=[story_task],
                process=Process.hierarchical
            )
            itinerary.story = story_crew.kickoff()
        
        return itinerary
    
    def book_trip(self, user, itinerary):
        book_task = BookTask(user, itinerary, self.booker)
        booking_crew = Crew(
            agents=[self.booker],
            tasks=[book_task],
            process=Process.sequential
        )
        return booking_crew.kickoff()