import reflex as rx
from Portfolio.components.media import media

def footer()-> rx.Component:
    return rx.vstack(
        rx.text("Andrés Vargas"),
        media(),
        width = "100%"
    )