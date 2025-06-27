import fitz  # PyMuPDF
from rich.table import Table
from rich.console import Console

console = Console()

# Define the skills to search for
KEYWORDS = [
    "Python", "Java", "C", "C++", "JavaScript", "SQL", "HTML", "CSS", "Django",
    "Flask", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
    "Pandas", "NumPy", "Scikit-learn", "Keras", "AWS", "Azure", "GCP", "Git",
    "Tableau", "Power BI", "React", "Node.js"
]

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to count keyword mentions
def count_keywords(text, keywords):
    text_lower = text.lower()
    counts = {}
    for keyword in keywords:
        count = text_lower.count(keyword.lower())
        counts[keyword] = count
    return counts

# Function to print results using Rich
def display_results(counts):
    table = Table(title="Resume Skill Analysis")
    table.add_column("Skill", style="cyan", justify="left")
    table.add_column("Count", style="magenta", justify="center")

    missing = []

    for skill, count in counts.items():
        table.add_row(skill, str(count))
        if count == 0:
            missing.append(skill)

    console.print(table)

    if missing:
        console.print("\n[bold yellow]Suggestions: Consider adding these skills if relevant:[/bold yellow]")
        for skill in missing:
            console.print(f"- {skill}", style="green")

# Main CLI logic
if __name__ == "__main__":
    path = input("Enter path to your resume PDF: ").strip()
    try:
        resume_text = extract_text_from_pdf(path)
        if not resume_text.strip():
            console.print("[red]No text extracted. Please make sure the PDF is not scanned or image-based.[/red]")
        else:
            counts = count_keywords(resume_text, KEYWORDS)
            display_results(counts)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
