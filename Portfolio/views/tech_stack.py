import reflex as rx
from Portfolio.styles.styles import Size

def tech_stack() -> rx.Component:
    return rx.vstack(
        rx.heading("Teconologías"),
        rx.flex(
            rx.badge(
                rx.icon("braces"),
                "Python",
                variant="outline",
                color_scheme="sky",
                radius="full",
                ),
            rx.badge(
                rx.icon("brackets"),
                "JavaScript",
                variant="outline",
                color_scheme="yellow",
                radius="full",
                ),
            spacing=Size.SMALL.value,
            width="100%",
        ),
        width="100%"
    )