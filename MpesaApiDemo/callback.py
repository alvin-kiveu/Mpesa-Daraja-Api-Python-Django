import json
from django.http import JsonResponse

def process_stk_callback(request):
    stk_callback_response = json.loads(request.body)
    log_file = "Mpesastkresponse.json"
    with open(log_file, "a") as log:
        json.dump(stk_callback_response, log)
    
    merchant_request_id = stk_callback_response['Body']['stkCallback']['MerchantRequestID']
    checkout_request_id = stk_callback_response['Body']['stkCallback']['CheckoutRequestID']
    result_code = stk_callback_response['Body']['stkCallback']['ResultCode']
    result_desc = stk_callback_response['Body']['stkCallback']['ResultDesc']
    amount = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
    transaction_id = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
    user_phone_number = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']
    
    if result_code == 0:
      #  store the transaction details in the database
        