### Background Details

This folder contains experiments with improving a baseline RAG in a structured and organized manner through
evaluations of the retrieval and generation steps. 

Using the [LLM-as-a-Judge](https://arxiv.org/abs/2306.05685) paradigm, a few important metrics are calculated namely:

1. Relevance (b/w context and question)
2. Recall (b/w context and ground truth)
3. Faithfulness (b/w context and generated answer)
4. Response quality (b/w generated answer and ground truth)

The definitions for the first three metrics are similar to ones reported in RAGAS and DeepEval.
The reason for not using RAGAS and DeepEval were:

1. Their reliance on OpenAI api for evaluations. 
2. Inconsistency in metric calculations in RAGAS (string matching for a few and LLM based for others).
3. Less control over output format (either Verbose or binary outputs in DeepEval) 

### Experiments
With the above, the following limited experiments were done locally on i71335U/16GB with Ollama+ChromaDB.

#### Baseline Setup:
_Model - llama3.2:1b, chunk_size = 250, chunk_overlap = 0, k=3_

Comments: Showed moderate relevance, recall, quality and very low faithfulness i.e. 
the model relied more on its own knowledge for generating response instead of the
provided context.

#### Updated Setup 1:
_Prompt updated with strict instructions, chunk_overlap = 50_
Resulted in 20% improvement in faithfulness score.

#### Updated Setup 2:
_Model - llama3.2:3b, chunk_size = 350, chunk_overlap = 50, k=4_ 
Resulted in improvements in relevance and response quality by 
30% and 10% respectively.

Recall did not improve in these experiments much.

### Evaluation Summary:

| experiment_id | relevance_score | recall_score | faithfulness_score | response_quality_score | comments |
| ------------- | --------------- | ------------ | ------------------ | ---------------------- | -------- |
| 0             | 0.625882        | 0.5          | 0.469412           | 6.470588               | baseline |
| 1             | 0.625882        | 0.5          | 0.550588           | 6.823529               | setup 1  |
| 2             | 0.815882        | 0.5          | 0.500588           | 7.058824               | setup 2  |


### Future Work
1. With better memory & compute resources, we can do a parametrized search over pipeline parameters to find
   the optimal pipeline w.r.t evaluation metrics for retrieval and generation.
2. Calculating retrieval metrics based on information retrieval techniques requires a good and extensive
   ground truth. For example, calculating recall the IR way, would require all relevant chunks in ground
   truth for each query. We can leverage LLM's + Vector stores together for such ground truth generation. 
