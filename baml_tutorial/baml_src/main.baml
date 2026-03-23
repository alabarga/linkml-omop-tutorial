// Tutorial: structured extraction from free text.

class Person {
  name string @description("Full name as stated or best normalized form")
  sex string? @description("e.g. male, female, unknown — use lowercase single word if possible")
  birthdate string? @description("ISO date YYYY-MM-DD if inferable; otherwise null")
}

function ExtractPersonFromText(raw_text: string) -> Person {
  client OpenAI
  prompt #"
    You extract a single person record from unstructured text.

    Rules:
    - If a field is not present or ambiguous, use null (omit or JSON null for optional strings).
    - **name**: required if any person is mentioned; concatenate given + family if split.
    - **sex**: only if explicitly stated or strongly implied by pronouns/titles; else null.
    - **birthdate**: only if a clear calendar date; normalize to YYYY-MM-DD; else null.

    Text to parse:
    ---
    {{ raw_text }}
    ---
  "#
}
