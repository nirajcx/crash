class Survey():
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_questions(self):
        print(self.question)

    def show_responses(self):
        print(self.responses)

    def store_responses(self, new_responses):
        self.responses.append(new_responses)

    def show_result(self):
        print("Printing responses")
        for i in self.responses:
            print(i, ' are the responses')
