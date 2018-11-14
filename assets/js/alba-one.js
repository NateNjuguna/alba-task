(function($) {
    $(document).ready(function() {
        $('input#date').datepicker({
            autoHide: true,
            format: 'dd-mm-yyyy'
        });
        $('input#phoneNumber').blur(function(e) {
            var element = $(e.target);
            if ($.trim(element.val())) {
                if (!element.intlTelInput('isValidNumber')) {
                    e.target.setCustomValidity('The phone number you entered is invalid');
                    element.parents('div.field:first').addClass('error');
                }else{
                    e.target.setCustomValidity('');
                    element.parents('div.field:first').removeClass('error');
                }
            }
        }).intlTelInput({
            autoPlaceholder: 'aggressive',
            formatOnDisplay: true,
            hiddenInput: 'phone_number',
            placeholderNumberType: "FIXED_LINE_OR_MOBILE",
            utilsScript: '/assets/js/intl-tel-input.utils.js'
        });
    });
})(window.jQuery);
