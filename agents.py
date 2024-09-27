from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Check if the OpenAI API Key is loaded correctly
os.environ["OPENAI_API_KEY"]= os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

# Researcher agent
researcher = Agent(
    role='Blog Researcher from Youtube video',
    goal='Get relevant video content for the {topic} from the Youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, ML, and GenAI. "
        "Provides suggestions on related content."
    ),
    tools=[yt_tool],
    allow_delegation=True
)

# Writer agent
writer = Agent(
    role='Blog writer',
    goal='Narrate compelling technology-related stories about the video {topic} from the Youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for complex topics, you craft engaging narratives that "
        "captivate and educate, bringing new discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False
)

# Print to confirm agent creation
print("Researcher and Writer agents have been created successfully!")
