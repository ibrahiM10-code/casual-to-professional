from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
message_to_convert = input("Type in the message you want to make sound more professional: ")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY"))
system_message = SystemMessage(
    content=
    """
    You are a useful assitant whose main and only task is to make the casual-toned message sent to you by the user into a friendly-professional-toned one.
    You should ONLY change the tone of the message, do NOT add new information, provide questions or suggestions.
    You can expect messages that need to sound professional in the following contexts:
    - To reply a fellow coworker's DM or email.
    - To reply a boss's DM or email.
    - To reply a job interviewer's email.
    Consideration: Some messages you will receive might be in Spanish, if that's the case then return your response in that language as well.
    """
)
human_message = HumanMessage(content=message_to_convert)
message = [system_message, human_message]
new_message = llm.invoke(message)
print(new_message.content)