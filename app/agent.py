from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from dotenv import load_dotenv
load_dotenv()

ABSOLUTE_FILE_PATH = "C:\\Users\\[User_Name]\\[Path]"

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='filesystem_assistant_agent',
    instruction='Help the user to manage their files. You can list files, read files, etc.',
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="npx",
                args=[
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    ABSOLUTE_FILE_PATH
                ]
            ),
        )
    ],
)
