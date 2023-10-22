import tkinter as tk
from tkinter import ttk
import statistics
import matplotlib.pyplot as plt

class StudentScoresApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Scores Analyzer")

        self.info_label = tk.Label(root, text="Enter the scores separated by spaces:")
        self.info_label.pack()

        self.scores_entry = tk.Entry(root)
        self.scores_entry.pack()

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_scores)
        self.calculate_button.pack()

        self.result_frame = ttk.Frame(root)
        self.result_frame.pack()

        self.result_text = tk.Text(self.result_frame, height=10, width=50)
        self.result_text.pack(side=tk.LEFT)

        self.plot_frame = ttk.Frame(self.result_frame)
        self.plot_frame.pack(side=tk.LEFT)

    def calculate_scores(self):
        scores_input = self.scores_entry.get()
        scores = [float(score) for score in scores_input.split()]

        if not scores:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, "No scores provided.")
            return

        scores.sort()  # Sort the scores in ascending order

        result = f"The scores in ascending order: {scores}\n"
        result += f"The average (mean): {statistics.mean(scores)}\n"
        result += f"The median: {statistics.median(scores)}\n"
        result += f"The standard deviation: {statistics.stdev(scores)}\n"
        result += f"The minimum: {min(scores)}\n"  # Use min() to calculate the minimum
        result += f"The maximum: {max(scores)}\n"
        result += f"The range: {max(scores) - min(scores)}\n"
        result += "The scores above average: " + " ".join([str(score) for score in scores if score > statistics.mean(scores)])

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)

        self.plot_scores(scores)

    def plot_scores(self, scores):
        # Create a figure and axis
        plt.figure(figsize=(8, 6))
        plt.xlabel("Student")
        plt.ylabel("Score")
        plt.title("Student Scores")

        # Use integers as student numbers
        students = list(range(1, len(scores) + 1))

        # Plot the scores as a line with a unique color
        plt.plot(students, scores, label="Scores", color='blue')

        # Define a list of colors for statistics lines
        colors = ['red', 'green', 'orange', 'purple', 'pink']

        # Calculate and plot other statistics as horizontal lines
        for i, statistic_name in enumerate(["mean", "median", "stdev"]):
            statistic_value = getattr(statistics, statistic_name)(scores)
            plt.axhline(statistic_value, linestyle='--', label=f"{statistic_name.capitalize()}", color=colors[i], alpha=0.7)

        # Calculate and plot the minimum and maximum
        min_value = min(scores)
        max_value = max(scores)
        plt.axhline(min_value, linestyle='--', label="Min", color=colors[len(colors) - 2], alpha=0.7)
        plt.axhline(max_value, linestyle='--', label="Max", color=colors[len(colors) - 1], alpha=0.7)

        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        plt.savefig("student_scores.png")

        img = tk.PhotoImage(file="student_scores.png")
        img_label = tk.Label(self.plot_frame, image=img)
        img_label.photo = img
        img_label.pack()

def main():
    root = tk.Tk()
    app = StudentScoresApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
