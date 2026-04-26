class VatCalc:
    @staticmethod
    def calculate_vat(amount, rate, mode):
        if amount is None:
            return None
        if mode == "add":
            return round(amount * (1 + rate / 100), 9)
        elif mode == "remove":
            return round(amount / (1 + rate / 100), 9)
        else:
            return "Invalid operation!"
