# Reflection Agents

This folder contains implementation of reflection agents and their application in generating curriculum for educational
applications.

## Reflection Mechanism

The reflection mechanism implemented in these agents includes the following steps:

1. **Initial Output Generation**:
   - An agent called the generation agent produces an initial response of the query.

2. **Evaluation**:
   - The output is assessed against predefined evaluation criteria by another reflection agent.

3. **Feedback Generation**:
   - Feedback is generated, identifying strengths, weaknesses, and specific areas for improvement and shared back.

4. **Iterative Refinement**:
   - The generation agent applies the feedback to produce an improved version of the output.
   - This step is repeated until the desired quality level is achieved or a convergence criterion is met.

This mechanism aligns with research on self-reflective AI systems, which use feedback loops to iteratively refine and improve performance.

---

## Contents

- `1-ielts-essay-reflection-agent.ipynb`: Notebook implementing the reflection agent for IELTS essay generation with feedback.
- `2-gmat-exam-builder-reflection-agent.ipynb`: Notebook implementing the reflection agent for GMAT multiple-choice question generation.

---

## Key Features

### IELTS Essay Generation Agent
- Analyzes essay responses based on IELTS grading criteria.
- Provides iterative suggestions to improve:
  - Task response.
  - Coherence and cohesion.
  - Lexical resource.
  - Grammatical range and accuracy.

### GMAT Exam Builder Agent
- Generates GMAT-style quantitative reasoning questions.
- Validates solutions to ensure correctness and logical consistency.
- Iteratively improves question clarity and answer options.

---

## References

### Core Papers
- **Self-reflection in Language Models**  
  Stiennon, N., et al. (2020). *Learning to Summarize with Human Feedback*.  
  [Paper](https://arxiv.org/abs/2009.01325)  
  This work discusses the role of feedback in improving language models, which underpins the self-reflective capabilities of these agents.

- **Iterative Refinement in AI**  
  Madaan, D., et al. (2023). *Self-Reflective Models: Improving Model Performance through Feedback*.  
  [Paper](https://arxiv.org/abs/2303.11313)  
  This paper introduces iterative refinement techniques for enhanced performance in reasoning tasks.

- **Educational AI**  
  Feng, S., et al. (2018). *Automatic Essay Scoring Systems: A Review of the State of the Art*.  
  [Paper](https://arxiv.org/abs/1811.01744)  
  Insights from this paper informed the essay feedback agent design.

