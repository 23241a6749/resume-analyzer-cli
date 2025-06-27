# 📄 Resume Analyzer CLI  
A command-line Python tool that analyzes PDF resumes for key skill mentions and suggests improvements based on missing keywords.  
## 🚀 Features  
- Extracts text from `.pdf` resumes using PyMuPDF  
- Scans for important tech skills (like Python, SQL, ML, etc.)  
- Displays skill counts in a table  
- Suggests missing or underrepresented skills  
- Colorful output using Rich CLI library  
## 🛠 Installation  
Make sure you have Python 3.7+ installed. Install required libraries:  
```bash
pip install pymupdf rich
```  
## ⚙️ Usage  
Clone this repository:  
```bash
git clone https://github.com/sai-mohaneesh/resume-analyzer-cli.git  
cd resume-analyzer-cli
```  
Run the tool:  
```bash
python analyzer.py
```  
Enter the path to your PDF resume when prompted:  
```bash
Enter path to your resume PDF: D:/resumes/my_resume.pdf
```  
## 🧠 Example Output  
```text
Enter path to your resume PDF: D:/resumes/my_resume.pdf  
[Extracted Resume Text]  
Sai Mohaneesh Neela  
Hyderabad, Telangana, India  
...  
Resume Skill Analysis  
┌──────────────────────────┬───────┐  
│ Skill                   │ Count │  
├──────────────────────────┼───────┤  
│ Python                  │ 3     │  
│ SQL                     │ 1     │  
│ TensorFlow              │ 0     │  
│ ...                     │ ...   │  
└──────────────────────────┴───────┘  
Suggestions: Consider adding these skills if relevant:  
- TensorFlow  
- AWS  
- Tableau  
```  

## 📁 File Structure  
```text
resume-analyzer-cli/  
├── analyzer.py  
├── README.md  
├── screenshot.png  
└── sample_resume.pdf  
```  
## 👨‍💻 Author  
**Sai Mohaneesh Neela**  
[LinkedIn](https://www.linkedin.com/in/sai-mohaneesh-neela-423476289)  
## 📄 License  
MIT License
