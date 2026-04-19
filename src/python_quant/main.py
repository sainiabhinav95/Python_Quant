from python_quant.utils.text import print_intro_message
import argparse



def main():
    print_intro_message()
    arg_parser = argparse.ArgumentParser(description="Run the Python Quant app")
    arg_parser.add_argument(
        "--debug",
        action="store_true",
        help="Run the app in debug mode (default: False)",
    )
    args = arg_parser.parse_args()

    from python_quant.app.app import start_app
    start_app(debug=args.debug)

if __name__ == "__main__":
    main()
