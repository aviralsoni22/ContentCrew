from crewai import Task
from tools import yt_tool
from agents import researcher, writer

#research task

research_task = Task(
    description = (
        "Identify the video on the {topic}."
        "Get detailed information about the video from the channel."
    ),
    expected_output='A comprehensive 3 paragraph long request based on the topic {topic}',
    tools = [yt_tool],
    agent = researcher
)

writer_task = Task(
    description = (
        "Get the information from the youtube channel on the topic {topic}."
    ),
    expected_output='Summarize the information from the youtube channel video on the topic {topic} and create the content based on that information',
    tools = [yt_tool],
    agent = writer,
    async_execution = False, #agents working parallelly if true
    output_file = 'new-blog-post.md'
)