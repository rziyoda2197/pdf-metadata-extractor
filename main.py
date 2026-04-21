class TelegramBot:
    def __init__(self):
        self.messages = []

    def send_message(self, user_id, message):
        self.messages.append((user_id, message))

    def get_messages(self):
        return self.messages

class BotSimulator:
    def __init__(self):
        self.bot = TelegramBot()

    def start(self):
        while True:
            user_input = input("Botga yozing: ")
            if user_input.lower() == "quit":
                break
            user_id = input("Foydalanuvchi ID: ")
            self.bot.send_message(user_id, user_input)

    def get_bot_messages(self):
        return self.bot.get_messages()

def main():
    simulator = BotSimulator()
    simulator.start()
    print("Botga yuborilgan xabarlar:")
    for message in simulator.get_bot_messages():
        print(f"Foydalanuvchi ID: {message[0]}, Xabar: {message[1]}")

if __name__ == "__main__":
    main()
