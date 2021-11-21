from human_company import app
# import funcs


@app.route("/payments", methods=["GET"])
def get_payments():
    return funcs.get_payments()


@app.route("/payment/create", methods=["POST"])
def create_payment():
    return funcs.create_payment()