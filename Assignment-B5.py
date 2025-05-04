def get_bot_response(user_input):
    user_input = user_input.lower()
    responses = {
        "courses": (
            "We offer various courses:\n"
            "- Engineering\n- Pharma\n- Management\n- C-DAC\n- MCA\n"
            "Visit our website for more details."
        ),
        "fees": (
            "Fees vary by course. Visit our website or contact admissions for details."
        ),
        "faculty": "We have experienced and highly qualified faculty members.",
        "features": (
            "Our courses offer practical skills, hands-on projects, and expert guidance."
        ),
        "contact": "For assistance, please contact us via our website."
    }
    for keyword, reply in responses.items():
        if keyword in user_input:
            return reply
    return "Sorry, I didn't understand. Could you rephrase your question?"
def main():
    print("----Welcome to MET-BKC----")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        print("Chatbot:", get_bot_response(user_input))
if __name__ == "__main__":
    main()
