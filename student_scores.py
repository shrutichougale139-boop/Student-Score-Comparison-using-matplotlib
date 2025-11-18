import matplotlib.pyplot as plt

def get_scores():
    subjects = []
    marks = []

    n = int(input("How many subjects? "))

    for i in range(n):
        sub = input(f"Enter subject {i+1} name: ")  # FIXED (no int())
        mark = float(input(f"Enter marks for {sub}: "))
        subjects.append(sub)
        marks.append(mark)

    return subjects, marks


def plot_scores(subjects, marks):
    plt.figure(figsize=(10, 6))

    combined = list(zip(subjects, marks))
    combined.sort(key=lambda x: x[1], reverse=True)
    subjects, marks = zip(*combined)

    plt.bar(subjects, marks)
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Student Score Comparison")
    plt.ylim(0, max(marks) + 10)

    for i, mark in enumerate(marks):
        plt.text(i, mark + 1, str(mark), ha='center')

    mean_score = sum(marks) / len(marks)
    plt.axhline(mean_score, linestyle='--')
    plt.text(len(subjects)-1, mean_score + 2, f"Mean: {mean_score:.2f}")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    subjects, marks = get_scores()
    plot_scores(subjects, marks)
