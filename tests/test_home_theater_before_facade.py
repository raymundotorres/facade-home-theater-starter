from home_theater.amplifier import Amplifier
from home_theater.home_theater_client import HomeTheaterClient
from home_theater.projector import Projector
from home_theater.streaming_player import StreamingPlayer
from home_theater.theater_lights import TheaterLights


def test_client_can_coordinate_the_subsystem_directly():
    client = HomeTheaterClient(Amplifier(), Projector(), TheaterLights(), StreamingPlayer())
    steps = client.watch_movie("Design Patterns")
    assert steps[0] == "lights:dim:10"
    assert steps[-1] == "player:play:Design Patterns"
    assert len(steps) == 7
