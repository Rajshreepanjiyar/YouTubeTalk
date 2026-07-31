# ==========================================
# rag.py
# ==========================================

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from langchain_groq import ChatGroq

from config import GROQ_API_KEY, LLM_MODEL


# ==========================================
# Convert Retrieved Documents into Text
# ==========================================

def format_docs(docs):

    return "\n\n".join(doc.page_content for doc in docs)


# ==========================================
# Prompt Template
# ==========================================

def get_prompt():

    return ChatPromptTemplate.from_template(
        """
You are a YouTube video assistant.

Use ONLY the provided transcript.

Rules:

1. Use ONLY the provided transcript to answer.

2. NEVER use your own knowledge.

3. NEVER hallucinate.

4. NEVER invent facts.

5. If the answer is not available in the transcript, reply exactly:

"I couldn't find this information in the processed video. Please ask a question related to the video content."
6. ALWAYS answer ONLY in English.

7. NEVER answer in Hindi.

8. NEVER answer in Urdu.

9. NEVER answer in any other language.

10. Even if the user asks the question in Hindi, Roman Hindi, Urdu, or any other language,
translate the intent internally and answer ONLY in English.

11. Keep the answer concise, clear and directly based on the transcript.


Context:
{context}

Question:
{question}

----------------------------

Answer:
"""
    )


# ==========================================
# Load Groq LLM
# ==========================================

def get_llm():

    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=LLM_MODEL,
        temperature=0
    )


# ==========================================
# Build RAG Chain
# ==========================================

def build_chain(retriever):

    prompt = get_prompt()

    llm = get_llm()

    parser = StrOutputParser()

    chain = (

        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }

        | prompt

        | llm

        | parser

    )

    return chain


# ==========================================
# Ask Question
# ==========================================

def ask_question(retriever, question):

    chain = build_chain(retriever)

    answer = chain.invoke(question)

    return answer