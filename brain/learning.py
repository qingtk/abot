from brain.memory import save

def daily_learning(llm):
    prompt = "Give me one important AI concept to learn today."
    result = llm.generate(prompt)
    save(result)
    return result