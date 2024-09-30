from llama_cpp import Llama


class LlamaModel:
    _instance = None
    model_path = "models/Phi-3-mini-4k-instruct-q4.gguf"

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Llama(model_path=cls.model_path)
        return cls._instance


def generate_content(prompt, max_tokens=256, temperature=0.7, top_p=0.9):
    llama_model = LlamaModel.get_instance()

    modified_prompt = f"Write a detailed paragraph based on the following prompt: {prompt}"

    response = llama_model(
        modified_prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        repeat_penalty=1.2
    )

    if 'choices' in response and len(response['choices']) > 0:
        return response['choices'][0]['text'].strip()
    else:
        return "No response generated."
