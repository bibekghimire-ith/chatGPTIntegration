import openai

openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"

def askChatGpt(prompt):
    # Generate a response
    # response = openai.Completion.create(
    #     engine=model_engine,
    #     prompt=prompt,
    #     max_tokens=1024,
    #     # n=1,
    #     # stop=None,
    #     temperature=0.5,
    # )
    # print(response)
    # print(response.choices[0])

    response = openai.Completion.create(
        model=model_engine,
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n"]
    )
    responseText = response.choices[0].text
    return responseText

print("********* ChatGPT Integration *********")
print("Provide Human: value as 'Q' to quit")
print("***************************************")
query = ""
while(True):
    prompt = input(" Human: \n")
    print("")
    if(prompt=="Q"):
        exit(0)
    else:
        # query += f"\n\n{prompt}"
        # print(query)
        response = askChatGpt(query)
        print(" AI:")
        print(response.lstrip())
        print("--------")