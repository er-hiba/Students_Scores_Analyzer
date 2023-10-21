class StudentScoresAnalyzer:
    def __init__(self):
        self.scores = []
    
    def input_scores(self, userInput=0):
        if userInput != 0:
            n = userInput
        else:
            n = int(input("Enter the number of students: "))
        for i in range(n):
            score = float(input(f"Enter the score of student {i + 1}: "))
            self.scores.append(score)
    
    def calculate_average(self):
        return sum(self.scores) / len(self.scores)
    
    def calculate_median(self):
        self.scores.sort()
        n = len(self.scores)
        if n % 2 == 0:
            median = (self.scores[n // 2] + self.scores[n // 2 - 1]) / 2
        else:
            median = self.scores[n // 2]
        return median
    
    def calculate_standard_deviation(self):
        average = self.calculate_average()
        n = len(self.scores)
        squared_diff = [(x - average) ** 2 for x in self.scores]
        variance = sum(squared_diff) / n
        std_dev = variance ** 0.5
        return std_dev
    
    def calculate_range(self):
        return max(self.scores) - min(self.scores)
    
    def scores_above_average(self):
        average = self.calculate_average()
        above_average = [score for score in self.scores if score > average]
        above_average.sort()
        return above_average

if __name__ == "__main__":
    analyzer = StudentScoresAnalyzer()
    analyzer.input_scores()

    print("The scores in ascending order:", sorted(analyzer.scores))
    print("The average (mean):", analyzer.calculate_average())
    print("The median:", analyzer.calculate_median())
    print("The standard deviation:", analyzer.calculate_standard_deviation())
    print("The minimum:", min(analyzer.scores))
    print("The maximum:", max(analyzer.scores))
    print("The range:", analyzer.calculate_range())
    print("The scores above average:", analyzer.scores_above_average())
