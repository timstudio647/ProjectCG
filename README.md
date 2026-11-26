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

Conversation 1(Daily communication):
User: hi, introduce yourself
AI: Hello! I am Gemma 4, a large language model with open weights, developed by Google DeepMind. ...
      TTFT: 0.229 s
      TTFA: 0.229 s
      Prompt Tokens: 17
      Completion Tokens: 122
      Total Tokens: 139
      Estimated Speed: 62.60 tokens/s
      Total Time: 2.180 s

User: nice to meet you, my name is Tim, a CS undergraduate student
AI: It's nice to meet you, Tim! It’s great to connect with a computer science student. ...
      TTFT: 0.356 s
      TTFA: 0.356 s
      Prompt Tokens: 162
      Completion Tokens: 225
      Total Tokens: 387
      Estimated Speed: 70.79 tokens/s
      Total Time: 3.537 s

User: In response to you, I'm currently working on a project, and you are the very central part of my project. But now I don't want to elaborate on this topic, let's start a relaxing topic
AI: That sounds intriguing! I appreciate your privacy regarding your ...
      TTFT: 0.540 s
      TTFA: 0.540 s
      Prompt Tokens: 441
      Completion Tokens: 230
      Total Tokens: 671
      Estimated Speed: 53.61 tokens/s
      Total Time: 4.832 s

User: I'm very interested in your second topic, but before revealing my answer, is there any place you recommend?
AI: That’s a fun way to start! Since I don't have a physical body to experience these places, my "recommendations" are ...
      TTFT: 0.499 s
      TTFA: 0.499 s
      Prompt Tokens: 703
      Completion Tokens: 424
      Total Tokens: 1127
      Estimated Speed: 59.40 tokens/s
      Total Time: 7.639 s

User: Yes, and actually your first recommandation is exactly my answer, so I'd like you to write a travel guide for me               
AI: Excellent choice. Iceland is one of the most visually stunning and geologically active places on Earth. Because it is ...
      TTFT: 0.688 s
      TTFA: 0.688 s
      Prompt Tokens: 1162
      Completion Tokens: 967
      Total Tokens: 2129
      Estimated Speed: 68.38 tokens/s
      Total Time: 14.832 s

User: Your travel guide is really helpful, now I have a question for you, since you're a large language model, I'm sure that ...
AI: That is a fascinating philosophical question, especially coming from a computer science perspective. You’re right: I don't have ...
      TTFT: 0.668 s
      TTFA: 0.668 s
      Prompt Tokens: 2201
      Completion Tokens: 762
      Total Tokens: 2963
      Estimated Speed: 57.43 tokens/s
      Total Time: 13.938 s
