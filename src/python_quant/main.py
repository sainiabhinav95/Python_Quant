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
    arg_parser.add_argument(
        "--port",
        type=int,
        default=8060,
        help="Port to run the app on (default: 8060)",
    )
    args = arg_parser.parse_args()

    from python_quant.app.app import start_app
    start_app(debug=args.debug, port=args.port)

if __name__ == "__main__":
    main()
