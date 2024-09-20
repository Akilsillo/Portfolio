import reflex as rx
from .icon_button import icon_button, email_icon_button
from Portfolio.styles.styles import Size

def media() -> rx.Component:
    return rx.flex(
        email_icon_button(
                url="mailto:avargasgut@gmail.com",
                icon="mail",
                variant="solid",
                text="avargasgut@gmail.com"),
        icon_button(
                icon="file-text",
                variant="outline"),
        icon_button(
                url="https://github.com/Akilsillo",
                icon="github",
                variant="outline"),
        icon_button(
                url="https://www.linkedin.com/in/andres-vargas-618027282/",
                icon="linkedin",
                variant="outline"),
        spacing= Size.SMALL.value
    )
    