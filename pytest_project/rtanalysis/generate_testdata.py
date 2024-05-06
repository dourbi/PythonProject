from datetime import datetime, timedelta

import os


def create_session_files(num_sessions_per_day, total_days, **kwargs):
    # Create a directory to store session files
    directory = "session_files"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Get today's date
    today = datetime.now().date()

    # Iterate over each day
    for i in range(total_days):
        date = today - timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')

        # Create a subdirectory for each day
        day_directory = os.path.join(directory, date_str)
        if not os.path.exists(day_directory):
            os.makedirs(day_directory)

        # Calculate number of sessions for the day
        num_sessions = num_sessions_per_day if i == 0 else 1

        # Create session files
        for i in range(total_days):
            date = today - timedelta(days=i)
            date_str = date.strftime('%Y-%m-%d')

            # Create a subdirectory for each day
            day_directory = os.path.join(directory, date_str)
            if not os.path.exists(day_directory):
                os.makedirs(day_directory)

            # Calculate number of sessions for the day
            num_sessions = num_sessions_per_day if i == 0 else 1

            # Create session files
            for j in range(num_sessions):
                filename = f"session_{j + 1}.log"
                filepath = os.path.join(day_directory, filename)

                # Generate wire payment data
                wire_payment_data = generate_wire_payment_data(**kwargs)

                # Write wire payment data to session log file
                with open(filepath, 'w') as f:
                    f.write(str(wire_payment_data))
def get_filename_with_today_date():
    """
    Generate a filename with the current timestamp in the format 'wire_payment_data_YYYY-MM-DD.log'.
    """
    today = datetime.now()
    print(f"wire_payment_data_{today.strftime('%Y-%m-%d')}.log")
    return f"wire_payment_data_{today.strftime('%Y-%m-%d')}.log"


def generate_wire_payment_data(
        original_amount: float,
        normalized_original_amount: float,
        original_currency_cd: str,
        source_cd: str,
        party_key: str,
        account_key: str,
        transaction_type: str,
        payee_data_account_number: str,
        payee_name: str,
        payee_last_name: str,
        payee_address_line1: str,
        payee_state: str,
        payee_country_cd: str,
        routing_number: str,
        is_add_edit_payee: bool = False,
        payment_speed_cd: str = "0",
        is_standing_order: bool = True,
        originator_to_beneficiary_info: str = ""
) -> dict:
    amount_data = amount_dict(original_amount, normalized_original_amount, original_currency_cd)
    return {
        "amount": amount_data,
        "baseTransactionA": {
            "channel": "OFFLINE",
            "sourceCd": source_cd,
            "transactionNormalizedDateTime": "2023-04-01T00:16:27.000Z",
            "transactionLocalDateTime": "2023-04-01T00:16:27.000Z",
            "resendDueToFailureInd": True,
            "partyKey": party_key
        },
        "baseTransactionB": {
            "accountKey": account_key
        },
        "baseTransactionC": {
            "transactionKey": "2023040130035",
            "transactionType": transaction_type
        },
        "monetaryTransactionB": {
            "transactionId": "2023040130035",
            "payeeDataAccountNumber": payee_data_account_number,
            "fundsDirectionCd": "O"
        },
        "partyReference": {
            "partyType": "Organization"
        },
        "title": "detectionRequestWire",
        "transferTransaction": {
            "isAddEditPayee": is_add_edit_payee,
            "paymentSpeedCd": payment_speed_cd,
            "executionDate": "2023-04-01T00:16:27.000Z",
            "isStandingOrder": is_standing_order
        },
        "trxMonitoredAccountData": {
            "accountNumber": "590325426"
        },
        "trxPayeeAccountData": {
            "routingNumber": routing_number,
            "accountNumber": payee_data_account_number,
            "routingType": "BIC"
        },
        "trxPayeePartyData": {
            "name": payee_name,
            "lastName": payee_last_name,
            "addressData": {
                "addressLine1": payee_address_line1,
                "state": payee_state,
                "countryCd": payee_country_cd
            }
        },
        "wirePayee": {
            "wirePayeeAddress": "56466 Yan Rapids",
            "originatorToBeneficiaryInfo": originator_to_beneficiary_info
        }
    }


def amount_dict(original_amount: float, normalized_original_amount: float, original_currency_cd: str):
    return {
        'originalAmount': original_amount,
        'normalizedOriginalAmount': normalized_original_amount,
        'originalCurrencyCd': original_currency_cd
    }


def source_cd(source_cd: str):
    return {'source_cd': source_cd}


def party_key(party_key: str):
    return {'party_key': party_key}


def account_key(account_key: str):
    return {'account_key': account_key}


def transaction_type(transaction_type: str):
    return {'transaction_type': transaction_type}


def payee_data_account_number(payee_data_account_number: str):
    return {'payee_data_account_number': payee_data_account_number}


def payee_name(payee_name: str):
    return {'payee_name': payee_name}


def payee_last_name(payee_last_name: str):
    return {'payee_last_name': payee_last_name}


def payee_address_line1(payee_address_line1: str):
    return {'payee_address_line1': payee_address_line1}


def payee_state(payee_state: str):
    return {'payee_state': payee_state}


def routing_number(routing_number: str):
    return {'routing_number': routing_number}


def create_add_edit_payee_dict(is_add_edit_payee: bool = False):
    return {'is_add_edit_payee': is_add_edit_payee}


def payment_speed_cd(payment_speed_cd: str = "0"):
    return {'payment_speed_cd': payment_speed_cd}


def is_standing_order(is_standing_order: bool = True):
    return {'is_standing_order': is_standing_order}


def originator_to_beneficiary_dict(originator_to_beneficiary_info: str = ""):
    return {'originator_to_beneficiary_info': originator_to_beneficiary_info}


