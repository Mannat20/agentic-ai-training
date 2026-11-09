import os
from dotenv import load_dotenv
load_dotenv()
MongoDB_user = os.getenv("MongoDB_user")
MongoDB_password = os.getenv("MongoDB_password")
MongoDB_Cluster= os.getenv("MongoDB_Cluster")
MongoDB_uri = "mongodb+srv://{MongoDB_user}:{MongoDB_password}@{MongoDB_Cluster}"
agent_id = os.getenv("agent_id")
api_key = os.getenv("French_tutor_api_key")
openai_api_key1 = os.getenv("openai_api_key1")