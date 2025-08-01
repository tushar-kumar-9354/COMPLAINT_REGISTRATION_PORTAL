import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyBBQosOXYbKNUA5490LcvTT4D9_znWr6hs"  # Replace with your actual key

# Configure the Gemini client
genai.configure(api_key=GEMINI_API_KEY)

def summarize_text(text):
    prompt = f"Summarize this complaint in 2-3 lines:\n{text}"
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    print(f"Summary response: {response.text.strip()}")
    return response.text.strip()

def suggest_category(text):
    prompt = f"""Suggest a category for this complaint:
    {text}
    Choose only from these options: Sanitation, Water, Road, Electricity, Public Safety, Other.
    Return just the category name, nothing else."""
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    print(f"Category suggestion response: {response.text.strip()}")
    return response.text.strip()