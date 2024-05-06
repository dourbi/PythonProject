from rtanalysis.generate_testdata import create_session_files, get_filename_with_today_date


def test():
    create_session_files(
        num_sessions_per_day=100,
        total_days=2,
        original_amount=100.0,
        normalized_original_amount=90.0,
        original_currency_cd="USD",
        source_cd="source",
        party_key="key",
        account_key="account",
        transaction_type="type",
        payee_data_account_number="account_number",
        payee_name="name",
        payee_last_name="last_name",
        payee_address_line1="address",
        payee_state="state",
        payee_country_cd="country",
        routing_number="routing_number"
    )

def test1():
    get_filename_with_today_date()