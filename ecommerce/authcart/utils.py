from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
# from django.utils.encoding import force_text
# from django.utils.encoding import force_str
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self,user,timestamp):
        return (six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_active))
generate_token=TokenGenerator()