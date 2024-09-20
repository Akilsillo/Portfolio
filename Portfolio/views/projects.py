import reflex as rx
from Portfolio.styles.styles import Size
from Portfolio.components.project import project

def projects()-> rx.Component:
    return rx.vstack(
        rx.heading("Proyectos"),
        rx.vstack(
            project(),
            project(),
            width="100%",
            spacing=Size.DEFAULT.value
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )