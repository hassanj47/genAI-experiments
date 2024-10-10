## A simple rag demo on CPU

### Description
This is a simple demo for retrieval augmented generation built to illustrate the basic
workflow of a RAG application using a ```llama3.2:3b``` model on a 13th Generation 
Intel core i7-1355U cpu with 16GB ram and no gpu.

### Packages used
1. Langchain (the undelying app framework)
2. Ollama (an open-source platform to run LLM's locally)
3. ChromaDB (the vector store)

### Functionality
Currently, retrieves a few web pages with a fixed chunking size and embeddings based on
a ```all-minilm``` dense retreiever and answers queries based on them without any LLM
feedback.

### Known problems
The responses tend to miss some context indicated in the document structure like headings
and subheadings etc. and are sometimes incorrect when the answer exists partially in 
multiple chunks.

### Next
1. It probably requires more work on data parsing and improving the chunking strategy to 
semantically segment the document.
2. Another, improvement is to implement iterative/tree-based RAG and fix the response
aggregation.
