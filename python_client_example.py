try:
    import secrets
except ImportError:  # Python < 3.6
    import random as secrets

from ihela_client.merchant_client import MerchantClient

if __name__ == "__main__":
    # client_id = "4sS7OWlf8pqm04j1ZDtvUrEVSZjlLwtfGUMs2XWZ"
    # client_id = "12CMmsS2e3aqONxYHCSpHaG3p7VWls9vtczbNk1b"

    client_id = "Dh7vlEWXVn25Gu1Jhr1OEM2URqeI5Y7Ua0bePRY6"
    # client_id = "KziHxNoydAhWV2uVSfimZf7ApMY1tdjW9vYXfGwk"
    # client_secret = "HN7osYwSJuEOO4MEth6iNlBS8oHm7LBhC8fejkZkqDJUrvVQodKtO55bMr845kmplSlfK3nxFcEk2ryiXzs1UW1YfVP5Ed6Yw0RR6QmnwsQ7iNJfzTgeehZ2XM9mmhC3"  # noqa
    # client_secret = "duwbLBiKPoJTytFnMcAbP8QxmaAJPboNQHslRpqgCsSplNo5Es4tBFDJl2Iae0WAErpP4QcQ0iUGpxkoFdFXnOeGDMvtX5JLVyrlvRE6DfScBagKExHdmugWwDstFHgP"  # noqa
    # client_secret = "LjATwjOk70mGVdkyGZNxRih0FLe4lfF2UEgHAGAF7ovK38jQQ9dBdd1SSmWoXZl44wee0bFamQQclq1sQFUBL6XBsGqjRV8DR8isa2GEVNNMroLWiB1K5ZZf3H9UoCyt" # noqa
    client_secret = "RqdOuijrmLaUnkkqVKpQm1G5N2FINsMeRg8kdpO7MXiJ07jk7N15HHvcJlluGIpxgrOH6jJuYgBeJCyP7y8KgZZCtDtKVKePfShEfq5rfGxxfyYvbKLkmKno7QWMg04T"  # noqa

    cl = MerchantClient(
        client_id,
        client_secret,
        pin_code="4321",
        ihela_url="http://10.30.0.7/",
    )
    # )  # , ihela_url="http://127.0.0.1:8080/")
    print("\nPING IHELA : ", cl.ihela_base_url)
    ping = cl.ping()
    print("PING DATA : ", ping)

    # banks = cl.get_bank_list(list_type="cashout")

    # print("\nBANKS LIST : ", banks)

    merchant_reference = str(secrets.token_hex(10))
    bill = cl.init_bill(
        # 2000,
        # # "76077736",
        # "pierreclaverkoko@gmail.com",
        # "My description",
        # str(secrets.token_hex(10)),
        # # bank="MOB-0003"
        debit_bank="MF1-0001",
        debit_account="0000000016-01",
        amount="500",
        description="test bill creation",
        merchant_description="user test bill creation",
        merchant_reference=merchant_reference,
        pin_code="4321",
    )
    print("\n BILL CREATION : ", bill)

    bill_verif = cl.verify_bill(
        code=bill.get("response_data", None).get("code", None),
        reference=merchant_reference,
        pin="4321",
    )
    print("\n BILL VERIFICATION: ", bill_verif)

    # a = bill.get("merchant_reference", None)
    # if a is not None:
    #     bill_verif = cl.verify_bill(
    #         code=bill.get("response_data", None).get("reference", None),
    #         reference=bill.get("merchant_reference", pin="4321"),
    #     )

    #     print("\n BILL VERIFICATION: ", bill_verif)

    client = cl.customer_lookup("MF1-0001", "000016-01")

    print("\nCUSTOMER LOOKUP : ", client)

    cashin = cl.cashin_client(
        bank_slug="MF1-0001",
        account="000016-01",
        account_holder="Pierre Claver Koko",
        amount="2000",
        merchant_reference="jklop09",
        description="Cashin description",
    )

    print("\nCASHIN TO CLIENT : ", cashin)

    # init_bill = cl.init_bill(
    #     debit_bank="MF1-0001",
    #     debit_account="0000000016-01",
    #     amount=600,
    #     description="Payment merchant",
    #     merchant_description="Payment from client 001 752000",
    #     merchant_reference="752000",
    #     redirect_uri="https=//myredirecturi.com/payments",
    #     payment_product_id="",
    #     pin_code="1234",
    # )

    # print("\nBILL : ", init_bill)

    # bill = cl.verify_bill(code="CODE-20230321-9E29QH1", pin="1234", reference="752000")

    # print("\nBILL : ", bill)
