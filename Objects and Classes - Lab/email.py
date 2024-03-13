class Email:

    def __init__(self, sender, receiver, content, sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.sent = sent

    def send(self):
        self.sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.sent}"


emails = []

while True:
    command = input()

    if command == "Stop":
        break

    sender, receiver, content = command.split()

    email = Email(sender, receiver, content)
    emails.append(email)

send_emails = [int(x) for x in input().split(", ")]

for x in send_emails:
    emails[x].send()

for mail in emails:
    print(mail.get_info())
