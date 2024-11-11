### Background
This folder contains an experiment to generate synthetic question/answer datasets from Clinical guideline
documents. It can be useful to generate domain specific QA datasets as well as extended to create dialogues.

The approach is similar to the one in Deep Eval's Synthesizer, but provides a template to modify it
as needed with custom similarity logic, query fromat restrictions for specialized knowledge and 
advanced filtering that you can implement for your own use case.

### Approach
The approach is as follows:
1. Chunk and vectorize a domain specific document. It can be in a vector store. For this example,
   it is stored in-memory.
2. Pick a random chunk.
3. Find K similar chunks to the reference chunk based on a similarity metric. Here, cosine similarity was used.
4. Pass these chunks as context to an LLM for generating a QA pair relevant to the context.
5. Filter QA pairs for duplicates or any other domain specific constraints.

### Results
Here, we generate QA pairs from a Clinical guideline for managing Covid19. This serves as a good starting point of generating 
domain specific datasets for LLM finetuning. 

### Future Work
1. The generated QA pairs can further be evaluated using the evaluation metrics like relevance, recall and faithfulness etc.
2. This approach can be experimented with to generate dialogue datasets in future.
