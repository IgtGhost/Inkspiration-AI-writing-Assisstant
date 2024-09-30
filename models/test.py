from llama_cpp import Llama

def test_phi3mini():
    # Path to your downloaded PHI 3 Mini model in GGUF format
    model_path = "Phi-3-mini-4k-instruct-q4.gguf"  # Adjust the path as necessary

    # Load the model
    llama = Llama(model_path=model_path)

    # Generate a response to a sample prompt
    prompt = (
        "Write a detailed essay about democracy, including its origins, principles, "
        "advantages, disadvantages, and its role in modern society."
    )

    response = llama(
        prompt,
        max_tokens=2048,  # Set a higher max_tokens to allow for a longer response

        temperature=0.5,  # Control the randomness of the output
        top_p=0.9,  # Adjust diversity of the output
        repeat_penalty=1.2  # Prevent repetitive text
    )

    # Extract the text from the response
    if 'choices' in response and len(response['choices']) > 0:
        output_text = response['choices'][0]['text'].strip()
        print("Model Response:", output_text)
    else:
        print("No response generated.")

if __name__ == "__main__":
    test_phi3mini()
