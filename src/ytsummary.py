from langchain_community.document_loaders import YoutubeLoader
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI
import os

def get_summary(url):
	loader = YoutubeLoader.from_youtube_url(url, language=os.getenv("LANGUAGE", "en"))
	documents = loader.load()
	llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
	
	# Split the document into chunks
	from langchain.text_splitter import RecursiveCharacterTextSplitter
	text_splitter = RecursiveCharacterTextSplitter(
    	chunk_size=20000,
    	chunk_overlap=0
	)
	chunks = []
	for document in documents:
		chunks += (text_splitter.create_documents([document.page_content], [document.metadata]))

	# Run the summarization chain
	chain = load_summarize_chain(llm, chain_type="map_reduce")
	summary = chain.invoke(chunks)

	return summary['output_text']

def get_summary2(url):
	loader = YoutubeLoader.from_youtube_url(url, language=os.getenv("LANGUAGE", "en"))
	documents = loader.load()
	llm = ChatOpenAI(temperature=0, model_name="gpt-4o")

	# Split the document into chunks
	from langchain.text_splitter import RecursiveCharacterTextSplitter
	text_splitter = RecursiveCharacterTextSplitter(
		chunk_size=20000,
		chunk_overlap=0
	)

	chain = load_summarize_chain(llm, chain_type="stuff")
	summary = []
	for document in documents:
		chunk = (text_splitter.create_documents([document.page_content], [document.metadata]))
		summary.append(chain.invoke(chunk))
	return "\n".join([s['output_text'] for s in summary])

def get_summary3(url):
	loader = YoutubeLoader.from_youtube_url(url, language=os.getenv("LANGUAGE", "en"))
	documents = loader.load()
	llm = ChatOpenAI(temperature=0, model_name="gpt-4o")

	# Split the document into chunks
	from langchain.text_splitter import RecursiveCharacterTextSplitter
	text_splitter = RecursiveCharacterTextSplitter(
		chunk_size=5000,
		chunk_overlap=0
	)
		
	from langchain.prompts import ChatPromptTemplate, PromptTemplate, HumanMessagePromptTemplate
	prompt = ChatPromptTemplate(
    input_variables=['text'],
    messages=[
        HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                input_variables=['text'],
                template="""
Read the provided text and identify all the key concepts:
Identify: Recognize all distinct concepts mentioned in the text.
For each concept, Reword and Rephrase the concept if necessary to ensure clarity and conciseness.
Output the summary of each concept and the conclusions and points of view of the discussion about it without any title in plain text.
Ensure that the output is comprehensive and captures every idea presented in the text. Use same language as the text.

Text:
{text}
"""
                )
            )
    ]
)

	from langchain_core.runnables import RunnablePassthrough

	chain = (
    {
        "text": RunnablePassthrough(),
    }
    | prompt
    | llm
)
	summary = []
	for document in documents:
		chunk = (text_splitter.create_documents([document.page_content], [document.metadata]))
		summary.append(chain.invoke(chunk))
	return "\n".join([aimessage.content for aimessage in summary])

