# Cover Letter Generation Tool

Cover letter generator for job applicants using groq, langchain and streamlit. It allows users to input the URL of a job's detail page. The tool then extracts job requirements from that page and generates a personalized cover letter. This letter includes relevant skills sourced from a vector database, based on the descriptions of the user's previous experiences using these skills.

## Set-up

1. To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside `app/.env` update the value of `GROQ_API_KEY` with the API_KEY you created.

2. (Optional) You can create a virtual environment to install the dependencies required in the exact versions

3. To get started, first install the dependencies using:
   ```commandline
    pip install -r requirements.txt
   ```
4. Run the streamlit app:
   ```commandline
   streamlit run app/main.py
   ```

Copyright (C) Codebasics Inc. All rights reserved.

**Additional Terms:**
This software is licensed under the MIT License. However, commercial use of this software is strictly prohibited without prior written permission from the author. Attribution must be given in all copies or substantial portions of the software.
