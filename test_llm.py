
from src.llm_classifier import analyze_message

messages = {
    "English": "Your bank account will be blocked. Update KYC immediately.",

    "Hindi": "आपका बैंक खाता बंद हो जाएगा। तुरंत केवाईसी अपडेट करें।",

    "Hinglish": "Aapka bank account block ho jayega. Jaldi KYC update karo.",

    "Normal": "Hey, are we meeting at college tomorrow?"
}

for language, message in messages.items():

    print("\n" + "=" * 60)
    print(f"LANGUAGE: {language}")
    print(f"MESSAGE: {message}")
    print("=" * 60)

    try:
        result = analyze_message(message)

        print(f"VERDICT: {result.verdict}")
        print(f"SCAM TYPE: {result.scam_type}")

        print("\nRED FLAGS:")
        if result.red_flags:
            for flag in result.red_flags:
                print(f" - {flag}")
        else:
            print(" None")

        print(f"\nEXPLANATION: {result.explanation}")
        print(f"RECOMMENDED ACTION: {result.recommended_action}")

    except Exception as error:
        print(f"ERROR: {type(error).__name__}: {error}")
