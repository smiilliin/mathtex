class Problem:
    def __init__(self, prompt, choices, width_count=3):
        self.prompt = prompt
        self.choices = choices
        self.width_count = width_count

    def get_tex(self, number):
        result = (
            f"\\noindent\n\\begin{{minipage}}{{\\linewidth}}\n{number}. {self.prompt}"
            + f"\\begin{{tasks}}[label=\\textcircled{{\\scriptsize\\arabic*}},label-width=13pt]({self.width_count})"
        )
        for choice in self.choices:
            result += f"\\task {choice}"
        result += "\\end{tasks}\n\\end{minipage}"
        return result


class MathTex:
    def __init__(self, title, author, answer_key_title="Answer Key"):
        self.title = title
        self.author = author
        self.packages = ["tasks", "kotex", "datetime2", "multicol", "amsmath"]
        self.problems = []
        self.answer_key_title = answer_key_title
        self.answer_keys = []

    def add_package(self, package):
        if isinstance(package, list):
            self.packages.extend(package)
        else:
            self.packages.append(package)

    def add_problem(self, problem):
        self.problems.append(problem)

    def add_answer_key(self, answer_key):
        if isinstance(answer_key, list):
            self.answer_keys.extend(answer_key)
        else:
            self.answer_keys.append(answer_key)

    def write(self, path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("\\documentclass{article}\n")
            for package in self.packages:
                f.write(f"\\usepackage{{{package}}}\n")
            f.write(f"\\usepackage[a4paper, margin=1in]{{geometry}}\n")
            f.write(
                f"\\title{{{self.title}}}\n\\author{{{self.author}}}\n\\date{{\\today}}"
            )
            f.write("\\begin{document}\n\\maketitle")
            f.write("\\begin{multicols*}{2}\n")
            for i, problem in enumerate(self.problems):
                f.write(problem.get_tex(str(i + 1)) + "\n")
                f.write("\\bigskip\n\n")
            f.write("\\newpage\n" + f"\\section*{{{self.answer_key_title}}}\n")

            for i, key in enumerate(self.answer_keys):
                if i % 5 == 0:
                    if i != 0:
                        f.write("\n\\end{minipage}\n\n")
                    f.write("\\noindent\\begin{minipage}{\\linewidth}\n\n")
                    f.write(f"{i+1}. ")
                f.write(f"\\textcircled{{{key}}} ")
            f.write("\n\n\\end{minipage}")

            f.write("\\end{multicols*}\n")
            f.write("\\end{document}")
