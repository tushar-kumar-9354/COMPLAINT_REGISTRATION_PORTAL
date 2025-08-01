
import google.generativeai as genai
import os

# 1. API Key Security: Use environment variables
# It's highly recommended to set your API key as an environment variable
# For example: export GOOGLE_API_KEY="YOUR_API_KEY"
# The code below will try to get the key from the environment.
# If that fails, it falls back to a hard-coded key (for demonstration purposes only).
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
except KeyError:
    print("Warning: GEMINI_API_KEY environment variable not set. Using a hardcoded key. This is not secure.")
    genai.configure(api_key="AIzaSyBBQosOXYbKNUA5490LcvTT4D9_znWr6hs")

model = genai.GenerativeModel("gemini-2.0-flash")

def get_tone(complaint_text: str) -> str:
    """Analyzes the tone of the complaint using Gemini API."""
    prompt = f"""Analyze the tone of this complaint and return only one word: Angry, Polite, Urgent, or Neutral.
Complaint: "{complaint_text}" """
    
    # 2. API Call Robustness: Add try...except block
    try:
        # Use a low temperature for a more deterministic response
        response = model.generate_content(prompt, generation_config=genai.types.GenerationConfig(temperature=0.1))
        # 3. Handle unexpected responses
        tone = response.text.strip().lower()
        if tone in ["angry", "polite", "urgent", "neutral"]:
            return tone.capitalize()
        else:
            # Fallback for unexpected model output
            print(f"Warning: Unexpected tone output from model: '{response.text.strip()}'. Returning 'Neutral'.")
            return "Neutral"
    except Exception as e:
        print(f"Error getting tone from API: {e}")
        return "Neutral" # Default value on failure

def get_priority(complaint_text: str) -> int:
    """Assigns a priority score (1-5) using Gemini API."""
    prompt = f"""Assign a priority score (1-5) based on the urgency and tone of this complaint. Return only the digit.
Complaint: "{complaint_text}" """
    
    # 2. API Call Robustness: Add try...except block
    try:
        # Use a low temperature for a more deterministic response
        response = model.generate_content(prompt, generation_config=genai.types.GenerationConfig(temperature=0.1))
        # 4. Improved number parsing and validation
        priority_str = "".join(filter(str.isdigit, response.text))
        if priority_str:
            priority = int(priority_str)
            return max(1, min(5, priority)) # Ensure the score is within the 1-5 range
        else:
            print(f"Warning: Priority score not found in API response: '{response.text.strip()}'. Returning 1.")
            return 1 # Default value if no number is found
    except Exception as e:
        print(f"Error getting priority from API: {e}")
        return 1 # Default value on failure

def generate_auto_response(complaint_text: str) -> str:
    """Generates an automated response based on the complaint."""
    # 5. Integrate is_toxic check
    if is_toxic(complaint_text):
        print("Complaint detected as toxic. A standard, non-engaging response will be used.")
        return "Thank you for your feedback. We have received your message and will review it shortly."

    tone = get_tone(complaint_text)
    priority = get_priority(complaint_text)
    
    # Generate a more natural, contextual response based on tone and priority
    prompt = f"""
You are a helpful assistant. Based on the following complaint, write a polite acknowledgment message that reflects the urgency and tone of the complaint. 
Avoid repeating the complaint text verbatim. Do not include priority labels or explicit tone descriptions in the message.
Complaint: "{complaint_text}"
Tone: "{tone}"

The response should:
- Be respectful and professional.
- Acknowledge the issue clearly.
- Imply urgency if needed based on tone.
"""
    # 2. API Call Robustness: Add try...except block
    try:
        response = model.generate_content(prompt)
        generated_response = response.text.strip()
        print(f"Generated auto response: {generated_response}")
        return generated_response
    except Exception as e:
        print(f"Error generating response from API: {e}")
        return "We have received your message and will get back to you as soon as possible." # Default response on failure

# The following functions are not fully integrated but are improved for robustness
def is_toxic(content: str) -> bool:
    """Checks for toxic keywords in the content."""
    toxic_keywords = ["idiot", "stupid", "useless", "hate", "corrupt", "fraud", "moron"]
    content = content.lower()
    return any(word in content for word in toxic_keywords)

def is_duplicate_complaint(description: str, existing_descriptions: list) -> tuple:
    """Dummy logic for checking duplicate complaints (needs a real-world implementation)."""
    if description in existing_descriptions:
        return True, 0.95
    return False, None
def tone_to_emoji(tone: str) -> str:
    """Converts tone to an emoji representation."""
    tone_emojis = {
        "Angry": "😠",
        "Polite": "🙂",
        "Urgent": "⚠️",
        "Neutral": "😐"
    }
    return tone_emojis.get(tone, "❓")  # Default to question mark if tone is unknown

# # Example usage
# complaint_1 = "Thanks!, I am very very happy with the service."
# complaint_2 = "I'm not having trouble with my billing statement. Thanks!, I am very very happy with the service."
# generate_auto_response(complaint_2)
# print(tone_to_emoji(get_tone(complaint_2)))
# print(is_duplicate_complaint(complaint_2, [complaint_1]))
