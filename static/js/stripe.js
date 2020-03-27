// The Javascript code that is required by Stripe´s API, 
// provideded from this page https://stripe.com/docs/payments/accept-a-payment-charges#web

// The data will be transferred to Stripe when the payment form is submitted.
$(function () {
    $("#payment-form").submit(function () {
        var form = this;
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };

        Stripe.createToken(card, function (status, response) {
            if (status === 200) {
                $("#credit-card-errors").hide();
                $("#id_stripe_id").val(response.id);

                // Prevents the credit card details from being submitted
                // to the server, and visible to the user. It´s only submitted to Stripe´s server.
                $("#id_credit_card_number").removeAttr('name');
                $("#id_cvv").removeAttr('name');
                $("#id_expiry_month").removeAttr('name');
                $("#id_expiry_year").removeAttr('name');

                form.submit();

                // if a 200 code or another error does not occur, 
                // this enables to post a stripe error message or a card error.
            } else {
                $("#stripe-error-message").text(response.error.message);
                $("#credit-card-errors").show();
                $("#validate_card_btn").attr("disabled", false);
            }
        });
        return false;
    });
});