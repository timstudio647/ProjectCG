# ProjectCG
A project that aims to create an interactive electronic life


26/11/24
Write python script to call the lm studio api
model_id = "google/gemma-4-12b-qat"


Conflict:
  1. The model takes to long to respond
  2. The model doesn't have context and long term memory in this api


Test data:
  Hardware: RTX 5070Ti Laptop(140w)
  Comparison Items: qwen2.5-0.5b-instruct vs google/gemma-4-12b-qat(Thinking disabled)
    Trial 1: hi, introduce yourself!
      qwen2.5-0.5b-instruct: 
        TTFT: 0.162 s
        TTFA: 0.162 s
        Prompt Tokens: 34
        Completion Tokens: 55
        Total Tokens: 89
        Estimated Speed: 269.00 tokens/s
        Total Time: 0.368 s
      google/gemma-4-12b-qat:
        TTFT: 0.096 s
        TTFA: 0.096 s
        Prompt Tokens: 18
        Completion Tokens: 123
        Total Tokens: 141
        Estimated Speed: 62.58 tokens/s
        Total Time: 2.063 s
    Trial 2: hi, ask me a silly question
      qwen2.5-0.5b-instruct: 
        TTFT: 0.037 s
        TTFA: 0.037 s
        Prompt Tokens: 36
        Completion Tokens: 13
        Total Tokens: 49
        Estimated Speed: 373.67 tokens/s
        Total Time: 0.073 s
      google/gemma-4-12b-qat:
        TTFT: 0.258 s
        TTFA: 0.258 s
        Prompt Tokens: 20
        Completion Tokens: 42
        Total Tokens: 62
        Estimated Speed: 68.88 tokens/s
        Total Time: 0.871 s
    Trial 3: hi, I have a story here: Three logicians walk into a bar. The bartender looks up and asks, "Do you all want a beer?" The first logician thinks for a moment and says, "I don't                 know." The second logician also thinks for a moment and says, "I don't know." The third logician smiles confidently and says, "Yes!"
      qwen2.5-0.5b-instruct: 
        TTFT: 0.064 s
        TTFA: 0.064 s
        Prompt Tokens: 107
        Completion Tokens: 337
        Total Tokens: 444
        Estimated Speed: 389.78 tokens/s
        Total Time: 0.930 s
      google/gemma-4-12b-qat:
        TTFT: 0.328 s
        TTFA: 0.328 s
        Prompt Tokens: 93
        Completion Tokens: 549
        Total Tokens: 642
        Estimated Speed: 70.15 tokens/s
        Total Time: 8.154 s



    26/11/25
    add context manage to the current python script
    test long term memory and preformance when the context is long
