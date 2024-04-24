from rest_framework_simplejwt.tokens import RefreshToken


def createToken(user):
    refresh_token = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh_token),
        'access': str(refresh_token.access_token)
    }
