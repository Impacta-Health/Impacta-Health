from django.contrib.auth.password_validation import (
    CommonPasswordValidator,
    MinimumLengthValidator,
    NumericPasswordValidator,
    UserAttributeSimilarityValidator,
)
from django.core.exceptions import ValidationError



class CustomUserValidationError(ValidationError):
    def __init__(self, error_list, code=None, message=None):
        super().__init__(error_list, code=code)
        self.message = message


class CustomPasswordValidator:
    MINIMUM_DEFAULT_PASSWORD_LENGTH = 8

    @staticmethod
    def __default_password_validators():
        return [
            UserAttributeSimilarityValidator(),
            CommonPasswordValidator(),
            NumericPasswordValidator(),
            MinimumLengthValidator(CustomPasswordValidator.MINIMUM_DEFAULT_PASSWORD_LENGTH),
        ]

    @staticmethod
    def get_help_text():
        pass

    def validate(self, password):
        errors = []
        for validator in self.__default_password_validators():
            try:
                validator.validate(password)
            except ValidationError as error:
                errors.extend(error.error_list)
        if errors:
            raise CustomUserValidationError(
                error_list=errors,
                code="password_validation_error",
            )
