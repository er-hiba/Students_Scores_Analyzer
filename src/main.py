import tkinter as tk
from tkinter import *
import statistics
import matplotlib.pyplot as plt

class StudentScoresApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Scores Analyzer")

        # Frame to hold the main elements
        self.main_frame = Frame(root)
        self.main_frame.pack()

        # Labels and Text Entry for user input
        self.info_label = Label(self.main_frame, text="Enter the scores separated by a space:", font=("Courier", 12))
        self.info_label.grid(row=0, column=0, padx=10, pady=10)

        self.scores_entry = tk.Text(self.main_frame, width=50, height=10)
        self.scores_entry.grid(row=1, column=0, padx=10, pady=10)

        # Button to submit scores for analysis
        self.submit_button = Button(self.main_frame, text="Submit", command=self.analyze_scores)
        self.submit_button.grid(row=2, column=0, pady=10)

        # Label and Text widget to display analysis results
        self.result_label = Label(self.main_frame, text="Results:", font=("Courier", 12))
        self.result_label.grid(row=3, column=0, pady=10)

        self.result_text = Text(self.main_frame, height=20, width=50)
        self.result_text.grid(row=4, rowspan=2, column=0, padx=10, pady=10)
        self.result_text.config(font=("Courier", 12))

        # Frame to hold the plot
        self.plot_frame = Frame(self.main_frame)
        self.plot_frame.grid(row=5, column=1, pady=10)

    def analyze_scores(self):
        # Retrieve scores inputted by the user
        scores_input = self.scores_entry.get("1.0", tk.END).strip()
        if not scores_input:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, "No scores provided.")
            for widget in self.plot_frame.winfo_children():
                widget.destroy()
            return

        # Convert input string to a list of scores and perform analysis
        scores_list = list(map(float, scores_input.split()))
        scores_list.sort()

        # Generate analysis results
        result = "- The scores in ascending order: \n"+" ".join([str(score) for score in scores_list])
        result += f"\n\n- The average (mean): {statistics.mean(scores_list)}\n"
        result += f"- The median: {statistics.median(scores_list)}\n"
        result += f"- The standard deviation: {statistics.stdev(scores_list)}\n"
        result += f"- The minimum: {min(scores_list)}\n"
        result += f"- The maximum: {max(scores_list)}\n"
        result += f"- The range: {max(scores_list) - min(scores_list)}\n"
        result += "\n- The scores above average: " + " ".join([str(score) for score in scores_list if score > statistics.mean(scores_list)])

        # Display analysis results in the text widget
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)

        # Generate and display the plot
        self.plot_scores(scores_list)

    def plot_scores(self, scores):
        # Create a figure and axis
        plt.figure(figsize=(4, 4))
        plt.xlabel("Students")
        plt.ylabel("Scores")
        plt.title("Students Scores")

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

        # Add legend, grid, and adjust layout
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Save the plot as an image and display it in the Tkinter window
        plt.savefig("student_scores.png")

        img = tk.PhotoImage(file="student_scores.png")
        img_label = tk.Label(self.plot_frame, image=img)
        img_label.photo = img
        img_label.grid(row=2, column=0, pady=10)


def main():
    # Create the Tkinter root window and start the application
    root = tk.Tk()
    app = StudentScoresApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
