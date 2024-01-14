# generator.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generate_code_file(language: str, program_type: str) -> str:
    """
    Generates a code file content using OpenAI API.
    """
    prompt = f"""
    Generate a complete, working {language} program that implements a {program_type}.
    
    Requirements:
    - The code MUST be at least 100 lines long. This is a STRICT requirement.
    - Do NOT use filler comments or huge whitespace. Use meaningful code (multiple functions, classes, error handling, helper methods).
    - If the simple logic is too short, EXPAND it: add a CLI menu, add input validation, add logging, add unit tests within the file.
    - It must be self-contained and runnable.
    - If external libraries are absolutely necessary, list them in a comment at the top.
    - Include error handling and clean code practices.
    - Add a header comment with instructions on how to run the file.
    - The output should ONLY be the code, no markdown code blocks (```) or explanation text outside the code. 
      If you include markdown blocks, I will have to strip them, so prefer just raw code.
    
    Specifics for {program_type}:
    - Be creative and robust.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4", 
            messages=[
                {"role": "system", "content": "You are an expert polyglot programmer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2500
        )
        
        content = response.choices[0].message.content
        
        # Cleanup markdown code blocks if present
        if content.startswith("```"):
            lines = content.split('\n')
            lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            content = "\n".join(lines)
            
        return content
        
    except Exception as e:
        print(f"Error generating code for {language} - {program_type}: {e}")
        return f"# Error generating code: {e}"
