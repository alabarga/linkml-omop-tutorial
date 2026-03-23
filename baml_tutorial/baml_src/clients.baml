// OpenAI — OPENAI_API_KEY + OPENAI_MODEL required.

client<llm> OpenAI {
  provider openai
  options {
    model env.OPENAI_MODEL
    api_key env.OPENAI_API_KEY
  }
}
