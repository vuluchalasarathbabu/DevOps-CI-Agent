from google_adk import Agent, Tool
import requests

# Tool that queries FastAPI for Jenkins logs
class JenkinsLogsTool(Tool):
    def run(self, query: str):
        # Fetch last 10 logs from FastAPI
        resp = requests.get("http://localhost:8000/logs?n=10")
        return resp.json()

# Create agent with the tool
agent = Agent(
    name="jenkins-agent",
    tools=[JenkinsLogsTool()]
)

if __name__ == "__main__":
    # Example interaction
    print(agent.run("Show me the latest Jenkins logs"))
