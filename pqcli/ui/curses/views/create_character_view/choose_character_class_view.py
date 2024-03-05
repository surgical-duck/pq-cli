import functools
import typing as T

from pqcli import random
from pqcli.config import CLASSES, Class
from pqcli.ui.curses.util import KEYS_CANCEL, KEYS_RANDOM, Choice
from pqcli.ui.curses.views.menu_view import MenuView


class ChooseCharacterClassView(MenuView):
    def __init__(
        self, screen: T.Any, class_: T.Optional[Class] = None
    ) -> None:
        super().__init__(
            screen,
            "Choose character class",
            CLASSES.index(class_) if class_ is not None else 0,
        )

        for y, class_ in enumerate(CLASSES, 1):
            key: T.Optional[str] = str(y % 10) if y <= 10 else None
            self._choices.append(
                Choice(
                    keys=[ord(key)] if key is not None else [],
                    desc=f"[{key or '-'}] {class_.name}",
                    callback=functools.partial(self.on_confirm, class_),
                )
            )

        self._choices.append(
            Choice(
                keys=list(KEYS_RANDOM),
                desc="[R] Random",
                callback=functools.partial(self.on_confirm, class_=random.choice(CLASSES)),
            )
        )

        self._choices.append(
            Choice(
                keys=list(KEYS_CANCEL),
                desc="[Q] Cancel",
                callback=self.on_cancel,
            )
        )
