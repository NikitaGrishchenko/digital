from ...services import CaptchaEncodeService


def captcha_is_valid(uuid, user_answer):
    return CaptchaEncodeService.execute(
        {
            "uuid": uuid,
            "user_answer": user_answer,
        }
    )
