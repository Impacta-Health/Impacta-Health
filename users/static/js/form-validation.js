
$(document).ready(function () {
    var usernameField = $('#id_username');
    var emailField = $('#id_email');
    var passwordField1 = $('#id_password1');
    var passwordField2 = $('#id_password2');
    var firstNameField = $('#id_first_name');
    var lastNameField = $('#id_last_name');

    function showFeedback(element, message) {
        element.text(message).fadeIn();
    }

    function hideFeedback(element) {
        element.fadeOut();
    }

    function handleFieldInput(field, feedbackElement, validationUrl, successCallback) {
        field.on('input', _.debounce(function () {
        var value = field.val();

        if (value.trim() !== '') {
            $.ajax({
            url: validationUrl,
            type: 'POST',
            data: { [field.attr('name')]: value },
            success: function (response) {
                if (successCallback) {
                successCallback(response, feedbackElement);
                }
            },
            error: function (xhr, textStatus, errorThrown) {
                if (xhr.status === 400) {
                showFeedback(feedbackElement, xhr.responseJSON[field.attr('name')][0]);
                } else {
                // Trate outros erros aqui, se necessário
                }
            }
            });
        } else {
            hideFeedback(feedbackElement);
        }
        }, 1000)); // Atraso de 1 segundo
    }

    // Função para adicionar marcação vermelha e mensagem de erro
    function markFieldAsError(field) {
        field.addClass('error-field');
        field.next('.error-message').text('Este campo é obrigatório.').fadeIn();
    }

    // Função para remover a marcação vermelha e a mensagem de erro
    function clearFieldError(field) {
        field.removeClass('error-field');
        field.next('.error-message').text('').fadeOut();
    }

    // Lidar com a entrada do campo de nome de usuário
    handleFieldInput(usernameField, $('.username-feedback'), '{% url "users:signup-verify" %}', function (response, feedbackElement) {
        if (response.username_exists) {
        showFeedback(feedbackElement, 'Username already exists.');
        } else {
        hideFeedback(feedbackElement);
        }

        if (response.username_error) {
        showFeedback(feedbackElement, response.username_error);
        }
    });

    // Lidar com a entrada do campo de e-mail
    handleFieldInput(emailField, $('.email-feedback'), '{% url "users:signup-verify" %}', function (response, feedbackElement) {
        if (response.email_exists) {
        showFeedback(feedbackElement, 'Email already exists.');
        } else {
        hideFeedback(feedbackElement);
        }

        if (response.email_error) {
        showFeedback(feedbackElement, response.email_error);
        }
    });

    // Lidar com a entrada do campo de senha
    passwordField2.on('input', function () {
        var password1 = passwordField1.val();
        var password2 = passwordField2.val();

        if (password2.trim() !== '') {
        if (password1 !== password2) {
            showFeedback($('.password-feedback'), 'Passwords do not match.');
        } else {
            hideFeedback($('.password-feedback'));
        }
        } else {
        hideFeedback($('.password-feedback'));
        markFieldAsError(passwordField2); // Marque o campo de senha como erro se estiver vazio
        shakeFieldWithError(passwordField2); // Adicione estremecimento ao campo de senha
        }
    });

    var form = $('form'); // Selecione o formulário apropriado por ID ou classe

    // Manipulador de envio do formulário
    form.on('submit', function (e) {
        var isValid = true;

        // Função para adicionar estremecimento a um campo com erro
        function shakeFieldWithError(field) {
        field.addClass('error-field error-shake');
        }

        // Verifique os campos com erro e aplique as classes e mensagens de erro
        form.find('.invalid-feedback').each(function () {
        var feedbackElement = $(this);
        var field = feedbackElement.siblings('input');
        if (feedbackElement.is(':visible')) {
            isValid = false;
            markFieldAsError(field); // Marque o campo com erro
            shakeFieldWithError(field); // Adicione estremecimento ao campo com erro
        } else {
            clearFieldError(field); // Remova a marcação de erro e estremecimento do campo sem erro
        }
        });

        // Verifique se há campos vazios e destaque-os com vermelho
        form.find('input').each(function () {
        var inputField = $(this);
        if (inputField.val().trim() === '') {
            isValid = false;
            markFieldAsError(inputField); // Marque o campo com erro
            shakeFieldWithError(inputField); // Adicione estremecimento ao campo com erro
        } else {
            clearFieldError(inputField); // Remova a marcação de erro e estremecimento do campo sem erro
        }
        });

        // Verificar se first_name e last_name estão preenchidos
        if (firstNameField.val().trim() === '') {
        isValid = false;
        markFieldAsError(firstNameField); // Marque o campo com erro
        shakeFieldWithError(firstNameField); // Adicione estremecimento ao campo com erro
        } else {
        clearFieldError(firstNameField); // Remova a marcação de erro e estremecimento do campo sem erro
        }

        if (lastNameField.val().trim() === '') {
        isValid = false;
        markFieldAsError(lastNameField); // Marque o campo com erro
        shakeFieldWithError(lastNameField); // Adicione estremecimento ao campo com erro
        } else {
        clearFieldError(lastNameField); // Remova a marcação de erro e estremecimento do campo sem erro
        }

        if (!isValid) {
        e.preventDefault(); // Impede o envio padrão do formulário

        // O formulário não é válido, adicione uma animação de estremecimento aos campos com erro
        setTimeout(function () {
            form.find('.error-shake').removeClass('error-shake');
        }, 1000); // Remova a classe de estremecimento após 1 segundo (ajuste conforme necessário)
        }
    });
});
