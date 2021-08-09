from fastapi import FastAPI

from .autowire import Autowirer
from .controllers import controller1, controller2, controller3
from .domain import Bar, Foo
from .services import FooPrinter

aw = Autowirer()


@aw.register
def int_factory() -> int:
    return 10


@aw.register
@aw.autowire
def float_factory(val: int) -> float:
    return 10.0 * val


aw.register(aw.autowire(Foo))
aw.register(aw.autowire(FooPrinter))


@aw.register
@aw.autowire
def bar_factory(foo: Foo) -> Bar:
    return Bar(foo.value1 + 1, foo.value2 + 2)


app = FastAPI()
app.add_api_route("/1", aw.autowire(controller1))
app.add_api_route("/2", aw.autowire(controller2))
app.add_api_route("/3", aw.autowire(controller3))
