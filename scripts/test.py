import subprocess


def main() -> None:
    subprocess.run("coverage run --source=\".\" manage.py test")


if __name__ == "__main__":
    main()
