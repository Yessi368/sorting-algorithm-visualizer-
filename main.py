from controller import Controller
from renderer import Renderer


def main():
    controller = Controller()
    renderer = Renderer(controller)
    renderer.run()


if __name__ == "__main__":
    main()
