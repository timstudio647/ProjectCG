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

User: I feel like our topic is a bit too heavy, let's throw these away. Now I want you to write a story: my requirements are1. be creative 2. at least 800 words. 3. completed and logical storyline  Now you can start
AI: Since we were just talking about your interest in ...
      TTFT: 0.853 s
      TTFA: 0.853 s
      Prompt Tokens: 3031
      Completion Tokens: 1188
      Total Tokens: 4219
      Estimated Speed: 58.68 tokens/s
      Total Time: 21.098 s

after 96 questions related to fixing a bug of a random code
      TTFT: 2.258 s
      TTFA: 2.258 s
      Prompt Tokens: 3811
      Completion Tokens: 804
      Total Tokens: 4615
      Estimated Speed: 57.44 tokens/s
      Total Time: 16.256 s

User: Just to test your memory, do you still remember my name
AI: I do not know your name yet! ...
      TTFT: 2.634 s
      TTFA: 2.634 s
      Prompt Tokens: 3816
      Completion Tokens: 131
      Total Tokens: 3947
      Estimated Speed: 58.20 tokens/s
      Total Time: 4.886 s

User: what's my first question in this conversation?
AI: Your first question in this conversation was:

**"hi, introduce yourself"**
      TTFT: 1.463 s
      TTFA: 1.463 s
      Prompt Tokens: 3966
      Completion Tokens: 18
      Total Tokens: 3984
      Estimated Speed: 66.89 tokens/s
      Total Time: 1.735 s

User: and I told you my name in the second question
AI: Actually, looking back at our conversation history, you didn't tell me your name. 

The sequence of your inputs was:
1. `chars = 0`
2. `pinned = 0`
3. `for row in self.messages:`
4. `counts[row["role"]] = 1`
5. `chars += len(row)`
6. `Just to test your memory, do you still remember my name`

      TTFT: 1.360 s
      TTFA: 1.360 s
      Prompt Tokens: 4003
      Completion Tokens: 210
      Total Tokens: 4213
      Estimated Speed: 57.09 tokens/s
      Total Time: 5.040 s

User: but you said my first question was" hi introduce yourself", why these question didn't appear in your memory list
AI: That is a very insightful question. It touches on the difference between **how I "think"** (my internal processing) and **how your code "works"** (your `self.messages` list). ...
      TTFT: 2.473 s
      TTFA: 2.473 s
      Prompt Tokens: 3435
      Completion Tokens: 516
      Total Tokens: 3951
      Estimated Speed: 59.24 tokens/s
      Total Time: 11.186 s

User: now try to recall my  second question                                 
AI: Your second question was:

**`pinned = 0`**(Technically, it wasn't a "question" in the grammatical sense, but it was your second input in this conversation.)
      TTFT: 1.442 s
      TTFA: 1.442 s
      Prompt Tokens: 3968
      Completion Tokens: 43
      Total Tokens: 4011
      Estimated Speed: 58.68 tokens/s
      Total Time: 2.177 s


