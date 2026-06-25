from config.gemini_config import model

from agents.hr_agent import hr_agent
from agents.project_agent import project_agent
from agents.analytics_agent import analytics_agent
from agents.report_agent import report_agent


def manager_agent(query):

    prompt = f"""
    You are a routing agent.

    Decide which agent should handle the query.

   Available Agents:

   HR
   PROJECT
   ANALYTICS
   REPORT

   If the query is general knowledge,
   coding,
   interview preparation,
   career guidance,
   or does not belong to the above categories,

   return GENERAL

    Return ONLY ONE WORD.

    Query:
    {query}
    """

    response = model.generate_content(prompt)

    agent = response.text.strip().upper()

    print("Selected Agent:", agent)

    if agent == "HR":
        return hr_agent(query)

    elif agent == "PROJECT":
        return project_agent(query)

    elif agent == "ANALYTICS":
        return analytics_agent(query)

    elif agent == "REPORT":
        return report_agent(query)
    
    elif agent == "GENERAL":

        response = model.generate_content(query)

        return response.text

    else:

      response = model.generate_content(query)

      return response.text