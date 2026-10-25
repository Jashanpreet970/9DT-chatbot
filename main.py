import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download required NLTK datasets
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()

response = []
def process_text(user_input):
    """Normalizes, tokenizes, and lemmatizes user input."""
    lowered = user_input.lower()
    tokens = word_tokenize(lowered)
    return [lemmatizer.lemmatize(token) for token in tokens]

# Sollutions 
SOLUTIONS = {
    'power': [
        "Alright first lets try holding down the power button for 15 seconds to force a hard restart.",
        "Plug the device on charge with a working cable and plug,then wait 10 mins. Your device might have just ran out of battery",
        "Lastly, Check if the outlet has power, or try plugging into a different wall socket."
    ],
    'screen': [
        "Try adjusting the brightness settings or shine a flashlight at the screen to see if display content is visible.",
        "Connect the device to an external monitor or TV to test iclef it is a display hardware issue.",
        "Force restart the device using the physical button shortcut for your model."
    ],
    'not_charging': [
        "Clean out the charging port gently using a toothpick or compressed air to clear any dust or lint.",
        "Inspect your cable and charging port for any physical damage or bent pins",
        "Try using a different charging cable and adapter block."
        
    ],
    'battery_drain': [
        "Check your Battery Settings to see if a specific app is consuming high background power, and close or uninstall it.",
        "Lower your screen brightness, shorten auto-lock time, and turn on Low Power / Battery Saver mode.",
        "Disable location services, Bluetooth, and background app refresh for apps you aren't actively using."
    ],
    'general': [
        "Try restarting the device completely.",
        "Check for any pending software or system updates.",
        "Try closing all open applications and running a quick system cleanup."
    ]
}

print('Bot: Welcome to Tech support, I am here to help you fix any device issues.')
print("Type 'quit' or 'exit' at any point to stop the conversation.\n")

# Questions
while True:
    print("=" * 45)

    # STEP 1: Device Identification
    device_name = ""
    while True:
        device_input = input("\nBot: What kind of device are you having trouble with? (example: laptop, phone, tablet)\nYou: ")
        run = process_text(device_input)

        if any(w in run for w in ['quit', 'exit']):
            print("\nBot: Thanks for reaching out! Have a great day! Goodbye!")
            exit()

        if any(word in run for word in ['laptop', 'computer', 'pc', 'macbook', 'desktop']):
            print("\nBot: Got it, computer issues can definitely be annoying.")
            device_name = device_input.lower()
            break
        elif any(word in run for word in ['tablet', 'ipad', 'kindle']):
            print("\nBot: Got it, tablet support. Let's take a look.")
            device_name = device_input.lower()
            break
        elif any(word in run for word in ['phone', 'mobile', 'iphone', 'android']):
            print("\nBot: Alright, phone issues! Mobile fixes are usually pretty quick.")
            device_name = device_input.lower()
            break
        else:
            print("\nBot: Sorry, I didn't understand that. Could you please specify if it's a phone, laptop, or tablet?")

    # STEP 2: Issue Categorization
    print("\n" + "-" * 45)
    category = None

    while category is None:
        issue_input = input(f"\nBot: What seems to be the problem with your device? (e.g., screen broken, won't turn on, battery draining, not charging)\nYou: ")
        issue_run = process_text(issue_input)

        if any(w in issue_run for w in ['quit', 'exit']):
            print("\nBot: Thanks for using Tech Support! Have a great day! Goodbye!")
            exit()

        if any(word in issue_run for word in ['screen', 'display', 'cracked', 'broken']):
            category = 'screen'
        elif any(word in issue_run for word in ['power', 'turn', 'boot', 'dead', 'off']):
            category = 'power'
        elif any(word in issue_run for word in ['drain', 'draining', 'dying', 'fast', 'quick', 'percentage']):
            category = 'battery_drain'
        elif any(word in issue_run for word in ['charge', 'charging', 'plug', 'plugged', 'cable']):
            category = 'not_charging'
        else:
            print("\nBot: Sorry, I didn't understand that. Could you please describe the problem using terms like 'screen', 'power', 'battery draining', or 'not charging'.")

    # STEP 3: Sequential Troubleshooting Loop
    solution_list = SOLUTIONS[category]
    solution_index = 0
    problem_solved = False

    while solution_index < len(solution_list):
        print(f"\nBot: Option {solution_index + 1}: {solution_list[solution_index]}")

        while True:
            feedback = input("\nBot: Did that solve your problem? (yes/no)\nYou: ")
            feedback_run = process_text(feedback)

            if any(w in feedback_run for w in ['quit', 'exit']):
                print("\nBot: Thanks for using Tech Support! Goodbye!")
                exit()

            if any(word in feedback_run for word in ['yes', 'y', 'yeah', 'yep', 'fixed', 'worked', 'good']):
                print("\nBot: Awesome! Glad we could get that sorted out.")
                problem_solved = True
                break
            elif any(word in feedback_run for word in ["no", "n", "nope", "nah", "not", "didn't"]):
                print("\nBot: Sorry to hear that didn't work. Let's try the next step.")
                solution_index += 1
                break
            else:
                print("\nBot: Sorry, I didn't quite catch that. Please respond with a simple 'yes' or 'no'.")

        if problem_solved:
            break

    # Suggested Solutions don't work
    if not problem_solved:
        print("\nBot: If it still doesn't work, I recommend taking your device to an authorized technician or contacting manufacturer support.")

    # STEP 4: Session Continuation Check
    print("\n" + "-" * 45)
    should_restart = False

    while True:
        again = input("\nBot: Do you need help with anything else? (yes/no)\nYou: ")
        again_run = process_text(again)

        if any(w in again_run for w in ['quit', 'exit']):
            break
        elif any(word in again_run for word in ['yes','y' ,'yeah', 'yep', 'sure', 'ok']):
            should_restart = True
            break
        elif any(word in again_run for word in ['no', 'nope', 'nah', 'not']):
            break
        else:
            print("\nBot: Sorry, I didn't catch that. Do you need help with another problem? (yes/no)")

    if not should_restart:
        print("\nBot: Thanks for using Tech Support! Have a great day! Goodbye!")
        break