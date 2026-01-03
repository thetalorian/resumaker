from airium import Airium
import lipsum
import yaml
import argparse
from models import *
from htmlresume import HTMLResume

def read_file(input: str):
    with open(input) as file:
        data = yaml.safe_load(file)
        return data


def main():
    """Generate HTML Resume
    """
    parser = argparse.ArgumentParser(description="A script that generates a resume from yaml data.")
    # Add a required positional argument
    parser.add_argument("file", type=str, help="YAML formatted data file.")
    parser.add_argument('-o', '--output', type=str, default="resume.html", help="The output filename (default: %(default)s)")
    args = parser.parse_args()

    data = read_file(args.file)
    resume = Resume.model_validate(data)

    html = HTMLResume(resume)
    with open(args.output, 'w') as file:
        file.write(str(html))


if __name__ == "__main__":
    main()