import spacy
import os
import re
import pandas as pd
from collections import Counter

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract information from resume text
def extract_information(resume_text):
    # NLP pipeline
    doc = nlp(resume_text)
    
    # Extracting name (assuming the first proper noun as name)
    name = None
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break
    
    # Extracting email
    email = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', resume_text)
    email = email.group(0) if email else None
    
    # Extracting phone number
    phone = re.search(r'\+?\d[\d -]{8,}\d', resume_text)
    phone = phone.group(0) if phone else None
    
    # Extracting skills (keywords matching predefined skill set)
    skills = ["Python", "SQL", "Power BI", "Tableau", "JavaScript", "React", "Excel", "Machine Learning", "NLP"]
    found_skills = [skill for skill in skills if skill.lower() in resume_text.lower()]
    
    # Extracting experience (years of experience)
    experience = re.search(r'\b(\d+)\+?\s*years?\b', resume_text, re.IGNORECASE)
    experience = experience.group(1) if experience else "0"
    
    return {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Skills": ", ".join(found_skills),
        "Experience": experience
    }

# Function to analyze multiple resumes in a folder


def analyze_resumes(folder_path):
    resumes_data = []
    
    # Read resumes from folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"): # Process only .txt files
            with open(os.path.join(folder_path, file_name), "r", encoding="utf-8") as file:
                resume_text = file.read()
                resume_info = extract_information(resume_text)
                resume_info["File"] = file_name
                resumes_data.append(resume_info)
    
    # Convert to DataFrame
    df = pd.DataFrame(resumes_data)
    return df

# Main program
if __name__ == "__main__":
    # Specify the folder containing resume files
    # folder_path = "resumes"
    folder_path=r"F:\Python course\ResumeAnlyser\resumes"
    # folder_path=r"resumes/"
    # Analyze resumes
    if os.path.exists(folder_path):
        df = analyze_resumes(folder_path)
        print("Resume Analysis Completed!")
        print(df)
        
        # Save results to CSV
        output_file = "resume_analysis.csv"
        df.to_csv(output_file, index=False)
        print(f"Analysis saved to {output_file}")
    else:
        print(f"Folder '{folder_path}' does not exist. Please create it and add .txt resumes.")