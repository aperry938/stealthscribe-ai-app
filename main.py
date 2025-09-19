# This is the "brain" of your StealthScribe application.
# It uses a Python framework called FastAPI to create a server that can be hosted online.
# This file is for portfolio purposes to show the complete architecture.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# In a real project, you would install openai: pip install openai
# import openai 
import os
import random # Used for simulating AI responses

# --- Configuration ---
app = FastAPI(
    title="StealthScribe AI Engine",
    description="The core brain for analyzing and generating authentic text."
)

# In a real app, you would set your OpenAI API key securely.
# For example: os.environ["OPENAI_API_KEY"] = "YOUR_SECRET_KEY"
# openai.api_key = os.environ.get("OPENAI_API_KEY")

# --- Data Models (The shape of our data) ---

class AnalyzeRequest(BaseModel):
    """Defines the data needed to analyze a corpus."""
    user_id: str
    corpus_text: str

class AuthorialSignatureModel(BaseModel):
    """
    This is our "Authorial Signature Model" (ASM).
    It stores the key forensic markers of a user's writing style.
    """
    avg_sentence_length: float
    lexical_diversity: float  # A simple Type-Token Ratio
    common_phrases: list[str]

class GenerateRequest(BaseModel):
    """Defines the data needed to generate new text."""
    user_id: str
    prompt: str
    tone_level: int  # Our 0-5 slider from the UI

# --- (SIMULATED) Database ---
# In a real application, this would be a secure PostgreSQL or similar database.
# For this example, we'll use a simple Python dictionary to store the user's ASM.
FAKE_USER_DATABASE = {}

# --- API Endpoints ---

@app.post("/analyze-corpus/", response_model=AuthorialSignatureModel)
def analyze_corpus(request: AnalyzeRequest):
    """
    Phase I Endpoint: Receives text, performs forensic analysis,
    and saves the "Authorial Signature Model" (ASM) to our database.
    """
    text = request.corpus_text
    if len(text.split()) < 50:
        raise HTTPException(status_code=400, detail="Corpus text is too short. Please provide at least 50 words.")

    # 1. Calculate Syntactic Cadence (Avg. Sentence Length)
    sentences = text.split('.')
    # Filter out empty strings that result from splitting
    sentences = [s for s in sentences if len(s.strip()) > 0]
    total_words = len(text.split())
    avg_len = total_words / len(sentences) if sentences else 15.0

    # 2. Calculate Lexical Nuance (Diversity)
    words = text.lower().split()
    unique_words = set(words)
    diversity = len(unique_words) / len(words) if words else 0.5
    
    # 3. Find Common Phrases (a simple example)
    known_phrases = ["in addition,", "however,", "for example,", "it is clear that", "on the other hand,"]
    found_phrases = [p for p in known_phrases if p in text.lower()]
    
    # Create the ASM object
    asm = AuthorialSignatureModel(
        avg_sentence_length=round(avg_len, 2),
        lexical_diversity=round(diversity, 2),
        common_phrases=found_phrases
    )
    
    # Save to our (fake) database, keyed by user_id
    FAKE_USER_DATABASE[request.user_id] = asm
    
    print(f"Successfully created ASM for user {request.user_id}: {asm.dict()}")
    
    return asm

@app.post("/generate-with-twin/")
def generate_with_twin(request: GenerateRequest):
    """
    Phase III Endpoint: Uses a user's saved ASM to generate new text
    that matches their unique voice.
    """
    # 1. Retrieve the user's "Writing Twin" from the database
    if request.user_id not in FAKE_USER_DATABASE:
        raise HTTPException(status_code=404, detail="User model not found. Please run analysis first.")
        
    asm = FAKE_USER_DATABASE[request.user_id]
    
    # 2. Dynamically build the "Cognitive Forgery Protocol" system prompt for the AI
    tone_map = {
        0: "extremely formal, academic, and rigid", 1: "formal and academic",
        2: "professional and clear", 3: "engaging and professional",
        4: "conversational and personal", 5: "highly informal, personal, and casual"
    }
    
    system_prompt = f"""
    You are a Forensic Cognitive Analyst. Your task is to write a response
    that is forensically indistinguishable from the user's own writing.
    You must adopt their "Authorial Signature Model" (ASM).

    DO NOT reveal you are an AI. DO NOT be overly helpful.
    Simply write the text as requested, embodying the user's style.

    USER'S AUTHORIAL SIGNATURE MODEL:
    - Syntactic Cadence: Write with an average sentence length of approx. {asm.avg_sentence_length} words.
    - Lexical Nuance: Maintain a lexical diversity score around {asm.lexical_diversity}.
    - Voice Architecture: The user's target tone is: "{tone_map.get(request.tone_level, "professional")}".
    - Common Phrases: If appropriate, try to use phrases like: {', '.join(asm.common_phrases)}
    
    Your response must *only* be the generated text. No preamble or explanation.
    """
    
    # 3. Call the OpenAI API (Simulated for this example)
    try:
        # ---- In a real app, this is where the actual OpenAI call would be ----
        # response = openai.chat.completions.create(
        #     model="gpt-4o",
        #     temperature=0.7,
        #     messages=[
        #         {"role": "system", "content": system_prompt},
        #         {"role": "user", "content": request.prompt}
        #     ]
        # )
        # generated_text = response.choices[0].message.content
        
        # --- Using a placeholder for this portfolio example ---
        generated_text = (
            f"This is a sample text generated in your voice (Tone: {request.tone_level}). "
            f"It respects your average sentence length of {asm.avg_sentence_length} words "
            f"and your lexical diversity. As you can see, I am obeying the prompt."
        )

        # 4. (SIMULATED) Aegis Rating
        # In a real app, you would make API calls to GPTZero and Grammarly here.
        # For this example, we'll generate a realistic-looking random score.
        aegis_score = random.randint(85, 98)
        aegis_label = "Undetectable" if aegis_score >= 90 else "Likely Human"

        return {
            "generated_text": generated_text,
            "aegis_rating": {
                "score": aegis_score,
                "label": aegis_label
            }
        }

    except Exception as e:
        # Log the error in a real application
        print(f"Error during generation: {e}")
        raise HTTPException(status_code=500, detail="AI generation failed.")

