from openai import OpenAI
import time

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
)

def generate_response(messages, model_name, temperature=0.7):

    start_time = time.perf_counter()

    first_token_time = None
    first_answer_time = None
    last_token_time = None

    usage = None
    full_response = ""

    stream = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=temperature,
        stream=True,
        stream_options={"include_usage": True}
    )

    print("AI: ", end="", flush=True)

    for chunk in stream:

        if chunk.usage is not None:
            usage = chunk.usage

        if not chunk.choices:
            continue

        delta = chunk.choices[0].delta

        content = delta.content or ""

        reasoning = (
            getattr(delta, "reasoning_content", None)
            or getattr(delta, "reasoning", None)
            or ""
        )

        if content or reasoning:

            now = time.perf_counter()

            if first_token_time is None:
                first_token_time = now

            last_token_time = now

        if content:

            if first_answer_time is None:
                first_answer_time = now

            print(content, end="", flush=True)
            full_response += content

    end_time = time.perf_counter()

    print("\n")
    print("-" * 45)
    print("[Inference Statistics]")

    if first_token_time is not None:
        ttft = first_token_time - start_time
        print(f"TTFT: {ttft:.3f} s")

    if first_answer_time is not None:
        ttfa = first_answer_time - start_time
        print(f"TTFA: {ttfa:.3f} s")

    if usage is not None:

        print(f"Prompt Tokens: {usage.prompt_tokens}")
        print(f"Completion Tokens: {usage.completion_tokens}")
        print(f"Total Tokens: {usage.total_tokens}")

        if first_token_time is not None:

            generation_time = last_token_time - first_token_time

            if generation_time > 0:
                tps = (usage.completion_tokens - 1) / generation_time
                print(f"Estimated Speed: {tps:.2f} tokens/s")

    print(f"Total Time: {end_time - start_time:.3f} s")
    print("-" * 45)

    return full_response

model_id = "google/gemma-4-12b-qat"


userMsg = input()

while userMsg!="quit":
    messages = [{"role": "user", "content": userMsg}]
    response = generate_response(messages,model_id, temperature=0.75)
    userMsg = input()

#test input: 
# hi, introduce yourself!
# hi, ask me a silly question
# hi, I have a story here: Three logicians walk into a bar. The bartender looks up and asks, "Do you all want a beer?" The first logician thinks for a moment and says, "I don't know." The second logician also thinks for a moment and says, "I don't know." The third logician smiles confidently and says, "Yes!"