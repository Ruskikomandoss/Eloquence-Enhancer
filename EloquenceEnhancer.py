from langchain_core.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chat_models.openai import ChatOpenAI
from EE_prompts import system_prompt, user_prompt


def czat():
    return ChatOpenAI(
        temperature=0.9,
        model='gpt-4-1106-preview',
        max_tokens=1000
    )

def get_language():
    return input("Write your output language here:\n")

def get_phrase():
    return input("Write your phrase here:\n")


if __name__ == "__main__":
    ready_system_prompt = SystemMessagePromptTemplate.from_template(system_prompt)
    ready_human_prompt = HumanMessagePromptTemplate.from_template(user_prompt)
    chat_message = ChatPromptTemplate.from_messages([ready_system_prompt, ready_human_prompt]).format_messages(phrase=f'{get_phrase()}', language=f'{get_language()}')
    ready_chat = czat()
    print(ready_chat(chat_message).content)
    
