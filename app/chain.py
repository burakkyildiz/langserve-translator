from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def build_chain(model):
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "Just translate the following from {input_language} "
            "to {output_language}. Do not write anything else."
        ),
        ("human", "{text}")
    ])

    parser = StrOutputParser()

    return prompt | model | parser