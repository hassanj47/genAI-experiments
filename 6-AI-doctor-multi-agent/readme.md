# AI Doctor: Multi-Agent System for Medical Queries

This folder contains an implementation of an agent based system designed to assist with medical queries. 
The system uses two specialized agents powered by the llama3.2:3b model.

---

## Repository Structure

- `llama32-ai-doctor-multi-agent.ipynb`: Notebook implementing a multi-agent framework for handling various medical scenarios, from initial diagnosis to personalized treatment recommendations.

---
### Architectural Overview
1. Two ReAct Agents interact with each other as Doctor and Specialist.
2. Only, the doctor, converses with the patient and elicits symptoms step by step
3. Everytime, the patient mentions a new symptom, the doctor adds it to
a list, searches for plausible diagnoses and asks relevant follow up questions based
on the most likely diagnosis at that step.
5. Once the doctor has reached a definitie conclusion, he passes on the diagnosis
to a Specialist agent.
6. The specialist evaluates the diagnosis andcross-checks it against the set of symptoms through a 
reverse search and recommends treatment. 

### Future Work
1. Experimenting with better models like OpenAI or Anthropic.
2. llama3.2:3b is a small language model which is not as controllable as better models.
3. Designing the agent graph in accordance with the typical workflow for diagnosis.
4. Access to medical domain databases for question and answering.
5. Adding more states to cover patient history, testing recommendations and multiple self-reflection steps.  

