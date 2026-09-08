questions = [
    {
        "question": "What does 'HTTP' stand for?",
        "options": ["A) HyperText Transfer Protocol", "B) HighText Transfer Program", "C) HyperText Testing Process", "D) Hosted Text Transmission Protocol"],
        "answer": "A"
    },
    {
        "question": "Which port number is used by default for secure HTTPS traffic?",
        "options": ["A) 21", "B) 80", "C) 443", "D) 8080"],
        "answer": "C"
    },
    {
        "question": "Which device connects different networks together and routes traffic between them?",
        "options": ["A) Switch", "B) Router", "C) Hub", "D) Repeater"],
        "answer": "B"
    },
    {
        "question": "Which layer of the OSI model is responsible for IP addressing and routing?",
        "options": ["A) Transport Layer", "B) Data Link Layer", "C) Network Layer", "D) Application Layer"],
        "answer": "C"
    },
    {
        "question": "What is the main purpose of a DNS server?",
        "options": ["A) To block malicious websites", "B) To assign IP addresses automatically", "C) To translate domain names into IP addresses", "D) To encrypt web communication"],
        "answer": "C"
    }
]
score = 0
try:
    for item in questions:
        print(item["question"])
        for opt in item["options"]:
            print(opt)
        while True:
            try:
                user_ans = input("Your answer (A/B/C/D): ").strip().upper()
                if user_ans not in ["A", "B", "C", "D"]:
                    raise ValueError("Invalid choice! Please enter A, B, C, or D.")
                break  # Keçərli cavab verildikdə dövrədən çıxır
            except ValueError as e:
                print(f"Error: {e}\n")
        if user_ans == item["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer was {item['answer']}\n")
    print(f"Final Score: {score}/{len(questions)}")
except KeyboardInterrupt:
    print("\nQuiz interrupted by user. Goodbye!")
