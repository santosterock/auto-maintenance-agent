from smolagents import (
    CodeAgent,
    LiteLLMModel,
)

model = LiteLLMModel(
    model_id="lm_studio/google/gemma-3-12b",
    litellm_provider="local",
    api_base="http://localhost:1234/v1",
    api_key="some key",
)

runModel = CodeAgent(
    tools=[],
    model=model,
    additional_authorized_imports=["re"],

    # system_prompt="""You are an automobile maintenance schedule agent
    # Follow these steps:
    # 1. Use your built-in data to gather information
    # 2. if needed accept an automobile user-manual from the user
    # 3. Parse the user-manual for relevance and give answers only using the data in the user manual
    # 4. Save the final markdown file
    # """
)


def write_output(topic, output_file="output.md"):

    result = runModel.run(f"""Respond to the question: {topic}
    1. First, research the topic thoroughly, focus on specific products and sources
    2. Then, use any attachment that the user provided to provide specific responses
    3. Finally, edit and polish the content
    """)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"Output has been saved to {output_file}")

    return result


topic = "What maintenance should i do at 40,000 miles in my 2022 jeep wrangler jlu"
print(topic)
write_output(topic)
