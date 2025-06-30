# Gamertags

Methods:

- <code title="post /v0/gamertag/charges">client.gamertags.<a href="./src/zbdpay/resources/gamertags.py">create_charge</a>(\*\*<a href="src/zbdpay/types/gamertag_create_charge_params.py">params</a>) -> None</code>
- <code title="get /v0/user-id/gamertag/{gamertag}">client.gamertags.<a href="./src/zbdpay/resources/gamertags.py">retrieve_by_gamertag</a>(gamertag) -> None</code>
- <code title="get /v0/gamertag/user-id/{id}">client.gamertags.<a href="./src/zbdpay/resources/gamertags.py">retrieve_by_zbd_id</a>(id) -> None</code>
- <code title="get /v0/gamertag/transaction/{id}">client.gamertags.<a href="./src/zbdpay/resources/gamertags.py">retrieve_payment</a>(id) -> None</code>
- <code title="post /v0/gamertag/send-payment">client.gamertags.<a href="./src/zbdpay/resources/gamertags.py">send_payment</a>(\*\*<a href="src/zbdpay/types/gamertag_send_payment_params.py">params</a>) -> None</code>

# LightningCharges

Methods:

- <code title="post /v0/charges">client.lightning_charges.<a href="./src/zbdpay/resources/lightning_charges.py">create</a>(\*\*<a href="src/zbdpay/types/lightning_charge_create_params.py">params</a>) -> None</code>
- <code title="get /v0/charges/{id}">client.lightning_charges.<a href="./src/zbdpay/resources/lightning_charges.py">retrieve</a>(id) -> None</code>

# InternalTransfer

Methods:

- <code title="post /v0/internal-transfer">client.internal_transfer.<a href="./src/zbdpay/resources/internal_transfer.py">initiate</a>(\*\*<a href="src/zbdpay/types/internal_transfer_initiate_params.py">params</a>) -> None</code>

# LightningAddress

Methods:

- <code title="post /v0/ln-address/fetch-charge">client.lightning_address.<a href="./src/zbdpay/resources/lightning_address.py">create_charge</a>(\*\*<a href="src/zbdpay/types/lightning_address_create_charge_params.py">params</a>) -> None</code>
- <code title="post /v0/ln-address/send-payment">client.lightning_address.<a href="./src/zbdpay/resources/lightning_address.py">send_payment</a>(\*\*<a href="src/zbdpay/types/lightning_address_send_payment_params.py">params</a>) -> None</code>
- <code title="get /v0/ln-address/validate/{address}">client.lightning_address.<a href="./src/zbdpay/resources/lightning_address.py">validate</a>(address) -> None</code>

# LightningStaticCharges

Methods:

- <code title="post /v0/static-charges">client.lightning_static_charges.<a href="./src/zbdpay/resources/lightning_static_charges.py">create</a>(\*\*<a href="src/zbdpay/types/lightning_static_charge_create_params.py">params</a>) -> None</code>
- <code title="get /v0/static-charges/{id}">client.lightning_static_charges.<a href="./src/zbdpay/resources/lightning_static_charges.py">retrieve</a>(id) -> None</code>
- <code title="patch /v0/static-charges/{id}">client.lightning_static_charges.<a href="./src/zbdpay/resources/lightning_static_charges.py">update</a>(id, \*\*<a href="src/zbdpay/types/lightning_static_charge_update_params.py">params</a>) -> None</code>

# Vouchers

Methods:

- <code title="post /v1/create-voucher">client.vouchers.<a href="./src/zbdpay/resources/vouchers.py">create</a>(\*\*<a href="src/zbdpay/types/voucher_create_params.py">params</a>) -> None</code>
- <code title="get /v0/vouchers/{id}">client.vouchers.<a href="./src/zbdpay/resources/vouchers.py">retrieve</a>(id) -> None</code>
- <code title="post /v0/redeem-voucher">client.vouchers.<a href="./src/zbdpay/resources/vouchers.py">redeem</a>(\*\*<a href="src/zbdpay/types/voucher_redeem_params.py">params</a>) -> None</code>
- <code title="post /v0/revoke-voucher">client.vouchers.<a href="./src/zbdpay/resources/vouchers.py">revoke</a>(\*\*<a href="src/zbdpay/types/voucher_revoke_params.py">params</a>) -> None</code>

# WithdrawalRequests

Methods:

- <code title="post /v0/withdrawal-requests">client.withdrawal_requests.<a href="./src/zbdpay/resources/withdrawal_requests.py">create</a>(\*\*<a href="src/zbdpay/types/withdrawal_request_create_params.py">params</a>) -> None</code>
- <code title="get /v0/withdrawal-requests/{id}">client.withdrawal_requests.<a href="./src/zbdpay/resources/withdrawal_requests.py">retrieve</a>(id) -> None</code>

# LightningPayments

Methods:

- <code title="get /v0/payments/{id}">client.lightning_payments.<a href="./src/zbdpay/resources/lightning_payments.py">retrieve</a>(id) -> None</code>
- <code title="post /v0/payments">client.lightning_payments.<a href="./src/zbdpay/resources/lightning_payments.py">send</a>(\*\*<a href="src/zbdpay/types/lightning_payment_send_params.py">params</a>) -> None</code>

# Wallet

Methods:

- <code title="get /v0/wallet">client.wallet.<a href="./src/zbdpay/resources/wallet.py">retrieve_balance</a>() -> None</code>

# Utils

Methods:

- <code title="get /v0/is-supported-region/{ip}">client.utils.<a href="./src/zbdpay/resources/utils.py">check_ip_support</a>(ip) -> None</code>
- <code title="post /v0/decode-invoice">client.utils.<a href="./src/zbdpay/resources/utils.py">decode_lightning_charge</a>(\*\*<a href="src/zbdpay/types/util_decode_lightning_charge_params.py">params</a>) -> None</code>
- <code title="get /v0/prod-ips">client.utils.<a href="./src/zbdpay/resources/utils.py">list_prod_ips</a>() -> None</code>
- <code title="get /v0/btcusd">client.utils.<a href="./src/zbdpay/resources/utils.py">retrieve_btc_usd</a>() -> None</code>

# Oauth2

Methods:

- <code title="get /v1/oauth2/authorize">client.oauth2.<a href="./src/zbdpay/resources/oauth2.py">create_authorization_url</a>() -> None</code>
- <code title="post /v1/oauth2/token">client.oauth2.<a href="./src/zbdpay/resources/oauth2.py">refresh_token</a>() -> None</code>
- <code title="get /v1/oauth2/user">client.oauth2.<a href="./src/zbdpay/resources/oauth2.py">retrieve_user_data</a>() -> None</code>
- <code title="get /v1/oauth2/wallet">client.oauth2.<a href="./src/zbdpay/resources/oauth2.py">retrieve_wallet_data</a>() -> None</code>

# KeysendPayments

Methods:

- <code title="post /v0/keysend-payment">client.keysend_payments.<a href="./src/zbdpay/resources/keysend_payments.py">send</a>(\*\*<a href="src/zbdpay/types/keysend_payment_send_params.py">params</a>) -> None</code>

# EmailPayments

Methods:

- <code title="post /v0/email/send-payment">client.email_payments.<a href="./src/zbdpay/resources/email_payments.py">send</a>(\*\*<a href="src/zbdpay/types/email_payment_send_params.py">params</a>) -> None</code>
