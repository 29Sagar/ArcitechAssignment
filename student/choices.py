from djchoices import ChoiceItem, DjangoChoices

class StatusChoices(DjangoChoices):
    PENDING = ChoiceItem("pending","PENDING")
    COMPLETED = ChoiceItem("completed","COMPLETED")