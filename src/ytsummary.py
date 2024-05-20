from langchain_community.document_loaders import YoutubeLoader
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI

def get_summary(url):
	loader = YoutubeLoader.from_youtube_url(url)
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
	loader = YoutubeLoader.from_youtube_url(url)
	documents = loader.load()
	llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

	# Split the document into chunks
	from langchain.text_splitter import RecursiveCharacterTextSplitter
	text_splitter = RecursiveCharacterTextSplitter(
		chunk_size=2000,
		chunk_overlap=0
	)

	chain = load_summarize_chain(llm, chain_type="stuff")
	summary = []
	for document in documents:
		chunk = (text_splitter.create_documents([document.page_content], [document.metadata]))
		summary.append(chain.invoke(chunk))
	return "\n".join([s['output_text'] for s in summary])


