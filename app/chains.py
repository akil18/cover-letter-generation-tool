import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-70b-versatile",
)
    
    def extract_task(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped data is from the job page of a website.
            Your task is to extract the job details and return them in JSON format containing following keys: 'experienceLevel', 'skills' and 'description'.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )

        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data': cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too large. Unable to parse tasks.")
        return res if isinstance(res, list) else res
    
    def generate_cover_letter(self, task, links):
        prompt_coverletter = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {task_description}

            ### INSTRUCTION:
            You are a competitive software engineer. You have experience in working with these {link_list}.
            Your job is to write a short cover letter(maximum 2 paragraphs and very personalized, not robotic) describing how you can contribute to the advancement of the company.
            Do not mention your experience in technologies outside the scope of these {link_list}. If none of these attributes are mentioned in the {task_description}, then just return a result saying this job is not applicable giving valid reason.
            Do not provide a preamble.
            ### COVER LETTER (NO PREAMBLE):
            
            """
        )

        chain_coverletter = prompt_coverletter | self.llm
        res = chain_coverletter.invoke({"task_description": str(task), "link_list": links})
        return res.content

# if __name__ == "__main__":
#     print(os.getenv("GROQ_API_KEY"))