import os
import argparse
import runpy

from .patch import patch_numpy_save, patch_torch_save


def run_script(script_path):
    """Execute the given script using runpy instead of exec."""
    script_path = os.path.abspath(script_path)  # Ensure script_path is absolute
    runpy.run_path(script_path, run_name="__main__")


def main():
    """Automatically create a dotfile for numpy and/or torch save calls."""
    parser = argparse.ArgumentParser(
        description="Automatically create a dotfile for numpy and/or torch save calls."
    )
    parser.add_argument("script", help="The Python script to run")
    parser.add_argument("--npsave", action="store_true", help="Patch numpy.save")
    parser.add_argument("--torchsave", action="store_true", help="Patch torch.save")

    args = parser.parse_args()

    script_path = os.path.abspath(args.script)

    if args.npsave:
        patch_numpy_save(script_path)
    if args.torchsave:
        patch_torch_save(script_path)

    run_script(script_path)


if __name__ == "__main__":
    main()
