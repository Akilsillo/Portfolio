import reflex as rx
from .styles.styles import STYLESHEETS ,BASE_STYLE, MAX_WIDTH, EmSize, Size
from .views.header import header
from .views.about import about
from .views.tech_stack import tech_stack
from .views.projects import projects
from .views.footer import footer



def index()-> rx.Component:
    return rx.center(
        rx.vstack(
            header(),
            about(),
            rx.divider(),
            tech_stack(),
            projects(),
            rx.divider(),
            footer(),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%",
        ),
    )

app = rx.App(

    style=BASE_STYLE,
    theme = rx.theme(
        radius="full"
    )
)

app.add_page(
    index,
    title="Andrés Vargas",
)