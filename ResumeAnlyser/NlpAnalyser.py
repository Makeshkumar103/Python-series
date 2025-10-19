import re
import spacy
import pandas as pd
from spacy.matcher import Matcher

# Load spaCy's pre-trained model
nlp = spacy.load("en_core_web_sm")

# Define a function to extract names from the text
def extract_name(resume_text):
    doc = nlp(resume_text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

# Define a function to extract phone numbers
def extract_phone_number(resume_text):
    phone_pattern = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
    matches = phone_pattern.findall(resume_text)
    return matches[0] if matches else None

# Define a function to extract email addresses
def extract_email(resume_text):
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    matches = email_pattern.findall(resume_text)
    return matches[0] if matches else None

# Define a function to extract skills from the text
def extract_skills(resume_text, skills_list):
    resume_text = resume_text.lower()
    extracted_skills = [skill for skill in skills_list if skill.lower() in resume_text]
    return extracted_skills

# Define a function to extract experience details
def extract_experience(resume_text):
    experience_pattern = re.compile(r'(?i)(\d+\+? years? experience|experience of \d+ years)')
    matches = experience_pattern.findall(resume_text)
    return matches if matches else None

# Define a function to extract education details
def extract_education(resume_text, education_keywords):
    resume_text = resume_text.lower()
    education = [keyword for keyword in education_keywords if keyword.lower() in resume_text]
    return education

# Load a list of predefined skills and education keywords
skills_list = ["Python", "Java", "C++", "SQL", "Machine Learning", "Deep Learning", "NLP", "Data Analysis", "Cloud Computing"]
education_keywords = ["Bachelor's", "Master's", "PhD", "B.Sc", "M.Sc", "B.Tech", "M.Tech", "MBA"]

# Define a function to analyze a resume
def analyze_resume(resume_text):
    name = extract_name(resume_text)
    phone = extract_phone_number(resume_text)
    email = extract_email(resume_text)
    skills = extract_skills(resume_text, skills_list)
    experience = extract_experience(resume_text)
    education = extract_education(resume_text, education_keywords)

    return {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Skills": skills,
        "Experience": experience,
        "Education": education
    }

# Example Usage
# if __name__ == "__main__":
#     sample_resume = """
#     John Doe
#     Email: john.doe@example.com
#     Phone: (123) 456-7890
#     Experienced software developer with 5+ years experience in Python, Machine Learning, and Data Analysis.
#     Education: Bachelor's in Computer Science from XYZ University.
#     """

#     analysis = analyze_resume(sample_resume)
#     print(pd.DataFrame([analysis]))

if __name__ == "__main__":
    import os
    
    # Directory containing resumes in .txt format
    resumes_dir = "resumes/"
    resume_files = [f for f in os.listdir(resumes_dir) if f.endswith(".txt")]
    
    for resume_file in resume_files:
       # with open(os.path.join(resumes_dir, resume_file), "r", encoding="utf-8") as file:\n            resume_text = file.read()
            print(f"Analyzing {resume_file}...")
            analysis = analyze_resume(resume_text)
            print(pd.DataFrame([analysis]))
            print("\n" + "-"*50 + "\n")
           
           
            # results.append(analysis)
            # pd.DataFrame(results).to_csv("resume_analysis_results.csv", index=False)
